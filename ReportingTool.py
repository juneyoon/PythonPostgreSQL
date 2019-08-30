#!/usr/bin/env python
import psycopg2

conn = None

conn = psycopg2.connect("dbname=news")

cur = conn.cursor()

cur.execute("""SELECT path, count(id) FROM log
WHERE length(path) > 2 GROUP BY path
ORDER BY count(id) desc limit 3""")

rows = cur.fetchall()

print("the most popular three articles are")
for row in rows:
    print(row[0].split('/', 2)[-1] + ' : ' + str(row[1]) + ' views')

cur.execute("""select authors.name, count(log.id) as View
from authors, articles, log where articles.author = authors.id
and length(path) > 2 and authors.name not like 'Anonymous%'
group by authors.name order by count(log.id) desc;""")

rows = cur.fetchall()

print("Who are the most popular article authors of all time?")
for row in rows:
    print(str(row[0]), str(row[1]) + "views")

cur.execute("""select time::date from log where status not like '200 OK'
group by time::date order by count(status) DESC limit 1;""")

rows = cur.fetchall()
print("day of more than 1% of requests lead to errors : " + str(rows[0]))

conn.close()
