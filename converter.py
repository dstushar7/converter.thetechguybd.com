from flask import Flask, render_template, request, jsonify
import convert as doConvert


converter = Flask(__name__)

@converter.route('/')
def index():
    return render_template('index.html')

@converter.route('/convert', methods=['POST'])
def convert():
    data = request.json
    conversion_type = int(data['type'])
    text = data['text']

    # Implement your conversion logic here
    if conversion_type == 1:
        result = unicode_to_bijoy(text)
    else:
        result = bijoy_to_unicode(text)

    return jsonify(result=result)

def unicode_to_bijoy(text):
    # Implement your conversion logic here
    test = doConvert.Unicode()
    result = test.convertUnicodeToBijoy(text)
    return result

def bijoy_to_unicode(text):
    # Implement your conversion logic here
    return text

if __name__ == '__main__':
    converter.run(debug=True)
