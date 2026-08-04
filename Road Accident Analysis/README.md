# Road Accident Analysis

An **EDA / Visualization & Statistical Analysis** project exploring UK road collisions in 2021 (**101,087 records**) from the UK Department for Transport (DfT), examining collision severity, vehicle/casualty footprints, peak crash timing, speed limit lethality thresholds, and environmental risk factors.

## Problem Statement
When do crashes happen, how severe are they, and what roadway and environmental conditions surround them? This project provides grounded exploratory data analysis, data storytelling, categorical label mapping, and statistical independence testing.

## Dataset
- **Source**: [UK DfT Road Safety Data, 2021 collisions](https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data) (`dft-road-casualty-statistics-collision-2021.csv`)
- **101,087 collisions × 15 columns**: `collision_index`, `date`, `day_of_week`, `time`, `collision_severity`, `number_of_vehicles`, `number_of_casualties`, `speed_limit`, `light_conditions`, `weather_conditions`, `road_surface_conditions`, `urban_or_rural_area`, `road_type`, `longitude`, `latitude`.

## Project Structure
```
Road Accident Analysis/
├── 01_eda.ipynb        # Dataset structure, completeness, numeric & mapped categorical distributions
├── 02_analysis.ipynb   # Severity breakdown, peak timing, speed limit & urban/rural exposure, Chi-Square statistical testing
├── utils.py            # Code label dictionaries (SEVERITY_MAP, ROAD_TYPE_MAP, etc.), label mapping & chi2 test helpers
├── requirements.txt    # Dependencies (pandas, numpy, matplotlib, seaborn, scipy, jupyter)
├── README.md           # Project documentation and key findings
└── data/
    └── accidents.csv   # Raw UK collision dataset
```

## Key Findings
All figures produced by executing the updated notebooks, grounded in empirical data:
- **101,087 Collisions in 2021**: **77.5% slight (78,329)**, **21.1% serious (21,284)**, and **1.5% fatal (1,474)**.
- **Peak Temporal Risk**: Crashes peak on **Fridays (16.2% of weekly crashes)** and specifically during the **15:00 to 18:00 evening rush hour** (combining school-run and commute traffic).
- **Urban Volume vs. Rural Lethality Paradox**:
  - **~68% of collisions occur in Urban areas** due to higher junction and traffic density.
  - However, **rural and high-speed roads are far deadlier per crash**: the fatal share rises sharply from **1.0% on 30mph roads** up to **3.5%–4.2% on 60–70mph roads**.
- **Road Type Dominance**: **Single carriageways** account for ~72.3% of all collisions (73,054 crashes), followed by dual carriageways (~15.1%).
- **Statistical Independence Testing**: $\chi^2$ Chi-Square tests confirm that **Speed Limit**, **Urban/Rural Area**, and **Light Conditions** have a statistically significant relationship with **Collision Severity** ($p < 10^{-100}$).

## Tech Stack
- Python 3.x
- pandas, numpy, matplotlib, seaborn, scipy

## Getting Started
```bash
pip install -r requirements.txt
jupyter notebook 01_eda.ipynb
```
