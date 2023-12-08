# It it considered a best practice to delete branches after you have merged them with the main and are done working with them.
# This is becuase you no longer need it and if you accidently end up in one and then do all your work, that is a really big issue.
# Lets start by making a new branch.

"""
git checkout -b branch-to-remove
    # Make some changes to the read me 
git add .
git commit -m "Updated README.md"
git push -u origin branch-to-remove
^(Remember that this will push the entire branch up to github)
"""
# Now to to github and merge the branch to your main.
# Okay, now you don't need it anymore, how do we get rid of it.
# We are going to start by deleting the local branch first.
"""
git checkout main
git branch -d branch-to-remove
"""
# Now if you type "git branch" you will see that it is gone.
# Now run a git pull so that you have the change that you made with the branch that you merged on the remote origin.
# Now we want to delete it on github. Here's how we can do that.
"""
git push origin --delete branch-to-remove
"""
# And you're done
