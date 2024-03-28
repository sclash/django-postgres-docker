import psycopg2

conn = psycopg2.connect(database = "postgres_django", 
                        user = "asergi", 
                        host= '172.26.35.20',
                        password = "abcde",
                        port = 5432)
print(conn)
cur = conn.cursor()



conn = psycopg2.connect(database = "postgres_django", 
                        user = "asergi", 
                        host= '172.17.0.1',
                        password = "abcde",
                        port = 5432)
print(conn)
cur = conn.cursor()
