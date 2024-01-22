from flask import Flask, render_template, request
import my_library as ml
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['s1'])
    b = float(request.form['s2'])
    c = float(request.form['s3'])
    area = ml.triangle_area(a, b, c)
    return render_template('result.html', area=area.numpy())


if __name__ == '__main__':
    app.run(debug='True')




