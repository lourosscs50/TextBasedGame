Whispers of the Carnival is a command-line text adventure game where players explore a haunted carnival, collect enchanted relics, and confront the sinister Ringmaster Hex.

To win, the player must collect all 6 relics before entering the Big Top Tent. Entering unprepared results in defeat.

This project demonstrates:

Game state management

Command parsing and input normalization

Dictionary-based world modeling

Inventory systems

Win/Loss state logic

Functional program decomposition

Type hint usage for clarity and maintainability

The design emphasizes clean separation of responsibilities and scalable structure for future expansion.


Initialize Game State
        ↓
Display Status
        ↓
Parse Player Input
        ↓
Execute Action
        ↓
Update Game State
        ↓
Check Win/Loss
        ↓
Repeat


rooms = {
    "Room Name": {
        "North": "Another Room",
        "South": "Another Room",
        "item": "Item Name"
    }
}


Win Condition

Player collects all 6 relics

Enters the Big Top Tent

Game ends with victory message

Loss Condition

Player enters Big Top Tent

Has fewer than 6 relics

Immediate defeat


While this is a game project, the architectural principles mirror real-world systems:

State machines

User input parsing

Data modeling

Permission checks (inventory gate logic)

Controlled transitions between states

These patterns apply directly to:

Backend systems

Workflow engines

CLI tools

Finite state applications

Game development fundamentals


