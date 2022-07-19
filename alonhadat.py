from bs4 import BeautifulSoup
from hamcrest import none
import requests
import csv
import json

def get_data():
    data = {}
    try:
        title = soup.find("div", class_="title").h1.text
    except Exception as e:
        title = None
    try:
        body = soup.find("div", class_="detail text-content").text
    except Exception as e:
        body = None
    try:
        price = soup.find("span", class_="price").text
    except Exception as e:
        price = None
    try:
        area = soup.find("span", class_="square").text
    except Exception as e:
        area = None
    try:
        location = soup.find("div", class_="address").text
    except Exception as e:
        locals = None
    try:
        detail = soup.find("div", class_="infor").text
    except Exception as e:
        detail = None
    data["Title"] = title
    data["Decribe"] = body
    data["Price"] = price
    data["Area"] = area
    data["Location"] = location
    data["Detail"] = detail
    print(data)
    csv_writer.writerow([title, str(body), price, area, location, detail])    
    json.dump(data, json_file, indent = 4)

try:
    with open("alonhadat.csv", "w", newline="", encoding = 'utf-8') as f:
        json_file = open("myfile.json", "w", encoding = 'utf-8')
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
    json_file.close()