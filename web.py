# import requests
# from bs4 import BeautifulSoup
# url ="https://www.11st.co.kr/products/4232515159"
# _get = requests.get(url)    
# html_data =_get.text
# soup = BeautifulSoup(html_data,'html.parser')
# price = soup.find('span',{'class' :'value'})
# _el = price.text
# print(_el)

# _find = html_data.find('<span class="value">')
# _index = price[_find:_find +200]
# spl = _index.split('<span class="value">')
# spl_2 = spl[1].split('</span>')
# print(spl_2[0])

# import requests
# from bs4 import BeautifulSoup
# url ="https://www.11st.co.kr/products/3482281057"
# _get = requests.get(url)
# html_data = _get.text
# soup = BeautifulSoup(html_data,'html.parser')
# title = soup.find('h1',{'class':'title'})
# _el = title.text
# spl =_el.split(' 10cp(1.3kg내외) * 2송이/2개 구매시 5송이 외 파인애플/애플청포도')[0]
# print(spl.strip())

# _find = title.find('<h1 class="title">')
# _index = title[_find:_find +100]
# spl = _index.split('<h1 class="title">')
# spl_1 = spl[1].split('</h1>')
# strip_=spl_1[0].strip()
# print(strip_)


# import requests
# from bs4 import BeautifulSoup
# url ='https://www.11st.co.kr/products/4265804599?inpu=&trTypeCd=22&trCtgrNo=895019'
# _get = requests.get(url)
# html_data = _get.text
# soup = BeautifulSoup(html_data,'html.parser')
# review = soup.find('span',{'class':'flag_text flag_em'})
# _el = review.text
# print(_el)

# _find = stars.find('<span class="flag_text flag_em">추천 리뷰</span>')
# _index = stars[_find:_find +100]

# spl = _index.split('<span class="flag_text flag_em">')

# spl_2 = spl[1].split('</span>') 

# print(spl_2[0])

# import requests
# from bs4 import BeautifulSoup
# url ='https://www.11st.co.kr/products/1828263810'
# _get = requests.get(url)
# html_data = _get.text
# soup = BeautifulSoup(html_data,'html.parser')
# post_office = soup.find('span',{'class':'text_num'})
# _el = post_office.text
# print(_el)


# _find = post_office.find('<span class="text_num">우체국택배/등기</span>')
# _index = post_office[_find:_find+100]

# spl = _index.split('<span class="text_num">')

# spl_1 = spl[1].split('</span>')
# print(spl_1[0])

# import requests
# from bs4 import BeautifulSoup
# url ='https://www.11st.co.kr/products/1883525698?inpu=&trTypeCd=22&trCtgrNo=895019'
# _get = requests.get(url)
# html_data = _get.text
# soup = BeautifulSoup(html_data,'html.parser')
# point = soup.find_all('span',{'class':'text_em2'})
# print(point)
# _el =point.text
# print(_el)

# basket= _get.text
# _find = basket.find('<span>장바구니</span>')
# _index = basket[_find:_find+200]

# spl = _index.split('<span>')

# spl_2 = spl[1].split('</span>')
# print(spl_2[0])





# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.11st.co.kr/products/2423274503'
# res = requests.get(url)
# html_data = res.text
# soup = BeautifulSoup(html_data,'html.parser')
# print(soup)
# review = soup.find('span',{'class':'c_seller_grade c_product_grade_size2 grade_90'})
# _el =review.text


# spl = _el.split('판매자 평점 별')[1].split('개 중 4.4개')[0]
# print(spl)
# spl_2 = _el.split('판매자 평점 별5개 중 ')[1].split('개')[0]
# print(spl_2)

# print(f'평점 :{spl_2}/{spl}')



# _float = float(spl_2)
# _round =round(_float)
# print(_round)
# star = ''
# for idx in range(_round):
#     star+='★'
# print(star)

# for idx in range(5-_round):
#     star+='☆'
# print(star)        


# star = '★'*_round + '☆' *(5 -_round) 
# print(star)


import requests
from bs4 import BeautifulSoup

#html 데이터를 받아오는 함수
# def get_html_data(url):
#     res = requests.get(url)
#     html_data = res.text
#     return html_data
    
    
#score 만큼의 별을 출력해주는 함수
    

# def draw_star(base_star,user_star):
#     _round = round(user_star)
#     star = '★'*_round + '☆' *(base_star -_round) 
    
#     return star
        

# # html 태그에서 원하는 beautifulsoup을 이용하여 원하는 값을 출력하는 함수이다
# def parsing_score(html_data):
    
#     soup = BeautifulSoup(html_data,'html.parser')

#     point_dl = soup.find( 'span', {'class':'c_seller_grade c_product_grade_size2 grade_90'})
#     point =point_dl.text
#     base_star = point.split("판매자 평점 별")[1].split('개 중')[0]
#     user_star = point.split("판매자 평점 별5개 중 ")[1].split("개")[0]
    
#     return (base_star,user_star)
    
# def parsing_title(html_data):
#     soup = BeautifulSoup(html_data,'html.parser')
#     title = soup.find("h1",{"class":"title"})
    
#     return title.text.strip()
# def new_site(html_data):
#     soup =BeautifulSoup(html_data,'html.parser')
#     title =soup.find('div',{'class':'c_product_info_title'})
#     _title = title.findAll



# urls = ['https://www.11st.co.kr/products/1418504992',
# 'https://www.11st.co.kr/products/3749557832', 
# 'https://www.11st.co.kr/products/4773550827',
# 'https://www.11st.co.kr/products/4281523508',
# 'https://www.11st.co.kr/products/4265121026',
# 'https://www.11st.co.kr/products/pa/3823432266',
# ]




# for url in urls:
#     html_data = get_html_data(url)
#     title = parsing_title(html_data)
#     parsing= parsing_score(html_data)
#     star_result = draw_star(int(parsing[0]),float(parsing[1]))
#     print(title,star_result)
    


# import requests
# from bs4 import BeautifulSoup

# url ='https://www.11st.co.kr/products/1883525698?inpu=&trTypeCd=22&trCtgrNo=895019'
# _get = requests.get(url)
# html_data = _get.text
# soup = BeautifulSoup(html_data,'html.parser')
# # point = soup.find('span',{'class':'text_em2'})
# # _el =point.text
# # print(_el)

# point_dl = soup.find( 'dl', {'class':'list'})
# point_dd = point_dl.find_all( 'dd' )

# for item in point_dd:
#     temp = item.find("span", {"class":"text_em2"})
#     k = temp.text
    
    

                                                            





