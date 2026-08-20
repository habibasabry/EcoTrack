import json
import os

from waste_logging import log_waste_entry

from recycling_summary import calculate_recycling_summary

from environmental_impact import (
    calculate_environmental_impact,
    CO2_SAVED_PER_KG
)

from history_recommendations import (
    view_history,
    search_history,
    generate_recommendations
)


# File used to permanently store all waste records.
# JSON persistence allows data to remain available after
# the application is closed and opened again.
DATA_FILE = "waste_log.json"


def display_main_menu():
    """
    Display the main EcoTrack menu and available system functions.
    """

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║              🌱  E C O T R A C K  🌱             ║")
    print("║          Sustainable Waste Tracker ♻️             ║")
    print("║                                                  ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║                                                  ║")
    print("║       ♻️   1. Log Waste                           ║")
    print("║       📊  2. Recycling Summary                   ║")
    print("║       🌍  3. Environmental Impact                ║")
    print("║       📖  4. View Waste History                  ║")
    print("║       🔎  5. Search Waste History                ║")
    print("║       💡  6. Get Recommendations                 ║")
    print("║       🚪  7. Exit                                ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print("          🌿 Small actions. Greener cities. 🌿\n")


def load_data():
    """
    Load previously recorded waste data from the JSON file.

    Returns:
        list: A list containing all saved waste records.
        An empty list is returned if the file does not exist
        or contains invalid data.
    """

    # Check whether the data file exists before attempting
    # to read it.
    if not os.path.exists(DATA_FILE):
        return []

    try:
        # Open the JSON file and convert its contents
        # into Python data.
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

            # Ensure that the stored data has the expected
            # list structure.
            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        # Prevent the application from crashing if the file
        # is corrupted, unreadable, or unavailable.
        print("\n⚠️  Unable to load previous data.")
        print("🌱 Starting with an empty waste log.\n")
        return []


def save_data(waste_log):
    """
    Save the current waste records to the JSON file.

    This provides data persistence so that users do not
    lose their waste history when the application closes.
    """

    try:
        # Write the complete waste log to the JSON file.
        # indent=4 keeps the JSON file readable.
        with open(DATA_FILE, "w") as file:
            json.dump(waste_log, file, indent=4)

    except OSError:
        # Handle file-saving errors without stopping
        # the entire application.
        print("\n⚠️  There was a problem saving your data.")


def get_menu_choice():
    """
    Get and validate the user's menu choice.

    Returns:
        int: A valid menu number between 1 and 7.
    """

    while True:
        choice = input("🌱 Choose an option (1-7): ").strip()

        # Check that the user entered a number.
        if not choice.isdigit():
            print("\n⚠️  Please enter a number from 1 to 7.")
            continue

        choice = int(choice)

        # Accept only menu options that exist.
        if 1 <= choice <= 7:
            return choice

        print("\n⚠️  Invalid choice. Please choose a number from 1 to 7.")


def calculate_current_recycling_rate(waste_log):
    """
    Calculate the current recycling rate for recommendations.

    The function calculates:

        Recycling Rate =
        (Total Recycled Weight / Total Waste Weight) × 100

    Parameters:
        waste_log (list): List of waste records.

    Returns:
        float: Current recycling rate as a percentage.
    """

    # If there are no records, the recycling rate is 0%.
    if not waste_log:
        return 0.0

    total_waste = 0.0
    recycled_waste = 0.0

    # Process every waste record.
    for entry in waste_log:

        # Get the recorded weight safely.
        weight = entry.get("weight_kg", 0)

        try:
            weight = float(weight)
        except (TypeError, ValueError):
            # Ignore invalid weight values.
            continue

        # Ignore negative weights.
        if weight < 0:
            continue

        total_waste += weight

        # Add the weight only when the item was recycled.
        if entry.get("recycled", False):
            recycled_waste += weight

    # Prevent division by zero when all records have zero weight.
    if total_waste == 0:
        return 0.0

    return (recycled_waste / total_waste) * 100


def main():
    """
    Main function that controls the EcoTrack application.

    The function loads saved data, displays the main menu,
    processes user choices, and keeps the application
    running until the user selects Exit.
    """

    # Load existing waste records when the application starts.
    # This ensures that previous user activity is available
    # during the current session.
    waste_log = load_data()

    # Display the EcoTrack welcome message.
    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║            🌿 WELCOME TO ECOTRACK 🌿             ║")
    print("║                                                  ║")
    print("║       Your little step towards a greener city    ║")
    print("║                                                  ║")
    print("║          ♻️   Reduce • Reuse • Recycle  ♻️         ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")

    # Keep displaying the menu until the user chooses Exit.
    while True:

        display_main_menu()
        choice = get_menu_choice()

        # ==========================================================
        # OPTION 1: LOG WASTE
        # ==========================================================
        if choice == 1:

            # Call the Waste Logging Module to collect a new
            # waste record from the user.
            log_waste_entry(waste_log)

            # Save the updated list immediately so that the
            # newly entered record is not lost.
            save_data(waste_log)

        # ==========================================================
        # OPTION 2: RECYCLING SUMMARY
        # ==========================================================
        elif choice == 2:

            # Call the Recycling Summary Module.
            # This module groups waste by category and calculates
            # the total waste, recycled waste, and recycling rate.
            calculate_recycling_summary(waste_log)

        # ==========================================================
        # OPTION 3: ENVIRONMENTAL IMPACT
        # ==========================================================
        elif choice == 3:

            print("\n🌍 Environmental Impact Report")
            print("======================================")

            # Calculate the estimated CO₂ savings from recycled
            # materials stored in the waste log.
            #
            # The environmental impact function checks each
            # recycled material and applies its CO₂-saving factor:
            #
            #     CO₂ Saved = Weight × CO₂ Saving Factor
            #
            # The individual results are then added together.
            total_co2_saved = calculate_environmental_impact(
                waste_log,
                CO2_SAVED_PER_KG
            )

            # Display the final environmental impact.
            print(f"🌱 Estimated CO₂ saved: {total_co2_saved:.2f} kg")
            print("======================================")

        # ==========================================================
        # OPTION 4: VIEW WASTE HISTORY
        # ==========================================================
        elif choice == 4:

            # Display all previously recorded waste entries.
            # The History Module handles the formatting and display.
            view_history(waste_log)

        # ==========================================================
        # OPTION 5: SEARCH WASTE HISTORY
        # ==========================================================
        elif choice == 5:

            print("\n🔎 Search Waste History")
            print("======================================")

            # Ask the user for a category or search keyword.
            search_filter = input(
                "Enter a waste category to search: "
            ).strip()

            # Search the waste log using the user's keyword.
            # The search function handles matching and displaying
            # the results.
            search_history(waste_log, search_filter)

        # ==========================================================
        # OPTION 6: RECOMMENDATIONS
        # ==========================================================
        elif choice == 6:

            # Calculate the user's current recycling rate.
            # This value is passed to the recommendation module.
            recycling_rate = calculate_current_recycling_rate(
                waste_log
            )

            # Generate rule-based recommendations according
            # to the user's recycling performance.
            generate_recommendations(recycling_rate)

        # ==========================================================
        # OPTION 7: EXIT
        # ==========================================================
        elif choice == 7:

            # Save all current records before closing the application.
            # This ensures that no waste data is lost between sessions.
            save_data(waste_log)

            print("\n")
            print("╔══════════════════════════════════════════════════╗")
            print("║                                                  ║")
            print("║                🌱 GOODBYE! 🌱                    ║")
            print("║                                                  ║")
            print("║      Thank you for making sustainable choices!   ║")
            print("║                                                  ║")
            print("║        ♻️    Every small action counts! 💚        ║")
            print("║                                                  ║")
            print("╚══════════════════════════════════════════════════╝")
            print()

            # End the main application loop.
            break


# Run the application only when this file is executed directly.
# This prevents main() from running automatically if main.py
if __name__ == "__main__":
    main()
