import sqlite3
conn = sqlite3.connect('lostfinds.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS lostfinds
             (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, location TEXT, item_type TEXT,other TEXT, contact TEXT)''')

def add_lostfind(date, location, item_type, other, contact):
    c.execute("INSERT INTO lostfinds (date, location, item_type, other, contact) VALUES (?, ?, ?, ?, ?)", 
              (date, location, item_type, other, contact))
    conn.commit() 

def view_lostfinds():
    c.execute("SELECT * FROM lostfinds")
    lostfinds = c.fetchall()
    if not lostfinds:
        print("No items recorded.")
    else:
        for i in lostfinds:
            print(f"ID: {i[0]}, Date: {i[1]}, Location: {i[2]}, Item: {i[3]}, Feauture: {i[4]}, Contact: {i[5]}")
def view_lostfind_by_id(lostfind_id):
    c.execute("SELECT * FROM lostfinds WHERE id=?", (lostfind_id,))
    lostfind_id = c.fetchone()
    if lostfind_id:
        print(f"ID: {lostfind_id[0]}, Date: {lostfind_id[1]}, Location: {lostfind_id[2]}, Item: {lostfind_id[3]}, Feauture: {lostfind_id[4]}, Contact: {lostfind_id[5]}")
    else:
        print("No items recorded with this ID.")
            
def delete_lostfind(lostfind_id):
    c.execute("DELETE FROM lostfinds WHERE id=?", (lostfind_id,))
    conn.commit()
    
def main():
    print("Introduction:\nWelcome to our Lost & Found program, where mu members can report found items or search for missing belongings making it easy to reunite lost treasures\nwith their rightful owners!")
    print("\nHow to use:\nReport lost item(s)  ---- Enter 1")
    print("View and search lost item(s) ---- Enter 2")
    print("Delete item(s)' record  ---- Enter 3")
    print("Exit ---- Enter 4")
    while True:
        print("\nChoices:")
        print("1. Add found item(s)")
        print("2. Find lost item(s)")
        print("3. Delete found item(s)")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1' or choice.lower() == 'one':
            print("Please finish the following questions about the found item(s)")
            found_date = input("Enter the date of found item(s) (DD/MM/YY): ")
            print("Please use this pattern when you answering the location(JCC, E0313)")
            found_location = input("Enter the location(Main Campus or JCC or IOH, Room) of found item(s): ")
            item_type = input("Enter the found item (apple pencil, calculator, other): ")
            print('If you want to skip question you can enter nothing.')
            found_other = input("Enter other special features of found item(s)(colour, size, total number): ")
            found_contact = input("Enter the phone number/school email: ")
            add_lostfind(found_date, found_location, item_type, found_other, found_contact)
            print("Thank you for your submission!")
            print("Item(s) has/have been added!")
            print("You can check your item(s)' information in choice 2")
            
        elif choice == '2' or choice.lower() == 'two':
            print("Items in database:")
            view_lostfinds()
            print("\nPlease enter '0' when you do not find out your item(s).")
            while True:
                lostfind_id = input("Enter the item(s) ID: ")
                try:
                    ID = int(lostfind_id)
                    break
                except ValueError:
                    print("Please enter an integer for answer")
            view_lostfind_by_id(lostfind_id)
            print("Please back to this program for deleting the item(s)' record after you get back your lost property")
        elif choice == '3' or choice.lower() == 'three':
            lostfind_id = int(input("Enter item(s) ID:"))
            delete_lostfind(lostfind_id)
            print('Item(s) have been deleted!')

        elif choice == '4'or choice.lower() == 'four':
            break

        else:
            print("Invalid choice, please try again.")
if __name__ == '__main__':
    main()

conn.close()

