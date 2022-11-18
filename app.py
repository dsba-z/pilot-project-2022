import importlib
import inspect
import io
import os
from contextlib import redirect_stdout

from flask import Flask, render_template, request

functions_list = []
app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.before_first_request
def make_tasks_list():
    modules = []
    workshops_directory = "src/workshops"
    for path, directory, module in os.walk(workshops_directory):
        for cur in module:
            if "__init__" in cur:
                break
            if ".pyc" in cur:
                break
            with open(os.path.join(workshops_directory, cur), encoding='utf-8') as f:
                source_code = ''.join(f.readlines())
                if "input()" in f.read():
                    break
            module = importlib.import_module(workshops_directory.replace('/', '.') + "." + cur.replace(".py", ""))
            for func in [i[1] for i in inspect.getmembers(module, inspect.isfunction)]:
                docstring = inspect.getdoc(func)
                if docstring is not None:
                    doc_first_line = docstring.split("\n", maxsplit=1)[0]
                    functions_list.append({"prompt": doc_first_line, "function": func, "source_code": source_code,
                                           "id": len(functions_list)})


@app.route('/')
def index():
    return render_template("index.html", title="Pilot project 2022", tasks=functions_list)


@app.route('/task', methods=('GET', 'POST'))
def task():
    task_id = int(request.args.get('id'))
    current_task = functions_list[task_id]

    if request.method == 'POST':
        task_input = request.form['task_input']
        task_output = ''
        try:
            f = io.StringIO()
            with redirect_stdout(f):
                task_output = current_task['function'](task_input)
            if f.getvalue() != '':
                task_output = f.getvalue()
        except Exception as e:
            task_output = str(e)
        return render_template("task.html", title=current_task["prompt"], task=current_task,
                               output=task_output)
    return render_template("task.html", title=current_task["prompt"], task=current_task)
