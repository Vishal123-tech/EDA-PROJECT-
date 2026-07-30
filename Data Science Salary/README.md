# Data Science Salary — Exploratory Data Analysis

Exploratory data analysis of data science salaries using Python, pandas, Matplotlib, and Seaborn.

## Project overview

This project explores salary patterns in data-related roles and visualizes how compensation varies by:

- Work year
- Experience level
- Employment type
- Job title
- Salary distribution
- Employee and company location
- Remote-work ratio
- Company size

The notebook also replaces abbreviated categorical values with more descriptive labels to make the analysis and charts easier to interpret.

## Repository contents

| File | Description |
| --- | --- |
| `Data_Science_Salary-EDA.ipynb` | Main analysis notebook |
| `ds_salaries.csv` | Salary dataset used in the analysis |

## Dataset fields

The dataset includes work year, experience level, employment type, job title, salary, salary currency, salary in USD, employee residence, remote ratio, company location, and company size.

## Getting started

1. Clone this repository:

   ```bash
   git clone https://github.com/Vishal123-tech/EDA-PROJECT-.git
   cd EDA-PROJECT-
   ```

2. Install the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Data_Science_Salary-EDA.ipynb
   ```

4. To run it locally, update the notebook's `pd.read_csv(...)` path to:

   ```python
   pd.read_csv("ds_salaries.csv")
   ```

## Analysis workflow

The notebook follows this sequence:

1. Import the analysis libraries.
2. Load and inspect the dataset.
3. Review shape, data types, missing values, duplicates, unique values, and summary statistics.
4. Identify categorical and numerical columns.
5. Clean and expand abbreviated category labels.
6. Create visualizations for jobs, experience levels, employment types, and salary distributions.

## Source

The dataset is the **Data Science Salaries 2023** dataset. Please review the original dataset license and attribution requirements before redistributing it or using it commercially.

## License

No project-specific license has been added yet. Unless a license is provided, default copyright rules apply to the original work in this repository.
