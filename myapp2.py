from flask import Flask,render_template
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)
