import os
user =os.getlogin()
print("\nCurrent Logged in user:\n{}".format(user))

info=os.name
print("\nCurrnet operating system Info:\n{}".format(info))

files=os.listdir()
print("\nFiles in Current Working Directory:\n{}".format(files))