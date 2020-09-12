import os


class BackupManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def backup_exist(self):
        return os.path.exists(self.file_path)

    def get_backup_value(self):
        file = open(self.file_path, 'r')
        value = file.read()
        file.close()
        try:
            value = int(value)
        except ValueError:
            print("Erreur lors de la lecture de la sauvegarde")
            value = -1
        return value

    def delete_backup(self):
        os.remove(self.file_path)

    def make_backup(self, value: int):
        file = open(self.file_path, 'w')
        file.write(str(value))
        file.close()
