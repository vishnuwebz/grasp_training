class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.is_following = 0
        self.followers = 0

    def follow(self, user_to_follow):
        user_to_follow.followers += 1
        self.is_following += 1

# child class inheriting from user
class PremiumUser(User):
    def __init__(self, user_id, username, subscription_tier):
        super().__init__(user_id, username)
        self.subscription_tier = subscription_tier


    def view_exclusive_content(self):
        print(f"{self.username} is viewing exclusive content as a {self.subscription_tier} member")

# testing the classes
standard_user = User("001", "alice")
premium_user = PremiumUser("002", "bob", "Gold")

# PremiumUser can still use methods from User
premium_user.follow(standard_user)

print(f"{premium_user.username} is following {premium_user.is_following} people")

print(f"{standard_user.username} has {standard_user.followers} followers")

# and PremiumUser can use its own methods
premium_user.view_exclusive_content()


print("\n")

