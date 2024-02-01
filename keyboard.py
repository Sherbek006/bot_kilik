from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove
lang = ReplyKeyboardMarkup(keyboard=[
    [
     KeyboardButton(text="💳 Cilik Premum"),
     KeyboardButton(text="💳Kartalarim"),
    ],
     [
     KeyboardButton(text="💵To'lovlar"),
     KeyboardButton(text="💰Bonuslar"),
     ],
     [
     KeyboardButton(text="📲O'tkazmalar"),
     KeyboardButton(text="🗓 to'lovlar tarixi")
     ],
     [
         KeyboardButton(text="↙️kiruvchi xisoblar"),
         KeyboardButton(text="⭐️Saralangan to'lovlar"),
     ],
     [
         KeyboardButton(text="cilik-hamyoni"),
         KeyboardButton(text="😍 katta keshbek"),
     ],
     [
         KeyboardButton(text="😥menig qarzlarim"),

     ],
     [
         KeyboardButton(text="📍jooylarda to'lov"),
         KeyboardButton(text="🛠 sozlamalar")
     ],
     [
         KeyboardButton(text="☎️ biz bilan aloqa"),
         KeyboardButton(text="🔤 nima yangiliklar")
     ]
    # [
    #    KeyboardButton(text="Contact",request_contact=True)
    # #     KeyboardButton(text='Location',request_location=True)
    # ]
],resize_keyboard=True)