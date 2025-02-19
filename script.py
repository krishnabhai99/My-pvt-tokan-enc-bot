class Txt(object):

    PRIVATE_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴅᴏ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ɪɴ ɴᴇɢʟɪɢɪʙʟᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏss ᴏғ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ
"""
    GROUP_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ɴᴇɢʟɪɢɪʙʟᴇ sɪᴢᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏᴏsɪɴɢ ᴛʜᴇ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ

❗**Yᴏᴜ ʜᴀsɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴍᴇ ʏᴇᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ғɪʀsᴛ sᴛᴀʀᴛ ᴍᴇ sᴏ ɪ ᴄᴀɴ ᴡᴏʀᴋ ғʟᴀᴡʟᴇssʟʏ**
"""
    PROGRESS_BAR = """<b>
🚀🌌 Uploading to the Stars... 🌌🚀  

📁 **File Size:** `{1} | {2}` 🌍💾  
📊 **Progress:** `{0}%` ✅📈🔵  
⚡ **Speed:** `{3}/s` 🚀⚡🔥  
⏳ **ETA:** `{4}` ⏱️⏩🏁  

🌟 **Hang tight! Your file is taking off into the universe!** ✨🌠💖 </b>"""

    SEND_FFMPEG_CODE = """
❪ SET CUSTOM FFMPEG CODE ❫

Send me the correct ffmpeg code for more info.


☛ <a href=https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg#:~:text=ffmpeg%20%2Di%20input.mp4%20%2Dvcodec%20libx265%20%2Dcrf%2028%20output.mp4> FOR HELP </a>

⦿ Fᴏʀᴍᴀᴛ Oɴ Hᴏᴡ Tᴏ Sᴇᴛ

☞ ffmpeg -i input.mp4 <code> -c:v libx264 -crf 23 </code> output.mp4

<code> -c:v libx264 -crf 23 </code> Tʜɪs ɪs ʏᴏᴜʀ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ ✅

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Krishna99887722
"""

    SEND_METADATA ="""
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="My Video" -metadata author="John Doe" -metadata:s:s title="Subtitle Title" -metadata:s:a title="Audio Title" -metadata:s:v title="Video Title" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @Krishna99887722
"""

    
    HELP_MSG = """
Available commands:-

➜ /set_ffmpeg - To set custom ffmpeg code
➜ /set_metadata - To set custom metadata code
➜ /set_caption - To set custom caption
➜ /del_ffmpeg - Delete the custom ffmpeg code
➜ /del_caption - Delete caption
➜ /see_ffmpeg - View custom ffmpeg code
➜ /see_metadata - View custom metadata code
➜ /see_caption - View caption 
➜ To Set Thumbnail just send photo


<b>⦿ Developer:</b> <a href=https://t.me/Krishna99887722>KRISHNA ❄️</a>
"""

    ABOUT_TXT = """<b>╭────[ 🛸 𝗕𝗢𝗧 𝗜𝗡𝗙𝗢 ]────⍟  
├ 👤 **BOT NAME:** @{}  
├ 👨‍💻 **DEVELOPER:** <a href="https://t.me/Krishna99887722">KRISHNA</a>  
├ 🌍 **INSTAGRAM:** <a href="https://t.me/Animes_India_bot">Animes India Bot</a>  
├ 🏆 **FOUNDER OF:** <a href="https://t.me/new_animes_hindi_dub_india">ANIME</a>  
├ 📚 **LIBRARY:** <a href="https://github.com/pyrogram">Pyrogram</a>  
├ 💻 **LANGUAGE:** <a href="https://www.python.org">Python 3</a>  
├ 💾 **DATABASE:** <a href="https://cloud.mongodb.com">MongoDB</a>  
├ 🚀 **SERVER:** <a href="https://dashboard.heroku.com">Heroku</a>  
╰──────────────────────────⍟  
 """
