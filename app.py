from flask import Flask, render_template, url_for, redirect, send_file
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

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/blog/blog_entry/<string:post>')
def blog_entry(post):
	print(f"Argument passed: {post}")
	return render_template(f'blog_entry_{post}.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/download')
def download_file():
	file = 'CV_Data_Science.pdf'
	return send_file(file, as_attachment=True)

if __name__ == '__main__':
	app.run(debug=True)

