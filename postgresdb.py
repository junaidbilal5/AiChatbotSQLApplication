import psycopg

def execute_query(query):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description] if cur.description else []
            return  columns, rows

def get_schema(table_name):
    query = f"""SELECT  column_name, data_type
        FROM information_schema.columns
        WHERE 
         table_schema = 'public'
        AND table_name = '{table_name}'"""
    schema = execute_query(query)
    return schema

#result = get_schema("orders")
#print(result)