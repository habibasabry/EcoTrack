"""
EcoTrack — Waste Logging Module

Handles collecting a new waste entry from the user, validating it,
and appending it to the shared waste_log list.
"""

from datetime import date

# The categories the app accepts. "landfill" means it was NOT recycled.
VALID_CATEGORIES = ["plastic", "paper", "glass", "metal", "organic", "landfill"]

# Which categories are counted by piece instead of weighed directly.
# Any category NOT listed here is assumed to be entered directly in kg.
COUNTED_CATEGORIES = {
    "plastic": {"singular": "bottle", "plural": "bottles", "kg_per_unit": 0.02},
    "paper": {"singular": "sheet", "plural": "sheets", "kg_per_unit": 0.005},
}


def log_waste_entry(waste_log):
    """
    Prompts the user for a waste category and weight, validates both,
    and appends a new entry (as a dictionary) to waste_log.

    Parameters:
        waste_log (list): the shared list of waste entry dictionaries

    Returns:
        None — modifies waste_log in place
    """

    print("\n♻️  --- Log a Waste Entry ---")
    print("Valid categories:", ", ".join(VALID_CATEGORIES))

    category = get_valid_category()
    amount, unit, weight_kg = get_valid_amount(category)

    # Only "landfill" counts as NOT recycled — every other category does
    recycled = category != "landfill"

    new_entry = {
        "date": str(date.today()),
        "category": category,
        "amount": amount,          # what the user actually typed (e.g., 5 bottles, or 2.5 kg)
        "unit": unit,               # "bottle/item", "sheet", or "kg"
        "weight_kg": weight_kg,     # always present, always in kg — this is what
                                     # the summary and impact modules read from
        "recycled": recycled
    }

    waste_log.append(new_entry)

    print(f"\n✅ Entry saved: {amount} {unit} of {category} "
          f"(≈ {weight_kg:.3f} kg) logged on {new_entry['date']}.\n")


def get_valid_category():
    """
    Repeatedly asks the user for a category until a valid one is entered.
    Returns the category as a lowercase string.
    """

    while True:
        category = input("Enter waste category: ").strip().lower()

        if category in VALID_CATEGORIES:
            return category

        print(f"\n⚠️  Invalid category. Please choose from: {', '.join(VALID_CATEGORIES)}\n")


def get_valid_amount(category):
    """
    Asks the user for an amount, using the right unit for the category:
    - For categories in COUNTED_CATEGORIES (plastic, paper): asks for a
      whole count (e.g., number of bottles or sheets), then converts it
      to an estimated kg value automatically.
    - For every other category: asks directly for a weight in kg.

    Parameters:
        category (str): the waste category already chosen

    Returns:
        tuple: (amount, unit, weight_kg)
            amount   -> the number the user actually typed
            unit     -> "bottle/item", "sheet", or "kg"
            weight_kg -> always a kg value, for use by other modules
    """

    if category in COUNTED_CATEGORIES:
        unit_info = COUNTED_CATEGORIES[category]
        singular = unit_info["singular"]
        plural = unit_info["plural"]
        kg_per_unit = unit_info["kg_per_unit"]

        while True:
            count_input = input(f"Enter number of {plural}: ").strip()

            try:
                count = float(count_input)

                if count <= 0:
                    print("\n⚠️  Amount must be greater than 0. Please try again.\n")
                    continue

                weight_kg = count * kg_per_unit
                unit_label = singular if count == 1 else plural
                return count, unit_label, weight_kg

            except ValueError:
                print("\n⚠️  Invalid input. Please enter a numeric value (e.g., 5).\n")

    else:
        while True:
            weight_input = input("Enter weight in kg: ").strip()

            try:
                weight = float(weight_input)

                if weight <= 0:
                    print("\n⚠️  Weight must be greater than 0. Please try again.\n")
                    continue

                return weight, "kg", weight

            except ValueError:
                print("\n⚠️  Invalid input. Please enter a numeric value (e.g., 2.5).\n")



