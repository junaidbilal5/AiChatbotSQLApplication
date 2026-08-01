# Import required libraries
##https://www.youtube.com/watch?v=Qp30nYYFvM0

from dotenv import load_dotenv
from openai import OpenAI
import json
import os
# Import database helper functions
from postgresdb import execute_query,get_schema
from pydantic import BaseModel


# Load environment variables
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

#if openai_key:
#    print(" OpenAI API key loaded successfully")
#    print("Key starts with:", openai_key[:8] + "...")
#else:
#    print("OPENAI_API_KEY not found")


# ----------------------------------------------
class QueryResult(BaseModel):
    sql: str
    question: str

# ----------------------------------------------

schema = get_schema("orders")
# ----------------------------------------------
while True:
    #user_question = "top 5 customers"
    #user_question = "top 5 product"
    #user_question = "top 5 product based on number of orders"
    user_question = input("Enter your question (or type 'exit' to quit): ")
    if user_question.lower() == 'exit':
        break
    else:
        #prompt = f"""
        #You are a SQL expert.
        #
        #Generate a SQL query for this user question:
        #
        #{user_question}
        #
        #Use this database schema:
        #
        #orders(
        #  order_id,
        #    customer_id,
        #    customer_name,
        #    product_name,
        #    quantity,
        #    order_date,
        #    status,
        #    total_amount,
        #    payment_status,
        #    shipping_address,
        #    created_at,
        #    price
        #)
        #
        #Return only the SQL query and the original question.
        #"""
    
    
        prompt = f"""
        You are a SQL expert.
    
        Generate a SQL query for this user question:
    
        {user_question}
    
        Use this database schema:
    
        {schema}
        )
    
        Return only the SQL query and the original question.
        """
    
    
        #-----------------------------------------------
    
        # Create OpenAI client
        client = OpenAI(api_key=openai_key)
    
    
        response = client.beta.chat.completions.parse(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format=QueryResult
        )
    
    
        result = response.choices[0].message.parsed
    
        #print("Question:", result.question)
    
        final_sql = result.sql.replace("\\n", "\n")
        final_result = execute_query(final_sql)
    
        print(f"prompt:{prompt}")
        print(f"schema:{schema}")
        print(f"SQL:{final_sql}")
        print(f"final_result:{final_result}")