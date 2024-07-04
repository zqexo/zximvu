class ChatParticipant:
    """
    Класс для представления информации об участнике чата.
    """

    def __init__(self, id, username, avatar_url):
        self.id = id
        self.username = username
        self.avatar_url = avatar_url

    def __repr__(self):
        return f'{self.username} ({self.id})'

    @classmethod
    def create_participants(cls, data):
        """
        Получение данных об участниках чата.
        """
        instances = []
        for part_info in data:
            instances.append(cls(
                id=part_info.get('id'),
                username=part_info.get('username'),
                avatar_url=part_info.get('avatar_url')
            ))
        return instances
