# First go make some changes to your files.
# To see exacly what has been altered you can use the following command
"""
git diff my_file.py
^(The name at the end of the command makes it so you will only see one change, but it's not necessary.
  You can choose to look at all of the changes simply by leaving that off.)
"""
# If you see minus signs it means you have removed those lines of code from the file.

# Now if you wan't to revert to the previous commit (don't like the new changes) use the following code.
"""
git checkout .
"""
# TADA!

# Now create a new file.
# Now check the git status

# You will see that it is an unttracked file. Now try to revert it.
"""
git checkout .
"""

# Now check the status: You will notice that nothing happened.
# This happens because git will only change files that it is tracking.
# Now, if you just want to get rid of the file you can do this.
"""
rm my_bad_file.py
"""