from slackbot.bot import respond_to, listen_to
from plugins.keyphrase import keyphrase
from plugins.bible_capsule_toys import get_random_answer


@respond_to("(.*)")
def cheer(message, something):
    answer = keyphrase(something)
    answer = answer.sentence_reply()
    message.reply("{}".format(answer))

@respond_to('聖書ガチャ')
@listen_to("聖書ガチャ")
def bible_capsule_toys(message):
    something = get_random_answer().get_random_answer()
    message.reply("{}".format(something))
    message.react('name')
