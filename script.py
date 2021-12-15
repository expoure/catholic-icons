from bs4 import BeautifulSoup 
import requests
import os

def create_dir(url):
    urlCategoryName = url.split("/", 5)[4]
    # Directory
    dir_ = urlCategoryName
    # Parent Directory path
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    # Path
    path = os.path.join(parent_dir, dir_)
    if os.path.exists(urlCategoryName):
        return path
    os.mkdir(path)
    return path


iconsCategoryList = [
    "https://www.monasteryicons.com/category/icons-of-christ/a",
    "https://www.monasteryicons.com/category/icons-of-the-virgin-mary/a",
    "https://www.monasteryicons.com/category/icons-of-the-great-feasts/a",
    "https://www.monasteryicons.com/category/icons-of-the-holy-angels/a",
    "https://www.monasteryicons.com/category/icons-of-saints/a",
    "https://www.monasteryicons.com/category/women-saints/a",
    "https://www.monasteryicons.com/category/icons-of-modern-and-new-world-saints/a",
    "https://www.monasteryicons.com/category/monastery-icons-christmas-icons/a",
    "https://www.monasteryicons.com/category/icon-crucifixes/a",
    "https://www.monasteryicons.com/category/most-recent-additions/a",
    "https://www.monasteryicons.com/category/original-icons-of-the-virgin-mary/a",
    "https://www.monasteryicons.com/category/original-icons-of-the-saints-and-angels/a",
    "https://www.monasteryicons.com/category/16-by-20-original-icons/a",
    "https://www.monasteryicons.com/category/cathedral-size-original-icons/a",
    "https://www.monasteryicons.com/product/saint-scholastica-icon-423/s"
]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for url in iconsCategoryList:
    pageResponse = requests.get(url, headers=headers)
    pageSoup = BeautifulSoup(pageResponse.text, "html.parser")
    pageImgsTags = pageSoup.find_all('img', {'class': 'product_image'})
    for img in pageImgsTags:
        if img.has_attr('src'):
            response = requests.get(img['src'].replace('thumb', 'popup'))
            if img.has_attr('title'):
                name = img['title']
            elif img.has_attr('alt'):
                name = img['alt']
            with open(create_dir(url) + "/" + name + '.png', 'wb') as handler:
                handler.write(response.content)
