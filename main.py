from src.imvu_api import IMVUAPI
from src.db_manager import DBManager
from src.participant import ChatParticipant
from src.utils import filter_participants, sort_participants, get_top_participants, print_participants


def user_interaction():
    imvu_api = IMVUAPI()
    print('''Добавьте в свою базу данных таблицу participants (параметры на примере) 

    CREATE TABLE participants (
    id SERIAL PRIMARY KEY,
    username TEXT,
    avatar_url TEXT
    );
    ''')

    db_manager = DBManager(dbname='IMVUDB', user='postgres', password='your_password')

    chat_id = input("Введите ID чата для IMVU: ")
    top_n = int(input("Введите количество участников для добавления в базу данных: "))
    filter_words = input("Введите ключевые слова для фильтрации участников: ").split()

    try:
        chat_data = imvu_api.get_chat_participants(chat_id)
        participants_list = ChatParticipant.create_participants(chat_data)

        for participant in participants_list[:top_n]:
            db_manager.add_participant(participant)

        filtered_participants = filter_participants(participants_list, filter_words)
        sorted_participants = sort_participants(filtered_participants)
        top_participants = get_top_participants(sorted_participants, top_n)

        print_participants(top_participants)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        db_manager.close()


if __name__ == "__main__":
    user_interaction()
