#/usr/bin/bash

# Merging Branches in Git

# Explore repository
cd ~/food-scripts
cat favorite_foods.log
./food_count.py
./food_question.py


# Understanding the repository
git status
git log
# configure git
git config user.name "HN"
git config user.email "hnxxxxxx@gmail.com"

# Add a new feature
git branch improve-olutput
git checkout improve-output
nano food_count.py
# add the line below before printing for loop (or we can use echo "line" >> found_count.py):
# print("Favorite foods, from most popular to least popular")
./food_count.py
git add food_count.py
git commit -m "adding a line in the output describing the utility of food_count.py script"

# Fix the script
./food_question.py
git log
git revert [commit-ID]
./food_question.py

# Merge operation
git checkout master
git merge improve-output
./food_question.py
git status
git log
