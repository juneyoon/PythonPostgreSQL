

## **Introduction of the Reporting Tool**

## **Generated contents**

 1. What are the most popular three articles of all time?    
Query : SELECT path, count(id) FROM log WHERE length(path) > 2 GROUP BY path ORDER BY count(id) desc limit 3

	Output : 
	candidate-is-jerk : 338647 views
	bears-love-berries : 253801 views
	bad-things-gone : 170098 views

 2. The most popular three articles of all time
 Query design : WITH AUTH AS (select path, count(id) from log where length(path) > 2 group by path order by count(id) desc limit 1) select authors.name from authors where authors.id = (select distinct articles.author from articles, AUTH where articles.title ~ split_part(REGEXP_REPLACE(AUTH.path,'/','-'),'-', 3)) ;

	Output : 
	the most popular article author ('Rudolf von Treppenwitz',)

 3. On which days did more than 1% of requests lead to errors
 Query design : select time::date from log where status not like '200 OK' group by time::date order by count(status) DESC limit 1;
 
	Output : 
	day of more than 1% of requests lead to errors : (datetime.date(2016, 7, 17),)



## How to run the reporting tool

1. install VirtualBox
	download from here (https://www.virtualbox.org/wiki/Downloads)
2. install Vagrant
	download from here (https://www.vagrantup.com/downloads.html)
3. setup the news database (PostgreSQL) : 
	sudo apt-get install postgresql 
	refer to https://www.python.org/dev/peps/pep-0249/ and http://initd.org/psycopg/docs/
4. setup vagrant and run
	vagrant init ubuntu/trusty64
	vagrant up
5. log into the Linux instance
	vagrant ssh
6. run the application
**python ReportingTool.py**

