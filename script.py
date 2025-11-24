from splinter import Browser
from bs4 import BeautifulSoup

username = '' # Write your username here
password = '' # Write your password here
journal_suffix = 'ms' # Management Science

b = Browser('firefox', headless=True)
b.visit('https://mc.manuscriptcentral.com/' + journal_suffix)

b.fill('USERID', username)
b.fill('PASSWORD', password)

if b.find_by_id('onetrust-accept-btn-handler'):
    b.find_by_id('onetrust-accept-btn-handler').click()

b.find_by_id('logInButton').click()
b.links.find_by_partial_href("AUTHOR").click()

# I hope your paper is accepted!
print(BeautifulSoup(b.html, "lxml").find("span", attrs={"class": "pagecontents"}).string)
