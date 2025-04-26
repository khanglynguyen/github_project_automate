import subprocess
import os

def upload_local_repo_with_token(local_path, repo_name, remote_url):
    """Uploads an existing local Git repository to an online GitHub repository using token."""
    os.chdir(local_path)
    # git add .
    add_process = subprocess.run(
        ["git", "add", "."],
        check=True,
        capture_output=True,
        text=True
    )
    # git commit
    commit_process = subprocess.run(
    ["git", "commit", "-m", f"Initial commit for {repo_name}"],
    capture_output=True,
    text=True
    )

    # git remote add origin
    remote_process = subprocess.run(
    ["git", "remote", "add", "origin", f"{remote_url}"],
    #check=True,
    capture_output=True,
    text=True
    )

    # git branch -M main
    rename_branch_process = subprocess.run(
    ["git", "branch", "-M", "main"],
    check=True,
    capture_output=True,
    text=True
    )

    # git push
    push_process = subprocess.run(
    ["git", "push", "-u", "origin", "main"],
    #check=True,
    capture_output=True,
    text=True
    )
                
    print("Successfully pushed to 'origin' branch 'main'")
    print("----------------------------------------------")
    os.chdir("..")