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
        subprocess.call(["/usr/bin/git", "clone", url, repo_location], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
        install(repo_location)

def check_for_updates(repo_path, name):
    subprocess.call(["/usr/bin/git", "fetch"], cwd=repo_path);
    exit_code = subprocess.call("git -C " + repo_path + " status | grep -q 'up to date'", shell=True)
    if (exit_code != 0 ):
        # Update
        subprocess.call(["/usr/bin/git", "pull"], cwd=repo_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL);
        install(repo_path)
        print("updating " + name)

def install(repo_path):
    global any_updates
    subprocess.call(["/bin/bash", repo_path + "/install.sh"], cwd=repo_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
    print("applying updates")
    subprocess.call(["/sbin/reboot"])
