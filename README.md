# Text_To_SQL
This project is a simple and interactive application that takes English questions as input and generates corresponding SQL queries using Google Gemini. It also executes these queries on a SQLite database and displays the results.<br>

Features
Natural Language to SQL: Converts natural language questions into SQL queries using the Google Gemini generative AI model.<br>
Database Integration: Runs generated SQL queries on a SQLite database (student.db).<br>
Interactive Interface: Built with Streamlit for a user-friendly, interactive experience.<br>
Project Structure<br>
app.py: The main application file. Contains the Streamlit interface and the logic for querying the database.<br>
sql.py: Script to set up the SQLite database (student.db) with a STUDENT table and sample records.<br>
Getting Started <br>
Prerequisites <br>
Python 3.7 or above <br>

Install dependencies:<br>
pip install -r requirements.txt<br>
Set up the .env file to include your Google Gemini API key:<br>
GOOGLE_API_KEY=your_google_api_key<br>
Run the sql.py script to set up the SQLite database:<br>
python sql.py<br>
Start the Streamlit application:<br>
streamlit run app.py<br>
How It Works<br>
Input your natural language question into the Streamlit app.<br>
The app sends the question and a predefined prompt to Google Gemini.<br>
Google Gemini generates an SQL query based on the input question.
The app executes the SQL query on the STUDENT table in student.db.
Results are displayed directly on the app.
Example Usage
Input: "How many students are in the Data Science class?"
Generated SQL Query: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
Result: Displays rows matching the query.
