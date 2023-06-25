import telethon
from telethon import events
from config import *
import os
import logging
import aCYncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from payment import *
from help import *
from checktele import *
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

CYthon.start()
c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    6291329457,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


@CYthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await CYthon(JoinChannelRequest("@Cython2"))
    except BaseException:
        pass
        
@CYthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await CYthon(JoinChannelRequest("@CY_tem"))
    except BaseException:
        pass
      

@CYthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await CYthon(JoinChannelRequest("@Cython2"))
    except BaseException:
        pass  
        
        




@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
aCYnc def _(event):
    await event.edit(commands)

@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
aCYnc def _(event):
    start = datetime.datetime.now()
    await event.edit("جارٍ...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**☆ WELCOME TO CYTHON
☆ VERSION : 1.3
☆ PING : `{ms}`
☆ DATE : `{m9zpi}`
☆ ID : `{event.sender_id}`
☆ SOURCE CYTHON : @Cython2**

-قـم بإرسال `.الاوامر`
''')


@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
aCYnc def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
aCYnc def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
aCYnc def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.م4"))
aCYnc def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

    
ownerhson_id = 6291329457
@CYthon.on(events.NewMessage(outgoing=False, pattern='/start'))
aCYnc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('مرحبا ايها المطور')

@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
aCYnc def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتظر 1-2 دقيقة  .")
    await CYthon.disconnect()
    await CYthon.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@CYthon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
aCYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await CYthon(JoinChannelRequest('Cython2'))
    channel_entity = await CYthon.get_entity(bot_username)
    await CYthon.send_message(bot_username, '/start')
    await aCYncio.sleep(4)
    msg0 = await CYthon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await aCYncio.sleep(4)
    msg1 = await CYthon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aCYncio.sleep(4)

        list = await CYthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await CYthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | CY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CYthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await CYthon(ImportChatInviteRequest(bott))
            msg2 = await CYthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CYthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CYthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | CY**")

@CYthon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
aCYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await CYthon(JoinChannelRequest('Cython2'))
    channel_entity = await CYthon.get_entity(bot_usernamee)
    await CYthon.send_message(bot_usernamee, '/start')
    await aCYncio.sleep(4)
    msg0 = await CYthon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await aCYncio.sleep(4)
    msg1 = await CYthon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aCYncio.sleep(4)

        list = await CYthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await CYthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | CY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CYthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await CYthon(ImportChatInviteRequest(bott))
            msg2 = await CYthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CYthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CYthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | CY**")

@CYthon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
aCYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await CYthon(JoinChannelRequest('Cython2'))
    channel_entity = await CYthon.get_entity(bot_usernameee)
    await CYthon.send_message(bot_usernameee, '/start')
    await aCYncio.sleep(4)
    msg0 = await CYthon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await aCYncio.sleep(4)
    msg1 = await CYthon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aCYncio.sleep(4)

        list = await CYthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await CYthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | CY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CYthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await CYthon(ImportChatInviteRequest(bott))
            msg2 = await CYthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CYthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CYthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | CY**")


@CYthon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
aCYnc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await CYthon(JoinChannelRequest('Cython2'))
    channel_entity = await CYthon.get_entity(bot_usernameeee)
    await CYthon.send_message(bot_usernameeee, '/start')
    await aCYncio.sleep(4)
    msg0 = await CYthon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await aCYncio.sleep(4)
    msg1 = await CYthon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await aCYncio.sleep(4)

        list = await CYthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await CYthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | CY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await CYthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await CYthon(ImportChatInviteRequest(bott))
            msg2 = await CYthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await CYthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await CYthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | CY**")


@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
aCYnc def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await CYthon.disconnect()
    await CYthon.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@CYthon.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
aCYnc def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await CYthon.disconnect()
    await CYthon.send_message("me", "**اكتمل ايقاف التكرار**")


LOGS = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

aCYnc def join_channel():
    try:
        await CYthon(JoinChannelRequest("@Cython2"))
    except BaseException:
        pass
 
 
GCAST_BLACKLIST = [
    -1001884452589,
    -1001884452589,
]

DEVS = [
    6291329457,
]

def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"


@CYthon.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
aCYnc def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')


@CYthon.on(events.NewMessage(outgoing=True, pattern=".للكروبات(?: |$)(.*)"))
aCYnc def gcast(event):
    CYthon = event.pattern_match.group(1)
    if CYthon:
        msg = CYthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحظة")
    er = 0
    done = 0
    aCYnc for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة إلى ** `{done}` **من الدردشات ، خطأ في إرسال إلى ** `{er}` **من الدردشات**"
    )


@CYthon.on(events.NewMessage(outgoing=True, pattern=".للخاص(?: |$)(.*)"))
async def join_channel(event):
    CYthon = event.pattern_match.group(1)
    if CYthon:
        msg = CYthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "**⌔∮ يجب الرد على رساله او وسائط او كتابه النص مع الامر**"
        )
        return
    roz = await event.edit("⌔∮ يتم الاذاعة في الخاص انتظر لحظة")
    er = 0
    done = 0
    aCYnc for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**⌔∮  تم بنجاح الأذاعة إلى ** `{done}` **من الدردشات ، خطأ في إرسال إلى ** `{er}` **من الدردشات**"
    )

@CYthon.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
aCYnc def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


aCYnc def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await aCYncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await aCYncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await aCYncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@CYthon.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
aCYnc def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
 
    
@CYthon.on(events.NewMessage(outgoing=True, pattern=".سورس"))
aCYnc def _(event):
      await event.reply("""السـورس يعمـل | 𝐂𝐘𝐓𝐇𝐎𝐍
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

- المطور : علي

- سورس بسيط يحتوي على الاوامر المهمة التي تحتاجها

قناة السورس : https://t.me/Cython2
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍"""
)

@CYthon.on(events.NewMessage(outgoing=True, pattern=".مطور"))
aCYnc def _(event):
      await event.reply("""OWNER : @RPPJP"""
)

@CYthon.on(events.NewMessage(outgoing=True, pattern=".حلويات"))
aCYnc def _(event):
    event = await event.edit("candy")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(100):
        await aCYncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)

@CYthon.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
aCYnc def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await aCYncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@CYthon.on(events.NewMessage(outgoing=True, pattern=".العد التنازلي"))
aCYnc def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("🔟")
    animation_chars = [
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",

    ]
    for i in animation_ttl:
        await aCYncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

        
@CYthon.on(events.NewMessage(outgoing=True, pattern=".قمر"))
aCYnc def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await aCYncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)
        
@CYthon.on(events.NewMessage(outgoing=True, pattern=".قمور"))
aCYnc def _(event):
    event = await event.edit("قمور")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await aCYncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])






print("- CYthon Userbot Running ..")
CYthon.run_until_disconnected()
