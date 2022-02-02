<h1 align="center">LastLife Website</h1>

[View the live project here.]()

<h2 align="center"><img src=""></h2>

## Project Summary

LastLife is a website for a second hand video game store. This store will sell everything from consoles and accessories to the games themselves and will be equiped with everything to be expected from a modern online store such as account management, payment security, and an intuative shopping cart. The website will be a full stack application using an SQL relational database, the Django/Python full stack MVC framework and related contemporary technologies. The data model, application features and business logic will manage, query and manipulate relational data to meet the given needs of this real-world domain. It will present authorisation, authentication and permission features in a full stack web application solution. It will contain an intergrated Stripe e-commerce payment system, in a cloud-hosted full stack web application. The entire development process will be documented via git version control and the final iterations will be deployed to Heroku and hosted via AWS.

## Website Design Objectives

#### DO1 Design, develop and implement a full stack web application, with a relational database, using the Django/Python Full Stack MVC framework and related contemporary technologies

-   (1.1) Design a full stack web application to be built using the Django framework and to incorporate a relational database and multiple apps (an app for each potentially reusable component)
-   (1.2) Design a front end for a full stack web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provide a set of user interactions
-   (1.3) Develop and implement a full stack web application built using the Django framework, to incorporate a relational database, an interactive front end and multiple apps (an app for each potentially reusable component)
-   (1.4) Implement at least one form, with validation, that allows users to create and edit models in the backend
-   (1.5) Build a Django file structure that is consistent and logical, following the Django conventions
-   (1.6) Write code that clearly demonstrates characteristics of ‘clean code’
-   (1.7) Define application URLs in a consistent manner
-   (1.8) Incorporate a main navigation menu and structured layout
-   (1.9) Demonstrate proficiency in the Python language by including sufficient custom logic in your project
-   (1.10) Write Python code that includes functions with compound statements such as if conditions and/or loops
-   (1.11) Design and implement manual, and automated test procedures to assess functionality, usability, responsiveness and data management within the full web application

#### DO2 Design and implement a relational data model, application features and business logic to manage, query and manipulate relational data to meet given needs in a particular real-world domain

-   (2.1) Design a relational database schema with clear relationships between entities
-   (2.2) Create at least TWO original custom Django models
-   (2.3) Create at least one form with validation that will allow users to create records in the database (in addition to the authentication mechanism)
-   (2.4) All CRUD (create, select/read, update, delete) functionality is implemented


#### DO3 Identify and apply authorisation, authentication and permission features in a full stack web application solution

-   (3.1) Implement an authentication mechanism, allowing a user to register and log in, addressing a clear reason as to why the users would need to do so
-   (3.2) Implement login and registration pages that are only available to anonymous users
-   (3.3) Implement functionality that prevents non-admin users from accessing the data store directly without going through the code

#### DO4 Design, develop and integrate an e-commerce payment system in a cloud-hosted, full stack web application

-   (4.1) Implement at least one Django app containing some e-commerce functionality using an online payment processing system (e.g. Stripe). This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc
-   (4.2) Implement a feedback system that reports successful and unsuccessful purchases to the user, with a helpful message

#### DO5 Document the development process through a git based version control system and deploy the full application to a cloud hosting platform

-   (5.1) Deploy the final version of your code to a hosting platform and test that it matches the development version
-   (5.2) Ensure that all final deployed code is free of commented out code and has no broken internal links
-   (5.3) Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off
-   (5.4) Use a git-based version control system for the full application, generating documentation through regular commits and in the project README
-   (5.5) Create a project README that is well-structured and written using a consistent markdown format
-   (5.6) Document the full deployment procedure, including the database, and the testing procedure, in a README file that also explains the application’s purpose and the value that it provides to its users

## User Experience (UX)

-   ### User stories

    -   #### Viewing and Navigation

        1. As a User, I want to easily understand the main purpose of the site and learn more about the business.
        2. As a User, I want to be able to view a list of products and select some to purchase.
        3. As a User, I want to view individual product details so I can identify the appearance, price, description and rating.
        4. As a User, I want to quickly identify deals, clearance items and special offers so I can take advantage of special savings on items I'd like to purchase.
        5. As a User, I want to easily view the total of my purchases at any time so I can avoid spending too much or make a mispurchase.

    -   #### Registration and User Accounts

        1. As a User, I want to register for an account so I can have a personal account and be able to view my user profile.
        2. As a User, I want to login or logout so I can access my personal account information.
        3. As a User, I want an option to recover password in case I forget it so I can regain access to my account.
        4. As a User, I want to recieve an email confirmation after registering so I can verify that my account registration was successful
        5. As a User, I want to have a personalized user profile so I can view my personal order history and order confirmations, and save my payment information.

    -   #### Sorting and Searching

        1. As a User, I want to sort the list of available products so I can easily identify the best-selling, best-priced, or best-rated items available.
        2. As a User, I want to sort a specific category of products so I can find the best-priced or best-rated product in a specific category, or sort the                    products in that category by name.
        3. As a User, I want to sort multiple categories of products simultaneously so I can find the best-priced or best-rated products across broad categories,              such as "genres" or "accessories".
        4. As a User, I want to search a product by name or description so I can find a specific product I would like to purchase.
        5. As a User, I want to see what I've searched for and number of results so I can quickly identify whether the product I want is available or not.

    -   #### Purchasing and Checkout

        1. As a User, I want to easily select the quantity of a product, if applicable, so I can ensure I dont accidentally select the wrong product or quantity of products.
        2. As a User, I want to view the items in my cart to be purchased so I can identify the total cost of my purchase and all items I will recieve.
        3. As a User, I want to adjust the quantity of individual items in cart if applicable so I can make changes before checkout.
        4. As a User, I want to easily enter my payment information so I can check out quickly with no hassle.
        6. As a User, I want to view an order confirmation after checkout so I know that my order was successful.
        7. As a User, I want to recieve an email confirmation after checkout so I can keep the confirmation of what I purchased for personal records.

    -   #### Administration and Store Management

        1. As a User, I want to add a product listing so I can add new products to my store.
        2. As a User, I want to edit or update a product listing so I can change product prices, descriptions, images, and other product information.
        3. As a User, I want delete functionality so I can remove items that are no longer for sale.

-   ### Design
    -   #### Colour Scheme
        -   For this site I have chosen to use a complimantary colour scheme using white and jet black as the base colors with high contrasting colors, like Rosso             Corsa red and May green, to draw the users attention to certain actions or events such as clearance sales or new items. Dark orange will be used for decoration, highlights and buttons. 
        -   Here is a [link to the palette](https://github.com/JMuckian94/MSP4_LastLife/blob/main/wireframes/lastlifepalette.png) created using Coolers.co.
    -   #### Typography
        -   The primary font is Open Sans, a very popular font used by millions of sites, due to its elegant look and its legibillity. San serif will load in its               place if there is problems with the browser loading the primary font.
    -   #### Imagery
        -   Imagery will be used for two roles on the website. The first set are for decorating the pages, particularly the landing page. These images are relevant             to the websites purpose so new users can quickly identify who and what our company is. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

-   ### Wireframes

    -   Mobile Wireframes - [View](https://github.com/JMuckian94/MSP4_LastLife/tree/main/wireframes/mobile)

    -   Tablet Wireframes - [View](https://github.com/JMuckian94/MSP4_LastLife/tree/main/wireframes/tablet)

    -   Desktop Wireframes - [View](https://github.com/JMuckian94/MSP4_LastLife/tree/main/wireframes/desktop)

-   ### Database Structure

product
| Name         | Type          |
|--------------|---------------|
| id           | INT           |
| name         | CharField(254)| 
| desc         | TEXT          |
| SKU          | VARCHAR(255)  |
| category  | INT           |
| price        | DECIMAL(8, 2) |
| discount_id  | INT           |

product_inventory
| Name        | Type      |
|-------------|-----------|
| id          | INT       |
| quantity    | INT       |
| created_at  | TIMESTAMP |
| modified_aT | TIMESTAMP |
| deleted_at  | TIMESTAMP |

discount
| Name             | Type          |
|------------------|---------------|
| id               | INT           |
| name             | VARCHAR(255)  |
| desc             | TEXT          |
| discount_percent | DECIMAL(8, 2) |
| active           | TINYINT(1)    |
| created_at       | TIMESTAMP     |
| modified_at      | TIMESTAMP     |
| deleted_at       | TIMESTAMP     |

Order
| Variable | Type | Field | Field | Field | Field | Field |
|---|---|---|---|---|---|---|
| order_number | CharField(32) | null=False | editable=False |  |  |  |
| user_profile | FOREIGNKEY | 'UserProfile' | on_delete=models.SET_NULL | null=True | blank=True | related_name='orders' |
| full_name | CharField(50) | null=False | blank=False |  |  |  |
| email | EmailField(254) | null=False | blank=False |  |  |  |
| phone_number | CharField(20) | null=False | blank=False |  |  |  |
| street_address1 | CharField(80) | null=False | blank=False |  |  |  |
| street_address2 | CharField(80) | null=True |  |  |  |  |
| postcode | CharField(20) | null=True |  |  |  |  |
| town_or_city | CharField(40) | null=False | blank=False |  |  |  |
| county | CharField(80) | null=True |  |  |  |  |
| country | CountryField() | blank_label='Country *' | null=False | blank=False |  |  |
| date | DateTimeField | auto_now_add=True |  |  |  |  |
| delivery_cost | DecimalField(6,2) | null=False | default=0 |  |  |  |
| order_total | DecimalField(10,2) | null=False | default=0 |  |  |  |
| grand_total | DecimalField(10,2) | null=False | default=0 |  |  |  |
| original_cart | TextField | null=False | blank=False | default='' |  |  |
| stripe_pid | CharField(254) | null=False | blank=False |  |  |  |

OrderLineItem
| Variable | Type | Field | Field | Field | Field | Field |
|---|---|---|---|---|---|---|
| order | ForeignKey | Order | null=False | blank=False | on_delete=models.CASCADE | related_name='lineitems' |
| product | ForeignKey | Product | null=False | blank=False | on_delete=models.CASCADE |  |
| quantity | IntegerField | Order | null=False | blank=False | default=0 |  |
| lineitem_total | DecimalField(6,2) | null=False | blank=False | editable=False |  |  |
|  |  |  |  |  |  |  |

UserProfile
| Variable | Type | Field | Field | Field |
|---|---|---|---|---|
| user | OneToOneField | User | on_delete=models.CASCADE |  |
| default_phone_number | CharField(20) | null=True | blank=True |  |
| default_street_address1 | CharField(80) | null=True | blank=True |  |
| default_street_address2 | CharField(80) | null=True | blank=True |  |
| default_postcode | CharField(20) | null=True | blank=True |  |
| default_town_or_city | CharField(40) | null=True | blank=True |  |
| default_county | CharField(80) | null=True | blank=True |  |
| default_country | CountryField | blank_label='Country *' | null=True | blank=True |

shopping_session
| Name        | Type          |
|-------------|---------------|
| id          | INT           |
| user_id     | VARCHAR(255)  |
| total       | DECIMAL(8, 2) |
| created_at  | TIMESTAMP     |
| modified_at | TIMESTAMP     |

cart_item
| Name        | Type      |
|-------------|-----------|
| id          | INT       |
| session_id  | INT       |
| product_id  | INT       |
| quantity    | INT       |
| created_at  | TIMESTAMP |
| modified_at | TIMESTAMP |

payment_details
| Name        | Type         |
|-------------|--------------|
| id          | INT          |
| order_id    | INT          |
| amount      | INT          |
| provider    | VARCHAR(255) |
| status      | VARCHAR(255) |
| created_at  | TIMESTAMP    |
| modified_at | TIMESTAMP    |

user_address
| Name          | Type         |
|---------------|--------------|
| id            | INT          |
| user_id       | INT          |
| address_line1 | VARCHAR(255) |
| address_line2 | VARCHAR(255) |
| city          | VARCHAR(255) |
| post_code     | VARCHAR(255) |
| country       | VARCHAR(255) |
| telephone     | VARCHAR(255) |
| mobile        | VARCHAR(255) |

user_payment
| Name         | Type         |
|--------------|--------------|
| id           | INT          |
| user_id      | INT          |
| payment_type | VARCHAR(255) |
| provider     | VARCHAR(255) |
| account_no   | INT          |
| expiry       | DATE         |

admin_type
| Name        | Type         |
|-------------|--------------|
| id          | INT          |
| admin_type  | VARCHAR(255) |
| permissions | VARCHAR(255) |
| created_at  | TIMESTAMP    |
| modified_at | TIMESTAMP    |

adminuser
| Name        | Type          |
|-------------|---------------|
| id          | INT           |
| username    | VARCHAR(255)  |
| password    | TEXT          |
| first_name  | DECIMAL(8, 2) |
| last_name   | VARCHAR(255)  |
| type_id     | INT           |
| last_login  | TIMESTAMP     |
| created_at  | TIMESTAMP     |
| modified_at | TIMESTAMP     |




## Features

-   Responsive on all screen sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML](https://en.wikipedia.org/wiki/HTML5)
-   [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Bootstrap:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome Icons was used throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/JMuckian94/MSP4_LastLife/tree/main/wireframes) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

### Testing User Stories from User Experience (UX) Section


-   #### Viewing and Navigation

    1. As a User, I want to easily understand the main purpose of the site and learn more about the business.

        1. The user can identify the name and purpose of the site from the hero image, logo, blurb and call to action.
        2. Using the navigation options, the user can quickly dart around the site to get a feel for what the sites purpose is and what its like to shop here.

    2. As a User, I want to be able to view a list of products and select some to purchase.

        1. The user can click the call to action on the home page which will take them to the all products view.
        2. Products can be organised by their name, price, category and ratings. If the category is games, they can also be sorted by genre.
        3. Clicking items brings users to the product detail page.

    3. As a User, I want to view individual product details so I can identify the appearance, price, description and rating.

        1. The product details page has a product image, the title of the product, a description, rating, a quantity selector and buttons to either return to the previous page or add to their shopping cart.
        2. Every detail is clearly legible and intended to be responsive on mobile. All interactive elements are functioning.
    
    4. As a User, I want to quickly identify deals, clearance items and special offers so I can take advantage of special savings on items I'd like to purchase.

        1. .
        2. ...
        3. ...
    
    5. As a User, I want to easily view the total of my purchases at any time so I can avoid spending too much or make a mispurchase.

        1. When the user clicks the 'add to shopping cart' button the user is notified of the action via a toast which appears from the top right of the screen where the shopping cart icon in the navbar is located.
        2. If the user clicks the shopping cart icon they will be taken to the cart page where they can view all of the items they have added. The customer will have the option to remove excess items or add a greater quantity of them.
        3. The customers item cost totals will be listed towards the bottom. The customer can avail of free delivery if they spend over the specified delivery delta amount advertised in both a fixed banner under the navbar and in the toasts when an item is added to the cart.

-   #### Registration and User Accounts
    
    1. As a User, I want to login or logout so I can access my personal account information.

        1. The user can log in and out of the website if they have created a user account, either through the options in the navigation, which will take them to the login/signup screen, or by creating an account on checkout, which will save the information they provided to their user profile automatically.
        2. Loging in will require the user enter their username and password, which will be held securely in the sites database.
        3. Loging out is as simple as clicking the account icon on the navbar and selecting logout.
    
    2. As a User, I want an option to recover password in case I forget it so I can regain access to my account.

        1. On the login screen there is a link to reset password. The user will be taken to the reset password screen where they will need to enter their new password.
        2. The form
        3. ...
    
    3. As a User, I want to recieve an email confirmation after registering so I can verify that my account registration was successful

        1. When the user registers a new account successfully they will recieve a notification on the website that they have been sent an email confirmation.
        2. If the user then proceeds to their email account they should see an email. The email is populated with two .txt files, one which populates the body and another for the subject of the mail.
    
    4. As a User, I want to have a personalized user profile so I can view my personal order history and order confirmations, and save my payment information.

        1. On the user profile the user can edit their default information via the provided form, in case there is an error or personal change with the data.
        2. ...
        3. ...

-   #### Sorting and Searching

    1. As a User, I want to sort the list of available products so I can easily identify the best-selling, best-priced, or best-rated items available.

        1. All items are sorted via several criteria such as price, name, rating, promotions and genre (if the item is a game).
        2. The products page has a sort option dropdown with criteria the user can select to arrange the products the way the user desires.
    
    3. As a User, I want to sort multiple categories of products simultaneously so I can find the best-priced or best-rated products across broad categories, such as       "genres" or "accessories".

        1. The user has all the options they need to sort products by prices, ratings, genres or categories. 
        2. If they wish to sort all categories their best option is to use the all products page available when they first enter the site or via the navbar.
    
    4. As a User, I want to search a product by name or description so I can find a specific product I would like to purchase.

        1. The navbar has a search element which will allow users to search for a specific product if the information matches a product in the site database.
    
    5. As a User, I want to see what I've searched for and number of results so I can quickly identify whether the product I want is available or not.

        1. After a search query has been inputted the user will be provided a list of products based on what was inputted. This list should contain a specific suggestion or a broader set depending on how broad or narrow the search phrase is.

-   #### Purchasing and Checkout

    1. As a User, I want to easily select the quantity of a product, if applicable, so I can ensure I dont accidentally select the wrong product or quantity of products.

        1. The user has the option to change the quantity of an item on two occations, firstly on the product details page before they add the item to their card and on the cart page itself with the buttons provided or by clicking the box and typing the desired amount manually.

    2. As a User, I want to view the items in my cart to be purchased so I can identify the total cost of my purchase and all items I will recieve.

        1. The user will be notified whenever they add a item successfully to the cart with a toast message. Users can recieve error and warning messages too via this format. 
        2. All items on the cart main page will be tallied up and a subtotal and a total will be generated. The delivery charge will be added or withheld depending on if the user has spend over the required threshold.
    
    3. As a User, I want to adjust the quantity of individual items in cart if applicable so I can make changes before checkout.

        1. All items in the cart will have an option to adjust the quantity.
    
    4. As a User, I want to easily enter my payment information so I can check out quickly with no hassle.

        1. The payment form is generated using crispy forms and bootstrap styling. Each field has a placeholder specifying what needs to be entered there.
        2. Before asking for payment the site will request the users billing and shipping information.
        3. Once the form above is complete, the user must enter valid card information into the box provided.
        4. When the payment is being processed a brick red overlay will appear with an arrow spinner icon.
    
    6. As a User, I want to view an order confirmation after checkout so I know that my order was successful.

        1. 
        2. ...
        3. ...
    
    7. As a User, I want to recieve an email confirmation after checkout so I can keep the confirmation of what I purchased for personal records.

        1. .
        2. ...
        3. ...

-   #### Administration and Store Management

    1. As a User, I want to add a product listing so I can add new products to my store.

        1. .
        2. ...
        3. ...

    2. As a User, I want to edit or update a product listing so I can change product prices, descriptions, images, and other product information.

        1. .
        2. ...
        3. ...
    
    3. As a User, I want to delete a product so I can remove items that are no longer for sale.

        1. .
        2. ...
        3. ...

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
        3. The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
        4. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
        5. The email button is set up to automatically open up your email app and autofill there email address in the "To" section.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result.
-   On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Shanika Wickramasinghe's article on [What’s an Example of Good E-Commerce Database Design?](https://resources.fabric.inc/blog/answers/ecommerce-database-design-example)

-   Tutor support at Code Institute for their support.
