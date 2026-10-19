import streamlit as st
from questions import questions

st.set_page_config(
    page_title="SQL Quiz",
    page_icon="📚",
    layout="centered"
)

st.title("SQL Practice Quiz")
st.write("Students and Grades")
st.write("5 questions | 20 points total")

st.divider()

# Display each SQL question
for i, q in enumerate(questions):
    st.subheader(f"Question {i + 1} ({q['points']} points)")
    st.write(q["question"])

    # Show a hint
    with st.expander("Show Hint"):
        st.write(q["hint"])

    # SQL input
    st.text_area(
        "Write your SQL query:",
        key=f"sql_{i}",
        height=120,
        placeholder="SELECT ..."
    )

    st.divider()
