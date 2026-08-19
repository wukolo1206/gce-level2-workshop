import subprocess, os, shutil, stat

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

workshop_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'
deploy_dir = r'd:\備課ai\研習講義\.gh_deploy_temp'

if os.path.exists(deploy_dir):
    try:
        shutil.rmtree(deploy_dir, onexc=remove_readonly)
    except Exception:
        pass

if not os.path.exists(deploy_dir):
    print("Cloning https://github.com/wukolo1206/gce-level2-workshop.git...")
    subprocess.run(['git', 'clone', 'https://github.com/wukolo1206/gce-level2-workshop.git', deploy_dir], check=True)
else:
    print("Pulling latest from origin...")
    subprocess.run(['git', 'pull', 'origin', 'main'], cwd=deploy_dir, check=True)

# Copy all HTML files, images, docs, json from workshop_dir to deploy_dir
print("Syncing updated files from workshop directory to deploy directory...")
for item in os.listdir(workshop_dir):
    if item in ['.git', '__pycache__']:
        continue
    src_path = os.path.join(workshop_dir, item)
    dst_path = os.path.join(deploy_dir, item)
    if os.path.isdir(src_path):
        if os.path.exists(dst_path):
            try:
                shutil.rmtree(dst_path, onexc=remove_readonly)
            except Exception:
                pass
        shutil.copytree(src_path, dst_path)
    else:
        shutil.copy2(src_path, dst_path)

if not os.path.exists(os.path.join(deploy_dir, 'index.html')) and os.path.exists(os.path.join(deploy_dir, 'study_guide_app.html')):
    shutil.copy2(os.path.join(deploy_dir, 'study_guide_app.html'), os.path.join(deploy_dir, 'index.html'))

# Check status in deploy_dir
status_res = subprocess.run(['git', 'status', '--short'], cwd=deploy_dir, capture_output=True, text=True)
print("Git Status in deploy dir:\n", status_res.stdout)

# Add all and commit
subprocess.run(['git', 'add', '-A'], cwd=deploy_dir, check=True)
commit_res = subprocess.run(['git', 'commit', '-m', 'feat: add Gmail personal vs education account UI comparison'], cwd=deploy_dir, capture_output=True, text=True)
print("Commit result:\n", commit_res.stdout)

# Push to origin main
push_res = subprocess.run(['git', 'push', 'origin', 'main'], cwd=deploy_dir, capture_output=True, text=True)
print("Push output:\n", push_res.stdout, push_res.stderr)

print("Deployment to GitHub Pages complete!")
