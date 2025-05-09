# 2025 AMAWaterways Cruise Decompile

I am taking a cruise. Unfortunately, there is no way to look at the excursions available for our cruise trip online. Thankfully, I am able to intercept the JSON file from the app.

## Usage

1. Interept the activities call from AMAWaterways app using Charles Proxy or similar tool.

2. Run `uvx build.py` to read `activities.json` and create a new file called `Excursions.md` in the same directory. This file contains the excursion information in a more readable Markdown format.

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

##### What you will see

Margaret Bridge, Nyugati Railway Station

##### What you will visit

Aquincum Museum, Elizabeth Square, St. Stephen’s Basilica, Liberty Square

```

Notes for generation.

* `POIName`, `Date` is used to make the title of the day.
* Show Full Day, Morning, Afternoon, Evening, in that order for each day.
  * Don't show anything if there's nothing for that section.
* Only show things with a `Difficulty` value. Hide the rest.
* Append `Notes` to the end of each excursion entry in bold markdown text.

