import pyodbc

connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" 

                            "Server=MY_PC\SQLEXPRESS;"

                            "Database=phonebook;"

                            "Trusted_Connection=yes;")                      # For making connection with SQL database.


def INSERT():

    id = int(input('Enter the id - '))
    name = input('Enter a name - ')
    namet = name.title()
    phonenumber = int(input('Enter a phonenumber - '))
    email = input('Enter the email address - ')

    cursor = connection.cursor()

    sql= 'INSERT INTO phone_book VALUES (?, ?, ?, ?)' # SQL code.

    tup = (id, namet, phonenumber, email)

    cursor.execute(sql, tup)

    connection.commit()


def FIND():
    
    y = 0
    while not (1 <= y <= 3):
        y = int(input('''
            With which parameter do you want to FIND?
            For name enter 1
            For phonenumber enter 2
            For email enter 3
            Enter -  '''))

    cursor = connection.cursor()

    if y == 1:

        name = input('\t\tEnter a name - ')
        sql = 'SELECT * FROM phone_book WHERE name = ?' # SQL code.
        tup = (name)
        cursor.execute(sql, tup)
        
    elif y == 2:

        phonenumber = int(input('\t\tEnter a phonenumber - '))
        sql = 'SELECT * FROM phone_book WHERE phonenumber = ?' # SQL code.
        tup = (phonenumber)
        cursor.execute(sql, tup)

    elif y == 3:

        email = input('\t\tEnter a email - ')
        sql = 'SELECT * FROM phone_book WHERE email = ?' # SQL code.
        tup = (email)
        cursor.execute(sql, tup)

    for row in cursor: # print the row.

        print('\n', row)

    connection.commit()


def UPDATE():

    id = int(input('Enter the ID you want to update - ')) # Need ID or else we will end up updating every where.

    z = 0
    while not (1 <= z <= 3):
        z = int(input('''
            With which parameter do you want to EDIT?
            For name enter 1
            For phonenumber enter 2
            For email enter 3
            Enter -  '''))
 
    cursor = connection.cursor()

    if z == 1:

        name = input('\t\tEnter a name - ')
        sql = 'UPDATE phone_book SET name = ? WHERE id = ?' # SQL code.
        tup = (name, id)
        cursor.execute(sql, tup)
   
    elif z == 2:

        phonenumber = int(input('\t\tEnter a phonenumber - '))
        sql = 'UPDATE phone_book SET phonenumber = ? WHERE id = ?' # SQL code.
        tup = (phonenumber, id)
        cursor.execute(sql, tup)

    elif z == 3:

        email = input('\t\tEnter a email - ')
        sql = 'UPDATE phone_book SET email = ? WHERE id = ?' # SQL code.
        tup = (email, id)
        cursor.execute(sql, tup)

    # print updated data.

    sql_2 = 'SELECT * FROM phone_book WHERE id = ?' # SQL code.
    tup_2 = (id)
    cursor.execute(sql_2, tup_2)

    for row in cursor:

        print('\n', row)

    connection.commit()


def DELETE():

    id = int(input('\tEnter the id you want to delete - ')) # Need ID or else we will end up deleting every thing.

    cursor = connection.cursor()

    sql= 'DELETE FROM phone_book WHERE id = ?' # SQL code.

    tup = (id)

    cursor.execute(sql, tup)

    connection.commit()


x = 0
while not (1 <= x <= 4):
    x = int(input('''
What do you want to do?
For enter new data enter 1
For find existing data enter 2
For edit existing data enter 3
For delete existing data enter 4
Enter - '''))

match x:
    case 1  : INSERT()
    case 2  : FIND()       # Added different parameters in version 2.0
    case 3  : UPDATE()     # Added in version 3.0
    case 4  : DELETE()     # Added in version 2.0

print('\n---END of Code---\n')