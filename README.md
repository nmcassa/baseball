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
    "url": "/previews/2022/SFN202209180.shtml",
    "home_team": {
        "name": "San Francisco Giants",
        "abb": "SFG",
        "last_ten": "4-6",
        "pitcher": {
            "name": "Alex Cobb",
            "era": "3.48",
            "s_IP": {
                "seven": 41.0,
                "five": 16.1
            },
            "s_ER": {
                "seven": 10.0,
                "five": 10.0
            },
            "s_ERA": 3.1523642732049035
        }
    },
    "away_team": {
        "name": "Los Angeles Dodgers",
        "abb": "LAD",
        "last_ten": "8-2",
        "pitcher": {
            "name": "Andrew Heaney",
            "era": "2.84",
            "s_IP": {
                "seven": 33.2,
                "five": 26.0
            },
            "s_ER": {
                "seven": 16.0,
                "five": 20.0
            },
            "s_ERA": 5.472972972972973
        }
    }
}
```

TODO in game.py:
- grab statistics 
  - RSA
- improve game object with those stats


### bug

if no given pitcher for team. 

```
home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
```

just check for # of tables
