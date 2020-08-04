import psycopg2
import csv

def create_tables():
    "create tables in the PostgreSQL database"
    
    command = ('''

    CREATE TABLE IF NOT EXISTS "oblasti" (
        "id" varchar PRIMARY KEY,
        "name" varchar
    );

    CREATE TABLE IF NOT EXISTS "obstini" (
        "id" varchar PRIMARY KEY,
        "name" varchar,
        "oblast_id" varchar
    );

    CREATE TABLE IF NOT EXISTS "selishta" (
        "id" varchar PRIMARY KEY,
        "name" varchar,
        "type" varchar,
        "obstina_id" varchar
    );

    ALTER TABLE "obstini" ADD FOREIGN KEY (oblast_id) REFERENCES "oblasti" (id);

    ALTER TABLE "selishta" ADD FOREIGN KEY (obstina_id) REFERENCES "obstini" (id);
    
    ''')

    #connect to the database
    connection = psycopg2.connect("dbname='selishta_postgres' user='samuil2001ivanov' password='samuil123'")
    connection.autocommit = True
    cur = connection.cursor()

    connection = None
    try:
        #create the tables in the database
        cur.execute(command)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def import_data():
    try:
        #connect to the database
        connection = psycopg2.connect("dbname='selishta_postgres' user='samuil2001ivanov' password='samuil123'")
        connection.autocommit = True
        cur = connection.cursor()

        file_path_oblasti = "/home/samuil2001ivanov/Downloads/Oblasti.csv"
        file_path_obstini = "/home/samuil2001ivanov/Downloads/Obstini.csv"
        file_path_selishta = "/home/samuil2001ivanov/Downloads/Selishta.csv"

        #load data into 'Oblasti' table
        with open(file_path_oblasti, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            row_count = sum(1 for row in reader)
            if row_count <= 1:
                for row in reader:
                    cur.execute(
                        'insert into public."oblasti" (id, name) values (%s, %s)',
                        row
                    )
        
        connection.commit()

        #load data into 'Obstini' table
        with open(file_path_obstini, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            row_count = sum(1 for row in reader)
            if row_count <= 1:
                for row in reader:
                    cur.execute(
                        'insert into public."obstini" (id, name, oblast_id) values (%s, %s, %s)',
                        row
                    )
        
        connection.commit()

        #load data into 'Selishta' table
        with open(file_path_selishta, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            row_count = sum(1 for row in reader)
            if row_count <= 1:
                for row in reader:
                    cur.execute(
                        'insert into public."selishta" (id, name, type, obstina_id) values (%s, %s, %s, %s)',
                        row
                    )

        connection.commit()
    except psycopg2.Error as e:
        print(e)
    
    cur.close()
    connection.close()

def getCountRecordsInTables():
     #connect to the database
    connection = psycopg2.connect("dbname='selishta_postgres' user='samuil2001ivanov' password='samuil123'")
    connection.autocommit = True
    cur = connection.cursor()

    #get the number of records in the 'oblasti' table
    count_sql_query = 'select count(*) from public."oblasti"'
    cur.execute(count_sql_query)
    records_count = cur.fetchone()[0]
    print('count of records in table "oblasti": ' + str(records_count))

    #get the number of records in the 'obstini' table
    count_sql_query = 'select count(*) from public."obstini"'
    cur.execute(count_sql_query)
    records_count = cur.fetchone()[0]
    print('count of records in table "obstini": ' + str(records_count))

    #get the number of records in the 'selishta' table
    count_sql_query = 'select count(*) from public."selishta"'
    cur.execute(count_sql_query)
    records_count = cur.fetchone()[0]
    print('count of records in table "selishta": ' + str(records_count))

    cur.close()
    connection.close()

if __name__ == '__main__':
    #create_tables()
    import_data()
    #getCountRecordsInTables()