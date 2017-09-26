# "Database code" for article view report generation

import datetime
import psycopg2

DBNAME = "news"

# Queries 3 most popular articles from log table
query1 = """
select title, count(*) as num
from log join articles
on articles.slug = substring(log.path from '/article/(.*)')
group by title order by num desc limit 3
"""

# Queries 3 most popular articles from log table
query2 = """
select name, sum(num) as total_view
from authors join
(
  select author, count(*) as num
  from log join articles
  on articles.slug = substring(log.path from '/article/(.*)')
  group by author
) as article_view
on authors.id = article_view.author
group by name order by total_view desc """


query3 = """
select day, fail_rate from (select date_trunc('day', time) as day,
  cast(sum(case when status != '200 OK' then 1 else 0 end) as float)
  /cast(count(*) as float) as fail_rate
from log group by day) as fetch_fr where fail_rate > 0.01
"""


def main():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute(query1)
    rows = c.fetchall()

    print ""
    print "=====Section 1: Most Popular Three Articles of All Time========="
    for row in rows:
        print """ "{}" --- {}""".format(row[0], row[1])

    c.execute(query2)
    rows = c.fetchall()

    print ""
    print "=====Section 2: Most Popular Authors of All Time========="
    for row in rows:
        print """{} --- {} views""".format(row[0], row[1])

    c.execute(query3)
    rows = c.fetchall()

    print ""
    print "=====Section 3: Days When Error Rate > 1.0% ========="
    for row in rows:
        percent = row[1] * 100.0
        print """{0:%B %d, %Y} --- {1:.2f}% error""".format(row[0], percent)

    print ""
    db.close()

if __name__ == '__main__':
    main()
