from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="Hello ๐๐ป {}!\n\n๐ ๐๐ฆ ๐ฌ๐ข๐ฆ๐ฉ๐ฅ๐ ๐ฒ๐๐ญ ๐ฉ๐จ๐ฐ๐๐ซ๐๐ฎ๐ฅ ๐๐จ๐ญ ๐๐จ ๐๐ข๐ง๐ ๐ฆ๐๐ ๐ง๐๐ญ ๐ฅ๐ข๐ง๐ค๐ฌ ๐๐ซ๐จ๐ฆ ๐๐ฎ๐ฅ๐ญ๐ข๐ฉ๐ฅ๐ ๐๐จ๐ซ๐ซ๐๐ง๐ญ ๐๐ข๐ญ๐๐ฌ.\n\n๐๐ญ๐ช๐ค๐ฌ /help ๐๐ฐ๐ณ ๐๐ฐ๐ณ๐ฆ ๐๐ฆ๐ญ๐ฑ ๐๐ฏ ๐๐บ ๐๐ด๐ข๐จ๐ฆ โค".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("๐ซUPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("๐ตโโCREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("๐ABOUT", callback_data= "about"),
            InlineKeyboardButton("๐ CLOSE", callback_data= "close")
            ]]
        ),
        disable_web_page_preview=True
    )



@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><u>About Me</u></b>\n\nโข ๐๐๐ฆ๐ : แดแดสสแดษดแด ๊ฑแดแดสแดสแดส \n\nโข ๐๐๐ง๐ ๐ฎ๐๐ ๐ : แดแดสแดแดษด \n\nโข ๐๐ข๐๐ซ๐๐ซ๐ฒ : แดสสแดษขสแดแด \n\nโข ๐๐๐ซ๐ฏ๐๐ซ :  สแดสแดแดแด \n\nโข ๐๐ญ๐๐ญ๐ฎ๐ฌ :  V 1.0 \n\nโข ๐๐ซ๐๐๐ญ๐จ๐ซ : <b><a href='https://t.me/diago_x'>แดษชแดษขแด</a></b>\n\n<b>แดแดแดแดแดแดแด แดษด 1-6-21 ษชษดแดษชแดษด แดษชแดแด 10:00 แดแด</b>\n\n<b><a href='https://t.me/coderzHex'>ยฉแดแดแดแดสแดขสแดx</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("๐CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online โ**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="๐๏ธ Support Group ๐๏ธ", url="https://t.me/MusicBotSupports")
              ]]
          )
      )


@Client.on_message(filters.command(["help", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        text="""<b><u>help</u></b>
๐ก ๐๐ฆ๐ฏ๐ฅ ๐ฎ๐ฆ ๐ข๐ฏ๐บ ๐ฎ๐ฐ๐ท๐ช๐ฆ ๐ฏ๐ข๐ฎ๐ฆ ๐ฐ๐ณ ๐ด๐ฆ๐ณ๐ช๐ฆ๐ด
(๐ฑ๐ญ๐ฆ๐ข๐ด๐ฆ ๐ต๐บ๐ฑ๐ฆ ๐ค๐ฐ๐ณ๐ณ๐ฆ๐ค๐ต ๐ด๐ฑ๐ฆ๐ญ๐ญ๐ช๐ฏ๐จ)

<b>@CoderzHex</b>
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="๐ซUPDATES", url="https://t.me/CoderzHEX"),
              InlineKeyboardButton("๐CLOSE", callback_data = "close")
              ]]
          )
      )
