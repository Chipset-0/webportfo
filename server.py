from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

price = "$3.50"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def renderpage(page_name):
    return render_template(page_name + ".html")

@app.route('/submit_form', methods=["POST", "GET"])
def submitform():
	if request.method == "POST":
		data = request.form.to_dict()
		write_csv_database(data)
		return redirect("/")

def write_database(data):
	with open('database.txt', mode='a') as database:
		name = data["name"]
		email = data["email"]
		message = data["message"]
		file = database.write(f"\n{name}, {email}, {message}")

def write_csv_database(data):
	with open('database.csv', mode='a', newline='') as database2:
		name = data["name"]
		email = data["email"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter=",", quotechar="|", quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, email, message])