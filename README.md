# Sticky Notes App README

## Overview

The Sticky Notes App is a simple yet powerful application built with Django that allows users to create, read, update, and delete digital sticky notes. Each note can have a title, content, creation timestamp, and last modification timestamp. Users can easily navigate through their notes, edit them, or delete them as needed.

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

## Usage

Once the server is running, you can perform various operations such as creating, viewing, editing, and deleting notes through the web interface.

- To create a new note, click on the "Create a New Note" link on the main page.
- To view a list of all notes, simply visit the main page.
- To view the details of a specific note, click on the note's title from the list.
- To edit a note, click on the "Edit Note" link below the note's details.
- To delete a note, click on the "Delete Note" link below the note's details.

## Contributing

Contributions to the Sticky Notes App are welcome. Please feel free to submit pull requests or report issues through the GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
