from My_Music_App.album.models import Album
from My_Music_App.functionality.profile import get_profile
from My_Music_App.functionality.view_form import view_form
from My_Music_App.user_profile.forms import ProfileModelBaseForm
from My_Music_App.user_profile.models import ProfileModel
from My_Music_App.functionality.items import get_all_items


def index(request):
    profile = get_profile(ProfileModel)

    if profile:
        return view_form(
            request=request,
            base_form=ProfileModelBaseForm,
            redirect_url='index',
            base_url='common/home-with-profile.html',
            addition_data={
                'albums': get_all_items(Album)
            }
        )

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/home-no-profile.html',
        addition_data={
            'no_profile': True
        }
    )
