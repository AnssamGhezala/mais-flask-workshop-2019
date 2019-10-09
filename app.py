from flask import Flask, render_template, request
from gpt2_predictor import GPT2_predictor
from mnist_predictor import MNIST_predictor


app = Flask(__name__)

mnist = MNIST_predictor()
gpt2 = GPT2_predictor()

# Base endpoint to perform prediction.
@app.route('/', methods=['POST'])
def make_prediction():
    if request.form['predictor'] == 'mnist':
        prediction = mnist.predict(request)
        return render_template('index.html', prediction=prediction, generated_text=None, tab_to_show='mnist')
    elif request.form['predictor'] == 'gpt2':
        prediction = gpt2.predict(request)
        return render_template('index.html', prediction=None, generated_text=prediction, tab_to_show='gpt2')


@app.route('/', methods=['GET'])
def load():
    return render_template('index.html', prediction=None, generated_text=None, tab_to_show='mnist')


if __name__ == '__main__':
    app.run(debug=True)