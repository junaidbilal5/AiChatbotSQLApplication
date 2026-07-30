# Import PostgreSQL database driver
import psycopg


# Execute SQL query against PostgreSQL database
#
# This function:
# 1. Opens a database connection
# 2. Creates a cursor
# 3. Executes the provided SQL query
# 4. Fetches query results
# 5. Returns column names and rows
def execute_query(query):

    # Establish PostgreSQL database connection
    # Connection details should ideally be moved to environment variables
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres"
    ) as conn:

        # Create database cursor for executing SQL commands
        with conn.cursor() as cur:

            # Execute the SQL query
            cur.execute(query)

            # Retrieve all returned rows
            rows = cur.fetchall()

            # Extract column names from query metadata
            # Some SQL statements may not return columns
            columns = [desc[0] for desc in cur.description] if cur.description else []

            # Return both column names and query results
            return columns, rows



# Retrieve database table schema information
#
# This function queries PostgreSQL metadata tables
# to understand the structure of a database table.
#
# Schema information is provided to the LLM so it can
# generate SQL queries based on available columns.
def get_schema(table_name):

    # Query PostgreSQL information_schema
    # to fetch column names and data types
    query = f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE 
            table_schema = 'public'
            AND table_name = '{table_name}'
    """

    # Execute schema query
    schema = execute_query(query)

    # Return table schema details
    return schema



# Example usage:
# result = get_schema("orders")
# print(result)