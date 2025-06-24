# API

```yaml
# List and add a CARD
# /api/card/ after a POST it returns the single card that was added
# {"id": ..., "front": ..., "back": ..., "card_type": "Flashcard"}
/api/card/      # [GET, POST]
/api/card/1     # [GET, POST, DELETE, PUT]

# List a QUIZ
/api/quiz/      # [GET]
/api/quiz/1     # [GET]


# Add a QUIZ
# /add/        → Lists all cards to assign to a quiz
# /add/?quiz=2 → Lists only the cards in the quiz id
# Quiz id is 2 in this case and it filters cards for the 'Operating Systems' quiz
/api/quiz/add/            # [GET, POST]
/api/quiz/add/?quiz=1     # [GET, POST]

# Example
1. Add a CARD               (/api/quiz/add/)
2. Go to the QUIZ endpoint  (/api/quiz/add/)
3. Assign a card to a QUIZ or multiple QUIZZES
```

# Quizzes

```yaml
# Model: Quiz
Keeps track of of (1) the id its details and (2) an id of the card belonging to the quiz

# Model: Quiz details
# Keeps name and category
# Category is only used for sorting the quizzes
# To keep them together
╔═════════════════╦══════════════════╗
║       Name      ║     Category     ║
╠═════════════════╬══════════════════╣
║ Algorithms      ║ Computer Science ║
╠═════════════════╬══════════════════╣
║ Data Structures ║ Computer Science ║
╠═════════════════╬══════════════════╣
║ OS              ║ Computer Science ║
╠═════════════════╬══════════════════╣
║ Programming     ║ Programming      ║
╠═════════════════╬══════════════════╣
║ Python          ║ Programming      ║
╠═════════════════╬══════════════════╣
║ Django          ║ Programming      ║
╠═════════════════╬══════════════════╣
║ React           ║ Programming      ║
╠═════════════════╬══════════════════╣
║ Backend         ║ Programming      ║
╚═════════════════╩══════════════════╝
```