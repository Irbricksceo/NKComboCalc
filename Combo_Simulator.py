import random
from combinations import *


# Shuffles deck
def shuffle(deck):
    random.shuffle(deck)


# Draws 5 cards
def draw(deck, n):
    hand = []
    test_deck = deck.copy()
    shuffle(test_deck)
    for i in range(n):
        hand.append(test_deck.pop(0))
    return hand


# Keeps track of results
def combo_sim(deck, n):
    full_combo = 0
    partial_combo = 0
    trap_dump = 0
    herald_extend = 0
    plays_through_one_ht = 0

    for i in range(0, n):
        test_hand = draw(deck, 5)
        print("Hand: " + ', '.join(map(str, test_hand)))
        shuffle(deck)
        results = combo(test_hand, deck)

        if results[0]:
            full_combo += 1

        if results[1]:
            partial_combo += 1

        if results[2]:
            trap_dump += 1

        if results[3]:
            herald_extend += 1

        if results[4]:
            plays_through_one_ht += 1

    # Converts totals into percentages
    fullratio = round(full_combo / n * 100, 2)
    partialratio = round(partial_combo / n * 100, 2)
    trapratio = round(trap_dump / n * 100, 2)
    heraldratio = round(herald_extend / n * 100, 2)
    throughonehtratio = round(plays_through_one_ht / n * 100, 2)

    # Outputs results. commented out lines are tests without the logic fully implemented yet.
    print("Full Combo Success Rate through no Handtraps: " + str(fullratio) + "%")
    print("Partial Combo Success Rate through no Handtraps: " + str(partialratio) + "%")
    print("Percentage of hands that mill at least 1 trap: " + str(trapratio) + "%")
    print("Percentage of hands that can extend into herald: " + str(heraldratio) + "%")
    print("Percentage of hands that can reach at least partial combo through one HT: " + str(throughonehtratio) + "%")


