from database.flask_ini import app

from database.models import note, note_log, action

from database.db_utils import *

from database.schemas import NoteSchema


@app.route("/note", methods=["POST"])
@db_lifecycle
@session_lifecycle
def create_note():
    data = NoteSchema().load(request.get_json())
    obj = note(**data)
    act = action("created note")

    session.add(act)
    session.add(obj)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

    log = note_log(obj.id, request.json.get("user_id", None), act.id)

    session.add(log)

    return jsonify(NoteSchema().dump(obj))


@app.route('/note', methods=["GET"])
def get_notes():
    return get_objects(NoteSchema, note)


@app.route("/note/<int:Id>", methods=["GET"])
def get_note_by_Id(Id):
    return get_obj_by_Id(NoteSchema, note, Id)


@app.route("/note/<int:Id>", methods=["PUT"])
@db_lifecycle
@session_lifecycle
def upd_note_by_Id(Id):
    new_data = NoteSchema().load(request.get_json())
    obj = session.query(note).filter_by(id=Id).first()
    act = action(obj.name)

    session.add(act)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

    log = note_log(obj.id, request.json.get("user_id", None), act.id)

    session.add(log)

    if obj is None:
        raise InvalidUsage("Object not found", status_code=404)

    for key, value in new_data.items():
        setattr(obj, key, value)

    return jsonify(NoteSchema().dump(obj))


@app.route("/note/<int:Id>", methods=["DELETE"])
def delete_note_by_id(Id):
    return delete_obj_by_id(NoteSchema, note, Id)