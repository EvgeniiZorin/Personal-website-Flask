from flask import Flask, render_template, url_for, redirect
# from flaskext.markdown import Markdown

app = Flask(__name__)
# Markdown(app)

@app.route('/') # Decorator
@app.route('/home')
def home_route():
	return render_template('home.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)

