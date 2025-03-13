from flask import Flask, request, render_template, url_for, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/l2day1')
def l2day1():
    mp3_url = url_for('static', filename='l2day1.mp3')
    return render_template('l2day1.html', mp3_url=mp3_url)

@app.route('/l2day2')
def l2day2():
    mp3_url = url_for('static', filename='l2day2.mp3')
    return render_template('l2day2.html', mp3_url=mp3_url)

@app.route('/submit_l2day1', methods=['POST'])
def submit_l2day1():
    user_answers = {}
    for key in request.form.keys():
        if key.startswith('answer'):
            user_answers[key] = request.form[key]

    # Log the user answers to a file
    with open('user_answers_day1.log', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {user_answers}\n"
        log_file.write(log_entry)

    return "答案已记录"

@app.route('/submit_l2day2', methods=['POST'])
def submit_l2day2():
    user_answers = {}
    for key in request.form.keys():
        if key.startswith('answer'):
            user_answers[key] = request.form[key]

    # Log the user answers to a file
    with open('user_answers_day2.log', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {user_answers}\n"
        log_file.write(log_entry)

    return "答案已记录"

if __name__ == '__main__':
    app.run(debug=True)



