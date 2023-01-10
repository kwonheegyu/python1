from flask import Flask,request,render_template #HTTP 통신이 필요한 프로그램을 작성할 때 가장 많이 사용되는 라이브러리입니다
import json

backend = Flask(__name__) # 플라스크는 마이크로 웹 프레임 워크이다 
                        #django와 같이 쓰는 경우도 있다 특히 api서버를 만들기에 매우 편리하다
                        #templates에 저장된 html을 불러올 때 사용하는 함수
@backend.route("/get_board_data")
def get_board_data():
    file = open("backend.txt","r")
    k= file.read()
    _json = json.loads(k)
    
    file.close()
    return _json


@backend.route("/modify_board_data")
def modify_board_data():
    _idx = request.args.get("idx")
    # 1. 기존의 게시글 정보를 불러온다.
    f = open("backend.txt", "r")
    board_data = f.read()   # type: str
    f.close()
    try:
        json_data = json.loads(board_data)
    except Exception as e:
            return {"return": False, "message": f"예외발생: {e.msg}"}
    

    # 2. idx탐색
    target_data = {}
    for item_idx in range(len(json_data)):
        item = json_data[item_idx]
        print(item,_idx)
        if item["idx"] == _idx:
            target_data = item
            break
    
        
        
        

    # item_idx 가 target_data가 저장되어 있는 index번호    
    # 3. idx에 맞는 게시글 수정
    if target_data == {}:
        return {"return": False, "message": "데이터 누락됨"}
    else:
        new_content = request.args.get("new_data")
        print(new_content)
        target_data["content"] = new_content
        json_data[item_idx] = target_data
        
        
        # # 4. 게시글을 파일로 저장
        data = json.dumps(json_data)
        f = open("backend.txt", "w")
        f.write(data)
        f.close()
        return {"return": True, "message": "데이터 수정됨!"}      

@backend.route("/create_data")
def create_data():  
    
    _title = request.args.get("title")
    _writer = request.args.get("writer")
    _date = request.args.get("date")
    _content = request.args.get("content")
    f = open("backend.txt", "r")
    
    board_data = f.read()   # type: str
    f.close()
    json_data = json.loads(board_data)
    if _title== "None" or _writer== "None" or _date== "None" : 
        return {"return": False, "message": "데이터 누락됨"}
    
        
           
        
    else: #정상
        before_idx = len(json_data)-1
        current_idx = before_idx +1
        
        new_data ={"idx":f"{current_idx}","title":f"{_title}","writer":f"{_writer}","date":f"{_date}","content":f"{_content}"}
        print(json_data)
        json_data.append(new_data) 
        
        data = json.dumps(json_data)
        f = open("backend.txt", "w")
        f.write(data)
        f.close()
        return  {"return":True, "message": "추가 생성되었씁니다"}
    
    
@backend.route("/delete_data")
def delete_data():
    _idx = request.args.get("idx")
    f = open("backend.txt", "r")
    
    board_data = f.read()   # type: str
    f.close()
    json_data = json.loads(board_data)
    target_data = {}
    for item_idx in range(len(json_data)):
        item = json_data[item_idx]
        if item["idx"] == _idx:
            target_data = item
            break 
    if  target_data not in json_data :
        
        return {"return":False, "message": "누락되버렸네요!!"}
    
    
        
    else:    
        json_data.remove(target_data)
        for i in range(int(_idx),len(json_data)):
            json_data[i]["idx"] = str(i)
    
        
        
        data = json.dumps(json_data)
        f = open("backend.txt", "w")
        f.write(data)
        f.close()
        
        return {"return":True, "message": "삭제 했습니당!"}       
    
        
        
    
    
    
       

                
if __name__ == "__main__":
    backend.run(host="0.0.0.0",port =1181, debug=True)
                  
                  
    
     
