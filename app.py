import streamlit as st
from supabase import create_client
from questions import questions

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

st.divider()

# Quiz questions
for i, q in enumerate(questions):
    st.subheader(f"Question {i + 1} ({q['points']} points)")
    st.write(q["question"])

    with st.expander("Show Hint"):
        st.write(q["hint"])
        st.code(q["expected_sql"], language="sql")

    st.text_area(
        "Write your SQL query:",
        key=f"sql_{i}",
        height=120,
        placeholder="SELECT ..."
    )

    st.divider()
