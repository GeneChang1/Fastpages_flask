from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Nathan/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/Gene/')
def kangaroos():
    return render_template("kangaroos.html")

@app_projects.route('/Toby/')
def walruses():
    return render_template("walruses.html")

@app_projects.route('/Caleb/')
def hawkers():
    return render_template("hawkers.html")