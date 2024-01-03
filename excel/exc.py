import requests
import bs4

import pandas as pd

x=pd.read_excel('/home/kali/Downloads/Baku Electronics _ 24STREAM.xlsx')

links=x['Link'].to_list()

codes=[]
counter=0
for i in links[:2]:
    if i and i is not None and i != 'none':
        # print('-=-=-==-=-=-=-=-=')
        counter+=1
        # try:
        r=requests.get(links)
        w=bs4.BeautifulSoup(r.text,'html.parser')
    
        code=w.find('span',class_='product__code').text
        # print(counter,':', code.split(':')[1])
        codes.append(code)
    else:
        codes.append(None)
        # print(counter,':',code.split(':')[1])
            
        # except Exception:
        #     codes.append(None)
        #     print(counter,':',code.split(':')[1])
        
    
    
x['ProductCodes']=codes
x.to_excel('products_with_codes.xlsx',index=False)
    
    
    