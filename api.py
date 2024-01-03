

import requests
from bs4 import BeautifulSoup

s = 1

for page_number in range(1, 6):  
    base_url = f"https://www.bakuelectronics.az/catalog/avto-ve-moto-mehsullari/motosiklet/?page={page_number}"
    r = requests.get(base_url)
    data = BeautifulSoup(r.text, "html.parser")

    for card in data.select(".product__card"):
        href = card.select_one("a").attrs["href"]
        get_data = requests.get(href)
        data = BeautifulSoup(get_data.text, "html.parser")
        all_images_div = data.select('.product__gallery-nav')
        pro_code = data.find('span', class_='product__code').text

        with open(f'vahid1.txt', 'a') as f:  
            f.write(f'{pro_code}\n')
            for images in all_images_div:
                for img_tag in images.select('img'):
                    f.write(f'{s}. https://www.bakuelectronics.az{img_tag.attrs["src"]}\n')
                    s += 1
            f.write('\n')