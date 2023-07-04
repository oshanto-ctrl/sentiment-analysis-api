# Import flask modules and transformers pipeline.
from flask import Flask, request, render_template, jsonify, json
from transformers import pipeline

# Create an instance of Flask app.
app = Flask(__name__)

# Load sentiment-analysis model from Hugging Face
# Transfomers library using pipeline.
model = pipeline('sentiment-analysis')

# Route of home page
@app.route('/')
def home():
    return render_template('home.html')


# Route of sentiment analysis api
@app.route('/analyze', methods=['POST'])
def sentiment_analysis():
    try:
        # The text to be analyzed from the form data
        text = request.form['text']

        # Analyze the sentiment of text using pre-trained model
        result = model(text)[0]
        sentiment = result['label']

        sentiment_jsonify = {}
        # text_jsonify = {}
        
        # Create JSON response.
        json_text = {'text': text}
        json_data = {'sentiment': sentiment} 
        
        # Print JSON respone to command prompt
        sentiment_jsonify = json_data
        print(json.dumps(json_data))

        # Return the rendered template with sentiment and text
        return render_template('home.html', sentiment=sentiment, sentiment_json=sentiment_jsonify, json_text=json_text)

    except Exception as e:
        # If an exception occurs, display an error message in the template
        error_msg = str(e)
        return render_template('home.html', error_msg=error_msg)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


















