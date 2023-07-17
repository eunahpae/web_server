from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == "GET":
       os_info = dict(request.headers)
       print(os_info)
       return render_template('index.html',header=os_info)
    elif request.method == "POST":
       return render_template('index.html',header="안녕하세요, 배은아입니다.")
        
    # req_data = request.data
    # print(req_data)
   
    #  render_template('index.html',jinja2문법(가변키워드인자로 전달받음) 파이썬언어는 {%~~~~%}, 전달할 데이터 직접전달시 {{~~~~}}  )

if __name__ == '__main__':
    app.run(debug=True)
    # debug=True 파일을 수정해도 재실행안해도 업데이트 되는 코드