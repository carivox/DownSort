# 🧹 Downsort

**Downsort** ist ein einfaches, leises und plattformübergreifendes Python-Skript, das das ständige Chaos im Downloads-Ordner beseitigt. Es analysiert alle Dateien in deinem Downloads-Verzeichnis und sortiert sie automatisch nach Dateityp in passende Unterordner ein.

---

## 🌟 Features

- 💻 **Plattformübergreifend:** Funktioniert unter Windows, macOS und Linux.
- 📁 **Saubere Struktur:** Erstellt übersichtliche Unterordner direkt in deinem Downloads-Verzeichnis.
- ⚡ **Sicher:** Vorhandene Ordner werden nicht angetastet und Dateien mit gleichem Namen im Zielordner werden nicht überschrieben.
- ⚙️ **Anpassbar:** Neue Dateiendungen oder eigene Kategorien lassen sich mit wenigen Zeilen Code hinzufügen.

---

## 📂 Die Ordnerstruktur

Nach der Ausführung sieht dein Downloads-Ordner wie folgt aus:

```text
Downloads/
├── Bilder/        # .jpg, .png, .gif, .svg, .webp ...
├── Dokumente/     # .pdf, .docx, .xlsx, .pptx, .txt ...
├── Archive/       # .zip, .rar, .7z, .tar, .gz ...
├── Audio/         # .mp3, .wav, .aac, .flac ...
├── Video/         # .mp4, .mkv, .mov, .avi ...
├── Programme/     # .exe, .msi, .dmg, .pkg, .deb ...
└── Sonstiges/     # Alle übrigen Dateitypen
