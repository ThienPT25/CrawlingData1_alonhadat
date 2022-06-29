from bs4 import BeautifulSoup
from hamcrest import none
import requests
import csv

def get_data():
    try:
        title = soup.find("div", class_="title").h1.text
    except Exception as e:
        title = None
    print(title)
    try:
        body = soup.find("div", class_="detail text-content").text
    except Exception as e:
        body = None
    print(body)
    try:
        price = soup.find("span", class_="price").text
    except Exception as e:
        price = None
    print(price)
    try:
        area = soup.find("span", class_="square").text
    except Exception as e:
        area = None
    print(area)
    try:
        location = soup.find("div", class_="address").text
    except Exception as e:
        location = None
    print(area)
    try:
        detail = soup.find("div", class_="infor").text
    except Exception as e:
        detail = None
    print(detail)
    print()
    csv_writer.writerow([title, str(body), price, area, location, detail])    

try:
    with open("alonhadat.csv", "w", newline="", encoding = 'UTF-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Title", "Describe", "Price", "Area", "Location", "Detail"])
        responsee = requests.get("https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/15/binh-dinh.html")
        soup = BeautifulSoup(responsee.content, "html.parser")
        titles = soup.find_all("div", class_="ct_title")
        links = [link.find('a').attrs["href"] for link in titles]
        for link in links:
            news = requests.get("https://alonhadat.com.vn/" + link)
            soup = BeautifulSoup(news.content, "html.parser")
            get_data()
        n = 5
        for i in range(1, n):
            i = i + 1
            responsee = requests.get("https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/15/binh-dinh/trang--" + str(i) + ".html")
            soup = BeautifulSoup(responsee.content, "html.parser")
            titles = soup.find_all("div", class_="ct_title")
            links = [link.find('a').attrs["href"] for link in titles]
            for link in links:
                news = requests.get("https://alonhadat.com.vn/" + link)
                soup = BeautifulSoup(news.content, "html.parser")
                get_data()
finally:
    f.close()