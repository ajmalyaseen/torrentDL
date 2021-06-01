import pyrogram
from pyrogram import filters
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
 

#all buttons 

#start buttons 

start_button=InlineKeyboardMarkup(
        [
               [
                 InlineKeyboardButton("📫 UPDATES", url="https://t.me/coderzHex"),
                 InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
               ],
               [
                 InlineKeyboardButton("📕ABOUT", callback_data="about_data"),
                 InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
               ]
        ]
)

 
# about button 

about_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
) 


@autocaption.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@autocaption.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True,
          reply_markup = help_button           
      )


@autocaption.on_message(filters.command("about") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = about_button
      )   




# call_backs 

@autocaption.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "about_data" in cb_data:
        await cmd.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode="markdown", 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                      InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME),
               parse_mode="markdown", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                        
                       [
                        InlineKeyboardButton("📫 UPDATES", url="https://t.me/coderzHex"),
                        InlineKeyboardButton("🕵‍♂CREATOR", url="https://t.me/DIAGO_X")
                       ],
                       [
                        InlineKeyboardButton("📕ABOUT", callback_data="about_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
                   ]
               )
          )
    elif "close_data" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()

    
          else:
             await cmd.message.edit(
                  text=Translation.NOT_ADMIN_TEXT,
                  parse_mode="html", 
                  disable_web_page_preview=True, 
                  reply_markup=InlineKeyboardMarkup(
                      [
                          [
                           InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                           InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                          ]
 
                      ] 
                  ) 
             )
 
