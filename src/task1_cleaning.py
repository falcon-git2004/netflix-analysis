import pandas as pd
df = pd.read_csv("data/Dataset.csv")
print(df.shape)

text_cols = ["title", "director", "country", "type", "rating", "listed_in"]
for c in text_cols:
    df[c] = df[c].str.strip()

df = df.replace("Not Given", pd.NA)
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
print(df.isna().sum())

cols = ["title", "type", "release_year", "country"]
df = df.drop_duplicates(subset=cols, keep="first")
print(df.shape)

df["date_added"] = pd.to_datetime(df["date_added"], format="%m/%d/%Y")

rating_group = {
    "TV-Y": "Kids", "TV-G": "Kids", "G": "Kids",
    "TV-Y7": "Older Kids", "TV-Y7-FV": "Older Kids", "TV-PG": "Older Kids", "PG": "Older Kids",
    "TV-14": "Teens", "PG-13": "Teens",
    "TV-MA": "Adults", "R": "Adults", "NC-17": "Adults",
    "NR": "Not Rated", "UR": "Not Rated",
}
df["rating_group"] = df["rating"].map(rating_group)
print(df["rating_group"].isna().sum())

df["duration_value"] = df["duration"].str.split(" ").str[0].astype(int)
df["duration_min"] = df["duration_value"].where(df["type"] == "Movie")
df["seasons"] = df["duration_value"].where(df["type"] == "TV Show")
df = df.drop(columns=["duration_value"])

df.to_csv("outputs/Netflix_cleaned.csv", index=False)
check = pd.read_csv("outputs/Netflix_cleaned.csv")
print(check.shape)
print(check.isna().sum().sum())