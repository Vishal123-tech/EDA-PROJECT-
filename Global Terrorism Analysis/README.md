# Global Terrorism Analysis

A reproducible exploratory data analysis project examining global terrorism incidents from 1970 to 2017 using the Global Terrorism Database. The notebooks combine data-quality review, descriptive analysis, visual exploration, geographic comparisons, and perpetrator-group analysis.

## Project Overview

This project uses notebook-based analysis to turn incident-level terrorism records into clear patterns about when, where, how, and against whom attacks occurred. The analysis is descriptive and intended for educational and portfolio use; it does not make causal or predictive claims about terrorism.

## Dataset

- **Source:** Global Terrorism Database
- **Coverage:** 1970–2017
- **Records:** 181,691 attacks
- **Dimensions explored:** country, region, city, year, attack type, target type, weapon type, perpetrator group, success, and suicide indicator

The dataset is not redistributed in this folder. Download the appropriate public release and update the notebook file path before running the analysis.

## Objectives

- Review dataset structure, data types, missing values, and distributions.
- Explore attack volume across years, countries, regions, and cities.
- Compare attack types, target types, weapon types, and perpetrator groups.
- Analyze successful and suicide attacks using descriptive comparisons.
- Present geographic and time-based patterns through charts and maps.
- Communicate findings clearly while documenting data limitations.

## Notebooks

| Notebook | Purpose |
| --- | --- |
| `01_eda.ipynb` | Dataset overview, shape and type checks, missing-value review, univariate distributions, and top-category exploration. |
| `02_analysis.ipynb` | Deeper analysis of attack trends, geography, attack and target categories, perpetrator groups, success, suicide attacks, and visual comparisons. |

## Analysis Workflow

`Raw data → Data inspection → Missing-value review → Exploratory analysis → Visualizations → Findings`

## Technology Stack

- Python
- pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Geographic and categorical visualization

## Key Analysis Areas

- Yearly and regional incident trends
- Country and city-level comparisons
- Attack and target-type distributions
- Weapon-type usage
- Named perpetrator-group activity
- Successful versus unsuccessful attacks
- Suicide-attack patterns
- Geographic visualization and top-category charts

## How to Run

1. Download the relevant Global Terrorism Database release.
2. Place the dataset at the file path expected by the notebooks.
3. Install the analysis dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

4. Run the notebooks in order:

   ```bash
   jupyter notebook 01_eda.ipynb
   ```

   Then open `02_analysis.ipynb` to review the deeper analysis.

## Limitations

- The dataset contains historical, observational records; relationships should not be interpreted as causal.
- Missing, unknown, and inconsistently reported fields can affect comparisons.
- Terrorism classifications and perpetrator-group labels may vary by source and period.
- Results depend on the selected database release and the filtering decisions in the notebooks.
- This project is for education and data-analysis practice, not operational security or forecasting.

## Author

**Vishal Yadav**

Part of the [EDA Project Portfolio](https://github.com/Vishal123-tech/EDA-PROJECT-).
