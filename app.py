import streamlit as st
from supabase import create_client
from questions import questions
import psycopg2
import pandas as pd

st.set_page_config(
    page_title="SQL Quiz",
    page_icon="📚",
    layout="centered"
)

st.title("SQL Practice Quiz")
st.write("Students and Grades | 20 Points")

# Connect to Supabase
@st.cache_resource
def get_supabase():
    return create_client(
        st.secrets["SUPABASE_URL"],
        st.secrets["SUPABASE_KEY"]
    )

supabase = get_supabase()

# Initialize login session
if "access_token" not in st.session_state:
    st.session_state.access_token = None

if "user_email" not in st.session_state:
    st.session_state.user_email = None

# Login
if not st.session_state.access_token:
    st.subheader("Student Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Sign In")

    if login:
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            st.session_state.access_token = response.session.access_token
            st.session_state.user_email = response.user.email
            st.session_state.user_id = response.user.id
            st.rerun()
        
        except Exception as e:
            st.error(f"Login failed: {e}")


    st.stop()

# Logged-in view
st.success(f"Signed in as {st.session_state.user_email}")

if st.button("Sign Out"):
    supabase.auth.sign_out()
    st.session_state.access_token = None
    st.session_state.user_email = None
    st.rerun()


    if st.button("Save Answer", key=f"save_{i}"):
        answer = st.session_state[f"sql_{i}"].strip()

        if not answer:
            st.warning("Please enter a SQL answer before saving.")
        else:
            try:
                # Authenticate the request using the signed-in user's token
                supabase.postgrest.auth(st.session_state.access_token)

                # Save or update this user's answer
                supabase.table("quiz_answers").upsert(
                    {
                        "user_id": st.session_state.user_id,
                        "question_number": i + 1,
                        "sql_answer": answer,
                    },
                    on_conflict="user_id,question_number",
                ).execute()

                st.success("Answer saved successfully!")

            except Exception:
                st.error("Unable to save your answer. Please try again.")

st.divider()


def run_sql(query):
    # Connect using the read-only database user
    connection = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        dbname=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        sslmode=st.secrets["DB_SSLMODE"],
        connect_timeout=10,
    )

    try:
        # Prevent queries from modifying the database
        connection.set_session(readonly=True, autocommit=False)

        with connection.cursor() as cursor:
            cursor.execute("SET LOCAL statement_timeout = '5s'")
            cursor.execute(query)

            if cursor.description is None:
                raise ValueError("Only queries returning results are allowed.")

            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

        return pd.DataFrame(rows, columns=columns)

    finally:
        connection.rollback()
        connection.close()


# Quiz questions
for i, q in enumerate(questions):
    st.subheader(f"Question {i + 1} ({q['points']} points)")
    st.write(q["question"])
    
    with st.expander("Show Hint"):
        st.write(q["hint"])

    with st.expander("Show Expected Answer"):
        st.code(q["expected_sql"], language="sql")
        st.write("Run this query to view the expected results.")


    st.text_area(
        "Write your SQL query:",
        key=f"sql_{i}",
        height=120,
        placeholder="SELECT ..."
    )

    if st.button("Run SQL", key=f"run_{i}"):
        query = st.session_state[f"sql_{i}"].strip()

        if not query:
            st.warning("Please enter a SQL query.")
        elif not query.lower().startswith(("select ", "with ", "select\n", "with\n")):
            st.error("Only SELECT queries are allowed.")
        else:
            try:
                result = run_sql(query)
                st.dataframe(result, use_container_width=True)
            except Exception:
                st.error("Query failed. Check your SQL syntax and try again.")

    st.divider()
