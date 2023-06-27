# **_EbinNaturals - Project Portfolio 5 - Django Full Stack Framework_**
* ## Introduction

   EbinNaturals is a fictional B2C e-commerce store that is  designed and implemented
   with Django python web framework, HTML, CSS and some Javascript. 
   It specialises in selling beauty products to consumers online. 
   However, it has to be noted that this site is for educational use only.

   Link to deployed site can be found [Here](https://ebinnaturals.herokuapp.com/)

* ## Showcase
![Home page](static/images/home_mockup.png)

# Contents

* [**Strategy**](<#strategy>)
* [**Colour Scheme**](<#colour-scheme>)
* [**User Experience UX**](<#user-experience-ux>)
    *  [Database](<#database>)
    *  [Design](<#design>)
    *  [Ecommerce type](<#Ecommerce>)
  
* [**Features**](<#features>)
    * [**Home**](<#navigation-menu>)
         * [Home](<#home>)
         * [Navigation Menu](<#navigation-menu>)
         * [Log In](<#log-in>)
         * [Contact](<#contact>)
         * [Footer](<#footer>)
    * [**Future Features**](<#future-features>)
         * [Testimonials](<#testimonials>)
         * [Latest News](<#latest-news>)
         * [Newsletter](<#latest-news>)
* [**Technologies Used**](<#technologies-used>)
* [**Manual and Automated Testing**](<#manaual and automated testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgments**](<#acknowledgements>)


* ### Strategy
      EbinNaturals is a B2C type of e-commerce business. Due to pressure of life from work and family, 
      people have opted for online shopping. EbinNaturals aims to offer flexible online shopping to 
      its customers by availing them to natural readymade homemade recipes that saves them time.

* ### Colour Scheme
      The colour scheme eventually chosen is one based on a green, black and white. 
      This colour scheme gives off a earthly, warm and happy feeling to the website.

![Colour Palette image](static/images/ebin_colorpalette.png)


# UX
## User stories
* ### As Admin
      * As admin I can manage user's accounts so that 
         I can make any required changes to them if needed
      * As admin I can manage products so that I can
          create,edit, update or delete products when necessary
      * As admin I can view created orders so that 
         I can fullfill the orders or amend if needed
      * As admin I can delete  comments so that
          I can remove them if I nolonger feel they are still necessary or needed
      * As admin I can view messages sent via contact form so that I can act upon them
      * As admin I can manage the blog content so 
         that I can make amendments if needed
      * As admin I can manage the business social media 
         profiles so that i can advertise my business.
      * As admin I can create, edit and delete comments.

* ### As a site user
      * As a site user I can easily register an  account
          so that I can have a personal account
      * As a site user I can login in my account
          so that I can view my order history
      * As a site user I can easily login and logout 
         so that I can I can access my personal information.
      * As a site user I can easily recover my password 
         if I forget so that I can recover access to my account.
      * As a site user I can receive an email confirmation 
         after registering so that I can verify that my account registration was successful.
      * As a site user I can have a peronalized user profile 
         so that I can view my perosnal order history and 
            order confirmations and save my perosnal information.
      * As a site user I can search for products by name or 
         description so that I can find the best rated products in a specific category.
      * As a site user I can sort multiple categories of       
        products simultaneously so that I can find the best rated across broad categories.
      * As a shopper I can view list of products 
         so that I can select the one to purchase
      * As a shopper I can look at product details so
          that I can view the price and other product details.
      * As a site user I can view the contents of my 
         shopping bag so that I can be able to make any adjustments.
      * As a site user I can view the total of my purchase 
         so that I can avoid spending too much.
      * As a site user I can update my bag by adding more or 
         remove products so that I can decide on the number of products I intend to buy.
      * As a site user I can identify deals and clearance 
         so that I can take advantage of special savings on products.
      * As a site user I can view my order summary 
         so that I can verify it before confirming
      * As a site user I can easily select the quantity of a product 
      so that I can ensure I select the right quantity.
      * As a site user I can checkout securely so 
         that I can I maintain the level of trust on the site
      * As a site user I can view blog posts
         so that I can select which posts to view.
      * As a site user I can view all posts so that I can 
         decide what I may be interested in reading.
      * As a site user I can create, read , update or  
         delete comments on a blog post.
      * As a site user I can use the contact form
          so that I can contact the site owners.
      * As a site user/shopper I can contact the business 
         through their social media profiles.
      * As a site user I can sign up to newsletter 
         so that I can keep updated on the latest news.
      


* ### Database
      I created a a sketch of the database diagram.
       Due to the site's free plan, I can only create 15 tables.
   
 Link to database diagram can be found [Here](https://drawsql.app/teams/gbemisola-ajebeku/diagrams/ebin)


* ### Design
      Before I wrote any code for this site, I had to pin point a simple design of
       what I wanted my site to look like by using wireframes.
<details>
<summary>Click here to view Wireframes:</summary>

  ![](static/images/HomePage.png)
  ![](static/images/product_detail_page.png)
  ![](static/images/product_listing_page.png)
  ![](static/images/Bag.png)
  ![](static/images/checkout_page.png)
  ![](static/images/Register.png)
  ![](static/images/Blog.png)
  ![](static/images/contactus_copy.png)
  
  </details>


</details>

* ### E-commerce type

      EbinNaturals is an e-commerce B2C online retail store that sells directly to customers. 
      The functionality on this site for a customer is the ability to make purchases 
      swiflty and efficiently. 
      For the owners, the goal is to archieve CRUD products and other functionalities.


* ### Marketing
      Though there are a lot of marketing techniques for businesses, 
      EbiinNaturals decided to first use the cheaper way, 
      that is facebook to drive its' content and engage with customers.
   Visit our facebook page [Here](https://www.facebook.com/EbinNaturals/)



## Features

* ### Home Page

     The website is designed to be welcoming and easy to use. 
     It features a nav bar and nav links. It starts with the name of the website on the top left,
     search field in the midddle, my account and shopping bag to the right, 
     followed by a navigation menu links,free shipping threshold text and footer. 
     All these appear on every page on the site. Also,  found on home page is  a hero
      image accompanied by a hero text, and a shop now button beneath it.

![home](static/images/welcome_page.png)


* ### The Nav bar
      This nav bar can be seen on all pages of the website. 
![header](static/images/home-nav.png)


* ### Shop Now
      This call to action button takes the user to the list of all products.
![shopnow](static/images/shop_now.png)


* ### Products
      This shows the list of all the products and their titles, prices and ratings.
![products](static/images/products_home.png)


* ### Sort by price,rating, category
      This shows the list of the products sorting the user can go through.
 ![sorting](static/images/product_sort.png)


* ### Product detail and add to bag

      Each product on site has a detailed information in form of a name,
       price,image, description and its category. 
      The user is displayed with a quantity input box to select the quantity they n
      need to add to the shopping bag either increasing or decreasing. 
      They have an option to go back to products by clicking the keep shopping button. 
       Each time a user add a product to the bag they get a popup notification that alerts them of that action.

   ![detail](static/images/product_detail.png)
   ![bagmessage](static/images/bag_screenshot.png)


* ### The shopping bag

      Consists of the price, quantity of each item and sub total. 
      The User have an option to update their bag or remove some items from bag. 
      They can easily go back to products by clicking keep shopping or go to checkout.

   ![bag](static/images/shop_bag.png)

* ### Checkout

      On the left side of the checkout is where user puts their information,
       and on the right side is a summary of their order that is the total, the delivery.

   ![checkout](static/images/checkout-bag.png)

      User have the option to save their information to a profile. 
      Users will need to input the card number for payment. 
      They still have an option to adjust the bag at this point 
      by clicking the adjust bag, or then completing the order.

   ![checkout bottom](static/images/checkout_bottom.png)


<!-- * ### Checkout success -->
      After completing an order, users receive an 
      order confirmation with their details including order number.

   ![checkout success](static/images/checkout_success.png)

* ### Register/Sign up
      On the right side of the home page, for the first time user
       they will need to register their account to enjoy most of the site
        benefits such as saving their orders, commenting on blogs. 
        When registering users are asked their username, email and password

* ### Sign in

      Registered users would need to sign in when they visit the site again. 
      They will be asked to enter their username and password. 
      The Remember me option is also available making life easier for returning users. 
      It's users need to reset their password, a forgot password is also available.


* ### Logout
      Users are able to protect their account by logging out of the site.


* ### Footer

      The footer appears on all pages of the site, 
      it contains the newsletter sign up, about us, privacy policy and social media links.

![footer](static/images/footer.jpg)

* ### Newsletter

Users can subscribe via their email to receive news, 
offers and deals straight into their inbox.
![newsletter](static/images/newsletter_signup.png)


* ### Privacy policy

![privacy policy](static/images/privacy_policy.png)


* ### Blog

      Users can view all the blog articles and select 
      which one to read by clicking the image
    ![blog](static/images/blogpost.png)

* ### Blog detail

   Only logged in users are permitted to comment on
    articles in as much as they can read other comments written by other users

   After logging in they can leave a comment on any blog article

### Blog management

* ### Add blog

      Super users are the creators of the blog articles.
       To add a new blog they have to put title, slug, body and image and then save.

![add blog](static/images/add_blog.png)

* ### Edit blog

      Super users can also edit the blog and update the changes
![edit blog](static/images/edit_blog.png)

* ### Delete post

      If the post is no longer serving its purposes, super users can also delete it
![delete blog](static/images/deletepost.jpg)

## Add comment

Logged-in Users/Superusers have the ability to add comments.

## Edit comment

Superusers/Logged-in Users/ have the ability to edit comments.

## Delete comment
Superusers/Logged-in Users have the ability to delete comments.


# Contact us

A contact us page is available for users who need to get in touch with the store owners. 
They have to put their name, email, the topic and the overall message before sending.
![contact](static/images/contact_form.png)

## My Profile

  The my profile page displays a user's saved 
   contact infomation and their order history.


# 404 page

 A 404 page is also available to handle navigation errors with a
 home link button to take them back to the home page.
![error handling](static/images/404.png)

### Future features

* Users replying to other blog comments.
* Blog likes.
* Additional blog posts.

# Web marketing

* ### Email marketing

      The free version of mailchimp was chosen with the current status of the business.
    Each user that signs up is added to the weekly newsletter and they might 
    turn out to be future customers henceforth low cost to drive sales.

* ### Search engine optimization

      SEO keywords

* ### Social media marketing

      A facebook page was created to build community from the target market. 
      Facebook is free and it also takes little to no time to set up.
      also, it has so many users whom a business can strive to maintain a certain relationship,
       create content and connect with a target audience.

   ![facebook](static/images/facebook_img.png)

## Technologies
### Languages

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

* [Javascript](https://www.javascript.com/)

* [Python](https://www.python.org/)

### Frameworks, programs and libraries used

* [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that 
   encourages rapid development and clean, pragmatic design.

* [Bootstrap4](https://getbootstrap.com/) - A css framework

* [Gitpod](https://www.gitpod.io/) - Gitpod was used as an IDE

* [Github](https://github.com/) - I used Github to store all the data of my project after pushing it

* [Heroku](https://www.heroku.com/) - is a cloud platform service  I used to deploy and host the project

* [ElephantSQL](https://www.elephantsql.com/) - used as a database for the project

* [Font Awesome](https://fontawesome.com/) - Was used to add icons for my social media links.

* [PEP8ci](https://pep8ci.herokuapp.com/) - I used it to validate python code

* [dbdiagram](https://dbdiagram.io/home) - was used to draw the database schema

* [Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

* [AWS](https://aws.amazon.com/s3/) - for  object storage through a web service interface.

* [Pexels](https://www.pexels.com/) - images used for the project

* 


# Testing
## Manual Testing
 | Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| EBINNATURALS  | Selecting logo on homepage |  directs user back to homepage |  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Search no results | No search | Entering a no results search returns error message and shows all products  |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant pages |  Pass |
| All products  | Selecting all products |  directs user to all products |  Pass |
| Back to top | Back to top arrow | Select the arrow box on the products page brings the user back to the top of the page  |  Pass |
| Sort By  | Selecting the filter Sort |  successfully sort by price, name and category options |  Pass |
| Shop Now button  | Selecting Shop Now button |  directs user to all  products page |  Pass |
| Adjust quantity | Plus or minus button |  adjust the quantity of product |  Pass |
| Add to bag | Adding to bag | successfully add products to bag| Pass |
| Keep Shopping | Keep shopping button |  directs user back to all products page  |  Pass |
| Delete from bag | deleting products from bag | successfully delete products from bag| Pass |
| Shopping bag  | Shows the added products and total |  directs user to checkout page |  Pass |
| Secure Checkout button  | Using the secure checkout button |  directs user to checkout form and payment details |  Pass |
| Sign up for our newsletter | selecting Sign up for our newsletter |  directs user Sign up for our newsletter page |  Pass |
| Privacy policy | Selecting privacy policy |  directs user to privacy policy|  Pass |
| facebook icon | Selecting  facebook icon |  directs user to facebook page |  Pass |
| Special offers | Selecting all specials |  directs user to all special offers |  Pass |
| Blog | Selecting blog |  directs user to blog page |  Pass |
| Blog detail | Selecting Blog detail |  directs user to blog detail |  Pass |
| Leave a Comment when signed in | Submitting comment|  successfully submit and display comment |  Pass |
| Edit a Comment when signed in | Editing comment|  successfully submit and edit comment |  Pass |
| Delete a Comment when signed in | Deleting comment|  successfully deleted comment |  Pass |
| Add blog | Adding a new blog | successfully add new blog to blog page  |  Pass |
| As Admin edit blog | editing blog|  successfully edited the blog |  Pass |
| As Admin Delete Comment | Deleting comment|  successfully remove comment |  Pass |
| Contact | Selecting Contact | directs user to contact page  |  Pass |
| Contact form submission | submitting contact form | successfully sends submit form and can seen be in admin |  Pass |
| My account | Selecting my account as admin | displays dropdown menu unique to admin apart from profile and logout  |  Pass |
| Add product | Adding a new product| successfully add new product to products page  |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| As Admin edit product | editing product |  successfully edited the product |  Pass |
| As Admin Delete product | Deleting product|  successfully remove product |  Pass |
| Register | Register for an account | selecting Register in my account directs user signup page |  Pass |
| Register | Registering as a new user | Registering as a new user form works |  Pass |
| Login | Login to an account | selecting Login in my account directs user to Login page |  Pass |
| Login | Login to an account | login-in as a new user form works |  Pass |
| Login as admin| Login to as admin gives access to blog/product management | login-in as a new user form works |  Pass |
| Logout | message shown | Logging out message shown |  Pass |
| Newsletter | Subscribe to newsletter|  successfully showed subscribed|  Pass |


## User story testing
### Admin
* As a admin I can manage users' accounts so that
    I can make any required changes to them if needed
   > Admin can manage user accounts from admin panels
* As a admin I can manage products so that I can add ,
    update or delete products when necessary
   > Admin can add, delete and update products on the site
* As a admin I can view created orders so that I can full fill the orders or amend if needed.
   > Admin can view orders in admin panel
* As a Admin I can delete any of comments so that
    I can remove them if I nolonger feel they are still necessary or needed.
   > Only admin can delete comments 
* As a Admin I can view messages sent via contact form so that I can act upon them
   > Admin can view send messages in the admin panel
* As an admin I can manage the blog content so that I can make amendments if needed
   > Admin can add, edit or delete blogs via blog management. only accessible to admin

## User story testing
### User
* As a site user I can create or edit my account so that I can update my details accordingly
   > A user can create an account using register and update on my profile
* As a site user I can login in my account so that I can view my order history
   > Logged in user can view order history if they made a purchase before
* As a site user I can search for products so that I can find specific products
   > I made sure users can search for what they want using search bar
* As a site user I can sort products on criteria
 such as price and category so that I can I have a method of ordering the products
   > I made products to be filtered by 
   price or category for users to choose how they want to view products as I prefer
* As a site user I can browse through products 
so that I can decide what I may be interested in buying
   > I made the site such that its easy to browse through all products so they see what to order
* As a site user I can look at product details so that I can decide if I want to purchase it
   > Each product has a  detailed description so users understands more of it
* As a site user I can easily add products 
I want to purchase to a basket so that I can decide whether to purchase or not
   > Users can easily add products to bag
* As a site user I can view the contents of my shopping basket 
   so that I can be able to make any adjustments
   > User can view bag contents by clicking the bag itself
* As a site user I can update my bag by adding more or remove products 
   so that I can decide on the number of products I intend to buy
   > User can update the bag to a quantity they want or remove everything entirely.
* As a site user I can view my order summary so that I can verify it before confirming.
   > From secure checkout, users can verify their order summary before buying
* As a site user I can checkout securely so that I can I 
   maintain the level of trust on the site.
   > I made sure users have secure checkout when completeing a purchase
* As a site user I can view  posts so that I can select which posts to view.
   > Blog posts are clear and easy to see so to select which to view
* As a site user I can view all posts so that I can decide what
 I may be interested in reading.
   > Users can easily choose which one to read
* As a site user I can create,edit,update or delete comment to the
   blog posts so that I can express my opinion to the post.
   > I made the site such that signed in user can create,edit,update 
      or delete comment on blog posts.
* As a site user I can use the contact form so that I can contact the site owners.
  > By using the contact form, user can send messages to the site owners.
* As a site user I can sign up to newsletter so that I can keep updated on the latest news.
  > By going to sign up newsletter on the footer, 
   users can easily sign up to receive latest news.

## Functionality testing

Throughout developing this site, I have been using Chrome, and chrome dev tools to help with debugging issues. 
Testing responsiveness was done using chrome emulated devices.

## Compatibility testing

Chrome emulated devices, and hardware devices iphone 13, samsung A51 and samsung tablet E were used to test compatibility

##  HTML TEST
 <details>
  <summary>Click here for Lighthouse results</summary>
 Desktop

  ![Lighthouse_test](static/images/lighthouse_test.png)

Mobile

  ![Mobile](static/images/lighthouse_mobile.png)
 
  </details> 

  <details>
  <summary>Click here for HTML Markup results</summary>

   ![](static/images/htmlchecker_ebin.png)

  </details> 

## CSS JIGSAW
  <details>
  <summary>Click here for CSS results </summary>

  ![css_test](static/images/jigsaw_css.png)

  </details> 

### Python
[ Flake8 was used to test python code.

## Bugs

   For this project there were so many major bugs I encountered during the project development. 
   Some of them I ended up taking them to tutor support whom have been very helpful. 
   Also, my dear husband who is also a developer who helped me to resolve issues 
   that tutor support couldn't help with.

### Bug 1
   1.During development, product detail wasn't displaying beacause of erroneous template.
   Tutor support helped me in locating the erroneous template which was spelt wrongly.

![Bug1](static/images/Productdetail_bug.png)

### Bug 2

2. 
   While trying to copy recursively some templates I realized the command wasn't working,
   tutor support guided me in fixing it by giving me the right command.

![](static/images/Productdetail_bug.png)
 
 
### Bug 3

  3. While I was in the process of connecting django to S3 bucket I encountered 
  the issue of heroku configset:DISABLE_COLLECTSTATIC which prevented a successful deployment from django. 
  After several attempts I manually created a static file in the root directory, I manually uploaded in the S3 website.

### Bug 4
   4. I had this error "TypeError: __init__() got an unexpected keyword argument 'providing_args'" while trying to migrate the allauth app.
      I uninstalled django and reinstalled it, thereafter running python3 manage.py migrate which worked successfu



# Deployment

I developed this site on Gitpod, using git for version control. Then deployed to Heroku using the following steps

* Log in to [Heroku](https://id.heroku.com/login) or create an account

* Click New and Create New App

* I selected Europe as region.

* Click Create App button

I then went to create a database to connect to the new created app.

* Login to [ElephantSQL](https://www.elephantsql.com/)

* Create new instance

* Set up your plan - Give the plan a name and select Tiny Turtle free plan

* Select region button

* Select a data center near you. I selected EU-West-2(London)

* Click Review

* Click Create instance

* Return to elephantsql dashboard, click on database instance name

* In the url section, clicking the copy icon will copy the database url to the clipboard

* Go back to Heroku to your created app, go to Settings

* Add config var DATABASE-URL, and for the value, copy in your databse url from ElephantSQL. do not add quotation marks around your database

* In Gitpod install dj-database_url and psycopg2 to connect to your external database

* Update requirements.txt: pip freeze > requirements

* import dj_database_url in settings and update your database

* Migrate your database

* create a new superuser for your database and at this point your database is exposed do not commit it to github

* Install gunicorn and freeze into the requirements file

* Then create Procfile

* DISABLE_COLLECTSTATIC

* Commit and push to github

* On your app in Heroku go to Deploy and connect it to github and search your repository, click connect.

* Choose automatic or manual deploy. I chose manual. Click deploy branch

* When complete click View to open the deployed app

## From Github docs

### Forking 

* Open GitHub page that hosts the repository you wish to fork.
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning

* Open Go to the repository page on Github
* click on the green button that says "Code".
* You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
* Copy the URL under the HTTPS tab to clone using https.
* In a new window, and set the current directory to the one you want to contain the clone from.
* Type git clone and paste the URL copied from the GitHub page.
* The repository clone will now be created on your machine. 

## Credits

* Homepage banner image by Silvia from pixabay

* Images are from [Pixabay](https://pixabay.com/) , [Pexels](https://www.pexels.com/)

* Code Institute Botique Ado walkthrough and fourth project NaijaNetherlands

* I went through other student's project to get ideas pn their projects and check their readme but the one I used the most was from 
   Pauline Rugwevera project and MikeR94 Readme.

* Hello django code institute.

* [Stack overflow](https://stackoverflow.com/) for debugging issues.

* [Coolors](https://coolors.com) for generating color palette.


#### Blog content

* [Blog link](https://www.kitchen-concoctions.com/2012/05/avocado-banana-hair-mask/)

### Acknowledgement and support

* My very own lovely husband who supported me throughout this course, my mentor, tutor support and the slack community.



