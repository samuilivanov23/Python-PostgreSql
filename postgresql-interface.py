import psycopg2

#connect to the database
connection = psycopg2.connect("dbname='selishta_postgres' user='samuil2001ivanov' password='samuil123'")
connection.autocommit = True
cur = connection.cursor()

selishte = input("Enter name of selishte: ")

count_sql_query = "select * from public." + '"selishta"' + " where name=%s"
cur.execute(count_sql_query, (selishte,))
records = cur.fetchall() 
   
#print(" id    name    type    obstina_id")
print("\n ")
for row in records:
    #print(row[0] + "    " + row[1] + "    " + row[2] + "    " + row[3] + "\n")
    print("id = " + row[0])
    print("name = " + row[1])
    print("type  = " + row[2])
    print("obstina_id = " + row[3] + "\n")
