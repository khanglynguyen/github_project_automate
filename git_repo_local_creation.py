import subprocess
import os

def initialize_git_repos(project_path, item):
    os.chdir(project_path)
    print(f"Initializing Git repository in: {item}")
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        print(f"  Successfully initialized Git in {item}")
    except subprocess.CalledProcessError as e:
        print(f"  Error initializing Git in {item}:")
        print(f"  Command: {e.cmd}")
        print(f"  Stdout: {e.stdout.decode()}")
        print(f"  Stderr: {e.stderr.decode()}")
    except FileNotFoundError:
        print("  Git not found. Ensure Git is installed and in your PATH.")
    finally:
        os.chdir("..")