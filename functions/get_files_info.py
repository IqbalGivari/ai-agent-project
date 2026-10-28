import os

def get_files_info(working_directory, directory):
    try:
        # 1. Validasi path
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        result_lines = []
        with os.scandir(target_dir) as entries:
            for entry in entries:
                name = entry.name
                is_dir = entry.is_dir()
                try:
                    file_size = entry.stat().st_size
                except OSError:
                    file_size = 0
                
                result_lines.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}