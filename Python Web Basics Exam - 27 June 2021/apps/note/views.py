from django.shortcuts import render

from apps.functionality.items import find_item
from apps.functionality.view_model import view_form
from apps.note.forms import NoteModelBaseForm, NoteDeleteForm
from apps.note.models import NoteModel


# Create your views here.

def note_create(request):
    return view_form(
        request=request,
        base_form=NoteModelBaseForm,
        redirect_url='index',
        base_url='note/note-create.html',
    )


def note_details(request, pk):
    note = find_item(NoteModel, pk)
    return render(request, 'note/note-details.html', {'note': note})


def note_edit(request, pk):
    note = find_item(NoteModel, pk)
    return view_form(
        request=request,
        base_form=NoteModelBaseForm,
        item_instance=note,
        redirect_url='index',
        base_url='note/note-edit.html',
        addition_data={'note': note}
    )


def note_delete(request, pk):
    note = find_item(NoteModel, pk)
    return view_form(
        request=request,
        base_form=NoteDeleteForm,
        item_instance=note,
        redirect_url='index',
        base_url='note/note-delete.html',
        addition_data={'note': note},
        delete_form=True
    )
