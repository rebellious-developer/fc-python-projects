#!/usr/bin/env python3
"""
Renames all files in a directory based on a specified pattern.

Requirements:
- The program should accept the following command-line arguments:
  * --in_dir: The path to the directory containing files to rename.
  * --out_dir: The path to the directory where renamed files will be saved.
  * --pattern: The renaming pattern. Use {name} for original name, {ext} for extension, and {num} for a sequential number.
- The program should create a COPY of the original files with the new names in a specified output directory.
- The new names should follow the specified pattern, replacing the placeholders with the appropriate values.
- The program should handle large files efficiently, ensuring that it does not load the entire file into memory at once.
- The program should handle errors gracefully, such as invalid directory paths or permission issues.
- For security reasons the the program should not allow directory traversal outside of the specified input directory. This applies to be input and output directories.
"""

import argparse
import json
import os

arg_defaults = {
    "in_dir": "./sample_files",
    "out_dir": "./renamed_sample_files",
    "pattern": "renamed_{num}_{name}.{ext}",
}


def create_safe_path_abs(root_dir, path) -> str:
    """
    Creates a safe absolute path by preventing directory traversal outside the root directory.

    Args:
        root_dir (str): The root directory to prevent traversal outside of.
        path (str): The input path to be made safe.

    Returns:
        str: A safe absolute path within the root directory.
    """
    abs_root = os.path.abspath(root_dir)
    abs_path = os.path.abspath(os.path.join(abs_root, path))

    if not abs_path.startswith(abs_root):
        raise ValueError(
            f"Unsafe path detected: '{path}' attempts to traverse outside '{root_dir}'"
        )

    return abs_path


def copy_file(src_path, dst_path):
    """
    Copies a file by reading and writing in binary chunks.
    """
    try:
        with open(src_path, "rb") as src_file, open(dst_path, "wb") as dst_file:
            # Read and write in chunks of 1MB
            chunk_size = 1024 * 1024
            while True:
                chunk = src_file.read(chunk_size)
                if not chunk:
                    break
                dst_file.write(chunk)
        print("File copied successfully.")
    except FileNotFoundError:
        print(f"Error: The file at {src_path} was not found.")
    except PermissionError:
        print(
            "Error: You do not have permission to read the source or write to the destination."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def rename_files(in_dir_safe, out_dir_safe, pattern):
    """
    Renames files in a directory based on a given pattern.

    Args:
        in_dir_safe (str): The safe absolute path to the directory containing the files.
        out_dir_safe (str): The safe absolute path to the directory where renamed files will be saved.
        pattern (str): The renaming pattern with placeholders.
    """
    if not in_dir_safe or not out_dir_safe:
        print("ERROR: Input and output directory paths must be provided.")
        return

    # Ensure the input folder exists
    if not os.path.exists(in_dir_safe):
        print(f"ERROR: Input directory '{in_dir_safe}' does not exist.")
        return

    print(
        f"Renaming files\n  * From: {in_dir_safe}\n  * To: {out_dir_safe}\n  * Pattern: {pattern}\n"
    )

    try:
        os.makedirs(out_dir_safe, exist_ok=True)
        files = [
            f
            for f in os.listdir(in_dir_safe)
            if os.path.isfile(os.path.join(in_dir_safe, f))
        ]

        for i, filename in enumerate(files):
            name, ext = os.path.splitext(filename)
            new_name = pattern.format(name=name, ext=ext.lstrip("."), num=i + 1)
            old_path = os.path.join(in_dir_safe, filename)
            new_path = os.path.join(out_dir_safe, new_name)

            try:
                # Copy the file to the new location with the new name
                # Technically this isn't a rename via os.rename, but since we are outputting to a seperate directory, we copy instead
                print(f"Copy: {filename} -> {new_name}")
                copy_file(old_path, new_path)
            except OSError as e:
                print(f"Error renaming file {filename}: {e}")

    except FileNotFoundError as e:
        print(f"Error: File not found at '{e.filename}'")
    except PermissionError as e:
        print(f"Error: Permission denied to access file '{e.filename}'")


def create_arg_parser() -> argparse.ArgumentParser:
    """
    Creates and returns the argument parser for command-line arguments.

    Returns:
        argparse.ArgumentParser: The argument parser.
    """
    parser = argparse.ArgumentParser(description="Bulk rename files in a directory.")
    parser.add_argument(
        "--in_dir",
        help=f"The path to the directory containing files to rename. Default is '{arg_defaults['in_dir']}'.",
        default=arg_defaults["in_dir"],
    )
    parser.add_argument(
        "--out_dir",
        help=f"The path to the directory where renamed files will be saved. Default is '{arg_defaults['out_dir']}'.",
        default=arg_defaults["out_dir"],
    )
    parser.add_argument(
        "--pattern",
        help=f"The renaming pattern. Use {{name}} for original name, {{ext}} for extension, and {{num}} for a sequential number. Default is '{arg_defaults['pattern']}'.",
        default=arg_defaults["pattern"],
    )
    return parser


def extract_args(parser: argparse.ArgumentParser, root_dir: str) -> dict:
    """
    Extracts command-line arguments and applies default values if necessary.
    """
    parsed = parser.parse_args()

    args = arg_defaults.copy()
    for key in arg_defaults.keys():
        if getattr(parsed, key) is not None:
            args[key] = getattr(parsed, key)

    args["in_dir_safe"] = create_safe_path_abs(root_dir, args["in_dir"])
    args["out_dir_safe"] = create_safe_path_abs(root_dir, args["out_dir"])

    return args


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("File Renaming Sample Project\n")
    arg_parse = create_arg_parser()
    print("Usage:", arg_parse.format_help())

    args = extract_args(arg_parse, script_dir)
    print("Arguments:", json.dumps(args, indent=4), "\n")

    in_dir = args["in_dir_safe"]
    out_dir = args["out_dir_safe"]
    pattern = args["pattern"]
    rename_files(in_dir, out_dir, pattern)


if __name__ == "__main__":
    main()
