from asyncio.windows_events import NULL
import requests

def check_repo_files(repo_url, username, token):
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'


    response = requests.get(repo_url, headers=headers)

    contents = response.json()
    #print(f"Contents: {contents}") #for debugging
    
    # Check if the repository contains any files
    for item in contents:
        if "type" in item:
            if item['type'] == "file":
                return True  # Found at least one file
        elif "message" in item:
            if item[1] == "This repository is empty.":
                return False #no files found
