from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return return_template("contact.html")

@app.route("/course")
def course():
    return render_template("courses.html")

@app.route("/trainers")
def course():
    return render_template("trainers.html")

@app.route("/register",method=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        dob=request.form["dob"]
        gender=request.form["gender"]
        course=request.form["course"]
        return render_template("register.html")
if __name__ =='__main__':
    app.run(debug=True)