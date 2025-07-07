from flask import Flask 
app=Flask(__name__)

@app.route("/<nothing>")
def no(nothing):
    return "give the value in side url like this: /fact/<your number>"

def fa(x):   
    if x < 0:
        return "give correct number in positive"
    elif(x==1 or x==0):
        return 1
    else:
        return x * fa(x-1)


@app.route("/fact/<int:n>")
def fact(n):
    result = fa(n)
    if result is None:
        return "Please provide a positive number only."
    return f"Factorial of {n} is {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)