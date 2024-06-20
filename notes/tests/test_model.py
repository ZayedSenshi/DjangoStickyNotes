from django.test import TestCase
from notes.models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        """
        Tests that a Note object has the expected title.

        This test retrieves a specific Note object from the database and compares its 'title' attribute with the
        expected string. It verifies that the 'title' attribute of the Note object matches the expected value,
        ensuring that the note has the correct title.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Compares the 'title' attribute of the Note object with the expected string, 'Test Note'.

        Expected Outcome: - The 'title' attribute of the Note object matches the expected string, confirming that the
        note has the correct title.
        """
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        """
        Tests that a Note object has the expected content.

        This test retrieves a specific Note object from the database and compares its 'content' attribute with the
        expected string. It verifies that the 'content' attribute of the Note object matches the expected value,
        ensuring that the note contains the correct content.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Compares the 'content' attribute of the Note object with the expected string, 'This is a test note.'

        Expected Outcome: - The 'content' attribute of the Note object matches the expected string, confirming that
        the note contains the correct content.
        """
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

    def test_first_name_max_length(self):
        """
        Tests the maximum length allowed for the 'title' field of a Note model instance.

        This test retrieves a specific Note object from the database and accesses its '_meta' attribute to find the
        maximum length allowed for the 'title' field. It then verifies that the maximum length matches the expected
        value, which is typically defined in the model's field definition.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Uses the _meta API to access the 'title' field of the Note object and retrieves its maximum length.
            3. Compares the retrieved maximum length with the expected value, which is 100 characters in this example.

        Expected Outcome: - The maximum length of the 'title' field is 100 characters, confirming that the field
        adheres to the defined constraints.
        """
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        """
        Tests the implementation of the `get_absolute_url` method for a Note model instance.

        This test retrieves a specific Note object from the database and calls its `get_absolute_url` method,
        which should return the absolute URL for the detail view of the note. It then verifies that the returned URL
        matches the expected format, which includes the relative path '/detail/' followed by the note's ID.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Calls the `get_absolute_url` method on the Note object to obtain the absolute URL for its detail view.
            3. Compares the returned URL with the expected format, which includes the note's ID.

        Expected Outcome: - The `get_absolute_url` method returns the correct absolute URL for the detail view of the
        note, matching the expected format.
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.get_absolute_url(), '/detail/1/')

    def test_title_label(self):
        """
        Tests the label associated with the 'title' field of a Note model instance.

        This test retrieves a specific Note object from the database and accesses its '_meta' attribute to find the
        verbose name of the 'title' field. It then verifies that the verbose name matches the expected string, 'title'.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Uses the _meta API to access the 'title' field of the Note object and retrieves its verbose name.
            3. Compares the retrieved verbose name with the expected value, 'title'.

        Expected Outcome:
            - The verbose name of the 'title' field is 'title', confirming that the field label is correctly set.
        """
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_content_label(self):
        """
        Tests the label associated with the 'content' field of a Note model instance.

        This test retrieves a specific Note object from the database and accesses its '_meta' attribute to find the
        verbose name of the 'content' field. It then verifies that the verbose name matches the expected string,
        'content'.

        Steps:
            1. Retrieves a Note object with ID 1 from the database.
            2. Uses the _meta API to access the 'content' field of the Note object and retrieves its verbose name.
            3. Compares the retrieved verbose name with the expected value, 'content'.

        Expected Outcome:
            - The verbose name of the 'content' field is 'content', confirming that the field label is correctly set.
        """
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')
