#-------------------------------------------------
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from postgresdb import execute_query, get_schema


# Load environment variables
load_dotenv()


# Streamlit config
st.set_page_config(
    page_title="Ask your orders data",
    page_icon="📊"
)

st.title("📊 Ask your orders data")


# OpenAI response schema
class QueryResult(BaseModel):
    sql: str
    question: str


# OpenAI client
@st.cache_resource
def get_client():
    return OpenAI()


# Load database schema
@st.cache_data
def load_schema():
    return get_schema("orders")


client = get_client()
schema = load_schema()


# Chat history
if "history" not in st.session_state:
    st.session_state.history = []


# Display previous messages
for turn in st.session_state.history:

    with st.chat_message("user"):
        st.write(turn["question"])

    with st.chat_message("assistant"):

        if turn.get("error"):
            st.error(turn["error"])

        else:
            st.code(turn["sql"], language="sql")
            st.dataframe(turn["dataframe"])


# User input
user_input = st.chat_input(
    "Ask a question about the orders table..."
)


if user_input:

    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):

        turn = {
            "question": user_input
        }


        with st.spinner("Generating SQL..."):

            prompt = f"""
You are an expert SQL generator.

Generate ONLY a SQL query based on the user question.

User question:
{user_input}


Database schema:
{schema}


Rules:
- Use only columns from the schema.
- Do not add explanations.
- Do not use markdown.
- Return valid SQL only.
"""


            try:

                # Generate SQL using OpenAI
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


                result = (
                    response
                    .choices[0]
                    .message
                    .parsed
                )


                final_sql = result.sql


                # Display SQL
                st.subheader("Generated SQL")
                st.code(
                    final_sql,
                    language="sql"
                )


                turn["sql"] = final_sql


                # Execute query
                columns, rows = execute_query(final_sql)


                df = pd.DataFrame(
                    rows,
                    columns=columns
                )


                st.subheader("Result")

                st.dataframe(df)


                turn["dataframe"] = df



            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )

                turn["error"] = str(e)



        st.session_state.history.append(turn)