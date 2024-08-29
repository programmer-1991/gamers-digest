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

### Epic 1: Account Management
- User Account Registration (MUST HAVE)
- Login to user account (MUST HAVE)
- Log out of User account (MUST HAVE)
- Show authentication status (SHOULD HAVE)
- Delete user account (SHOULD HAVE)
- Restore your password (COULD HAVE)
- Create a list of favourites (COULD HAVE)
- Full Control Over User Accounts (WON'T HAVE)

### Epic 2: User Interaction
- Open a news post (MUST HAVE)
- Open a game post (MUST HAVE)
- Leave a comment on a post (COULD HAVE)
- Leave a review on a game (COULD HAVE)
- Manage content items (WON'T HAVE)

### Epic 3: Site Management
- Manage news items (MUST HAVE)
- Manage game items (MUST HAVE)
- Receive confirmation messages (SHOULD HAVE)
- Receive validation messages (SHOULD HAVE)
- Categorize news posts (COULD HAVE)
- Categorize game posts (COULD HAVE)
- Track User Engagement and Analytics (WON'T HAVE)

### Epic 4: User Experiences
- Make the interface visually Appealing (MUST HAVE)
- Have access to page about website (SHOULD HAVE)
- Paginate lists for easy navigation (SHOULD HAVE)
- Receive page load error Messages (SHOULD HAVE)

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
    - This view is an engaging card that presents the title, topic, intro, and updated date.
    - Two buttons 'Edit' and 'Delete', are only accessible to superusers.
    - Right after that a detailed content about the news.
    - Below the news content, the user can see a list of related posts to the game

  - **Create Post View:**
    - This page is a form for submitting posts.
    - The form has four fields title, slug, intro, and content.
    - New posts, once published, are prominently displayed on the home page.
  
  - **Game List View:**
    - In the game list page the user can view a list of game posts.
    - Each game is displayed as an engaging card, featuring a clickable picture and game title.

  - **Create Game View:**
    - This page is a form for submitting games.
    - The form has nine fields title, slug, genre , description, platform, age rating, developer, publisher, release date and featured_image.
    - New games, once added, are prominently displayed on the game list page.

  - **Game details view:**
    - The game page shows details about each game.
    - Two buttons 'Edit' and 'Delete', are only accessible to superusers.
    - The user can see a description and a picture, and details: such as developer, publisher, platform, etc.
    - Related news to the game can be seen at the bottom of the page.

- __Wireframes__

## Features

### Existing Features
- Logo is the application's name and it takes you to the home page when clicking on it.
- A navigation bar with links to:
  - Home page
  - Games: it shows all games in a list
  - Create a post or a game
  - Register and log in if the user is logged out 
  - Just log out if the user is logged in.
- An informative message that tells if the user is logged in.
- About us section: It provides information about the website
- Read a news post
- Read game details
- Only administrators have access to the following functions:
  - Create a news post
  - Create a game 
  - Edit a news post
  - Edit a game 
  - Delete a news post
  - Delete a game
- View posts list on homepage
- Navigate to see more posts
- Filter posts by game genre
- Register an account
- Log in 
- Log out
- A footer that tells about the website's creator associated with clickable Social media links.
### Additional Features to Implement

## Testing

## Code Validation

### HTML Validation
I used the[W3C Markup Validation](https://validator.w3.org/) service to check the HTML code of my project for compliance with web standards. This tool is essential for identifying syntax errors and ensuring robust and standard-compliant HTML.

The HTML pages were extracted from dev tools using Google Chrome's inspect feature and then copy the HTML code for every page from sources. This code doesn't include Django Template Language to avoid validation errors (Some characters are not allowed) when using tools like W3C validator.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|login.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_login.png)</details>| ✅
|logout.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_logout.png)</details>| ✅
|signup.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_sign_up.png)</details>| ✅
|about_us.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_about_us.png)</details>| ✅
|index.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_index.png)</details>| ✅
|game.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_game.png)</details>| ✅
|post_detail.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_post_detail.png)</details>| ✅
|create_post.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_create_post.png)</details>| ✅
|post.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_posts.png)</details>| ✅
|game_list.html| No errors | <details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/wc3_html_posts.png)</details>| ✅

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by W3C that allows you to validate and check the correctness of your CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|style.css| No errors |<details><summary>Screenshot of result</summary>![Result](docs/test.md/wc3/css_wc3_validation.png)</details>| ✅

### Javascript Validation:
- No errors were found when passing javascript code through the official [Jshint validator](https://jshint.com/). The following metrics were returned:
  - point 1
  - point 2
  - point 3
  - point 4

### Python Validation:
[PEP 8](https://pep8ci.herokuapp.com/) serves as a comprehensive style guide for writing Python code, emphasizing consistency and readability as its core principles. It offers guidance on code formatting, variable and function naming conventions, and various best practices. Adhering to PEP 8 principles contributes to enhancing code quality, making it more readable and maintainable.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| gamers_digest/settings.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_settings.png)</details> | ✅ |
| gamers_digest/urls.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_cc_urls.png)</details> | ✅ |
| news/models.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_models.png)</details> | ✅ |
| news/views.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_test_views.png)</details> | ✅ |
| news/forms.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_forms.png)</details> | ✅ |
| blog/urls.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_blog_urls.png)</details> | ✅ |
| news/admin.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_admin.png)</details> | ✅ |
| news/tests/test_views.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_test_views.png)</details> | ✅ |
| news/tests/test_models.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_test_models.png)</details> | ✅ |
| news/tests/test_urls.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_test_urls.png)</details> | ✅ |
| news/tests/test_forms.py | All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/test.md/pep8/ci_linter_test_forms.png)</details> | ✅ |

&nbsp;

## Manual Testing
&nbsp;
### Security Testing

Ensuring that users cannot access or modify content created by the superuser is crucial for maintaining the integrity and security of the application. The table demonstrates the application's robustness in handling unauthorized access attempts, ensuring user data security and integrity.

The following tests were conducted to verify that unauthorized access attempts are properly handled.

| Test Case | Description | Method | Expected Outcome | Actual Outcome | Result |
| --------- | ----------- | ------ | ---------------- | -------------- | --------- |
| Create Post Unauthorized Access | Non-admin attempting to create a post | Manual URL manipulation | The news-post creation form  is unavailable | A message tells this feature is only available to superusers | ✅ |
| Create Game Unauthorized Access | Non-admin attempting to create a game | Manual URL manipulation | The game-post creation form is unavailable | A message tells this feature is only available to superusers | ✅ |
| Edit Post Unauthorized Access | Non-admin attempting to edit a post | Manual URL manipulation | The adress non-functional | Redirect to post details page | ✅ | 
| Delete Post Unauthorized Access | Non-admin attempting to delete a post | Manual URL manipulation | The adress non-functional | Redirect to game list page | ✅ |
| Edit Game Unauthorized Access | Non-admin attempting to edit a game |  Manual URL manipulation | The adress non-functional | Redirect to game details page | ✅ |
| Delete Game Unauthorized Access | Non-admin attempting to delete a post | Manual URL manipulation | The adress non-functional | Redirect to game list page | ✅ |

### Testing user stories

**Epic 1: User Authentication & Profile Management**

| User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [User Account Registration (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/2) | Implemented a user registration system allowing visitors to create new accounts. Register option is in the navigation bar. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_sign_up.png)</details> |
| [Log Out of User Account (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/3) | Provided logout functionality for user accounts. Log out option is in the navigation bar.| <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_log_out.png)</details>|
| [Log in to User Account (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/3) | Provided login functionality for user accounts. Log in option is in the navigation bar.| <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_log_out.png)</details>|
| [Show authentication status (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/3) | The user can see opposite the logo a confirmation message that tells the authentication status.| <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_log_out.png)</details>|
| [Full Control Over User Accounts (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/43) | This feature was not implemented in this phase, but admin can have full control in admin site. | No result image |
| | | |

&nbsp;
**Epic 2: User Interaction**

| User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Open a news post (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/7) | Users can open news posts and read details. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_create_new_post.png)</details> |
| [Open a game post (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/8) | Users can open game posts and read details. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_blogpost_detail.png)</details> |
| [ Manage content items (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/30) | Non-admin users can't manage data. | No result image |
|

&nbsp;

**Epic 3: Administration & Analytics**

| Site Owner Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| [Manage news items (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/13) | Admin can create, update and delete news items.| <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_admin_full_control.png)</details> |
| [Manage game items (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/14) | Admin can create, update and delete game items. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_admin_postlist.png)</details> <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_admin_commentlist.png)</details> |
| [Receive confirmation messages (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/15) | Admin gets a confirmation message when: login, logout, create, edit and delete content items. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_admin_manage_post.png)</details> |
| [ Receive error messages (SHOULD HAVE) ](https://github.com/DebbieBergstrom/Culture-Club/issues/15) | Admin gets an error message when item creation, update, and deletion fails. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_admin_manage_post.png)</details> |
| [ Track User Engagement and Analytics (WON'T HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/16) | This feature for tracking analytics was not implemented in the current phase. | No result image |
| | | |

&nbsp;

**Epic 4: User Experience & Accessibility**

- Make the interface visually Appealing (MUST HAVE)
- Have access to page about website (SHOULD HAVE)
- Paginate lists for easy navigation (SHOULD HAVE)
- Receive page load error Messages (SHOULD HAVE)


| User Goals | How to achieve this | Screenshot |
| --- | --- | --- |
| [ Interact visually Appealing interface (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/17) | Design the interface in a well structured manner, Make it responsive and accessible. | <details><summary>Screenshot of result</summary>![Result](docs/features/login_landing_page.png)</details> |
| [ access page about the website (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/18) | Included clear navigation to the 'About Us' section to inform users about the website. Can always be seen in the navbar or the collapsed menu in smaller screens. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_about_us.png)</details> |
| [ Browse lists (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/32) | Implemented pagination for easy browsing of news and game posts. | <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_pagination_next.png)</details> <details><summary>Screenshot of result</summary>![Result](docs/test.md/userstories/us_pagination_prev.png)</details> |
| [Receive page load error Messages (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/42) | User gets an error page if something isn't working correctly. | <details><summary>Screenshot of result</summary>![Result](docs/features/500_error_page.png)</details> |
| | | |

&nbsp;
### Responsivness:
Tested the website responsiveness for different device types using [responsive design checker](https://responsivedesignchecker.com/) tool. The result was that heroku server doesn't allow access for this tool. Tested also with [Am I Responsive](https://ui.dev/amiresponsive) and [Responsive test tool](https://responsivetesttool.com/) and they showed the same result as in the first test.

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
- Add the environment variable <mark>SECRET KEY</mark> to the Heroku app's config vars in the settings for security reasons.
- Now, let's return to the Heroku dashboard, and in your app, click on the Deploy tab.
- In the Deployment method section enable GitHub integration by clicking on Connect to GitHub.
- Search for your GitHub repo and connect it to the Heroku app.
- Scroll down and Manually deploy the main branch of this GitHub repo.
- In your new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on.
- Click on <mark>Open app</mark> to open the rendered webpage.
---
### Fork the Repository:
By forking the GitHub Repository, you can create a copy of the original repository without affecting the original. To implement that follow these steps below:

- Log into GitHub account or create one if you don't have one.
- Locate the Repository. Note! the repository is at https://github.com/programmer-1991/gamers-digest.
- At the top right of the repository page, click "Fork" to create a copy in your own GitHub repository.

**Clone the Repository:**
When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. Creating a clone allows you to have a local copy of the project. Follow these steps:

- Navigate to https://github.com/programmer-1991/gamers-digest.
- Click the green "Code" button at the top right.
- Select the "Clone by HTTPS" option and copy the web URL to the clipboard.
- Open your code editor or terminal and navigate to the directory where you want to clone the repository.
- Run `git clone` followed by the copied URL.
- Press enter, and Git will clone the repository to your local machine.

# Credits
### Here's a collection of sites that were helpful in creating this website:

- [Django documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/) is used for guidance with models, forms, templates, and various aspects of Django development.

- [Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/) is used to increase knowledge of Bootstrap framework.

- [W3 Schools](https://www.w3schools.com/)


- [Stackoverflow](https://stackoverflow.com/) was used for:
  - Scroll down the page upon clicking the Edit button.

- Tutorials and YouTube videos:
  - [Portfolio Project 4: The guide to MVP](https://www.youtube.com/watch?v=vIv1c6RLBac)
  - [Assessments Q&A: Focus on PP4](https://www.youtube.com/watch?v=_0VXXEgchw4)
  - [The guide to the Github Agile Tool](https://www.youtube.com/watch?v=U_dMihBgUNY)

- Other sites:
  - [Styling Crispy forms](https://blog.appseed.us/django-forms-styling-with-bootstrap/)
  - [Organize Imports](https://peps.python.org/pep-0008/)
  - [Generate Slugs](https://www.kodnito.com/posts/slugify-urls-django/)
  - [How to override default django templates](https://www.makeuseof.com/override-default-templates-django-allauth/)
  - [Automated testing tutorial](https://www.youtube.com/watch?v=6I_haJimhPY)

- The base structure of the project is inspired by the walkthrough project `I think therefore I blog`.
- Readme structure is based on [readme template](https://github.com/DebbieBergstrom/Culture-Club/blob/main/README.md) belonging to `Culture Club project` created by [DebbieBergstrom](https://github.com/DebbieBergstrom).
- The favicon used in the application was taken from [favicon io](https://favicon.io/).
- The fonts used in the application was taken from [Google Fonts](https://fonts.google.com/).

- [Favicon Generator](https://favicon.io/) to create a favicon in the browser tab.
- [Pexels Free Images](https://www.pexels.com/sv-se/) to find some user profile mockup images.
- [Freepik Free Images](https://www.freepik.com/free-photos-vectors/user-profile) to find user profile symbols and default images.
