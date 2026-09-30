#Skeleton of flask



from flask import Flask



#it creates an instance of flask class
#Which will be your wsgi application

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this best course , hello world"

@app.route("/index")
def index():
    return "Welcome to the index"



#if we don't specify debug=true the the changes made in the code won't dynamically update on web page
if __name__=="__main__":
    app.run(debug=True)             
    