import pymysql
import os

# Database credentials
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'Manjil@1982'
DB_NAME = 'agency_db'

def load_data():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()
    
    print("Loading data...")
    count = 0
    statement = ""
    
    with open('data.sql', 'r', encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith('--') or stripped.startswith('/*'):
                continue
            
            # Append line to statement
            statement += line
            
            # Check if statement ends with semicolon
            if stripped.endswith(';'):
                # Process statement
                clean_stmt = statement.strip()
                if clean_stmt.upper().startswith('INSERT INTO'):
                    try:
                        cursor.execute(clean_stmt)
                        count += 1
                        if count % 10 == 0:
                            print(f"Executed {count} statements...")
                    except Exception as e:
                        # Ignore duplicate entry errors if re-running
                        # 1062 is fail on duplicate
                        if isinstance(e.args, tuple) and len(e.args) > 0 and e.args[0] == 1062:
                             pass
                        else:
                             print(f"Error executing statement: {e}")
                             # print(clean_stmt[:100])
                
                # Reset statement
                statement = ""

    conn.commit()
    print(f"Successfully executed {count} INSERT statements.")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_data()
