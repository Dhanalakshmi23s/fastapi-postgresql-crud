# fastapi-postgresql-crud
A simple and clean FastAPI CRUD application connected to a PostgreSQL database using SQLAlchemy — built in under an hour. This project demonstrates how to structure a basic RESTful API with full Create, Read, Update, and Delete functionality, along with modular routers and schema validation.
# 🚀 FastAPI PostgreSQL CRUD API

A simple and clean FastAPI CRUD application connected to a PostgreSQL database using SQLAlchemy — built in under an hour. This project demonstrates how to structure a RESTful API with modular routers, schema validation, and full Create, Read, Update, and Delete functionality.

---

## 📦 Tech Stack

- **FastAPI** – Web framework for building APIs with Python 3.7+
- **PostgreSQL** – Relational database
- **SQLAlchemy** – ORM to interact with the PostgreSQL database
- **Pydantic** – For data validation and serialization

---


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/fastapi-postgresql-crud.git
cd fastapi-postgresql-crud

```

2. Install dependencies
```bash
pip install -r requirements.txt
```
If you don’t have requirements.txt, run:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary

```
3. Set up PostgreSQL

Make sure PostgreSQL is installed and running. Then create a database and update the connection URL in database.py:
```bash
SQLALCHEMY_DATABASE_URL = 'postgresql://username:password@localhost/your_database'
```
4. Run the server
```bash
uvicorn main🔠 --reload
```

🧪 API Endpoints

Use Postman, Swagger UI (http://127.0.0.1:8000/docs), or curl to test these routes.
Method	Endpoint	Description
GET	/	Root message
GET	/hello/{name}	Greet by name
GET	/posts/	Get all posts
POST	/posts/	Create a new post
GET	/posts/{id}	Get a single post
DELETE	/posts/{id}	Delete a post
PUT	/posts/{id}	Update a post
💡 Sample JSON for Creating a Post

{
  "content": "This is a sample blog post.",
  "title": "My First Post",
  "id": 1
}


📌 To-Do / Next Steps

    Add user authentication with JWT

    Create user-post relationships

    Add environment variable support (python-dotenv)

    Write unit tests with pytest

    Deploy on Render, Railway, or Heroku

🙌 Acknowledgments

Thanks to the FastAPI docs and community for making it incredibly easy to build powerful APIs with Python!


---

Let me know if you want me to generate a `requirements.txt` or add `.env` handling next!
