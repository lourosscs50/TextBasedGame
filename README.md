🎪 Whispers of the Carnival

Whispers of the Carnival is a command-line text adventure game where players explore a haunted carnival, collect enchanted relics, and confront the sinister Ringmaster Hex.

To achieve victory, players must collect all six relics before entering the Big Top Tent. Entering unprepared results in immediate defeat.

While presented as a game, this project focuses on software architecture concepts commonly used in real-world systems such as state management, command parsing, and controlled workflow transitions.

⸻

🚀 Overview

The game simulates a finite-state environment where player actions drive transitions between locations and outcomes. The system continuously processes user input, updates game state, and evaluates win/loss conditions.

The design emphasizes maintainability, modular structure, and scalability for future feature expansion.

⸻

✨ Features
	•	Interactive command-line gameplay
	•	Room-based navigation system
	•	Collectible inventory system
	•	Command parsing with input normalization
	•	Win/Loss state evaluation
	•	Structured world modeling using dictionaries
	•	Modular function-based architecture
	•	Type hint usage for clarity and maintainability

⸻

🧱 Tech Stack
	•	Language: Python
	•	Concepts Used:
	•	State management
	•	Data modeling
	•	Input parsing
	•	Functional decomposition
	•	Type hints
	•	CLI interaction

🏗️ Game Architecture
Game Loop
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

World Model

The game world is represented using a dictionary-based structure:
rooms = {
    "Room Name": {
        "North": "Another Room",
        "South": "Another Room",
        "item": "Item Name"
    }
}


This structure enables scalable expansion of rooms, items, and navigation logic.

⸻

🧠 Engineering Concepts Demonstrated

Although implemented as a game, the architecture mirrors real-world software systems:
	•	State machines
	•	Command parsing engines
	•	Structured data modeling
	•	Inventory-based permission checks
	•	Controlled state transitions
	•	Workflow logic management

These patterns directly apply to:
	•	Backend systems
	•	Workflow engines
	•	CLI tools
	•	Finite state applications
	•	Game development fundamentals

⸻

🏆 Win Condition
	•	Player collects all 6 enchanted relics
	•	Player enters the Big Top Tent
	•	Victory message displayed

⸻

💀 Loss Condition
	•	Player enters the Big Top Tent
	•	Fewer than 6 relics collected

Result: Immediate defeat.


⚙️ How to Run

Clone Repository
git clone https://github.com/lourosscs50/Whispers-of-the-Carnival.git
cd Whispers-of-the-Carnival
Run Game
hauntedcarnival.py

🎯 Purpose

This project was built to demonstrate structured program design through an interactive system emphasizing:
	•	State-driven logic
	•	User input handling
	•	Modular architecture
	•	Maintainable code organization

It highlights how game systems share architectural similarities with production software systems.

⸻

🔮 Future Improvements
	•	Save/load game state
	•	Expanded world map
	•	NPC interaction system
	•	Command auto-complete
	•	GUI version
	•	JSON-based world configuration

⸻

👨‍💻 Author

Lou Carron
Software Developer | Backend Systems | Python | .NET

GitHub: https://github.com/lourosscs50
LinkedIn: https://www.linkedin.com/in/lou-carron-2b2652123?trk=contact-info

📄 License

This project is intended for educational and portfolio demonstration purposes.