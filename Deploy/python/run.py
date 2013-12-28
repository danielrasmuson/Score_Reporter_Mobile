# import urllib.request
from bs4 import BeautifulSoup

def getSource(url):
    #!/usr/bin/env python
    from contextlib import closing
    from selenium.webdriver import Firefox # pip install selenium
    from selenium.webdriver.support.ui import WebDriverWait

    # use firefox to get page with javascript generated content
    with closing(Firefox()) as browser:
        browser.get(url)
        # button = browser.find_element_by_name('tourninfo')
        # button.click()
        # wait for the page to load
        # WebDriverWait(browser, timeout=10).until(
         # lambda x: x.find_element_by_id('someId_that_must_be_on_new_page'))
        # store it to string variable
        page_source = browser.page_source
    return page_source


# sourceCode = getSource("http://scores.usaultimate.org/scores/#college-womens/tournament/14197")
sourceCode = getSource("http://scores.usaultimate.org/scores2012/#masters/tournament/11323")
# textFile = open("source.txt","r")
# sourceCode = textFile.read()
# textFile.close()

soup = BeautifulSoup(sourceCode)

# for each_div in soup.findAll('table', { "class" : "tourninfo" }):
    # print(each_div.get_text())  # .get_text()
for each_div in soup.findAll('table', { "class" : "brackets" }):
    print(each_div)  # .get_text()