### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True 
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    sample1 = Email("sample1@gmail.com", "Test1", "Testing")
    sample2 = Email("sample2@gmail.com", "Test2", "Testing, testing")
    sample3 = Email("sample3@gmail.com", "Test3", "Testing, testing, testing")
    
    inbox.append(sample1)
    inbox.append(sample2)
    inbox.append(sample3)
   
def list_emails():
    # Create a function which prints the emails subject_line, along with a corresponding number.
    for count, email in enumerate(inbox):
        print(f"*email {count + 1}* subject: {email.subject_line}")

def read_email(index):
    # Create a function which displays a selected email.
    print(f'\n from:\t\t{inbox[index-1].email_address}')
    print(f'\n subject:\t{inbox[index-1].subject_line}')
    print(f'\n message:\t{inbox[index-1].email_content}')
    print(f'\n\n *** Email from {inbox[index-1].email_address} marked as read ***')
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    inbox[index-1].mark_as_read()
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')

    if user_choice == "1":
        list_emails()
        # add logic here to read an email
        read_email(int(input(f"\nselect an email to read (from 1 to {len(inbox)}): ")))

    elif user_choice == "2":
        # add logic here to view unread emails
        unread_msgs = []
        for email in inbox:
            if email.has_been_read == False:
                print(f"from:\t\t{email.email_address}")
                print(f"subject:\t{email.subject_line}")
                print(f"message:\t{email.email_content}\n")
                unread_msgs.append(email)
        
        if len(unread_msgs) == 0:
             print("\nYou have no unread messages.")             
                 
    elif user_choice == "3":
        # add logic here to quit appplication
        print("\nGoodbye!\n")
        exit()

    elif user_choice.isdigit() == False:
        print("Oops - incorrect input.")

    else:
        print("Oops - incorrect input.")


