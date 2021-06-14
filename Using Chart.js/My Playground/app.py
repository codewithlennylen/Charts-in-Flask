# https://www.chartjs.org/
# https://www.chartjs.org/docs/latest/samples/line/line.html
# https://www.chartjs.org/docs/latest/samples/other-charts/doughnut.html
# https://www.chartjs.org/docs/latest/samples/other-charts/pie.html
# https://youtu.be/DSlUGncFxa4

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/line')
def home():
    data = [
        ("January", 10),
        ("February", 23),
        ("March", 34),
        ("April", 56),
        ("May", 23),
        ("June", 65),
        ("July", 21),
        ("August", 65),
        ("September", 23),
        ("October", 77),
        ("November", 95),
        ("December", 37),
    ]


    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    values2 = [row[1] for row in reversed(data)]

    return render_template("line.html", labels=labels, values=values, values2=values2)

@app.route('/')
@app.route('/bar')
def bar():
    data = [
        ("January", 15),
        ("February", 23),
        ("March", 34),
        ("April", 56),
        ("May", 23),
        ("June", 65),
        ("July", 21),
        ("August", 65),
        ("September", 23),
        ("October", 77),
        ("November", 95),
        ("December", 37),
    ]


    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("bar.html", labels=labels, values=values)


@app.route('/dougnut')
def dougnut():
    data = [
        ("Lenny", 44),
        ("Georgia", 32),
        ("Fanuel", 39),
        ("Others", 21),
    ]

    colors = [
        '#4dc9f6',
        '#f67019',
        '#f53794',
        '#537bc4',
        '#acc236',
        ]


    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("dougnut.html", labels=labels, values=values, colors=colors)


@app.route('/pie')
def pie():
    data = [
        ("Lenny", 44),
        ("Georgia", 32),
        ("Fanuel", 39),
        ("Others", 21),
    ]

    colors = [
        '#4dc9f6',
        '#f67019',
        '#f53794',
        '#537bc4',
        '#acc236',
        ]


    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("pie.html", labels=labels, values=values, colors=colors)
