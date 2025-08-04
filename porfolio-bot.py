from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio


TOKEN = "8381011175:AAHgihFaYTtnxrFCMUAHUdyoOzgiksAtRyQ"
channel_name = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == '/start':
        await start(message)
    elif 'holat' not in user_data[user_id]:
        await ask_phone(message)
    elif message.text == '💻 Projects':
        await projects(message)
    elif message.text == '👨‍💻 Portfolio':
        await portfolio(message)
    elif message.text == '🎯 projects':
        await proects(message)
    elif message.text == '💼 GitHub':
        await git_hub(message)
    elif message.text == '⬅️ Back':
        await ask_phone(message)
    elif message.text == '🧑‍💻 Experience':
        await exp(message)
    elif message.text == '🌐 Turon Telecom':
        await turon(message)
    elif message.text == '🏪 Shop':
        await shop(message)
    elif message.text == '💊 DelaverMed':
        await delaver(message)
    elif message.text == '◀️ Back':
        await exp(message)
    elif message.text == '🧑‍🏫 Education':
        await educate(message)
    elif message.text == '📚 Courses':
        await educate_page(message)
    elif message.text == '🧑‍💻 Ustudy':
        await ustudy(message)
    elif message.text == '🇺🇸 MyStep':
        await mystep(message)
    elif message.text == '➕➖ Galaktika':
        await galaktika(message)
    elif message.text == '🔙 Back':
        await ask_phone(message)
    elif message.text == '📞 Contact':
        await contact(message)
    elif message.text == '📨 Telegram':
        await telegram(message)
    elif message.text == '📸 Instagram':
        await instagram(message)
    elif message.text == "/start":
        await start(message)
    elif message.text == "/contact":
        await contact(message)
    elif message.text == "/projects":
        await projects(message)
    elif message.text == "/experience":
        await exp(message)
    elif message.text == "/education":
        await educate(message)
    elif message.text == '🏀⚽️🥋 Sport':
        await sport(message)
    elif message.text == '⚽️ Football':
        await football(message)
    elif message.text == '🥋 Karate':
        await karate(message)
    elif message.text == '🏀 Bassketball':
        await bassketball(message)
    elif message.text == '♟ Chess':
        await chess(message)
    elif message.text == '🧑🏻‍💻 Mohirdev':
        await mohirdev(message)
    elif message.text == '🤝 Youth Affairs Agency — Assistant':
        await assist(message)
    elif message.text == '🇺🇸 Barkamol Avlod':
        await barkamol(message)
    elif message.text == '🏆 Achievements and Certificates':
        await achievements(message)
    elif message.text == '✅ Kaggle Python Coder Certificate':
        await kaggle(message)
    elif message.text == '✅ Python Programming – Mohirdev':
        await mohir(message)
    elif message.text == '✅ English Certificate – Elementary (MyStep)':
        await mystep_element(message)
    elif message.text == '✅ English Certificate – Pre-Intermediate (MyStep)':
        await mystep_preinter(message)
    elif message.text == '✅ English Course – Barkamol Avlod (Elementary Level)':
        await barkamol_element(message)
    elif message.text == '✅ Python, Data Science and ML – Ustudy Center':
        await ustudy_data(message)
    elif message.text == '🏆 Football Tournament Participation – Kazakhstan':
        await football_tour(message)
    elif message.text == '🏀 Basketball Tournament – 3rd Place (x2)':
        await bassketball_tour(message)
    elif message.text == '♟️ Chess Tournament – 2nd Place':
        await chess_tour(message)
    elif message.text == '🥋 Karate Tournament – 1st & 2nd Place (City Level)':
        await karate_tour(message)
    elif message.text == '🥋 White Belt Stripes (Nasadka) Certification – Karate':
        await karate_white(message)
    elif message.text == '🟦 Blue Belt – Karate Certification':
        await karate_blue(message)
    elif message.text == '🏫 School':
        await school(message)
    elif message.text == '🗣️🧠🤝 Ibrat Debate':
        await ibrat(message)
    elif message.text == '🟨 Participation Certificate – Ibrat Debate Camp':
        await ibrat_debate(message)





@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇺🇸 English")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Hello! With this bot, you can explore Mirzakhmedov Mirazim's portfolio.😊", reply_markup=keyboard)
    print(user_data)


async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    user_data[user_id]['holat'] = language
    button = [
        [types.KeyboardButton(text='💻 Projects'), types.KeyboardButton(text='🧑‍💻 Experience')],
        [types.KeyboardButton(text='🧑‍🏫 Education'), types.KeyboardButton(text='🏀⚽️🥋 Sport')],
        [types.KeyboardButton(text='🏆 Achievements and Certificates'), types.KeyboardButton(text='📞 Contact')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Select one of the following buttons:\n\n"
                         "💻 Projects — Check out my projects.\n\n"
                         "🧑‍💻 Experience — Learn about my experience.\n\n"
                         "🧑‍🏫 Education — Learn about my education background.\n\n"
                         "🏀⚽️🥋 Sport  —  Discover my sports journey\n\n"
                         "🏆 Achievements and Certificates — My key accomplishments backed by official certificates.\n\n"
                         "📞 Contact — View my contacts.", reply_markup=keyboard)
    print(user_data)




async def projects(message: types.Message):
    user_id = message.from_user.id
    projects = message.text
    user_data[user_id]['projects'] = projects
    button = [
        [types.KeyboardButton(text='👨‍💻 Portfolio'), types.KeyboardButton(text='🎯 projects')],
        [types.KeyboardButton(text='💼 GitHub'), types.KeyboardButton(text='⬅️ Back')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/projects.jpg"
    caption_text = ("🧑‍💻 Here you can explore my projects")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)



async def portfolio(message: types.Message):
    user_id = message.from_user.id
    portfolio = message.text
    user_data[user_id]["portfolio"] = portfolio
    button = [
        [types.InlineKeyboardButton(text="Link", url='http://project13732653.tilda.ws')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "projects/portfolio.png"
    caption_text = ("By clicking this button, you will access my portfolio website\n"
                    "👇👇👇👇")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    print(user_data)



async def proects(message: types.Message):
    user_id = message.from_user.id
    proects = message.text
    user_data[user_id]["proects"] = proects
    button = [
        [types.InlineKeyboardButton(text="House price prediction", url='https://github.com/DeAdPoOl-01/housing-new-price-prediction'), types.InlineKeyboardButton(text="Car price prediction", url='https://github.com/DeAdPoOl-01/cars-prediction')],
        [types.InlineKeyboardButton(text="LesAiles Telegram Bot",url='https://github.com/DeAdPoOl-01/Lesailes_bot/blob/main/tg_bot/les.py'), types.InlineKeyboardButton(text="Register Telegram Bot", url='https://github.com/DeAdPoOl-01/registration/blob/main/register.py')],
        [types.InlineKeyboardButton(text="Book Scrapy from Amazon",url='https://github.com/DeAdPoOl-01/boo-scrapy-from-Amazon/blob/main/scrapy'), types.InlineKeyboardButton(text="Laptop Scrapy from Amazon", url='https://github.com/DeAdPoOl-01/Laptop-scrapy-from-Amazon/blob/main/scrapy')],
        [types.InlineKeyboardButton(text="Housing RandomFrorest",url='https://github.com/DeAdPoOl-01/housing-RandomForest'), types.InlineKeyboardButton(text="Diabetes Classification", url='https://github.com/DeAdPoOl-01/diabetes-classification')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "projects/proects.jpg"
    caption_text = ("🗂 Through GitHub, you can explore the code of my projects\n"
                    "Click the link below to open GitHub:\n"
                    "👇👇👇👇")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    print(user_data)




async def git_hub(message: types.Message):
    user_id = message.from_user.id
    git_hub = message.text
    user_data[user_id]["git_hub"] = git_hub
    button = [
        [types.InlineKeyboardButton(text="Link", url='https://github.com/DeAdPoOl-01')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "projects/Git Hub.jpg"
    caption_text = ("🧑‍💻 Here you can explore my projects")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    print(user_data)



async def exp(message: types.Message):
    user_id = message.from_user.id
    exp = message.text
    user_data[user_id]["exp"] = exp
    button = [
        [types.KeyboardButton(text='🌐 Turon Telecom'), types.KeyboardButton(text='🏪 Shop')],
        [types.KeyboardButton(text='💊 DelaverMed'), types.KeyboardButton(text='🤝 Youth Affairs Agency — Assistant')],
        [types.KeyboardButton(text='⬅️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Experience.jpg"
    caption_text = ("🗂 In this section, you will learn about my work experience."
                    "Click the buttons to get more details."
                    "👇👇👇👇👇👇")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)



async def turon(message: types.Message):
    user_id = message.from_user.id
    turon = message.text
    user_data[user_id]["turon"] = turon
    button = [
        [types.KeyboardButton(text='◀️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Turon.png"
    caption_text = ("🌐 Turon Telecom\n"
                    "2024🗓\n"
                    "Position: Sales Agent.\n"
                    "Worked in the sales team, providing customer consultations, promoting telecom services, and handling service subscriptions. Gained hands-on experience in client communication, sales techniques, and negotiation skills.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)



async def shop(message: types.Message):
    user_id = message.from_user.id
    shop = message.text
    user_data[user_id]["shop"] = shop
    button = [
        [types.KeyboardButton(text='◀️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Shop.jpg"
    caption_text = ("🏪 Shop\n"
                    "2023🗓\n"
                    "Position: Sales Manager.\n"
                    "Handled customer service, provided product consultations, assisted with purchases, and maintained store displays. Participated in inventory management and daily operations. Gained valuable experience in retail sales and customer interaction.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)



async def delaver(message: types.Message):
    user_id = message.from_user.id
    delaver = message.text
    user_data[user_id]["delaver"] = delaver
    button = [
        [types.KeyboardButton(text='◀️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Delaver.jpg"
    caption_text = ("💊 DelaverMed\n"
                    "2024-2025🗓\n"
                    "Position: Sales Manager.\n"
                    "Worked in a pharmaceutical company, handling sales of medical products and consulting clients. Maintained communication with pharmacies and healthcare organizations, processed orders, and managed documentation. Gained experience in B2B sales, healthcare product knowledge, and professional communication.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)

async def assist(message: types.Message):
    user_id = message.from_user.id
    assist = message.text
    user_data[user_id]["assist"] = assist
    button = [
        [types.KeyboardButton(text='◀️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/asist.png"
    caption_text = ("🤝 Youth Affairs Agency — Assistant\n"
                    "2024🗓\n"
                    "Position: Assistant.\n"
                    "Assisted in organizing youth programs and events, supported communication with participants, and helped coordinate local initiatives. Gained valuable experience in public service, documentation, and youth engagement.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)




async def educate(message: types.Message):
    user_id = message.from_user.id
    educate = message.text
    user_data[user_id]["educate"] = educate
    button = [
        [types.KeyboardButton(text='📚 Courses'), types.KeyboardButton(text='⬅️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Education.jpg"
    caption_text = ("In this section, you can learn about the educational institutions I attended and the courses I completed, as well as explore my personal and technical skills. 🧑‍💻if you want to know more information click the buttons below:👇👇👇👇👇👇")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)



async def educate_page(message: types.Message):
    user_id = message.from_user.id
    educate_page = message.text
    user_data[user_id]["educate_page"] = educate_page
    button = [
        [types.KeyboardButton(text='🧑‍💻 Ustudy'), types.KeyboardButton(text='🇺🇸 MyStep')],
        [types.KeyboardButton(text='➕➖ Galaktika'), types.KeyboardButton(text='🇺🇸 Barkamol Avlod')],
        [types.KeyboardButton(text='🧑🏻‍💻 Mohirdev'), types.KeyboardButton(text='🗣️🧠🤝 Ibrat Debate')],
        [types.KeyboardButton(text='🔙 Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/Education.jpg"
    caption_text = ("📚 Detailed information about the courses I have taken")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)




async def ustudy(message: types.Message):
    user_id = message.from_user.id
    ustudy = message.text
    user_data[user_id]["ustudy"] = ustudy
    file_path = "projects/ustudy.jpg"
    caption_text = ("💻 Ustudy: Python AI\n\n"
                    "2024–2025 📆\n\n"
                    "At the Ustudy learning center, I studied Python programming,data analysis and artificial intelligence.The course was practice-oriented and helped me work on real projects.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)



async def mystep(message: types.Message):
    user_id = message.from_user.id
    mystep = message.text
    user_data[user_id]["mystep"] = mystep
    file_path = "projects/mystep.png"
    caption_text = ("🇺🇸 MyStep\n"
                    "2023-2025📆\n"
                    "MyStep Online School — English Language Course\n"
                    "Completed several levels of English training:\n"
                    "— Elementary (A1–A2)\n"
                    "— Pre-Intermediate (A2–B1)\n"
                    "— Currently at Intermediate level (B1)\n"
                    "The course included grammar, reading, listening, and speaking practice. I continue to improve my language skills through regular learning.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)



async def galaktika(message: types.Message):
    user_id = message.from_user.id
    galaktika = message.text
    user_data[user_id]["galaktika"] = galaktika
    file_path = "projects/galaktika.jpg"
    caption_text = ("➕➖ Galaktika\n"
                    "2024–2025 📆\n"
                    "Currently enrolled in a mathematics course covering algebra, functions, probability, and fundamentals of calculus. The program supports my growth in Data Science and Machine Learning by strengthening my mathematical foundation.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)

async def mohirdev(message: types.Message):
    user_id = message.from_user.id
    mohirdev = message.text
    user_data[user_id]["mohirdev"] = mohirdev
    file_path = "projects/mohirdev.png"
    caption_text = ("🧑🏻‍💻 Mohirdev\n"
                    "Mohirdev — Python Course\n"
                    "2022 📆\n"
                    "I completed a Python course on the Mohirdev platform, where I learned the fundamentals of the language, including variables, loops, functions, modules, and object-oriented programming. The course included hands-on exercises that helped me strengthen my core and intermediate programming skills.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)

async def barkamol(message: types.Message):
    user_id = message.from_user.id
    barkamol = message.text
    user_data[user_id]["barkamol"] = barkamol
    file_path = "projects/barkamol.png"
    caption_text = ("🇺🇸 Barkamol Avlod\n"
                    "Barkamol Avlod — English Language Course\n"
                    "2021-2022 📆\n"
                    "I studied English at the Barkamol Avlod extracurricular education center. During the course, I gained basic knowledge of grammar, vocabulary, and everyday communication. By the end of the program, I had reached the Elementary (A1–A2) level.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)

async def ibrat(message: types.Message):
    user_id = message.from_user.id
    ibrat_debate = message.text
    user_data[user_id]["ibrat_debate"] = ibrat_debate
    file_path = "projects/ibrat.jpg"
    caption_text = ("➕➖ Ibrat Debate Camp\n"
                    "July 2025 📆\n"
                    "I took part in the Ibrat Debate Camp, a youth educational program aimed at developing public speaking, logical reasoning, and English communication skills through structured debates and interactive workshops.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',)
    print(user_data)

async def sport(message: types.Message):
    user_id = message.from_user.id
    sport = message.text
    user_data[user_id]["sport"] = sport
    button = [
        [types.KeyboardButton(text='⚽️ Football'), types.KeyboardButton(text='🥋 Karate')],
        [types.KeyboardButton(text='🏀 Bassketball'), types.KeyboardButton(text='♟ Chess')],
        [types.KeyboardButton(text='🔙 Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/sport.jpg"
    caption_text = ("🏅 Detailed Overview of My Sports Training, Achievements, and Motivation")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)

async def football(message: types.Message):
    user_id = message.from_user.id
    football = message.text
    user_data[user_id]["football"] = football
    file_path = "projects/futbol.jpg"
    caption_text = ("⚽ Football\n"
                    "I started playing football at the age of 6 and trained seriously for many years.\n"
                    "I was a member of several youth academies, including EdenSport, OdilJunior, and Bunyodkor — some of the most well-known youth football clubs in Uzbekistan.\n"
                    "Thanks to football, I had the opportunity to travel to Kazakhstan with my team to participate in an international tournament, which gave me invaluable experience competing at a higher level.\n"
                    "I also took part in multiple training camps, where I improved my teamwork, discipline, and tactical understanding of the game.\n"
                    "Football taught me how to stay focused, push my limits, and work closely with others — all of which now help me in professional and academic life.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def bassketball(message: types.Message):
    user_id = message.from_user.id
    bassketball = message.text
    user_data[user_id]["bassketball"] = bassketball
    file_path = "projects/basketbal.jpg"
    caption_text = ("🏀 Basketball\n"
                    "I began playing basketball at the age of 14 and quickly grew passionate about the sport.\n"
                    "I participated in several local tournaments and school-level competitions, where I earned 3rd place twice with my team.\n"
                    "Through basketball, I developed strong skills in team coordination, strategic thinking, and quick decision-making under pressure.\n"
                    "The game taught me how to adapt fast, support my teammates, and stay resilient even in tough situations.\n"
                    "These lessons continue to influence how I approach collaboration and problem-solving in other areas of life.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def karate(message: types.Message):
    user_id = message.from_user.id
    karate = message.text
    user_data[user_id]["karate"] = karate
    file_path = "projects/karate.jpg"
    caption_text = ("🥋 Karate\n"
                    "I started practicing karate at the age of 12 and trained consistently for several years.\n"
                    "During this time, I participated in various city and regional tournaments, where I earned 1st and 2nd place in different categories.\n"
                    "I successfully passed multiple belt examinations, and I currently hold a blue belt, which reflects my technical skills and dedication to the discipline.\n"
                    "Karate has taught me focus, patience, self-control, and the importance of continuous improvement — qualities that I now apply in both personal and professional areas of my life.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def chess(message: types.Message):
    user_id = message.from_user.id
    chess = message.text
    user_data[user_id]["chess"] = chess
    file_path = "projects/ches.jpg"
    caption_text = ("♟️ Chess\n"
                    "I began playing chess at the age of 13 and quickly became fascinated by its strategic depth and mental challenge.\n"
                    "I participated in several local tournaments, where I achieved a 2nd place finish in one of the competitions.\n"
                    "Chess helped me strengthen my analytical thinking, patience, and decision-making skills, all of which have proven valuable in programming, data science, and everyday life.\n"
                    "This intellectual sport continues to influence how I approach complex problems and think several steps ahead.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def achievements(message: types.Message):
    user_id = message.from_user.id
    achievements = message.text
    user_data[user_id]["achievements"] = achievements
    button = [
        [types.KeyboardButton(text='✅ Kaggle Python Coder Certificate'), types.KeyboardButton(text='✅ Python Programming – Mohirdev')],
        [types.KeyboardButton(text='✅ English Certificate – Elementary (MyStep)'), types.KeyboardButton(text='✅ English Certificate – Pre-Intermediate (MyStep)')],
        [types.KeyboardButton(text='✅ English Course – Barkamol Avlod (Elementary Level)'), types.KeyboardButton(text='✅ Python, Data Science and ML – Ustudy Center')],
        [types.KeyboardButton(text='🏆 Football Tournament Participation – Kazakhstan'), types.KeyboardButton(text='🏀 Basketball Tournament – 3rd Place (x2)')],
        [types.KeyboardButton(text='♟️ Chess Tournament – 2nd Place'), types.KeyboardButton(text='🥋 Karate Tournament – 1st & 2nd Place (City Level)')],
        [types.KeyboardButton(text='🥋 White Belt Stripes (Nasadka) Certification – Karate'), types.KeyboardButton(text='🟦 Blue Belt – Karate Certification')],
        [types.KeyboardButton(text='🏫 School'), types.KeyboardButton(text='🟨 Participation Certificate – Ibrat Debate Camp')],
        [types.KeyboardButton(text='🔙 Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    file_path = "projects/sport.jpg"
    caption_text = ("🏅 Detailed Overview of My Sports Training, Achievements, and Motivation")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown',
                              reply_markup=keyboard)
    print(user_data)

async def kaggle(message: types.Message):
    user_id = message.from_user.id
    kaggle = message.text
    user_data[user_id]["kaggle"] = kaggle
    file_path = "projects/kaggle.jpg"
    caption_text = ("🧑🏻‍💻 Kaggle\n"
                    "I actively use Kaggle — the world’s largest platform for data science competitions and learning.\n"
                    "On Kaggle, I completed various Python and Data Science courses, earning the Kaggle Python Coder Certificate.\n")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def mohir(message: types.Message):
    user_id = message.from_user.id
    mohir = message.text
    user_data[user_id]["mohir"] = mohir
    file_path = "projects/mohirdev.jpg"
    caption_text = ("💻 Mohirdev — Python Basics Course\n"
                    "I completed the Python basics course on the Mohirdev platform, where I learned the core concepts of programming in my native language.\n"
                    "The course covered:\n\n"
                    "— Variables and data types\n\n"
                    "— Basic logic and syntax\n\n"
                    "— Simple projects and hands-on practice\n\n"
                    "This course helped me build a strong foundation in Python and start working on real projects confidently.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def mystep_element(message: types.Message):
    user_id = message.from_user.id
    mystep_element = message.text
    user_data[user_id]["mystep_element"] = mystep_element
    file_path = "projects/mystep_element.png"
    caption_text = ("📘 English – Elementary Level (MyStep Online School)\n"
                    "I completed the Elementary level (A1–A2) English course at MyStep Online School, where I gained fundamental skills in:\n"
                    "— Reading and understanding simple texts\n\n"
                    "— Writing basic sentences and short messages\n\n"
                    "— Listening to everyday conversations\n\n"
                    "— Speaking about familiar topics like daily life, family, and hobbies\n\n"
                    "This certificate confirms my ability to communicate in English at the elementary level, providing a strong base for continued language learning.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def mystep_preinter(message: types.Message):
    user_id = message.from_user.id
    mystep_preinter = message.text
    user_data[user_id]["mystep_preinter"] = mystep_preinter
    file_path = "projects/mystep_inter.png"
    caption_text = ("📘 English – Pre-Intermediate Level (MyStep Online School)\n"
                    "I successfully completed the Pre-Intermediate (A2–B1) English course at MyStep, where I improved my language skills in:\n"
                    "— Reading and understanding short articles and everyday texts\n\n"
                    "— Writing simple paragraphs and informal emails\n\n"
                    "— Listening to conversations and short talks.\n\n"
                    "— Speaking about daily routines, opinions, and personal experiences\n\n"
                    "This level helped me move beyond the basics and communicate more confidently in real-life situations, laying the groundwork for my Intermediate studies.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def barkamol_element(message: types.Message):
    user_id = message.from_user.id
    barkamol_element = message.text
    user_data[user_id]["barkamol_element"] = barkamol_element
    file_path = "projects/barkamol_element.png"
    caption_text = ("📗 English Course – Barkamol Avlod (Elementary Level)\n"
                    "I studied Elementary level English (A1–A2) at Barkamol Avlod, a youth development center in Uzbekistan.\n"
                    "The course focused on:\n\n"
                    "— Basic grammar and vocabulary\n\n"
                    "— Everyday communication\n\n"
                    "— Reading short texts and dialogues\n\n"
                    "— Introduction to listening and speaking skills\n\n"
                    "This foundational course gave me the confidence to continue learning English and improve my communication abilities in both academic and daily contexts.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def ustudy_data(message: types.Message):
    user_id = message.from_user.id
    ustudy_data = message.text
    user_data[user_id]["ustudy_data"] = ustudy_data
    file_path = "projects/ustudy.png"
    caption_text = ("💻 Ustudy Center – Python & Machine Learning Track\n"
                    "I am currently studying Python, Data Science, and Machine Learning at Ustudy Center, a modern education hub located within Uzinfocom in Tashkent.\n"
                    "The program covers:\n\n"
                    "— Python programming fundamentals\n\n"
                    "— Data analysis and visualization\n\n"
                    "— Machine learning algorithms and model building\n\n"
                    "— Practical tasks and hands-on projects\n\n"
                    "This course helps me strengthen my technical skills and apply them to real-world problems in AI and data science.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def ibrat_debate(message: types.Message):
    user_id = message.from_user.id
    ibrat_debate = message.text
    user_data[user_id]["ibrat_debate"] = ibrat_debate
    file_path = "projects/ibrat_debate.jpg"
    caption_text = ("🟨 Participation Certificate – Ibrat Debate Camp\n"
                    "Date: July 2025\n"
                    "Organizer: Ibrat Farzandlari"
                    "I took part in the Ibrat Debate Camp, a youth educational program aimed at developing public speaking, logical reasoning, and English communication skills through structured debates and interactive workshops.\n"
                    "This experience reflects:\n\n"
                    "— Active participation in English-language debates and team discussions\n\n"
                    "— Development of critical thinking and argumentation skills\n\n"
                    "— Collaboration with peers in an intellectually stimulating environment\n\n"
                    "— Exposure to international-style debate formats (e.g., British Parliamentary, Lincoln-Douglas)\n\n"
                    "Participating in the camp enhanced my confidence in public speaking, improved my ability to express complex ideas clearly, and strengthened my teamwork and leadership abilities.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def football_tour(message: types.Message):
    user_id = message.from_user.id
    football_tour = message.text
    user_data[user_id]["football_tour"] = football_tour
    file_path = "projects/footbal_tour.png"
    caption_text = ("🏆 Football Tournament – Kazakhstan Participation\n"
                    "I took part in an international youth football tournament in Kazakhstan as a member of my team.\n"
                    "This experience gave me the opportunity to:\n\n"
                    "— Represent my club on an international level\n\n"
                    "— Compete with strong teams from other countries\n\n"
                    "— Develop teamwork, discipline, and competitive spirit\n\n"
                    "— Visit sports camps and gain valuable experience off the field\n\n"
                    "This tournament was a key moment in my early sports journey and strengthened my passion for football.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def bassketball_tour(message: types.Message):
    user_id = message.from_user.id
    bassketball_tour = message.text
    user_data[user_id]["bassketball_tour"] = bassketball_tour
    file_path = "projects/bassketball3place.jpg"
    caption_text = ("🏀 Basketball Tournaments – Double 3rd Place Winner\n"
                    "I began playing basketball at the age of 14 and actively participated in local school and city tournaments.\n"
                    "This experience gave me the opportunity to:\n\n"
                    "— Improve my physical endurance and coordination\n\n"
                    "— Develop strong teamwork and leadership skills\n\n"
                    "— Gain competitive experience through real matches\n\n"
                    "— Earn 3rd place in two official competitions\n\n"
                    "These achievements motivated me to continue pushing my limits in sports and taught me the value of consistency, effort, and team spirit.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)

async def chess_tour(message: types.Message):
    user_id = message.from_user.id
    chess_tour = message.text
    user_data[user_id]["chess_tour"] = chess_tour
    file_path1 = "projects/chess3place.jpg"
    file_path2 = "projects/chess3place.jpg"
    caption_text = ("♟️ Chess Tournament – 3nd Place\n"
                    "I started learning chess at the age of 13, driven by curiosity and a passion for strategic thinking.\n"
                    "This experience gave me the opportunity to:\n\n"
                    "— Improve focus, patience, and decision-making skills\n\n"
                    "— Learn to analyze situations and plan several moves ahead\n\n"
                    "— Participate in various local tournaments\n\n"
                    "— Achieve 3nd place in a regional chess competition\n\n"
                    "Chess has helped me develop critical thinking and discipline, which I apply not only in games but also in learning and problem-solving.")
    await message.reply_photo(photo=types.FSInputFile(path=file_path1), parse_mode='Markdown')
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path2), parse_mode='Markdown')
    print(user_data)

async def karate_tour(message: types.Message):
    user_id = message.from_user.id
    karate_tour = message.text
    user_data[user_id]["karate_tour"] = karate_tour
    file_path1 = "projects/karate1place.jpg"
    file_path2 = "projects/karate2place.jpg"
    caption_text = ("🥋 Karate Tournament – 1st & 2nd Place (City Level)\n"
                    "I began practicing karate at the age of 12, driven by a passion for martial arts and self-discipline.\n"
                    "This journey gave me the opportunity to:\n\n"
                    "— Participate in city and regional tournaments\n\n"
                    "— Win 1st and 2nd place in several competitions\n\n"
                    "— Improve physical strength, reflexes, and mental focus\n\n"
                    "— Pass multiple belt exams and earn the blue belt\n\n"
                    "— Complete early-level assessments (white belt stripes)\n\n"
                    "Karate taught me the values of perseverance, respect, and continuous improvement — both on and off the mat.")
    await message.reply_photo(photo=types.FSInputFile(path=file_path1), parse_mode='Markdown')
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path2), parse_mode='Markdown')
    print(user_data)

async def karate_white(message: types.Message):
    user_id = message.from_user.id
    karate_white = message.text
    user_data[user_id]["karate_white"] = karate_white
    file_path1 = "projects/karate_white10.jpg"
    file_path2 = "projects/karate_white10_dan.jpg"
    file_path3 = "projects/karate_white9.jpg"
    file_path4 = "projects/karate_white9_dan.jpg"
    caption_text = ("🥋 White Belt Stripes Certification – Karate\n"
                    "At the beginning of my karate journey, I successfully passed the belt stripe (nasadka) examinations for the white belt level.\n"
                    "This early achievement helped me:\n\n"
                    "— Build foundational skills in movement, technique, and form\n\n"
                    "— Understand dojo discipline and respect-based training\n\n"
                    "— Gain confidence to advance through further belt levels\n\n"
                    "— Lay the groundwork for earning my blue belt\n\n"
                    "These first steps marked the start of my progress in martial arts and encouraged me to keep improving with every level.")
    await message.reply_photo(photo=types.FSInputFile(path=file_path1), parse_mode='Markdown')
    await message.reply_photo(photo=types.FSInputFile(path=file_path2), parse_mode='Markdown')
    await message.reply_photo(photo=types.FSInputFile(path=file_path3), parse_mode='Markdown')
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path4), parse_mode='Markdown')
    print(user_data)

async def karate_blue(message: types.Message):
    user_id = message.from_user.id
    karate_blue = message.text
    user_data[user_id]["karate_blue"] = karate_blue
    file_path1 = "projects/karate_white8.jpg"
    file_path2 = "projects/karate_white8_dan.jpg"
    caption_text = ("🟦 Blue Belt – Karate Certification\n"
                    "After consistent training and multiple examinations, I earned the blue belt in karate — a milestone that reflects both physical progress and mental discipline.\n"
                    "This achievement represents:\n\n"
                    "— Mastery of key techniques and advanced combinations\n\n"
                    "— Strong understanding of kata, stances, and sparring methods\n\n"
                    "— Commitment to regular training and personal growth\n\n"
                    "— Participation in tournaments and progression beyond beginner level\n\n"
                    "Earning the blue belt is a proud moment in my martial arts journey and a symbol of dedication, perseverance, and self-improvement.")
    await message.reply_photo(photo=types.FSInputFile(path=file_path1), parse_mode='Markdown')
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path2), parse_mode='Markdown')
    print(user_data)

async def school(message: types.Message):
    user_id = message.from_user.id
    school = message.text
    user_data[user_id]["school"] = school
    file_path = "projects/school.jpg"
    caption_text = ("📖 Certificate: Best Reader of the School Library\n"
                    "After showing a strong passion for reading and consistent engagement with school literature, I was awarded the Best Reader certificate by my school library in 2nd grade.\n"
                    "This achievement reflects:\n\n"
                    "— A deep interest in literature from an early age\n\n"
                    "— Active participation in library activities\n\n"
                    "— Regular reading and exploration of new books\n\n"
                    "— Recognition by teachers for curiosity and enthusiasm\n\n"
                    "Receiving this award marked the beginning of my journey as a lifelong learner and reader. It symbolizes not only academic initiative but also the joy of discovering the world through books.")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown')
    print(user_data)






async def contact(message: types.Message):
    user_id = message.from_user.id
    contact = message.text
    user_data[user_id]["contact"] = contact
    button = [
        [types.KeyboardButton(text='📨 Telegram'), types.KeyboardButton(text='📸 Instagram')],
        [types.KeyboardButton(text='⬅️ Back')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("You can contact me through the following platforms. Please choose one of the buttons:👇👇👇👇", reply_markup=keyboard)
    print(user_data)




async def telegram(message: types.Message):
    user_id = message.from_user.id
    telegram = message.text
    user_data[user_id]["telegram"] = telegram
    await message.answer("To contact me, use the following details:@DeAdpOl_01 ✉️\n"
                         "Phone number: +998-90-187-01-88 ☎️")
    print(user_data)



async def instagram(message: types.Message):
    user_id = message.from_user.id
    instagram = message.text
    user_data[user_id]["instagram"] = instagram
    button = [
        [types.InlineKeyboardButton(text="Link", url='https://www.instagram.com/m.mirzak1medov/')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "projects/instagram.jpg"
    caption_text = ("📸 Instagram Link\n"
                    "Click the link below to open Instagram:"
                    "👇👇👇👇")
    await message.reply_photo(caption=caption_text, photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    print(user_data)





async def main():
    await dp.start_polling(bot)



print("The bot is running...")
asyncio.run(main())
