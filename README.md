<h1 align="center">LastLife Website</h1>

[View the live project here.](https://lastlifemain.herokuapp.com/)


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
        4. As a User, I want to quickly identify promotional offers so I can take advantage of special savings on items I'd like to purchase.
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

Product
| Variable | Type | Field | Field | Field | Field |
|---|---|---|---|---|---|
| id | INT |  |  |  |  |
| sku | VARCHAR(254) | null=True | blank=False |  |  |
| category | FOREIGNKEY | 'Category' | null=True | blank=True | on_delete=models.SET_NULL |
| genre | FOREIGNKEY | 'Genre' | null=True | blank=True | on_delete=models.SET_NULL |
| name | VARCHAR(254) |  |  |  |  |
| description | TEXTFIELD |  |  |  |  |
| price | DECIMALFIELD(6, 2) |  |  |  |  |
| rating | DECIMALFIELD(1, 1) | null=True | blank=True |  |  |
| image_url | URLFIELD(1024) | null=True | blank=True |  |  |
| image | IMAGEFIELD | null=True | blank=True |  |  |


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

Promotions
| Variable | Type | Field | Field | Field |
|---|---|---|---|---|
| name | VARCHAR(254) | null=True | blank=False |  |
| product | FOREIGNKEY | 'Product' | on_delete=models.CASCADE |  |
| valid_from | DATETIMEFIELD |  |  |  |
| valid_to | DATETIMEFIELD |  |  |  |
| discount | INT | validators = | [MinValueValidator(1), | MaxValueValidator(100)]) |
| active | BOOLEANFIELD |  |  |  |

Genre
| Variable | Type |
|---|---|
| name | VARCHAR(100) |
| friendly_name | VARCHAR(100) |

Category
| Variable | Type |
|---|---|
| name | VARCHAR(100) |
| friendly_name | VARCHAR(100) |

## Features

-   Responsive on all screen sizes
-   Intuative navigation
-   Interactive elements
-   Search and sort functionality
-   CRUD implementation
-   Stripe payments
-   Toast messages
-   Attractive storefront

## Technologies Used

### Languages Used

-   [HTML](https://en.wikipedia.org/wiki/HTML5)
-   [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language)

### Frameworks, Libraries & Programs Used

1. [Bootstrap:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome Icons was used throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
    - jQuery is used for various elements to reduce use of raw javascript code.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/JMuckian94/MSP4_LastLife/tree/main/wireframes) during the design process.
8. [Django:](https://docs.djangoproject.com/en/4.0/)
    - Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern. It allows a user to quickly put together full stack applications with responsive frontend design and intuative backend controls.
9. [Heroku:](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is a cloud platform as a service (PaaS) supporting several programming languages. It serves as the host platform for my website.
10. [Amazon Web Services:](https://en.wikipedia.org/wiki/Amazon_Web_Services)
    - Amazon Web Services, Inc. (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. It is where I am storing my static and media files for this project.
 

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
    
    4. As a User, I want to quickly identify promotional offers so I can take advantage of special savings on items I'd like to purchase.

        1. The user has the option to search for the available promotions using the option on the navbar.
        2. The choice sorts out products which have had a promotion applied, however there is no indication of a deduction being applied to the products. This is an obvious design oversite.
        3. Due to time contraints this feature remains incomplete.
    
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
        2. The form will ask them twice to enter the password and then to confirm with a button click towards the bottem of the form.
        3. A toast appears notifying the user if the process was successful or if there was an error.
    
    3. As a User, I want to recieve an email confirmation after registering so I can verify that my account registration was successful

        1. When the user registers a new account successfully they will recieve a notification on the website that they have been sent an email confirmation.
        2. If the user then proceeds to their email account they should see an email. The email is populated with two .txt files, one which populates the body and another for the subject of the mail.
    
    4. As a User, I want to have a personalized user profile so I can view my personal order history and order confirmations, and save my payment information.

        1. On the user profile the user can edit their default information via the provided form, in case there is an error or personal change with the data.
        2. The user also has access to their order history, listing out previous purchases with costs and other critera included.
        3. The user has an option to wipe all data from their profile and start afresh. However, there is no available option to delete user altogether from the customers side. This can only be done by the site admins through the admin panel.

-   #### Sorting and Searching

    1. As a User, I want to sort the list of available products so I can easily identify the best-selling, best-priced, or best-rated items available.

        1. All items are sorted via several criteria such as price, name, rating, promotions and genre (if the item is a game).
        2. The products page has a sort option dropdown with criteria the user can select to arrange the products the way the user desires.
        3. Products are being sorted correctly. The list is responding correctly to user input and everything is sorting correctly
    
    3. As a User, I want to sort multiple categories of products simultaneously so I can find the best-priced or best-rated products across broad categories, such as       "genres" or "accessories".

        1. The user has all the options they need to sort products by prices, ratings, genres or categories. 
        2. If they wish to sort all categories their best option is to use the all products page available when they first enter the site or via the navbar.
        3. All items are sorting correctly and the user can have all the available products in one list.
    
    4. As a User, I want to search a product by name or description so I can find a specific product I would like to purchase.

        1. The navbar has a search element which will allow users to search for a specific product if the information matches a product in the site database.
        2. On mobile this bar will collapse into a maginifying glass icon to save screen space. 
        3. The search function targets any products with a word or criteria related to the search query provided by the user.
    
    5. As a User, I want to see what I've searched for and number of results so I can quickly identify whether the product I want is available or not.

        1. After a search query has been inputted the user will be provided a list of products based on what was inputted. This list should contain a specific suggestion or a broader set depending on how broad or narrow the search phrase is. Near the top it will display a list of how many items are in the given search.
        2. Beneath each item card there are category or genre markers to give the user quick feedback in their search.

-   #### Purchasing and Checkout

    1. As a User, I want to easily select the quantity of a product, if applicable, so I can ensure I dont accidentally select the wrong product or quantity of products.

        1. The user has the option to change the quantity of an item on two occations, firstly on the product details page before they add the item to their card and on the cart page itself with the buttons provided or by clicking the box and typing the desired amount manually.

    2. As a User, I want to view the items in my cart to be purchased so I can identify the total cost of my purchase and all items I will recieve.

        1. The user will be notified whenever they add a item successfully to the cart with a toast message. Users can recieve error and warning messages too via this format. 
        2. All items on the cart main page will be tallied up and a subtotal and a total will be generated. The delivery charge will be added or withheld depending on if the user has spend over the required threshold.
    
    3. As a User, I want to adjust the quantity of individual items in cart if applicable so I can make changes before checkout.

        1. All items in the cart will have an option to adjust the quantity. 
        2. It was planned originally for there to be a limit to availability of certain products such as limited editions or rare items.
        3. This will be available in future versions.
    
    4. As a User, I want to easily enter my payment information so I can check out quickly with no hassle.

        1. The payment form is generated using crispy forms and bootstrap styling. Each field has a placeholder specifying what needs to be entered there.
        2. Before asking for payment the site will request the users billing and shipping information.
        3. Once the form above is complete, the user must enter valid card information into the box provided.
        4. When the payment is being processed a brick red overlay will appear with an arrow spinner icon.
    
    6. As a User, I want to view an order confirmation after checkout so I know that my order was successful.

        1. When an order has been processed successfully the user will be taken to a new screen where they will be shown their confirmation with their details.
        2. The user will also recieve a toast message as a bit of extra user feedback.
        3. The user will be encouraged to return to products at the bottom if they feel they wish to continue shopping.
    
    7. As a User, I want to recieve an email confirmation after checkout so I can keep the confirmation of what I purchased for personal records.

        1. After checkout an email is deployed automatically, with the subject and body populated by .txt files. The email will have records of the order.

-   #### Administration and Store Management

    1. As a User, I want to add a product listing so I can add new products to my store.

        1. The admin has access to several sections under the product model. The genre and category sections have already been filled out so it will rarely be necessary to add more items to those tables.
        2. The product table is accessible through either the admin panel or via a section of the website locked to ordinary users. Here the admin can select category, genre (if it is a game), and set details such as price, rating, name, sku and other criteria.

    2. As a User, I want to edit, update or delete a product listing so I can change product prices, descriptions, images, and other product information or delete if necessary.

        1. If the admin user is signed in as a superuser they have the option to edit or delete directly from the product and product detail pages. This can provide an option for users who prefer the frontend way over the django admin panel.
        2. The django panel however is the most efficient way of editing and deleting products, allowing you to delete groups if so desired. The only downside is you cannot view product images uploaded in django admin until you check the running server.



    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of device widths such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX. This is done by using Google Chromes intuative developer tools.
-   A large amount of testing was done to ensure that all pages were linking correctly. All buttons, forms, searches, sorts and payments were tested prior to deployment.

### Known Bugs

-   Sometimes the footer will appear halfway up the page if there is no content to push it down. This only happens rarely.
-   On xl screens the content can have gaps between boxes and the edges of the screen.
-   

## **Deployment**

### Local Deployment

I have created the project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. Each push is a snapshot of a section being put in place.
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

For this project you need to create an account on Stripe for the order module as well as an account on AWS in order to store your static and media files.

This project can be ran locally by following the following steps: 
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/JMuckian94/MSP4_LastLife
    ``` 

2. Access the folder in your terminal window and install the application's [link to re/reqquired modules](https://github.com/JMuckian94/MSP4_LastLife/blob/main/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

3. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEVELOPMENT"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "STRIPE_PUBLIC_KEY"
    os.environ["STRIPE_SECRET_KEY"] = "STRIPE_SECRET_KEY"
    os.environ["STRIPE_WH_SECRET"] = "STRIPE_WH_SECRET"
    os.environ["STRIPE_CURRENCY"] = "EUR"

    ```
    
    If you're not sure how to get the above Stripe variables, please visit the [Stripe Documentation](https://stripe.com/docs)

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

4. Migrate the database models with the following command
    ```
    python3 manage.py migrate
    ```
5. Create a superuser and set up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```
6. Run the app with the following command
    ```
    python manage.py runserver
    ```
    The address to access the website is displayed in the terminal  
    Add /admin to the end to access the admin panel with your superuser credentials

    
### Heroku Deployment 

1. Login to your Heroku account and create a new app. Choose your region. 
2. Once the app is created click on the resources button and under Add-ons, look for the Heroku Postgres to attach a postgres database to your project.
    Select the Hobby Dev - Free plan and click 'Submit order form'

    ![Heroku Postgress Add on](/images-readme/heroku-postgress-addon.png)

3. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py ():

    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True
    
    DATABASE_URL = "This variable is automatically set when adding the Postgres Add on"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```
4. From this screen, copy the value of DATABASE_URL
5. After this go to your settings.py the lastlifemain directory and comment out the default database configuration and add:
    ```
    DATABASES = {
        'default': dj_database_url.parse('Put your DATABASE_URL here'))
    }
    ```
6. Migrate again with the following command
    ```
    python3 manage.py migrate
    ```


7. Create a superuser for the postgres database so you can have access to the django admin by setting up the credentials with the following command
    ```
    python3 manage.py createsuperuser
    ```

    --> Don't forget to login to the admin page and check the boxes 'Verified and primary"

8. Load the data into your newly created database by using the following command: 

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 


9. After migrations are complete, change database configurations to:
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```
This set up will allow your site to use Postgres in deployment and sqlite3 in development.


10. Make sure you have your requirements.txt file and your Procfile. In case you don't, follow the below steps:
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
11. The Procfile should contain the following line:
    ```
    web: gunicorn <project_name>.wsgi:application

    ```

12. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

13. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
14. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
15. Go back to HEROKU and click "Deploy" in the navigation. 
16. Scroll down to Deployment method and Select Github. 
17. Look for your repository and click connect. 
18. Under automatic deploys, click 'Enable automatic deploys'

19. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
20. In order to commit your changes to the branch, use git push to push your changes. 


21. Store your static files and media files on AWS. You can find more information about this on [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html). Alternatively, check out [this tutorial on Youtube from Amazon Web Services](https://youtube.com/watch?v=e6w9LwZJFIA). Very helpful!

22. Set up email service to send confirmation email and user verification email to the users. You can do this by following the next steps (Gmail only)

(Be aware that this migth be different for other providers or the process might have changed over time)

* Go to your email account and go to your account settings
* Under Security, scroll down to Signing in to Google and make sure 2 step verification is turned on
* Under the same heading (Signing in to Google) you will see the 'App passwords' option.
* Click on the option, select mail for the app and under device type select other and fill in 'Django'
* You will now get a password which you should copy and set it as a config variable in Heroku:

```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
```
* Go to your settings.py in casa_pedra_nobre directory and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```


## Credits

### Content

-   The bones of this project is based off of the Boutique Ado tutorial with various items adjusted, modified, added or removed to fit the theme of the site owners business. Other elements were drawn from Youtube tutorials and Slack and StackOverflow discussions with other developers.

### Media

-   All Images were sourced online from sources using creative commons licences or from royalty free sites like Pixabay, Stockvault and Pexels.

### Acknowledgements

-   My Mentor Simen "Eventyret_mentor" for continuous helpful feedback and getting my head back in the game when im like a lost sheep in the woods.

- A big thank you to the Slack community. There is great value in what people are doing there and coding is so much easier knowing im not the only one who finds it difficult or struggles with certain issues.

- A thanks to Chris Z. "ckz8780" for the very helpful tutorial of Boutique Ado. A lot of the work done on this project was heavily inspired by and learned from those videos. With them I have started to get a real good grip for MVC frameworks. 

- Shanika Wickramasinghe's article on [What’s an Example of Good E-Commerce Database Design?](https://resources.fabric.inc/blog/answers/ecommerce-database-design-example)

- A thank you to my family who have been very supportive on my coding journey.

- All the fine people on StackOverflow for providin both simple and complex solutions to a variety of coding problems.


