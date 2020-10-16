import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

#res = requests.get("test.html", headers =headers)
soup = BeautifulSoup(open("test.html"),"html.parser")

# print(soup.prettify())

# print("title----------->", soup.title)
# print("head----------->", soup.head)
# print("p----------->", soup.p)
# print("a----------->", soup.a)


print("selector-->", soup.select("p > a #link2"))



# for sibling in soup.a.next_siblings:
#     print("---a--->",sibling)

#price = soup.select('#page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_price ')
#print(price)



