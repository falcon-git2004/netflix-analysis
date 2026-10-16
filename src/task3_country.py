import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("outputs/Netflix_cleaned.csv")
print(df.shape)

known = df[df["country"] != "Unknown"]
print(known.shape)
top10 = known["country"].value_counts().head(10)
#print(top10)
share = top10 / len(known) * 100
#print(share.round(1))



top10.sort_values().plot(kind="barh", color="red")
plt.title("Top 10 Countries by Number of Netflix Titles")
plt.xlabel("Number of titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("outputs/task3_top10_countries.png", dpi=200)
#plt.show() 
mix = pd.crosstab(known["country"], known["type"])
#print(mix.head())
mix10 = mix.loc[top10.index]
#print(mix10)
mix10.iloc[::-1].plot(kind="barh", stacked=True, color=["red", "black"])
plt.title("Movies vs TV Shows in the Top 10 Countries")
plt.xlabel("Number of titles")
plt.ylabel("")
plt.legend(title="")
plt.tight_layout()
plt.savefig("outputs/task3_movies_vs_tv.png", dpi=200)
#plt.show()
tv_pct = mix10["TV Show"] / mix10.sum(axis=1) * 100
print(tv_pct.round(1))

tv_pct.sort_values().plot(kind="barh", color="black")
plt.title("TV Show Share of Titles in the Top 10 Countries")
plt.xlabel("TV Shows (% of country's titles)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/task3_tv_share.png", dpi=200)
#plt.show()