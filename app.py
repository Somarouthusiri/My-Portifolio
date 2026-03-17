from flask import Flask, render_template

# Configure Flask to use your specific folders
app = Flask(__name__, template_folder='Templates', static_folder='Static', static_url_path='/Static')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/education.html')
def education():
    return render_template('education.html')

@app.route('/skills.html')
def skills():
    return render_template('skills.html')

@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000)
