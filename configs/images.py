# fileName: configs/images.py
# copyright ©️ 2021 nabilanavab

import os


# ❌ FEEDBACK LINK ❌ [EDITABLE]
FEEDBACK = "https://forms.gle/eph61t6bTy4aNZcR7"


# ❌ DEFAULT THUMBNAIL ❌ [EDITABLE]
# NB: Thumbnails can’t be reused and can be only uploaded as a new file.
# from Configs.images import PDF_THUMBNAIL
PDF_THUMBNAIL = "./images/tmb.png"
# PDF_THUMBNAIL="https://te.legra.ph/file/a780afd8b5cef866a388d.jpg"


# ❌ WELCOME IMAGE ❌ [EDITABLE]
# from Configs.images import WELCOME_PIC
# WELCOME_IMAGE="./images/start.jpeg"
WELCOME_PIC = "https://i.imgur.com/okNplgz.png"


# ❌ BANNED IMAGE ❌ [EDITABLE]
# from Configs.images import BANNED_PIC
# BANNED_MESSAGE="./images/banned.jpeg"
BANNED_PIC = "https://i.imgur.com/yfUBysD.png"


# ❌ BIG FILE ❌ [EDITABLE]
# from Configs.images import BIG_FILE
#  = "./images/bigFile.jpeg"
BIG_FILE = "https://i.imgur.com/okNplgz.png"


# ❌ Load UsersId with custom thumbnail ❌
CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C = [], []


# file name [if needed]
DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)


#                                                             @nabilanavab
