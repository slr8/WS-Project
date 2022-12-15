from bs4 import BeautifulSoup
import requests

for page in range(1,50):
  url = "https://www.jumia.com.eg/all-products/" + "?page=" +str(page)+"#catalog-listing"
  Jumia = requests.get(url)
  jsoup = BeautifulSoup(Jumia.content , 'html.parser')
  products = jsoup.find_all('div' , class_ = 'info')

  for product in products:
      Name = product.find('h3' , class_="name").text
      Price = product.find('div' , class_= "prc").text
      try:
        Rating = product.find('div', class_='stars _s').text
      except:
        Rating = 'None'

      info = [ Name, Price,Rating]
      print(info)

