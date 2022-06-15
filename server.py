from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'test'

@app.route('/')
def welcome():
      return render_template('index.html')

@app.route('/checkout',methods=['POST'])
def user():
    now = datetime.now()
    dt = now.strftime("%B %d, %Y %I:%M %p")
    data = {"name":request.form['name'],"studID":request.form['studID'],
    "strawberry":int(request.form['strawberry']),"banana":int(request.form['banana']),
    "raspberry":int(request.form['raspberry']),"apple":int(request.form['apple']),
    "mango":int(request.form['mango']),"rambutan":int(request.form['rambutan']),"grapes":int(request.form['grapes']),
    'datetime':dt
    }

    return render_template('checkout.html',data=data)

if __name__=="__main__":
    app.run(debug=True)


