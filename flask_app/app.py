from flask import Flask, request, render_template

app=Flask(__name__)

#Home page Route
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return "we r programmers... "

## passing json to the fn as paramenter using apis.. 
@app.route("/demo", methods=['POST'])
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
@app.route("/calculator", methods=['POST'])
def calculator():
    if(request.method=="POST"):
        operation = request.form['operation']

        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if (operation == 'add'):
            result = num1 + num2
        elif (operation == 'multiply'):
            result = num1 *num2
        elif (operation == 'divide'):
            result = num1/num2
        else:
            result = num1 - num2

        return render_template("result.html", result=result)
        #return "The operation is {} and result is {}".format(operation,result)

"""
@app.route("/multiply", methods=['POST'])
def multiply():
    if(request.method=="POST"):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = num1 * num2

        return "The operation is {} and result is {}".format(operation,result)

"""
if __name__=="__main__":
    #app.run(host='0.0.0.0')## internal local server ip
    # where ur app is running thatt address is 0.0.0.0
    app.run(host='127.0.0.1',port=3000)
    # by default port is 5000.. make sure port should be avilable