from google import genai
from dotenv import load_dotenv
from google.genai import types
import json
from pydantic import BaseModel
from postgresdb import execute_query,get_schema

load_dotenv()

class QueryResult(BaseModel):
    sql : str
    question : str 

client = genai.Client()

#prompt = input("ask your question: " )
schema = get_schema("orders")

while True:
    user_input = input("enter your question: ")
    if user_input == 'exit':
        break
    else:
        prompt = f"""write a sql based on the question below:
        {user_input}
        use below orders table schema
        {schema}
        """

        response = client.models.generate_content(
            model= 'gemini-3.5-flash',
            contents= prompt,
            config= types.GenerateContentConfig(
                response_mime_type= 'application/json',
                response_schema = QueryResult
            )
        )

        json_response = json.loads(response.text)
        final_sql= json_response['sql']
        final_result = execute_query(final_sql)
        #print(final_sql)
        print(final_result)
