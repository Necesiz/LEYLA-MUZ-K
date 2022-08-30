from pyrogram import Client
import asyncio
from config import SUDO_USERS
from config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Salam, Musiqi asistanı hizmətindədir.\n\n ❗️ qaydalar:\n - Sohbətə icazə yox.\n - Bilgi ve Komutlarım üçün qrupunuzun sohbətində **/bilgi** yazarsanız. (Asistan söhbətinə bilgi yazmayın.) Musiqi komutlarını örgənəbilərsiz. \n - İstənməyən postaya icazə verilməz \n\n 🚨 **Userbot qrupunuza qatılmırsa >> DƏVƏT KATILMA ÖZƏLLİYİNİ VƏ SƏS YÖNƏTİMİ ÖZƏLLİKLƏRİNİ VER YÖNƏTİCİ EDİN. <<**\n\n ⚠️ DİQQƏT: Burada bir mesaj gönderiyosanız. Yönəticinin ilətinizin görəcəyi anlamına gəlir.\n - Özəl bilgiləri burada paylaşmayınız. (Musiqi Botunu Xaiş Edirəm Gizli Qruplara almayınız.) 📚 Bilgi için [Sahibime 🧩](https://t.me/oldteamabasof) Yazabilərsiz 🇦🇿\n",
            )
            return
 
    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Artıq mənə yaza bilərsən")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Artıq mənə yaza bilmərəsn")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**Hey Userbot Yazışması artıq başarılı.**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Yaxlaşıq olaraq PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Bu şəkildə PM")
        return
    message.continue_propagation()
