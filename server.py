from flask import Flask, render_template
app = Flask(__name__)

# always use the decorator
# display the table
@app.route("/")
def display_table():
    users = [
    {'f_name' : 'Michael', 'l_name' : 'Choi'},
    {'f_name' : 'John', 'l_name' : 'Supsupin'},
    {'f_name' : 'Mark', 'l_name' : 'Guillen'},
    {'f_name' : 'KB', 'l_name' : 'Tonel'}
]
    return render_template("index.html",users = users)









if __name__ == "__main__":
    app.run(debug=True)