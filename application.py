from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/books')
def books():
	return render_template('main.html')
	
if __name__ == '__main__':
	app.degug = True
	app.run(host='0.0.0.0', port=8000)

