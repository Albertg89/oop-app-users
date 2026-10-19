from User import FreeUser, PremiumUser

free_user = FreeUser("Jane Doe", "jane.doe@example.com", 111111111)
premium_user = PremiumUser("Albert Garcia", "albert.garcia@example.com", 123456789)

free_user.add_post("Test 1")
free_user.add_post("Test 2")
free_user.add_post("Test 3")

premium_user.add_post("Premium Test 1")
premium_user.add_post("Premium Test 2")
premium_user.add_post("Premium Test 3")

print(free_user.posts)  # Output: ['Test 1', 'Test 2']
print(premium_user.posts)  # Output: ['Premium Test 1', 'Premium Test 2', 'Premium Test 3']