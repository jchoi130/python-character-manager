#
# File: assignment3_chojy083.py
# Author: Joon Choi
# Email Id: chojy083
# Description: Programming Assignment 3 – Manage Character (Hero and Villain) Information
# This is my own work as defined by the University's Academic Misconduct policy.
#

import random


def read_file(filename):
    """
    Reads characters from a text file in groups of 3 lines and returns a List of Lists.
    Only uses split() and strip() here to parse the file.
    Structure per character:
    [name, secret_id, hero_flag, no_battles, no_won, no_lost, no_drawn, health]
    """
    character_list = []
    infile = open(filename, "r")  # Looks in the same folder you run this program from

    # Index names (local to avoid magic numbers and avoid globals)
    idx_name = 0
    idx_secret = 1
    idx_flag = 2
    idx_battles = 3
    idx_won = 4
    idx_lost = 5
    idx_drawn = 6
    idx_health = 7

    line = infile.readline()

    # While not end of file
    while line != "":
        name = line.strip("\n")

        line = infile.readline()
        secret_id = line.strip("\n")

        # Third line: flag and numbers
        line = infile.readline()
        stats_tokens = line.split()  # e.g. ['h', '5', '5', '0', '0', '90']

        # Extract values (convert to int where needed)
        hero_flag = stats_tokens[0]  # 'h' or 'v'
        no_battles = int(stats_tokens[1])
        no_won = int(stats_tokens[2])
        no_lost = int(stats_tokens[3])
        no_drawn = int(stats_tokens[4])
        health = int(stats_tokens[5])

        # Build character record
        new_character = [None, None, None, 0, 0, 0, 0, 0]
        new_character[idx_name] = name
        new_character[idx_secret] = secret_id
        new_character[idx_flag] = hero_flag
        new_character[idx_battles] = no_battles
        new_character[idx_won] = no_won
        new_character[idx_lost] = no_lost
        new_character[idx_drawn] = no_drawn
        new_character[idx_health] = health

        character_list.append(new_character)

        # Read next name (first line of next record)
        line = infile.readline()

    infile.close()
    return character_list


def write_to_file(filename, character_list):
    """Writes the character list back to a text file in the original format."""
    outfile = open(filename, "w")  # Saves/overwrites in the same folder you run this program from

    idx_name = 0
    idx_secret = 1
    idx_flag = 2
    idx_battles = 3
    idx_won = 4
    idx_lost = 5
    idx_drawn = 6
    idx_health = 7

    current_index = 0
    total_items = len(character_list)
    while current_index < total_items:
        character = character_list[current_index]
        # name
        outfile.write(str(character[idx_name]) + "\n")
        # secret identity
        outfile.write(str(character[idx_secret]) + "\n")
        # third line
        third = (
            str(character[idx_flag])
            + " "
            + str(character[idx_battles])
            + " "
            + str(character[idx_won])
            + " "
            + str(character[idx_lost])
            + " "
            + str(character[idx_drawn])
            + " "
            + str(character[idx_health])
        )
        outfile.write(third)
        # no extra blank line after last record
        if current_index != total_items - 1:
            outfile.write("\n")
        current_index = current_index + 1

    outfile.close()


def display_characters(character_list, display_type):
    """
    Prints the characters table.
    display_type: 0=all, 1=heroes only, 2=villains only
    """
    idx_name = 0
    idx_flag = 2
    idx_battles = 3
    idx_won = 4
    idx_lost = 5
    idx_drawn = 6
    idx_health = 7

    # Column width for name so the table matches spec output
    CHARACTER_NAME_WIDTH = 27

    # Header
    print("===================================================")
    print("-     Character (heroes and villains) Summary     -")
    print("===================================================")
    print("-                               P  W  L  D   Health -")
    print("---------------------------------------------------")

    # Rows
    current_index = 0
    total_items = len(character_list)
    while current_index < total_items:
        character = character_list[current_index]
        should_display = False
        if display_type == 0:
            should_display = True
        elif display_type == 1 and character[idx_flag] == "h":
            should_display = True
        elif display_type == 2 and character[idx_flag] == "v":
            should_display = True

        if should_display:
            name_str = str(character[idx_name])
            battles = int(character[idx_battles])
            won = int(character[idx_won])
            lost = int(character[idx_lost])
            drawn = int(character[idx_drawn])
            health = int(character[idx_health])

            output_row = (
                "-  "
                + format(name_str, "<" + str(CHARACTER_NAME_WIDTH) + "s")
                + format(battles, ">3d")
                + " "
                + format(won, ">2d")
                + " "
                + format(lost, ">2d")
                + " "
                + format(drawn, ">2d")
                + " "
                + format(health, ">7d")
                + "  -"
            )
            print(output_row)
            print("---------------------------------------------------")

        current_index = current_index + 1

    print("===================================================")


def find_character(character_list, name):
    """Returns index of character with exact (case-sensitive) name, or -1 if not found."""
    idx_name = 0
    current_index = 0
    total_items = len(character_list)
    found_index = -1
    while current_index < total_items:
        if character_list[current_index][idx_name] == name:
            found_index = current_index
        current_index = current_index + 1
    return found_index


def add_character(character_list, name, secret_identity, hero_flag):
    """Adds a new character if not exists; returns (possibly) updated list. Must call find_character()."""
    idx_battles = 3
    idx_won = 4
    idx_lost = 5
    idx_drawn = 6
    idx_health = 7

    found_index = find_character(character_list, name)
    if found_index != -1:
        print(str(name) + " already exists in character list.")
        return character_list

    # Build new record
    new_character = [name, secret_identity, hero_flag, 0, 0, 0, 0, 100]
    character_list.append(new_character)
    print("Successfully added " + str(name) + " to character list.")
    return character_list


def remove_character(character_list, name):
    """Removes a character by name; returns updated list. Must call find_character()."""
    found_index = find_character(character_list, name)
    if found_index == -1:
        print(str(name) + " is not found in characters.")
        return character_list

    # Rebuild list without the character (no remove/pop methods; append allowed)
    updated_character_list = []
    current_index = 0
    total_items = len(character_list)
    while current_index < total_items:
        if current_index != found_index:
            updated_character_list.append(character_list[current_index])
        current_index = current_index + 1

    print("Successfully removed " + str(name) + " from character list.")
    return updated_character_list


def display_highest_battles_won(character_list):
    """Displays the character with the highest number of battles won; tie-breaker: lower battles fought."""
    if len(character_list) == 0:
        print("No such character found; please try again later.")
        return

    idx_name = 0
    idx_battles = 3
    idx_won = 4

    current_index = 0
    total_items = len(character_list)
    best_index = -1
    while current_index < total_items:
        if best_index == -1:
            best_index = current_index
        else:
            wins_i = int(character_list[current_index][idx_won])
            wins_best = int(character_list[best_index][idx_won])
            battles_i = int(character_list[current_index][idx_battles])
            battles_best = int(character_list[best_index][idx_battles])
            if wins_i > wins_best:
                best_index = current_index
            elif wins_i == wins_best and battles_i < battles_best:
                best_index = current_index
        current_index = current_index + 1

    # Check if all wins are zero
    all_wins_zero = True
    current_index = 0
    while current_index < total_items:
        if int(character_list[current_index][idx_won]) != 0:
            all_wins_zero = False
        current_index = current_index + 1
    if all_wins_zero:
        print("No such character found; please try again later.")
        return

    # Exact tie (same wins and same battles)
    exact_tie_exists = False
    current_index = 0
    while current_index < total_items:
        if current_index != best_index:
            if (
                int(character_list[current_index][idx_won]) == int(character_list[best_index][idx_won])
                and int(character_list[current_index][idx_battles]) == int(character_list[best_index][idx_battles])
            ):
                exact_tie_exists = True
        current_index = current_index + 1
    if exact_tie_exists:
        print("No such character found; please try again later.")
        return

    print(
        "Highest number of battles won => "
        + str(character_list[best_index][idx_name])
        + " with "
        + str(character_list[best_index][idx_won])
        + " opponents defeated!"
    )


def do_battle(character_list, opponent_one_index, opponent_two_index):
    """Simulates a battle between two characters selected by index. Prompts for rounds (1–5)."""
    idx_name = 0
    idx_health = 7
    idx_battles = 3
    idx_won = 4
    idx_lost = 5
    idx_drawn = 6

    MIN_ROUNDS = 1
    MAX_ROUNDS = 5
    MIN_DMG = 0
    MAX_DMG = 50

    # Read number of rounds with validation
    valid_rounds = False
    rounds = 0
    while (not valid_rounds):
        try:
            rounds = int(input("Please enter number of battle rounds: "))
            if rounds >= MIN_ROUNDS and rounds <= MAX_ROUNDS:
                valid_rounds = True
            else:
                print("Not a valid command - please try again.")
        except Exception:
            print("Not a valid command - please try again.")

    name1 = str(character_list[opponent_one_index][idx_name])
    name2 = str(character_list[opponent_two_index][idx_name])

    print()
    print("-- Battle --")
    print()
    print(name1 + " versus " + name2 + " - " + str(rounds) + " rounds")
    print()

    current_round = 0
    while (
        current_round < rounds
        and int(character_list[opponent_one_index][idx_health]) > 0
        and int(character_list[opponent_two_index][idx_health]) > 0
    ):
        current_round = current_round + 1
        damage_one = random.randint(MIN_DMG, MAX_DMG)
        damage_two = random.randint(MIN_DMG, MAX_DMG)

        health_one = int(character_list[opponent_one_index][idx_health]) - damage_one
        health_two = int(character_list[opponent_two_index][idx_health]) - damage_two
        if health_one < 0:
            health_one = 0
        if health_two < 0:
            health_two = 0
        character_list[opponent_one_index][idx_health] = health_one
        character_list[opponent_two_index][idx_health] = health_two

        print("Round: " + str(current_round))
        print("  > " + name1 + " - Damage: " + str(damage_one) + " - Current health: " + str(health_one))
        print("  > " + name2 + " - Damage: " + str(damage_two) + " - Current health: " + str(health_two))
        print()

    print("-- End of battle --")
    print()

    final_health_one = int(character_list[opponent_one_index][idx_health])
    final_health_two = int(character_list[opponent_two_index][idx_health])

    # Update battle counts (one battle)
    character_list[opponent_one_index][idx_battles] = int(character_list[opponent_one_index][idx_battles]) + 1
    character_list[opponent_two_index][idx_battles] = int(character_list[opponent_two_index][idx_battles]) + 1

    if final_health_one > 0 and final_health_two > 0:
        if final_health_one > final_health_two:
            character_list[opponent_one_index][idx_won] = int(character_list[opponent_one_index][idx_won]) + 1
            character_list[opponent_two_index][idx_lost] = int(character_list[opponent_two_index][idx_lost]) + 1
            print("** " + name1 + " wins! **")
        elif final_health_two > final_health_one:
            character_list[opponent_two_index][idx_won] = int(character_list[opponent_two_index][idx_won]) + 1
            character_list[opponent_one_index][idx_lost] = int(character_list[opponent_one_index][idx_lost]) + 1
            print("** " + name2 + " wins! **")
        else:
            character_list[opponent_one_index][idx_drawn] = int(character_list[opponent_one_index][idx_drawn]) + 1
            character_list[opponent_two_index][idx_drawn] = int(character_list[opponent_two_index][idx_drawn]) + 1
            print("-- A tie. Nobody wins.")
    elif final_health_one <= 0 and final_health_two <= 0:
        print("** " + name1 + " has died **")
        print("** " + name2 + " has died **")
        character_list[opponent_one_index][idx_drawn] = int(character_list[opponent_one_index][idx_drawn]) + 1
        character_list[opponent_two_index][idx_drawn] = int(character_list[opponent_two_index][idx_drawn]) + 1
    elif final_health_one <= 0:
        print("** " + name1 + " has died **")
        character_list[opponent_two_index][idx_won] = int(character_list[opponent_two_index][idx_won]) + 1
        character_list[opponent_one_index][idx_lost] = int(character_list[opponent_one_index][idx_lost]) + 1
    else:
        print("** " + name2 + " has died **")
        character_list[opponent_one_index][idx_won] = int(character_list[opponent_one_index][idx_won]) + 1
        character_list[opponent_two_index][idx_lost] = int(character_list[opponent_two_index][idx_lost]) + 1


def sort_by_health(character_list):
    """Returns a COPY of the list sorted by health (desc), tie: battles fought (desc). No list.sort()."""
    # make a copy using only append
    copy_list = []
    idx = 0
    n = len(character_list)
    while idx < n:
        copy_list.append(character_list[idx])
        idx = idx + 1

    idx_health = 7   # health column
    idx_battles = 3  # battles column

    # Bubble sort (health desc, then battles desc)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            left = copy_list[j]
            right = copy_list[j + 1]

            swap = False
            if int(left[idx_health]) < int(right[idx_health]):
                swap = True
            elif int(left[idx_health]) == int(right[idx_health]) and int(left[idx_battles]) < int(right[idx_battles]):
                swap = True

            if swap:
                temp = copy_list[j]
                copy_list[j] = copy_list[j + 1]
                copy_list[j + 1] = temp

            j = j + 1
        i = i + 1

    return copy_list


def print_header(author_name, email_id, file_name):
    print("File     : " + str(file_name))
    print("Author   : " + str(author_name))
    print("Email ID : " + str(email_id))
    print("Description: Programming Assignment 3 - Manage Character (Hero and Villain) Information")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    print()


def main():
    # Local header variables (edit these three values before submission)
    file_name_shown = "assignment3_chojy083.py"
    author_shown = "Joon Choi"
    email_shown = "chojy083"

    print_header(author_shown, email_shown, file_name_shown)

    # Load data
    try:
        character_list = read_file("characters.txt")
    except FileNotFoundError:
        print("characters.txt was not found in the same folder as this program.")
        print("Place 'characters.txt' next to this .py file and run again.")
        return

    # Menu loop (no while True)
    choice = ""
    while choice != "quit":
        print("Please enter choice")
        choice = input("[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")

        if choice == "list":
            display_characters(character_list, 0)
        elif choice == "heroes":
            display_characters(character_list, 1)
        elif choice == "villains":
            display_characters(character_list, 2)
        elif choice == "search":
            name = input("Please enter name: ")
            found_index = find_character(character_list, name)
            if found_index == -1:
                print(name + " is not found in character (heroes and villains) list.")
            else:
                idx_name = 0
                idx_secret = 1
                idx_flag = 2
                idx_battles = 3
                idx_won = 4
                idx_lost = 5
                idx_drawn = 6
                idx_health = 7

                role = "HERO"
                if character_list[found_index][idx_flag] == "v":
                    role = "VILLAIN"
                print("\nAll about " + str(character_list[found_index][idx_name]) + " --> " + role + "\n")
                print("Secret identity: " + str(character_list[found_index][idx_secret]) + "\n")
                print("Battles fought: " + str(character_list[found_index][idx_battles]))
                print("  > No won:  " + format(int(character_list[found_index][idx_won]), ">3d"))
                print("  > No lost: " + format(int(character_list[found_index][idx_lost]), ">3d"))
                print("  > No drawn:" + format(int(character_list[found_index][idx_drawn]), ">3d"))
                print("Current health: " + str(character_list[found_index][idx_health]) + "% ")
        elif choice == "reset":
            name = input("Please enter name: ")
            found_index = find_character(character_list, name)
            if found_index == -1:
                print(name + " is not found in character (heroes and villains) list.")
            else:
                idx_health = 7
                character_list[found_index][idx_health] = 100
                print("Successfully updated " + name + "'s health to 100")
        elif choice == "add":
            name = input("Please enter name: ")
            secret_id = input("Please enter secret_identity: ")
            hero = ""
            while hero != "h" and hero != "v":
                hero = input("Is this character a hero or a villain [h|v]? ")
                if hero != "h" and hero != "v":
                    print("Not a valid command - please try again.")
            character_list = add_character(character_list, name, secret_id, hero)
        elif choice == "remove":
            name = input("Please enter name: ")
            character_list = remove_character(character_list, name)
        elif choice == "high":
            display_highest_battles_won(character_list)
        elif choice == "battle":
            opponent_one_name = input("Please enter opponent one's name: ")
            opponent_one_index = find_character(character_list, opponent_one_name)
            while opponent_one_index == -1:
                print(opponent_one_name + " is not found in character (heroes and villains) list.")
                opponent_one_name = input("Please enter opponent one's name: ")
                opponent_one_index = find_character(character_list, opponent_one_name)

            opponent_two_name = input("Please enter opponent two's name: ")
            opponent_two_index = find_character(character_list, opponent_two_name)
            while opponent_two_index == -1 or opponent_two_name == opponent_one_name:
                if opponent_two_name == opponent_one_name:
                    print("A character must not battle against himself/herself.")
                else:
                    print(opponent_two_name + " is not found in character (heroes and villains) list.")
                opponent_two_name = input("Please enter opponent two's name: ")
                opponent_two_index = find_character(character_list, opponent_two_name)

            do_battle(character_list, opponent_one_index, opponent_two_index)
        elif choice == "health":
            sorted_copy = sort_by_health(character_list)
            display_characters(sorted_copy, 0)
        elif choice == "quit":
            write_to_file("new_characters.txt", character_list)
            print("\n-- Program terminating --\n")
        else:
            print("\nNot a valid command - please try again.\n")


if __name__ == "__main__":
    main()
