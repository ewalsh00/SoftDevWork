import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/data")
def data():
    data = []
    with open("data.csv") as csv_file:
        reader = csv.reader(csv_file)
        # skip the first row, which is the header row
        next(reader)
        for entry in reader:
            data.append({'school': entry[1], 'testtakers': int(entry[2]), 'reading': int(entry[3]), 'math': int(entry[4]), 'writing': int(entry[5])})

    data = jsonify(data)
    return data



if __name__ == "__main__":
    app.debug = True
    app.run()
