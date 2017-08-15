import os

for old in os.listdir('img'):
    os.rename(os.path.join('img', old),
        os.path.join('img', bytes(old,'iso-8859-1').decode('utf-8')))