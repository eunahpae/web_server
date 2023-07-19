from flask import Flask, render_template, request, redirect, session
from mysql import Mysql
from data import Articles
import config
import pymysql

app = Flask(__name__)
app.secret_key = "eungok"
mysql=Mysql(password=config.PASSWORD)

@app.route('/' , methods=['GET','POST'])
def index():
    # if request.method == "GET":
    # #    os_info = dict(request.headers)
    # #    print(os_info)
    # #    name = request.args.get("name")
    # #    print(name)
    # #    hello = request.args.get("hello")
    # #    print(hello)
    #    return render_template('index.html')
    # elif request.method == "POST":
    #      data = request.form.get("name")
    #      data_2 = request.form["hello"]
    #      print(data_2)
    #      return render_template('index.html',header="안녕하세요. 배은아입니다.")
    return render_template('index.html')
        
    # req_data = request.data
    # print(req_data)
   
    #  render_template('index.html',jinja2문법(가변키워드인자로 전달받음) 파이썬언어는 {%~~~~%}, 전달할 데이터 직접전달시 {{~~~~}}  )
    


@app.route('/list', methods=['GET'])
def list():
    data = Articles()
    return render_template('list.html',data=data)

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == "POST":
        user_name = request.form["user_name"] 
        email = request.form["email"] 
        phone = request.form["phone"] 
        password = request.form["password"]  
        print(user_name,email,phone,password)
        
        db = pymysql.connect(host=mysql.host, user=mysql.user, db=mysql.db, password=mysql.password, charset=mysql.charset)
        curs = db.cursor()
        sql=f'SELECT * FROM user WHERE email = %s;'
        curs.execute(sql,email)
        
        rows = curs.fetchall()
        print(rows)   
            
        if rows:
            
            return render_template('register.html', data=1)
        else: 
            result=mysql.insert_user(user_name,email,phone,password)
            # print(result)
            return redirect('/login')
    elif request.method == "GET":
        return render_template('register.html',data=0)
    
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
         email = request.form['email']
         password = request.form['password']
         db = pymysql.connect(host=mysql.host, user=mysql.user, db=mysql.db, password=mysql.password, charset=mysql.charset)
         curs = db.cursor()
         sql=f'SELECT * FROM user WHERE email = %s;'
         curs.execute(sql,email)
        
         rows = curs.fetchall()
         print(type(rows))   
            
         if rows:
             result = mysql.verify_password(password,rows[0][4])
             if result:
                 session['is_loged_in'] = True
                 session['user_name'] = rows[0][1]
                 return redirect('/')
             else:
                 return redirect('/login')
         else: 
             return render_template('login.html')

       

if __name__ == '__main__':
    app.run(debug=True)
    # debug=True 파일을 수정해도 재실행안해도 업데이트 되는 코드