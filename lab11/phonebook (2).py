import psycopg2
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="1234", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
    number BIGINT PRIMARY KEY,
    name VARCHAR(255),
    second_name VARCHAR(255)
);
""")

print("Type 'Insert' if you want to insert a new contact.")
print("Type 'Update' if you want to update a contact.")
print("Type 'Delete' if you want to delete a contact.")
print("Type 'Query' if you want to query a contact.")
mode = input()

if mode == "Insert":
    print("Choose insertion method: Console/CSV/List")
    inmode = input()
    if inmode == "Console":
        while True:
            number = input("Number: ")
            name = input("Name: ")
            second_name = input("Second Name: ")
            
            cur.execute("""INSERT INTO phonebook (number, name, second_name) VALUES (%s, %s, %s);""", (number, name, second_name))
            conn.commit()
            
            entries = input("Do you want to insert another contact? (yes/no): ")
            if entries.lower() != "yes":
                break
    elif inmode == "CSV":
        print("Enter the name of the file:")
        csvfile = input()
        with open(csvfile+'.csv', 'r') as f:
            cur.copy_from(f, 'phonebook', sep=',')
            conn.commit()
    elif inmode == "List":
        def insList(users):
            for user in users:
                name, second_name, number = user
                cur.execute("INSERT INTO phonebook (name, second_name, number) VALUES (%s, %s, %s);", (name, second_name, number))
                conn.commit()
        MyList = []
        print("Enter user data (name, second_name, number) separated by commas. Type 'done' when finished.")
        while True:
            user_data = input("User data: ")
            if user_data.lower() == "done":
                break
            MyList.append(tuple(user_data.split(',')))

        insList(MyList)
    else: 
        print("Invalid!")

if mode == "Update":
    print("Choose 'number', 'name', or 'second_name' to update:")
    upmode = input()
    if upmode == "number":
        old_number = input("Old Number: ")
        new_number = input("New Number: ")
        cur.execute("""UPDATE phonebook
                       SET number = %s
                       WHERE number = %s;""", (new_number, old_number))
        conn.commit()
    elif upmode == "name":
        old_name = input("Old Name: ")
        new_name = input("New Name: ")
        cur.execute("""UPDATE phonebook
                       SET name = %s
                       WHERE name = %s;""", (new_name, old_name))
        conn.commit()
    elif upmode == "second_name":
        old_second_name = input("Old Second Name: ")
        new_second_name = input("New Second Name: ")
        cur.execute("""UPDATE phonebook
                       SET second_name = %s
                       WHERE second_name = %s;""", (new_second_name, old_second_name))
        conn.commit()
    else:
        print("Invalid!")
        conn.commit()

if mode == "Delete":
    print("Choose name/number to delete:")
    modedel = input()
    if modedel == "name":
        to_delete = input()
        cur.execute("""DELETE FROM phonebook
                    WHERE name = %s;""", (to_delete,))
        conn.commit()
    elif modedel == "number":
        to_delete = input()
        cur.execute("""DELETE FROM phonebook
                    WHERE number = %s;""", (to_delete,))
        conn.commit()
    else:
        print("Invalid!")

if mode == "Query":
    print("Choose filter: data/pagination/part?")
    modeque = input("")
    if modeque == "data":
        print("Choose to quering name/second_name/number?")
        option = input()
        if option == "name":
            name = input("Enter name: ")
            cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        elif option == "second_name":
            second_name = input("Enter second name: ")
            cur.execute("SELECT * FROM phonebook WHERE second_name = %s", (second_name,))
        elif option == "number":
            number = input("Enter number: ")
            cur.execute("SELECT * FROM phonebook WHERE number = %s", (number,))
    elif modeque == "pagination":
        print("Page size: ")
        page_size = input()
        print("Offset: ")
        offset = input()
        cur.execute(f"SELECT * FROM phonebook LIMIT {page_size} OFFSET {offset};")
    elif modeque == "part":
        print("part of name/second_name/number:")
        modik = input()
        if modik == "name":
            print("part of name:")
            substr = input()
            cur.execute("SELECT * FROM phonebook WHERE name LIKE %s", ('%' + substr + '%',))
        elif modik == "second_name":
            print("part of second name:")
            substr = input()
            cur.execute("SELECT * FROM phonebook WHERE second_name LIKE %s", ('%' + substr + '%',))
        elif modik == "number":
            print("part of number:")
            substr = input()
            cur.execute("SELECT * FROM phonebook WHERE number::text LIKE %s", ('%' + substr + '%',))
    else:
        print("Invalid option")

    rows = cur.fetchall()
    if not rows:
        print("No matching contacts found")
    else:
        print("Matching contacts:")
        for row in rows:
            print(row)
    conn.commit()


cur.close()
conn.close()