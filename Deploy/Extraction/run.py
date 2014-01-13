from bs4 import BeautifulSoup

def getSource(url):
    from contextlib import closing
    from selenium.webdriver import Firefox
    from selenium.webdriver.support.ui import WebDriverWait
    with closing(Firefox()) as browser:
        browser.get(url)
        page_source = browser.page_source
    return page_source

def toFile(fileName,text):
    textFile = open("tests\\all\\"+fileName + ".html","w")
    cssSheets = '<link rel="stylesheet" href="..\\allCSS.css"><link rel="stylesheet" href="..\\allCSS2.css">'
    textFile.write(cssSheets + text)
    textFile.close()
    

class tournamentPageInfo():
    """docstring for tournamentPageInfo"""
    def __init__(self, sourceCode):
        self.soup = BeautifulSoup(sourceCode)
        self.pageName = self.soup.title.string
        self.description = self.soup.find('table', { "class" : "tourninfo" })
        self.pools, self.brackets = self.findPoolsAndBrackets()
        self.map = self.soup.find('div',{'class':'gm-style'})
    def findPoolsAndBrackets(self):
        """The reason only 1 function is that they are in the same element"""
        pools = self.soup.findAll('table', { "class" : "pool" })
        poolList = []
        bracketList = []
        for pool in pools:
            poolName = pool.find('td', { "class" : "poolname" }).get_text()
            if str(poolName).split()[0] == "Pool":
                poolList.append(str(pool))
            else:
                bracketList.append(str(pool))
        return [poolList,bracketList]
    def getPageName(self):
        return str(self.pageName)
    def getDescription(self):
        return str(self.description)
    def getPools(self):
        return self.pools
    def getBrackets(self):
        return self.brackets
    def getMap(self):
        """Currently just returns the html of the 
        initial picture I.E. is not interactive"""
        return str(self.map)

# # Source from site
sourceCode = getSource("http://scores.usaultimate.org/scores/#college-womens/tournament/12237")

# # Source from file
# textFile = open("tests\\sourceCode.html","r")
# sourceCode = textFile.read()
# textFile.close()

tournamentPage = tournamentPageInfo(sourceCode)
toFile(tournamentPage.pageName + " description",tournamentPage.getDescription())
toFile(tournamentPage.pageName + " brackets","<br><br><br>".join(tournamentPage.getBrackets()))
toFile(tournamentPage.pageName + " pools","<br><br><br>".join(tournamentPage.getPools()))
toFile(tournamentPage.pageName + " map",tournamentPage.getMap())
