import os
import subprocess

any_updates = False

def process_repo(url, name):
    repo_location = "/tmp/" + name
    if (os.path.isdir(repo_location)):
        # if dir exists - check update
        check_for_updates(repo_location, name)
    else:
        # clone gh repo to temp dir
        subprocess.call(["/usr/bin/git", "clone", url, repo_location]);
        install(repo_location)

def check_for_updates(repo_path, name):
    completed_process = subprocess.call(["/usr/bin/git", "diff", "remotes/origin/HEAD"], cwd=repo_path);
    if (completed_process.returncode != 0 ):
        # Update
        completed_process = subprocess.call(["/usr/bin/git", "pull"], cwd=repo_path);
        install(repo_path, name)
        print("updating " + name)

def install(repo_path):
    subprocess.call([repo_path + "/install.sh"])
    any_updates = True

# read tracking file
track = open("/usr/local/etc/track.csv", "r")
for line in track:
    tracking_data = line.split(',')
    name = tracking_data[0]
    gh_url = tracking_data[1].strip()
    process_repo(gh_url, name)

track.close()

if (any_updates):
    subprocess.call(["/sbin/reboot"])
