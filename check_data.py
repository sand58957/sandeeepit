import pymysql

# Database credentials
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'Manjil@1982'
DB_NAME = 'agency_db'

def check_data():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()
    
    tables = ['blog_blogs', 'home_aboutsection', 'accounts_user']
    
    for table in tables:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"Table {table}: {count} rows")
        except Exception as e:
            print(f"Error checking {table}: {e}")
            
    conn.close()

if __name__ == "__main__":
    check_data()
