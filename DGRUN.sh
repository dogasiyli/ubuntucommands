#!/bin/bash

CALLING_DIR=$(pwd)

# Define the repository URL
REPO_URL="git@github.com:dogasiyli/ubuntucommands.git"

# Define the directory where you want to clone the repo
GIT_FOLD_BASE="$HOME/GitHubUbuntU"
TARGET_DIR="$GIT_FOLD_BASE/ubuntucommands"

# Clone the repository if not already cloned
if [ ! -d "$TARGET_DIR" ]; then
  git clone $REPO_URL $GIT_FOLD_BASE
else
  # Fetch and pull the latest changes if the directory exists
  cd $TARGET_DIR
  git fetch
  git pull
fi

# Navigate to the calling directory
cd $CALLING_DIR

# Run the Python script with the desired command
python3 $TARGET_DIR/run_commands.py $1