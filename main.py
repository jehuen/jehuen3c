from flask import Flask, render_template
app = Flask(__name__)

@app.route('/page1')
def page_1():
    return render_template('page1.html')

@app.route('/page2')
def page_2():
    return render_template('page2.html')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

