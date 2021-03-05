from flask import Flask, request, jsonify
import predict_image as pi

app = Flask(__name__)

@app.route('/')
def index():
    return 'CNX2021 !'

@app.route('/predict')
def predict():
    p_image_url = request.values['p_image_url']
    res = pi.predicting(p_image_url)
    res = "ที่นี่คือ "+res+" เจ้า"
    result = {'result':res}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
