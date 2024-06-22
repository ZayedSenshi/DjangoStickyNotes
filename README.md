# Sticky Notes App README :notebook_with_decorative_cover:

## Table of Contents :orange_book:

### Introduction
- **Overview/Description**

### Key Sections
- **Features**
    - Note Creation
    - Note Listing
    - Note Detail
    - Note Editing
    - Note Deletion
    - User Interface

- **Getting Started**
    - **Installation**
        - Prerequisites
        - Setup Steps
    - **Usage**

- **Contributing**


### Additional Resources
- **Credits**
    - Acknowledgments and Thanks

## Overview/Description

The Sticky Notes App is a straightforward yet impactful application developed with Django, enabling users to create, read, update, and delete digital sticky notes. Each note includes a title, content, creation timestamp, and last modification timestamp, facilitating easy navigation, editing, and deletion of notes. Understanding and implementing CRUD operations in web development, as demonstrated by the Sticky Notes App, is vital because it lays the groundwork for most web applications' functionality. It enhances problem-solving skills, accelerates development processes, and ensures security and scalability, making it a cornerstone of effective web development. Learning how to utilise the Django framework has been important because it equips you with the skills to develop efficient, scalable, and secure web applications quickly and cost-effectively. It opens up opportunities for career advancement and offers a solid foundation for further exploration in web development. 


## Features

- **Note Creation**: Users can add new notes with titles and contents.
- **Note Listing**: View a list of all notes, including a brief summary of each note's content.
- **Note Detail**: Access detailed information about a specific note, including its full content and timestamps.
- **Note Editing**: Update the title and content of existing notes.
- **Note Deletion**: Remove notes permanently from the database.
- **User Interface**: A clean and intuitive interface for managing notes, with options to create, edit, delete, and view notes.

## Getting Started

To run this application locally, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. You will also need to install Django and other required packages.

bash pip install django djangorestframework


### Setup

1. **Clone the Repository or Download Project Files**
   
2. **Navigate to the Project Directory**

3. **Create a Virtual Environment and Activate It**

bash python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate


4. **Install Required Packages Listed in `requirements.txt`**

bash pip install -r requirements.txt


5. **Run Migrations to Set Up the Database Schema**

bash python manage.py migrate


6. **Start the Development Server**

bash python manage.py runserver


7. **Access the Application**

   Open your web browser and visit `http://127.0.0.1:8000/`.


8. **Create a superuser**

   If you want to access the Django admin interface, you can create a superuser account with the following command:

(Note: When creating a superuser the password field will remain blank while you are typing the password, Django is in    fact accepting your input.)

   python manage.py createsuperuser

   1. In Username add admin
   2. In email add your email example@email.com
   3. in passowrd type your password
   4. in password (again) retype your password

   Run migrations and start the server

   Open your web browser and visit `http://127.0.0.1:8000/`.
   To access the admin interface, visit 'http://127.0.0.1:8000/admin/'.

   The admin page will look like this:
   ![admin page](https://github.com/ZayedSenshi/codingTasks/blob/master/Screenshots/Django%20admin.png)

   You can also create users by clicking on 'Users' under the 'Authentication and Authorization' heading: 
    ![admin users](https://github.com/ZayedSenshi/codingTasks/blob/master/Screenshots/admin_users.png)


## Usage

Once the server is running, you can perform various operations such as creating, viewing, editing, and deleting notes through the web interface.
   Open your web browser and visit `http://127.0.0.1:8000/`.


- To create a new note, click on the "Create a New Note" link on the main page. Your screen should now look like this: 
  ![create note](https://github.com/ZayedSenshi/codingTasks/blob/master/Screenshots/note_create.png)

- To view a list of all notes, simply visit the main page. By default, `http://127.0.0.1:8000/` will take you to this page. Alternatively, when creating or editing a note, you can navigate back to this page by clicking the hyperlink 'Back to Notes list' It should look like this:
  ![list note](https://github.com/ZayedSenshi/codingTasks/blob/master/Screenshots/note_list.png)

- To view the details of a specific note, click on the note's title from the list. It will look like this: 
  ![view note](https://github.com/ZayedSenshi/codingTasks/blob/master/Screenshots/note_detail.png)

- To edit a note, click on the "Edit Note" link below the note's details.
- To delete a note, click on the "Delete Note" link below the note's details.

## Contributing

Contributions to the Sticky Notes App are welcome. Please feel free to submit pull requests or report issues through the GitHub repository.


## Credits

This project was developed by Simon Mills

