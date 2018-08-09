import datetime

print datetime.datetime.now()

rootDir = 'pdfdata'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('Found directory: %s' % dirName)
    for fname in fileList:
    	prefix = os.path.join(subdirList, fname)
        print('\t%s' % prefix)


fileSet = set()
for dir_, _, files in os.walk(rootDir):
    for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        relFile = os.path.join(relDir, fileName)
        fileSet.add(relFile)

print(fileSet)


================
cz@Y900:~$ ssh-keygen -t rsa -b 4096 -C clzsanjose@gamil.com
cz@Y900:~$ vim /home/cz/.ssh/id_rsa.pub
cz@Y900:~$ eval "$(ssh-agent -s)"
Agent pid 5525
cz@Y900:~$ ssh-add ~/.ssh/id_rsa
Identity added: /home/cz/.ssh/id_rsa (/home/cz/.ssh/id_rsa)
cz@Y900:~$ vim /home/cz/.ssh/id_rsa.pub
cz@Y900:~$ echo "# homeproject" >> README.md
cz@Y900:~$ git init
Reinitialized existing Git repository in /home/cz/.git/
cz@Y900:~$ git add README.md

cz@Y900:~$ git config --global user.email clzsanjose@gmail.com
cz@Y900:~$ git config --global user.name alexucb
cz@Y900:~$ git commit -m "first commit"
[master (root-commit) c244cac] first commit
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
cz@Y900:~$ git remote add origin https://github.com/alexucb/homeproject.git
fatal: remote origin already exists.
cz@Y900:~$ git push -u origin master
Username for 'https://github.com': alexucb
Password for 'https://alexucb@github.com': 