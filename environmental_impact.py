"""
EcoTrack - Environmental Impact Module

This module calculates the estimated CO2 savings
from recycled waste materials.
"""


# Estimated CO2 savings per kilogram of recycled material.
# Values are used as educational estimates for this project.
CO2_SAVED_PER_KG = {
    "plastic": 1.5,
    "paper": 0.9,
    "glass": 0.3,
    "metal": 2.0,
    "organic": 0.5
}


def calculate_environmental_impact(waste_log, co2_saved_per_kg):
    """
    Calculate the total estimated CO2 saved from recycled waste.

    Parameters:
        waste_log (list):
            A list containing waste records.

        co2_saved_per_kg (dict):
            A dictionary containing the estimated CO2 savings
            per kilogram for each recyclable material.

    Returns:
        float:
            Total estimated CO2 saved in kilograms.
    """

    total_co2_saved = 0.0

    for entry in waste_log:

        # Get the waste category
        category = entry.get("category", "").lower()

        # Get the waste weight in kilograms
        weight_kg = entry.get("weight_kg", 0)

        # Check whether the waste was recycled
        recycled = entry.get("recycled", False)

        # Only recycled materials contribute to CO2 savings
        if recycled and category in co2_saved_per_kg:

            co2_factor = co2_saved_per_kg[category]

            co2_saved = weight_kg * co2_factor

            total_co2_saved += co2_saved

    return total_co2_saved
