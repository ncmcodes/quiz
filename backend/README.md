# API

| URL                        	| Methods                      	| Description                                                                                                                                        	|
|----------------------------	|------------------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|
| /api/card/                 	| GET<br>POST                  	| A list of all cards<br>- id<br>- front<br>- back<br>- card_type<br>- front_html<br>- back_html                                                     	|
| /api/card/\<id\>             	| GET<br>POST<br>PUT<br>DELETE 	|                                                                                                                                                    	|
| /api/quiz/                 	| GET                          	| A list of all quizzes<br>- id<br>- name<br>- category                                                                                              	|
| /api/quiz/\<id\>             	| GET                          	|                                                                                                                                                    	|
| /api/cards/categorize/     	| GET                          	| A list of cards with a quizzes array (which quizzes does this card belong to)<br>- id<br>- front<br>- quizzes [{"quiz_id": val, "name": val}, ...] 	|
| /api/cards/categorize/\<id\> 	| PUT                          	| Update a the list of quizzes a card belongs to |


---
# Database Example
```
╔═══════════════════════════════════════╗
║               Quiz Details            ║
╠════╦═══════════════╦══════════════════╣
║ id ║ name          ║ category         ║
╠════╬═══════════════╬══════════════════╣
║ 1  ║ US Presidents ║ History          ║
╠════╬═══════════════╬══════════════════╣
║ 2  ║ WWI           ║ History          ║
╠════╬═══════════════╬══════════════════╣
║ 3  ║ OS            ║ Computer Science ║
╠════╬═══════════════╬══════════════════╣
║ 4  ║ Data Struct   ║ Computer Science ║
╠════╬═══════════════╬══════════════════╣
║ 5  ║ Algorithms    ║ Computer Science ║
╠════╬═══════════════╬══════════════════╣
║ 6  ║ Backend       ║ Programming      ║
╚════╩═══════════════╩══════════════════╝

╔═════════════════════╗
║         Quiz        ║
╠═══════════╦═════════╣
║ quiz      ║ card_id ║
╠═══════════╬═════════╣
║ 1         ║ 1       ║  (card about US presidents, History)
╠═══════════╬═════════╣
║ 1         ║ 2       ║  (card about US presidents, History)
╠═══════════╬═════════╣
║ 3         ║ 3       ║  (card about OS, CS)
╚═══════════╩═════════╝

╔════════════════════════════════════════════════════════════════════════════╗
║                                    Card                                    ║
╠════╦═══════════════════════════════════════╦═══════════════════╦═══════════╣
║ id ║ front                                 ║ back              ║ card_type ║
╠════╬═══════════════════════════════════════╬═══════════════════╬═══════════╣
║ 1  ║ Name of the 1st USA president         ║ George Washington ║ Flashcard ║
╠════╬═══════════════════════════════════════╬═══════════════════╬═══════════╣
║ 2  ║ Name of the 2nd USA president         ║ John Adams        ║ Flashcard ║
╠════╬═══════════════════════════════════════╬═══════════════════╬═══════════╣
║ 3  ║ Difference between process and thread ║ ...               ║ Flashcard ║
╚════╩═══════════════════════════════════════╩═══════════════════╩═══════════╝
```

---

# Tests

```bash
# Get refresh_token and access_token (HTTPONLY JWT Cookie)
http --session=auth_session POST http://127.0.0.1:8000/auth/token/ username='test' password='test'

# Given the refresh_token get a renewed access_token (HTTPONLY JWT Cookie)
http --session=auth_session POST http://127.0.0.1:8000/auth/token/refresh/

# Add a flashcard
http --session=auth_session POST 127.0.0.1:8000/api/card/ front="USA's 3rd President" back="Thomas Jefferson" card_type="Flashcard"
http POST 127.0.0.1:8000/api/card/ front="USA's 3rd President" back="Thomas Jefferson" card_type="Flashcard" Cookie:"access_token=…"

# Add a card to a list of quizzes
http --session=auth_session PUT 127.0.0.1:8000/api/cards/categorize/3 quizzes:='[1, 2, 3]'
http PUT 127.0.0.1:8000/api/cards/categorize/3 quizzes:='[1, 2, 3]' Cookie:"access_token=…"



# ----------#
# Run tests #
# ----------#
uv run manage.py test quizAPI --settings=quiz.settings.tests
uv run manage.py test quizAUTH --settings=quiz.settings.tests
```
