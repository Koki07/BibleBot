# coding:utf-8
import sqlite3
import plugins.list_only_one
import MeCab

conn = sqlite3.connect("path", check_same_thread=False)
cursor = conn.cursor()


class keyphrase(object):
    def __init__(self, sentence):
        self.sentence = sentence

    def extractKeyword(self):
        tagger = MeCab.Tagger('-Ochasen')
        node = tagger.parseToNode(self.sentence)
        noun = []
        while node:
            if str(node.feature).split(',')[0] == '名詞':
                noun.append(node.surface)
            node = node.next
        noun = plugins.list_only_one.f7(noun)
        return noun

    def sentence_reply(self):
        result = self.extractKeyword()
        for x in range(len(result)):
            trouble = cursor.execute("SELECT sentence FROM db_name WHERE sentence LIKE '%%%s%%'" % (result[x],))
            trouble = trouble.fetchone()
            if trouble != None:
                trouble = str("'".join(list(trouble)))
                return trouble
                break
            return '諦めてください'
