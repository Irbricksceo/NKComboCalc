from Combo_Simulator import combo_sim


# function reads the decklist files and creates the source data for the combo sim
def import_deck(filename):
    with open(filename) as f:
        deck = [line.strip() for line in f if not line.startswith('#')]
        return deck


# Main function defined, it outputs an intial statement on what operation is being run,and calls import/sim functions.
def main(deck_txt, n):
    print("Running " + n + " test hands on decklist: " + deck_txt)
    deck = import_deck(deck_txt)
    combo_sim(deck, n)


# Here we define first the decklist we wish to use, and the number of test hands to run.
src = "Decklists/NK12.1"
amt = 100000

main(src, amt)