import re
import requests
from bs4 import BeautifulSoup
import json
def collect_s():
    url = "https://www.11st.co.kr/products/1678632786/review-list"
    _headers = {"content-type": "application/json; charset=UTF-8"
        }
    _data = {"pageSize":20,"pageNo":1,"myProduct":False,"pntVals":[],"rtype":[],"sortType":"01","themeNm":[],"optNm":"","kkukNo":0}
    _post = requests.post(url,headers =_headers, data = json.dumps(_data))
    html_data = _post.text

    soup = BeautifulSoup(html_data,'html.parser')
    reviews = soup.find_all("p",{"class":"cont_review_hide"})
    stars = soup.find_all("p",{"class" :"grade"})
    _list = []
    for idx in range(len(reviews)):
        k = (reviews[idx].text.strip(),stars[idx].text.strip())
        _list.append(k)
        
    return(_list)
    
for idx in collect_s():
    
    print(idx) 
    print("==========")      
    
    


     
# def collect_s():
#     url = "https://www.11st.co.kr/products/1678632786/review-list"
#     _headers = {"content-type": "application/json; charset=UTF-8"
#         }
#     _data = {"pageSize":20,"pageNo":1,"myProduct":False,"pntVals":[],"rtype":[],"sortType":"01","themeNm":[],"optNm":"","kkukNo":0}
#     _post = requests.post(url,headers =_headers, data = json.dumps(_data))
#     html_data = _post.text

#     soup = BeautifulSoup(html_data,'html.parser')
#     stars = soup.find_all("p",{"class" :"grade"})
#     return(stars)   
# for idx in collect_s():
#     print(idx.text.strip())    