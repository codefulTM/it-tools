from ..models import UserRole

# Get all function
def get_all_user_roles():
    users = UserRole.objects.all()
    return users

# Get user by id function
def get_user_role_by_id(user_role_id):
    try:
        user = UserRole.objects.get(id=user_role_id)
        return user
    except UserRole.DoesNotExist:
        return None
    
# Create user role
def create_user_role(user_role):
    # If the user role has existed
    if UserRole.objects.filter(role=user_role).exists():
        return None
    user_role = UserRole(role=user_role)
    user_role.save()
    return user_role

# Update user role
def update_role(user_role_id, user_role):
    user_role = get_user_role_by_id(user_role_id)
    if user_role is None:
        return None
    user_role.role = user_role
    user_role.save()
    return user_role