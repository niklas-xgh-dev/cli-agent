# CLI Agent

A minimal AI coding agent using Google's Gemini API.

## What It Does

CLI tool accepts a natural-language coding task (e.g., "fix my calculator app") and uses a loop of predefined functions to iteratively:

* Scan files in a directory
* Read and modify file contents
* Execute Python code
* Re-analyze and repeat

All decisions are made by a Gemini LLM, simulating the behavior of tools like Cursor or Claude Code.

## Example

```bash
uv run main.py "fix my calculator app, it's not starting correctly"
```

Output:

```
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# ...
# Final response:
# Great! The calculator app now seems to be working correctly.
```