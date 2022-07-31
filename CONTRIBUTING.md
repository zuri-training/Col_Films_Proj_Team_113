# Contributing to this repository

Contributions are limited to team members for now! This guide walks you through how you will make contributions to the project repository.

## Fork this repository

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

## Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon.

Open a terminal and run the following git command:

```sh
git clone https://github.com/<your-username>/Col_Films_Proj_Team_113
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

## Make a Pull Request

Push your changes using the command `git push`:

```sh
git push origin -u add-your-branch-name
```

replacing `add-your-branch-name` with the name of the branch you created earlier.

Now go to your repository on github, you should see a `Compare & pull request` button, then click on it.

Enter the necessary information you wish to add to your pull request and click on `Create pull request` button.

Your pull request will then be merged with the main repository after being reviewed by the repo maintainer.

_This guide will constantly be updated, please create an issue if you have any difficulty following the guide._