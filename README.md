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

## algor.py

```python
(['Texas Rangers', 102.99279], ['Los Angeles Angels', -134.5134])
(['Kansas City Royals', -20.48413], ['Minnesota Twins', -1.019])
(['Colorado Rockies', -50.93149], ['San Francisco Giants', 98.029])
(['Oakland Athletics', -127.87431], ['Seattle Mariners', 92.51616])
(['San Diego Padres', -3.04592], ['St. Louis Cardinals', 14.55666])
(['Pittsburgh Pirates', 3.47835], ['Chicago Cubs', 103.765])
(['Cincinnati Reds', -37.39926], ['Milwaukee Brewers', 71.53885])
(['Tampa Bay Rays', 54.691], ['Toronto Blue Jays', 38.31496])
(['Baltimore Orioles', 105.955], ['Houston Astros', 78.81206])
(['New York Yankees', 37.20105], ['Boston Red Sox', 139.12821])
(['Philadelphia Phillies', 58.65269], ['Atlanta Braves', 66.6907])
(['Chicago White Sox', 95.2095], ['Cleveland Guardians', 121.49254])
(['Los Angeles Dodgers', 182.70279], ['Arizona Diamondbacks', 184.31606])
```

### print_all_difference

```python
New York Yankees 112
Philadelphia Phillies 38
Oakland Athletics ND New York Mets
Miami Marlins 103
Toronto Blue Jays 56
Chicago Cubs 60
Cincinnati Reds 25
Baltimore Orioles ND Houston Astros
Cleveland Guardians 21
Chicago White Sox 77
Seattle Mariners 178
Minnesota Twins 52
Arizona Diamondbacks 31
San Diego Padres 221
Los Angeles Dodgers 41
```

### bug

if no given pitcher for team. 

```
home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
```

just check for # of tables

haven't reproduced
