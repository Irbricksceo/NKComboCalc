from sets import *


# Verifies if hand can combo successfully

def combo(hand, deck):
    debug = False
    win = False
    play_vs_nibiru = False
    play_vs_imperm = False
    bricked_on_phalanx = False
    partial_combo = False

    # Checks if drawn handtraps
    open_ht, open_two_hts = two_hts(hand)

    # Combo with One card
    for i in normal_one_card_combo:
        if i in hand:
            possible_win = True

            # Case if no phalanx in deck, then it is not combo
            if phalanx_brick(hand, deck):
                if ("Harpie Perfumer" in hand):
                    bricked_on_phalanx = True
                    possible_win = False

            if possible_win:
                win = True
                if debug:
                    print("One Card Perfumer Combo")
                if ("Harpie's Feather Storm" in hand) & (("Harpie Perfumer" in hand) | ("Unexpected Dai" in hand)):
                    play_vs_nibiru = True
                if "Swallow's Nest" in hand:
                    play_vs_imperm = True
                break

    # Combo with Channeler + Discard
    if ((not win) or not play_vs_nibiru) & ("Harpie Channeler" in hand):
        chan_hand = hand.copy()
        chan_hand.remove("Harpie Channeler")
        for i in harpie_card:
            if i in chan_hand:
                    possible_win = True
                    chan_hand.remove(i)

                    for j in harpie_extender + ["Unexpected Dai", "Harpie Oracle"]:
                        if (("Gravedigger's Trap Hole" not in chan_hand) &
                                ("Gravedigger's Trap Hole" in deck) & (j in chan_hand)):
                            # Make Traptrix Rafflesia in 5 Summons
                            play_vs_nibiru = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(chan_hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("Channeler + Discard Combo")
                        if "Harpie's Feather Storm" in chan_hand:
                            play_vs_nibiru = True
                        if "Swallow's Nest" in chan_hand:
                            play_vs_imperm = True
                        break

    # Combo with a harpie + harpie extender
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_harpies + ["Unexpected Dai"]:
            for j in harpie_extender + no_monster_extender:
                if (i in hand) & (j in hand) & (i != j):
                    possible_win = True
                    has_vanilla = False

                    if (j in vanilla_access) | (i in vanilla_access):
                        has_vanilla = True

                    extender_test_hand = hand.copy()
                    extender_test_hand.remove(j)
                    # Board will be 2 winged beasts (1 guaranteed harpie) with possible vanilla access
                    winged_beasts = 2
                    for k in egotist_extender:
                        if k in extender_test_hand:
                            winged_beasts += 1
                            has_vanilla = True
                            extender_test_hand.remove(k)

                    for l in egotist_extender:
                        if l in extender_test_hand:
                            winged_beasts += 1
                            has_vanilla = True
                            extender_test_hand.remove(l)

                    if "Harpie Perfumer" in hand:
                        # Perfumer counts as 2
                        winged_beasts += 1

                    if ("Garuda the Wind Spirit" in extender_test_hand) & has_vanilla:
                        winged_beasts += 1

                    if debug:
                        print("Num Winged Beasts = " + str(winged_beasts))

                    if ((winged_beasts >= 4) & ("Gravedigger's Trap Hole" not in hand)
                            & ("Gravedigger's Trap Hole" in deck)):
                        play_vs_nibiru = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("Harpie + Harpie Extender Combo")
                        if "Harpie's Feather Storm" in hand:
                            play_vs_nibiru = True
                        break

    # Combo with a dragon + no monster SS
    if (not win) or not play_vs_nibiru:
        for i in normal_summon_dragons:
            for j in no_monster_extender:
                if (i in hand) & (j in hand):
                    possible_win = True

                    # Case if no phalanx in deck, then it is not combo
                    if phalanx_brick(hand, deck):
                        bricked_on_phalanx = True
                        possible_win = False

                    if possible_win:
                        win = True
                        if debug:
                            print("No Monster SS + Dragon Combo")
                        if ("Harpie's Feather Storm" in hand) and (j == "Unexpected Dai"):
                            play_vs_nibiru = True
                        break

    # Combo with Vanilla + World Chalice Guardragon
    if (not win) or not play_vs_nibiru:
        for i in vanilla_access:
            if i in hand:
                possible_win = False
                if "World Chalice Guardragon" in hand:
                    possible_win = True

                if "Tempest, Dragon Ruler of Storms" in hand:
                    for j in wind_attribute:
                        if j in hand:
                            # Tempest + Discard for WCG
                            possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Vanilla + WCG Combo")
                    if ("Harpie's Feather Storm" in hand):
                        play_vs_nibiru = True
                    break

    # Combo with Double Lyrilusc Turquoise Warbler
    if (not win) or not play_vs_nibiru:
        if "Lyrilusc - Turquoise Warbler" in hand:
            lyrilusc_hand = hand.copy()
            lyrilusc_hand.remove("Lyrilusc - Turquoise Warbler")
            if "Lyrilusc - Turquoise Warbler" in lyrilusc_hand:
                possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Double Lyrilusc Turquoise Warbler")

                    for i in normal_summon_harpies:
                        if ("Harpie's Feather Storm" in lyrilusc_hand) & (i in lyrilusc_hand):
                            play_vs_nibiru = True

                    if "Harpie Channeler" in lyrilusc_hand:
                        lyrilusc_hand.remove("Harpie Channeler")
                        for j in harpie_card:
                            if (("Gravedigger's Trap Hole" not in lyrilusc_hand) & ("Gravedigger's Trap Hole" in deck) &
                                    (j in lyrilusc_hand)):
                                # Make Traptrix Rafflesia in 5 Summons
                                play_vs_nibiru = True

                    if "Harpie Perfumer" in lyrilusc_hand:
                        if ("Gravedigger's Trap Hole" not in lyrilusc_hand) & ("Gravedigger's Trap Hole" in deck):
                            # Make Traptrix Rafflesia in 5 Summons
                            play_vs_nibiru = True

                    for i in normal_summon_harpies:
                        for j in harpie_extender:
                            if (i in hand) & (j in hand):
                                # Make Traptrix Rafflesia in 5 Summons
                                play_vs_nibiru = True

    # Combo with Vanilla + Garuda the Wind Spirit
    if (not win) or not play_vs_nibiru:
        for i in vanilla_access:
            if (i in hand) & ("Garuda the Wind Spirit" in hand):
                possible_win = True

                # Case if no phalanx in deck, then it is not combo
                if phalanx_brick(hand, deck):
                    bricked_on_phalanx = True
                    possible_win = False

                if possible_win:
                    win = True
                    if debug:
                        print("Vanilla + Garuda Combo")
                    if ("Harpie's Feather Storm" in hand):
                        play_vs_nibiru = True
                    break

    # Partial Combo with No monster SS + O-Lion (Just Simorgh)
    if (not win) or (not play_vs_nibiru) or (not partial_combo):
        for i in no_monster_extender:
            if (i in hand) & ("Mecha Phantom Beast O-Lion" in hand):
                partial_combo = True
                if ("Harpie's Feather Storm" in hand) & ("Unexpected Dai" in hand):
                    play_vs_nibiru = True
                    break

    # Partial Combo with  Phalanx + Divine Lance (Just Simorgh)
    if (not win) or (not play_vs_nibiru) or (not partial_combo):
        if ("Dragunity Phalanx" in hand) & ("Dragunity Divine Lance" in hand):
            if phalanx_brick(hand, deck):
                bricked_on_phalanx = True
            else:
                partial_combo = True

    win_nibiru = (win | partial_combo) & play_vs_nibiru
    win_imperm = win & play_vs_imperm
    open_ht = (win | partial_combo) & open_ht
    open_two_hts = (win | partial_combo) & open_two_hts
    if win:
        partial_combo = False
    return [win, open_two_hts, win_nibiru, open_ht, win_imperm, bricked_on_phalanx, partial_combo]


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
