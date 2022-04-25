from flask import Flask, render_template
import sys

sys.path.insert(1, 'helpers')
# Importing helper packages
from load_model import load_model

app = Flask(__name__)


#Loading the model at app startup
global model
model_name = 'finetuned_BART_epoch_1.model'
model = load_model(model_name)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
    