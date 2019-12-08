from flask import Flask, redirect, url_for, request
from calculator import rateGenerator, rateGeneratorController
app = Flask(__name__)

@app.route('/success')
def success():
   i1 = request.args.get('entry',None)
   i2 = request.args.get('exit',None)
   g = rateGeneratorController(i1,i2)
   if g.isValid():
    return g.calculatePayment()
   else:
    return 'Validation Error'

@app.route('/calculator',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      input1 = request.form['entryfield']
      input2 = request.form['exitfield']
      return redirect(url_for('success',entry=input1,exit=input2))
   else:
      input1 = request.args.get('entryfield')
      input2 = request.args.get('exitfield')
      return redirect(url_for('success',entry=input1,exit=input2))

if __name__ == '__main__':
   app.run(host='0.0.0.0')