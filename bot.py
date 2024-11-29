from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError
import logging
from datetime import datetime
import random
from dotenv import load_dotenv
import os
import unicodedata

load_dotenv()  # Load variables from the .env file
token = os.getenv("BOT_TOKEN")
if not token:
    logging.critical("BOT_TOKEN not found. Exiting application.")
    exit(1)

# Configure logging to log to a file
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot_logs.txt"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console as well
    ]
)
logging.getLogger("httpx").setLevel(logging.WARNING)  # Suppress httpx logs

# Create the Application instance
application = Application.builder().token(token).build()

async def log_interaction(update: Update, response: str = None):
    user = update.effective_user
    username = user.username if user and user.username else "Unknown"
    user_text = update.message.text if update.message else "No text"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"[{timestamp}] User: {username}, Text: '{user_text}', Bot Response: '{response or 'None'}'")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error("Exception occurred:", exc_info=context.error)
    if update and update.effective_user:
        try:
            await update.message.reply_text("Oops! Something went wrong. Please try again later.")
        except TelegramError:
            logging.error("Failed to send error message to user.")

# All Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username if update.effective_user.username else "there"
    response = f"""
Hello *@{username}*!

Use */help* for all useful commands.

⚠️ *Important:* Read */privacypolicy* before continuing to the bot.

⚠️ *Note:* This bot is under development. Expect occasional errors or downtime.
"""
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*/start* - Start the bot.
*/help* - List all commands.
*/hello* - Start a good conversation.
*/about* - All about me.
*/biharlife* - About my Bihar life.
*/schoollife* - About my School life.
*/techjourney* - About my Tech journey.
*/socialmedia* - Get social media links.
*/contact* - Contact me.
*/privacypolicy* - Important to read before starting with bot.
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    replies = [
        "I am Aryan Raj!",
        "Hey there! How can I assist you today?",
        "What's up? Hope you're doing great!",
        "Hello! Nice to see you here.",
        "Hi! How's it going?",
        "Greetings! Need any help?",
        "Hehe!",
        "🤫",
        "Hello?",
        "Yes!",
        "2+2 != 5",
        "🐍",
        "🎂 2024/11/24 🎂",
        "I love India",
        "Hi"
    ]
    response = random.choice(replies)  # Select a random reply
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username if update.effective_user.username else "there"
    response = f"""
Hi *@{username}*!

It's me *Aryan Raj* from lovely India ❤️
In India I am from Bihar and I am *proud to be Bihari* 😌
use */biharlife* for more info.

I am student at Kendriya Vidyalaya. I am in 10th grade.
use */schoollife* for more info.

I love computers and tech.
That's why I am too interested in coding & programming. And you can see the result in this bot created on python 🐍
use */techjourney* for more info.

Use */socialmedia* to get my all Social Media Links.

That's all I think about me.
Have a great day ✨

*Aryan 🙃*
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def biharlife(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*Bihar Life*

Adding Soon... ⌨️
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def schoollife(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*School Life*

I am in 10th grade right now at Kendriya Vidyalaya.
It's a lovely school. It's infrastructure is really awesome.

I have many supportive friends.
We do fun all day in the classroom. We eat each other's lunches.
Sometimes we do fight but we get back soon 😄

Our class teacher is very good. He is a Maths teacher.
Sometimes he makes us bored 🥱 
But he teaches very well.

And you know an interesting fact, I am the tallest boy in my class 😏
I sit at the back bench. Yeah 😌 I am back bencher.
My bench partner and I eat all our friends lunch 😁. You can say that we are foody guys.

And about my academics. I am an average student. I can be a topper but I don't study that much 🙂. I perform well in my exams.

*More about my schooling:*
I did 1st-6th grade from Kendriya Vidyalaya, Ara
And 7th-till now 10th grade from Kendriya Vidyalaya, Sasaram.
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def techjourney(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*Tech Journey*

I started coding in 7th grade. In 7th grade our computer teacher started teaching us HTML & CSS. At that time I got interested in coding.
I had a Lenovo Tablet. In which I started coding HTML codes. And on YouTube and the internet I started surfing about HTML and started learning from there.
I was too fast from my computer teacher syllabus. I learnt the whole HTML. Before she started CSS, I already completed it 😎.

Then I made some projects on Bootstrap. And started making the whole website from basic. 

And in 8th grade, I said to my parents to buy a keyboard and a mouse for coding. Then they bought it for me.
It was a big boost for me. After that I started making many websites and learning more.

After sometime I learnt Python from the Apna College YouTube channel. I want to thank Sharadha Didi for teaching me Python.

*This is the video link of that Python video: https://youtu.be/vLqTf2b6GZw?si=-9ZQwhnel82U0kNa*

And then I started making projects in Python.


More... Adding Soon ⌨️
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def socialmedia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*Social Media Links*

*Instagram:* https://www.instagram.com/aryan\_raj\_7167
*Telegram:* https://t.me/aryan\_raj\_7167
*Discord:* https://discord.gg/gQS7Jp2Q
*QQ:* https://qm.qq.com/q/Pvcjmaf7gq

*Other:*

*Email:* aryanraj7167ar@gmail.com
*GitHub:* https://github.com/dev-aryan-com
*Slowly:* 2NNQLJL

Use */about* to know more about me.
"""
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*Contact Me*

**@aryan\_raj\_7167**

*Email:* aryanraj7167ar@gmail.com 
*Social Media:* /socialmedia
    """
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

async def privacypolicy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = """
*Privacy Policy*

https://www.aryan-raj-7167-bot.html-5.me/privacypolicy/
	"""
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

# Handle unknown commands
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = "Sorry, I didn't understand that command. Use */help*"
    await update.message.reply_text(response, parse_mode='Markdown')
    await log_interaction(update, response)

def is_emoji(character):
    """Check if a character is an emoji."""
    try:
        return unicodedata.name(character).startswith("EMOJI") or \
               "FACE" in unicodedata.name(character) or \
               unicodedata.category(character) in ['So', 'Sk']
    except ValueError:
        return False

def categorize_input(user_message):
    has_text = False
    has_emoji = False

    for char in user_message:
        if is_emoji(char):
            has_emoji = True
        elif char.isprintable() and not char.isspace():
            has_text = True

    if has_text and has_emoji:
        return "Mixed"
    elif has_text:
        return "Text"
    elif has_emoji:
        return "Emoji"
    else:
        return "Unknown"

# All questions
name = [
    "name?",
    "what's your name?",
    "what is your name?",
    "may I know your name?",
    "can you tell me your name?",
    "who are you?",
    "what should I call you?",
    "how should I address you?",
    "do you have a name?",
    "what's your full name?",
    "what is your first name?",
    "what is your last name?",
    "who am I talking to?",
    "may I ask your name?",
    "what's your nickname?",
    "what do people call you?",
    "what's the meaning of your name?"
]

age = [
    "age?",
    "what's your age?",
    "how old are you?",
    "may I ask your age?",
    "can you tell me your age?",
    "how many years old are you?",
    "what is your birth year?",
    "when were you born?",
    "what age group do you belong to?",
    "are you under 18?",
    "are you over 18?",
    "are you in your twenties?",
    "are you older than me?",
    "are you younger than me?",
    "which age category are you in?",
    "how old do you look?",
    "what age do you feel?",
    "are you a minor?",
    "are you middle-aged?",
    "are you a senior citizen?",
    "how long have you been alive?"
]

# Handle specific text messages
async def log_other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()  # Convert to lowercase for case-insensitive matching
    response = None  # Default response is None
    user_emoji = categorize_input(user_message)
    username = update.effective_user.username if update.effective_user.username else "there"
    
    # Define responses to specific messages
    if user_emoji == "Emoji":
        response = user_message
    elif user_message == "hi":
        await hello(update, context)
        return
    elif user_message == "hello":
        await hello(update, context)
        return
    elif user_message == "how are you?":
        response = f"""
I'm just a bot, but I'm functioning perfectly! 🤖
How about you @{username}?
        """
    else:
        user_message = user_message.strip().rstrip('?') + '?'
        if user_message in name:
            response = """
I'm *Aryan Raj*

Use */about* to know more about me.
            """
        elif user_message in age:
            response = "I'm *16*!"
        else:
            response = """I see you sent some text!
I'm still *learning* to respond to all messages.
            """

    # Send the response if defined
    if response:
        await update.message.reply_text(response, parse_mode="Markdown")  # Use Markdown formatting
    await log_interaction(update, response)  # Log the interaction

# Add handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('hello', hello))
application.add_handler(CommandHandler('about', about))
application.add_handler(CommandHandler('biharlife', biharlife))
application.add_handler(CommandHandler('schoollife', schoollife))
application.add_handler(CommandHandler('techjourney', techjourney))
application.add_handler(CommandHandler('socialmedia', socialmedia))
application.add_handler(CommandHandler('contact', contact))
application.add_handler(CommandHandler('privacypolicy', privacypolicy))
application.add_handler(MessageHandler(filters.COMMAND, unknown))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_other_messages))
application.add_error_handler(error_handler)

# Run the bot
if __name__ == "__main__":
    application.run_polling()
