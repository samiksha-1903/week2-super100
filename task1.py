users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
def add_user(name, email):
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {"id": new_id, "name": name, "email": email}
    users.append(new_user)
    return new_user
def update_user(user_id, name=None, email=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        return user
    return None
def delete_user(user_id):
    global users
    user = get_user_by_id(user_id)
    if user:
        users = [u for u in users if u["id"] != user_id]
        return True
    return False
if __name__ == "__main__":
    print("All users:", users)

    print("\nAdding a new user
