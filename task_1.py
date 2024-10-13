import shutil
from pathlib import Path


def sort_files(src_path: Path, dest_path: Path = Path("dist")) -> None:
    # Створюємо директорію призначення, якщо вона не існує
    dest_path.mkdir(parents=True, exist_ok=True)

    try:
        # Проходимо по всіх елементах у директорії
        for element in src_path.iterdir():
            if element.is_dir():
                # Рекурсивно обробляємо піддиректорії
                sort_files(element, dest_path)
            elif element.is_file():
                # Визначаємо розширення файлу
                file_extension = element.suffix[1:].lower() or "no_extension"
                extension_dir = dest_path / file_extension

                # Створюємо піддиректорію за розширенням, якщо її ще немає
                extension_dir.mkdir(exist_ok=True)

                # Копіюємо файл до відповідної піддиректорії
                try:
                    shutil.copy(element, extension_dir)
                    print(f"File '{element.name}' copied to '{extension_dir}'")
                except PermissionError:
                    print(f"Permission denied: {element}")
                except Exception as e:
                    print(f"Error copying file '{element}': {e}")
    except PermissionError:
        print(f"Permission denied: {src_path}")
    except Exception as e:
        print(f"Error processing directory '{src_path}': {e}")


if __name__ == "__main__":

    src_path = Path("./Temp")
    sort_files(src_path)
