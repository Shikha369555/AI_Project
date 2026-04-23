import pandas as pd
import joblib
from preprocess import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

loaded_model = joblib.load("models/model.pkl")
loaded_vectorizer = joblib.load("models/vectorizer.pkl")



# load dataset
df = pd.read_csv("data/data.csv")

# apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# show output
print(df[["text", "clean_text"]])
from collections import Counter

# combine all cleaned text
all_words = " ".join(df["clean_text"]).split()

# count frequency
word_freq = Counter(all_words)

# show top 10 words
print("\nTop 10 most common words:")
print(word_freq.most_common(10))
print("\n\nInsight:")
print("Most complaints are related to:", word_freq.most_common(1)[0][0])
# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_text"])
print("\nTF-IDF Shape:", X.shape)
print("\nFeature Names:")
print(vectorizer.get_feature_names_out())

y = df[ "department" ]
print("\nTarget values:")
print(y)
print("\nUnique categories:")
print(y.unique())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nTrain shape:", X_train.shape)
print("Test shape:", X_test.shape)
model = LogisticRegression()
model.fit(X_train, y_train)
print("\nModel training completed")
y_pred = model.predict(X_test)
print("\nPredictions:")
print(y_pred)
print("\nActual vs Predicted:")
for actual, pred in zip(y_test, y_pred):
    print(f"Actual: {actual} → Predicted: {pred}")
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)
user_input = input("\nEnter your complaint: ")
print("User Input:", user_input)
clean_input = clean_text(user_input)
print("Cleaned Input:", clean_input)
input_vector = vectorizer.transform([clean_input])
print("Input vector shape:", input_vector.shape)
prediction = model.predict(input_vector)
print("\nPredicted Department:", prediction[0])
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")