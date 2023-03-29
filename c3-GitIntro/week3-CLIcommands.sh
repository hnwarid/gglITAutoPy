#/usr/bin/bash

# Introduction to Github

# Create a git repository
# Open Github, login, click the + sign in the top-right corner of the page
# and then click on New repository
# git created on https://github.com/hnwarid/GitIntro

# Git operations
# change directory to local disk at directory_name
# cd directory_name
git clone https://github.com/hnwarid/GitIntro.git
# or use a one-line command
# git clone https://github.com/hnwarid/GitIntro.git directory_name


# Configure Git
git config --global user.name "HN"
git config --global user.email "hnxxxxxx@gmail.com"

# Edit the file and add it to the repository
nano README.md
# Add following text:
# I am editing the README file. Adding some more details about the project description."
# can be done in one line:
echo "I am editing the README file. Adding some more details about the project description." >> README.md
git add README.md
git commit
# commit message: "I am editing the README file.
git push origin main

# Create a new file and commit it to the repository
nano example.py
# add the script:
# def git_operation():
#     print("I am editing example.py file to the remote repository.")
# git_operation()
git add example.py
git commit

# Add an empty file to the repository through web UI
# go to the Github repo > click Add file > Create new file
# leave the file empty > enter commit message > click Commit new file button
# back to terminal
git push origin main
# expected error
git pull origin main
git push origin main
