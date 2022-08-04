# Contributing to this repository

Contributions are limited to team members for now! This guide walks you through how you will make contributions to the project repository.

## Fork this repository

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

## Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon.

Open a terminal and run the following git command:

```sh
git clone https://github.com/<your-username>/Col_Films_Proj_Team_113.git
```

where `your-username` is your github username.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```sh
cd Col_Films_Proj_Team_113
```

Now create a branch using the git switch command:

```sh
git switch -c your-new-branch-name
```

replace `your-new-branch-name` with your preferred branch name.

You can now make any additions to the repo inside this branch.

If you already have a branch to work with, you can easily switch to it with the command:

```sh
git switch branch-name
```

## Make a Pull Request

Push your changes using the command `git push`:

```sh
git push origin -u add-your-branch-name
```

replacing `add-your-branch-name` with the name of the branch you created earlier.

Now go to your repository on github, you should see a `Compare & pull request` button, then click on it.

Enter the necessary information you wish to add to your pull request and click on `Create pull request` button.

Your pull request will then be merged with the main repository after being reviewed by the repo maintainer.

## Syncing a Fork branch

It is good practice to keep your fork of the main repo that is being actively worked on by other contributors in sync.

### Setup

Before you can sync, you need to add a remote that points to the upstream repository. Do this with this command:

```sh
git remote add upstream https://github.com/zuri-training/Col_Films_Proj_Team_113.git
```

You can verify the new remote you just added with `git remote -v`

```sh
upstream https://github.com/zuri-training/Col_Films_Proj_Team_113.git (fetch)
upstream https://github.com/zuri-training/Col_Films_Proj_Team_113.git (push)
```

### Fetch

Now, fetch the branches and their respective commits from the upstream repository

```sh
git fetch upstream
```

### Merge

Then to merge the changes that has been fetched from the remote into your local branch, first checkout your fork's local default branch:

```sh
git checkout main
```

and merge the changes from the upstream default branch into your own local default branch

```sh
git merge upstream/main
```

This will update your local fork, but not on github yet. So to sync with that of github, run this command:

```sh
git push origin main
```

**Note**: Ensure you always switch to your own branch and not the `main` branch before you make any changes to be committed. **Do not** commit directly to the `main` branch.

## Pushing new changes

If you have made new changes which you want to commit to the upstream repo, follow the steps:

1. Update changes to be committed
```sh
git add .
```
2. Enter a commit message
```sh
git commit -m 'your-commit-message'
```
3. Push your commit
```sh
git push
```

Now go to your fork repo and click on `Compare & pull request` button. Enter the necessary information you wish to add to your pull request and click on `Create pull request` button and wait for your commits to be merged.

_This guide will constantly be updated, please create an issue if you have any difficulty following the guide._