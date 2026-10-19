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

class PremiumUser(User): # inherits from User class
    pass

class FreeUser(User):
    def add_post(self, post: str):
        if len(self.posts) < 2: # .posts is an instance variable that stores the posts for this specific user
            super().add_post(post) # super() calls the add_post method from the parent User class
        else:
            print(f"{self.name} has reached the 2 post limit. Upgrade to premium for unlimted posts!")

# user1 = User("Albert Garcia", "albert.garcia@example.com", 123456789)
# user2 = User("Maria Lopez", "maria.lopez@example.com", 987654321)
# user3 = User("John Smith", "john.smith@example.com", 555555555)

# print(user1.name)  # Output: Albert Garcia
# print(user2.email)  # Output: maria.lopez@example.com
# print(user3.drivers_license)  # Output: 555555555

# user1.add_post("Hello, this is my first post!")
# user2.add_post("Excited to join this platform!")

# print(user1.posts)  # Output: ['Hello, this is my first post!']
# print(user2.posts)  # Output: ['Excited to join this platform!']
# print(User.all_posts)  # Output: ['Hello, this is my first post', 'Excited to join this platform!']


# user1.delete_post("Hello, this is my first post!")

# print(user1.posts)  # Output: []
# print(User.all_posts)  # Output: ['Excited to join this platform!']