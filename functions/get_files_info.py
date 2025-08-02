import os

def get_files_info(working_directory, directory="."):
    try:
        # Join and resolve the full path
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory)

        # Security check: ensure full_path is within working_directory
        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Ensure it's a directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(full_path)
        result_lines = []
        for entry in entries:
            entry_path = os.path.join(full_path, entry)
            is_dir = os.path.isdir(entry_path)
            try:
                size = os.path.getsize(entry_path)
            except Exception as e:
                return f'Error: Could not get size of "{entry}": {str(e)}'

            result_lines.append(f'- {entry}: file_size={size} bytes, is_dir={is_dir}')

        return "\n".join(result_lines)

    except Exception as e:
        return f"Error: {str(e)}"
