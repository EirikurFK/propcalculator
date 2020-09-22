import requests
from bs4 import BeautifulSoup

def get_visir_properties(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    txt = open("soup.txt", "w+")
    txt.write(str(soup))

    apartments = soup.find_all("div", class_="property__details")

    properties = []

    for apartment in apartments:
        size = apartment.find("div", class_="property__size").text
        price = apartment.find("div", class_="property__price").text
        rooms = apartment.find("div", class_="property__arrangement").text
        property_properties = {"size": size, "price": price, "rooms": rooms}
        properties.append(property_properties)
    
    return properties
    
print(get_visir_properties("http://fasteignir.visir.is/search/results/?stype=sale#/?stype=sale&zip=101,102,103,104,105,107,108,109,110,111,112,113,116,162"))