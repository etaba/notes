# Git


## gitting started

## pushing/pulling

## merging

## branching

To checkout a remote branch
	`git fetch` followed by `git checkout <branch>`


## miscellaneous

`git update-index --assume-unchanged file` - removes file from git index so that changes made on it wont be committed to the repo. Useful for config files and files containing sensitive information. use `git update-index --no-assume-unchanged file` to revert.