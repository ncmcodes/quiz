# API

| URL                        	| Methods                      	| Description                                                                                                                                        	|
|----------------------------	|------------------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|
| /api/card/                 	| GET<br>POST                  	| A list of all cards<br>- id<br>- front<br>- back<br>- card_type<br>- front_html<br>- back_html                                                     	|
| /api/card/<id>             	| GET<br>POST<br>PUT<br>DELETE 	|                                                                                                                                                    	|
| /api/quiz/                 	| GET                          	| A list of all quizzes<br>- id<br>- name<br>- category                                                                                              	|
| /api/quiz/<id>             	| GET                          	|                                                                                                                                                    	|
| /api/cards/categorize/     	| GET                          	| A list of cards with a quizzes array (which quizzes does this card belong to)<br>- id<br>- front<br>- quizzes [{"quiz_id": val, "name": val}, ...] 	|
| /api/cards/categorize/<id> 	| PUT                          	| Update a the list of quizzes a card belongs to<br><br>Test with:<br>http PUT 127.0.0.1:8000/api/cards/categorize/2 quizzes="[1, 2, 3]"             	|


---
# Database Details
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
# Add a card to a list of quizzes
http PUT 127.0.0.1:8000/api/cards/categorize/3 quizzes:='[1, 2, 3]'

# Add a flashcard
http POST 127.0.0.1:8000/api/card/ front="Name USA's 3rd President" back="Thomas Jefferson" card_type="Flashcard"

# Create a new user
http POST 127.0.0.1:8000/auth/users/ username='djoser' password='super_secret_00_password'

# Create a JWT for the user
http POST 127.0.0.1:8000/auth/jwt/create/ username='djoser' password='super_secret_00_password'

# Get user details
# For token instead of JWT we would replace 'Bearer' with 'Token'. However, this project uses JWT not Token authentication
http GET 127.0.0.1:8000/auth/users/me/ -A bearer -a 'JWT_GOES_HERE'
curl http://127.0.0.1:8000/auth/users/me/ -H 'Authorization: Bearer ACCESS_JWT_HERE'
```
