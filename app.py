from flask import Flask,render_template,request,session
import pandas as pd
from Static.utils  import func



app=Flask(__name__)
app.app_context().push()
app.secret_key = "abc"  


cal=[0,0]
todo=func.Todo()
auth=func.Authentication()





@app.route("/")
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST','GET'])        
def welcome():
    flag=[]
    if request.method=='POST':
        email=str(request.form['email'])
        password=str(request.form['password'])
        flag=auth.login(email,password)
        print(flag)
    session['name']=flag[1]
    session['uid']=int(flag[2])
    if(flag[0]): 
        return render_template("home.html",list=todo.displayTodo(session['uid']),uname=session['name'])
    else:
        return render_template("login.html",func='myFunction()')

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/sign', methods=['POST','GET'])        
def signins():
    if request.method=='POST':
        name=str(request.form['name'])
        email=str(request.form['email'])
        password=str(request.form['password'])
        auth.signup(name,email,password)
    return render_template("login.html",func="")

@app.route("/home")
def home():
    return render_template('home.html',list=todo.displayTodo(session["uid"]),uname=session['name'])

@app.route("/task")
def task():
    return render_template('Task.html',list=todo.displayTodo(session["uid"]))

@app.route("/dashboard")
def dashboard():
    print(cal)
    return render_template('dashboard.html',list=todo.displayTodo(session["uid"]),cal=cal)

@app.route('/add', methods=['POST','GET'])        
def addtodo():
    if request.method=='POST':
        task=str(request.form['task'])
        comment=str(request.form['comment'])
        date=pd.to_datetime(request.form['date'])
        todo.addTodo(session["uid"],task,comment,pd.to_datetime(date))
        cal[0]+=1
    return render_template("Task.html",list=todo.displayTodo(session["uid"]))

@app.route("/finish",methods=['POST','GET'])
def finishtodo():
    ind=int(request.form["keys"])
    Page=str(request.form["page"])
    print(ind)
    todo.finishTodo(ind)
    cal[1]+=1
    return render_template(Page,list=todo.displayTodo(session["uid"]),uname=session['name'])

#todo.addTodo(session["uid"],"day","comment",pd.to_datetime("2023-01-16"))
#todo.addTodo(session["uid"],"week","comment",pd.to_datetime("2023-01-10"))
#todo.addTodo(session["uid"],"monthly","comment",pd.to_datetime("2022-12-16"))


if __name__ == '__main__':
    app.run(debug = False)
