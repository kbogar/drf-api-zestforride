# Zest For Ride API

![](/docs/welcome.png)

Zest For Ride API provides a backend database to have a complete CRUD(create, read, update, delete) functionality for users to work with data, and it was created for Zest For Ride React app.

The overall structure of the project was modeled based on Code Institutes [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough, with additional functionality added by me.

- [Deployed Zest For Ride API](https://zest-for-ride-bf40c62cc6cb.herokuapp.com/)
- [Deployed Zest For Ride Frontend webapp](https://zestforride-51d93abad130.herokuapp.com/)
- [Frontend Repository](https://github.com/kbogar/zestforride)

# Table of Contents
* [Entity Relationship Diagram](#entity-relationship-diagram)
* [Agile Methodology](#agile-methodology)
* [Technologies and Tools Used](#technologies-and-tools-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)

# Entity Relationship Diagram
Before starting the project, I conducted thorough research to define the data models needed for the application. This involved identifying entities, relationships, and creating a comprehensive list of fields and actions required for the app to function correctly. With this information, I built the necessary models, ensuring the application meets its goals.

![](/docs/erd.png)

# Agile Methodology
This project was developed using the agile methodology and version control on GitHub. Tasks were tracked and managed through Github's issue-tracking system, allowing for rapid progress and continued progress tracking.
## [User Stories Board](https://github.com/users/kbogar/projects/5)
![](/docs/user_stories.png)

## [Issues](https://github.com/kbogar/zestforride/issues)
![](/docs/issues.png)
Agile Methodology proved invaluable for my project. Breaking it into smaller tasks helped me track progress, stay on schedule, and adapt plans efficiently. The satisfaction of completing User Stories was a great motivator.

[Back to top](#table-of-contents)

# Technologies and Tools Used
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) - to create a Github repository.
- [Python](https://www.python.org/) - The functionality for the DRF backend framework.
- [Django](https://www.djangoproject.com/) - Python Web Framework.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication, registration, account management.
- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate Python code.
- [Heroku](https://www.heroku.com) - Used to deploy the app.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files and images.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal used to push changes to the GitHub repository.
- [GitPod](https://www.gitpod.io/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Cloud based git repository used.

## Libraries
The following libraries and modules are used in the project and they are located in requirements.txt file.
- asgiref==3.7.2
- cloudinary==1.33.0
- dj-database-url==0.5.0
- dj-rest-auth==2.1.9
- Django==3.2.19
- django-allauth==0.44.0
- django-cloudinary-storage==0.3.0
- django-cors-headers==4.1.0
- django-filter==23.2
- djangorestframework==3.14.0
- djangorestframework-simplejwt==4.7.2
- gunicorn==20.1.0
- oauthlib==3.2.2
- Pillow==8.2.0
- psycopg2==2.9.6
- PyJWT==2.7.0
- python3-openid==3.2.0
- pytz==2023.3
- requests-oauthlib==1.3.1
- sqlparse==0.4.4
- urllib3==1.26.16

[Back to top](#table-of-contents)

# Testing
All testing information can be found in [TESTING.md](https://github.com/kbogar/drf-api-zestforride/blob/main/TESTING.md)

# Bugs
I encountered a few errors during the coding of my project and there were fixed throughout the development.

## Solved
- I had an issue when I started to connect the frontend React app with the backend API at the Profile detail page, the events count didn't work correctly. The problem was I forgot add the events_count to API, so I solved the issue by adding it to the correct app classes.
<details
>
<summary>Click to view screenshots</summary>

![](/docs/events%20count%20issue.PNG)

![](/docs/events%20count%20issue2.png)

![](/docs/events%20count%20issue3.png)

![](/docs/events%20count%20issue4.png)

</details>

<br>

## Unsolved
At the moment there are no known bugs left to solve.

# Deployment
This project is deployed using [Heroku](https://www.heroku.com).
- Before deployment I created a env.py file in Gitpod. This file contains all the sensitive information that we must not push to Github. So I added env.py to .gitignore file.
- Modify settings.py to make django project aware of the env.py file.
- Created a requirements.txt containing the necessary libraries and modules for the app to run properly.
- Also created Procfile, this tells Heroku how to run this project.

The steps for deploying through Heroku are as follows:
- Go to Heroku website and log in.
- Go to Dashboard, click on 'New' and 'Create New App'.

<details>

<summary>Click to view screenshots</summary>

![](/docs/heroku1.png)

</details>

<br>

- Add name for your app and choose region.
- Then click 'Create app'.

<details>

<summary>Click to view screenshots</summary>

![](/docs/heroku2.png)

</details>

<br>

- Navigate to 'Deploy' tab and choose 'Connect to Github'.
- Search for your repository that you want to deploy.
- Click 'Connect'.

<details>

<summary>Click to view screenshots</summary>

![](/docs/heroku3.png)

</details>

<br>

- You can choose if you want manual or automatic deployment.
- Choose Main Branch and click 'Deploy Branch'.

<details>

<summary>Click to view screenshots</summary>

![](/docs/heroku4.png)

</details>

<br>

- When the deployment is succesfully finished, go to Settings tab.
- Click on 'Reveal Config Vars'.
- Add the necessary variables; `CLOUDINARY_URL`, `DATABASE_URL`, `PORT`, `SECRET_KEY`, `ALLOWED_HOST`, `CLIENT_ORIGIN`,...
- Click 'Open app'.

<details>

<summary>Click to view screenshots</summary>

![](/docs/heroku5.png)

</details>

<br>

## Forking the GitHub Repository
Forking allows you to view and edit the code without affecting the original repository.
- Navigate to GitHub repository.
- Click on 'Fork' in the top right corner.
- This will take you to your own repository to fork with the same name as the original branch.

## Creating Local Clone
Steps to create a local clone:
- Click on the code tab under the repository name.
- Then click 'Code' button to the right above the files listed.
- Click on clipboard icon to copy the URL.

[Back to top](#table-of-contents)

# Credits
## Content
- [Django](https://www.djangoproject.com/) for general tips and how to.
- 'Django Rest Framework' walkthrough project on how to setup the whole code environment, models, views, etc.
- [Slack](https://slack.com/) for any issues and questions.
- [W3CSchool](https://www.w3schools.com/) for general and helpful tips.
- [Stack Overflow](https://stackoverflow.com/) when I was stucked and needed help with code.

# Acknowledgements
- This project was built as a part of the Full Stack Software Development education at [Code Institute](https://codeinstitute.net/).
- My mentor Spencer Barriball for the guidance and encouragement.
- My Wifi thank you for all the support.

[Back to top](#table-of-contents)