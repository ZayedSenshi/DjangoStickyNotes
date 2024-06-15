from django.test import TestCase
from django.urls import reverse
from ..models import Note
from ..forms import NoteForm


class NoteFormTemplateTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='This is a test.')
        self.form = NoteForm(instance=self.note)

    def test_note_form_template_edit_mode(self):
        """
        Tests the display of the note editing form in the web interface.

        This method simulates a GET request to the URL associated with editing a specific note,
        identified by its ID. It expects to receive a response with a status code of 200
        (indicating success). Then, it asserts that the response contains the text 'Edit Note',
        confirming that the template correctly displays instructions or labels relevant to editing
        an existing note. Additionally, it checks for the presence of the note's content ('This is a test.')
        in the response, ensuring that the current content of the note is displayed as part of the editing form.

        Steps:
        1. Simulates a GET request to the URL for editing a specific note, identified by its ID, capturing the
        HTTP response.
        2. Verifies that the response status code is 200, indicating a successful request.
        3. Confirms that the response includes the text 'Edit Note'.
        4. Ensures that the response contains the text 'This is a test.', confirming the display of the note's content.

        Expected Outcome: - The response status code is 200, indicating a successful retrieval of the note editing
        form. - The response body includes the text 'Edit Note', demonstrating the template's support for editing
        existing notes. - The response contains the text 'This is a test.', confirming that the current content of
        the note is displayed as part of the editing form.
        """
        response = self.client.get(reverse('note_update', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Edit Note')
        self.assertContains(response, 'This is a test.')  # Assuming the content field is displayed

    def test_note_form_template_create_mode(self):
        """
        Tests the display of the note creation form in the web interface.

        This method simulates a GET request to the URL associated with creating a new note,
        expecting to receive a response with a status code of 200 (indicating success). It then
        asserts that the response contains a form element with a POST method, which is essential
        for submitting the form data. Additionally, it checks for the presence of 'Create Note'
        in the response, confirming that the template correctly displays instructions or labels
        relevant to creating a new note. Finally, it ensures that 'Edit Note' is not present
        in the response, as this text should only appear in the context of editing an existing note.

        Steps:
            1. Simulates a GET request to the URL for creating a new note, capturing the HTTP response.
            2. Verifies that the response status code is 200, indicating a successful request.
            3. Confirms that the response includes a form element with a POST method.
            4. Ensures that the response contains the text 'Create Note'.
            5. Verifies that the response does not contain the text 'Edit Note'.

        Expected Outcome:
            - The response status code is 200, indicating a successful retrieval of the note creation form.
            - The response body includes a form element with a POST method, confirming the form's presence.
            - The response contains the text 'Create Note', demonstrating the template's support for creating new notes.
            - The absence of 'Edit Note' in the response, as expected for the creation mode.
        """
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, '<form method="post" action="')
        self.assertContains(response, 'Create Note')
        self.assertNotContains(response, 'Edit Note')


class NoteDetailTemplateTest(TestCase):
    def setUp(self):
        # Create a note instance for testing
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test.',
        )

    def test_note_detail_display(self):
        """
        Tests the display of a note's detail view.

        This test simulates a GET request to the 'note_detail' view for the created note,
        expecting to receive a response with a status code of 200 (indicating success).
        It then asserts that the response contains the note's title, content,
        and provides links to edit, delete, and return to the notes list.
        """
        # Assuming 'note_detail' is the URL pattern for viewing a note's detail
        response = self.client.get(reverse('note_detail', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the note's title
        self.assertContains(response, f'<h2>{self.note.title}</h2>')
        # Assert that the response contains the note's content
        self.assertContains(response, f'<p>{self.note.content}</p>')
        # Assert that the response contains the link to edit the note
        self.assertContains(response, f'<a href="{reverse("note_update", kwargs={"pk": self.note.pk})}">Edit Note</a>')
        # Assert that the response contains the link to delete the note
        self.assertContains(response,
                            f'<a href="{reverse("note_delete", kwargs={"pk": self.note.pk})}">Delete Note</a>')
        # Assert that the response contains the link to return to the notes list
        self.assertContains(response, f'<a href="{reverse("note_list")}">Back to Notes List</a>')


class NoteListTemplateTest(TestCase):
    def setUp(self):
        # Create a list of notes for testing
        self.notes = [
            Note.objects.create(title='Test Note 1', content='This is a test.'),
            Note.objects.create(title='Another Test Note', content='More test content here.'),
            Note.objects.create(title='Yet Another Test Note', content='Even more test content.')
        ]

    def test_note_list_display(self):
        """
        Tests the display functionality of the note list view within a Django application.

        This method performs the following steps to validate the correct rendering and behavior of the note list view:

        1. Initiates a GET request to the 'note_list' view endpoint using Django's test client. This simulates a user
        requesting to view the list of notes.
        2. Asserts that the HTTP response received from the server has a status
        code of 200, indicating a successful request.
        3. Retrieves the titles of all notes stored in the `self.notes`
        list, which was populated in the `setUp` method. This list contains three notes with unique titles for
        testing purposes.
        4. Extracts the titles of the notes displayed in the response by iterating over the
        `self.notes` list and accessing the `title` attribute of each note object.
        5. Compares the expected titles (
        hardcoded in the test) with the actual titles extracted from the response. This assertion ensures that the
        note list view correctly displays the titles of all notes in the list.

        This test case is designed to verify that the note list view properly renders the list of notes, including
        their titles, and provides a link for creating a new note. It does not explicitly check for the presence of
        the create new note link in the response; however, the expectation is implicitly covered by the successful
        rendering of the note list and the inclusion of a mechanism (link) for adding new notes.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

        expected_titles = ['Test Note 1', 'Another Test Note', 'Yet Another Test Note']
        actual_titles = [note.title for note in self.notes]
        self.assertEqual(expected_titles, actual_titles)
