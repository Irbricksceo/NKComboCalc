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


# Keeps track of numbers times we can successfully combo
def combo_sim(deck, n):
    success_no_hts = 0
    success_2hts = 0
    success_vs_nibiru = 0
    success_vs_imperm = 0
    num_phalanx_bricks = 0
    opened_ht = 0
    success_partial_combo = 0
    for i in range(0, n):
        test_hand = draw(deck, 5)
        #print("Hand: " + ', '.join(map(str, test_hand)))
        shuffle(deck)
        results = combo(test_hand, deck)
        if results[0]:
            success_no_hts += 1
        if results[1]:
            success_2hts += 1

        if results[2]:
            success_vs_nibiru += 1

        if results[3]:
            opened_ht += 1

        if results[4]:
            success_vs_imperm += 1

        if results[5]:
            num_phalanx_bricks += 1

        if results[6]:
            success_partial_combo += 1

    # Prints the results
    no_hts_ratio = round(success_no_hts / n * 100, 2)
    two_hts_ratio = round(success_2hts / n * 100, 2)
    nibiru_ratio = round(success_vs_nibiru / n * 100, 2)
    imperm_ratio = round(success_vs_imperm / n * 100, 2)
    open_ht_ratio = round(opened_ht / n * 100, 2)
    phalanx_brick_ratio = round(num_phalanx_bricks / n * 100, 2)
    partial_ratio = round(success_partial_combo / n * 100, 2)
    full_partial_ratio = round((success_partial_combo + success_no_hts) / n * 100, 2)
    print("Full Combo Success Rate through no Handtraps: " + str(no_hts_ratio) + "%")
    #print("Full + Partial Combo Success Rate through no Handtraps: " + str(full_partial_ratio) + "%")
    print("Combo Success Rate through Nibiru: " + str(nibiru_ratio) + "%")
    print("Combo with drawing at least 1 extra Handtrap/Disruption : " + str(open_ht_ratio) + "%")
    print("Phalanx Brick Rate: " + str(phalanx_brick_ratio) + "%")
    # print("Combo with atleast drawing 2 Handtraps in your hand: " + str(two_hts_ratio) + "%")
