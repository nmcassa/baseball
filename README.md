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
 Get info for home stadium

## game.py

The game class currently only fetches the urls for all games then creates a basic game object that contains this:  

```json
{
    "url": "/previews/2022/SFN202209130.shtml",
    "home_team": {
        "name": "San Francisco Giants",
        "abb": "SFG",
        "last_ten": "5-5",
        "pitcher": "Jakob Junis"
    },
    "away_team": {
        "name": "Atlanta Braves",
        "abb": "ATL",
        "last_ten": "7-3",
        "pitcher": "Kyle Wright"
    }
}
```

TODO in game.py:
- grab statistics 
  - eras
  - stadium
  - RSA
- improve game object with those stats
