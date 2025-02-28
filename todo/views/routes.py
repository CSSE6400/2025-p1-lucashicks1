from flask import Blueprint, jsonify, request

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/health")
def health():
    return jsonify({"status": "ok"})


@api.route("/todos", methods=["GET"])
def get_todos():
    args = request.args
    completed: bool = args.get("completed", default=True, type=bool)
    window: int = args.get("window", default=0, type=int)  # noqa: F841

    return jsonify(
        [
            {
                "id": 1,
                "title": "Watch CSSE6400 Lecture",
                "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
                "completed": completed,
                "deadline_at": "2023-02-27T00:00:00",
                "created_at": "2023-02-20T00:00:00",
                "updated_at": "2023-02-20T00:00:00",
            }
        ]
    )


@api.route("/todos", methods=["POST"])
def create_todo():
    return (
        jsonify(
            {
                "id": 1,
                "title": "Watch CSSE6400 Lecture",
                "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
                "completed": True,
                "deadline_at": "2023-02-27T00:00:00",
                "created_at": "2023-02-20T00:00:00",
                "updated_at": "2023-02-20T00:00:00",
            }
        ),
        201,
    )


@api.route("/todos/<int:id>", methods=["GET"])
def get_todo(id: int):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00",
        }
    )


@api.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id: int):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00",
        }
    )


@api.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id: int):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": True,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00",
        }
    )
