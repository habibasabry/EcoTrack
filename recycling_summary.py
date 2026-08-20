"""
EcoTrack — Recycling Summary Module

Calculates and displays a summary of recorded waste by category,
including total waste, recycled waste, and the overall recycling rate.
"""


def calculate_recycling_summary(waste_log):
    """
    Calculate and display the recycling summary from the shared waste log.

    Parameters:
        waste_log (list): A list of waste entry dictionaries.

    Returns:
        None
    """

    # Handle the case where no waste records are available.
    if not waste_log:
        print("\nNo waste records available.")
        return

    category_totals = {}
    total_waste = 0
    recycled_waste = 0

    # Process each waste record.
    for entry in waste_log:
        category = entry["category"]
        weight = entry["weight_kg"]

        # Add the weight to its corresponding category.
        if category in category_totals:
            category_totals[category] += weight
        else:
            category_totals[category] = weight

        total_waste += weight

        # Count only entries marked as recycled.
        if entry["recycled"]:
            recycled_waste += weight

    # Calculate the overall recycling rate.
    recycling_rate = (recycled_waste / total_waste) * 100

    # Display the recycling summary.
    print("\n📊 --- Recycling Summary ---")

    for category, weight in category_totals.items():
        print(f"{category.title()}: {weight:.2f} kg")

    print(f"\nTotal Waste: {total_waste:.2f} kg")
    print(f"Recycled Waste: {recycled_waste:.2f} kg")
    print(f"Overall Recycling Rate: {recycling_rate:.2f}%")
