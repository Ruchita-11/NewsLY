from flask import Flask,render_template,request
from pymongo import MongoClient
from bson import ObjectId

cluster=MongoClient("127.0.0.1:27017")
db=cluster['bvc']
users=db['users']
newsp=db["newsp"]

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/addnews")
def addnews():
    return render_template("form.html")

@app.route("/adminform",methods=['post'])
def adminform():
    d=request.form.get("category")
    f=request.form.get("subcategory")
    a=request.form.get("title")
    b=request.form.get("location")
    e=request.form.get("image")
    c=request.form.get("description")
    newsp.insert_one({"category":d,"subcategory":f,"title":a,"location":b,"image":e,"description":c})
    return render_template("form.html",status="News added successfully")

@app.route("/signupForm", methods=["post"])
def registerData():
    a=request.form.get("username")
    b=request.form.get("email")
    c=request.form.get("password")
    d=request.form.get("cpassword")
    print(a,b,c,d)
    user=users.find_one({"username":a})
    if(user):
        return render_template("signup.html", status="Username Already Exists")
    users.insert_one({"username":a,"email":b,"password":c,"cpassword":d})
    return render_template("login.html", status="Registration Successful")

@app.route("/loginForm", methods=["post"])
def login():
    a=request.form.get("username")
    c=request.form.get("password")
    print(a,c)
    user=users.find_one({"username":a})
    if(user):
        if user['username']=="Manoj" and user['password']=="Mohan":
            return render_template("form.html")
        elif user["password"]==c:
            return render_template("Index.html",)
    return render_template("login.html", result="Invalid Credentials")

@app.route("/sign")
def sign():
    return render_template("signup.html")

@app.route("/log")
def log():
    return render_template("login.html")

@app.route("/use")
def use():
    return render_template("signup.html")

# Index page Routing

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/entertainment")
def entertainment():
    return render_template("ent.html")

@app.route("/politics")
def politics():
    a=newsp.find({"category":"Politics"})
    return render_template("sport1.html",data=a)

@app.route("/technology")
def technology():
    a=newsp.find({"category":"Technology"})
    return render_template("sport1.html",data=a)

@app.route("/government")
def government():
    a=newsp.find({"category":"Business"})
    return render_template("sport1.html",data=a)

@app.route("/weather")
def weather():
    a=newsp.find({"category":"Health"})
    return render_template("sport1.html",data=a)

#Sports page Routing 

@app.route("/sport1")
def sport1():
    a=newsp.find({"subcategory":"cricket"})
    return render_template("sport1.html",data=a)

@app.route("/sport2")
def sport2():
    a=newsp.find({"subcategory":"Football"})
    return render_template("sport1.html",data=a)

@app.route("/sport3")
def sport3():
    a=newsp.find({"subcategory":"Basketball"})
    return render_template("sport1.html",data=a)

@app.route("/sport4")
def sport4():
    a=newsp.find({"subcategory":"Olympics"})
    return render_template("sport1.html",data=a)

@app.route("/sport5")
def sport5():
    a=newsp.find({"subcategory":"Hockey"})
    return render_template("sport1.html",data=a)

@app.route("/sport6")
def sport6():
    a=newsp.find({"subcategory":"Badminton"})
    return render_template("sport1.html",data=a)

#Entertainment page Routing

@app.route("/tollywood")
def tollywood():
    a=newsp.find({"subcategory":"Tollywood"})
    return render_template("sport1.html",data=a)

@app.route("/hollywood")
def hollywood():
    a=newsp.find({"subcategory":"Hollywood"})
    return render_template("sport1.html",data=a)

@app.route("/kollywood")
def kollywood():
    a=newsp.find({"subcategory":"Kollywood"})
    return render_template("sport1.html",data=a)

@app.route("/mollywood")
def mollywood():
    a=newsp.find({"subcategory":"Mollywood"})
    return render_template("sport1.html",data=a)

@app.route("/bollywood")
def bollywood():
    a=newsp.find({"subcategory":"Bollywood"})
    return render_template("sport1.html",data=a)

@app.route("/otherwood")
def otherwood():
    a=newsp.find({"subcategory":"Anime"})
    return render_template("sport1.html",data=a)

#Politics page Routing 

@app.route("/poli1")
def poli1():
    a=newsp.find({"category":"Politics"})
    return render_template("sport1.html")




#Technology page Routing

@app.route("/loc1")
def loc1():
    return render_template("loc1.html")

@app.route("/loc2")
def loc2():
    return render_template("loc2.html")

@app.route("/loc3")
def loc3():
    return render_template("loc3.html")

@app.route("/loc4")
def loc4():
    return render_template("loc4.html")

@app.route("/loc5")
def loc5():
    return render_template("loc5.html")

@app.route("/loc6")
def loc6():
    return render_template("loc6.html")

#Government page routing

@app.route("/gov1")
def gov1():
    return render_template("gov1.html")

@app.route("/gov2")
def gov2():
    return render_template("gov2.html")

@app.route("/gov3")
def gov3():
    return render_template("gov3.html")

@app.route("/gov4")
def gov4():
    return render_template("gov4.html")

@app.route("/gov5")
def gov5():
    return render_template("gov5.html")

@app.route("/gov6")
def gov6():
    return render_template("gov6.html")

#Weather page routing

@app.route("/wet1")
def wet1():
    return render_template("wet1.html")

@app.route("/wet2")
def wet2():
    return render_template("wet2.html")

@app.route("/wet3")
def wet3():
    return render_template("wet3.html")

@app.route("/wet4")
def wet4():
    return render_template("wet4.html")

@app.route("/wet5")
def wet5():
    return render_template("wet5.html")

@app.route("/wet6")
def wet6():
    return render_template("wet6.html")

@app.route("/readarticle")
def readarticle():
    id=request.args.get("id")
    a=newsp.find_one({"_id":ObjectId(id)})
    return render_template("readarticle.html",data=a)

#homepage routing 
@app.route("/homepage")
def homepage():
    return render_template("Index.html")

@app.route("/contactpage")
def contactpage():
    return render_template("contact.html")

@app.route("/aboutpage")
def aboutpage():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
