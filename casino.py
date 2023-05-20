import sqlite3
import hashlib
from random import randint
import getpass

def md5sum(value):  #hashirovanie
    return hashlib.md5(value.encode()).hexdigest()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    query = """ 
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name VARCHAR(30),
        age INTEGER(3),
        balance INTEGER NOT NULL DEFAULT 1000,
        login VARCHAR(15),
        password VARCHAR(20)
        );
    CREATE TABLE IF NOT EXISTS casino(
        name VARCHAR(50),
        description TEXT(300),
        balance BIGINT NOT NULL DEFAULT 5000
    )
    """

    cursor.executescript(query)



def registration():
    print("-----------------------------------------------")
    name = input("Reg Name: ")
    age = int(input("Reg Age: "))
    login = input("Reg Login: ")
    password = getpass.getpass("Reg Password: ")
    print("-----------------------------------------------")
    try:
        db = sqlite3.connect("database.db")
        cursor = db.cursor()

        db.create_function("md5", 1, md5sum)

        cursor.execute("SELECT login FROM users WHERE login = ?", [login])
        if cursor.fetchone() is None:
            values =[name, age, login, password]

            cursor.execute("INSERT INTO users(name, age, login, password) VALUES(?, ?, ?, md5(?))", values)
            db.commit()
            log_in()
        else:
            print("This login is exists")
            registration()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()


def log_in():
    login = input("Login: ")
    password = getpass.getpass("Password: ")

    #db.create_function("md5", 1, md5sum)

    try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            
            db.create_function("md5", 1, md5sum)

            cursor.execute("SELECT login FROM users WHERE login = ?", (login,))
            if cursor.fetchone() is None:
                    print("This login is not exists")
                    registration()
            else:
                cursor.execute("SELECT password FROM users WHERE login = ? AND password = md5(?)", (login, password,))
                if cursor.fetchone() is None:
                    print("Password is not correct. Try again.")
                    log_in()
                else:
                    play_casino(login)
    except sqlite3.Error() as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()
        

def play_casino(login):
    print("\nCASINO 🎰🎲")
    try:
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            
            cursor.execute("SELECT age FROM users WHERE login = ? AND age >= ?", [login, 18])
            if cursor.fetchone() is None:
                print("You are so small")
            else:
                balance = cursor.execute("SELECT balance FROM users WHERE login = ?", [login]).fetchone()[0]
                print("You have,", balance, "$")
                bet = int(input("Bet: "))
                number = randint(1, 100)

                
                if balance < bet:
                    print("You are dont have money")
                    print("\nBy by👋👋👋\n")
                elif balance <= 0:
                    print("You are dont have any money")
                else:
                    if number < 50:
                        cursor.execute("UPDATE users SET balance = balance - ? WHERE login = ?", [bet, login])
                        cursor.execute("UPDATE casino SET balance = balance + ?", [bet])
                        print("YOU ARE LOOSE")
                        new_balance = cursor.execute("SELECT balance FROM users WHERE login = ?", [login]).fetchone()[0]
                        print("You have,", new_balance, "$")
                        
                        trychance = input("Do you want try again? (Y/N) ")
                        while trychance != 'Y' or trychance != 'N' or trychance != 'y' or trychance != 'n':
                            if trychance == 'Y' or trychance == 'N' or trychance == 'y' or trychance == 'n':
                                break
                            print("I dont understand you.")
                            trychance = input("Do you want try again? (Y/N) ")
                        if trychance == 'Y' or trychance == 'y':
                            db.commit()
                            play_casino(login)
                        elif trychance == 'N' or trychance == 'n':
                            print("\nBy by👋👋👋\n")
                        
                    else:
                        cursor.execute("UPDATE users SET balance = balance + ? WHERE login = ?", [bet, login])
                        cursor.execute("UPDATE casino SET balance = balance - ?", [bet])
                        print("YOU ARE WIN")
                        new_balance = cursor.execute("SELECT balance FROM users WHERE login = ?", [login]).fetchone()[0]
                        print("You have,", new_balance, "$")
                        
                        trychance = input("Do you want try again? (Y/N) ")
                        while trychance != 'Y' or trychance != 'N' or trychance != 'y' or trychance != 'n':
                            if trychance == 'Y' or trychance == 'N' or trychance == 'y' or trychance == 'n':
                                break
                            print("I dont understand you.")
                            trychance = input("Do you want try again? (Y/N) ")
                        if trychance == 'Y' or trychance == 'y':
                            db.commit()
                            play_casino(login)
                        elif trychance == 'N' or trychance == 'n':
                            print("\nBy by👋👋👋\n")
                            
                db.commit()
                
    except sqlite3.Error() as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()
    #db = sqlite3.connect("database.db")
    #cursor = db.cursor()
    #for i in cursor.execute('SELECT balance FROM casino'):
    #    print(i)
    #cursor.close()
    #db.close()
    
    
#registration()
log_in()