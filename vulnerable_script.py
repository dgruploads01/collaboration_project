  import hashlib

def create_user_password(username, password):
    # This is a bad security practice as MD5 is weak.
    # A code scanner should flag this.
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    print(f"User {username} created with password hash: {hashed_password}")
    return hashed_password

def check_password(username, password_to_check):
    # Another bad practice with a hardcoded password.
    if password_to_check == "admin_password":
        print("Warning: Hardcoded password used!")
        return True
    return False

if __name__ == "__main__":
    create_user_password("test_user", "my_secret_password")
    check_password("admin", "admin_password")
