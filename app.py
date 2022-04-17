from flask import Flask, render_template, request, redirect
import scrapeurl, comparator

app = Flask('app')
app.config["TEMPLATES_AUTO_RELOAD"] = True

url1 = ''
url2 = ''

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    form_name = request.form.get("name","")
    return render_template("final.html", text = form_name)


  else: 
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000)
