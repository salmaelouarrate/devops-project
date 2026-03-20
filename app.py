from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("home"))

    return render_template("todo.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    try:
        tasks.pop(task_id - 1)
    except IndexError:
        pass
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)