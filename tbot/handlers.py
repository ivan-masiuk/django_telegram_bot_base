from telebot import types
from telebot.apihelper import ApiTelegramException

from tbot_base.bot import tbot as bot


@bot.message_handler(func=lambda message: True)
def text_messages(message: types.Message):
    bot.send_message(message.from_user.id, 'Hello!')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    bot.send_message(call.from_user.id, 'Hello!')

    # remove the "clock" on the inline button
    try:
        bot.answer_callback_query(callback_query_id=call.id, text='')
    except ApiTelegramException:
        pass
