from sets import *


# Verifies if hand can combo successfully

def combo(hand, deck):
    debug = False
    full_combo = False
    partial_combo = False
    trap_dump = False
    herald_extend = False
    play_through_ht = False

    # Checks if drawn handtraps
    open_ht, open_two_hts = two_hts(hand)

    # Checks if we can make Isolde

    can_isolde(hand)

    has_tuner(hand)

    can_herald(hand)

    can_trap(hand)

    can_play_through(hand)

    return [full_combo,partial_combo,trap_dump,herald_extend,play_through_ht]

# Checks if we have a handtrap in hand
def hts(hand):
    return any(i in handtraps for i in hand)

# Checks if we have 2 playable handtraps in hand
def two_hts(hand):
    open_one_ht = False
    open_two_hts = False
    for i in hand:
        if i in handtraps:
            open_one_ht = True
            if i in opt_handtraps:
                open_two_hts = hts(remove_all(hand.copy(), i))
            else:
                temp_hand = hand.copy()
                temp_hand.remove(i)
                open_two_hts = hts(temp_hand)
    return open_one_ht, open_two_hts


def can_isolde(hand):
    success = False


def has_tuner(hand):
    success = False


def can_herald(hand):
    success = False


def can_trap(hand):
    success = False


def can_play_through(hand):
    success = False
