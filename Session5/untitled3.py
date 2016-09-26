from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("session6.html")

@app.route('/new')
def new():
    return redirect(url_for('hello_world'))

class Person:
    def __init__(self,name,img): #constructure
        self.name = name
        self.image = img



My_sister = Person("My sister",
                 "http://jobstr.com/user_images/international-flower-buyer-4426.jpg")

Bill_gates = Person("Bill_gates",
                   "http://www.kiemtien.com/wp-content/uploads/2016/03/Bill-Gates.jpg")
# person_list = [My_sister, Bill_gates]
#
# person = {
#     "My sister" = My sister,
#     "Bill_gates" = Bill_gate }


@app.route('/ngahaha')
def view_ngahaha():
    return render_template("session6.html",person=ngahaha)

@app.route("/rm/<name>")
def view_role_models(name):
    return name

@app.route('/rm/<int:index>')
def view_role_model(index):
    return render_template("rolemodel.html",person = person_list[index])

# @app.route('/rm/<name>')
# def view_role_model(name):
#     return name

# bill_gates = Person()
# bill_gates.name = "Bill_gate"
# bill_gates.image = "http://www.kiemtien.com/wp-content/uploads/2016/03/Bill-Gates.jpg"

@app.route('/bill_gates')
def view_billgates():
    return render_template("session6.html",
                           name=bill_gates.name,
                           image=bill_gates.img)


if __name__ == '__main__':
    app.run()
