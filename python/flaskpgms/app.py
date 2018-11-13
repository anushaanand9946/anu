from flask import Flask,render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def home():
    return 'haiii'
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getNAME=request.form['name']
        return getNAME
    




if(__name__=='__main__'):
    app.run(debug=True)