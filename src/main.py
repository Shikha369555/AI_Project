import pandas as pd
from preprocess import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

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