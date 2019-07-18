from flask import *
import os
 
app = Flask(__name__)
 
 items =[]
 
 @app.route('/')
def index():
    return render_template('index.html', items = items)
 
 @app.route('/add_todo')
 def add_todo():
     item = request.args.get("item")
     item = append(item)
     return item
    return redirect("http://localhost:5000/", code = 302)



@app.route('/foo/<name>')
def foo(name):
    return render_template('index2.html', to=name)


if __name__ == '__main__':
    port = os.environ.get('Port', 5000)
    app.run(debug=True, host='0.0.0.0', port = port)
