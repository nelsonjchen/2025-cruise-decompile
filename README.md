# 2025 AMAWaterways Cruise Decompile

I am taking a cruise. Unfortunately, there is no way to look at the excursions available for our cruise trip online. Thankfully, I am able to intercept the JSON file from the app.

## Usage

1. Interept the activities call from AMAWaterways app using Charles Proxy or similar tool.

2. Run `uv run generate.py` to read `activities.json` and create a new file called `Excursions.md` in the same directory. This file contains the excursion information in a more readable Markdown format.

## Desired Output format of `Excursions.md`

The below is a sample of the desired output format.

```markdown
# Excursions Info

## Budapest - Sun, Jul 06

### Morning

#### Hidden Budapest Tour

* Excursion Time: Morning
* Duration: 3 hrs 30 mins
* Level of Difficulty: 1-2
* Duration of walk: 2 hrs
* Duration of bus ride: 1 hr 15 mins

Often described as the “Queen of the Danube,” Budapest is well-known for Fisherman’s Bastion, Buda Hill and its magnificent Hungarian Parliament building. However, this sprawling city is full of rich history and culture and offers many “hidden” treasures as you venture further past its river banks. During this excursion, your guide will take you deeper into the city to discover fascinating sites lesser-known to the average traveler.

**What you will see**

Margaret Bridge, Nyugati Railway Station

**What you will visit**

Aquincum Museum, Elizabeth Square, St. Stephen’s Basilica, Liberty Square

```

Notes for generation.

* `POIName`, `Date` is used to make the title of the day.
* Show Full Day, Morning, Afternoon, Evening, in that order for each day.
  * Don't show anything if there's nothing for that section.
* Only show things with a `Difficulty` value. Hide the rest.
* Append `Notes` to the end of each excursion entry in bold markdown text.
* Prepend an emoji to the excursion name based on the `Type`:
    *   "ALT": 🔄
    *   "BIKE": 🚴
    *   "HIKE": ⛰️
    *   "MAIN": ⭐
    *   "OPT": 💰

Annotated JSON with some notes on the format:

```jsonc
{
    "Id": "LND-MAIN-BUD-HIDDENBUDAPEST-STD-AM",
    "Key": 36439,
    "Type": "MAIN",
    "ActivityTypeName": "Main Tour",
    "TimeOfDay": "Morning",
    "TimeOfDayCode": "AM",
    "Name": "Hidden Budapest Tour ",
    "Description": "Often described as the “Queen of the Danube,” Budapest is well-known for Fisherman’s Bastion, Buda Hill and its magnificent Hungarian Parliament building. However, this sprawling city is full of rich history and culture and offers many “hidden” treasures as you venture further past its river banks. During this excursion, your guide will take you deeper into the city to discover fascinating sites lesser-known to the average traveler.",
    "WhatSee": "Margaret Bridge, Nyugati Railway Station",
    "WhatVisit": "Aquincum Museum, Elizabeth Square, St. Stephen’s Basilica, Liberty Square",
    "Notes": null, // This is null but some others have text so append it to the end of the excursion entry in bold markdown text.
    "AcceptMessage": null,
    "SellPrice": null, // When this is not null, replace "[@SellPrice]" with the value."
    "IsOptionalSelected": false,
    "IsTransferActivity": false,
    "Difficulty": "1-2",
    "DifficultyNum": 1.5,
    "Durations": {
      "Total": "3 hrs 30 mins",
      "Bus": "1 hr 15 mins",
      "Walk": "2 hrs ",
      "Bike": null,
      "Train": null,
      "Boat": null,
      "CableCar": null,
      "Performance": null,
      "Tasting": null,
      "Other": null,
      "FreeTime": null
    },
    "Distance": "",  // If present, append to the bullet points as "Distance: <value>""
    "DistanceKm": null,
    "DistanceMi": null,
    "PreCruise": true,
    "PostCruise": false,
    "Day": 2,
    "CruiseDay": -1,
    "Date": "2025-07-06", // This is used to make the title of the day
    "Cutoff": "2025-07-05T15:00:00",
    "CutoffUtc": "2025-07-05T14:00:00Z",
    "CutoffReminder": "2025-07-05T12:00:00",
    "CutoffReminderUTC": "2025-07-05T11:00:00Z",
    "CutoffMessage": "You can no longer change your selection for this excursion.\r\nPlease contact your Cruise Manager to make a change.",
    "ActivityCutoffConfig": null,
    "IsCutoffCruiseOverride": false,
    "Order": 1751792399,
    "POIId": "e19bd7f061ec7e738c85c8cca5941b30",
    "POIName": "Budapest", // This is used to make the title of the day.
    "POICode": null,
    "Registered": null,
    "RegisteredDetails": null,
    "CanSelect": true,
    "NonSelectMessage": null,
    "NonDeselectMessage": null,
    "PleaseNote": null,
    "Paces": {
      "Regular": "REG",
      "Gentle": "GEN"
    },
    "WaiverTypeKey": null,
    "GuestTypeLimit": 0,
    "GuestLimitMessage": null,
    "IgnoreBikeCapacityLimitCheck": false
  },
```

## Development

Just use Roo Code and the orchestrator mode. Excursions.md is not in `.gitignore` so it will be created in the same directory as the script so it can be pushed to GitHub for easy Markdown reading.