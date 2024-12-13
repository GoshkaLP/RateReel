import uuid


def generate_movie_logo_file_path(file_id: uuid.UUID) -> str:
    return f"/api/file/{file_id}"
