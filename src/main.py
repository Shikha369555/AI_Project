import pandas as pd
from preprocess import clean_text

# load dataset
df = pd.read_csv("../data/data.csv")

# apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# show output
print(df[["text", "clean_text"]])