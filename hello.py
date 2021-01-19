from flask import Flask, request, render_template 
app = Flask(__name__)  
@app.route('/', methods =["GET", "POST"]) 
def fun(): 
    if request.method == "POST": 
        user_name = request.form.get("name")  
        return "Hello "+user_name 
    return render_template("form.html") 
if __name__=='__main__': 
    app.run() 
