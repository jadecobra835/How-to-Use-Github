# Go to one of your files and keep it open.
# Now we are going to duplicate it for demonstration purposes:
"""
cp my_file.py demo_file.py
^(cp = copy. From there you have the name of the file you're copying. Then the name of the new duplicate)
"""
# Now go into the git log.
# Some helpful git log keys:
"""
j or down-arrow = go down in the log
k or up-arrow = go up in the log
q = quit/exit the log
shift g = Go to the very bottom of the log.
"""
# Now go to a really old commit and get the commit id.
# Now run the following command:
"""
git checkout super-long-git-commit-id-that-lasts-fore -- my_file.py
^(Note that if the file name that you put at the end of the command is nested in other directories it won't work unless you give the full path.)
"""
# Now type git status: It should say that you have modified the my_file.py
# Now it says that you have changed it even though you haven't personally done anything. 
# This is nice because you can choose wether or not to commit it or you can just pull down the previous code.

# Now we can delete the demo file:
"""
rm demo_file.py
"""
# Now go through the standard process and commit your change to the remote repository.
# NOTE: Your git -m should look something like this.
"""
git commit -m "Reverted back to 93fa9c45e4349b01ef4ccf4cb25698cd5edb2106 for my_file.py"
"""