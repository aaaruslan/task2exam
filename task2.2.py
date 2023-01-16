from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def is_square():
    number = request.form.get("input_number")
    try:
        number = int(number)
        number_1 = number
        if number == 0:
            check = False
        else:
            check = (int(int(number ** (0.5)) ** 2) == number_1)
        if check:
            output = "True"
        else:
            output = "False"
    except:
        output = "Your number is empty or incorrect"
    return render_template("index.html", string=str(output))

if __name__ == '__main__':
    app.run()
