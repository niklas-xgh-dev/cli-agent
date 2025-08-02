import os
from .config import MAX_FILE_CONTENT_LENGTH

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs = os.path.abspath(working_directory)
        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return f'Error: {str(e)}'
        if len(content) > MAX_FILE_CONTENT_LENGTH:
            return content[:MAX_FILE_CONTENT_LENGTH] + f'[...File "{file_path}" truncated at {MAX_FILE_CONTENT_LENGTH} characters]'
        return content
    except Exception as e:
        return f'Error: {str(e)}'
