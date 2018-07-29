from robobrowser import RoboBrowser
import re
from bs4 import BeautifulSoup
br = RoboBrowser(history = True, user_agent='a python robot', parser='html.parser')

br.open('https://www.amazon.ca')
form =  br.get_form(class_ = 'nav-searchbar')
form['field-keywords'] = 'books on finance'
br.submit_form(form)

text = br.parsed()
print(type(text))
print(len(text))
books = []
for item in text:
    book = item.find_all('li', class_='s-result-item celwidget  ')
    books.extend(book)
next_page = []
for book in books:
    next_page.extend(book.find_all('a', class_='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'))

nameofBooks = []
for next in next_page:
    br.follow_link(next)
    page_html = br.parsed()
    paras = []
    for tags in page_html:
        paras.extend(tags.find_all('div', class_ = 'a-expander-content a-expander-partial-collapse-content'))
    find = False
    for i in paras:
        if i is not None and i.get_text().lower().find('warren buffett') != -1:
            find = True
    bookTitle = ''
    for i in page_html:
        found = i.find_all(id='productTitle')
        if len(found) > 0 and found is not None:
            name = found[0].get_text()
            bookTitle = name
            print(name)
            break
    if find:
        print("\nAdded\n")
        nameofBooks.append(bookTitle)



