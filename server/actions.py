from server.models import UserProfile

def do_get_create_user(user_id: str, access_token: str, name:str, picture_url:str) -> UserProfile:
    user = UserProfile.objects.filter(user_id=user_id).first()
    if user is not None:
        user.access_token = access_token
        user.full_name = name
        print(user.update_profile_picture_from_url(picture_url))
        user.save()
        return user

    user = UserProfile(
        user_id=user_id,
        full_name=name,
        access_token=access_token,
        is_active=True
    )
    user.update_profile_picture_from_url(picture_url)
    user.save()
    return user
