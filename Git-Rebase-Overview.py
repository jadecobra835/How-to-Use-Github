# If the main online repository has been updated so that your branch and local main are no longer up to date,
# You can do a pull command to update your main, and then you can use Rebase to update your branch. It looks something like this.

# Pre Rebase
"""
      A---B---C topic
     /
D---E---F---G Main
"""

# Post Rebase
"""
              A'---B'---C' topic
             /
D---E---F---G Main
"""

# As you can see this can be quite helpful. Note that doing this changes the A, B & C. (This is noted by the ' after each letter)
# The reason for this is git cannot move your a, b, and c. So it duplicates them, adds the new code, and moves them to the front of the line.

# VERY IMPORTANT RULE: You should never perform a rebase on a shared feature branch. (If you are working with team member on it no rebase. If you are alone, rebase is a-okay.)
    # Sereously though, people have been fired because they rebased a shared branch.

# The way we do a rebase is this:

"""
NOTE: He makes a new branch first.
# Making the new branch and commiting it
git checkout -b testing-rebase
git add .
git commit -m "Added new python code"

git checkout main

# REBASING
git pull name-of-remote  name-of-local-main
git rebase name-of-the-main-branch (Or whichever one has the most up to date code.)
"""

# Note that from a logging perspective whatever happened on the online git repository happened first, even if you commited other stuff without pushing it way before that.
# This can make things really tricky. This become an exponential problem if you are working on a team branch.