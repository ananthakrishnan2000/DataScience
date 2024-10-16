import requests
from bs4 import BeautifulSoup
print("SJC23MCA-2020 : A S Ananthakrishnan")
print("Batch : MCA 2023-25")
def getdata(url):
    r = requests.get(url)
    return r.content
htmldata = getdata("https://www.toppr.com/guides/essays/globalization-essay/")
soup = BeautifulSoup(htmldata,'html.parser')
data = ''
pr = len(soup.find_all('p'))
print("<p> tag ",pr)
for data in soup.find_all('p'):
    print(data.get_text())