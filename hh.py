import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Funktion, die den Desktop aufräumt
def cleanup_desktop():
    desktop_path = r"C:\Users\ivang\Neuer Ordner (3)"
    
    folders = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Programs': ['.exe', '.msi'],
    }

    # Ordner erstellen, falls sie nicht existieren
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
             os.makedirs(folder_path)

    # Dateien auf dem Desktop sortieren
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(desktop_path, folder))
                    moved = True
                    break
            
            # Unsortierte Dateien in 'Others' verschieben
            if not moved:
                others_folder = os.path.join(desktop_path, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)

    # Meldung anzeigen, wenn die Aktion abgeschlossen ist
    messagebox.showinfo("Fertig!", "Der Desktop wurde erfolgreich aufgeräumt!")

# Benutzeroberfläche erstellen
def create_gui():
    root = tk.Tk()
    root.title("Desktop Cleanup Tool")

    # Fenstergröße und Label
    root.geometry("300x150")
    label = tk.Label(root, text="Desktop Cleanup Tool", font=("Arial", 14))
    label.pack(pady=10)

    # Aufräum-Button
    cleanup_button = tk.Button(root, text="Desktop aufräumen", command=cleanup_desktop, font=("Arial", 12))
    cleanup_button.pack(pady=10)

    # Haupt-Event-Schleife starten
    root.mainloop()

# GUI starten
create_gui()