from flask import Flask ,render_template
from diff import diff

my_flask_app = Flask(__name__)



@my_flask_app.route ("/")
def index():
        
	return render_template("index.html", diff=diff())

if __name__ == "__main__":
	my_flask_app.run(debug=True)
