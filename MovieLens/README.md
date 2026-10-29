# 🎬 MovieLens Exploratory Data Analysis

An exploratory analysis of the **MovieLens latest dataset**, investigating movie releases, genres, rating behavior, user activity, and highly rated films.

![Genre distribution](./movielens_genre_distribution.png)

## 📊 Dataset at a Glance

- **58,098 movies**
- **27,753,444 ratings**
- **1,108,997 tag applications**
- **283,228 users**
- Data collected from **January 9, 1995 to September 26, 2018**
- Source: [GroupLens MovieLens](https://grouplens.org/datasets/movielens/)

## 🎯 Analysis Questions

### Movie Data

- How many movies were released each year?
- How many movies were released during the most recent years?
- Which genres were most common over time?
- What percentage of movies belongs to each genre?
- Which years had the highest number of releases?

### Rating Data

- What is the distribution of ratings from 0.5 to 5.0?
- How many ratings were submitted each year and month?
- Which users submitted the most ratings?
- How has the number of active users changed over time?
- Which movies received the most ratings?
- Which movies achieved the highest average ratings?
- How do rankings change when only movies with substantial rating counts are considered?

## 🔎 Key Insights

- Movie production and catalog size increase substantially in the later years of the dataset.
- Drama, Comedy, Thriller, and Romance are among the most frequently represented genres.
- Rating activity is concentrated among a small group of highly active users.
- Rating count measures popularity, while average rating measures perceived quality.
- Filtering for movies with a meaningful number of ratings produces more reliable ranking comparisons than using average rating alone.

## 🛠️ Technology Stack

- Python
- pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook

## 🗂️ Project Structure

~~~text
MovieLens/
├── Movie_Recommendation_EDA.ipynb
├── movielens_genre_distribution.png
└── README.md
~~~

## 🚀 Getting Started

~~~bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook Movie_Recommendation_EDA.ipynb
~~~

The notebook uses the MovieLens `movies.csv` and `ratings.csv` files. Download the dataset from GroupLens and update the file paths in the notebook before running it.

## 👤 Author

**Vishal Yadav**

Part of the [EDA Project Portfolio](https://github.com/Vishal123-tech/EDA-PROJECT-).
