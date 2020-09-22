import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
# url = "https://bland.is/classified/default.aspx?categoryId=59&sortby=latest&size=200&facets=Area[Höfuðborgarsvæðið]|TypeId[4]|HouseType[HouseType2]|Squaremeters[39%3B500]|iPrices[20000%3B440000]"
url = "https://bland.is/classified/default.aspx?categoryId=59&sortby=latest&size=200&facets=Area[Höfuðborgarsvæðið]|TypeId[4]|HouseType[HouseType2]|iPrices[15000%3B500000]"
page = requests.get(url)

book = Workbook()
sheet = book.active

sheet["A1"] = "Fermetrar"
sheet["B1"] = "Mánaðarleiga"
sheet["C1"] = "Herbergi"
soup = BeautifulSoup(page.content, 'html.parser')

apartments = soup.find_all("div", attrs={"class": "box classifiedentry pagenr1"})

for apartment in apartments:
    size = apartment.find("div", class_="featuredProperty featuredPropertyRight")
    # rooms = apartment.find("div", class_="featuredProperty ")

    price_text = (apartment.find("div", class_="priceTime").text).strip()
    price_text = price_text[:-3].replace(".", "")
    size_text = size.find("div", class_="featuredPropertyValue").text
    # rooms_text = rooms.find("div", class_="featuredPropertyValue").text
    sheet.append([int(size_text), int(price_text)])
    # sheet[f"C{index + 2}"] = rooms_text

book.save(filename="bland_apartments.xlsx")