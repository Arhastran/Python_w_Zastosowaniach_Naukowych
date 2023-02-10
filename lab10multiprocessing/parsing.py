import requests as re
import re as r
import time
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter
from io import BytesIO
from multiprocessing.pool import Pool

URL="http://www.if.pw.edu.pl/~mrow/dyd/wdprir"
num_process = 10

def get_images(url):
    conn = re.get(url)
    soup = BeautifulSoup(conn.text,'html.parser')
    links = soup.find_all('a', href=r.compile('.*?(?=png)'))
    return [img['href'] for img in links]

def download_and_convert(image_name):
    response = re.get(URL+"/"+image_name)
    img = Image.open(BytesIO(response.content))

    img = img.convert("L")

    img = img.filter(ImageFilter.GaussianBlur(radius = 5))

    img.save(image_name)

def test_sekwencyjne(images):
    start = time.time()
    for entry in images:
        download_and_convert(entry)
    end = time.time()
    print(f"Sekwencyjne przetwarzanie: {end - start}")

def test_wspolbiezne(images):
    start = time.time()
    pool = Pool(processes=num_process)
    pool.map(download_and_convert, images)
    end = time.time()
    print(f"Wspolbiezne przetwarzanie: {end - start}")


images = get_images(URL)
test_sekwencyjne(images)
test_wspolbiezne(images)

