



import requests
from bs4 import BeautifulSoup
import sys
import io



# Set the encoding for stdout to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


#function for saving html scrape content into file times.html
# def fetchAndSaveToFile(url,path):
#     r=requests.get(url)
#     with open (path,"w")as f:
#         f.write(r.text.encode('utf-8').decode('utf-8'))
# url="https://timesofindia.indiatimes.com/india/"
# fetchAndSaveToFile(url ,"Data/times.html")


url="https://pcet.org.in/youthconference/"
#step !:Get the Html Content
r=requests.get(url)
htmlContent=r.content
#printing all html code 
#print(htmlContent)
#step 2: parse the HTML content
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())


#step 3:Html tree traversal
title=soup.title

# print(type(title)) //Tag  

#print(type(soup)) //BeautifulSoup

#print(type(title.string)) //Navigablestring

#Get 1st Paragraph text
paras=soup.find('p').get_text()
print(paras)

#Getting all links from page
anchors=soup.find_all('a')
all_links=set()
for link in anchors:
    if(link.get('href')!='#'):
        link_text="https://pcet.org.in/youthconference"+link.get('href')
        all_links.add(link_text)
        print(all_links)


