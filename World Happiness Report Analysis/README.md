# 🌍 World Happiness Report Analysis

An exploratory data analysis project using the **2019 World Happiness Report** to understand how economic conditions, health, social support, freedom, generosity, and perceived corruption relate to national happiness.

The analysis covers **156 countries** and focuses on practical data cleaning, ranking analysis, correlation exploration, and clear visual storytelling.

![Top 10 countries by happiness score](./world_happiness_top10.svg)

## 🎯 Objectives

- Identify the countries with the highest and lowest happiness scores.
- Explore the relationship between happiness and the report's contributing factors.
- Compare the influence of GDP per capita, healthy life expectancy, social support, freedom, generosity, and corruption perceptions.
- Build reproducible notebooks with documented findings and visualizations.

## 📊 Dataset

- **Source:** [World Happiness Report 2019](https://worldhappiness.report/)
- **Coverage:** 156 countries
- **Year:** 2019
- **File:** [data/happiness.csv](./data/happiness.csv)
- **Main fields:** Overall rank, country, happiness score, GDP per capita, social support, healthy life expectancy, freedom, generosity, and perceptions of corruption.

## 🔎 Key Findings

- Finland, Denmark, and Norway rank among the happiest countries in the dataset.
- South Sudan, the Central African Republic, and Afghanistan appear among the least happy countries.
- Happiness has a strong positive relationship with GDP per capita, healthy life expectancy, and social support.
- Freedom has a moderate relationship with happiness, while perceived corruption shows a weaker relationship.
- Generosity has the weakest relationship among the major contributing factors examined.

## 🗂️ Project Structure

~~~text
World Happiness Report Analysis/
├── 01_eda.ipynb        # Dataset overview, quality checks, distributions, and initial visuals
├── 02_analysis.ipynb   # Rankings, correlations, comparisons, and advanced visualizations
├── data/
│   └── happiness.csv   # World Happiness Report dataset
├── world_happiness_top10.svg
├── utils.py
├── requirements.txt
└── README.md
~~~

## 🛠️ Technology Stack

- Python
- pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook

## 🚀 Getting Started

Clone the repository and move into the project folder:

~~~bash
git clone https://github.com/Vishal123-tech/EDA-PROJECT-.git
cd EDA-PROJECT-/World%20Happiness%20Report%20Analysis
~~~

Install the required packages:

~~~bash
pip install -r requirements.txt
~~~

Open the notebooks:

~~~bash
jupyter notebook 01_eda.ipynb
~~~

Run the notebooks from top to bottom to reproduce the analysis and visualizations.

## 📌 Notes

This is an exploratory analysis project. The findings describe relationships in the 2019 data and should not be interpreted as proof of causation.

## 👤 Author

**Vishal Yadav**

Part of the [EDA Project Portfolio](https://github.com/Vishal123-tech/EDA-PROJECT-).
