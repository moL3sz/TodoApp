def add_todo_db(id_,name,time,done):
    with open("db.txt","a") as db:
        db.write(f"{id_}#{name}#{time}#{done}\n")
def rewrite_db(todos):
    with open("db.txt","w") as db:
        for todo in todos:
            id_,name,time,done = todo["id"],todo["name"],todo["time"],todo["done"]
            db.write(f"{id_}#{name}#{time}#{done}\n")
def get_todo_db():
    with open("db.txt","r") as db:
        res = [{"id":id_,"name":name,"time":time,"done":d.strip()} for id_,name,time,d in [row.split("#") for row in db.readlines()]]
        return res
def update_todo_db(id,done):
    todos = get_todo_db()
    for i in range(len(todos)):
        if todos[i]["id"] == str(id):
            todos[i]["done"] = done
    rewrite_db(todos)
def remove_todo_db(id):
    todos = get_todo_db()
    i = 0
    for todo in todos:
        if todo["id"] == str(id):
            del todos[i]
            break
        i+=1
    rewrite_db(todos)
if __name__ == "__main__":
    get_todo_db()