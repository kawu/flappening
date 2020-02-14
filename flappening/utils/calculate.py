def avgScore(players: list) -> float:
    '''
        calculates average player score.
    '''

    SUM: float = 0

    for item in [player.getScore() for player in players]:
        SUM = SUM + item

    AVG = SUM / len(players)

    return AVG
