# Import Statements
from flask import Flask, render_template
from blueprints.characters import character_blueprint

# Declare flask app instance
app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

# Blueprints (aka Controllers!)
app.register_blueprint(character_blueprint)

# Listen on port 5000
if __name__ == '__main__':
    app.run()