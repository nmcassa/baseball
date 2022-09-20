# baseball

## team.py

The team class works to build an object that represents a team. The constructor takes the abbreviation of a team and then creates this object ("ATL" represented in JSON) : 

```json
{
    "abbreviation": "ATL",
    "url": "https://www.baseball-reference.com/teams/ATL/2022.shtml",
    "name": "Atlanta Braves",
    "win_to_loss": 0.6214285714285714,
    "home_vs_road": [
        " .653",
        " .588"
    ]
}
```

TODO in team.py:
- Get info for home stadium

## game.py

The game class currently only fetches the urls for all games then creates a basic game object that contains this:  

```json
{
    "url": "/previews/2022/CLE202209190.shtml",
    "home_team": {
        "name": "Cleveland Guardians",
        "abb": "CLE",
        "record": "79-67",
        "last_ten": "8-2",
        "pitcher": {
            "name": "Cal Quantrill",
            "era": "3.51",
            "s_IP": {
                "seven": 41.0,
                "five": 32.1
            },
            "s_ER": {
                "seven": 11.0,
                "five": 8.0
            },
            "s_ERA": 2.339261285909713
        },
        "RA/G": "3.95",
        "RS/G": "4.15"
    },
    "away_team": {
        "name": "Minnesota Twins",
        "abb": "MIN",
        "record": "73-73",
        "last_ten": "4-6",
        "pitcher": {
            "name": "Sonny Gray",
            "era": "2.83",
            "s_IP": {
                "seven": 38.2,
                "five": 25.2
            },
            "s_ER": {
                "seven": 9.0,
                "five": 8.0
            },
            "s_ERA": 2.4132492113564665
        },
        "RS/G": "4.32",
        "RA/G": "4.20"
    }
}
```

### bug

if no given pitcher for team. 

```
home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
```

just check for # of tables

haven't reproduced
