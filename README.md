# Gamers Digest

Gamers Digest is a website that aims to keep gamers updated with the latest gaming news on different platforms. The site targets people of various ages that are gamers and gives you the opportunity to read news and find details and related news about each game. The website is updated with news regularly to keep users coming back to the site.


## Project goals:
- __User goals__
  - To keep updated with the latest news in the gaming industry
  - To explore content on a wide range of games, genres, and platforms
- __Site owner goals__
  - To showcase a fullstack web application that meets the assessment criteria
  - To create a service that provides a useful and informative content for gamers

## User experience

### User category
  - Gamers Digest is directed towards game enthusiasts

### User expectations
  - Collected gaming news from different sources 
  - Details about various games of multiple genres and platforms
  - A website with a smooth navigation and responsive design
  - An easy and secure registration and authentication process

### User stories

### Epic 1: User Authentication
This epic focuses on user account management, including registration, login/logout.

- User Account Registration (MUST HAVE)
- Easy Login from Landing Page (MUST HAVE)
- Log out of User account (MUST HAVE)
- Create a list of favourites (COULD HAVE)

### Epic 2: Content Management
This epic deals with the core functionalities of the blog, such as creating, reading, editing, and deleting posts, as well as interacting with posts through comments and likes.

- Create, Edit & Delete News Posts (MUST HAVE)
- See Post Overview (SHOULD HAVE)
- Open a post (MUST HAVE)
- Leave a comment on a post (COULD HAVE)
- Bookmark Blog Posts (COULD HAVE)
- Like/ Unlike Blog Posts (COULD HAVE)
- Receive Validating Messages (SHOULD HAVE)
- Follow Other Users (WON'T HAVE)

### Epic 3: Administration & Analytics
This epic encompasses administrative control over the site, including user account management and content moderation, as well as tracking user engagement.

- Admin - Manage Blog Posts (MUST HAVE)
- Admin - Categorize Blog Posts (SHOULD HAVE)
- Admin - Full Control Over User Accounts (COULD HAVE)
- Admin - Track User Engagement and Analytics (WON'T HAVE)

### Epic 4: User Experience & Accessibility
This epic is focused on the overall user experience on the site, such as the appearance of the homepage, ease of navigation, and accessibility of information.

- Navigate through a well-designed website (MUST HAVE)
- Make the landing page Visually Appealing (SHOULD HAVE)
- Navigate to About Us (SHOULD HAVE)
- Site pagination for easy navigation (SHOULD HAVE)
- Receive Page Error Messages (SHOULD HAVE)

## Database
- __News application database schema__

When creating the database structure schema for this project, I utilized the [dbdiagram.io](https://dbdiagram.io/) website. This online tool allowed me to visually design and document the database schema, making it easier to plan and implement the database for the news application.

<center> 

![Database Schema image](directory)

</center>

## Database Schema Summary

### `User` Table
- Represents the basic user information according to Django's built-in User model.
- Fields: `username`, `email`, `password`.

### `Platform` Table
- Stores the different platforms that the superuser can select when creating a game.
- Fields: `platform_id`, `platform_name`.

### `Post` Table
- Stores comments made by users on blog posts.
- Fields: `post_id`, `title`,`slug`, `intro`, `content`, `topic`, `created_on`, `updated_on`.

### `Game` Table
- Stores news posts written by the superuser.
- Fields: `game_id`, `title`, `slug`, `genre`, `description`, `platform`, `age_rating`, `developer`, `publisher`, `release`,  `featured_image`.

This database schema lays out the structure for the Gamers Digest application, giving an opportunity for gamers to easily keep updated with the latest gaming news and game details including releases.

## Design
- __Color__
  - Use various sources that suggest different color combinations
- __Typography__
  - Select suitable fonts for:
    - post-list: topic, title, intro, details
    - post page: title, topic, details, content
    - game page: title, details, description
    - Header: logo, navigation bar, authentication status message
    - footer: informative text, icons

- __Layout__
The Gamers Digest website is designed with a user-friendly structure, ensuring seamless navigation and easy access to the website's content, which is about gaming. Below is an overview of the website's structure:

  - **The header:**
    - The header is located at the top of the website.
    - It contains a logo "Gamers Digest" to the left.
    - A navigation bar comes after the logo with a list of options in text form.
    - An authentication message that shows the user login status to the right.

  - **The footer:**
    - The footer is at the bottom of the page.
    - It has a signature and social media links in icon form.

  - **Home Page:**
    - In the main page the user can view a list of news posts.
    - Each post is displayed as an engaging card, featuring a clickable title, topic, intro, and creation date.

  - **News Post View:**
    - Each news post can be viewed in its entirety on a dedicated page.
    - This view presents an engaging card that presents the title, topic, intro, and updated date.
    - Also two clickable buttons, 'Edit' and 'Delete', are included when the poster is logged in.
    - Right after that a detailed content about the news.
    - Below the news content, the user can see a list of related posts to the game

  - **Create Post View:**
    - This page is a form for submitting posts.
    - The form has four fields title, slug, intro, and content.
    - New posts, once published, are prominently displayed on the home page.

  - **Game details view:**
    - The game page shows details about each game.
    - The user can see a game cover, description, and details: such as developer, publisher, platform, etc.
    - Related news can be seen at the bottom of the page.

- __Wireframes__

## Features

### Existing Features
- __The Header__  
- __The footer__

### Additional Features to Implement

## Testing
### Validator testing
### Bugs
#### Solved bugs
#### Unfixed bugs

## Deployment

**Create the Heroku app:**

- Navigate to your Heroku dashboard and create a new app with a unique name.
- Click on the Settings tab and reveal the config vars. 
- Add a key of DISABLE_COLLECTSTATIC and a value of 1 and click Add. 
- This step prevents Heroku from uploading static files, such as CSS and JS, during the build.
---
**Update your code for deployment:**

- Install a production-ready webserver for Heroku using the command <mark>pip3 install gunicorn~=20.1</mark>
- Add gunicorn==20.1.0 to the requirements.txt file with: <mark>pip3 freeze --local > requirements.txt</mark>
- Create a file named Procfile at the root directory of the project (same directory as requirements.txt).
- In the Procfile, declare this is a web process followed by the command to execute your Django project and start the server.
  <mark>web: gunicorn my_project.wsgi</mark> This assumes your project is named my_project.
- Open the my_project/settings.py file and replace DEBUG=True with DEBUG=False. and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.
- Git add, commit and push the code to your GitHub repo.
---
**Connect Heroku to PostgreSQL database:**
- Navigate to heroku dashbord and return to settings.
- Click on <mark>Reveal Config Vars</mark> and add <mark>DATABASE_URL</mark>.
- Note! if ElephantSQL is used as a PostgreSQL provider. 
- Navigate to https://www.elephantsql.com/, log in and create a database instance.
- Open your created instance and go to the details tag.
- copy the provided PostgreSQL <mark>URL</mark>.
- Assign it as a value to DATABASE_URL in the Heroku dashboard.
- Now your PostgreSQL cloud database is connected to your deployed app.
---
**Deploy to Heroku:**
- Now, let's return to the Heroku dashboard, and in your app, click on the Deploy tab. 
- In the Deployment method section enable GitHub integration by clicking on Connect to GitHub.
- Search for your GitHub repo and connect it to the Heroku app. 
- Scroll down and Manually deploy the main branch of this GitHub repo. In your new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on.
- Click on <mark>Open app</mark> to open the rendered webpage.

## Credits
### Content
### Media
