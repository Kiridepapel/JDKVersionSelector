import os
import subprocess
import tkinter as tk

class JDKVersionSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JDK Version Selector")

        panel = tk.Frame(self)
        panel.pack()

        java_versions = self.find_java_versions()
        total_height = 0
        row = 0
        paddingY = 10
        
        for version, path in java_versions.items():
            button = tk.Button(panel, text=version, command=lambda p=path: self.set_java_home(p))
            pady = (paddingY if row == 0 else 0, paddingY)
            button.grid(row=row, column=0, pady=pady)
            total_height += button.winfo_reqheight() + sum(pady)
            row += 1

        self.geometry(f"300x{total_height}")

    def find_java_versions(self):
        java_versions = {}
        java_dir = "C:\\Program Files\\Java"
        for item in os.listdir(java_dir):
            item_path = os.path.join(java_dir, item)
            if os.path.isdir(item_path) and item.startswith("jdk"):
                if item.startswith("jdk1.8"):
                    version = "8" + item[6:].replace("_", ".")
                else:
                    version = item.split("-")[-1]
                java_versions[f"Java {version}"] = item_path
        return java_versions

    def set_java_home(self, java_home_path):
        subprocess.run(["cmd.exe", "/c", "setx", "JAVA_HOME", f'{java_home_path}\\bin'])
        self.destroy()

if __name__ == '__main__':
    app = JDKVersionSelector()
    app.mainloop()
