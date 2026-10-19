# your User class goes here

class User:

    all_posts = [] # class variable to store all posts by all users

    def __init__(self, name: str, email: str, drivers_license: int):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.posts = [] # this instance variable will store posts for this specific user

    def add_post(self, post: str):
        self.posts.append(post) # Add the post to the user's own posts list
        User.all_posts.append(post) # adds the same post to the shared class variable list of all posts

# BONUS: Delete post method
    def delete_post(self, post: str):
        self.posts.remove(post) # Remove the post from the user's own posts list
        User.all_posts.remove(post) # Remove the same post from the shared class variable list of all posts

user1 = User("Albert Garcia", "albert.garcia@example.com", 123456789)
user2 = User("Maria Lopez", "maria.lopez@example.com", 987654321)
user3 = User("John Smith", "john.smith@example.com", 555555555)

# print(user1.name)  # Output: Albert Garcia
# print(user2.email)  # Output: maria.lopez@example.com
# print(user3.drivers_license)  # Output: 555555555

user1.create_post("Hello, this is my first post!")
user2.create_post("Excited to join this platform!")

# print(user1.posts)  # Output: ['Hello, this is my first post!']
# print(user2.posts)  # Output: ['Excited to join this platform!']
# print(User.all_posts)  # Output: ['Hello, this is my first post', 'Excited to join this platform!']


user1.delete_post("Hello, this is my first post!")

print(user1.posts)  # Output: []
print(User.all_posts)  # Output: ['Excited to join this platform!']