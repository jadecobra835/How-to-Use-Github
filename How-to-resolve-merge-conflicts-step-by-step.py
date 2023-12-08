# A merge conflict is when you and another team member have made changes to the same file and typically to the very same line of code.
# This can be an incredibly frusturating process and we are goint to make it as straightforward as possible.
# We are going to be doing merge conflicts with multiple files since fixing one is relativaley straightforward.
# The real problem only comes in when working with 2 or more.

# To start make changes to the README.md and the my_file.py online.
# Now make different changes to the exact same lines of code on your local files.
# Now run this code
"""
git add .
git commit -m "Updated readme and python script"
git fetch origin
"""
# So far, no problems right?
# Now do this
"""
git status
"""
# Okay, so the main and origin have diverged, no big deal, just merge them and it'll be good!
"""
git merge origin/main
"""
# Oh, that's not good now is it.
# Now type this.
"""
git status
"""
# It will say "both modified". That doesn't mean that your two files have both been changed.
# It's telling you that the the online and the local file have both been changed in different ways.
# Okay, now open up one of the files that has a merge conflice.
# Now this might look a little scary but all it is is git doing it's job. It is giving you choices as to what to do with it.

# Your local change will be on the top. You know this because it says "HEAD". Everything between head and the "=====" is your local changes.

# Everything below the "=====" is going to be the incoming changes from the remote origin.

# In order to clean it up is remove the elements you don't want. Then delete all of the lines that were added by git (The one's with lots of symbols)"HEAD" "======" "origin/master"

# Now do the same thing with the other file.

# Now run this code

"""
git status
"""
# Now you will see that it says "both modified"
# Now do the usual commands"
"""
git add .
git commit -m "Fixed Merge Conflicts"
git push
"""