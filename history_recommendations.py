"""
EcoTrack - History, Search & Recommendations Module

This module provides functions to:
1. Display previous waste entries.
2. Search and filter waste history.
3. Generate recycling recommendations based on performance.
"""


def view_history(waste_log):
    """
    Display all previously recorded waste entries.

    Parameters:
        waste_log (list): List containing waste records.
    """

    # Check whether there are any records to display.
    if not waste_log:
        print("\n📖 No waste records available.")
        return

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                📖  WASTE HISTORY                 ║")
    print("╚══════════════════════════════════════════════════╝")

    # Loop through every waste entry in the waste log.
    for index, entry in enumerate(waste_log, start=1):

        date = entry.get("date", "Unknown")
        category = entry.get("category", "Unknown").capitalize()
        weight = entry.get("weight_kg", 0)
        recycled = entry.get("recycled", False)

        # Convert the Boolean recycling status into
        # a user-friendly message.
        if recycled:
            status = "♻️ Recycled"
        else:
            status = "🗑️ Landfill"

        print(f"\nEntry {index}")
        print(f"Date:     {date}")
        print(f"Category: {category}")
        print(f"Weight:   {weight:.2f} kg")
        print(f"Status:   {status}")

    print("\n======================================")
    print(f"Total Entries: {len(waste_log)}")
    print("======================================")


def search_history(waste_log, filter):
    """
    Search waste history using a category or keyword.

    Parameters:
        waste_log (list): List containing waste records.
        filter (str): Category or keyword used for searching.
    """

    # Check whether the waste log is empty.
    if not waste_log:
        print("\n🔎 No waste records available to search.")
        return

    # Remove unnecessary spaces and make the search
    # case-insensitive.
    filter = filter.strip().lower()

    if not filter:
        print("\n⚠️ Please enter a search term.")
        return

    results = []

    # Check every waste record for a matching category.
    for entry in waste_log:

        category = entry.get("category", "").lower()

        if filter in category:
            results.append(entry)

    # Display a message when no matching records are found.
    if not results:
        print(f"\n🔎 No records found for: {filter}")
        return

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                🔎  SEARCH RESULTS                ║")
    print("╚══════════════════════════════════════════════════╝")

    # Display all matching records.
    for index, entry in enumerate(results, start=1):

        date = entry.get("date", "Unknown")
        category = entry.get("category", "Unknown").capitalize()
        weight = entry.get("weight_kg", 0)
        recycled = entry.get("recycled", False)

        status = "♻️ Recycled" if recycled else "🗑️ Landfill"

        print(f"\nResult {index}")
        print(f"Date:     {date}")
        print(f"Category: {category}")
        print(f"Weight:   {weight:.2f} kg")
        print(f"Status:   {status}")

    print("\n======================================")
    print(f"Records Found: {len(results)}")
    print("======================================")


def generate_recommendations(recycling_rate):
    """
    Generate rule-based recycling recommendations.

    Parameters:
        recycling_rate (float): User's recycling rate as a percentage.
    """

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║             💡  RECOMMENDATIONS                  ║")
    print("╚══════════════════════════════════════════════════╝")

    # Make sure the recycling rate is within a sensible range.
    recycling_rate = max(0, min(100, recycling_rate))

    print(f"\n📊 Your recycling rate: {recycling_rate:.2f}%")

    # Provide recommendations according to the user's performance.
    if recycling_rate < 30:
        print("\n🔴 Recycling Performance: Needs Improvement")
        print("💡 Start separating recyclable materials from landfill waste.")
        print("💡 Focus on recycling paper, plastic, glass, and metal.")
        print("💡 Try to reduce the amount of general/landfill waste.")

    elif recycling_rate < 60:
        print("\n🟠 Recycling Performance: Fair")
        print("💡 You are making progress, but there is room for improvement.")
        print("💡 Increase the amount of recyclable materials you separate.")
        print("💡 Pay special attention to plastic and paper waste.")

    elif recycling_rate < 80:
        print("\n🟡 Recycling Performance: Good")
        print("💡 Keep up your recycling habits!")
        print("💡 Try to reduce landfill waste further.")
        print("💡 Look for additional materials that can be recycled.")

    else:
        print("\n🟢 Recycling Performance: Excellent")
        print("💡 Great job! You have a strong recycling habit.")
        print("💡 Continue maintaining your current recycling practices.")
        print("💡 Encourage others in your household or community to recycle.")

    print("\n🌱 Every small action contributes to a greener community!")


# ----------------------------------------------------------
# TESTING THE MODULE
# ----------------------------------------------------------

if __name__ == "__main__":

    import json

    try:
        # Load existing waste records for testing.
        with open("waste_log.json", "r") as file:
            waste_log = json.load(file)

        # Test 1: View all history
        print("\n--- Testing View History ---")
        view_history(waste_log)

        # Test 2: Search for plastic records
        print("\n--- Testing Search History ---")
        search_history(waste_log, "plastic")

        # Test 3: Test recommendations
        print("\n--- Testing Recommendations ---")
        generate_recommendations(75)

    except FileNotFoundError:
        print("⚠️ waste_log.json was not found.")

    except json.JSONDecodeError:
        print("⚠️ waste_log.json contains invalid data.")
