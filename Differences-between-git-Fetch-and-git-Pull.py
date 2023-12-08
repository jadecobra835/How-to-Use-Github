# Git Pull brings down all the changed code from whatever branch you are wanting to pull down.
# Example
# Make some changes to the online repository and commit them.
# Then do the following commands in the terminal
"""
git checkout main
git pull
"""
# You will see that the changes are automaticly applied.

# Now go make some changes to your local files and the online files.
# Commit the changes but don't push them up.
# Now run these commands:
"""
git fetch
"""
# git fetch will bring back the changes, but look at this.
"""
git status
"""
# Notice that it says that they have diverged.
# Now go check out the file that you updated online.
# You will notice that it hasn't changed. This is because Fetch doesn't automaticaly update your files.
# Now, how do we merge the fetch command to our local system?
# This is how:
"""
git merge origin/main
"""
# This will automaticaly populate the changes made on both sides of the system to each.
# It may or may not ask for a commit message. If it does give an overview of what merge it was and the feature that you added that you are merging.
# Now the last thing you have to do is a git push command.

# Git pull is basically just git fetch and git merge in once command.
# Git fech is usually considered the best practice because it allows you to control each step in the process.
# This is really important when you are having merge conflicts.
# However, if you know there won't be any merge conflicts then git pull is great.