'''
A very common use case for context managers is managing database connections. Your task is to create a context manager named db_handler.

This context manager should:

"Open" a database connection on entering the with block.
yield the connection object so it can be used inside the block.
"Close" the database connection when exiting the block, even if an error occurred.
'''

from contextlib import contextmanager

class MockDBConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_connected = False

    def connect(self):
        print(f"Connecting to database '{self.db_name}'...")
        self.is_connected = True
        print("Connection successful.")

    def execute_query(self, query):
        if not self.is_connected:
            raise ConnectionError("Connection not established, Database is not connected.")
        print(f"Executing query: '{query}'...")
        return "Query results"

    def close(self):
        print(f"Closing connection to database '{self.db_name}'...")
        self.is_connected = False
        print("Connection closed.")

@contextmanager
def db_handler(db_name):
    # 1. Setup: Create a connection object and connect
    conn = MockDBConnection(db_name)
    conn.connect()
    try:
        # 2. Yield the connection object for use in the 'with' block
        yield conn
    finally:
        # 3. Teardown: Ensure the connection is closed
        conn.close()

# --- Example Usage ---
print("--- Test Case 1: Successful operation ---")
try:
    with db_handler("production_db") as conn:
        conn.execute_query("SELECT * FROM users")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- Test Case 2: Operation with an error ---")
try:
    with db_handler("analytics_db") as conn:
        conn.execute_query("SELECT * FROM events")
        # Simulate an error
        raise ValueError("Something went wrong during data processing!")
except Exception as e:
    print(f"Caught expected error: {e}")


# Expected output for Test Case 2 shows that "Closing connection"
# is printed even after the ValueError is raised, proving the teardown works.