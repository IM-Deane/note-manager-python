from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


# routes template
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note is too short!", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("New note added!", category='success')

    return render_template("home.html", user=current_user)
    

@views.route('/delete-note', methods=['DELETE'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/edit-note', methods=['PATCH'])
def edit_note():
    data = json.loads(request.data)
    print(data)
    noteId = data['noteId']
    updated_note_text = data['updatedText']
    current_note = Note.query.get(noteId)
    if current_note:
        if current_note.user_id == current_user.id:
            current_note.data = updated_note_text
            db.session.commit()

    return jsonify({})
