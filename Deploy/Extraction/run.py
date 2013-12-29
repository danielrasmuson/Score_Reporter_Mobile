# @todo if text does not contain a element will recieve error and program will crash
from bs4 import BeautifulSoup

def getSource(url):
    from contextlib import closing
    from selenium.webdriver import Firefox
    from selenium.webdriver.support.ui import WebDriverWait
    with closing(Firefox()) as browser:
        browser.get(url)
        page_source = browser.page_source
    return page_source


class tournamentPageInfo():
    """docstring for tournamentPageInfo"""
    def __init__(self, sourceCode):
        self.soup = BeautifulSoup(sourceCode)
    def getPageName(self):
        return self.soup.title.string
    def getDescription(self):
        return self.soup.find('table', { "class" : "tourninfo" })
    def getPools(self):
        """Returns a list of all pools in page"""
        pools = self.soup.findAll('table', { "class" : "pool" })
        resultList = []
        for pool in pools:
            poolName = pool.find('td', { "class" : "poolname" }).get_text()
            if str(poolName).split()[0] == "Pool":
                resultList.append(str(pool))

        return resultList
    def getBrackets(self):
        """Returns a list of all brackets in page"""
        #@TODO only difference is "!=" and "=="
        pools = self.soup.findAll('table', { "class" : "pool" })
        resultList = []
        for pool in pools:
            poolName = pool.find('td', { "class" : "poolname" }).get_text()
            if str(poolName).split()[0] != "Pool":
                resultList.append(str(pool))

        return resultList

# sourceCode = getSource("http://scores.usaultimate.org/scores2012/#masters/tournament/11648")

textFile = open("bracketTest\\sourceCode.txt","r")
sourceCode = textFile.read()
textFile.close()

tournamentPage = tournamentPageInfo(sourceCode)
print(tournamentPage.getDescription())
# print("<br><br><br>".join(tournamentPage.getBrackets()))
