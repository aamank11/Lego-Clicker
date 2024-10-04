from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'lego_secret_key'

@app.route('/')
def index():
    if 'points' not in session:
        session['points'] = 0
        session['points_per_click'] = 1
    return render_template('index.html', points=session['points'], points_per_click=session['points_per_click'])

@app.route('/click')
def click():
    session['points'] += session['points_per_click']
    return redirect(url_for('index'))

@app.route('/upgrade')
def upgrade():
    if session['points'] >= 50:
        session['points'] -= 50
        session['points_per_click'] += 1
    return redirect(url_for('index'))

@app.route('/upgrade_10')
def upgrade_10():
    if session['points'] >= 500:
        session['points'] -= 500
        session['points_per_click'] += 10
    return redirect(url_for('index'))

@app.route('/upgrade_100')
def upgrade_100():
    if session['points'] >= 5000:
        session['points'] -= 5000
        session['points_per_click'] += 100
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('points', None)
    session.pop('points_per_click', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
