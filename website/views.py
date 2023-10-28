from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    return render_template("home.html", user=current_user)

@views.route("/plan", methods=['GET','POST'])
def plan():
    return render_template("drawing_plan.html")

@views.route("/maps", methods=['GET','POST'])
def maps():
    return render_template("map2.html")

@views.route("/location", methods=['GET','POST'])
def location():
    return render_template("map.html")


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
