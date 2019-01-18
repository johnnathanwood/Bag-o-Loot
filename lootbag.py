import sqlite3

import sys

lootbagdb = '/Users/John/pythoncourse/exercises/bag/lootbag.db'

def getChildren():
  # The connect() function opens a connection to an SQLite database. It returns a Connection object that represents the database.
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM child')
    children = cursor.fetchall()
    print(children)  


def getChild(child):
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    cursor.execute(f'''SELECT  * FROM Child 
                      JOIN Gift 
                      ON Child.ChildId = Gift.giftId
                      WHERE Child.Name = '{child}'
                    ''')
    child = cursor.fetchone()
    print(child)
    return child

def addChild(child):
  with sqlite3.connect(lootbagdb) as conn:
    cursor = conn.cursor()

    try:
      # Have to use a specific syntax for inserts and updates, to keep baddies from using injection attacks
      cursor.execute(
        '''
        INSERT INTO Child
        Values(?,?,?)
        ''', (None, child["Name"], child["receiving"])
      )
    except sqlite3.OperationalError as err:
      print("oops", err)

def checkChild(child):
  with sqlite3.connect(lootbagdb) as conn:
      cursor = conn.cursor()
      try:
        print(child)
        cursor.execute(f'''SELECT *
                         FROM child
                         Where child.Name = '{child}'
                         ''')
        child_check = cursor.fetchone()
        print("test",child_check)
        if child_check == None:
          cursor.execute(
            '''
            Insert Into Child
              Values(?, ?, ?)
            ''', (None, child ,1)
          )
          cursor.execute(f'''SELECT *
                         FROM child 
                         Where child.Name = '{child}'
                         ''')
          child_check = cursor.fetchone()
          print(child_check)
          return child_check
      except sqlite3.OperationalError as err:
        print("Child already exist", err)
        print()

def addGift(gift):
    with sqlite3.connect(lootbagdb) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                '''
                INSERT INTO Gift
                values(?,?,?,?)
                ''',
                (None, gift["Name"], gift["delivered"], gift["childId"])
            )
        except sqlite3.OperationalError as err:
            print("oops", err)

# def removeGift(gift):
#     wit
















# Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word add. The second argument is the gift to be delivered. The third argument is the name of the child.

  

# Remove a toy from the bag o' loot in case a child's status changes before delivery starts.



# Produce a list of children currently receiving presents.



# List toys in the bag o' loot for a specific child.



# Specify when a child's toys have been delivered.





# Testing
# Each feature of the app must be tested. Use Python's unittest module to create test coverage for the following app requirements

# Items can be added to bag, and assigned to a child.


# Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.


# Must be able to list all children who are getting a toy.


# Must be able to list all toys for a given child's name.


# Must be able to set the delivered property of a child's toys -- which defaults to false-- to true.
if __name__ == '__main__':
    checkChild("Sam")

    # addGift({
    #     'Name': "dildo",
    #     'delivered': 0,
    #     'childId': 11,
    # })