# Text_To_SQL
This project is a simple and interactive application that takes English questions as input and generates corresponding SQL queries using Google Gemini. It also executes these queries on a SQLite database and displays the results.<br>

Features
Natural Language to SQL: Converts natural language questions into SQL queries using the Google Gemini generative AI model.
Database Integration: Runs generated SQL queries on a SQLite database (student.db).
Interactive Interface: Built with Streamlit for a user-friendly, interactive experience.
Project Structure
app.py: The main application file. Contains the Streamlit interface and the logic for querying the database.
sql.py: Script to set up the SQLite database (student.db) with a STUDENT table and sample records.
Getting Started
Prerequisites
Python 3.7 or above
<br>
Required Python libraries:
<br>
streamlit
sqlite3
google.generativeai
dotenv
A valid API key for Google Gemini (to be set in an .env file).
<br>
Setup
Clone this repository:
<br>
bash
Copy code
git clone https://github.com/your-username/repo-name.git
cd repo-name
Install dependencies:
<br>
bash
Copy code
pip install -r requirements.txt
Set up the .env file to include your Google Gemini API key:
<br>
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key
Run the sql.py script to set up the SQLite database:
<br>
bash
Copy code
python sql.py
Start the Streamlit application:
<br>
bash
Copy code
streamlit run app.py
Open the application in your browser and start querying!
<br>
How It Works
Input your natural language question into the Streamlit app.
The app sends the question and a predefined prompt to Google Gemini.
Google Gemini generates an SQL query based on the input question.
The app executes the SQL query on the STUDENT table in student.db.
Results are displayed directly on the app.
Example Usage
Input: "How many students are in the Data Science class?"
Generated SQL Query: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
Result: Displays rows matching the query.
