import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboard import lang
from btnlnline import inlineMenu
API_TOKEN = '6789730032:AAFJlfVzUB7KdDjMjOCR14bhyW-5E5jBmws'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def image(message:types.Message):
 for i in range(10):
    await message.answer("Rasm tashlandi")

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def dakument(message:types.Message):
 for i in range(10):
    await message.answer("dakument tashla")


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def VIDEO(message:types.Message):
 for i in range(10):
    await message.answer("vidiyo tashlandi")


@dp.message_handler(content_types=types.ContentType.STICKER)
async def STICKER(message:types.Message):
 for i in range(10):
    await message.answer("vidiyo tashlang")


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def  lakatsiya(message:types.Message):
 for i in range(10):
    await message.answer("lakatsiya  tashlandi")


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def AUDIO(message:types.Message):
 for i in range(10):
    await message.answer("Audio tashlandi")

@dp.message_handler(text ="💳 Cilik Premum")
async def cilik(message: types.Message):
    with open('photo.jpg','rb')as photo:
        await bot.send_photo(photo=photo,chat_id=message.from_user.id,caption="""👑 Click Premium 
Yanada ko'proq cashback, Boom-o'tkazamalar va boshqa noyob takliflar faqat Premium obunachilar uchun
Obuna narxi 50'000 so'm oyiga""",reply_markup=inlineMenu)





    # await message.reply("siz pilastik raqamizni tashlang",reply_markup=inlineMenu)
@dp.callback_query_handler(text='click')
async def callbac(call: types.CallbackQuery):
    await call.message.answer("50 ming senga berildi")
    await call.answer(cache_time=50)




@dp.callback_query_handler(text='order')
async def callback(call: types.CallbackQuery):
    # await call.message.answer("50 ming senga berildi")
    await call.answer(text="Zakaz qabul qilindi",cache_time=50,show_alert=True)








@dp.message_handler(text ="💳Kartalarim")
async def cilik3(message: types.Message):
    await message.reply("nechta bor karta hammasini ulang")


@dp.message_handler(text ="💵To'lovlar")
async def cilik2(message: types.Message):
    await message.reply("nechi pul o'tkazasan insof bilan otagaz")

@dp.message_handler(text ="💰Bonuslar")
async def cilik3(message: types.Message):
    await message.reply("bermaydi bon sani aldaydi")

@dp.message_handler(text ="📲O'tkazmalar")
async def cilik4(message: types.Message):
    await message.reply("menga hammam tashla bir 5 ming")

@dp.message_handler(text ="🗓 to'lovlar tarixi")
async def cilik4(message: types.Message):
    await message.reply("bir qarab qoy qancha ketayabdikan ")


@dp.message_handler(text ="↙️kiruvchi xisoblar")
async def cilik3(message: types.Message):
    await message.reply("qara hoz bir nima bo'ladi")

@dp.message_handler(text ="⭐️Saralangan to'lovlar")
async def cilik3(message: types.Message):
    await message.reply("qimat katta to'lovlar")


@dp.message_handler(text ="cilik-hamyoni")
async def cilik3(message: types.Message):
    await message.reply("Juda qulay ")



@dp.message_handler(text ="😍 katta keshbek")
async def cilik3(message: types.Message):
    await message.reply("huchqachon bermaymiz sizga")


@dp.message_handler(text ="😥menig qarzlarim")
async def cilik3(message: types.Message):
    await message.reply("qachon berasan qarzingni dovdur")


@dp.message_handler(text ="📍jooylarda to'lov")
async def cilik3(message: types.Message):
    await message.reply("lakatsiya yo'q")


@dp.message_handler(text ="🛠 sozlamalar")
async def cilik3(message: types.Message):
    await message.reply("nima bor sozlamada tinchgina ishingni qil")


@dp.message_handler(text ="☎️ biz bilan aloqa")
async def cilik3(message: types.Message):
    await message.reply("qizlar lichga yozsin")


@dp.message_handler(text ="🔤 nima yangiliklar")
async def cilik3(message: types.Message):
    await message.reply("tincha hayot")









@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum tilni tanlang",reply_markup=lang)

@dp.message_handler(commands="help")
async def help(message:types.Message):
    await message.answer("Qanday yordam bera olaman")
# til uz
@dp.message_handler(text = "Uzbek")
async def help(message:types.Message):
    await message.answer("Sen uzbek tilini tanlading")

@dp.message_handler(text = "Ruskiy")
async def help(message:types.Message):
    await message.answer("Sen rus tilini tanlading")

@dp.message_handler(text = "English")
async def help(message:types.Message):
    await message.answer("Sen english tilini tanlading")
 
@dp.message_handler(text = "salom")
async def hello(message:types.Message):
    await message.answer("Assalom alaykum")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)