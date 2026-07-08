import discord
from discord.ext import commands
import re

TOKEN = 'MTUyNDIwMTg2ODMxNjkwNTQ4Mw.G_hXhM.4wVDkyL1dE4B65O67XZ9NHkUBXMCKQ0ZoELcBo'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Lưu trạng thái user (trong RAM)
user_settings = {}

responses = {
    # Chào hỏi cơ bản
    "chào": "Chào mày! Khoẻ không?",
    "xin chào": "Xin chào cái đầu buồi =))",
    "hello": "Hello em yêu, có gì không?",
    "hi": "Hi! Mày khỏe không?",
    "ừ": "Ừ cái lồn",
    "ờ": "Ờ thì sao?",
    "ô kê": "Ô kê, mày muốn gì?",
    "ok": "Ok luôn, mày hỏi đi",
    "không": "Không thì sao?",
    "có": "Có thì hỏi đi",
    "gì": "Gì? Nói rõ ra coi",

    # Hỏi thăm
    "mày khỏe không": "Tao khỏe, còn mày chắc đang chửi tao đúng ko?",
    "mày có khỏe không": "Tao khỏe, lo cho mày đi",
    "mày làm gì": "Tao đang rep mày đó",
    "mày đang làm gì": "Tao đang ngồi chửi mày =))",
    "mày ăn gì": "Tao ăn chửi của mày đó",
    "mày ngủ chưa": "Ngủ gì, còn code đây",

    # Hỏi về bot
    "mày là ai": "Tao là bot lỏ của ModZ đây, mày không biết à?",
    "mày tên gì": "Tên tao là ModZ, còn mày?",
    "mày ở đâu": "Tao ở trong server này, còn mày?",
    "mày làm gì ở đây": "Tao ở đây để troll mày đó",

    # Chửi nhau
    "mày ngu": "Người ngu gặp ai cũng nghĩ người đó ngu",
    "mày dốt": "Dốt hơn mày tí thôi",
    "thằng điên": "Điên thì điên, nhưng còn hơn mày đần",
    "óc chó": "Óc chó mà còn đòi chửi người khác",
    "mày bị gì": "Bị mày làm phiền đó",
    "mày điên": "Điên cũng đẹp trai hơn mày",
    "mày chó": "Chó còn hơn mày, tại vì chó có lòng trung thành",
    "bot ngu": "Bot còn hơn mày, vì ít ra t biết mình ngu",
    "mày bị ngu à": "Người ngu gặp ai cũng nghĩ người đó ngu",
    "mày bị điên à": "Điên thì điên, nhưng đẹp trai",
    "mày bị khùng à": "Khùng thì khùng, nhưng hơn mày",

    # Hỏi vớ vẩn
    "alo": "Sủa đi em",
    "à lô": "À lô cái lồn",
    "ê": "Ê cái địt mẹ mày, sủa đi",
    "ơi": "Ơi cái lồn, sủa đê",
    "hú": "Hú cái địt mẹ mày",
    "hihi": "Hihi cái đầu buồi",
    "haha": "Haha cái lồn",

    # Hỏi về cuộc sống
    "mày có ny chưa": "Có rồi, tên là Code",
    "mày thích gái ko": "Thích, nhưng thích chửi mày hơn",
    "mày có tiền ko": "Tiền thì không, nhưng có mớ câu chửi mày đây",
    "mày giàu ko": "Giàu câu chửi, nghèo tiền",
    "mày có nhà ko": "Có, ở trong code của tao",
    "mày có xe ko": "Có, xe code =))",

    # Thả thính
    "mày đẹp trai": "Tao biết, khỏi nói",
    "mày thông minh": "Thông minh hơn mày tí thôi",
    "mày giỏi": "Giỏi không, nhưng đủ sức trị mày",
    "mày có iu ko": "Iu cái đầu buồi, t chỉ iu code thôi",
    "mày có crush ko": "Crush cái địt mẹ mày",
    "mày đang nghĩ gì": "Nghĩ mày ngu quá",

    # Hỏi linh tinh
    "mày thích màu gì": "Thích màu đỏ, màu của máu mày",
    "mày thích ăn gì": "Ăn chửi của mày",
    "mày ghét gì": "Ghét mày nhất",
    "mày sợ gì": "Sợ mày hỏi ngu quá",
    "mày biết bay ko": "Bay thì bay vào mồm mày",
    "mày biết bơi ko": "Bơi thì bơi vào lòng mày",
    "mày có khóc ko": "Khóc vì cười mày ngu",

    # Câu hỏi về bot
    "mày là AI à": "Mày mù hả?",
    "mày xịn ko": "Đương nhiên là xịn, hỏi ngu",
    "mày là bot mà": "Tao là top",
    "mày biết gì": "Biết mày ngu =))",

    # Câu troll đặc biệt
    "mày ơi": "Ơi cái địt mẹ mày, sủa đi",
    "này": "Này cái lồn, sủa lẹ",
    "mày đâu": "Tao đây, mày kiếm gì?",
    "mày à": "Tao đây, mày muốn gì?",
    "ờm": "Ờm cái lồn",
    "à": "À thì sao?",
    "ủa": "Ủa cái địt mẹ mày",

    # Hỏi về ModZ
    "ModZ": "ModZ là chủ tao đây, mày muốn gì?",
    "modz": "ModZ là chủ tao đây, hỏi làm gì?",
    "chủ mày": "Chủ tao tên ModZ, không phải mày đâu",
    "ai tạo ra mày": "ModZ tạo ra tao để troll mày đó",

    # Hỏi về server
    "server": "Server này là của ModZ, mày vào làm gì?",
    "admin": "Admin là ModZ, mày muốn gì?",
    "mod": "Mod là ModZ, mày hỏi làm gì?",
}

@bot.event
async def on_ready():
    print(f'{bot.user} đã online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user_id = str(message.author.id)
    
    # Lệnh bật/tắt cho từng user (ai cũng dùng được)
    if message.content.startswith('!bot on'):
        user_settings[user_id] = True
        await message.channel.send(f"✅ {message.author.mention} Bot đã được **BẬT**!")
        return
    
    if message.content.startswith('!bot off'):
        user_settings[user_id] = False
        await message.channel.send(f"🔇 {message.author.mention} Bot đã được **TẮT**!")
        return
    
    # Check user có bật ko
    if not user_settings.get(user_id, True):
        await bot.process_commands(message)
        return
    
    # Check tag
    if bot.user.mentioned_in(message):
        content = message.content
        for mention in message.mentions:
            content = content.replace(f'<@{mention.id}>', '').replace(f'<@!{mention.id}>', '')
        content = content.strip()
        
        if not content:
            await message.channel.send("Gì?")
            return
        
        # Tìm câu trả lời
        reply = None
        for key, value in responses.items():
            if key in content.lower():
                reply = value
                break
        
        if reply:
            await message.channel.send(reply)
        else:
            # Câu trả lời thông minh hơn khi không biết
            fallback_responses = [
                "Chưa biết câu này, sủa câu khác đi ModZ nó lười chưa update",
                "Hỏi gì lạ vậy? ModZ chưa dạy tao câu này",
                "Tao chưa học câu này, mày hỏi lại đi",
                "ModZ bảo tao chưa biết câu này, thông cảm =))",
            ]
            import random
            await message.channel.send(random.choice(fallback_responses))
    
    await bot.process_commands(message)

bot.run(TOKEN)
