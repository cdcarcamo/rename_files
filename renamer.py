from pathlib import Path

def rename_file(file, base_name, start):

    file = Path(file)

    archives = sorted(file.iterdir())

    counter = start

    for archive in archives:
        
        if archive.is_file():

            new_name = f"{base_name}_{counter}{archive.suffix}"

            new_path = archive.with_name(new_name)

            archive.rename(new_path)

            counter += 1

    