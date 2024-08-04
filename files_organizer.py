from pathlib import Path


def organize_files_by_extension(path_to_dir):
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.

    Args:
        path_to_dir (str): The path to the directory where files need to be organized.

    Raises:

    :param path_to_dir:
    :return:
    """
    path = Path(path_to_dir).resolve()
    print(f"Resolved path:", path)

    if path.exists() and path.is_dir():
        print(f"The directory {path} exits. Proceeding with file organization.")

    # Iterate over all items in the directory
    for item in path.iterdir():
        print(f"Found item: {item}")
        if item.is_file():
            # Determine the file extesion and create a target directory based on it
            extension = item.suffix.lower()
            target_dir = path / extension[1:]  # Use the extension as the folder name

            # Create the target direcotory if it does not already exist
            target_dir.mkdir(exist_ok=True)

            # Define the new path for the file
            new_path = target_dir / item.name

            # Move the file to the target directory
            item.rename(new_path)

            if new_path.exists():
                print(f"Successfully moved {item} to {new_path}")
            else:
                print(f"Failed to move {item} to {new_path}")
        else:
            print(f"Skipping non-file item: {item}")
    else:
        print(f"Error In: The path {path} does not exist or is not a directory.")


organize_files_by_extension("path")
