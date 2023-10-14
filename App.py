from flask import Flask, render_template, request , redirect, url_for
import random
app = Flask(__name__)

todos = [{
        'id' : 1,
        'name' : 'write SQL',
        'checked' : False,
    },

    {
        'id' : 1,
        'name' : 'write python',
        'checked' : False,
    }
    ] 

@app.route("/", methods=["GET","POST"] )
def home():
    if request.method== "POST" :
       todo_name = request.form["todo_name"]
       cur_id = random.randint(1, 1000)
       todos.append ( 
           { 
           'id' : cur_id,
           'name' : todo_name,
           'checked' : False 

       })
    return render_template ("index.html") 

@app.route("/checked/<int:todo_id>",methods=["POST"])
def checked_todo(todoid):
    for todo in todos:

        if todo['id']== todoid:
            todo['checked']= not todo['checked']
            break
        
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>",methods=["POST"])
def delete_todo(todo_id):
       global todos
       for todo in todos: 
           if todo['id'] == todo_id:
               todos.remove(todo)
               return redirect(url_for("/home"))



       return render_template("index.html", items=todos)
if __name__== "__main__":
    app.run(debug=True)
