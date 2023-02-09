import requests as re
import re as r
import argparse
import os
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
from io import BytesIO
import multiprocessing.dummy
import multiprocessing


def get_images(url):
    conn = re.get(url)
    soup = BeautifulSoup(conn.text,'html.parser')
    links = soup.find_all('a', href=r.compile('.*?(?=png|jpg|jpeg|gif)'))
    return [img['href'] for img in links]


def download_images(url, out, images):
    path = os.getcwd() + f"\\{out}"
    Path(path).mkdir(parents=True, exist_ok=True)

    num_threads = len(images) * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)

    def convert_and_download(img):
        data = Image.open(BytesIO(re.get(url + img).content)).convert("L")
        data.save(f"{path}\\{img}")

    p.map(convert_and_download, [img for img in images])




images = get_images("http://www.if.pw.edu.pl/~mrow/dyd/wdprir")
