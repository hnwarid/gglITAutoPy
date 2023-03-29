#/usr/bin/bash

# Install Git
sudo apt update
sudo apt install git
git --version

# Initialize a new repository
mkdir my-git-repo
cd my-git-repo
git init

# Configure Git
git config --global "HN"
git config --global "hnxxxxxx@gmail.com"

# Git Operations
nano README
# add this string: "This is my first repository."
git status
git add README
git commit
# add comment: "This is my first commit!"
nano README
# add this string on new line:
# "A repository is a location where all the files of a particular project are stored"
git status
git diff README
git add README
git status
git commit -m "This is my second commit."
git log
