# List of free warrior extenders
# Handtrap (will include function to draw 2 Card off Phantzamay later)
handtraps = ["Nibiru, the Primal Being", "Effect Veiler", "Fantastical Dragon Phantazmay",
             "Ghost Mourner & Moonlit Chill", "Ash Blossom & Joyous Spring", "Infinite Impermanence",
             "Ghost Ogre & Snow Rabbit", "PSY-Framegear Gamma", "Gizmek Uka, the Festive Fox of Fecundity",
             "Forbidden Droplet"]

# Handtraps that can only be used once per turn
opt_handtraps = ["Nibiru, the Primal Being", "Fantastical Dragon Phantazmay", "Ghost Mourner & Moonlit Chill",
                 "Ash Blossom & Joyous Spring", "Ghost Ogre & Snow Rabbit","PSY-Framegear Gamma",
                 "Gizmek Uka, the Festive Fox of Fecundity"]


FreeWarrior = ["Sky Striker Mecha - Hornet Drones", "Unexpected Dai", "The Phantom Knights of Shade Brigandine"]

# Warrior Tuners In Hand
TunerExtend = ["Infernoble Knight - Renaud", "Infernoble Knight Oliver", "Heritage of the Chalice",
               "Infernoble Arms - Durendal", "Glory of the Noble Knights", "Reinforcement of the Army"]

# Arms


def remove_all(hand, used):
    return [card for card in hand if card != used]
