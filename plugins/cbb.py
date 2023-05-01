#(©)Codexbotz
import contextlib
import datetime
import logging

from database import database
from database import del_user, present_user, full_userbase, add_user ,get_short
from pyrogram import Client, filters
from translation import *


from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(filters.command("shortener_api") & filters.private)
@private_use
async def shortener_api_handler(bot, message: Message):
    user_id = message.from_user.id
    user = await get_short(user_id)
    cmd = message.command
    if len(cmd) == 1:
        s = SHORTENER_API_MESSAGE.format(
            base_site=user["base_site"], shortener_api=user["shortener_api"]
        )

        return await message.reply(s)
    elif len(cmd) == 2:
        api = cmd[1].strip()
        await add_user(user_id, {"shortener_api": api})
        await message.reply(f"Shortener API updated successfully to {api}")

        
# @Client.on_message(filters.command("header") & filters.private)
# @private_use
# async def header_handler(bot, m: Message):
#     user_id = m.from_user.id
#     cmd = m.command
#     user = await get_user(user_id)
#     if m.reply_to_message:
#         header_text = m.reply_to_message.text.html
#         await update_user_info(user_id, {"header_text": header_text})
#         await m.reply("Header Text Updated Successfully")
#     elif "remove" in cmd:
#         await update_user_info(user_id, {"header_text": ""})
#         return await m.reply("Header Text Successfully Removed")
#     else:
#         return await m.reply(
#             HEADER_MESSAGE
#             + "\n\nCurrent Header Text: "
#             + user["header_text"].replace("\n", "\n")
#         )


# @Client.on_message(filters.command("footer") & filters.private)
# @private_use
# async def footer_handler(bot, m: Message):
#     user_id = m.from_user.id
#     cmd = m.command
#     user = await get_user(user_id)
#     if not m.reply_to_message:
#         if "remove" not in cmd:
#             return await m.reply(
#                 FOOTER_MESSAGE
#                 + "\n\nCurrent Footer Text: "
#                 + user["footer_text"].replace("\n", "\n")
#             )

#         await update_user_info(user_id, {"footer_text": ""})
#         return await m.reply("Footer Text Successfully Removed")
#     elif m.reply_to_message.text:
#         footer_text = m.reply_to_message.text.html
#         await update_user_info(user_id, {"footer_text": footer_text})
#         await m.reply("Footer Text Updated Successfully")
        
        
@Client.on_message(filters.command("base_site") & filters.private)
@private_use
async def base_site_handler(bot, message: Message):
    user_id = message.from_user.id
    user = await get_short(user_id)
    cmd = message.command
    site = user["base_site"]
    text = f"`/base_site (base_site)`\n\nCurrent base site: {site}\n\n EX: `/base_site shareus.in`\n\nAvailable base sites:\n Any sites \nAnd All alternate sites to droplink.co"
    if len(cmd) == 1:
        return await message.reply(text=text, disable_web_page_preview=True)
    elif len(cmd) == 2:
        base_site = cmd[1].strip()
        if not domain(base_site):
            return await message.reply(text=text, disable_web_page_preview=True)
        await add_user(user_id, {"base_site": base_site})
        await message.reply("Base Site updated successfully")
        
        
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/link_serials'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/dj_serials_bot'>Click here</a>\n○ Channel : @link_serials\n○ Support Group : @dj_serials_bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
