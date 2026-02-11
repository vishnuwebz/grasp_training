# lesson_09

class User:
    # The __init__ constructor
    def __init__(self, user_id, username):
        # we are setting up the attributes for the new object.
        # self.attribute_name = value_passed_in
        print(f"Creating a new user: {username}")
        self.id = user_id
        self.username = username
        self.is_following = 0 # A default attribute
        self.followers = 0 # A default attribute

    # this is a method
    def follow(self, user_to_follow):
        """Makes this user instance follow another user instance"""
        user_to_follow.followers += 1 # increment the other user's followers
        self.is_following += 1 # increment this user's following count

# Now, we can create objects (instances) by passing arguments to the class name
user_one = User("001", "alice")
user_two = User("002", "bob")


# The attributes are already set up correctly!
print(f"{user_one.username} has {user_one.followers} followers.")
print(f"{user_two.username} has {user_two.followers} followers.")


# now, let's use the method
user_one.follow(user_two)

print(f"--- After user_one follows user_two ---")
print(f"{user_one.username}'s stats: Followers: {user_one.followers}, Following: {user_one.is_following}")
print(f"{user_two.username}'s stats: Followers: {user_two.followers}, Following: {user_two.is_following}")

# print(user_one)
# print(user_two)

# manually assigning attributes

# user_one.username = "alice"
# user_one.id = "001"
#
# user_two.username = "bob"
# user_two.id = "002"
#
# print(f"User one's username is: {user_one.username}")
# print(f"User two's username is: {user_two.username}")