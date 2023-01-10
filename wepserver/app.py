from flask import Flask,request,render_template,redirect,url_for

import requests
import json

app = Flask(__name__)

@app.route("/")
def index_page():
    html = render_template("index.html")
    return html
    
@app.route("/$")
def two():
    html = render_template("hahah.html")
    return html

@app.route("/welcome")
def welcome_page():
    user = request.args.get("user")
    if user == None:
        user ="none"
    elif user.isnumeric() == True: # isnumeric 숫자
        user = "admin"
    else:
        user = "guest"
    html = render_template("first.html",user=user)    
    
    return html  
    
@app.route("/calc")
def calculater():
    a =request.args.get("a")
    b =request.args.get("b")
    sym =request.args.get("sym")
    # sign = ["-","+","*","/"]
    if sym == "sum":
        sym = int(a)+int(b)
        sign = "+"
    elif sym == "sub":
        sym = int(a)-int(b)
        sign = "-"
    elif sym == "mul":
        sym = int(a)*int(b)
        sign = "*"
    elif sym == "div":
        sym = int(a)/int(b)
        sign = "/"
    html = render_template("calcualtor.html",zero=a,first=b,second=sym,third=sign)

    return html

@app.route("/board")
def board():
    s = requests.get("http://localhost:1181/get_board_data")
    data = s.json()
        #Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷
    #데이터를 전송할때 사용
    
    html = '''<html>
    <head>
    <title>new create!</title>
    </head>
    <body>
    [Order] [Title] [Date] [Writer] [Content]<br>'''
    for item in data:
        body = "{0} {1} {2} {3}<br>".format(item["title"],item["date"],item["writer"],item["content"])
        html += body
    '''</body>
    </html>
    '''
    return html
    

@app.route("/modify_board_data")
def modify_board_data():
    
    _idx = request.args.get("idx")
    _content = request.args.get("content")
    print(_content)
    _requests = requests.get("http://localhost:1181/modify_board_data?idx={0}&new_data={1}".format(_idx,_content))
    back_data = _requests.json()
    
    if back_data["return"] == True:    
        return redirect(url_for('board'))
    
    elif back_data["return"] == False:
        html = f"<script> alert(\"{back_data['message']}\")</script>"
        return html      
    

@app.route("/create_data")
def create_data():
    # _idx = request.args.get("idx")
    _title = request.args.get("title")
    _writer = request.args.get("writer")
    _date = request.args.get("date")
    _content = request.args.get("content")
    _request = requests.get("http://localhost:1181/create_data?title={0}&writer={1}&date={2}&content={3}".format(_title,_writer,_date,_content))
    
    back_data = _request.json()
    if back_data["return"] == True:
        return redirect(url_for('board'))
    
    elif back_data["return"] == False:
        html = f"<script> alert(\"{back_data['message']}\")</script>"
        return html    
    


@app.route("/delete_data")
def delete_data():
    _idx = request.args.get("idx")
    _request = requests.get("http://localhost:1181/delete_data?idx={0}".format(_idx))
    _data = _request.json()
    if _data["return"] == True:
        return redirect(url_for('board'))
    elif _data["return"] == False:
        html = f"<script> alert(\"{_data['message']}\")</script>"
        return html    
    

    return redirect(url_for('board'))
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",port =1180, debug=True)
    
    


        

    

    














    