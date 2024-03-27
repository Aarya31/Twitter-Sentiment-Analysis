import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)



from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your pre-trained sentiment analysis model
model = joblib.load('trained_model (1).sav')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    account_id = request.form.get('account_id')
    account_name = request.form.get('account_name')

    # Use the input data with your sentiment analysis model
    # Replace the following line with the actual logic for sentiment analysis
    sentiment = "Positive"  # Placeholder result

    return render_template('result.html', account_id=account_id, account_name=account_name, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
