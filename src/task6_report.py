import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("outputs/Netflix_cleaned.csv", parse_dates=["date_added"])

print("Total titles:", len(df))
print(df["type"].value_counts())
print("Countries:", df.loc[df["country"] != "Unknown", "country"].nunique())
print("Release years:", df["release_year"].min(), "-", df["release_year"].max())
print("Last title added:", df["date_added"].max())

df["year_added"] = df["date_added"].dt.year
added = df.groupby(["year_added", "type"]).size().unstack()
print(added)

recent = added.loc[2015:]
recent.plot(kind="bar", stacked=True, color=["red", "black"])
plt.title("Titles Added to Netflix per Year (2021 = partial year)")
plt.xlabel("")
plt.ylabel("Number of titles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/task6_titles_per_year.png", dpi=200)
#plt.show()

tv_share = recent["TV Show"] / recent.sum(axis=1) * 100
#print(tv_share.round(1))

tv_share.plot(marker="o", color="red")
plt.title("TV Show Share of Titles Added per Year")
plt.xlabel("")
plt.ylabel("% of titles added")
plt.tight_layout()
plt.savefig("outputs/task6_tv_share_by_year.png", dpi=200)
#plt.show()


top_countries = df.loc[df["country"] != "Unknown", "country"].value_counts().head(10)
top_genres = df["listed_in"].str.split(", ").explode().value_counts().head(10)

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

recent.plot(kind="bar", stacked=True, color=["red", "black"], ax=axes[0, 0])
axes[0, 0].set_title("Titles Added per Year (2021 = partial)")
axes[0, 0].tick_params(axis="x", rotation=0)

tv_share.plot(marker="o", color="red", ax=axes[0, 1])
axes[0, 1].set_title("TV Show Share of Titles Added (%)")

top_countries.sort_values().plot(kind="barh", color="red", ax=axes[1, 0])
axes[1, 0].set_title("Top 10 Countries")

top_genres.sort_values().plot(kind="barh", color="black", ax=axes[1, 1])
axes[1, 1].set_title("Top 10 Genres")

for ax in axes.flat:
    ax.set_xlabel("")
    ax.set_ylabel("")

fig.suptitle("Netflix Catalogue Dashboard", fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("outputs/task6_dashboard.png", dpi=200)
#plt.show()

print(df["duration_min"].describe().round(1))
tv = df[df["type"] == "TV Show"]
print(tv["seasons"].value_counts().sort_index())
print("TV shows with 1 season (%):", round((tv["seasons"] == 1).mean() * 100, 1))

order = ["Kids", "Older Kids", "Teens", "Adults", "Not Rated"]
rating_pct = pd.crosstab(df["type"], df["rating_group"], normalize="index")[order] * 100
top_ratings = df["rating"].value_counts().head(8).sort_values()
seasons = tv["seasons"].clip(upper=8).astype(int).value_counts().sort_index()

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

rating_pct.plot(kind="barh", stacked=True, ax=axes[0, 0])
axes[0, 0].set_title("Audience Groups: Movies vs TV Shows (%)")
axes[0, 0].set_ylabel("")
axes[0, 0].legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=5)

top_ratings.plot(kind="barh", color="red", ax=axes[0, 1])
axes[0, 1].set_title("Top 8 Ratings")
axes[0, 1].set_ylabel("")

df["duration_min"].dropna().plot(kind="hist", bins=30, color="red", ax=axes[1, 0])
axes[1, 0].axvline(df["duration_min"].median(), color="black", linestyle="--")
axes[1, 0].set_title("Movie Length (minutes, dashed line = median)")
axes[1, 0].set_ylabel("Titles")

seasons.plot(kind="bar", color="black", ax=axes[1, 1])
axes[1, 1].set_title("TV Shows by Seasons (8 = 8 or more)")
axes[1, 1].set_xlabel("")
axes[1, 1].set_ylabel("Titles")
axes[1, 1].tick_params(axis="x", rotation=0)

fig.suptitle("Netflix Audience and Format Dashboard", fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.subplots_adjust(hspace=0.45)
plt.savefig("outputs/task6_dashboard2.png", dpi=200)
plt.show()