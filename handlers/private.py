from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/9ec743cdf3297926c0f53.png",
                caption=(f"""**𝖬𝖾𝗋𝗁𝖺𝖻𝖺 𝖡𝖾𝗇 𝖬𝖺𝗃𝖾𝗌𝗍𝖾 𝖬𝗎𝗌𝗂𝖼 𝖯𝗋𝗈 𝖡𝗈𝗍 !** \n\n**𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗍𝖾 𝖬𝗎𝗓𝗂𝗄 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝗂𝗋𝗂𝗆 !** \n\n**𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝖮𝗅𝖺𝗋𝖺𝗄 𝖤𝗄𝗅𝖾𝗒𝗂𝗉 𝖪𝖾𝗌𝗂𝗇𝗍𝗂𝗌𝗂𝗓 𝖬𝗎𝗓𝗂𝗀𝗂𝗇 𝖳𝖺𝖽𝗂𝗇𝗂 𝖢𝗂𝗄𝖺𝗋𝖺𝖻𝗂𝗅𝗂𝗋𝖺𝗂𝗇𝗂𝗓 . . . !** \n\n**𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂𝗆𝗂 𝖦𝗈𝗋𝗆𝖾𝗄 İ𝖼𝗂𝗇 /komutlar 𝖸𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇𝗂𝗓 !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 Asistan", url="https://t.me/MajesteMusicProAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 Sahibim", url="https://t.me/MacroPem"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 Sohbet Grubu", url=f"https://t.me/MajesteSohbet"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["komutlar", f"komutlar@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" **⇨ Not:** \n\n **⇨ Botun Aktif Çalışabilmesi için Şu 3 Yetkiye ihtiyacı vardır** \n\n **⇨ Sesli Sohbetleri Yönetme , Bağlantılar ile davet etme , Mesajları Silme** \n\n **⇨ bu 3 yetkiyi vererek botu kullanabilirsiniz**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📚 Tüm Komutlar", callback_data="herkes")
                 ],[
                     InlineKeyboardButton(
                         "🗯️ Ana Menü ", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "📩 Sahibim", url="https://t.me/Yorgun_Birisi")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("**⇨ Not:** \n\n **⇨ Botun Aktif Çalışabilmesi için Şu 3 Yetkiye ihtiyacı vardır** \n\n **⇨ Sesli Sohbetleri Yönetme , Bağlantılar ile davet etme , Mesajları Silme** \n\n **⇨ bu 3 yetkiyi vererek botu kullanabilirsiniz**", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "📚 Tüm Komutlar", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🗯️ Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "📩 Sahibim", url="https://t.me/Yorgun_Birisi")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nsᴇsʟɪ sᴏʜʙᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ \n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "📩 Sohbet Grubu", url="https://t.me/MajesteSohbet")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Yorgun_Birisi")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**𝖬𝖾𝗋𝗁𝖺𝖻𝖺 𝖡𝖾𝗇 𝖬𝖺𝗃𝖾𝗌𝗍𝖾 𝖬𝗎𝗌𝗂𝖼 𝖯𝗋𝗈 𝖡𝗈𝗍 !** \n\n**𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗍𝖾 𝖬𝗎𝗓𝗂𝗄 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝗂𝗋𝗂𝗆 !** \n\n**𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝖮𝗅𝖺𝗋𝖺𝗄 𝖤𝗄𝗅𝖾𝗒𝗂𝗉 𝖪𝖾𝗌𝗂𝗇𝗍𝗂𝗌𝗂𝗓 𝖬𝗎𝗓𝗂𝗀𝗂𝗇 𝖳𝖺𝖽𝗂𝗇𝗂 𝖢𝗂𝗄𝖺𝗋𝖺𝖻𝗂𝗅𝗂𝗋𝖺𝗂𝗇𝗂𝗓 . . . !** \n\n**𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂𝗆𝗂 𝖦𝗈𝗋𝗆𝖾𝗄 İ𝖼𝗂𝗇 /komutlar 𝖸𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇𝗂𝗓 !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 Beni Gruba Ekle 🎉", url=f"https://t.me/MajesteMusicProBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 Asistan", url="https://t.me/MajesteMusicProAsistan"
                    ),
                    InlineKeyboardButton(
                        "📝 Sahibim", url="https://t.me/MacroPem"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "📝 Sohbet Grubu", url=f"https://t.me/MajesteSohbet"
                    )
                ]
                
           ]
        ),
    )
