users = [
    {"id": 1, "name": "Nirav", "is_active": True, "role": "admin"},
    {"id": 2, "name": "Amit", "is_active": False, "role": "customer"},
    {"id": 3, "name": "Rahul", "is_active": True, "role": "customer"},
    {"id": 4, "name": "Neha", "is_active": True, "role": "admin"},
    {"id": 5, "name": "Jay", "is_active": False, "role": "customer"}
]

# Display only active user
print("------------ Display only active user -----------------")

for user in users:
    if user['is_active']:
        print(f"user {user['name']} {user['is_active']}")
        print()
        print()
        
# Count the Number of Active User
print("------------ Count the Number of Active User -----------------")
user_active = 0
for user in users:
    if user['is_active']:
        user_active += 1
print(f"the {user_active} are activate")
print()
print()

# display all admin users
print("------------display all admin users -----------------")
for user in users:
    if user['role'] == "admin":
        print(f"{user}")
        print()
        print()
# create a new list only containing active users
print("------------ create a new list only containing active users -----------------")
active_users = []
for user in users:
    if user['is_active']:
        active_users.append(user)
print(f"Active User lists is{active_users}")
print()
print()