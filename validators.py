from config import MAX_NOTE_LENGTH

def validate_note(content):
    """Memastikan isi catatan valid"""
    if not isinstance(content, str):
        return False, "Isi catatan harus berupa teks."

    content = content.strip()

    if not content:
        return False, "Catatan tidak boleh kosong."

    if len(content) > MAX_NOTE_LENGTH:
        return False, f"Catatan maksimal {MAX_NOTE_LENGTH} karakter."

    return True, content