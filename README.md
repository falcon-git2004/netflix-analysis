# Netflix Data Analysis Using Python

Internship project (Auspify Technologies, Data Analysis Using Python).
Dataset: 8,790 Netflix titles (movies and TV shows).
Tools: Python, pandas.

## Task 1: Data Cleaning and Preparation

Script: `src/task1_cleaning.py`
Output: `outputs/Netflix_cleaned.csv`

### What I did
- Found hidden missing values: the placeholder "Not Given" appeared in `director` (2,588 rows) and `country` (287 rows), so `isna()` showed zero missing.
- Replaced them with "Unknown" instead of deleting rows, to avoid losing about 29% of the data.
- Removed extra spaces from text columns, then removed 4 duplicate titles (same title, type, release year, and country).
- Converted `date_added` from text to a datetime column.
- Grouped 14 ratings into 5 audience groups (`rating_group`): Kids, Older Kids, Teens, Adults, Not Rated.
- Split `duration` into `duration_min` (movies) and `seasons` (TV shows).

### Result
8,786 rows and 13 columns, ready for analysis.

## How to run



## Task 3: Country-Wise Content Analysis

Script: `src/task3_country.py`
Charts: `outputs/task3_top10_countries.png`, `outputs/task3_movies_vs_tv.png`, `outputs/task3_tv_share.png`

I counted titles by production country. 287 titles with an unknown country were excluded, so the percentages below are based on 8,499 titles.

### Key findings
- **Netflix's catalogue is concentrated in a few countries.** The United States alone accounts for 38.1% of titles, and the top 3 countries (US, India, UK) make up about 58%. The top 10 countries cover roughly 78% of everything.
- **Each country has its own content style.** India is almost entirely films (975 movies vs 81 TV shows, only 7.7% TV), while Pakistan (83.1%), South Korea (77.1%) and Japan (66.4%) are mostly TV shows. Most Western countries sit between 26% and 39%.
- **Recommendation:** Netflix could invest in more series from film-heavy markets like India, and more films from series-heavy markets like South Korea, to balance its offering. This is only a hypothesis, because the dataset describes the catalogue and has no viewing data to show what audiences actually watch.

## Task 5: Content Rating and Genre Analysis

Script: `src/task5_rating_genre.py`
Charts: `outputs/task5_top_genres.png`, `outputs/task5_rating_by_type.png`, `outputs/task5_genre_vs_audience.png`

Interactive charts: `outputs/task5_top_genres_interactive.html`, `outputs/task5_genre_vs_audience_interactive.html` (open in any browser)

I grouped the 14 ratings into 5 audience groups, and split the `listed_in` column so each genre is counted separately. A title can have several genres, so genre counts add up to more than the number of titles (19,284 genre labels for 8,786 titles).

### Key findings
- **Netflix leans towards adult audiences.** TV-MA is the most common rating (3,204 titles). Adults make up 45.6% of titles and teens 30.1%, so about 76% of the catalogue targets teens and adults. Children's content (Kids and Older Kids) is only about 23%.
- **TV shows have more children's content than movies.** 29.5% of TV shows are rated for children, compared with 20.8% of movies. Movies are slightly more adult-focused (46.7% vs 43.0%).
- **Genres target different audiences.** Children & Family Movies are 96% children's content, while Independent Movies (71%) and Thrillers (68%) are mostly for adults. Dramas and Comedies, two of the most common genres, are spread between teens and adults.
- **Recommendation:** Children's content is a smaller part of the catalogue, so adding more family titles could be an opportunity for family accounts. This is a hypothesis, because the dataset has no viewing data to show real demand.

## Task 6: Netflix Business Insights Report

Script: `src/task6_report.py`
Charts: `outputs/task6_dashboard.png`, `outputs/task6_titles_per_year.png`, `outputs/task6_tv_share_by_year.png`

For this task I put everything together to get a big-picture view of the catalogue: 8,786 titles (6,123 movies and 2,663 TV shows) from 85 countries. The data stops in September 2021, so I treated 2021 as a partial year and did not compare it directly with full years.

### What I found
- **Netflix added the most titles in 2019.** That year it added 2,013 titles, then 1,879 in 2020. By September 2021 it was at 1,498, but that year isn't finished, so I can't call it a drop.
- **TV shows lost ground, then came back.** They were 41% of new titles in 2016, fell to 25% in 2018, and are back to about 32% in 2020. It's a recovery, not a steady rise.
- **A few countries make up most of the catalogue.** The US alone provides 38.1% of titles with a known country, and the top 10 countries cover about 78%.
- **The content leans towards adults.** Adult-rated titles are 45.6% of the catalogue, while content for children is only about 23%.
- **Most common genres:** International Movies, Dramas and Comedies.
- **Most movies are about 90 to 115 minutes long.** The median is 98 minutes and half of the movies fall between 87 and 114 minutes.
- **Two out of three TV shows have only one season.** That is 67.2% (1,790 of 2,663). The data can't tell us if these shows were cancelled or were planned as one season.


### What I would suggest
1. **Keep an eye on series.** Their share of new titles has been growing again since 2018. Before putting more money into them, Netflix should check how much people actually watch them.
2. **Depend less on a few countries.** Adding more local shows from smaller markets, like South Korea and Japan where most titles are series, would make the catalogue more varied.
3. **Add more family content.** Children's titles are a small part of the catalogue, so there may be room to grow for families.

### Limits of this analysis
The dataset only describes what is in the catalogue. It has no data about viewing, revenue or subscribers, so these suggestions are ideas to test, not proven facts. I also left out the 287 titles with an unknown country when analysing countries.




## How to run
pip install -r requirements.txt
python src/task1_cleaning.py
python src/task3_country.py
python src/task5_rating_genre.py
python src/task6_report.py