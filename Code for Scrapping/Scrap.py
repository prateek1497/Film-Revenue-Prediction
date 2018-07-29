from robobrowser import RoboBrowser
import re

from bs4 import BeautifulSoup
br = RoboBrowser(history = True, user_agent='a python robot', parser='html.parser')
br.open('http://www.koimoi.com/box-office/hits-flops/verdict-2018/')
tables = []
text = br.parsed()
for i in text:
    tables.extend(i.find_all('tbody', class_ = 'row-hover'))

s = set(tables)
rows = object()
for i in s:
    if(len(i)>15):
        print('enter')
        rows = i
        break

print("done")


for i in rows.children:
    cur = i.td
    main = cur
    names = (cur.get_text())
    cur = cur.next_sibling
    date = (cur.get_text())
    cur = cur.next_sibling
    firstday = (cur.get_text())
    cur = cur.next_sibling
    firstWeekend = (cur.get_text())
    cur = cur.next_sibling
    lifetime = (cur.get_text())
    br.follow_link(main)



header = 'Movie Name,' + 'Release Date,'+'1st Day,'+ '1st Weekend,'+ '1st Week,'+ 'Lifetime'

csv = open('2018.csv', 'w')
csv.write(header)
for i in range(len(date)):
    string = "\n" + names[i] + "," + date[i] + "," + firstday[i] + "," + firstWeekend[i] + "," + lifetime[i]
    print(string)
    csv.write(string)
csv.close()




