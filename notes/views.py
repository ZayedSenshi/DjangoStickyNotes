from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    View to display a list of all notes.
    :param request: HTTP request object.
    :return: Rendered template with a list of notes.
    """
    notes = Note.objects.all()
    # Creating a context dictionary to pass data
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    View to display details of a single note.
    :param request: HTTP request object.
    :param pk: Primary key of the note to display.
    :return: Rendered template with the note's details.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    View to create a new note.
    :param request: HTTP request object.
    :return: Rendered template with a form to create a new note.
    """
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    View to update an existing note.
    :param request: HTTP request object.
    :param pk: Primary key of the note to update.
    :return: Rendered template with a form to update the note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect(
                "note_list"
            )  # Redirect to the list view after successful update
    else:
        form = NoteForm(
            instance=note
        )  # Pre-populate the form with the current note's data

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    View to delete a note.
    :param request: HTTP request object.
    :param pk: Primary key of the note to delete.
    :return: Redirect to the list view after deletion.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note_list")  # Redirect to the list view after deletion


def index(request):
    return render(request, "base.html")
