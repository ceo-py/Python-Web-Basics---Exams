from apps.functionality.items import find_item
from apps.functionality.view_form import view_form
from apps.notes.forms import NotesModelBaseForm, NotesDeleteForm
from apps.notes.models import NotesModel


# Create your views here.

def notes_add(request):

    return view_form(
        request=request,
        base_form=NotesModelBaseForm,
        redirect_url='index',
        base_url='notes/note-create.html',
        addition_data={
            'add_note': True
        }
    )


def notes_edit(request, pk):
    note = find_item(NotesModel, pk)
    return view_form(
        request=request,
        item_instance=note,
        base_form=NotesModelBaseForm,
        redirect_url='index',
        base_url='notes/note-edit.html',
        addition_data={
            'note': note
        }
    )


def notes_delete(request, pk):
    note = find_item(NotesModel, pk)
    return view_form(
        request=request,
        item_instance=note,
        base_form=NotesDeleteForm,
        redirect_url='index',
        base_url='notes/note-delete.html',
        delete_form=True,
        addition_data={
            'note': note
        }
    )


def notes_details(request, pk):
    note = find_item(NotesModel, pk)
    return view_form(
        request=request,
        item_instance=note,
        base_form=NotesModelBaseForm,
        redirect_url='index',
        base_url='notes/note-details.html',
        addition_data={
            'note': note
        }
    )
