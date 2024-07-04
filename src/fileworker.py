import json
import os
from abc import ABC, abstractmethod
from participant import ChatParticipant

class FileWorker(ABC):
    @abstractmethod
    def add_participant(self, participant):
        pass

    @abstractmethod
    def get_participants(self, criteria):
        pass

    @abstractmethod
    def delete_participant(self, participant):
        pass

class JSONWorker(FileWorker):
    """
    Класс для работы с JSON-файлами.
    """

    def __init__(self, file_name: str):
        """
        Инициализация объекта класса JSONWorker.
        """
        self.file_name = file_name
        self.path = os.path.join('data', self.file_name)
        self.create_directory()

    def create_directory(self):
        """
        Создание директории 'data', если она не существует.
        """
        if not os.path.exists('data'):
            os.makedirs('data')

    def add_participant(self, participant: ChatParticipant):
        """
        Добавление участника
        """
        part_info = participant.__dict__
        content = self.read_file()
        content.append(part_info)
        self.write_file(content)

    def get_participants(self, criteria):
        """
        Получение участников
        """
        content = self.read_file()
        return [part for part in content if criteria in part['username']]

    def delete_participant(self, participant: ChatParticipant):
        """
        Удаление участника
        """
        content = self.read_file()
        content = [part for part in content if part['username'] != participant.username]
        self.write_file(content)

    def read_file(self):
        """
        Чтение файла
        """
        if not os.path.exists(self.path):
            return []
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        """
        Запись файла
        """
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
