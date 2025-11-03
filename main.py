# from dotenv import load_dotenv
# import os

# # Step 1: Load the .env file
# load_dotenv()

# # Step 2: Get all environment variables
# DB_HOST = os.getenv("DB_HOST")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_PORT = os.getenv("DB_PORT")

# # Step 3: Print (to verify)
# print("Host:", DB_HOST)
# print("Database:", DB_NAME)
# print("User:", DB_USER)
# print("Password:", DB_PASSWORD)
# print("Port:", DB_PORT)


from dotenv import load_dotenv
import os
import psycopg2

# Step 1: Load .env file
load_dotenv()

# Step 2: Get environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

# Step 3: Create database connection
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    print("Database connected successfully!")
except Exception as e:
    print("Connection failed:", e)
