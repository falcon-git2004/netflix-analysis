import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("outputs/Netflix_cleaned.csv")
print(df.shape)
#print(df["rating"].value_counts())
#print(df["rating_group"].value_counts())
#print(df["rating_group"].value_counts(normalize=True) * 100)


genres = df["listed_in"].str.split(", ")
print(genres.head())

genres = genres.explode()
print(genres.value_counts().head(10))

print(len(df["listed_in"].str.split(", ")))
print(len(genres))

top_genres = genres.value_counts().head(10)

top_genres.sort_values().plot(kind="barh", color="red")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of titles (a title can have several genres)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/task5_top_genres.png", dpi=200)
#plt.show()

order = ["Kids", "Older Kids", "Teens", "Adults", "Not Rated"]
type_group = pd.crosstab(df["type"], df["rating_group"], normalize="index")[order] * 100
print(type_group.round(1))


type_group.plot(kind="barh", stacked=True)
plt.title("Audience Groups: Movies vs TV Shows")
plt.xlabel("% of titles")
plt.ylabel("")
plt.legend(title="", bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig("outputs/task5_rating_by_type.png", dpi=200)
#plt.show()

exploded = df.assign(genre=df["listed_in"].str.split(", ")).explode("genre").reset_index(drop=True)
print(exploded.shape)

top12 = exploded["genre"].value_counts().head(12).index

genre_group = pd.crosstab(exploded["genre"], exploded["rating_group"], normalize="index")[order] * 100
genre_group = genre_group.loc[top12]
print(genre_group.round(0))


plt.figure(figsize=(9, 7))
sns.heatmap(genre_group, annot=True, fmt=".0f", cmap="Reds")
plt.title("Who Is Each Genre Made For? (% of titles)")
plt.xlabel("")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/task5_genre_vs_audience.png", dpi=200)
#plt.show()

top_sorted = top_genres.sort_values()

fig = px.bar(
    x=top_sorted.values,
    y=top_sorted.index,
    orientation="h",
    labels={"x": "Number of titles", "y": ""},
    title="Top 10 Genres on Netflix (interactive)",
)
fig.update_traces(marker_color="red")
fig.write_html("outputs/task5_top_genres_interactive.html")
#fig.show()

fig2 = px.imshow(
    genre_group.round(),
    text_auto=".0f",
    color_continuous_scale="Reds",
    aspect="auto",
    labels={"color": "% of titles"},
    title="Who Is Each Genre Made For? (interactive)",
)
fig2.write_html("outputs/task5_genre_vs_audience_interactive.html")
fig2.show()