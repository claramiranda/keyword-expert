from flask import Flask


app = Flask(__name__)


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)


@app.route('/<string:name>/')
def hello(name):
    return "Hello " + name
app.run()



#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('Clara e Pão')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
