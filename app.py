from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Hello Every Body'  # مفتاح سري لتشفير الجلسات

# تخزين البيانات بشكل بسيط في الذاكرة (بدون قاعدة بيانات)
problems = []
suggestions = []

@app.route('/')
def index():
    return render_template('index.html', problems=problems, suggestions=suggestions)

@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    problem = request.form['problem']
    if problem:
        problems.append(problem)
        flash('شكراً لك على مشاركتنا مشكلتك!', 'success')
    return redirect(url_for('index'))

@app.route('/submit_suggestion', methods=['POST'])
def submit_suggestion():
    suggestion = request.form['suggestion']
    if suggestion:
        suggestions.append(suggestion)
        flash('شكراً لك على مشاركتنا مقترحك!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
