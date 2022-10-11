# import requests
# url ="https://www.11st.co.kr/products/4232515159"
# _get = requests.get(url)    
# price =_get.text
# _find = price.find('<span class="value">')

# _index = price[_find:_find +200]

# spl = _index.split('<span class="value">')

# spl_2 = spl[1].split('</span>')

# print(spl_2[0])

# import requests
# url ="https://www.11st.co.kr/products/3482281057"
# _get = requests.get(url)
# title = _get.text
# _find = title.find('<h1 class="title">')
# _index = title[_find:_find +100]


# spl = _index.split('<h1 class="title">')

# spl_1 = spl[1].split('</h1>')
# strip_=spl_1[0].strip()
# print(strip_)

# import requests
# url ='https://www.11st.co.kr/products/4265804599?inpu=&trTypeCd=22&trCtgrNo=895019'
# _get = requests.get(url)
# stars = _get.text
# _find = stars.find('<span class="flag_text flag_em">추천 리뷰</span>')
# _index = stars[_find:_find +100]

# spl = _index.split('<span class="flag_text flag_em">')

# spl_2 = spl[1].split('</span>') 

# print(spl_2[0])

# import requests
# url ='https://www.11st.co.kr/products/1828263810'
# _get = requests.get(url)
# post_office = _get.text
# _find = post_office.find('<span class="text_num">우체국택배/등기</span>')
# _index = post_office[_find:_find+100]

# spl = _index.split('<span class="text_num">')

# spl_1 = spl[1].split('</span>')
# print(spl_1[0])

# import requests

# url ='https://www.11st.co.kr/products/1883525698?inpu=&trTypeCd=22&trCtgrNo=895019'
# _get = requests.get(url)
# basket= _get.text
# _find = basket.find('<span>장바구니</span>')
# _index = basket[_find:_find+200]

# spl = _index.split('<span>')

# spl_2 = spl[1].split('</span>')
# print(spl_2[0])

from gettext import find
import requests
from bs4 import BeautifulSoup
url = 'https://www.11st.co.kr/products/2423274503'
res = requests.get(url)
html_data = res.text
soup = BeautifulSoup(html_data,'html.parser')
review = soup.find('span',{'class':'c_seller_grade c_product_grade_size2 grade_90'})
_el =review.text
print(review)
print(_el)

spl = _el.split('판매자 평점 별')[1].split('개 중 4.4개')[0]
print(spl)
spl_2 = _el.split('판매자 평점 별5개 중 ')[1].split('개')[0]
print(spl_2)

print(f'평점 :{spl_2}/{spl}')
























