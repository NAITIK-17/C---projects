import random
# Game: Mafia

def assign_roles():
    roles = (
        ['Civilian'] * 4 +
        ['Mafia'] * 3 +
        ['Doctor'] * 2 +
        ['Cop'] * 4
    )
    random.shuffle(roles)
    user_role = roles.pop()  # Assign one role to user
    bot_roles = roles        # Remaining roles for bots

    # Assign names to bots
    bot_names = [f"Bot{i+1}" for i in range(len(bot_roles))]
    bots = dict(zip(bot_names, bot_roles))
    return user_role, bots

def get_alive_players(user_alive, bots_alive):
    alive = []
    if user_alive:
        alive.append("You")
    alive.extend([name for name, alive in bots_alive.items() if alive])
    return alive

def mafia_night(bots, bots_alive, user_alive, user_role):
    # Mafia chooses a target
    mafia_bots = [name for name, role in bots.items() if role == "Mafia" and bots_alive[name]]
    possible_targets = [name for name, alive in bots_alive.items() if alive and bots[name] != "Mafia"]
    if user_alive and user_role != "Mafia":
        possible_targets.append("You")
    if not possible_targets:
        return None
    target = random.choice(possible_targets)
    return target

def doctor_save(bots, bots_alive, user_alive, user_role):
    # Doctor chooses someone to save
    doctor_bots = [name for name, role in bots.items() if role == "Doctor" and bots_alive[name]]
    possible_saves = [name for name, alive in bots_alive.items() if alive]
    if user_alive:
        possible_saves.append("You")
    if not possible_saves:
        return None
    save = random.choice(possible_saves)
    return save

def main():
    print("Welcome to the Mafia Game!\n")
    input("Press Enter to start the game")
    user_role, bots = assign_roles()
    print(f"You are a {user_role} in the game.")
    print("\nBots and their roles (for debugging/demo):")
    for name, role in bots.items():
        print(f"{name}: {role}")

    # Track alive status
    bots_alive = {name: True for name in bots}
    user_alive = True

    round_num = 1
    while True:
        print(f"\n--- Night {round_num} ---")
        # Mafia chooses a target
        target = mafia_night(bots, bots_alive, user_alive, user_role)
        # Doctor chooses someone to save
        saved = doctor_save(bots, bots_alive, user_alive, user_role)

        # Announce actions (for demo)
        print(f"Mafia targeted: {target}")
        print(f"Doctor saved: {saved}")

        # Resolve night
        if target == saved:
            print(f"{target} was saved by the doctor!")
        else:
            if target == "You":
                user_alive = False
                print("You were eliminated by the mafia!")
            elif target:
                bots_alive[target] = False
                print(f"{target} was eliminated by the mafia!")

        # Check win conditions
        mafia_count = sum(1 for name, alive in bots_alive.items() if alive and bots[name] == "Mafia")
        civilian_count = sum(1 for name, alive in bots_alive.items() if alive and bots[name] != "Mafia")
        if user_alive and user_role != "Mafia":
            civilian_count += 1
        if mafia_count == 0:
            print("Civilians win! All mafia have been eliminated.")
            break
        if mafia_count >= civilian_count:
            print("Mafia win! Mafia have taken over the town.")
            break
        if not user_alive:
            print("Game over! You have been eliminated.")
            break

        round_num += 1

if __name__ == "__main__":
    main()
