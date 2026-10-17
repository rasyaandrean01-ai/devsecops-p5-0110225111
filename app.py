from flask import Flask, jsonify, request

from config import APP_NAME, APP_VERSION
from notes import NoteService

app = Flask(__name__)
notes = NoteService()

@app.get("/")
def home():
    return jsonify({
        "app": APP_NAME,
        "version": APP_VERSION,
        "message": "SecureNotes API is running"
    })

@app.get("/notes")
def list_notes():
    return jsonify({"notes": notes.list_notes()})

@app.post("/notes")
def create_note():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request harus berupa JSON object."}), 400

    try:
        note = notes.create_note(data.get("content"))
        return jsonify({"message": "Catatan berhasil dibuat.", "note": note}), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    if notes.delete_note(note_id):
        return jsonify({"message": "Catatan berhasil dihapus."})

    return jsonify({"error": "Catatan tidak ditemukan."}), 404


if __name__ == "__main__":
    app.run(debug=False)