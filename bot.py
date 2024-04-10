
# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL
from pyrogram import Client, filters
from pytube import YouTube
import asyncio

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_BOT_TOKEN' with your actual values

API_ID = '17095753'
API_HASH = '19a412647f01e0c04bb246b04c9d6f69'
BOT_TOKEN = '6300008988:AAF1YnOPHCFaLgJEwp-JnS8vkUT8lkFHdjU'

# Create a Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(filters.command("start"))
def start(client, message):
    user = message.from_user
    message.reply_text(f"<b>ʜᴇʏ @{user.username} !\n\nɪ ᴀᴍ ᴘᴏᴡᴇʀꜰᴜʟ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ. ɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ. ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏꜰ ᴛʜᴇ ᴠɪᴅᴇᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜᴘʟᴏᴀᴅ...♻️\n\n👨🏻‍💻ᴅᴇᴠʟᴏᴘᴇʀ - <a href=https://telegram.me/KING_WMP>Chethmina Kavishan</a>
⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <a href=https://telegram.me/CK4U2>CK4U2</a></b>")

# Help command handler
@app.on_message(filters.command("help"))
def help(client, message):
    help_text = """<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʏᴛ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ💗

ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ, ꜱɪᴍᴘʟʏ ꜱᴇɴᴅ ᴍᴇ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ.

ᴇɴᴊᴏʏ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ💥

⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ <i><a href=https://telegram.me/CK4U2>CK4U2</a></i></b>
    """
    message.reply_text(help_text)

# Message handler for processing YouTube links
@app.on_message(filters.regex(r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'))
async def process_youtube_link(client, message):
    youtube_link = message.text
    try:
        # Downloading text message
        downloading_msg = await message.reply_text("Downloading video...")

        # Download the YouTube video
        yt = YouTube(youtube_link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(filename='downloaded_video.mp4')

        # Uploading text message
        uploading_msg = await message.reply_text("Uploading video...")

        # Send the video file to the user
        sent_message = await app.send_video(message.chat.id, video=open('downloaded_video.mp4', 'rb'), caption=yt.title)

        # Delay for a few seconds and delete downloading and uploading
        await asyncio.sleep(2)
        await downloading_msg.delete()
        await uploading_msg.delete()

        # Send successful upload message
        await message.reply_text("\n\n⚡ᴘᴏᴡᴇʀᴇᴅ ʙʏ <i><a href=https://telegram.me/CK4U2>CK4U2</a></i></b>")

    except Exception as e:
        error_text = 'Error: Failed to process the YouTube link. Please make sure the link is valid and try again.'
        await message.reply_text(error_text)

# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
