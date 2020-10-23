#Scrum Team Crystal: Eva, Dane, Ida, Nivu, and Crystal

from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/trivia')
def trivia_route():
    #Flask import uses Jinga to render HTML
    return render_template("trivia.html")

@app.route('/numbergame')
def number_routes():
  return render_template("guess_the_number.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')