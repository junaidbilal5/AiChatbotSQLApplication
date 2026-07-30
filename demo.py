# Import required libraries
from google import genai
from dotenv import load_dotenv
from google.genai import types
import json
from pydantic import BaseModel

# Import database helper functions
from postgresdb import execute_query, get_schema


# Load environment variables from .env file
# This keeps sensitive information like API keys outside the source code
load_dotenv()


# Define the expected structure of the LLM response
# Using Pydantic helps validate and enforce a consistent response format
class QueryResult(BaseModel):
    sql: str
    question: str


# Initialize Gemini API client
# API credentials are automatically loaded from environment variables
client = genai.Client()


# Retrieve database schema information
# Providing schema context helps the LLM generate accurate SQL queries
schema = get_schema("orders")


# Continuous interaction loop
# Allows users to ask multiple questions until they choose to exit
while True:

    # Capture user's natural language question
    user_input = input("enter your question: ")

    # Exit the application when user enters 'exit'
    if user_input == 'exit':
        break

    else:
        # Create prompt containing:
        # 1. User's business question
        # 2. Database schema context
        #
        # Schema grounding improves SQL generation accuracy
        prompt = f"""
        Write a SQL query based on the question below:

        User Question:
        {user_input}

        Use the following orders table schema:
        {schema}
        """


        # Send prompt to Gemini model
        #
        # response_mime_type ensures structured JSON output
        # response_schema enforces the expected response format
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                response_schema=QueryResult
            )
        )


        # Convert Gemini JSON response into Python dictionary
        json_response = json.loads(response.text)


        # Extract generated SQL query from LLM response
        final_sql = json_response['sql']


        # Execute generated SQL query against PostgreSQL database
        final_result = execute_query(final_sql)


        # Display query result to user
        print(final_result)