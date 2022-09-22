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

going to contain the algorithms

```python
(['Texas Rangers', 149.2277853372434], ['Los Angeles Angels', -129.1286])
(['Kansas City Royals', -20.31413138686131], ['Minnesota Twins', -1.8470000000000093])
(['Colorado Rockies', -52.50888900523555], ['San Francisco Giants', 37.941])
(['Oakland Athletics', -121.73550695187166], ['Seattle Mariners', 102.3945614973262])
(['San Diego Padres', 18.42407692307695], ['St. Louis Cardinals', 21.725457142857152])
(['Pittsburgh Pirates', 17.816352313167236], ['Chicago Cubs', 3.9249999999999936])
(['Cincinnati Reds', -37.2224625], ['Milwaukee Brewers', 103.92925149359888])
(['Tampa Bay Rays', 8.291000000000004], ['Toronto Blue Jays', 16.384959550561813])
(['Baltimore Orioles', 100.73500000000001], ['Houston Astros', 112.78365542168677])
(['New York Yankees', 25.62965000000002], ['Boston Red Sox', 200.0978092485549])
(['Philadelphia Phillies', 75.67269230769229], ['Atlanta Braves', 105.87469863013699])
(['Chicago White Sox', 147.52309552238808], ['Cleveland Guardians', 165.72073669609082])
(['Los Angeles Dodgers', 208.9107948717949], ['Arizona Diamondbacks', 254.71306294820724])
```

### bug

if no given pitcher for team. 

```
home = data[3].find("div", {'class': ['placeholder']}).next_sibling.next_sibling
```

just check for # of tables

haven't reproduced
