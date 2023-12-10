import snowflake.connector

class SnowflakeConnector:
    def __init__(self, account, user, password, warehouse, database, schema):
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = snowflake.connector.connect(
                user=self.user,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema
            )
            self.cur = self.conn.cursor()
            print("Connected to Snowflake")
        except Exception as e:
            print(f"Error connecting to Snowflake: {str(e)}")

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None

    def close_connection(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            print("Connection closed")

# Example usage:
# Replace these values with your Snowflake account information
account = 'JQCIWYE-URB87198'
user = 'sourabh01'
password = 'Agarkar01'
warehouse = 'DATAWH'
database = 'snowflake_sample_data'
schema = 'tpch_sf1'

# Instantiate the SnowflakeConnector
snowflake_conn = SnowflakeConnector(account, user, password, warehouse, database, schema)

# Connect to Snowflake
snowflake_conn.connect()

# Execute a query
query_result = snowflake_conn.execute_query("select * from region")
print("Query Result:", query_result)

# Close the connection
snowflake_conn.close_connection()
