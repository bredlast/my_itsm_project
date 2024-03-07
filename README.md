# ITSM Flask App
This Flask application allows you to manage a simple IT service management (ITSM) system using a SQLite database. The system lets you create, update, delete, and view tickets.

# Prerequisites
Make sure you have the following installed:

# Python 3.x
Flask
Flask-SQLAlchemy
Running the Application
Save the code in a file named app.py.
Run the application with the following command:
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/ to access the home page.
Home Page
The home page displays a list of all the tickets in the system. You can click on a ticket to view its details or click on the "Update" or "Delete" button to modify or remove the ticket.

# Home Page

Adding a Ticket
To add a ticket, click on the "Add Ticket" button on the home page. This will take you to the add ticket page where you can enter the ticket's title, description, and status.

# Add Ticket Page

# Updating a Ticket
To update a ticket, click on the "Update" button on the home page. This will take you to the update ticket page where you can modify the ticket's title, description, and status.

# Update Ticket Page

# Deleting a Ticket
To delete a ticket, click on the "Delete" button on the home page. This will prompt you to confirm the deletion. Once you confirm, the ticket will be permanently removed from the system.

# Database Schema
The application uses a SQLite database with a single table named ticket. The table has the following columns:

id: the unique identifier of the ticket (primary key)
title: the title of the ticket (not null)
description: the description of the ticket (not null)
status: the status of the ticket (not null, default: 'open')
# Code Structure
The code is structured as follows:

app.py: the main Flask application file
