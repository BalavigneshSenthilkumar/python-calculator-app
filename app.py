from flask import Flask, request, render_template_string
from db import init_db, save_to_db, fetch_history

app = Flask(__name__)

# Initialize database
init_db()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
</head>
<body>
<h2>Python Calculator</h2>

<form method="post">
    <input type="text" name="expression" placeholder="Enter expression">
    <button type="submit">Calculate</button>
</form>

{% if result %}
<p><b>Result:</b> {{result}}</p>
{% endif %}

<h3>History</h3>
<ul>
{% for expr,res in history %}
<li>{{expr}} = {{res}}</li>
{% endfor %}
</ul>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def calculator():
    result=None
    if request.method=="POST":
        expression=request.form["expression"]
        try:
            result=str(eval(expression))
            save_to_db(expression,result)
        except Exception as e:
            result=f"Error: {e}"

    history=fetch_history()
    return render_template_string(HTML_PAGE,result=result,history=history)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
