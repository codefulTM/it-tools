from data_service.models import User, UserRole
import bcrypt

# Get all function
def get_all_users():
    users = User.objects.all()
    return users

# Get user by id function
def get_user_by_id(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None
    
# Create user
def create_user(username, email, password, role):
    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return None
    # Check if the email already exists
    if User.objects.filter(email=email).exists():
        return None
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    # Create the user
    user = User(username=username, email=email, password_hash=hashed_password, role=role)
    user.save()
    return user

# Update the user's password
def update_user_password(user_id, password):
    try:
        user = User.objects.get(id=user_id)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user.password_hash = hashed_password.decode('utf-8')
        user.save() 
        return user
    except User.DoesNotExist:
        return None
    
# Update the user's role
def update_user_role(user_id, role):
    try:
        user = User.objects.get(id=user_id)
        user.role = role
        user.save()
        return user
    except User.DoesNotExist:
        return None