# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence",
             "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma", "Gizmek Uka, the Festive Fox of Fecundity",
             "Gravedigger's Trap Hole", "Forbidden Droplet"]

# Handtraps that can only be used once per turn
opt_handtraps = ["Nibiru, the Primal Being", "Fantastical Dragon Phantazmay", "Ghost Mourner & Moonlit Chill",
                 "Ash Blossom & Joyous Spring", "Ghost Ogre & Snow Rabbit","PSY-Framegear Gamma",
                 "Gizmek Uka, the Festive Fox of Fecundity"]

# List of Harpie cards you can normal summon
normal_summon_harpies = ["Harpie Queen", "Harpie Harpist", "Harpie Lady", "Harpie Channeler", "Harpie Perfumer",
                         "Harpie Oracle", "Harpie Lady 1", "Cyber Harpie Lady", "Harpie Dancer"]

# List of Dragons you need a no_monster_extender to combo with
normal_summon_dragons = ["Dragunity Phalanx", "World Chalice Guardragon"]

# List of cards that can be special summon a winged beast if you control a harpie
harpie_extender = ["Elegant Egotist", "Swallow's Nest", "Hysteric Sign"]

# List of cards that act like Egotist
egotist_extender = ["Elegant Egotist", "Hysteric Sign"]

# List of cards you can SS if you control no monsters
no_monster_extender = ["Lyrilusc - Turquoise Warbler", "Unexpected Dai", "Cockadoodledoo"]

# Access to vanilla harpie lady
vanilla_access = ["Harpie Lady", "Unexpected Dai"]

# List of targets to discard/banish with tempest
wind_attribute = ["Lyrilusc - Truquoise Warbler", "Harpie Queen", "Harpie Oracle", "Harpie Harpist", "Harpie Channeler",
                  "Harpie Perfumer", "Harpie Lady", "Dragunity Phalanx", "World Chalice Guardragon",
                  "Mecha Phantom Beast O-Lion", "Garuda the Wind Spirit"]

# Normal summons that can combo by themselves
normal_one_card_combo = ["Harpie Perfumer", "Jet Synchron", "Tuning"]

harpie_card = ["Harpies' Hunting Ground", "Harpie Queen", "Harpie Oracle", "Harpie Harpist", "Harpie Channeler",
               "Harpie Perfumer", "Harpie Lady", "Harpie's Feather Rest", "Cyber Harpie Lady",
               "Harpie Lady Sisters", "Harpie Dancer", "Harpie Lady 1", "Harpie's Pet Dragon", "Harpie's Feather Storm"]

# Cards that play through Nibiru
vs_nibiru = ["Harpie's Feather Storm"]


def phalanx_brick(hand, deck):
    deck_count = deck.count("Dragunity Phalanx")
    hand_count = hand.count("Dragunity Phalanx")
    return hand_count == deck_count


def remove_all(hand, used):
    return [card for card in hand if card != used]
