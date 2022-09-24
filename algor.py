from game import *

one_weight = 40
two_weight = 30
four_weight = 50

def m_one(team) -> tuple:
    era = float(team['pitcher']['era'])
    ra = float(team["RA/G"])

    return (ra - era, one_weight)

def m_two(team) -> tuple:
    rs = float(team['RS/G'])
    ra = float(team['RA/G'])

    return (rs - ra, two_weight)

def m_three(team) -> tuple:
    era = float(team['pitcher']['era'])
    sera = float(team['pitcher']['s_ERA'])

    sip = team['pitcher']['s_IP']

    if sip['five'] + sip['seven'] < 20.0:
        return ("F", "F")

    return (era - sera, .6 * (sip['five'] + sip['seven'] * (1.2)))

def m_four(team) -> tuple:
    sera = float(team['pitcher']['s_ERA'])
    ra = float(team["RA/G"])

    return (ra - sera, four_weight)

def algor(game: Game) -> tuple:
    #home team has a 8.11% advantage, given by historical data

    home = 8.11 / 2 
    away = -8.11 / 2

    h_one = m_one(game.home_team)
    home += h_one[0] * h_one[1]

    a_one = m_one(game.away_team)
    away += a_one[0] * a_one[1]

    h_two = m_two(game.home_team)
    home += h_two[0] * h_two[1]

    a_two = m_two(game.away_team)
    away += a_two[0] * a_two[1]

    h_three = m_three(game.home_team)

    if h_three[0] == "F":
        return ([game.home_team['name'], "Filter"], [game.away_team['name'], "Filter"])

    home += h_three[0] * h_three[1]

    a_three = m_three(game.away_team)
    away += a_three[0] * a_three[1]

    return ([game.home_team['name'], round(home, 5)], [game.away_team['name'], round(away, 5)])

def all_print(show_json: bool) -> None:
    for game in get_all_game_days():
        one = Game(game)

        if show_json:
            print(one.jsonify())

        print(algor(one))

def one_print(show_json: bool) -> None:
    one = Game(get_all_game_days()[0])

    if show_json:
        print(one.jsonify())

    print(algor(one))

def all_print_difference() -> None:
    for game in get_all_game_days():
        one = Game(game)
        sol = algor(one)
        if sol[0][1] == "Filter":
            print("%s ND %s" % (sol[0][0], sol[1][0]))
        else:
            if sol[0][1] > sol[1][1]:
                print("%s %d" % (sol[0][0], sol[0][1] - sol[1][1]))
            else:
                print("%s %d" % (sol[1][0], sol[1][1] - sol[0][1]))

if __name__ == "__main__":
    #one_print(True)
    #all_print(False)
    all_print_difference()
