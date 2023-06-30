def get_profile(profile_model):
    try:
        return profile_model.objects.get()
    except profile_model.DoesNotExist as ex:
        return None