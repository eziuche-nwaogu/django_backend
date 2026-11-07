Book Library API

A RESTful Book Library API built with Django and Django REST Framework (DRF). The application provides endpoints for managing books and authors, including creating, retrieving, updating, and deleting records.

The project uses PostgreSQL as its database and provides interactive API documentation through Swagger UI and ReDoc.

Features
Author Management: Create, retrieve, update, and delete authors.
Book Management: Create, retrieve, update, and delete books.
Database Relationships: Each book is associated with an author through a ForeignKey relationship.
Data Serialization: Uses Django REST Framework ModelSerializers to convert model instances into JSON representations and validate incoming data.
Custom Validation: Validates book titles and prevents certain invalid entries.
Unique ISBN: Each book must have a unique ISBN.
Interactive API Documentation: Swagger UI and ReDoc documentation.
PostgreSQL Database: Uses PostgreSQL for local development and production deployment.
Technologies Used
Python
Django
Django REST Framework
PostgreSQL
psycopg2-binary
drf-spectacular
Swagger UI
ReDoc
Gunicorn
WhiteNoise
Render
Git and GitHub
Project Structure
text
book_drf/
│
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── books/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── tests.py
│
├── book_library_main/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
├── build.sh
└── .gitignore

Database Models
Author

The Author model stores information about book authors.

Field	Data Type	Description
id	AutoField	Primary key
author_first_name	CharField	Author's first name
author_last_name	CharField	Author's last name
Book

The Book model stores information about books.

Field	Data Type	Description
id	AutoField	Primary key
book_title	CharField	Title of the book
book_author	ForeignKey	Associated author
book_published_date	DateField	Publication date
book_isbn	CharField	Unique ISBN (maximum 13 characters)
price	DecimalField	Book price
is_available	BooleanField	Availability status
created_at	DateTimeField	Automatically recorded creation date

Relationship: One author can have multiple books, while each book belongs to one author. Deleting an author also deletes their associated books because of on_delete=models.CASCADE.

API Endpoints

The API uses version 1, with the base URL:

text
/api/v1/

Books
HTTP Method	Endpoint	Description
GET	/api/v1/books/	Retrieve all books
POST	/api/v1/books/	Create a new book
GET	/api/v1/books/{id}/	Retrieve a specific book
PUT	/api/v1/books/{id}/	Update a specific book
DELETE	/api/v1/books/{id}/	Delete a specific book
Authors
HTTP Method	Endpoint	Description
GET	/api/v1/authors/	Retrieve all authors
POST	/api/v1/authors/	Create a new author
GET	/api/v1/authors/{id}/	Retrieve a specific author
PUT	/api/v1/authors/{id}/	Update a specific author
DELETE	/api/v1/authors/{id}/	Delete a specific author
API Documentation

Interactive API documentation is available through:

Swagger UI: /api/docs/
ReDoc: /api/redoc/
OpenAPI Schema: /api/schema/

The documentation allows developers to explore the available endpoints, inspect request formats, and test API operations.

Installation and Setup
1. Clone the repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd book_drf

2. Create a virtual environment
bash
python -m venv venv


Activate it:

Windows:

bash
venv\Scripts\activate


Linux/macOS:

bash
source venv/bin/activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root directory.

Add:

env
SECRET_KEY=your_django_secret_key
DEBUG=True

DATABASE_URL=postgresql://postgres:your_password@localhost:5432/your_database_name

ALLOWED_HOSTS=localhost,127.0.0.1


Replace the database credentials with your local PostgreSQL credentials.

Important: Never commit your .env file or expose your secret key and database credentials on GitHub.

5. Run database migrations
bash
python manage.py makemigrations
python manage.py migrate

6. Start the development server
bash
python manage.py runserver


The application will be available at:

text
http://127.0.0.1:8000/

Production Deployment

The application is deployed using Render.

Backend Hosting: Render
Database: Render PostgreSQL
Application Server: Gunicorn
Static Files: WhiteNoise

Production environment variables are configured through the Render dashboard rather than committed to the repository.

Validation

The BookSerializer includes custom validation for book titles:

Book titles cannot be empty.
Book titles must contain at least five characters.
Book titles cannot match the associated author's first or last name.

ISBN values must also be unique.

Future Improvements

Potential improvements for future versions include:

Search and filtering.
Pagination.
Authentication and permissions.
Partial updates using PATCH.
Automated API tests.
More advanced validation and error handling.
Author

Your Name

GitHub: YOUR_GITHUB_USERNAME