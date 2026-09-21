"""Give gardening advice based on the season and the type of plant.

The advice is stored in dictionaries rather than long if/elif chains, so a
new season or plant can be supported by adding one line to the relevant
dictionary instead of editing the program's logic.
"""

# Advice keyed by season. Add a new entry here to support another season.
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Start planting and feed the soil with compost.",
    "autumn": "Clear fallen leaves and mulch your beds before the cold.",
}

# Advice keyed by plant type. Add a new entry here to support another plant.
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Pinch back the tips often to keep growth bushy.",
    "succulent": "Let the soil dry out completely between waterings.",
}


def get_season_advice(season):
    """Return the advice for the given season.

    Args:
        season (str): The season entered by the user, e.g. "summer".

    Returns:
        str: The matching advice, or a fallback message if the season is
            not one we have advice for.
    """
    return SEASON_ADVICE.get(season, "No advice for this season.")


def get_plant_advice(plant_type):
    """Return the advice for the given plant type.

    Args:
        plant_type (str): The plant type entered by the user, e.g. "flower".

    Returns:
        str: The matching advice, or a fallback message if the plant type is
            not one we have advice for.
    """
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def get_advice(season, plant_type):
    """Combine the season and plant advice into one message.

    Args:
        season (str): The season entered by the user.
        plant_type (str): The plant type entered by the user.

    Returns:
        str: The season advice and the plant advice on separate lines.
    """
    return f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"


def prompt_for(label, options):
    """Ask the user for a value and normalise what they type.

    Args:
        label (str): What we are asking for, e.g. "season".
        options (dict): The dictionary whose keys are the valid answers.
            Its keys are listed in the prompt so the user knows the choices.

    Returns:
        str: The user's answer, stripped of surrounding spaces and
            lowercased so it matches the dictionary keys.
    """
    choices = "/".join(options)
    return input(f"Enter the {label} ({choices}): ").strip().lower()


def main():
    """Ask the user for their season and plant, then print the advice."""
    season = prompt_for("season", SEASON_ADVICE)
    plant_type = prompt_for("plant type", PLANT_ADVICE)
    print(get_advice(season, plant_type))


# Only run main() when this file is executed directly, so the functions
# above can be imported and tested from another file without printing.
if __name__ == "__main__":
    main()
