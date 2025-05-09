import json
from datetime import datetime

def format_excursion(excursion):
    """Formats a single excursion into Markdown."""
    # Map activity types to emojis
    emoji_map = {
        "ALT": "🔄",
        "BIKE": "🚴",
        "HIKE": "⛰️",
        "MAIN": "⭐",
        "OPT": "💰"
    }
    activity_type = excursion.get('Type', '')
    emoji = emoji_map.get(activity_type, '')

    markdown = f"#### {emoji} {excursion['Name'].strip()}\n\n"
    markdown += f"* Excursion Time: {excursion['TimeOfDay']}\n"
    if excursion['Durations'] and excursion['Durations'].get('Total'):
        markdown += f"* Duration: {excursion['Durations']['Total'].strip()}\n"
    if excursion.get('Difficulty'):
        markdown += f"* Level of Difficulty: {excursion['Difficulty'].strip()}\n"
    if excursion['Durations'] and excursion['Durations'].get('Walk'):
        markdown += f"* Duration of walk: {excursion['Durations']['Walk'].strip()}\n"
    if excursion['Durations'] and excursion['Durations'].get('Bus'):
        markdown += f"* Duration of bus ride: {excursion['Durations']['Bus'].strip()}\n"
    # Add Distance if present
    if excursion.get('Distance'):
        markdown += f"* Distance: {excursion['Distance'].strip()}\n"


    markdown += f"\n{excursion['Description'].strip()}\n\n"

    if excursion.get('WhatSee'):
        markdown += f"**What you will see**\n\n"
        markdown += f"{excursion['WhatSee'].strip()}\n\n"

    if excursion.get('WhatVisit'):
        markdown += f"**What you will visit**\n\n"
        markdown += f"{excursion['WhatVisit'].strip()}\n\n"

    notes = excursion.get('Notes')
    if notes:
        # Check if SellPrice exists and is not null, and replace placeholder in notes
        sell_price = excursion.get('SellPrice')
        if sell_price is not None:
            notes = notes.replace('[@SellPrice]', str(sell_price))
        markdown += f"**{notes.strip()}**\n\n"

    return markdown

def generate_excursions_markdown(activities_data):
    """Generates the full Markdown content for Excursions.md."""
    markdown_content = "# Excursions Info\n\n"

    # Group activities by day (POI and Date)
    activities_by_day = {}
    for activity in activities_data:
        # Only include activities with a Difficulty value
        if activity.get('Difficulty'):
            date_str = activity['Date']
            poi_name = activity['POIName']
            day_key = (date_str, poi_name)
            if day_key not in activities_by_day:
                activities_by_day[day_key] = []
            activities_by_day[day_key].append(activity)

    # Sort days by date
    sorted_days = sorted(activities_by_day.keys())

    time_of_day_order = ["Full Day", "Morning", "Afternoon", "Evening"]

    for date_str, poi_name in sorted_days:
        # Format date for the title
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%a, %b %d")
        markdown_content += f"## {poi_name} - {formatted_date}\n\n"

        # Group activities by time of day for the current day
        activities_for_day = activities_by_day[(date_str, poi_name)]
        activities_by_time = {time: [] for time in time_of_day_order}
        for activity in activities_for_day:
            time_of_day = activity.get('TimeOfDay')
            if time_of_day in activities_by_time:
                activities_by_time[time_of_day].append(activity)

        # Add activities for each time of day in the specified order
        for time_of_day in time_of_day_order:
            if activities_by_time[time_of_day]:
                markdown_content += f"### {time_of_day}\n\n"
                for excursion in activities_by_time[time_of_day]:
                    markdown_content += format_excursion(excursion)

    return markdown_content

# Main execution
try:
    with open('activities.json', 'r') as f:
        activities_data = json.load(f)

    markdown_output = generate_excursions_markdown(activities_data)

    with open('Excursions.md', 'w') as f:
        f.write(markdown_output)

    print("Successfully generated Excursions.md")

except FileNotFoundError:
    print("Error: activities.json not found. Please make sure the file exists in the same directory.")
except json.JSONDecodeError:
    print("Error: Could not decode activities.json. Please ensure it is a valid JSON file.")
except Exception as e:
    print(f"An error occurred: {e}")