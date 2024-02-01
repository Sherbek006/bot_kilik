from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inlineMenu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='oyiga 50 ming som',callback_data='cilic'),
     InlineKeyboardButton(text='asalom hammaga',callback_data='text')
     ],
     [
         InlineKeyboardButton(text='Search',switch_inline_query_current_chat='')
     ],
     [
         InlineKeyboardButton(text='Ulashish',switch_inline_query=''),
         InlineKeyboardButton(text="Youtube",url="https://youtube.com/")
     ]
])