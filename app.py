from flask import Flask, render_template, request
# Import your models


app = Flask(__name__)

# Instantiate your models


# Base endpoint to perform prediction.
@app.route('/', methods=['POST'])
def make_prediction():
    return render_template('index.html', prediction=None, generated_text=None, tab_to_show='mnist')


@app.route('/', methods=['GET'])
def load():
    return render_template('index.html', prediction=None, generated_text=None, tab_to_show='mnist')


if __name__ == '__main__':
    app.run(debug=True)