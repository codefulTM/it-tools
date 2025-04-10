from data_service.models import UserRole

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
    
def get_user_role_by_name(user_role_name):
    try:
        user_role = UserRole.objects.get(role=user_role_name)
        return user_role
    except UserRole.DoesNotExist:
        if(user_role_name != 'admin' and user_role_name != 'regular' and user_role_name != 'premium'):
            return None
        else:
            return create_user_role(user_role_name)

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