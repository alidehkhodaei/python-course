class User:
    active_user_count = 0 # Class attribute (Similar to static in java)
    allowed_users=["Ali","Hasan","Ahmad"] # Class attribute

    def __init__(self, username, name_family):
        self.username = username
        self.name_family = name_family
        print(f"{self.username} logged in")
        User.active_user_count+=1

    def logout(self):
        print(f"{self.username} has logged out")
        User.active_user_count-=1

#---------------------

print(User.active_user_count) # 0

sara=User("Sara","Ahmadi")

ali=User("Ali","Movahed")

print(User.active_user_count) # 2

ali.logout()

print(User.active_user_count) # 1

#---------------------

print(User.allowed_users) # ['Ali', 'Hasan', 'Ahmad']

User.allowed_users.append("Reza")

print(User.allowed_users) # ['Ali', 'Hasan', 'Ahmad', 'Reza']

print(ali.allowed_users) # ['Ali', 'Hasan', 'Ahmad', 'Reza']

#---------------------

print(ali.allowed_users) # ['Ali', 'Hasan', 'Ahmad', 'Reza']

ali.allowed_users.append("Amir")

print(User.allowed_users) # ['Ali', 'Hasan', 'Ahmad', 'Reza', 'Amir']

print(ali.allowed_users) # ['Ali', 'Hasan', 'Ahmad', 'Reza', 'Amir']

#---------------------

print(User.allowed_users)  # ['Ali', 'Hasan', 'Ahmad', 'Reza', 'Amir']

User.allowed_users=["Jamshid"]

print(User.allowed_users) # ['Jamshid']

print(ali.allowed_users) # ['Jamshid']

#---------------------

print(User.allowed_users)  # ['Jamshid']

ali.allowed_users=["Test","Test2"]

print(User.allowed_users) #  ['Jamshid']

print(ali.allowed_users) # ['Test', 'Test2']
