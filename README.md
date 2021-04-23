# Bitcoin Rate API

### FEATURES

- Basically,those lines of codes gets data from google search engine instantly;
- Two library included;

### Explanation
- Bot program gets the data from search engine as html file;
- Bot program finds the exact position of the rate;
- After the position program retuns the rate as a string;

### Database connection
- If someone wants to connect database for storing values;
- It will be useful those code;

```python
    import sqlite3
    
    def databaseInsert(db_name,date,data):

        con = sqlite3.connect(db_name) 

        cursor = con.cursor() 

        cursor.execute("INSERT INTO data (time, value) VALUES ('date', 'data')")

        cursor.close()

```
## Licence & copyright

© Can Rollas , Bitcoin Rate Api

Licensed under the [Apache License](LICENSE).
