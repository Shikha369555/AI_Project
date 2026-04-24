# 🤖 AI Grievance Classification System

An AI-powered web application that classifies user complaints into the appropriate government department using Machine Learning and Natural Language Processing (NLP).

---

## 🚀 Project Overview

This project automates the process of routing public grievances to the correct department. Users can enter complaints, and the system predicts the relevant department instantly.

---

## 🎯 Features

* 🔹 Text preprocessing (cleaning & normalization)
* 🔹 Feature extraction using TF-IDF
* 🔹 Machine Learning model for classification
* 🔹 Real-time prediction system
* 🔹 Model saving & loading using joblib
* 🔹 Interactive web UI using Streamlit

---

## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit

---

## 📂 Project Structure

```
AI_Project/
│
├── data/
│   └── data.csv
│
├── src/
│   ├── main.py
│   └── preprocess.py
│
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── app.py
├── README.md
```

---

## ⚙️ How It Works

1. User enters a complaint
2. Text is cleaned using preprocessing
3. Converted into numerical features using TF-IDF
4. Trained Logistic Regression model predicts department
5. Result is displayed in UI

---

## 🖥️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/AI_Project.git
cd AI_Project
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

*(or manually install: pandas, scikit-learn, streamlit, joblib)*

### 3. Run the application

```
streamlit run app.py
```

---

## 📊 Example

**Input:**
`Water leakage in my street`

**Output:**
`Predicted Department: Water`

---

## 📈 Future Improvements

* 🔹 Larger dataset for better accuracy
* 🔹 Advanced ML models (Naive Bayes, SVM)
* 🔹 Deployment on cloud (AWS / Render)
* 🔹 Multi-language support
* 🔹 User authentication system

---

## 🎤 Project Description (for Review)

This project is an AI-based grievance classification system that processes user complaints using NLP techniques. It converts text into TF-IDF features and uses a Logistic Regression model to predict the appropriate department. The system also includes a Streamlit-based UI for real-time interaction.

---

## ❤️ Acknowledgement

Developed as part of an AI/ML project to demonstrate real-world application of text classification.

---

## 📌 Author

Your Name
GitHub: https://github.com/Shikha369555

