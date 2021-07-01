from flask import Flask, request,  render_template
import numpy as np
from joblib import load
app = Flask(__name__)

model = load("project.save")

@app.route('/')
def home():
    return render_template(r'index.html')

@app.route('/uploader',methods=['POST'])
def y_predict():
    l=[]
#    l.append(int((request.form.get("Gender"))))
    l.append(int((request.form.get("Married"))))
    l.append(int((request.form.get("Dep"))))
    l.append(int((request.form.get("Education"))))
    l.append(int((request.form.get("self_emp"))))
    l.append(int((request.form.get("Credit_History"))))
    l.append(int((request.form.get("Property_Area"))))
    l.append(np.log(int((request.form.get("ai")))+1))
    l.append(np.log(int((request.form.get("la")))+1))
    l.append(np.log(int((request.form.get("lat")))+1))
    l.append(np.log(int((request.form.get("ai")))+int((request.form.get("cap")))+1))
#    temp= np.log(int(request.form.get("ai")+1))
#    l.append(temp)
    result=model.predict([l])[0]
    
    
    q=['Loan not approved','Loan approved']
    
#    print(x_test)
#    prediction = model.predict(x_test)
#    print(prediction)
#    output=prediction[0]
    
    return render_template('index.html', prediction_text=q[result])







if __name__ == "__main__":
    app.run(debug=True)
