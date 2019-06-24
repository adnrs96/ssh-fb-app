from server.models import UserProfile

def do_get_create_user(user_id: str, access_token: str) -> UserProfile:
    user = UserProfile.objects.filter(user_id=user_id).first()
    if user is not None:
        return user

    user = UserProfile(user_id=user_id, access_token=access_token, is_active=True)
    user.save()
    return user
