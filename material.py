#SLIDE6 and SLIDE8----------------------------------------------
#Printing Hello World with Flask.

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/',methods=['GET','POST']) #----methods syntax is for slide 8------
def index():
	return "<h1>Hello World!</h1>"#-------<h1> is a HTML header tag,you can return a normal string as well---------


#SLIDE7----------------------------------------------------------
#Intro to Routes.
#Making another route to properly understand the concept of routes.

@app.route('/home') #--------home route
def home():
	return "<h1>You are on the home page </h1>"


@app.route('/json') #optional
def json():
	return jsonify({'key1':'value1','key2':'value2'})

#SLIDE9----------------------------------------------------------
#Route Variables

@app.route('/variable',methods=['GET','POST'],defaults={'name':'User'})
@app.route('/variable/<string:name>',methods=['GET','POST'])
def variable(name):
	return '<h1>Hello {},you are on the variables page'.format(name)

#SLIDE10-----------------------------------------------------------
#Requesting Query String

@app.route('/query')
def query():
	print(request.args)
	nm = request.args.get('name')
	loc = request.args.get('location')
	return '<h1> Hello {} ,you are from {}'.format(nm,loc)

#SLIDE11------------------------------------------------------------

@app.route('/theform',methods=['POST','GET'])
def form():
	return '''<form method="POST" action="/process">
                      Name<input type="text" name="name">
                      <br>
                      Location<input type="text" name="location">
                      <br>	
                      <input type="submit" value="Submit">
                  </form>'''

@app.route('/process',methods=['POST','GET'])
def process():
	nm = request.form.get('name')
	loc = request.form.get('location')
	return "<h1>Hello {}, from {}, you have successfully submitted the form </h1>".format(nm,loc)
	#return redirect(url_for('home', name=name, location=location)) for the redirect, url_for slide


#SLIDE12------------------------------------------------------------
#requesting json data
@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})




if __name__ == "__main__":
	app.run(debug=True)#port is for deployment puropose...


