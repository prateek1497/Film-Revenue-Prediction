from robobrowser import RoboBrowser
from time import sleep
br = RoboBrowser(history = True, user_agent='a python robot', parser='html.parser')
br.open('http://www.koimoi.com/box-office/hits-flops/verdict-2014/')
tables = []
text = br.parsed()
for i in text:
    tables.extend(i.find_all('tbody', class_ = 'row-hover'))
s = set(tables)
rows = []
for i in s:
    if(len(i)>15):
        rows = i
        break

print("done")
header = 'Movie Name,' + 'Release Date,'+'1st Day,'+ '1st Weekend,'+ '1st Week,'+ 'Lifetime,'+"stars,"+"cast,"+"director"+"\n"

csv = open('2014Full.csv', 'a')
csv.write(header)
children = list(rows.children)
children = children[32:]
print(len(children))
for x in range(0, len(children)):
    i = children[x]
    print(i.get_text())
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
    try:
        br.follow_link(main.a)
    except:
        continue
        print("Applying Brakes")
        csv.close()
        print(x)
        break
    curImp = []
    curText = br.parsed()
    for j in curText:
        curImp.extend(j.find_all('div', class_ = 'td-post-content'))
    curS = list(set(curImp))
    curRow = object()
    for i in curS:
        curRow = i
        break
    print("Movie Data")
    star = curRow.p
    starText = star.get_text()
    cast = star.next_sibling
    castText = cast.get_text()
    direct = cast.next_sibling
    directText = direct.get_text()
    starsSplit = starText.split(":")
    starsAct = starsSplit[1] if len(starsSplit)>=2 else ""
    castSplit = castText.split(":")
    castAct = castSplit[1] if len(castSplit)>=2 else ""
    directSplit = directText.split(":")
    directAct = directSplit[1] if len(directSplit)>=2 else ""

    string = names+","+date+","+firstday+","+firstWeekend+","+lifetime+","+starsAct+"["+castAct+"]"+","+"["+directAct+"]"+"\n"
    print(string)
    csv.write(string)
    br.back()
if csv:
    csv.close()




