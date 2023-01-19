class user:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New User being Created. ")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user1 = user("1206", "muhammad")
user2 = user("1207", "awan")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)


