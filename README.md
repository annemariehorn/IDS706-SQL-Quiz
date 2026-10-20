# IDS706 SQL Practice Quiz

A 20-point interactive SQL quiz built with Streamlit, PostgreSQL, and Supabase for IDS706: Data Engineering Systems.

## Live Application

[Open the SQL Practice Quiz](https://ids706-sql-quiz-myhp2pmt25fwtcsnxopr2.streamlit.app)

A test account is required to sign in and access the quiz.

## Features

- Five SQL questions worth 4 points each (20 points total)
- Supabase email/password authentication
- SQL hints and expected answers
- Live SQL execution against a hosted PostgreSQL database
- Read-only database access for SQL execution
- Save and update student answers
- Row Level Security (RLS) for saved answers
- Parameterized SQL queries using psycopg2
- Database-triggered audit log for answer changes
- GitHub Actions CI workflow

## Technologies

- Python
- Streamlit
- Supabase / PostgreSQL
- psycopg2
- pandas
- GitHub Actions

## How to Use

1. Open the live application.
2. Sign in with an authorized test account.
3. Read each SQL question and enter a query.
4. Click **Run SQL** to execute the query and view the results.
5. Click **Save Answer** to save or update your response.
6. Use the **Show Hint** and **Show Expected Answer** sections for guidance.

### Parameterized SQL

The application supports parameterized SQL queries using psycopg2. To use this feature, include `%s` as a placeholder in your query and enter the corresponding value in the SQL parameters field.

For example:

```sql
SELECT * FROM students WHERE grade > %s;
```

Enter `90` in the SQL parameters field, then click **Run SQL**. The application will return students whose grades are above 90.

Parameters are passed separately from the SQL query rather than inserted directly into the query string.

## Setup and Configuration

### 1. Clone the Repository

```bash
git clone https://github.com/annemariehorn/IDS706-SQL-Quiz.git
cd IDS706-SQL-Quiz
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Supabase

The application uses a Supabase project with a hosted PostgreSQL database.

The database includes:

- `students` — Sample student records used for SQL questions
- `quiz_answers` — SQL answers saved by authenticated users
- `quiz_audit_log` — Records inserts and updates to saved answers

Supabase Authentication manages student login accounts.

Row Level Security (RLS) restricts access to saved answers, and a database trigger automatically records answer changes in the audit log.

A restricted PostgreSQL role is used to execute student SQL queries with read-only permissions.

### 4. Configure Streamlit Secrets

The application requires Supabase authentication credentials and PostgreSQL connection details.

For local development, create a `.streamlit/secrets.toml` file with the following configuration:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_publishable_or_anon_key"

DB_HOST = "your_postgresql_host"
DB_PORT = 5432
DB_NAME = "postgres"
DB_USER = "your_read_only_database_user"
DB_PASSWORD = "your_database_password"
DB_SSLMODE = "require"
```

Replace the placeholder values with credentials from your own Supabase project.

Do not commit `secrets.toml` or database passwords to GitHub.

For the deployed application, these values are configured in Streamlit Community Cloud under the application's Secrets settings.

### 5. Run the Application

Start the Streamlit application locally:

```bash
streamlit run app.py
```

Open the local URL provided by Streamlit and sign in with an authorized Supabase account.

The deployed version is hosted on Streamlit Community Cloud and is linked above.

## Security

- Database credentials are stored in Streamlit Secrets rather than in the repository.
- SQL queries execute through a restricted, read-only PostgreSQL role.
- Supabase authentication is required to access the quiz.
- Saved answers are protected by Row Level Security (RLS).
- A database trigger automatically records answer inserts and updates in an audit log.
- GitHub Actions uses a repository secret to store the Supabase project URL.

## Continuous Integration

GitHub Actions runs automatically when changes are pushed to the main branch. The workflow:

- Installs Python dependencies
- Checks Python syntax
- Verifies that the quiz contains five questions totaling 20 points
- Checks that the required Supabase configuration secret is present

The workflow can also be run manually from the GitHub Actions tab.

## Project Structure

- `app.py` — Streamlit application, authentication, SQL execution, and answer saving
- `questions.py` — Quiz questions, hints, and expected SQL
- `requirements.txt` — Python dependencies
- `.github/workflows/sql-quiz.yml` — GitHub Actions CI workflow
- `.gitignore` — Files excluded from version control
