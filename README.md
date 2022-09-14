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
    "url": "/previews/2022/TEX202209140.shtml",
    "home_team": {
        "name": "Texas Rangers",
        "abb": "TEX",
        "last_ten": "4-6",
        "pitcher": {
            "name": "Dane Dunning",
            "era": "4.39",
            "last_seven_era": "4.62",
            "last_five_era": "2.84"
        }
    },
    "away_team": {
        "name": "Oakland Athletics",
        "abb": "OAK",
        "last_ten": "2-8",
        "pitcher": {
            "name": "JP Sears",
            "era": "3.33",
            "last_seven_era": "3.6",
            "last_five_era": "0"
        }
    }
}
```

TODO in game.py:
- grab statistics 
  - eras
  - stadium
  - RSA
- improve game object with those stats


### bug

if no given pitcher for team. 

```
home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
```

just check for # of tables
