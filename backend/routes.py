from flask import Blueprint, request, jsonify
from extension import db  
from models import Friend

bp = Blueprint('api', __name__)  

@bp.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friend.query.all()
    result = [friend.to_json() for friend in friends]
    return jsonify(result), 200

@bp.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        required_fields = ["name", "role", "description", "gender"]
        for field in required_fields:
            if field not in data or not data.get(field):
                return jsonify({"error": f'Missing required field: {field}'}), 400

        image_url = f"https://avatar.iran.liara.run/public/{'boy' if gender == 'male' else 'girl'}?username={name}" if gender in ["male", "female"] else None

        new_friend = Friend(name=name, role=role, description=description, gender=gender, image_url=image_url)

        db.session.add(new_friend)
        db.session.commit()
        return jsonify(new_friend.to_json()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route("/api/friends/<int:id>", methods=["DELETE"])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404
        
        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg": "Friend deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route("/api/friends/<int:id>", methods=["PATCH"])    
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404

        data = request.json
        friend.name = data.get("name",friend.name)
        friend.role = data.get("role",friend.role)
        friend.description = data.get("description",friend.description)
        friend.gender = data.get("gender",friend.gender)
        db.session.commit()
        return jsonify(friend.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
 