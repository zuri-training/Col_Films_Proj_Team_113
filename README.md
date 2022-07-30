# VidHut

# Table of Contents

- [About the Project](#about-the-project)
  * [Feature Requests](#feature-requests)
  * [Tech Stacks](#tech-stacks)
- [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)


## About The Project

A platform that operates like a movie streaming platform but for short movies created by college students.

### Feature Requests

User: Unauthenticated
* [ ] Visit the platform to view basic information about the platform
* [ ] View and Interact with the documentation
* [ ] Register to view more details
* [ ] No access to use until registered
* [ ] Able to view all available movies

User: Authenticated
* [ ] Full access to the platform
* [ ] Allow upload of short movies (not more than 15 minutes)
* [ ] User must be a verified college student
* [ ] Watch films uploaded by others
* [ ] Comments, react and share movies
* [ ] Show usage example to users
* [ ] Allow user save data and come back to download
 

### Tech Stacks

* Python
* Django
* Bootstrap
* [Add other languages or tools used here]

## Getting Started

### Dependencies

* Python
* Text editor (e.g VSCode)
* Web browser
* Git

### Installation

_Follow the steps below to get the program working on your system locally._

1. Clone the repo
    ```sh
    git clone https://github.com/zuri-training/Col_Films_Proj_Team_113
    ```
2. Change into the directory of the cloned repo
    ```sh
    cd Col_Films_Proj_Team_113
    ```
3. Setup a virtual environment
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment
    ```sh
    . venv/bin/activate
    ```
5. Install the project requirements
    ```sh
    pip install -r requirements.txt
    ```
6. Start the local development server
    ```sh
    python manage.py runserver
    ```
7. Visit the URL via the browser
    ```sh
    http://127.0.0.1:8000/
    ```


## Contributing

Contributions are limited to team members for now! This guide walks you through how you will make contributions to the project repository.

### Fork this repository

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

### Clone the repository

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the copy to clipboard icon.

Open a terminal and run the following git command:

```sh
git clone https://github.com/<your-username>/Col_Films_Proj_Team_113
```

where `your-username` is your github username.

### Create a branch

Change to the repository directory on your computer (if you are not already there):

```sh
cd Col_Films_Proj_Team_113
```

Now create a branch using the git switch command:

```sh
git switch -c your-new-branch-name
```

replace `your-new-branch-name` with your preferred branch name.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
