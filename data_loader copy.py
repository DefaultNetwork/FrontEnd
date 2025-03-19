"""
data_loader.py
Functions for loading and processing data for the BetterSave Energy Dashboard
"""

import os
import pandas as pd
import streamlit as st

# Load Data with improved error handling
@st.cache_data(ttl=3600)
def load_data():
    """
    Load and preprocess energy generation and consumption data

    Returns:
        tuple: (energy_generation_df, energy_consumption_df)
    """
    try:
        # Use the absolute path of this module's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Since data files are in the same directory as data_loader.py
        data_dir = script_dir

        gen_file = os.path.join(data_dir, "energy_generation_preprocessed.csv")
        cons_file = os.path.join(data_dir, "energy_consumption_preprocessed.csv")

        energy_gen = pd.read_csv(gen_file)
        energy_cons = pd.read_csv(cons_file)

        # Convert dates and handle errors
        energy_gen["Start date"] = pd.to_datetime(energy_gen["Start date"], errors="coerce")
        energy_gen["End date"] = pd.to_datetime(energy_gen["End date"], errors="coerce")
        energy_cons["Start date"] = pd.to_datetime(energy_cons["Start date"], errors="coerce")

        # Add datetime components for more granular analysis
        for df in [energy_gen, energy_cons]:
            df["Year"] = df["Start date"].dt.year
            df["Month"] = df["Start date"].dt.month
            df["Day"] = df["Start date"].dt.day
            df["WeekDay"] = df["Start date"].dt.day_name()
            df["Quarter"] = df["Start date"].dt.quarter
            df["MonthName"] = df["Start date"].dt.month_name()

            # Create a unique ID for each record
            df.insert(0, "ID", range(1, len(df) + 1))

        return energy_gen, energy_cons
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame(), pd.DataFrame()

def filter_data(energy_generation, energy_consumption, year_selection, month_selection, selected_sources):
    """
    Filter data based on year and month selections

    Args:
        energy_generation (DataFrame): Energy generation data
        energy_consumption (DataFrame): Energy consumption data
        year_selection (tuple): (min_year, max_year)
        month_selection (list): List of selected months
        selected_sources (list): List of selected energy sources

    Returns:
        tuple: (filtered_energy_generation, filtered_energy_consumption)
    """
    filtered_energy_gen = energy_generation[
        (energy_generation["Year"] >= year_selection[0]) &
        (energy_generation["Year"] <= year_selection[1]) &
        (energy_generation["Month"].isin(month_selection))
    ]

    filtered_energy_cons = energy_consumption[
        (energy_consumption["Year"] >= year_selection[0]) &
        (energy_consumption["Year"] <= year_selection[1]) &
        (energy_consumption["Month"].isin(month_selection))
    ]

    return filtered_energy_gen, filtered_energy_cons

def get_date_range_values(energy_generation, energy_consumption):
    """
    Get minimum and maximum years from the data

    Returns:
        tuple: (min_year, max_year)
    """
    min_year = int(min(energy_consumption["Year"].min(), energy_generation["Year"].min()))
    max_year = int(max(energy_consumption["Year"].max(), energy_generation["Year"].max()))

    return min_year, max_year

def get_energy_sources(energy_generation):
    """
    Extract available energy sources from the generation data

    Returns:
        list: List of energy source names
    """
    available_sources = [col.replace(" [MWh] Calculated resolutions", "")
                        for col in energy_generation.columns if "[MWh]" in col]

    return available_sources
