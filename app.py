from dotenv import load_dotenv # type: ignore

load_dotenv()  # Load environment variables

import streamlit as st # Correct alias for Streamlit
import os
import sqlite3

import google.generativeai as genai # type: ignore

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text # Use 'text' instead of 'txt'

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database is named STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
    \n\nFor example, \nExample1 - How many entries or records are present? 
    The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    \n\nExample2 - Tell me all the students studying in the Data Science class?
    The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS = "Data Science";
    Also, the SQL code should not have ``` in the beginning or end and the SQL word in the output.
    """
]

# Streamlit app
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the Question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The SQL Query is:")
    st.write(response)
    
    data = read_sql_query(response, "student.db")
    st.subheader("Query Results:")
    for row in data:
        st.write(row)
