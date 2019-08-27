import psycopg2

conn = None

    # connect database
try:
    conn = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print(e.diag.message_detail)
    sys.exit(1)
cur = conn.cursor()

    # Q1: select the most popular three articles

    # A1 : candidate-is-jerk, bears-love-berries, bad-things-gone

cur.execute("""SELECT path, count(id) FROM log 
WHERE length(path) > 2 GROUP BY path 
ORDER BY count(id) desc limit 3""")

rows = cur.fetchall()

print("the most popular three articles are")
for row in rows:
    print(row[0].split('/',2)[-1] + ' : ' + str(row[1]) + ' views')

cur.execute("""WITH AUTH AS (select path, count(id) from log where length(path) > 2  group by path order by count(id) desc
limit 1) select authors.name from authors where authors.id = (select distinct articles.author from articles, AUTH  
where articles.title ~ split_part(REGEXP_REPLACE(AUTH.path,'/','-'),'-', 3)) ;
""")

rows = cur.fetchall()

for row in rows:
    print("the most popular article author " + str(rows[0]))

cur.execute("select time::date from log where status not like '200 OK' group by time::date order by count(status) DESC limit 1;")

rows = cur.fetchall()
print("day of more than 1% of requests lead to errors : " + str(rows[0]))

conn.close()
