from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/23d4d63b9d91d12bc967f.jpg",
                caption=(f"""**Salam Mən L E Y L A Musiqi Botuyam !** \n\n**Səsli Söhbətinizdə Musiqi ifa edə bilərəm !** \n\n**Məni Qrupa Admin Olaraq əlavə edib donmadan Musiqinin Ləzətin Çıxara bilərsiz . . . !** \n\n**Komutları Görmək Üçün /komutlar Yazabilərsiz !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Qrupuna Əlavə Et ❱ ➕", url=f"https://t.me/leylamusiciBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🤵‍♀️ Asistan", url="https://t.me/aytenasisstan"
                    ),
                    InlineKeyboardButton(
                        "📝 Sahibim", url="https://t.me/oldteamabasof"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "⚛ Blog", url=f"https://t.me/TEAMABASOFX"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["komutlar", f"komutlar@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" **💬 MƏLUMAT:** \n\n **⇨ Botun Aktiv İşləməsi üçün Bu 3 Yetgiyə sahib olmaqım lazımdır** \n\n **⇨ Səsli Sohbətləri İdarə etmək , Bağlantılar ilə dəvət etmə , Mesajları Silmə** \n\n **⇨ bu 3 yetgini verərək botu işlədəbilərsən**", 
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
                         "📩 Sahibim", url="https://t.me/oldteamabasof")
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
            "📩 Sahibim", url="https://t.me/oldteamabasof")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\Bot Komutları \n» /vbul => video endirir . \n» /bul => Musiqi endirir . \n» /oynat => Musiqini ifa edir . \n» /durdur => Musiqini dayandır . \n» /devam => Musiqini davam etdir . \n» /atla =>  Musiqini dəyiş . \n» /son => Musiqini Bitir . \n» /katil => Asisstanı Qrupa Əlavə Edər . \n» /reload => Admin Siyahisini yenile .</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🎴 Blog", url="https://t.me/TEAMABASOFX")
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
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün komut menüsü 🤩\n\n ▶️ /devam - musiqi ifa etməyə davam et\n ⏸️ /durdur - oxuyan ifanı dayandırmaq üçün\n 🔄 /atla- Sıraya Alımmış ifanı oxudar.\n ⏹ /son - musiqi ifa etməyi dayandırmaq\n 🔼 /ver botun sadəcə yönətici üçün isdifadəedəbiləcəyi olan komutlarını isdifadə edə biləcəyi üçün kullanıcıya yetgi ver\n 🔽 /al botun yönətici komutlarını isdifadə edə bilən kullanıcının yetgisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qatılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         " Sahib", url="https://t.me/oldteamabasof")
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
                        "💎 Məni Qrupa Əlavə Et 💎", url=f"https://t.me/leylamusiciBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🇹🇷 Asistan", url="https://t.me/aytenasisstan"
                    ),
                    InlineKeyboardButton(
                        "📝 Sahibim", url="https://t.me/oldteamabasof"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "💎 Blog", url=f"https://t.me/TEMABASOFX"
                    )
                ]
                
           ]
        ),
    )
