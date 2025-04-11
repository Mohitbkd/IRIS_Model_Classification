# 🌸 Iris Species Prediction Web App

This is a Flask-based web application that predicts the species of an Iris flower using a machine learning model trained on the classic Iris dataset. The model and label encoder are saved and loaded at runtime. The project is deployed on [Render](https://render.com).

---

## 🚀 Demo

🔗 [Live App on Render](https://your-app-name.onrender.com)  
*(Replace this with your actual Render app URL)*

---

## 🧠 Model Details

The model is trained using scikit-learn on the Iris dataset. It predicts the species of an Iris flower based on the following features:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Output:
- Predicted Species: **Setosa**, **Versicolor**, or **Virginica**

---

## 🗂 Project Structure
├── app.py # Flask app main script 
├── model/ 
│ ├── savemodel.sav # Trained ML model 
│ └── label_encoder.pkl # Label encoder for target variable ├── templates/ 
│ └── index.html # HTML form for user input ├── static/ 
│ └── (optional CSS/JS files) 
├── requirements.txt # Python dependencies 
├── .render.yaml # Render deployment config 
└── README.md # Documentation


---

## ⚙️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Mohitbkd/IRIS_Model_Classification.git
cd iris-flask-app


** 2. Install dependencies ** 

pip install -r requirements.txt

** 3. Run the application **
python app.py


