from django.db import models
from django.urls import reverse


class Note(models.Model):
    """
    Model representing sticky notes

    Fields:
    - title: CharField for the note title with a maximum length
    of 200 characters.
    - content: TextField for the note content
    - created_at: DateTimeField set to the current date and time
    when the note is created.

    Methods:
        __str__(): Returns the string representation of the note,
        which is the note's title.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """
        Returns the absolute URL for the individual note instance.

        This method constructs a URL to the detail view of the current note instance
        using Django's URL dispatcher. It utilizes the 'note_detail' URL pattern
        to generate the URL, appending the primary key (ID) of the note as an argument
        to uniquely identify the note in the URL.

        The resulting URL is suitable for linking directly to the detail page of the
        note in web templates or redirects after creating or updating a note.

        :returns: A string representing the absolute URL to the detail view of the
                  current note instance.
        :rtype: str
        """
        return reverse('note_detail', args=[str(self.id)])

    def __str__(self):
        """
        Returns the string representation of the note.

        :return: The note's title.
        """
        return self.title
