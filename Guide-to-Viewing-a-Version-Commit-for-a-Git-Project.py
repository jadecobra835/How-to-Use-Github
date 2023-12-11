# In this guide we are going to see how we can look at our entire code project in a previous version.
# To do so run the following code:
"""
git checkout 93fa9c45e4349b01ef4ccf4cb25698cd5edb2106 -b investigation
^(The first part is basically the same as what we did preveously, but this time we are pulling in everything, now just one file.
  then we are storing it in a bracn (-b) because usually this is used when you are trying to find what file you are wanting to replace.)
"""
# You can then look at the files and then switch back to the main branch. Just to prove that you haven't changed anything.
# Usually you don't want to wipe away all of the previous changes but simply want to find all the changes you want to make and then revert those specific files.
# So once you have done that you can simply delete the branch.
"""
git branch -d investigation
"""