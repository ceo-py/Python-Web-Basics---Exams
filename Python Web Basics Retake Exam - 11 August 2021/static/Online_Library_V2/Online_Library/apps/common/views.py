from apps.books.models import BookModel
from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.functionality.view_form import view_form
from apps.user_profile.forms import ProfileModelBaseForm
from apps.user_profile.models import ProfileModel


# Create your views here.
def index(request):
    profile = get_profile(ProfileModel)

    if profile:

        return view_form(
            request=request,
            base_form=ProfileModelBaseForm,
            redirect_url='index',
            base_url='common/home-with-profile.html',
            addition_data={
                'profile': profile,
                'books': get_all_items(BookModel)
            }
        )

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/home-no-profile.html',
    )
