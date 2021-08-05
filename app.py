from os import stat_result
from types import MethodDescriptorType
from flask import Flask,render_template, request
from db import add_todo_db,get_todo_db,remove_todo_db, update_todo_db
import json
app = Flask(__name__,static_folder="/",template_folder="templates/")


@app.route("/get_todos",methods=["GET"])
def get_todos():
    return json.dumps(get_todo_db()), 200
@app.route("/update_row",methods=["POST"])
def update_row():
    id =int(request.form["id"])
    state = request.form["state"]
    print(id,state)
    update_todo_db(id,state)
    return "200"
@app.route("/remove_row",methods=["POST"])
def remove_row():
    id =int(request.form["id"])
    remove_todo_db(id)
    return "200"

@app.route("/add_todo",methods=["POST"])
def add_todo():
    name = request.form["name"]
    time = request.form["time"]
    last_id = 0
    if len(get_todo_db()) != 0:
        last_id = int(get_todo_db()[-1]["id"])+1
    add_todo_db(last_id,name,time,"0")
    print(name,time)
    return "200"
@app.route("/")
def index():
    return render_template("index.html")
    pass

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=80,debug=True)