from flask import Flask ,request,render_template,redirect,url_for,session

app=Flask(__name__)
app.secret_key="secret"
@app.route("/",methods=["GET","POST"])

def index():
	if request.method=="GET":
		msg="****Welcome to Student Registration****"
		return render_template("index.html",msg=msg)
	if request.method=="POST":
		price={
		"eggs":5,
		"milk":12,
		"bread":22}
		amount=0
		for item in ["eggs","milk","bread"]:
			if item not in session:
				session[item]=int(request.form[item])
			else:
				session[item]+=int(request.form[item])
			amount=amount+session[item]*price[item]
		return render_template("index.html",amount=amount)

if __name__=='__main__':
	app.run(debug=True)	
