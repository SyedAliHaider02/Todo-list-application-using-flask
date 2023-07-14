from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []


@app.route('/')
def index():
    return render_template('front.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    todo_list.append(item)
    return redirect('/')


@app.route('/remove', methods=['POST'])
def remove():
    item = request.form['item']
    if item in todo_list:
        todo_list.remove(item)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
