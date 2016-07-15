# coding:utf-8
import sqlite3
import numpy.random as np

conn = sqlite3.connect("path", check_same_thread=False)
cursor = conn.cursor()


class get_random_answer(object):
    def __init__(self):
        pass

    def get_random_answer(self):
        record = cursor.execute("SELECT COUNT(sentence) FROM db_name")
        record = str(record.fetchone()[0])
        random_id = np.randint(int(record))
        get_sentence = cursor.execute("SELECT sentence FROM db_name WHERE id = ?", (random_id,))
        get_sentence = get_sentence.fetchone()
        answer = str("'".join(list(get_sentence)))
        print(answer)
        return answer
