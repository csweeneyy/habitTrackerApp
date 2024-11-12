import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="habits",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        print("Connected to the database!")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_users_table(conn):
    cursor = conn.cursor()
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(100),
        user_email VARCHAR(100) UNIQUE NOT NULL
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    #print("Table created successfully!")
    cursor.close()

def insert_user(conn, name, email):
    try:
        cursor = conn.cursor()
        insert_query = '''INSERT INTO users (user_name, user_email) VALUES (%s, %s)'''
        cursor.execute(insert_query, (name, email))
        conn.commit()
        #print("Data inserted successfully!")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")



def create_habits_table(conn):
    cursor = conn.cursor()
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS habits (
        user_id SERIAL PRIMARY KEY,
        habit_name VARCHAR(100)
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully!")
    cursor.close()

def insert_habit(conn, name):
    try:
        cursor = conn.cursor()
        insert_query = f'''INSERT INTO habits (habit_name) VALUES (%s)'''
        cursor.execute(insert_query, (name,))
        conn.commit()
        print("Data inserted successfully!")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")

def check_name_exists(conn, name):
    try:
        cursor = conn.cursor()
        check_query = '''SELECT user_name FROM users WHERE user_name = %s'''
        cursor.execute(check_query, (name,))
        result = cursor.fetchone()  # Fetches the first row, if any
        cursor.close()

        if result:
            return True  # The name exists in the table
        else:
            return False  # The name does not exist in the table
    except Exception as e:
        print(f"Error checking if name exists: {e}")
        return False
