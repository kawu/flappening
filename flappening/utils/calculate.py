def avgScore(players: list) -> float:
    '''
        calculates average player score.
    '''

    # to avoid ZeroDivisionError
    if (len(players) == 0):
        return 0

    SUM: float = 0

    for item in [player.getScore() for player in players]:
        SUM = SUM + item

    AVG = SUM / len(players)

    return AVG
