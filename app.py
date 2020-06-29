from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict/", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            cc = float(request.form.get('displacement'))
            hp = float(request.form.get('bhp'))
            wt = float(request.form.get('weight'))
        except:
            return "Some Incorrect Data is Entered"
        else:
            fp = open('Mileage Prediction.pkl', 'rb')
            model = pickle.load(fp)
            fp.close()
            fp = open('scale_model.pkl', 'rb')
            s_model = pickle.load(fp)
            fp.close()
            data = s_model.transform([[cc, hp, wt]])
            prediction = model.predict(data)
            return f"The Mileage will be around {prediction[0]:.2f}"
app.run(host='localhost', debug=True)