from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Salom xush kelibsiz.",
    )


def help(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Qanday yordam berolaman.",
    )


def send_menu(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
        chat_id=update.message.chat.id,
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='Mahsulotlar',
                        web_app=WebAppInfo(url='https://tirikchilik.uz/')
                    ),
                    KeyboardButton(text="Bosh sahifa"),
                    KeyboardButton(text="Mening profilim"),
                ],
                [
                    KeyboardButton(
                        text="Location",
                        request_location=True,
                    ),
                    KeyboardButton(
                        text="Contact",
                        request_contact=True,
                    ),
                ],
            ],
            resize_keyboard=True,
        ),
    )
