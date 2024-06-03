import os
import subprocess
import sys

def run_command(command, info_only):
    if info_only:
        print(command)
    else:
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with error: {e}")
            sys.exit(1)

def bash_add(info_only):
    commands = [
        "echo 'export PATH=$PATH:~/GitHubUbuntU/ubuntucommands' >> ~/.bashrc",
        "source ~/.bashrc"
    ]
    for command in commands:
        run_command(command, info_only)

def nvm_install(info_only):
    commands = [
        "sudo apt update",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash",
        "source ~/.nvm/nvm.sh",  # Ensure nvm command is available
        "nvm install node",
        "node --version"
    ]
    for command in commands:
        run_command(command, info_only)

def node_update(info_only):
    commands = [
        "source ~/.nvm/nvm.sh",  # Ensure nvm command is available
        "nvm install --lts",
        "nvm use --lts"
    ]
    for command in commands:
        run_command(command, info_only)

def ubuntu_update(info_only):
    commands = [
        "sudo apt-get update",
        "sudo apt-get upgrade"
    ]
    for command in commands:
        run_command(command, info_only)

def expo_doctor(info_only):
    commands = [
        "npx expo-doctor@latest"
    ]
    for command in commands:
        run_command(command, info_only)

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_commands.py <command> [--info|-i]")
        sys.exit(1)

    command = sys.argv[1]
    info_only = '--info' in sys.argv or '-i' in sys.argv
    
    if command == "nvm_install":
        nvm_install(info_only)
    elif command == "node_update":
        node_update(info_only)
    elif command == "ubuntu_update":
        ubuntu_update(info_only)     
    elif command == "expo_doctor":
        expo_doctor(info_only)   
    elif command == "bash_add":
        bash_add(info_only)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
