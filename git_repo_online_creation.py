from math import e
import requests
import os
import subprocess

def create_github_repository(repo_name, username, token, api_url, public=True, description=None):
    """Creates a new repository on GitHub."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = {
        "name": repo_name,
        "public": public,
        "description": description,
    }

    response = requests.post(api_url, headers=headers, json=data)
    repo_info = response.json()
    ssh_url = repo_info.get("ssh_url")
    html_url = repo_info.get("html_url")
    print(f"Successfully created repository: {repo_name}")
    print(f"  SSH URL: {ssh_url}")
    print(f"  HTTPS URL: {html_url}")