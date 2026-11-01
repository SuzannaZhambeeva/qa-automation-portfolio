USER_SCHEMA = {
    "type": "object",
    "required": ["id", "email", "first_name"],
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    }
}

USERS_LIST_SCHEMA = {
    "type": "object",
    "required": ["page", "data"],
    "properties": {
        "page": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type":"object",
                "required": ["id", "email"],
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"}
                }
            }
        }
    }
}

USER_SCHEMA_POST = {
    "type": "object",
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ],
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    }
}