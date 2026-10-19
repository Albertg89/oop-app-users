# your User class goes here

class User:
    def __init__(self, name: str, email: str, drivers_license: int):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

user1 = User("Albert Garcia", "albert.garcia@example.com", 123456789)
user2 = User("Maria Lopez", "maria.lopez@example.com", 987654321)
user3 = User("John Smith", "john.smith@example.com", 555555555)

print(user1.name)  # Output: Albert Garcia
print(user2.email)  # Output: maria.lopez@example.com
print(user3.drivers_license)  # Output: 555555555