import os
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Python-Evaluate-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {}, I am a python evaluate telegram bot.

Made by @FayasNoushad
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )

@FayasNoushad.on_message(filters.private & filters.reply & filters.command(["eval", "evaluate", "run"]))
async def evaluation(bot, update):
    code = update.reply_to_message.text
    try:
        output = str(eval(code))
        if len(output) < 4096:
            await update.reply_text(
                text=output,
                disable_web_page_preview=True,
                quote=True
            )
        else:
            with BytesIO(str.encode(str(output))) as output_file:
                output_file.name = "output.txt"
                await update.reply_document(
                    document=output_file,
                    caption="Made by @FayasNoushad",
                    quote=True
                )
    except Exception as error:
        print(error)

FayasNoushad.run()
