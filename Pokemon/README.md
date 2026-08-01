# ⚡ Pokémon — Exploratory Data Analysis

An exploratory data analysis project examining Pokémon types, generations, legendary status, and battle statistics through structured cleaning, feature engineering, and visualization.

> **Project question:** How do Pokémon battle attributes vary across generations, types, and legendary status?

## 📌 Project overview

This project uses Python to turn the classic Pokémon dataset into clear, visual insights. The notebook covers data inspection, cleaning, derived features, univariate and multivariate analysis, and correlation analysis.

The analysis focuses on:

- Pokémon type combinations and dual-type classification
- Average battle statistics by generation
- The strongest and weakest Pokémon by individual skills
- Legendary versus non-legendary distribution
- Relationships among HP, Attack, Defense, Special Attack, Special Defense, and Speed
- Type-pair patterns and statistical correlations

## 🗂️ Repository contents

~~~text
Pokemon/
├── Pokemon.ipynb       # Complete exploratory analysis
├── Pokemon.csv         # Source dataset
└── README.md           # Project documentation
~~~

## 🧾 Dataset

The dataset contains **800 Pokémon records** with the following fields:

| Field | Type | Description |
| --- | --- | --- |
| # | Numeric | Original Pokémon identifier |
| Name | Text | Pokémon name |
| Type 1 | Categorical | Primary Pokémon type |
| Type 2 | Categorical | Secondary Pokémon type, when present |
| Total | Numeric | Combined base-stat total |
| HP | Numeric | Health points |
| Attack | Numeric | Physical attack strength |
| Defense | Numeric | Physical defense strength |
| Sp. Atk | Numeric | Special attack strength |
| Sp. Def | Numeric | Special defense strength |
| Speed | Numeric | Speed stat |
| Generation | Numeric | Pokémon generation from 1 to 6 |
| Legendary | Boolean | Whether the Pokémon is legendary |

## 🧹 Data cleaning

The notebook prepares the dataset by:

- Renaming columns for clearer and more consistent naming.
- Replacing spaces in column names with underscores and converting them to lowercase.
- Replacing missing Type 2 values with `No_2nd_Type`.
- Removing unnecessary identifier and aggregate columns when appropriate for analysis.
- Preserving real Pokémon stat values rather than treating unusual values as errors.

## 🧪 Feature engineering

The analysis creates additional features to support deeper comparisons:

- `is_dual_type`: identifies Pokémon with a valid secondary type.
- `average_total`: calculates the average of the six primary battle stats.
- `full_type`: combines Type 1 and Type 2 into one descriptive type label.

The Total stat is defined as:

~~~text
Total = HP + Attack + Defense + Special Attack + Special Defense + Speed
~~~

## 🔍 Analysis workflow

1. Import pandas, NumPy, Matplotlib, Seaborn, and Plotly.
2. Load and inspect the Pokémon dataset.
3. Review data types, missing values, summary statistics, and distributions.
4. Clean column names and represent missing secondary types.
5. Create dual-type, average-stat, and combined-type features.
6. Compare Pokémon skills and average scores across generations.
7. Visualize type distribution, legendary status, stat relationships, and correlations.
8. Summarize the main patterns and limitations.

## 📈 Visual analysis

The notebook includes:

- Minimum and maximum skill comparisons
- Average scores by generation
- Skill-distribution histograms
- Legendary Pokémon proportion
- Generation distribution
- Pokémon stat comparisons
- Type 1 and Type 2 heatmap
- Pairplot of battle statistics
- Correlation matrix

## 💡 Key takeaways

- Total is strongly correlated with the six individual battle statistics because it is calculated from their sum.
- Legendary Pokémon are a minority group, creating an imbalanced Legendary variable.
- Generations have broadly similar distributions, with some differences in average battle attributes.
- Missing Type 2 values represent single-type Pokémon rather than invalid records.
- Outlying stat values are retained because they represent actual Pokémon characteristics, not data-entry errors.

> These findings describe the supplied dataset and should be interpreted as exploratory patterns rather than competitive-battle recommendations.

## 🛠️ Tech stack

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## 🚀 Getting started

Clone the repository and open the project folder:

~~~bash
git clone https://github.com/Vishal123-tech/EDA-PROJECT-.git
cd EDA-PROJECT-/Pokemon
~~~

Install the required libraries:

~~~bash
python -m pip install pandas numpy matplotlib seaborn plotly jupyter
~~~

Launch the notebook:

~~~bash
jupyter notebook Pokemon.ipynb
~~~

When running locally, load the included dataset with:

~~~python
pd.read_csv("Pokemon.csv")
~~~

## 📚 Data source and attribution

The notebook identifies the source as the Kaggle Pokémon dataset. Please review the original dataset license and attribution requirements before redistributing or using it commercially.

## 📄 License

No project-specific license has been added. Unless a license is provided, default copyright rules apply to the original work in this repository.
