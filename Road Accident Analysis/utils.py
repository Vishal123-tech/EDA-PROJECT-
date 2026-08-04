"""
Road Accident Analysis — Utility Functions
Exploratory data analysis / visualization project. Loads the dataset and provides
helpers and label mapping dictionaries for human-readable reporting.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

SEVERITY_MAP = {1: 'Fatal', 2: 'Serious', 3: 'Slight'}

URBAN_RURAL_MAP = {1: 'Urban', 2: 'Rural', 3: 'Unallocated', -1: 'Data missing'}

ROAD_TYPE_MAP = {
    1: 'Roundabout',
    2: 'One way street',
    3: 'Dual carriageway',
    6: 'Single carriageway',
    7: 'Slip road',
    9: 'Unknown/Other',
    -1: 'Data missing'
}

WEATHER_MAP = {
    1: 'Fine no high winds',
    2: 'Raining no high winds',
    3: 'Snowing no high winds',
    4: 'Fine + high winds',
    5: 'Raining + high winds',
    6: 'Snowing + high winds',
    7: 'Fog or mist',
    8: 'Other',
    9: 'Unknown',
    -1: 'Data missing'
}

LIGHT_MAP = {
    1: 'Daylight',
    4: 'Darkness - lights lit',
    5: 'Darkness - lights unlit',
    6: 'Darkness - no lighting',
    7: 'Darkness - lighting unknown',
    -1: 'Data missing'
}

ROAD_SURFACE_MAP = {
    1: 'Dry',
    2: 'Wet or damp',
    3: 'Snow',
    4: 'Frost or ice',
    5: 'Flood over 3cm deep',
    6: 'Oil or diesel',
    7: 'Mud',
    -1: 'Data missing'
}

DAY_MAP = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}

def load_data(filepath="data/accidents.csv"):
    """Load the raw dataset."""
    return pd.read_csv(filepath, low_memory=False)

def add_mapped_labels(df):
    """Add human-readable string columns for encoded numeric codes."""
    df_out = df.copy()
    if 'collision_severity' in df_out.columns:
        df_out['severity_label'] = df_out['collision_severity'].map(SEVERITY_MAP)
    if 'urban_or_rural_area' in df_out.columns:
        df_out['area_label'] = df_out['urban_or_rural_area'].map(URBAN_RURAL_MAP)
    if 'road_type' in df_out.columns:
        df_out['road_type_label'] = df_out['road_type'].map(ROAD_TYPE_MAP)
    if 'weather_conditions' in df_out.columns:
        df_out['weather_label'] = df_out['weather_conditions'].map(WEATHER_MAP)
    if 'light_conditions' in df_out.columns:
        df_out['light_label'] = df_out['light_conditions'].map(LIGHT_MAP)
    if 'road_surface_conditions' in df_out.columns:
        df_out['road_surface_label'] = df_out['road_surface_conditions'].map(ROAD_SURFACE_MAP)
    if 'day_of_week' in df_out.columns:
        df_out['day_name'] = df_out['day_of_week'].map(DAY_MAP)
    return df_out

def missing_report(df):
    """Per-column missing counts and percentages, worst first."""
    m = df.isnull().sum()
    out = pd.DataFrame({"missing": m, "pct": (100*m/len(df)).round(2)})
    return out[out["missing"] > 0].sort_values("missing", ascending=False)

def top_counts(series, n=10, sep=None):
    """Value counts (optionally splitting multi-value cells on `sep`)."""
    s = series.dropna()
    if sep:
        s = s.str.split(sep).explode().str.strip()
    return s.value_counts().head(n)

def run_chi2_test(df, col1, col2):
    """Run a Chi-Square test of independence between two categorical columns."""
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p_val, dof, expected = chi2_contingency(contingency_table)
    return {
        'chi2': round(chi2, 2),
        'p_value': p_val,
        'dof': dof,
        'contingency_table': contingency_table
    }
