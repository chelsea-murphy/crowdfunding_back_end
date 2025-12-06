# crowdfunding_back_end

A repo to contain my She Codes Crowdfunding back end project

# Crowdfunding Back End

Chelsea Murphy

## Planning:

### Concept/Name

{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories

{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality

- {{ A page on the front end }}
  - {{ A list of dot-points showing functionality is available on this page }}
  - {{ etc }}
  - {{ etc }}
- {{ A second page available on the front end }}
  - {{ Another list of dot-points showing functionality }}
  - {{ etc }}

### API Spec

{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page.

It might look messy here in the PDF, but once it's rendered it looks very neat!

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL    | HTTP Method | Purpose                   | Request Body | Success Response Code | Authentication/Authorisation |
| ------ | ----------- | ------------------------- | ------------ | --------------------- | ---------------------------- |
| users/ | POST        | Create a new user account |

{
"username": "Four_Test",
"email": "fourtest+4@gmail.com",
"password": "password1"
} | 201 Created | Authentication - None Required |

| users/{id} | GET | Retrieve details of a specific user | No body | 200 OK | Authentication Required Bearer Token |
| api-token-auth/ | POST | Obtain authentication token | {
"username": "Two_Test",
"password": "password"
} | 200 OK | Inherit from parent |

| fundraisers/ | GET | Retrieve a list of all fundriasers | No body | 200 OK | Authentication Inherit from Parent |
| fundraisers/{id} | GET | Retrieve detailed information about a specific fundraiser, including the pledges | 200 OK | Authentication Inherit from parent |
| pledges/ | GET | Obtain a list of pledges | No body | 200 OK | Inherit from Parent |
| pledges/{id}/ | GET | Retrieve details of a specific pledge |
| pledges/{id}/ | PUT | Update a pledge | {
"amount": 90,
"comment": "Hey, it's Tuesday 2DEC!",
"anonymous": true,
"fundraiser": 2
} | 200 OK | Authentication Bearer Token

### DB Schema

![]( {{ ./relative/path/to/your/schema/image.png }} )
