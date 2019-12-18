# Sorting Tool

Sorting Tool.  Python/Flask and Javascript (d3).  Based on work from Mike Bostock (https://bost.ocks.org/mike/) and Rob Schmuecker (http://bl.ocks.org/robschmuecker/7880033).  Designed originally for the Unified Astronomy Thesuarus (http://astrothesaurus.org/), but can be used for a variety of projects.

Main repository: https://github.com/katieefrey/UAT-Scripts/tree/master/UAT%20Sorting%20Tool

## Adding sections/branches

Simply add a JSON file to the static/topconcepts folder to add a new branch/section to the sorting tool.

The name of the JSON file will be used as the display name in the dropdown menu.  For proper formatting, write the file name in all lower case and use underscores for spaces.

The JSON file must be in the following format:

```
{
    "name": "Exoplanet astronomy",
    "children": [{
        "name": "Exoplanet catalogs"
    }, {
        "name": "Exoplanet detection methods",
        "children": [{
            "name": "Astrometry",
            "children": [{
                "name": "Astronomical coordinate systems",
                "children": [{
                    "name": "Ecliptic coordinate system"
                }, {
                    "name": "Galactic coordinate system",
                    "children": [{
                        "name": "Galactic latitude"
                    }, {
                        "name": "Quadrants"
                    }]
                }, {
                    "name": "Horizontal coordinate system"
                }]
            }, {
                "name": "Planet hosting stars",
                "children": [{
                    "name": "Habitable zone"
                }]
            }]
        }]
    }]
}

```

### Running locally in debug mode

set FLASK_APP=sortingtool.py

set FLASK_DEBUG=1

python -m flask run

### To Do:
- download saved json option
- general look and feel
 - make feedback form smaller, or move it somewhere else on the screen?
 - make notes/instructions accessible while looking at the dendrogram too