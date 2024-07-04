import psycopg2
from participant import ChatParticipant

class DBManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cur = self.conn.cursor()

    def add_participant(self, participant: ChatParticipant):
        insert_query = """
            INSERT INTO participants (id, username, avatar_url)
            VALUES (%s, %s, %s)
        """
        self.cur.execute(insert_query, (participant.id, participant.username, participant.avatar_url))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
