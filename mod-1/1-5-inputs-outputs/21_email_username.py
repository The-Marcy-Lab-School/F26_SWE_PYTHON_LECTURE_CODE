# Run this file and type Reuben@MarcyLabSchool.org. Then run it again with an address that has no @.

email = input("What's your email? ").strip().lower()

if "@" in email:
    username = email[:email.find("@")]
    print(f"Welcome, {username}!")
else:
    print(f"Sorry, {email} is not an email address.")
