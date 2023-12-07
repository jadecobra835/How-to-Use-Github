# He starts by making a new branch
"""
git checkout -b stash-demo

# Make some changes

git checkout main

git status
"""

# You will see that if you did this you brought the branch changes with you to the main branch.
# This is not good. To undo that do this.

"""
git checkout .

git status

git checkout stash-demo

git status
"""

# What this does is it deletes the changes you made, which is still not great.
# With only a few small changes making a commit message (which is a benchmark in time)
# might not be what you want to do. That's where git stash comes in.

"""
git stash
"""
# This will stash the changes you make and you can then freely switch branches.
# When you return to the branch you need to run these commands to get your code back.
# First though, this is how you can see a list of your stashes.
"""
git stash list

git stash show
^(This will show the changes that you made that are stashed.)
"""

# Okay, here's how to get your stash back.

"""
git stash apply
"""

# From here, add and commit the changes. Now do the (git stash list) command again.
# You will notice that your stash is still there, which can create confusion if there are multiple stashes.
# To get rid of a stash once you are done with it type this.
"""
git stash clear
"""