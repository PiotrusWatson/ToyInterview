from flask import Flask, render_template, request, session, redirect
from whois import whois
from config import Config

app = Flask(__name__)
app_config = Config()
app.secret_key = app_config.secret_key

@app.route("/", methods = ("GET", "POST"))
def index():
    if request.method == "POST":
        details = whois(request.form["domain_name"])
        session["whois"] = dict(details)
        session["form_entry"] = request.form["domain_name"]
        return redirect(request.url)
    
    whois_details = session.get("whois", {})
    form_entry = session.get("form_entry", "")
    
    return render_template('index.html', details=whois_details, form_entry=form_entry)


