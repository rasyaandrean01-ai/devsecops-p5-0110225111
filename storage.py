from config import MAX_NOTES

class NoteStorage:
    """Penyimpanan catatan sederhana selama aplikasi berjalan"""

    def __init__(self):
        self.notes = []
        self._next_id = 1

    def get_all(self):
        return list(self.notes)

    def add(self, content):
        if len(self.notes) >= MAX_NOTES:
            raise ValueError("Penyimpanan catatan sudah penuh.")

        note = {
            "id": self._next_id,
            "content": content,
        }

        self.notes.append(note)
        self._next_id += 1
        return note

    def delete(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                return True

            
        return False