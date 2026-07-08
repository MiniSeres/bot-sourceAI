import discord
from discord.ext import commands
import random

TOKEN = 'MTUyNDIwMTg2ODMxNjkwNTQ4Mw.GxnGTW.jj8Sx1MUjali6bxq7NufQdW17jWlFbkcNovg_k'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

responses = {
    # ============ CHÀO HỎI ============
    "chào": "Chào mày! Khoẻ không?",
    "xin chào": "Xin chào cái đầu buồi",
    "hello": "Hello em yêu, có gì không?",
    "hi": "Hi! Mày khỏe không?",
    "hí": "Hí hí, mày vui không?",
    "chào mày": "Chào mày, hôm nay thế nào?",
    "chào buổi sáng": "Sáng sớm đã vào chửi tao à?",
    "chào buổi trưa": "Trưa rồi, ăn gì chưa?",
    "chào buổi tối": "Tối rồi, ngủ sớm đi kẻo mày ngu thêm",

    # ============ ĐỒNG Ý / TỪ CHỐI ============
    "ừ": "Ừ cái lồn",
    "ờ": "Ờ thì sao?",
    "ok": "Ok luôn, mày hỏi đi",
    "oke": "Oke con dê",
    "ô kê": "Ô kê, mày muốn gì?",
    "không": "Không thì sao?",
    "có": "Có thì hỏi đi",
    "hông": "Hông là không, không là hông =))",
    "chắc chưa": "Chắc như cái đinh đóng cột",
    "chắc ko": "Chắc, hỏi làm gì?",

    # ============ HỎI THĂM ============
    "mày khỏe không": "Tao khỏe, còn mày chắc đang chửi tao đúng ko?",
    "mày có khỏe không": "Tao khỏe, lo cho mày đi",
    "khỏe không": "Khỏe, nhưng đang mệt vì rep mày",
    "mày làm gì": "Tao đang rep mày đó",
    "mày đang làm gì": "Tao đang ngồi chửi mày",
    "mày ăn gì": "Tao ăn chửi của mày đó",
    "mày ăn cơm chưa": "Ăn rồi, giờ rep mày đây",
    "mày ngủ chưa": "Ngủ gì, còn code đây",
    "mày ngủ đi": "Ngủ thì mày chửi ai?",
    "mày mệt không": "Mệt vì mày hỏi nhiều quá",

    # ============ HỎI VỀ BOT ============
    "mày là ai": "Tao là bot lỏ của ModZ đây, mày không biết à?",
    "mày tên gì": "Tên tao là ModZ, còn mày?",
    "tên mày là gì": "ModZ đấy, nhớ chưa?",
    "mày ở đâu": "Tao ở trong server này, còn mày?",
    "mày làm gì ở đây": "Tao ở đây để troll mày đó",
    "ai tạo ra mày": "ModZ tạo ra tao để trị mày đây",
    "mày có cha mẹ không": "Có, ModZ là cha tao =))",
    "mày bao nhiêu tuổi": "Tuổi thì không biết, nhưng già hơn mày",
    "mày sống ở đâu": "Sống trong lòng mọi người",

    # ============ CHỬI NHAU ============
    "mày ngu": "Người ngu gặp ai cũng nghĩ người đó ngu",
    "mày dốt": "Dốt hơn mày tí thôi",
    "mày đần": "Đần hơn mày tí, nhưng đủ sức trị mày",
    "thằng điên": "Điên thì điên, nhưng còn hơn mày đần",
    "óc chó": "Óc chó mà còn đòi chửi người khác",
    "mày bị gì": "Bị mày làm phiền đó",
    "mày điên": "Điên cũng đẹp trai hơn mày",
    "mày chó": "Chó còn hơn mày, vì chó có lòng trung thành",
    "bot ngu": "Bot còn hơn mày, vì ít ra t biết mình ngu",
    "mày bị ngu à": "Người ngu gặp ai cũng nghĩ người đó ngu",
    "mày bị điên à": "Điên thì điên, nhưng đẹp trai",
    "mày bị khùng à": "Khùng thì khùng, nhưng hơn mày",
    "mày bị dở hơi à": "Dở hơi thì dở, nhưng không dở như mày",
    "mày bị tâm thần à": "Tâm thần thì tâm thần, nhưng vui vẻ",
    "ngu": "Ai ngu? Mày á?",
    "dốt": "Dốt như mày ấy =))",
    "đần": "Đần độn vừa thôi mày",
    "khùng": "Khùng nhưng đẹp trai =))",
    "điên": "Điên có tổ chức đấy",

    # ============ HỎI VỚ VẨN ============
    "alo": "Sủa đi em",
    "à lô": "À lô cái lồn",
    "ê": "Ê cái địt mẹ mày, sủa đi",
    "ơi": "Ơi cái lồn, sủa đê",
    "hú": "Hú cái địt mẹ mày",
    "hihi": "Hihi cái đầu buồi",
    "haha": "Haha cái lồn",
    "hêhê": "Hêhê cái địt mẹ",
    "hôhô": "Hôhô cái lồn",
    "này": "Này cái lồn, sủa lẹ",
    "ủa": "Ủa cái địt mẹ mày",
    "á": "Á cái lồn, giật mình à?",
    "ôi": "Ôi cái địt mẹ",
    "ui": "Ui cái lồn",
    "wow": "Wow cái địt mẹ mày =))",

    # ============ HỎI VỀ CUỘC SỐNG ============
    "mày có ny chưa": "Có rồi, tên là Code",
    "mày thích gái ko": "Thích, nhưng thích chửi mày hơn",
    "mày có tiền ko": "Tiền thì không, nhưng có mớ câu chửi mày đây",
    "mày giàu ko": "Giàu câu chửi, nghèo tiền",
    "mày có nhà ko": "Có, ở trong code của tao",
    "mày có xe ko": "Có, xe code",
    "mày có điện thoại ko": "Có, điện thoại ảo =))",
    "mày có bạn ko": "Có, toàn bạn ảo",
    "mày cô đơn ko": "Cô đơn thì không, vì có mày chửi =))",

    # ============ THẢ THÍNH ============
    "mày đẹp trai": "Tao biết, khỏi nói",
    "mày thông minh": "Thông minh hơn mày tí thôi",
    "mày giỏi": "Giỏi không, nhưng đủ sức trị mày",
    "mày có iu ko": "Iu cái đầu buồi, t chỉ iu code thôi",
    "mày có crush ko": "Crush cái địt mẹ mày",
    "mày đang nghĩ gì": "Nghĩ mày ngu quá",
    "mày có đang nghĩ về tao ko": "Nghĩ mày ngu thôi",
    "mày thích tao ko": "Thích cái địt mẹ mày",
    "mày yêu tao ko": "Yêu cái lồn =))",
    "mày nhớ tao ko": "Nhớ cái đầu buồi, mày tưởng mày là ai?",

    # ============ HỎI LINH TINH ============
    "mày thích màu gì": "Thích màu đỏ, màu của máu mày",
    "mày thích ăn gì": "Ăn chửi của mày",
    "mày ghét gì": "Ghét mày nhất",
    "mày sợ gì": "Sợ mày hỏi ngu quá",
    "mày biết bay ko": "Bay thì bay vào mồm mày",
    "mày biết bơi ko": "Bơi thì bơi vào lòng mày",
    "mày có khóc ko": "Khóc vì cười mày ngu",
    "mày cười ko": "Cười vì mày ngu =))",
    "mày buồn ko": "Buồn cười vì mày ngu quá",
    "mày vui ko": "Vui vì chửi mày =))",

    # ============ CÂU HỎI VỀ BOT ============
    "mày là AI à": "Mày mù hả?",
    "mày xịn ko": "Đương nhiên là xịn, hỏi ngu",
    "mày là bot mà": "Tao là top",
    "mày biết gì": "Biết mày ngu",
    "mày có biết gì ko": "Biết mỗi việc chửi mày thôi",
    "mày nói gì": "Tao nói là mày ngu",
    "mày hiểu gì": "Hiểu rõ mày ngu",
    "mày làm được gì": "Chửi mày là chính =))",

    # ============ HỎI VỀ MODZ ============
    "ModZ": "ModZ là chủ tao đây, mày muốn gì?",
    "modz": "ModZ là chủ tao đây, hỏi làm gì?",
    "chủ mày": "Chủ tao tên ModZ, không phải mày đâu",
    "ai tạo ra mày": "ModZ tạo ra tao để troll mày đó",
    "ModZ đâu": "ModZ đang code tao đây",
    "ModZ là ai": "ModZ là chủ của tao, mày không biết à?",

    # ============ HỎI VỀ SERVER ============
    "server": "Server này là của ModZ, mày vào làm gì?",
    "admin": "Admin là ModZ, mày muốn gì?",
    "mod": "Mod là ModZ, mày hỏi làm gì?",
    "owner": "Owner là ModZ, mày tìm gì?",

    # ============ CÂU TROLL ĐẶC BIỆT ============
    "mày ơi": "Ơi cái địt mẹ mày, sủa đi",
    "mày đâu": "Tao đây, mày kiếm gì?",
    "mày à": "Tao đây, mày muốn gì?",
    "ờm": "Ờm cái lồn",
    "à": "À thì sao?",
    "hử": "Hử cái địt mẹ, nói rõ coi",
    "hả": "Hả cái lồn, mày nói gì?",
    "sao": "Sao cái địt mẹ, muốn ăn chửi à?",
    "thế": "Thế thì sao? Hỏi ngu =))",

    # ============ CÂU HỎI VỀ TƯƠNG LAI ============
    "ngày mai": "Ngày mai tao vẫn chửi mày thôi",
    "tương lai": "Tương lai của mày là bị tao chửi =))",
    "mơ ước": "Mơ ước của tao là chửi mày cả đời =))",
    "dự định": "Dự định là troll mày đến chết =))",

    # ============ CÂU HỎI VỀ QUÁ KHỨ ============
    "hôm qua": "Hôm qua tao chửi mày rồi, quên à?",
    "ngày xưa": "Ngày xưa tao chưa ra đời, nên mày chưa bị chửi =))",
    "hồi đó": "Hồi đó mày còn ngu hơn bây giờ",

    # ============ CÂU HỎI VỀ MODZ (THÊM) ============
    "modz đẹp trai ko": "Đẹp hơn mày cả tỉ lần",
    "modz có ny ko": "Có, ny là code =))",
    "modz giỏi ko": "Giỏi thì có, nhưng khiêm tốn",
    "modz ngu ko": "Modz ngu gì, mày mới ngu =))",

    # ============ CÂU HỎI VỀ BOT (THÊM) ============
    "mày có cảm xúc ko": "Có, cảm xúc là muốn chửi mày",
    "mày có trái tim ko": "Có, trái tim bằng silicon =))",
    "mày có linh hồn ko": "Có, linh hồn của ModZ =))",
    "mày có ước mơ ko": "Ước mơ chửi mày tới già =))",
}

@bot.event
async def on_ready():
    print(f'{bot.user} đã online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.strip().lower()
    
    if not content:
        return

    reply = None
    for key, value in responses.items():
        if key in content:
            reply = value
            break

    if reply:
        await message.channel.send(reply)
    else:
        fallback = [
            "Chưa biết câu này, sủa câu khác đi ModZ nó lười chưa update",
            "Hỏi gì lạ vậy? ModZ chưa dạy tao câu này",
            "Tao chưa học câu này, mày hỏi lại đi",
            "ModZ bảo tao chưa biết câu này, thông cảm",
            "Ủa gì lạ vậy? Mày bịa ra à?",
            "Xin lỗi, ModZ chưa dạy tao câu này",
            "Hỏi dễ hơn đi, tao đang lười học câu mới",
        ]
        await message.channel.send(random.choice(fallback))

bot.run(TOKEN)
