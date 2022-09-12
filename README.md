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

The game class currently only fetches the urls for all games that are to play that day. 

```python
['/previews/2022/MIA202209121.shtml', '/previews/2022/CLE202209120.shtml', '/previews/2022/CIN202209120.shtml', '/previews/2022/DET202209120.shtml', '/previews/2022/TOR202209120.shtml', '/previews/2022/MIA202209122.shtml', '/previews/2022/NYN202209120.shtml', '/previews/2022/ARI202209120.shtml', '/previews/2022/SFN202209120.shtml']
```

TODO in game.py:
 grab statistics from these urls
 create a game object with those stats