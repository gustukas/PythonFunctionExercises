def blackjack(x,y,z):
    cardsum = 0
    while cardsum < 21:
        if (x > 0 and x < 11) or (y > 0 and y < 11) or (z > 0 and z < 11):
            pass
        else: return("Illegal")

        cardsum = x + y + z

        if cardsum <= 21:
            return cardsum
        elif cardsum > 21 and (x == 11 or y == 11 or z == 11):
            cardsum = cardsum - 10
    else: return("BUST!")

print(blackjack(2,10,11))


    