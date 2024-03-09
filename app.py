from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    recipes = []
    return render_template('recipes.html', recipes=recipes)










if __name__=='__main__':
    app.run(debug=True)