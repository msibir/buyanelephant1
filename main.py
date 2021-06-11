import telebot

bot = telebot.TeleBot('1732392723:AAFe2wPwgcX1v1585Gw8zJH4MH3CW4RBjaw')

group_id = -1001311790860
person_id = 1743731141
delete_last = True


@bot.message_handler(content_types=['audio'])
def get_text_messages(message):
    if message.from_user.id == person_id:
        bot.send_audio(group_id, message.audio.file_id)
        if delete_last:
            bot.delete_message(person_id, message.message_id)


bot.polling(none_stop=True, interval=0)
