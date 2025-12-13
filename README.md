# crowdfunding_back_end

A repo to contain my She Codes Crowdfunding back end project

# Crowdfunding Back End

Chelsea Murphy

## Planning:

### Concept/Name

Book Bank is a crowdfunding platform dedicated exclusively to improving literacy outcomes. The platform connects donors who are passionate about education with individuals, schools, and community organisations seeking funding for books, reading programs, and literacy initiatives. Unlike general crowdfunding sites, Book Bank focuses solely on literacy, creating a trusted space where every campaign directly impacts someone's ability to read, learn, and thrive.

Inspired by Roald Dahl's Matilda, the platform features verified campaigns, transparent fund tracking, and impact reporting that shows donors exactly how their contributions made a difference. Campaign creators can promote specific campaigns, fund adult literacy courses, or launch community reading programs. Donors can browse by cause, making it easy to support causes that resonate personally.
Book Bank rallies the community celebrating milestones with each funded campaign, sharing stories of transformation and progress. 

Literacy isn’t just an academic skill — it’s a human right and a tool for freedom. It empowers people to understand the world, imagine a better one, and have the voice to help create it.

### Intended Audience/User Stories

As an Educator, School year level coordinator, Librarian or School Parents & Citizens Association (P&C) I want to create a campaign for books so my students can access diverse, engaging reading materials. Alternatively I want to launch a campaign to fund places in literacy programs.

As a donor, I want to see campaigns so I can support literacy efforts in my own community.

As a parent, I want to fundraise for my child's reading needs so they can access new, different or specialised learning materials.

As a community organiser (such as an Aged Care facility or hospital), I want to launch a campaign for books or literacy alinged products or programs to support commnunity members to have a range of books or tools to support the love of reading.

### Front End Pages/Functionality

Log In
    Log in
    Sign Up
    +/- Reset Password

Home page
    See a list of open fundraises
    +/- See past fundraises
    +/- Search
    +/- Filtering

User Profile
    See details of currently signed in User account details – name, password, email
    Change details on user account – edit name, password, email
    +/- Archive user account
    +/- View past pledges
    +/- View related fundraiser

Fundraiser
-	Title
-	Owner (User ID)
-	Image
-	Target amount to raise
-	Status: Open / Closed / Deleted
-	Date of fundraiser creation
-	+/- Set a planned close date?
-	+/- See total of pledges amount / progress to target
-	Pledge action
o	An amount
o	The fundraiser
o	The user (supporter)
o	Whether the pledge is anonymous or not
o	A comment with the pledge
-	Update (Close)

Pledge
-	Make a pledge (amount, comment, anonymous (optional))
+/- Make an anonymous pledge


### API Spec

| URL    | HTTP Method | Purpose                   | Request Body | Success Response Code | Authentication/Authorisation |
| ------ | ----------- | ------------------------- | ------------ | --------------------- | ---------------------------- |
| users/ | POST        | Create a new user account | Includes strings such as:`{"username": "Four_Test","email": "fourtest+4@gmail.com", "password": "password1"}` | 201 Created | Authentication - None Required |
| users/{id}/ | GET | Retrieve details of a specific user | No body | 200 OK | Authentication Required Bearer Token |
| api-token-auth/ | POST | Obtain authentication token | Includes strings such as `{"username": "Two_Test","password": "password"}` | 200 OK | Inherit from parent |
| fundraisers/ | GET | Retrieve a list of all fundriasers | No body | 200 OK | Authentication Inherit from Parent |
| fundraisers/{id}/ | GET | Retrieve detailed information about a specific fundraiser, including the pledges | No body | 200 OK | Authentication Inherit from parent |
| fundraisers/ | POST | Create a new fundraiser | The JSON object contains a string, integer and boolean, such as: `{"title": "Matila Wormwood's 8th Birthday" "goal": 100, "is_open": true,}` | 201 Created | Authentication Required Bearer Token
| pledges/ | POST | Create a new pledge | The JSON object contains a string, integer and boolean, such as: {`"title": "Ashgrove SS Prep Book Program (Ashgrove P&C)" "description": "The Ashgrove P&C is establishing a Prep Book Drive to expand the home readers available for our 2026 Prep year group. Join us to bring some fun new titles to our prep year classrooms.","goal": 500,"image": "http://via.placeholder.com/201.jpg","is_open": true, "date_created": "2025-13-06T09:50:25.656443Z"}` | 201 Created | Authentication Required Bearer Token
| pledges/ | GET | Obtain a list of pledges | No body | 200 OK | Inherit from Parent |
| pledges/{id}/ | PUT | Update a pledge | `{"amount": 90,"comment": "Hey, it's Tuesday 2DEC!","anonymous": true,"fundraiser": 2}` | 200 OK | Authentication Bearer Token

### DB Schema

![DB Schema](<DB Schema.png>)

### Examples
![GET method example](<GET method Example.png>)![POST method example](<POST method Example.png>)![POST emthod example (Pledge)](<POST method Example (Pledge).png>)![User Token Example](<User Token Example.png>)!

### New User
https://book-bank-19bc3f3758c8.herokuapp.com/users/
The JSON object contains strings: `{"username": "Four_Test","email": "fourtest+4@gmail.com", "password": "password1"}`
![POST method - New User](<POST method - New User.png>)!

### New Fundraiser
https://book-bank-19bc3f3758c8.herokuapp.com/fundraisers/
The JSON object contains a string, integer and boolean, such as: `{"title": "Matila Wormwood's 8th Birthday" "goal": 100, "is_open": true,}`
![POST method - New fundraiser](<POST method - New fundraiser.png>)!