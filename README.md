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
    "url": "/previews/2022/CIN202209131.shtml",
    "home_team": {
        "name": "Cincinnati Reds",
        "abb": "CIN",
        "last_ten": "5-5",
        "pitcher": [
            "Luis Cessa",
            "4.97"
        ]
    },
    "away_team": {
        "name": "Pittsburgh Pirates",
        "abb": "PIT",
        "last_ten": "3-7",
        "pitcher": [
            "Johan Oviedo",
            "3.90"
        ]
    }
}
```

TODO in game.py:
- grab statistics 
  - eras
  - stadium
  - RSA
- improve game object with those stats
