from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "hello world!"

@app.route("/todos", methods=["GET"])
def get_todos():
  return "get todos"

@app.route("/todos/<id>", methods=["GET"])
def get_todos_detail(id):
  return f"get {id} todos detail"

@app.route("/todos/new", methods=["GET"])
def get_todos_new_page():
  return "get todos new page"

@app.route("/todos", methods=["POST"])
def create_todos():
  return "create todos"

@app.route("/todos/<id>/edit", methods=["GET"])
def get_todos_edit_page(id):
  return f"get {id} todos edit page"

@app.route("/todos/<id>", methods=["PUT"])
def update_todos(id):
  return f"update {id} todos"

@app.route("/todos/<id>", methods=["DELETE"])
def delete_todos(id):
  return f"delete {id} todos"



if __name__ == "__main__" :
  app.run(port= 8000, debug=True)
