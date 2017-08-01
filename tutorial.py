from flask import Flask, request, jsonify, session, render_template

app = Flask("My Secret Idea")
app.secret_key = 'super secret key'

# Most Basics


@app.route("/")
def index():
    return "hello"

# Simple data sending


@app.route("/echo/<data>")  # via URL
def echo(data):
    return data


# send it via GET param


@app.route("/echo-query")  # /echo-query/?data=hello
def echo_query():
    return request.args.get('data')


# Session


@app.route("/remember/<data>")
def remember(data):
    if 'data' not in session:
        session['data'] = []
    session['data'].append(data)
    return "OK I won't forget about " + data + " ."


@app.route("/recall")
def recall():
    if 'data' not in session:
        session['data'] = []
    return str(session['data'])


@app.route("/forget", methods=["GET"])
def forget():
    session['data'] = []
    return "What were you saying?"


# Post with Body


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    result = data['x'] + data['y']
    return jsonify({"result": result})


# Templating (Will cover security later)


@app.route("/plain/<name>")
def plain(name):  # painful
    return """
        <!doctype html>
        <html lang="en">
        <head>
          <title>{name}</title>
        </head>
        <body>
            <h1>Hello {name}</h1>
        </body>
        </html>
    """.format(name=name)


@app.route("/template/<name>")
def template(name):  # less painful (still old stuff though)
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', threaded=True)
