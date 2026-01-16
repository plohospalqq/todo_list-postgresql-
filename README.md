# 📝 PostgreSQL ToDo App (Python)

A simple console-based ToDo application written in **Python** using
**PostgreSQL** and **psycopg2**. This project is intended for learning
backend basics: database connections, CRUD operations, and environment
configuration.

------------------------------------------------------------------------

## 🚀 Features

-   Connects to PostgreSQL using environment variables
-   Create tasks
-   Read (list) tasks
-   Update tasks
-   Delete tasks
-   Uses `DictCursor` for readable query results

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.12+
-   PostgreSQL
-   psycopg2
-   python-dotenv

------------------------------------------------------------------------

## 📦 Installation

### 1. Clone the project

``` bash
git clone <your-repo-url>
cd postgresql-start
```

### 2. Create virtual environment

``` bash
python3 -m venv postgresql-venv
source postgresql-venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install psycopg2-binary python-dotenv
```

------------------------------------------------------------------------

## ⚙️ Environment Variables

Create a `.env` file in the project root:

    DB_HOST=localhost
    DB_USER=postgres
    DB_PASSWORD=your_password
    DB_PORT=5432
    DB_NAME=todo_list

------------------------------------------------------------------------

## 🗄 Database Setup

Example table schema:

``` sql
CREATE TABLE todo_list (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT
);
```

------------------------------------------------------------------------

## ▶️ Usage

``` python
user = UserToDo()

user.create_task("Buy milk", "2 liters of milk")
user.show_tasks()
user.update_task(1, "Buy bread", "Whole grain")
user.delete_task(1)
```

------------------------------------------------------------------------

## ⚠️ Important Notes

-   The application will **stop immediately** if database connection
    fails
-   All SQL queries are parameterized (safe from SQL injection)
-   Connection and cursor are closed at the end of execution

------------------------------------------------------------------------

## 📚 Learning Goals

-   Practice PostgreSQL with Python
-   Understand CRUD operations
-   Learn safe SQL execution
-   Work with environment variables

------------------------------------------------------------------------

## 👨‍💻 Author

Georhii\
Junior Python Backend Developer (in progress 🚀)
