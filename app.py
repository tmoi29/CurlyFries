from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hi():
    print app
    print request.method
    print request.args
    print request.form
    return render_template('stuff.html')

@app.route("/process")
def process():
    print request.args
    return render_template('stuff.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
