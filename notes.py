from storage import NoteStorage
from validators import validate_note

class NoteService:
    """Mengatur proses pengelolaaan catatan."""

    def __init__(self, storage=None):
        self.storage = storage if storage is not None else NoteStorage()

    def list_notes(self):
        return self.storage.get_all()

    def create_note(self, content):
        is_valid, result = validate_note(content)


        if not is_valid:
            raise ValueError(result)

        return self.storage.add(result)

    def delete_note(self, note_id):
        if not isinstance(note_id, int) or isinstance(note_id, bool):
            return False

        return self.storage.delete(note_id)