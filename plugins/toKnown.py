# fileName : plugins/toKnown.py
# copyright ©️ 2021 nabilanavab

from pyrogram.types import Message
from plugins.fileSize import get_size_format as gSF
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#--------------->
#--------> LOCAL VARIABLES
#------------------->

pdfInfoMsg = """`What shall i wanted to do with this file.?`

File Name : `{}`
File Size : `{}`

`Nomer halaman: {}`"""

#--------------->
#--------> EDIT CHECKPDF MESSAGE (IF PDF & NOT ENCRYPTED)
#------------------->

# convert unknown to known page number msgs
async def toKnown(callbackQuery, number_of_pages):
    try:
        fileName = callbackQuery.message.reply_to_message.document.file_name
        fileSize = callbackQuery.message.reply_to_message.document.file_size
        
        await callbackQuery.edit_message_text(
            pdfInfoMsg.format(
                fileName, await gSF(fileSize), number_of_pages
            ),
            reply_markup = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("METADATA",
                     callback_data=f"KpdfInfo|{number_of_pages}"),
                    InlineKeyboardButton("🗳️ PREVIEW 🗳️",
                                        callback_data="Kpreview")
                ],[
                    InlineKeyboardButton("IMAGES 🖼️",
                     callback_data=f"KtoImage|{number_of_pages}"),
                    InlineKeyboardButton("TEXT",
                      callback_data=f"KtoText|{number_of_pages}")
                ],[
                    InlineKeyboardButton("ENCRYPT",
                     callback_data=f"Kencrypt|{number_of_pages}"),
                    InlineKeyboardButton("DECRYPT",
                                   callback_data=f"notEncrypted")
                ],[
                    InlineKeyboardButton("COMPRESS",
                    callback_data=f"Kcompress|{number_of_pages}"),
                    InlineKeyboardButton("ROTATE",
                      callback_data=f"Krotate|{number_of_pages}")
                ],[
                    InlineKeyboardButton("SPLIT",
                       callback_data=f"Ksplit|{number_of_pages}"),
                    InlineKeyboardButton("🧬 MERGE 🧬",
                                           callback_data="merge")
                ],[
                    InlineKeyboardButton("STAMP",
                       callback_data=f"Kstamp|{number_of_pages}"),
                    InlineKeyboardButton("✏️ RENAME ✏️",
                      callback_data=f"Krename|{number_of_pages}")
                ],[
                    InlineKeyboardButton("OCR",
                         callback_data=f"Kocr|{number_of_pages}"),
                    InlineKeyboardButton("🥷 A4 FORMAT 🥷",
                      callback_data=f"Kformat|{number_of_pages}")
                ],[
                    InlineKeyboardButton("🚫 TUTUP 🚫P",
                                        callback_data="closeALL")
                ]]
            )
        )
    except Exception: pass

#                                                                                  Telegram: @nabilanavab
