def get_user_from_session(request):
    user_id = None
    username = None
    user_role = None
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        username = request.session.get('username')
        user_role = request.session.get('user_role')

    return user_id, username, user_role