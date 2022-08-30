from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["katil", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni öncə Yönətici etməlisən</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Sesmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Sənin Əmrin üzərə gəldim")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan Onsuzda Qrupta Var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 Xəta 🔵\n User {user.first_name} userbot üçün çoxlu qatılma istəkləri səbəbi ilə qrupunuza qatılamadı! Asistanın qrupta qadağan etmədiyində əmin olun."
            "\n\n Yada Asistan Hesabını Qruba Sən Əlavə Et </b>",
        )
        return
    await message.reply_text(
            "<b>Asistan Onsuzda Qrupta Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı qrubunuzdan ayrılamadı!."
            "\n\nYada Sən Çıxarabilirsin</b>",
        )
        return
 
 
 
