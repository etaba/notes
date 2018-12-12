# Git
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

## gitting started

## pushing/pulling

## stashing
When you have stuff in working directory that you dont want to commit but you need to switch branches 
	`git stash`
List what youve stashed
	`git stash list`
Now in the new branch if you want to apply the stashed work
	`git stash apply` -applies most recent stash, add stash name for more specificity
					  -include `--index` option reapply staged changes. Otherwise all applied changes will be unstaged
Discard a stash
	`git stash drop`


## merging

## branching
Create a new branch
	`git checkout -b <branch>`
	Note: this is shorthand for `git branch <branch>; git checkout <branch>`

See all branches
	`git branch -a`

To checkout a remote branch
	`git checkout <branch>`

Merging branch
	`git checkout <branch_your_merging_into>` i.e. 'development'
	`git merge <branch_your_merging>` i.e. 'hotfix123'
	now delete branch
	`git branch -d <branch_your_merging>`

Deleting branch
	`git push -d <remoteName> <branch>` - delete remote branch
	`git branch -d <branch>` - once remote branch deleted, delete local copy
	use `-D` to force delete branches that haven't been merged

## miscellaneous

`git update-index --assume-unchanged file` - removes file from git index so that changes made on it wont be committed to the repo. Useful for config files and files containing sensitive information. use `git update-index --no-assume-unchanged file` to revert.