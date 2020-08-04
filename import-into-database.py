import psycopg2
import csv

def create_tables():
    "create tables in the PostgreSQL database"
    
    command = ('''

    CREATE TABLE "oblasti" (
        "id" varchar PRIMARY KEY,
        "name" varchar
    );

    CREATE TABLE "obstini" (
        "id" varchar PRIMARY KEY,
        "name" varchar,
        "oblast_id" varchar
    );

    CREATE TABLE "selishta" (
        "id" varchar PRIMARY KEY,
        "name" varchar,
        "type" varchar,
        "obstina_id" varchar
    );

    ALTER TABLE "obstini" ADD FOREIGN KEY (oblast_id) REFERENCES "oblasti" (id);

    ALTER TABLE "selishta" ADD FOREIGN KEY (obstina_id) REFERENCES "obstini" (id);
    
    ''')

    connection = None
    try:
        # connect to the PostgreSQL server
        connection = psycopg2.connect("dbname = 'selishta_postgres' user='samuil2001ivanov' password='samuil123'")
        cur = connection.cursor()
        
        cur.execute(command)
        # close communication with the PostgreSQL database server
        
        cur.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def import_data():
    try:
        file_path_oblasti = "/home/samuil2001ivanov/Downloads/Oblasti.csv"
        file_path_obstini = "/home/samuil2001ivanov/Downloads/Obstini.csv"
        file_path_selishta = "/home/samuil2001ivanov/Downloads/Selishta.csv"

        connection = psycopg2.connect("dbname='selishta_postgres' user='samuil2001ivanov' password='samuil123'")
        connection.autocommit = True
        cur = connection.cursor()

        #load data into 'Oblasti' table
        with open(file_path_oblasti, 'r') as f:
            reader = csv.reader(f)
            next(reader)
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


if __name__ == '__main__':
    create_tables()
    import_data()