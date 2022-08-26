from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def frontp():
    return render_template("index.html") 

@app.route("/index.html")
def index_html():
    return render_template("index.html")        

@app.route("/about.html")
def about_html():
    return render_template("about.html")  

@app.route("/resume.html")
def resume_html():
    return render_template("resume.html")  

@app.route("/contact.html")
def contact_html():
    return render_template("contact.html") 

@app.route("/services.html")
def service_html():
    return render_template("services.html") 

@app.route("/portfolio.html")
def portf_html():
    return render_template("portfolio.html") 

@app.route("/info.html", methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        database = open('database.txt', 'a')
        result = database.write(f'\n {name} \n {email} \n {subject} \n {message}')
        if result:
            return render_template('info.html')           