#/usr/bin/bash

# Pushing Local Commit to Github

# Forking and detect function behavior
# open Github and login
# navigate to google/it-cert-automation-practice
# click Fork in the top-right corner
git clone https://github.com/hn-warid/it-cert-automation-practice.git
cd ~/it-cert-automation-practice
git remote -v
git remote add upstream https:github.com/hnwarid/it-cert-automation-practice.git
git remote -v


# Configure Git
git config --global user.name "HN"
git config --global user.email "hnxxxxxx@gmail.com"

# Fix the script
git branch improve-username-behavior
git checkout improve-username-behavior
cd ~/it-cert-automation-practice/Course3/Lab4
ls
cat validations.py
nano validations.py
# add some lines
python3 validations.py
nano validations.py
python3 validations.py

# Commit the changes
git status
git add validations.py
git status
git commit
# enter the commit message
# "Closes: #1
# Updated validations.py python script.
# Fixed the behavior of validate_user function in validations.py"

# Push changes
git push origin improve-username-behavior
# create a pull request on the forked repo on Github
