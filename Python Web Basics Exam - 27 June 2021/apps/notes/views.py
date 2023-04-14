from django.shortcuts import render

from apps.functionality.items import find_item
from apps.functionality.profile import get_profile
from apps.functionality.view_form import view_form
from apps.notes.forms import NoteModelBaseForm, NoteDeleteForm
from apps.notes.models import NoteModel
from apps.user.models import ProfileModel


# Create your views here.


def note_add(request):
    return view_form(
        request=request,
        base_form=NoteModelBaseForm,
        redirect_url='index',
        base_url='notes/note-create.html',
        addition_data={'add': 'False',
                       'profile': get_profile(ProfileModel)}
    )


def note_edit(request, pk):
    note = find_item(NoteModel, pk)

    return view_form(
        request=request,
        base_form=NoteModelBaseForm,
        item_instance=note,
        redirect_url='index',
        base_url='notes/note-edit.html',
        addition_data={'note': note,
                       'profile': get_profile(ProfileModel)}

    )


def note_delete(request, pk):
    note = find_item(NoteModel, pk)

    return view_form(
        request=request,
        base_form=NoteDeleteForm,
        item_instance=note,
        redirect_url='index',
        base_url='notes/note-delete.html',
        addition_data={'note': note,
                       'profile': get_profile(ProfileModel)},
        delete_form=True
    )


def note_details(request, pk):
    return render(request, 'notes/note-details.html', {'note': find_item(NoteModel, pk)})
