E-commerce API 🛒

A RESTful e-commerce backend API built with Python and FastAPI.

This project demonstrates backend development fundamentals including API routing, database integration, CRUD operations, data validation, and structured application development.

🚀 Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- REST API
- Git & GitHub

✨ Features

- Create products
- Retrieve products
- Update products
- Delete products
- Database integration
- API request validation
- Interactive API documentation with Swagger UI

📁 Project Structure

ecommerce-api/
│
├── app/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/Brolyne-Otieno/ecommerce-api.git

Enter the project directory:

cd ecommerce-api

Create a virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

▶️ Running the API

Start the FastAPI server:

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

📖 API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs

FastAPI's Swagger UI allows you to interact with and test the API endpoints directly from your browser.

🎯 What I Learned

Through this project, I practiced:

- Building REST APIs with FastAPI
- Structuring a backend application
- Working with SQLAlchemy
- Connecting an API to a database
- Implementing CRUD operations
- Validating API requests
- Using Git and GitHub for version control

👨‍💻 Author

Brolyne Otieno

GitHub: "Brolyne-Otieno" (https://github.com/Brolyne-Otieno)

Email: brolynebrin@gmail.com
