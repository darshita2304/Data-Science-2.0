from flask import Flask, request, render_template
import pandas as pd

billapp =Flask(__name__)

#Home page Route
@billapp.route("/")
def hello_world():
    return render_template("bill.html")

@billapp.route("/aboutus")
def aboutus():
    return "we r programmers... "

## passing json to the fn as paramenter using apis.. 
@billapp.route("/demo", methods=['POST'])
def math_operation():
    if(request.method=="POST"):
        operation = request.json['operation']

        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = 0

        if (operation == 'add'):
            result = num1 + num2
        elif (operation == 'multiply'):
            result = num1 *num2
        elif (operation == 'division'):
            result = num1/num2
        else:
            result = num1 - num2

        return "The operation is {} and result is {}".format(operation,result)


## passing form data to the calculator url..
@billapp.route("/calculate_bill", methods=['POST'])
def calculator():
    if(request.method=="POST"):

        products = request.form.getlist('product')
        quantity = request.form.getlist('quantity')
        prices = request.form.getlist('price')

        quantity = list(map(int,quantity))
        prices = list(map(int, prices))

        total = [quantity[i] * prices[i] for i in range(len(products))]

        result = sum(total)
        finaltotal = result

        if( result < 1000): # 10% discount
            finaltotal = result - (result*0.1)
        elif( result < 2000): #20% discount
            finaltotal = result - (result * 0.2)
        elif( result >= 2000): # 30% discount
            finaltotal = result - (result * 0.3)

        return render_template("result.html", result=finaltotal)
        #return result

if __name__=="__main__":
    #billapp.run(host='0.0.0.0')## internal local server ip
    # where ur billapp is running thatt address is 0.0.0.0
    billapp.run(debug=True)
    billapp.run(host='127.0.0.1',port=3000)
    # by default port is 5000.. make sure port should be avilable