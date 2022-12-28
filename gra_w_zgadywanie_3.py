from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    max_num = "0"
    min_num = "1000"
    if request.method == "GET":
        return render_template("start-game.html",min=min_num, max=max_num)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too small":
            max_number = guess
        elif user_answer == "too big":
            min_number = guess
        elif user_answer == "you won":
            return render_template("end-game.html", guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return render_template("game.html", guess=guess, min=min_number, max=max_number)

if __name__ == '__main__':
    app.run()