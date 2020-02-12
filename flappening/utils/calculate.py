# calculates average players score
def avgScore(players):

    SUM = 0

    for item in [player.getScore() for player in players]:
        SUM = SUM + item

    AVG = SUM / len(players)

    return AVG
