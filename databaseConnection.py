import sqlite3
from sqlite3 import Error
from cryptography.fernet import Fernet
from hashlib import sha256


class Criptography:
    def __init__(self, file=''):
        self.fileKey = file

    @staticmethod
    def create_key(file):
        key = Fernet.generate_key()
        with open(f'{file}.txt', 'wb') as file_key:
            file_key.write(key)

    @staticmethod
    def load_key(file):
        key = None
        with open(f'{file}.txt', 'r') as file_key:
            key = file_key.read()
        return key.encode()

    def crypt(self, message, type_encode='register', type_cryptography='fernet'):
        match type_cryptography:
            case 'fernet':
                key = Fernet(self.load_key(self.fileKey))
                # coding message
                message_code = key.encrypt(message.encode())
                match type_encode:
                    case 'register':
                        return message_code
                    case 'search':
                        return "b'"
            case 'hash':
                hash_password = sha256(message.encode())
                return hash_password.hexdigest()

    def decode(self, message):
        key = Fernet(self.load_key(self.fileKey))
        # decoding message
        message_decode = key.decrypt(message)
        return message_decode.decode('utf-8')


class DataBase:
    def __init__(self, file):
        self.file = file

    def conectionDatabase(self):
        conect = None
        try:
            conect = sqlite3.connect(self.file)
        except Error as er:
            return print(er)
        finally:
            return conect

    def searchDatabase(self, query):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        conect.close()
        return res

    def crud(self, sql, execute=0, valores=None):
        conect = self.conectionDatabase()
        cursor = conect.cursor()
        if execute == 0:
            cursor.execute(sql)
        elif execute == 1:
            cursor.executemany(sql, valores)
        conect.commit()
        conect.close()
