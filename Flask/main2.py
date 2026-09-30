from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def welcome():
    return "this is a welcome page"




#render templates is a function which fetches the html files from templates folder if
#templates folder doesn't exist it raise an template not found error

@app.route("/index")
def index():
    return render_template("index2.html")





#Methods post and get

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}'
    
    return render_template('forms2.html')



@app.route("/about")
def about():
    return "this is about page"





#Passsing the arguments dynamically

@app.route("/user/<int:marks>")
def user(marks):
    if marks>=40:
        return "hey you passed"
    else:
        return "you failed"




@app.route("/str/<name>")
def str(name):
    return f"hello {name},welcome to this website"



if __name__=="__main__":
    app.run(debug=True)