import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    # connect to default database
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="######") 
    except psycopg2.Error as e:
    print("Error: Could not make connection to the postgres database")
    print(e)
    
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)
        
    conn.set_session(autocommit=True)
        
    # create sparkify database with UTF8 encoding
    try:
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    except psycopg2.Error as e:
        print("Error: Could not drop Database")
        print(e)
    
    try:
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    except psycopg2.Error as e:
        print("Error: Could not create Database")
        print(e)    


    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="sparkifydb", user="postgres", password="Jinky450")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)    
    
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)
    
    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not drop table from query: {}".format(query))
            print(e)

def create_tables(cur, conn):
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not create table from query: {}".format(query))
            print(e)


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    cur.close();
    conn.close()


if __name__ == "__main__":
    main()
