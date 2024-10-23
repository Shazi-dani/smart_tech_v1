![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<img width="203" alt="Screenshot 2024-10-20 at 8 52 11 PM" src="https://github.com/user-attachments/assets/e80aa15f-e7c7-420c-a43d-f41005e5a2bf">
is my Final milestone project for my Level 5 Diploma in Web Application Development with the Code Institute.The project  was named as Smart Tech.I've created a full stack e-commerce website using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe as the payment processor & many more Features Like User friendly purchaces, Checkouts etc.Smart Tech is a full stack  B2C e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe as the payment processor & Email integration system.
The site can visible here  [Smart Tech]https://smart-tech-42a1ef4a43e4.herokuapp.com)
## Visit Website here




## Main Languages Used 

<img width="242" alt="Screenshot 2024-10-23 at 9 35 29 AM" src="https://github.com/user-attachments/assets/f94bf4c5-7669-4431-865e-9d0164d039de">
<img width="242" alt="Screenshot 2024-10-23 at 9 35 59 AM" src="https://github.com/user-attachments/assets/91f4eaa3-9ed6-4b35-a597-aa7e1ce53fe0">


## User Stories

|Story ID |AS A/AN |I WANT TO BE ABLE TO...|SO THAT I CAN...|
|---------|--------|-----------------------|----------------|
|<img width="28" alt="Screenshot 2024-10-11 at 8 09 32 AM" src="https://github.com/user-attachments/assets/e2612a7a-7a56-4e05-b371-5490b4dc0d7f">**Viewing & Navigation**|
|1|Any User|	Nevigate to Site or Home Screen| Get what i want or require| 
|2|Shopper/Buyer|View a list of products|	Select some to purchase|
|3|Shopper/Buyer|view Category Listing|Find specific items of my interested, without having to scroll through all products|
|4|Shopper/Buyer|Search By Typing Name of Product|Save my  Time| 
|5|Shopper/Buyer|Add Filers to Get Specific Offers|Save money| 
|6|Shopper/Buyer|View Items/ Products to Quickly identify deals & clearance or items  with  special offers|Take advantage of special savings on products I'd like to purchase|
|7|Shopper/Buyer|View individual product details|Identify the price, description, product rating, product image and available sizes.|
|8|Shopper/Buyer|View my wished/ Selected purchases|to view more detail about Product and pricing also ammend Quantity if needed|
|9|Shopper/Buyer|Easily view the total of my Ongoing purchases at any time|Avoid spending too much & Shipping Charges|
|10|Shopper/Buyer|View my product wish List|make purchase from this in future|
|11|Shopper/Buyer|View Cart / Bag |check that my concern things is in my Bag or CART|
|<img width="28" alt="Screenshot 2024-10-11 at 8 09 32 AM" src="https://github.com/user-attachments/assets/0d655526-7480-4390-8fca-4f338a4480e0">**Registration and User Accounts**|
|12|Site User|Easily register for an account|Have a personal account and be able to view my profile to check order details |
|13|Site User|Receive an email confirmation after registering	|Verify that my account registration was successful|
|14|Site User|Easily login or logout|To secure my personal account information|
|15|Site User|Easily recover my password |in case I forget it	Recover access to my account|
|16|Site User|Receive a confirmation email| verify| 
|17|Site User|Have a personalized user profile|View my personal order history and order confirmations, and save my payment information|
|<img width="28" alt="Screenshot 2024-10-11 at 8 09 32 AM" src="https://github.com/user-attachments/assets/8c86bda4-1a92-4796-897e-f64fc862e535">**Sorting and Searching**|
|18|Shopper/Buyer|Sort the list of available products|Easily identify the best rated, best priced and categorically sorted products|
|19|Shopper/Buyer|Sort a specific category of product	|Find the best-priced or best-rated product in a specific category, or sort the products in that category by name|
|20|Shopper/Buyer|Sort multiple categories of products simultaneously |	Find the best-priced or best-rated products across broad categories, such as "smart Phone" or "Tab"|
|21|Shopper/Buyer|Search for a product by name or description	|Find a specific product I'd like to purchase|
|22|Shopper/Buyer|Easily see what I've searched for and the number of results|Quickly decide whether the product I want is available or not|
|<img width="28" alt="Screenshot 2024-10-11 at 8 09 32 AM" src="https://github.com/user-attachments/assets/8c86bda4-1a92-4796-897e-f64fc862e535">**Purchasing and Checkouts**|
|23|Shopper/Buyer|Easily select the size and quantity of a product when purchasing it|Ensure I dont accidentally select the wrong product, quantity or size|
|24|Shopper/Buyer|View items in my bag /Cart to be purchased|Identify the total cost of my purchase and all items I will receive|
|25|Shopper/Buyer|Adjust the quantity of individual items in my bag or cart|Easily make changes to my purchase before checkout|
|26|Shopper/Buyer|Easily enter my payment information|Check out quickly and with no hassles|
|27|Shopper/Buyer|Feel my personal and payment information is safe and secure|Confidently provide the needed information to make a purchase|
|28|Shopper/Buyer|View an order detais for double confirmation|Recheck details & Verify that I haven't made any mistakes|
|29|Shopper/Buyer|Receive an email confirmation after checking out|Keep the confirmation of what I've purchased for my records|
|<img width="28" alt="Screenshot 2024-10-11 at 8 09 32 AM" src="https://github.com/user-attachments/assets/8c86bda4-1a92-4796-897e-f64fc862e535">**Admin and Store Management**|
|30|Store Owner/Admin|Add a product for sale|shopper can shop items to my store|
|31|Store Owner/Admin|Edit/update a product|Change product prices, descriptions, images, and other product criteria|
|32|Store Owner/Admin|Delete a product|Remove items that are no longer for sale|
|33|Store Owner/Admin|View all kind of products|access to all in-stock & out-Stock products|
##  Entity Relationship Diagram (ERD)
### ERD Structure:
- **User (Authentication)**: To manage user credentials (username, email, password).
- **UserProfile**: Holds customer-specific information such as full name, addresses, and phone number.
- **Category**: Categorizes products, now with fields like `name` and `friendly_name`.
- **Product**: Includes SKU, stock, price, image URL, and rating fields.
- **Order**: Contains information related to orders, including delivery cost, user profile link, and a payment identifier (e.g., Stripe PID).
- **OrderLineItem**: Tracks product quantities and total cost for each item in the order.
- **ContactForm**: Manages customer inquiries or messages.

<img width="1111" alt="Screenshot 2024-10-23 at 9 12 03 AM" src="https://github.com/user-attachments/assets/57424eda-3c2b-412b-bcc1-40f8cd8acd65">

## Design & Typography 
#### User Experience 


<img width="525" alt="Screenshot 2024-10-23 at 9 57 59 AM" src="https://github.com/user-attachments/assets/36c7b25a-a626-45f8-a812-9faf0fce9c2a">
<img width="404" alt="Screenshot 2024-10-23 at 9 48 30 AM" src="https://github.com/user-attachments/assets/4f49b8a2-29b4-488b-aab0-946373d187e4">
## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---
**June 18, 2024**
Happy coding!
