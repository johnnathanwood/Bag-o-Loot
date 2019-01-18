import sqlite3

import sys

lootbagdb = '/Users/John/pythoncourse/exercises/bag/lootbag.db'


def handleInputs():

    if len(sys.argv) == 2:
        method = sys.argv[1].upper()

    elif len(sys.argv) == 3:
        method = sys.argv[1].upper()
        first = sys.argv[2].title()

    elif len(sys.argv) == 4:
        method = sys.argv[1].upper()
        first = sys.argv[2].title()
        second = sys.argv[3].title()

    if method == "LS":
        if len(sys.argv) == 2:
            getChildren()
    
    if method == "ADD":
        taco = checkChild(second)
        print(taco)
        addGift(taco[0], first)


def getChildren():
  print("here it is")
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
        return child_check
      except sqlite3.OperationalError as err:
        print("Child already exist", err)
        print()



def addGift(childId, gift):
    with sqlite3.connect(lootbagdb) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                '''
                INSERT INTO Gift
                values(?,?,?,?)
                ''',
                (None, gift, 0, childId)
            )
        except sqlite3.OperationalError as err:
            print("oops", err)

def checkGift(name, childId):
  with sqlite3.connect(lootbagdb) as conn:
      cursor = conn.cursor()
      try:
        cursor.execute(f'''SELECT *
                          FROM gift
                          Join child
                          On child.childId = gift.childId
                          Where gift.Name = "{name}"
                          And child.childId = {childId}
                         ''')
        gift_check = cursor.fetchone()
        return gift_check
      except sqlite3.OperationalError as err:
        print("error", err)
        print()
        temp = "None"
        return temp

def removeGift(gift):
    print(gift)
    giftId = gift
    with sqlite3.connect(lootbagdb) as conn:
      cursor = conn.cursor()
      try:
        cursor.execute(f'''DELETE from gift
                          Where gift.giftId = {giftId}
                        ''')
        print(f"{gift} has been removed")
        print()
      except ValueError as err:
        print(f"Delete Error: {err}")
        print()



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
    handleInputs()
