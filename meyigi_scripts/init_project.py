import os
import subprocess
from pathlib import Path

def create_dirs():
    dirs = [
        "config",
        "data",
        "src/core",
        "src/services",
        "src/utils",
        "src/runner"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

def create_files():
    files = [
        "src/core/models.py",
        "src/core/interfaces.py",
        "config/settings.py",
        "config/.env"
    ]
    for f in files:
        Path(f).touch()
        print(f"Created file: {f}")

def setup_virtualenv():
    print("Creating virtual environment...")
    subprocess.run(["python3", "-m", "venv", ".venv"], check=True)
    print("Virtual environment created in .venv")

def setup_envrc():
    with open(".envrc", "w") as f:
        f.write("source .venv/bin/activate\n")
    subprocess.run(["direnv", "allow"])
    print("Setup .envrc and allowed direnv")

def init_project():
    create_dirs()
    create_files()
    setup_virtualenv()
    setup_envrc()
    print("✅ All done!")

if __name__ == "__main__":
    main()
