from .connection import Function
from src.logStore.database.database_handler import DatabaseHandler


class ChatFunction(Function):

    def __init__(self):
        self.__handler = DatabaseHandler()

    def insert_chat_msg(self, cbor):
        self.__handler.add_to_db(event_as_cbor=cbor)

    def get_chat_since(self, application, timestamp, feed_Id, chat_id):
        result = self.__handler.get_event_since(application, timestamp, feed_Id, chat_id)
        return result

    def get_full_chat(self, application, feed_Id, chat_id):
        return self.__handler.get_all_chat_msgs('chat', chat_id)
