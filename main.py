import os
from git_repo_files_check import check_repo_files
from git_repo_local_creation import initialize_git_repos
from git_repo_upload import upload_local_repo_with_token
from git_repo_online_creation import create_github_repository

GITHUB_USERNAME = 
GITHUB_TOKEN = 
BASE_URL = "https://api.github.com/user/repos"
num_projects = 0

def main():
    projects_root = "D:\Work\Python_Projects"

    for item in os.listdir(projects_root):
        #remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{item}.git"
        repo_contents_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{item}/contents"
        repo_url = f"https://github.com/{GITHUB_USERNAME}/{item}.git"
        project_path = os.path.join(projects_root, item)

        # First, initialize the Git repository locally
        if os.path.exists(os.path.join(project_path, ".git")):
            print(f"Already exist Github repository for local repository at: {project_path}")
        else:
            print(f"Warning: No local Git repository found at: {project_path}")
            print("Proceeding to create Github repository shortly...")
            initialize_git_repos(project_path, item)
        # Second, create the GitHub repository
        ssh_url = create_github_repository(item, GITHUB_USERNAME, GITHUB_TOKEN, BASE_URL, public=True, description=f"Automated creation for {item}")
        #link_local_repository(project_path, ssh_url)

        # Third, check if the repository contains files
        has_files = check_repo_files(repo_contents_url, GITHUB_USERNAME, GITHUB_TOKEN)

        if has_files:
            print(f"The repository {item} contains files.")
            print("-----------------------------------------------")
        else:
            print(f"The repository {item} does not contain any files.")
            print("Proceeding to upload local repository to Github repository shortly...")
            # Fourth, upload the local repository to GitHub
            upload_local_repo_with_token(project_path, item, repo_url)

        num_projects =+1

    print(f"Total number of projects processed: {num_projects}")


if __name__ == "__main__":
    main()

