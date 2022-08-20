import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


file = "ingredients.txt"
with open(file, "r+") as f:
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    fileString = f.read()
    
    fileString = ''.join(filter(whitelist.__contains__, fileString))
    fileString = fileString.lower()
    f.write(fileString)
