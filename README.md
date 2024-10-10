# Real Estate Flask Application

This project is a simple real estate web application built using Flask. It allows users to sign up, log in, and view property listings. The application also includes automatic insertion of dummy property data into a SQLite database upon the first run.

## Features
- User authentication (sign up, log in, log out)
- View property listings with details (price, location, type)
- Automatic insertion of dummy data on the first run
- Built with a responsive design

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python with Flask
- **Database:** SQLite
- **Dependencies:** Flask, Flask-JWT-Extended, Flask-SQLAlchemy, bcrypt

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/real_estate_project.git
   cd real_estate_project
2. Set up a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

  pip install -r requirements.txt
4. Run the Flask application:
  python app.py
  Access the application: Open your web browser and go to http://127.0.0.1:5000.

5.API Endpoints
POST /signup: Register a new user.
POST /login: Log in an existing user and receive a JWT token.
GET /properties: Get the list of properties (requires authentication).
