#Contact book
#I will create an agenda that saves information as personal contacts 

"""
Tasks: 
Create:
-Add new contacts 
-Each contact must have: Name, Telephone and Email

Read:
-List all contacts 
-Allow searching for a contact by name

Update: 
-Update the phone number or the email of a contact given his name

Delete: 
-Delete a contact using his name
""" 
#Considerations: 
#The name of the contact it must be unique in the agenda 
#When updating or deleting, this must first verify that the contact exists.

addressbook = {
"Carlos Pérez": {"phone": "3001234567", "email": "carlos@example.com"},
"Ana Torres": {"phone": "3119876543", "email": "ana@example.com"}
}

def add_contact(name, phone, email):
    if name in addressbook:
        print("❌ That contact already exists.")
        return
    addressbook[name] = {"phone": phone, "email": email}
    print("✅ Contact successfully added.")

def list_contacts():
    if not addressbook:
        print("📭 There are no contacts in the address book.")
        return
        print("📒 Registered contacts:")
        for name, info in addressbook.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact(name):
    results = {n: i for n, i in addressbook.items() if name.lower() in n.lower()}
    if results:
        print("🔍 Contacts found:")
        for n, i in results.items():
            print(f"Name: {n}, Phone: {i['phone']}, Email: {i['email']}")
    else:
        print("❌ No contact was found with that name.")

def update_contact(name, new_phone=None, new_email=None):
    if name not in addressbook:
        print("❌ The contact does not exist.")
        return
    if new_phone:
        addressbook[name]["phone"] = new_phone
    if new_email:
        addressbook[name]["email"] = new_email
        print("✅ Contact updated.")

def delete_contact(name):
    if name not in addressbook:
        print("❌ Contact does not exist.")
        return
    del addressbook[name]
    print("✅ Contact deleted.")

def menu():
    while True:
        print("\n📱 ADD TOUCH MENU 📱")
        print("1. Add contact")
        print("2. List all contacts")
        print("3. Search contact by name")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        option = input("Choose an option (1-6): ")

        if option == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)

        elif option == "2":
            list_contacts()

        elif option == "3":
            name = input("Name to search (partial or complete): ")
            search_contact(name)

        elif option == "4":
            name = input("Name of contact to update: ")
            new_phone = input("New phone (leave blank if unchanged): ") or None
            new_email = input("New email (leave blank if unchanged): ") or None
            update_contact(name, new_phone, new_email)

        elif option == "5":
            name = input("Name of contact to delete: ")
            delete_contact(name)

        elif option == "6":
            print("👋 Closing address book. See you soon!")
            break

        else:
            print("❌ Invalid option.")

menu()