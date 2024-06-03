!/bin/bash

# Define the repository URL
REPO_URL="git@github.com:dogasiyli/ubuntucommands.git"

# Define the directory where you want to clone the repo
TARGET_DIR="$HOME/GitHubUbuntU/ubuntucommands"

# Clone the repository if not already cloned
if [ ! -d "$TARGET_DIR" ]; then
  git clone $REPO_URL $TARGET_DIR
else
  # Fetch and pull the latest changes if the directory exists
  cd $TARGET_DIR
  git fetch
  git pull
fi

# Navigate to the target directory
cd $TARGET_DIR

# Run the Python script with the desired command
python3 $TARGET_DIR/run_commands.py $1
