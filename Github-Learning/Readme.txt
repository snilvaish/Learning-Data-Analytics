Github flow

# Learning-Github
Steps to follow while working on github
## Step 1: Turn on GitHub Pages (Site Publishing)
### Activity: Enable GitHub Pages
- Click on the [Settings](https://github.com/snilvaish/Learning-Github/settings) tab in this repository
- Scroll down to the "GitHub Pages" section
- From the "Source" drop down, select main branch
## Step 2: Cloning Repository to local system & Branch creation
### Cloning:
- open repository on chrome, click on code, either copy URL & use it on CLI/Git desktop or click on button open with Github desktop directly
-  This will create a clone repo on your local system, the folder name will be same as the repository name
### Using Github desktop:
- Create a new branch, select option want it as a clone to main or some other existing branch
## Step 3: Assigning issues
- Go to the Issue tab & click on the New issue button
- write about issues & assign/notify them through the "@" or Assignee button
- Use attach file option to add files & image
- Use labels
- Use other options for filtration purposes when u have many issues
## Step 4: Make changes on the clone branch
- write different scenarios to improve existing problems
- Github tracks all changes & save the screenshot of progress
-  Incase improvement is ready for collaboration, raise pull request
## Step 4: Pull request
- As in the Github video Tractor example, it is the stage where change is proposed & reviewed/discussed by other teammates 
- Ones signed up by all teammates
- Merge pull request
## PUSH, PULL, MERGE, COMMIT, FETCH, STASH:

### PUSH: 
- Sending data from the local repository to a remote server such as Github
### PULL:
- **let you tell others about changes you've pushed to a branch in a repository on GitHub**. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.
### MERGE:
- **A request from someone to merge in code from one branch to another**. You can create a MR from Assembla by clicking on New Merge Request, which is in almost all of git sub-tabs.
### FETCH:
- Data retrieving from local repo. through software by remote server
### STASH:
- If you have saved changes that you are not ready to commit yet, you can stash the **changes** for later. When you stash changes, the changes are temporarily removed from the files and you can choose to restore or discard the changes later. You can only stash one set of changes at a time with GitHub Desktop.
### Commit:
- Git commit basically **“records changes to the local repository**


Learning Git-hub:
git init
# git --version
# git restore
# git clean
# git clean -fd [force removal of directory]
# git restore --staged file name
# git diff --staged
# git ls-files
# git add .|*.log [all log files]
# git commit -m/am
# git rm/am
# git rm --cached -f
# git rm -h [To check/get help from remove file]
# git status -s [M: Modified; A: Added]
# echo Message > bin/file.log|bin|js [Message writing in file]
# echo Mesage >> bin/file.log|bin|js [Message apending in file]
# git mv main.js file.js [Renaming & moving files]
# git config --help | -h
# git config --global core.editor "code --wait"
# git config --global -e
# git log
# git log --oneline
# git log --oneline --reverse
# git show HEAD~1 [to see latest commit]
# git ls-tree Head~1




Diff. b/w "ls", "git ls-files", "ls -a"
"ls -a" shows all files incl. hidden .git
"git ls-files" shows all files not folder & files with in folders such as _posts-0000-01-02-lajpat.md

git config --global core autocrlf true [Carriage return (/r) & line feed (/n)]

# vscode://vscode.github-authentication/did-authenticate?windowid=1&code=eb37e5b909a2e48dc65f&state=26c8504a-bd3b-4d94-8ffb-ccb28efed9b8

