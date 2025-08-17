# TextBasedGame.py
# Author: Lou Carron
# Theme: Haunted Carnival – "Whispers of the Carnival"
# Goal: Collect all 6 relics before entering the Ringmaster's Big Top.

from typing import Dict, List, Tuple


def show_instructions() -> None:
    """Print the main menu and available commands for the player."""
    print("Whispers of the Carnival — Text Adventure")
    print("Collect all 6 enchanted relics to escape the haunted carnival.")
    print("If you enter the Big Top without all relics, you lose.")
    print("--------------------------------------------------------")
    print("Move commands: go North | go South | go East | go West")
    print("Shortcuts: N, S, E, W  (or just 'north', etc.)")
    print("Get item:   get <item name>")
    print("Quit:       exit")
    print("--------------------------------------------------------")


def show_status(current_room: str, inventory: List[str], rooms: Dict[str, Dict[str, str]]) -> None:
    """Display the player's current room, inventory, and visible item (if any)."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    room_item = rooms.get(current_room, {}).get('item')
    if room_item and room_item not in inventory:
        print(f"You see a {room_item}")
    print("-" * 30)


def normalize_direction(text: str) -> str | None:
    """
    Convert player text into a canonical direction string:
    Returns: 'North'|'South'|'East'|'West' or None if not a direction.
    Accepts 'north', 'N', 'go north', etc.
    """
    s = text.strip().lower()
    if s.startswith("go "):
        s = s[3:].strip()
    if s in {"n", "s", "e", "w"}:
        s = {"n": "north", "s": "south", "e": "east", "w": "west"}[s]
    if s in {"north", "south", "east", "west"}:
        return s.title()
    return None


def parse_command(raw: str) -> Tuple[str, str]:
    """
    Parse the player's input into a (verb, argument) tuple.
    Examples:
      'go north' -> ('move', 'North')
      'north'    -> ('move', 'North')
      'get Crystal Apple' -> ('get', 'Crystal Apple')
      'exit'     -> ('exit', '')
    """
    raw = raw.strip()
    if not raw:
        return "invalid", ""

    if raw.lower() == "exit":
        return "exit", ""

    # Move command variants
    direction = normalize_direction(raw)
    if direction:
        return "move", direction

    # 'get' command
    parts = raw.split(maxsplit=1)
    if len(parts) == 2 and parts[0].lower() == "get":
        return "get", parts[1].strip()

    # If player typed just 'get' with no item
    if raw.lower() == "get":
        return "get", ""

    return "invalid", ""


def main() -> None:
    # Map & items — no item in start or villain room
    rooms = {
        # Start room (no item)
        "Entrance Gate": {
            "West": "Broken Carousel",
            "East": "Cotton Candy Tunnels",
            "North": "Mirror Maze",
        },
        # Item rooms
        "Broken Carousel": {
            "East": "Entrance Gate",
            "South": "Ghost Train",
            "item": "Enchanted Locket",
        },
        "Ghost Train": {
            "North": "Broken Carousel",
            "South": "Clown’s Quarters",
            "item": "Silver Pocket Watch",
        },
        "Clown’s Quarters": {
            "North": "Ghost Train",
            "East": "Big Top Tent",
            "item": "Jester's Bell",
        },
        "Cotton Candy Tunnels": {
            "West": "Entrance Gate",
            "South": "House of Cards",
            "item": "Crystal Apple",
        },
        "House of Cards": {
            "North": "Cotton Candy Tunnels",
            "South": "Big Top Tent",
            "item": "Magic Deck",
        },
        "Mirror Maze": {
            "South": "Entrance Gate",
            "item": "Fractured Mirror Shard",
        },
        # Villain room (no item)
        "Big Top Tent": {
            "North": "House of Cards",
            "West": "Clown’s Quarters",
            # villain present here
        },
    }

    # Constants
    VILLAIN_ROOM = "Big Top Tent"
    TOTAL_ITEMS_REQUIRED = 6  # number of relics to win

    # Game state
    current_room = "Entrance Gate"
    inventory: List[str] = []

    show_instructions()

    # Gameplay loop ends on win or loss
    while True:
        show_status(current_room, inventory, rooms)
        user_input = input("Enter your move: ")
        verb, arg = parse_command(user_input)

        if verb == "exit":
            print("Thanks for playing. Goodbye!")
            break

        elif verb == "move":
            # Check if the direction exists from the current room
            next_room = rooms.get(current_room, {}).get(arg)
            if next_room:
                current_room = next_room

                # Check loss condition (entering villain room without all items)
                if current_room == VILLAIN_ROOM:
                    if len(inventory) == TOTAL_ITEMS_REQUIRED:
                        print("\nYou confront Ringmaster Hex armed with all relics!")
                        print("Congratulations! You have collected all items and defeated the Ringmaster!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                    else:
                        print("\nNOM NOM...GAME OVER!")
                        print("Ringmaster Hex traps your soul in the carnival.")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                    break  # game ends on win or loss

            else:
                print("You can't go that way.")

        elif verb == "get":
            room_item = rooms.get(current_room, {}).get("item")
            if not room_item:
                print("There's nothing to get here.")
                continue

            if not arg:
                print(f"Specify the item to get (e.g., get {room_item}).")
                continue

            # Compare case-insensitively to avoid strict typing errors
            if arg.lower() == room_item.lower():
                if room_item in inventory:
                    print("You already picked that up.")
                else:
                    inventory.append(room_item)
                    # Remove item from room so it can't be collected twice
                    rooms[current_room].pop("item", None)
                    print(f"{room_item} added to your inventory.")
                    # Win check (collect all items anywhere except villain)
                    if len(inventory) == TOTAL_ITEMS_REQUIRED:
                        print("\nYou feel the relics resonate... A way out has opened!")
                        print("Now you may face the Ringmaster in the Big Top and win.")
            else:
                print("That item isn't here.")

        else:
            print("Invalid command. Try 'go North', 'get <item>', or 'exit'.")


if __name__ == "__main__":
    main()