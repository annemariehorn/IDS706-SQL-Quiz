# IDS706 SQL Practice Quiz

A 20-point interactive SQL quiz built with Streamlit, PostgreSQL, and Supabase for IDS706: Data Engineering Systems.

## Live Application

[Open the SQL Practice Quiz](https://ids706-sql-quiz-myhp2pmt25fwtcsnxopr2.streamlit.app)

## Features

- Five SQL questions worth 4 points each (20 points total)
- Supabase email/password authentication
- SQL hints and expected answers
- Live SQL execution against a hosted PostgreSQL database
- Read-only database access for SQL execution
- Save and update student answers
- Row Level Security (RLS) for saved answers
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
5. Click **Save Answer** to save your response.

## Security

- Database credentials are stored in Streamlit Secrets, not in the repository.
- SQL queries run through a restricted, read-only PostgreSQL role.
- Supabase authentication is required to access the quiz.
- Saved answers are protected by Row Level Security.
- An audit trigger records answer inserts and updates.

## Continuous Integration

GitHub Actions automatically installs dependencies, checks Python syntax, and validates the quiz configuration.

The workflow uses a GitHub repository secret for the Supabase project URL.

## Project Structure

- `app.py` — Streamlit application
- `questions.py` — Quiz questions, hints, and expected SQL
- `requirements.txt` — Python dependencies
- `.github/workflows/sql-quiz.yml` — GitHub Actions workflow
