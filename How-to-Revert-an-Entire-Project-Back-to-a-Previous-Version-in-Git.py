# What we are going to be talking about here is one of the most dangerous concepts in reverting
# This includes updating the remote repository with these changes.
# YOU SHOULD NOT BE DOING THIS OFTEN AT ALL. What you are doing is basically rewriting history.
# You really should avoid this as much as possible, especially when working on a team.

# Run this
"""
git log
"""
# Notice that the HEAD is pointed at the most recent commit.
# When we change where the head is pointed, all of the commits above it will just go away. Forever.

# First we are going to check it out:
"""
git checkout fa9ddcf3aa5fc949eec4e279a230efd39f4aa9da -b investigation
"""
# Now for the really scary part. The permanent reset.
"""
git checkout main
git reset --hard fa9ddcf3aa5fc949eec4e279a230efd39f4aa9da
git log
"""
# Now you can see that everything we have done is changed.
# Now type git status
# It will say that you are behind the remote and that you should use git pull to fix it.
# This next command is called a force command.
"""
git push -f origin main
"""
# Typically when you use this it is only when you are working on it alone and it is a very new (not worked on a lot) application.
# You would never want to do this when you are working on a project with a team.
