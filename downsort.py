import os
import shutil
from pathlib import Path


def sort_downloads():
    downloads_path = Path.home() / "Downloads"

    if not downloads_path.exists():
        print(f"Fehler: Der Ordner {downloads_path} konnte nicht gefunden werden.")
        return

    print(f"Sortiere Dateien IN diesem Ordner: {downloads_path}\n")

    extensions_map = {
        "Bilder": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".webp"],
        "Dokumente": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
        "Archive": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Creative": [".psd", ".xfc", ".af", ".afdesign", ".afpub", ".afphoto"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4a"],
        "Programme": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".sh", ".apk"]
    }

    folder_map = {ext: folder for folder, exts in extensions_map.items() for ext in exts}

    count = 0

    for item in downloads_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()

            folder_name = folder_map.get(ext, "Sonstiges")

            target_dir = downloads_path / folder_name
            target_dir.mkdir(exist_ok=True)

            target_path = target_dir / item.name

            if target_path.exists():
                print(f"Übersprungen (existiert bereits): {item.name}")
                continue

            try:
                shutil.move(str(item), str(target_path))
                print(f"Verschoben: {item.name} -> Downloads/{folder_name}/")
                count += 1
            except Exception as e:
                print(f"Fehler bei {item.name}: {e}")

    print(f"\nFertig! {count} Dateien wurden in Unterordner innerhalb von 'Downloads' einsortiert.")


if __name__ == "__main__":
    sort_downloads()