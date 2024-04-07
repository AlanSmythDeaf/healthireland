# [HEALTHIRELAND](https://healthireland-1ca000fe5f73.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AlanSmythDeaf/healthireland)](https://github.com/AlanSmythDeaf/healthireland/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/AlanSmythDeaf/healthireland)](https://github.com/AlanSmythDeaf/healthireland/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/AlanSmythDeaf/healthireland)](https://github.com/AlanSmythDeaf/healthireland)


![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://healthireland-1ca000fe5f73.herokuapp.com)

## UX
There were many options to chose from project, what I wanted was to have user to create an input and get an answers. So I decided to create an Heath Ireland where a user can check their health

## User Stories

### New Site Users

- As a new site user, I would like to see where I want to go, so that I can find it.
- As a new site user, I would like to easily understand where I made a mistake, so that I can rectify my issue.

### Returning Site Users

- As a returning site user, I would like to know where to go.
- ?????

## Features

### Existing Features

- **Main Menu**

    - This is the first page when it's loaded, with the word health ireland and present the user with four options to chose from.

![screenshot](documentation/features/feature01.png)

- **Body Mass Index BMI**

    - BMI page, 
    - It ask the user to enter height in meters, if the user enter letter it gives an invalid input also the height needs to be between 1.00 to 2.44
    - Ask the user to to enter weight in KG, needs to be 35 to 199, if the user enter a letter or number that not between 35 to 199 it gives an invalid input
    - Once the two input are correct it will display the answer what weight catergory
    

![screenshot](documentation/features/feature02.png)

- **Heart Rate**

    - Heart Rate page  
    - It ask the user to enter your age
    - if the user enter a letter or number that not between 1 to 100 it gives an invalid output
    

![screenshot](documentation/features/feature03.png)

- **Waist to Hip Ratio**

    - Waist to Hip page  
    - It ask the user to enter gender male or female
    - if the user enter a letter or number that is not male or female it gives an invalid output

![screenshot](documentation/features/feature03.png)

- **How it works**

    - How it works page
    - This explains how the Health Ireland page works, giving examples on each section

![screenshot](documentation/features/feature03.png)

### Future Features

- Random Facts
    - I would like to add random facts section.
- Other Health tools
    - Checking Blood Pressue & Pregnacy due date & Exercise guidelines

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.

- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.

- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating flowchart.
- [![ChatGPT]()](https://copilot.microsoft.com/) used to help debug, troubleshoot, and explain things.

## Data Model

### Flowchart

To follow best practice, a flowchart was created using the
[Canva](https://www.canva.com/) so this give me an idea, how and what should happens when writing a code

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png) - HAVE THIS

### Functions

The primary functions used on this application are:

- `main_menu()`
    - Display the main menu options for the user.
- `bmi()`
    - Calculates BMI based on user input for weight and height.
- `heart_ratio()`
    - Displays section called Heart Ratio.
- `waist_hip()`
    - Displays section call waist to hip ratio.
- `how_it_work()`
    - Displays section how it works.
- `clear_tml()`
    -  Clears the terminal when called.
- `main()`
    - Run all program functions.

### Imports
I've used the following Python packages and/or external imported packages.
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://healthireland-1ca000fe5f73.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
    - `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
    - `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AlanSmythDeaf/healthireland) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/AlanSmythDeaf/healthireland.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AlanSmythDeaf/healthireland)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/AlanSmythDeaf/healthireland)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

At the end 

## Credits

### Content

| Source | Notes |  
| --- | --- | 
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | tool to help generate the Markdown files |
| [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/) | how to wrtie better git commit |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | Colormama for the text |
| [Code-Institute](https://codeinstitute.net/ie/) | Understanding???? |
| [Doctor Diary](https://github.com/Tony118g/doctor-diary/tree/main) | Love Sandwiches |
| [NHS](https://www.nhs.uk/health-assessment-tools/) | Tools for |

### Media

Use no media for this project

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.

- I would like to thank the [Code Institute](https://codeinstitute.net) for the weekly meet up for guidance, advice and hsupport.

- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for many differents ideas that have given me for the project and knowing that I am not alone for many different reason

- I would also like to thanks the Deaf people in the slack community


