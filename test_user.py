from User import User, FreeUser, PremiumUser

def test_user_has_attributes():
    user = User("John Doe", "john.doe@example.com", 123456789)
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"
    assert user.drivers_license == 123456789

def test_free_user_can_only_make_two_posts():
    user = FreeUser("John Doe", "john.doe@example.com", 123456789)
    user.add_post("Post 1")
    user.add_post("Post 2")
    user.add_post("Post 3")  # This should not be added
    assert user.posts == ["Post 1", "Post 2"]

def test_premium_user_can_make_unlimited_posts():
    user = PremiumUser("Albert Garcia", "albert.garcia@example.com", 987654321)
    user.add_post("Unlimited Post 1")
    user.add_post("Unlimited Post 2")
    user.add_post("Unlimited Post 3")
    assert user.posts == ["Unlimited Post 1", "Unlimited Post 2", "Unlimited Post 3"]

def test_add_post_updates_all_posts():
    User.all_posts.clear()  # Clear the class variable before testing
    user = PremiumUser("Albert Garcia", "albert.garcia@example.com", 987654321)
    user.add_post("Hello World!")
    assert User.all_posts == ["Hello World!"]

def test_delete_post_removes_from_both_lists():
    User.all_posts.clear()
    user = PremiumUser("Albert Garcia", "albert.garcia@example.com", 987654321)
    user.add_post("Hello World!")
    user.delete_post("Hello World!")
    assert User.all_posts == []
    assert user.posts == []