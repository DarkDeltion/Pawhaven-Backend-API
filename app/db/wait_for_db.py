# wait_for_db.py
import time
import os
import sys
import psycopg2
from psycopg2 import OperationalError

db_url = os.environ.get("DATABASE_URL")
if not db_url:
    print("DATABASE_URL not set")
    sys.exit(1)

print(f"Waiting for database at {db_url}...")

while True:
    try:
        conn = psycopg2.connect(db_url)
        conn.close()
        print("Database is ready!")
        break
    except OperationalError:
        print("Database not ready, retrying in 2 seconds...")
        time.sleep(2)

# Execute the command passed as arguments
os.execvp(sys.argv[1], sys.argv[1:])
