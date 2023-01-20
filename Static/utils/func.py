import datetime
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

class Authentication:
    def __init__(self):
        self.db=pd.read_csv("Static/utils/db.csv")
        self.uid=len(self.db)
    def login(self,uname,password):
        ls=[False,"",""]
        for i in range(0,len(self.db)):
            if(self.db.email[i]==uname and self.db.password[i]==password):
                ls=[True,self.db.name[i],self.db.uid[i]]
                break
        return ls
    def signup(self,name,email,password):
        dd=pd.DataFrame({"uid":[self.uid],"name":[name],"email":[email],"password":[password]})
        self.uid=self.uid+1
        df=self.db.append(dd)
        df.to_csv("Static/utils/db.csv",index=False)
        return True

        
class Todo:
    def __init__(self):
        self.todo=[]
        self.key=0
    def addTodo(self,uid,todo,comment,date):
        date=pd.to_datetime(date)
        self.todo.append([uid,self.key,todo,comment,date.strftime("%d %B %Y")])
        self.key+=1
    def finishTodo(self,key):
        self.todo=[i for i in self.todo if i[1] != key]
    def displayTodo(self,uid):
        ls=[]
        for i in range(0,len(self.todo)):
            if((self.todo[i][0])==uid):
                ls.append(self.todo[i])
        return ls
            
    # p1=Todo()
    # p1.addTodo(0,"This","message","34")
    # p1.addTodo(1,"This","message","35")
    # p1.addTodo(2,"This","message","36")
    # p1.addTodo(2,"This","message","37")
    # p1.addTodo(1,"This","message","38")
    # p1.addTodo(1,"This","message","39")
    # print(p1.displayTodo(1))
    # p1.finishTodo(4)
    # print(p1.displayTodo(1))

#p2=Authentication()
#print(p2.login("sr@gmail.com","passwords"))
#print(p2.signup("names","sr@gmail.com","passwords"))

