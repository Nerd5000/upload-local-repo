from os import remove, chmod
from subprocess import call

repoPath=input('Enter Repo Path : ')
gitCommitComment = input('Enter Commit Comment : ')
gitURL = input('Enter Repo URL : ')
gitUserName = input('Enter your Name : ')
gitUserEmail = input('Enter your Email : ')
gitBranchName = input('Enter Branch Name : ')

gitFile = open('{0}/git.sh'.format(repoPath), 'w')
gitFile.write(
    """
#!/bin/sh
git config user.name "{0}"
git config user.email "{1}"
git init
git add .
git commit -m "{2}"
git remote add origin {3}
git push origin -f {4}
""".format(gitUserName, gitUserEmail, gitCommitComment, gitURL, gitBranchName))
gitFile.close()

chmod('{0}/git.sh'.format(repoPath), 0o775)
call('{0}/git.sh'.format(repoPath), shell=True)
remove('{0}/git.sh'.format(repoPath))