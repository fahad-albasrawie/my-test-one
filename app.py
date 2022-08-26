from flask import Flask, render_template, request, redirect, url_for, flash ,jsonify
from wordArrangement import arrange_word, get_all_words

app = Flask("__name__")
app.config["SECRET_KEY"] = "habboon"
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")
    #return render_template("output.html", playerID=playerID)
    
data = get_all_words()
@app.route("/Warcelinta", methods=["POST", "GET"])
def check_plyer_id():
    mixed_word = request.form.get("word_entry")
    posible_answers = arrange_word(mixed_word, data)
    if posible_answers:
        flash("Fadlan xogta buuxi")
        return render_template("answer.html", posible_words=posible_answers)
    return render_template("word_not_found.html", posible_answers=mixed_word)
 
if __name__ == "__main__":
    app.run()
