import json

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

from postgresdb import execute_query, get_schema

load_dotenv()

st.set_page_config(page_title="Ask your orders data", page_icon="📊")
st.title("📊 Ask your orders data")


class QueryResult(BaseModel):
    sql: str
    question: str


@st.cache_resource
def get_client():
    return genai.Client()


@st.cache_data
def load_schema():
    return get_schema("orders")


client = get_client()
schema = load_schema()

if "history" not in st.session_state:
    st.session_state.history = []

for turn in st.session_state.history:
    with st.chat_message("user"):
        st.write(turn["question"])
    with st.chat_message("assistant"):
        if turn.get("error"):
            st.error(turn["error"])
        else:
            st.code(turn["sql"], language="sql")
            st.dataframe(turn["dataframe"])

user_input = st.chat_input("Ask a question about the orders table...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        turn = {"question": user_input}
        with st.spinner("Generating SQL..."):
            prompt = f"""write a sql based on the question below:
            {user_input}
            use below orders table schema
            {schema}
            """
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=QueryResult,
                    ),
                )
                json_response = json.loads(response.text)
                final_sql = json_response["sql"]
                st.code(final_sql, language="sql")
                turn["sql"] = final_sql

                columns, rows = execute_query(final_sql)
                df = pd.DataFrame(rows, columns=columns)
                st.dataframe(df)
                turn["dataframe"] = df
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                turn["error"] = str(e)

        st.session_state.history.append(turn)
