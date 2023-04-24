# Edu Smart

This application is designed to manage schools, users, and grades with different user roles and functionalities.

## User Roles

1. Super Admin
2. Staff
3. Student

## Features

### Dashboard

The dashboard provides an overview of the application's data and statistics.

### Schools

Manage the creation and updating of schools within the application.

### Users

Manage the creation and updating of users with different roles (Super Admin, Staff, and Student).

### Grades

View and manage student grades.

## Role-Based Functionalities

### 1. Super Admin

- Create and update schools and users
- Edit their own profile

### 2. Staff

- Create and update users (cannot create a Super Admin)
- Edit their own profile

### 3. Student

- Edit their own profile
- View their grades (hardcoded data)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Pre-requisites

What things you need to install the software and how to install them:

- Node.js (https://nodejs.org)
- PostgreSQL (https://postgresapp.com)
- pgAdmin 4 (https://www.pgadmin.org/download/)

### Client Server Setup

Follow these steps to set up the client server:

1. Navigate to the `edu-ui` directory:

   ```
   cd edu-ui
   ```

2. Install the required packages:

   ```
   npm install
   ```

3. Start the server:

   ```
   npm start
   ```

   Make sure there is no restriction on port 3000 on your machine. This will open the UI in your browser.

### Database Setup

Follow these steps to set up the database:

1. Install and run PostgreSQL from https://postgresapp.com/

2. Install pgAdmin 4 from https://www.pgadmin.org/download/

3. Create a master password and database. You can use pgAdmin tools to create this.

4. Update the password, username, and database details in `edu_be/settings.py` in the database section.

### Python Backend Code Setup

Follow these steps to set up the Python backend code after completing the database setup:

1. Install virtualenv:

   ```
   pip3 install virtualenv
   ```

2. Create a virtual environment:

   ```
   pip3 virtualenv .env
   ```

3. Activate the virtual environment:

   ```
   pip3 source .env/bin/activate
   ```

4. Install the required packages:

   ```
   pip3 install -r requirements.txt
   ```

5. Run migrations:

   ```
   python3 manage.py migrate
   ```

6. Start the server:

   ```
   python3 manage.py runserver
   ```

7. Create Super Admin user , run the following in pgAdmin

   ```
   INSERT INTO public.users_users(
   	name, email, phone, role, password, "schoolId_id")
   	VALUES ('TestUser', 'TestUser@gmail.com','111111111', 'Super Admin', 'Test@1234', null);
   ```

## Built With

- [React](https://reactjs.org/) - The web framework used
- [TypeScript](https://www.typescriptlang.org)
- [MUI](httos://mui.com) - The ui component library
- [Django](https://www.djangoproject.com/) - The backend framework used
- [PostgreSQL](https://www.postgresql.org/) - The database used
