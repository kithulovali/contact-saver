import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # I hope your name is root
    password="",  # Change this to your MySQL password
    database="contact_db"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20
    phone VARCHAR(15),
    email VARCHAR(50
)
""")
conn.commit()

# Function to add contact
def add_contact(name, phone, email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)

# Function to search contact by name
def search_contact(name):
    cursor.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    contact = cursor.fetchone()
    if contact:
        print(contact)
    else:
        print("Contact not found!")

# Function to delete contact
def delete_contact(name):
    cursor.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    print("Contact deleted successfully!")

# Menu-driven program
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)
    
    elif choice == '2':
        view_contacts()
    
    elif choice == '3':
        name = input("Enter Name to Search: ")
        search_contact(name)
    
    elif choice == '5':
        name = input("Enter Name to Delete: ")
        delete_contact(name)
    
    elif choice == '6':
        break
    
    else:
        print("Invalid Choice! Try again.")

# Close connection
cursor.close()
conn.close()











