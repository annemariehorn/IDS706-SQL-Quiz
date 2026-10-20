# SQL Quiz Questions
# Total: 20 points (5 questions, 4 points each)

questions = [
    {
        "question": "Display all students and their grades.",
        "points": 4,
        "hint": "Use SELECT to retrieve all columns.",
        "expected_sql": "SELECT * FROM students ORDER BY student_id;",
        "expected_result": "Returns all 10 students, including their IDs, names, grades, and courses."
    },
    {
        "question": "Find students with grades above 90.",
        "points": 4,
        "hint": "Use WHERE to filter grades greater than 90.",
        "expected_sql": "SELECT * FROM students WHERE grade > 90 ORDER BY student_id;",
        "expected_result": "Returns Alice (92), Diana (95), and Hannah (94)."
    },
    {
        "question": "List all students from highest to lowest grade.",
        "points": 4,
        "hint": "Use ORDER BY with DESC.",
        "expected_sql": "SELECT student_name, grade FROM students ORDER BY grade DESC, student_id;",
        "expected_result": "Returns all 10 students sorted by grade from highest to lowest, starting with Diana (95), Hannah (94), and Alice (92)."
    },
    {
        "question": "Calculate the average grade across all students.",
        "points": 4,
        "hint": "Use the AVG() aggregate function.",
        "expected_sql": "SELECT ROUND(AVG(grade), 2) AS average_grade FROM students;",
        "expected_result": "Returns one row with an average_grade of 86.80."
    },
    {
        "question": "Count how many students are enrolled in each course.",
        "points": 4,
        "hint": "Use COUNT(*) and GROUP BY.",
        "expected_sql": "SELECT course, COUNT(*) AS student_count FROM students GROUP BY course ORDER BY course;",
        "expected_result": "Returns three rows: English (3 students), Math (4 students), and Science (3 students)."
    }
]
