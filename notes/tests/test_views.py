from django.test import TestCase
from django.urls import reverse
from ..models import Note
from ..forms import NoteForm


class NoteListViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        """
        Tests the 'note_list' view, ensuring it lists all notes and displays them correctly.

        This test simulates a GET request to the 'note_list' view and verifies that the response indicates a
        successful operation (HTTP 200 OK status code), and that the response contains the text 'Test Note',
        indicating that at least one note is listed.

        Steps:
            1. Sends a GET request to the 'note_list' view.
            2. Verifies that the response status code is 200, indicating that the view was accessed successfully.
            3. Checks that the response contains the text 'Test Note', ensuring that at least one note is listed.

        Expected Outcome: - The response status code is 200, indicating a successful retrieval of the 'note_list'
        view. - The response body includes the text 'Test Note', confirming that the listing of notes is functioning
        correctly.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')


class NoteDetailViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_detail_view(self):
        """
        Tests the functionality of the 'note_detail' view for retrieving and displaying a note's details.

        This test retrieves a specific note identified by its ID (in this case, ID 1) and makes a GET request to the
        'note_detail' view, passing the note's primary key (PK) as an argument. It then verifies that the response
        indicates a successful operation (HTTP 200 OK status code), and checks that the response body contains the
        expected title and content of the note.

        Steps:
        1. Retrieves a note with ID 1 from the database.
        2. Sends a GET request to the 'note_detail' view with
        the note's PK as an argument.
        3. Verifies that the response status code is 200, indicating that the note's
        details were successfully retrieved.
        4. Checks that the response contains the expected title and content of
        the note.

        Expected Outcome: - The response status code is 200, indicating a successful retrieval and display of the
        note's details. - The response body includes the expected title ('Test Note') and content ('This is a test
        note.'), confirming accurate data presentation.
        """
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail',
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')


class NoteCreateViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_get_note_create_view(self):
        """
        Tests the retrieval of the 'note_create' view, ensuring it displays the note creation form correctly.

        This test simulates a GET request to the 'note_create' view and verifies that the response indicates a
        successful operation (HTTP 200 OK status code), and that the response contains an instance of the expected
        form class, `NoteForm`.

        Steps:
        1. Sends a GET request to the 'note_create' view.
        2. Verifies that the response status code is 200,
        indicating that the view was accessed successfully.
        3. Checks that the response context includes an instance of `NoteForm`,
           ensuring that the form for creating a note is displayed.

        Expected Outcome: - The response status code is 200, indicating a successful retrieval of the 'note_create'
        view. - The response context contains an instance of `NoteForm`, confirming that the form for creating a note
        is properly rendered.
        """
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], NoteForm)

    def test_post_note_create_view_with_valid_data(self):
        """
        Tests the successful creation of a note through the 'note_create' view with valid data.

        This test simulates a POST request to the 'note_create' view with valid data for creating a new note,
        specifically a title and content. It then verifies that a new note was successfully created and saved in the
        database, the response indicates a successful operation (HTTP 302 redirect), and the newly created note
        exists in the database.

        Steps:
        1. Records the initial count of notes in the database.
        2. Sends a POST request to the 'note_create'
        view with a dictionary containing valid data for creating a note, such as a title and content.
        3. Verifies the count of notes in the database has increased by one, confirming that a new note was created.
        4. Checks that the response status code is 302, indicating that the creation was successful and the system
        redirected. 5. Confirms that the newly created note exists in the database with the provided title.

        Expected Outcome:
            - The count of notes in the database increases by one, indicating a new note was successfully created.
            - The response status code is 302, indicating a successful creation and subsequent redirection.
            - The newly created note with the specified title exists in the database.
        """
        note_count_before = Note.objects.count()
        # takes the URL pattern as argument, returns corresponding URL
        # pattern name and data
        response = self.client.post(reverse('note_create'), {
            'title': 'Valid Title',
            'content': 'Valid Content'
        })
        self.assertEqual(Note.objects.count(), note_count_before + 1)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(Note.objects.filter(title='Valid Title').exists())

    def test_post_note_create_view_with_invalid_data(self):
        """
        Tests the 'note_create' view's handling of invalid data during note creation.

        This test simulates a POST request to the 'note_create' view with intentionally invalid data, specifically
        empty titles and contents for a new note. It then verifies that the response indicates the form was not
        processed successfully (HTTP 200 OK status code), and ensures that no new note was saved in the database due
        to the invalid data.

        Steps: 1. Sends a POST request to the 'note_create' view with a dictionary containing invalid data for
        creating a note, such as empty title and content fields.
        2. Verifies that the response status code is 200, indicating that the form submission was unsuccessful.
        3. Ensures that the count of notes in the database remains unchanged, confirming that no new note was created.

        Expected Outcome: - The response status code is 200, indicating that the attempt to create a note with
        invalid data was not successful. - No new note is added to the database, demonstrating that the invalid data
        prevented the creation of a new note.
        """
        response = self.client.post(reverse('note_create'), {
            'title': '',
            'content': ''
        })
        # status code 200 indicates a successful request but without redirection
        # Verifies that the view didn't attempt to redirect the user after
        # receiving invalid data, meaning form was not submitted successfully
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)  # Ensure no note was saved


class NoteUpdateViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title='Original Title', content='Original Content.')
        self.pk = self.note.pk

    def test_note_update_success(self):
        """
        Tests the successful update of a note through the 'note_update' view with valid data.

        This test prepares and submits a POST request to the 'note_update' view with valid data for updating a note,
        specifically a new title and content. It then verifies that the response indicates a successful operation (
        HTTP 302 redirect), and finally, it asserts that the note has been updated in the database accordingly.

        Steps:
        1. Prepares a dictionary containing valid data for updating a note, such as a new title and content.
        2. Sends a POST request to the 'note_update' view with the prepared valid data and a valid primary key (PK).
        3. Verifies that the response status code is 302, indicating that the update was successful and the system
        redirected.
        4. Fetches the updated note from the database using its PK to confirm that the title and content
        have been changed.

        Expected Outcome:
            - The response status code is 302, indicating a successful update and subsequent redirection.
            - The note corresponding to the provided PK has been updated in the database with the new title and content.
        """
        # Prepare the updated data
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated Content.'
        }

        # Send a POST request to the note_update view with the updated data
        response = self.client.post(reverse('note_update', kwargs={'pk': self.pk}), updated_data)

        # Verify that the response status code is 302 (redirect), indicating success
        self.assertEqual(response.status_code, 302)

        # Fetch the updated note from the database
        updated_note = Note.objects.get(pk=self.pk)

        # Assert that the note's title and content have been updated
        self.assertEqual(updated_note.title, 'Updated Title')
        self.assertEqual(updated_note.content, 'Updated Content.')

    def test_note_update_failure(self):
        """
        Tests the failure of the 'note_update' view to update a note with invalid data.

        This test prepares and submits a POST request to the 'note_update' view with intentionally invalid data,
        specifically empty titles and contents for a note. It then verifies that the response indicates the form was
        not processed successfully (HTTP 200 OK status code), and finally, it asserts that the original note remains
        unchanged.

        Steps:
        1. Prepares a dictionary containing invalid data for updating a note, such as empty title and content
        fields.
        2. Sends a POST request to the 'note_update' view with the prepared invalid data and a valid primary
        key (PK).
        3. Verifies that the response status code is 200, indicating that the form submission was
        unsuccessful.
        4. Retrieves the original note from the database using its PK to confirm that it has not been
        modified.

        Expected Outcome: - The response status code is 200, indicating that the attempt to update the note with
        invalid data was not successful. - The original note's title and content remain unchanged, demonstrating that
        the invalid update did not affect the database record.
        """
        # Prepare invalid data
        invalid_data = {
            'title': '',
            'content': ''
        }

        # Send a POST request to the note_update view with the invalid data
        response = self.client.post(reverse('note_update', kwargs={'pk': self.pk}), invalid_data)

        # Verify that the response status code is 200 (OK), indicating the form was not submitted successfully
        self.assertEqual(response.status_code, 200)

        # Assert that the original note was not modified
        original_note = Note.objects.get(pk=self.pk)
        self.assertEqual(original_note.title, 'Original Title')
        self.assertEqual(original_note.content, 'Original Content.')


class NoteDeleteViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')
        self.pk = self.note.pk

    def test_note_delete_success(self):
        """
        Tests the successful deletion of a note through the 'note_delete' view.

        This test simulates a GET request to the 'note_delete' view with a valid primary key (PK) of a note.
        It then verifies that the response indicates a successful operation (HTTP 302 redirect) and confirms
        that the note has been removed from the database by attempting to retrieve it and expecting it to not exist.

        Steps:
            1. Sends a GET request to the 'note_delete' view with a valid PK.
            2. Checks that the response status code is 302, indicating a successful redirection after deletion.
            3. Tries to fetch the deleted note from the database using its PK.
            4. Confirms that the note cannot be retrieved, implying it has been successfully deleted.

        Expected Outcome:
            - Response status code is 302, indicating a successful deletion and subsequent redirection.
            - The note corresponding to the provided PK is not found in the database, confirming its deletion.
        """
        response = self.client.get(reverse('note_delete', kwargs={'pk': self.pk}))

        # Verify that the response status code is 302 (redirect), indicating success
        self.assertEqual(response.status_code, 302)

        # Attempt to fetch the deleted note from the database
        try:
            deleted_note = Note.objects.get(pk=self.pk)
        except Note.DoesNotExist:
            deleted_note = None

        # Assert that the note was deleted
        self.assertIsNone(deleted_note)

    def test_note_delete_failure(self):
        """
        Tests that attempting to delete a non-existent note results in a 404 Not Found error.

        This test simulates a GET request to the 'note_delete' view with a non-existent primary key (PK=999).
        It expects the server to return a 404 status code, indicating that the requested note could not be found.

        Methods:
            get: Simulates a GET request to the 'note_delete' view with the specified PK.
            reverse: Generates the URL for the 'note_delete' view based on the provided arguments.
            assertEqual: Asserts that the response status code is 404, indicating a successful 404 Not Found error.
        """
        response = self.client.get(reverse('note_delete', kwargs={'pk': 999}))

        self.assertEqual(response.status_code, 404)
