from apps.functionality.deco_profile import check_profile_exists


# Create your views here.
@check_profile_exists
def index(request):
    pass
