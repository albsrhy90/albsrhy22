from config import Config 
import requests
from telebot import types
import random
import telebot
from datetime import date ,timedelta ,time
import time 
elhypamody = '5586079401'
bot = telebot.TeleBot(Config.TG_BOT_TOKEN)
p3 = types.InlineKeyboardMarkup()
p5 = types.InlineKeyboardButton(text = "حياكم في بوت نبا",url="t.me/o_z_g")
A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  f2 = message.from_user.first_name 
  t2 = message.from_user.username 
  bot.reply_to(message,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في بوت الاوامر، 
لمعرفة اوامر البوت ارسل الاوامر*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="abbas")

abod = ["متى تكون البراءه ذئب ؟",
            "هل تتوقع أن يصل البشر لمرحلة من التطور تجعلهم يتنقلون بين الكواكب بسهولة ؟",
            "أشياء ومنتجات جربتها في السفر أعجبتك ؟",
            "( الحياة مرة )/ هل قرأتها بالضمة أم بالفتحة ؟",
            "يتجاهلك بالقصد بعد صداقة طويلة، ما مقصده برأيك ؟",
            "شعورك الحالي في جملة ؟",
            "عندكم في الشلة ذلك الشخص الخجول جدًا ؟",
            "أشياء تجعلك تستمر وتتحمّل صعوبات الحياة ؟",
            "فنان/ة تحلم بلقائه ؟",
            "بتنام ولا بتواصل ؟",
            "ردة فعلك لو أوقفتك الشرطة في الطريق وسمعتهم يقولون هذا هو القاتل ؟",
            "شاركنا افضل قناة عندك ؟",
            "شيء جميل حصل معك اليوم ؟",
            "شاركنا صوره تمثل تخصصك ؟",
            "للإناث | لديكِ الجرأة لمصارحة الشخص اللي أذاك بكل شيء في قلبك ؟",
            "أكثر طبع غريب فيك وتحبه ؟",
            "أبسط شيء بعدل يومك كامل ؟",
            "سؤال تسأل نفسك فيه دائمًا ولا حصلت جواب ؟",
            "أسم تحب تقوله ؟",
            "أسم بنت تحبه ؟",
            "أسم ولد تحبه ؟",
            "وش تحس من يوم يناديك أبوك ؟",
            "مين أشد عصبية أمك أو أبوك ؟",
            "عادي تتابع فلم/مسلسل أكثر من مره ؟",
            "تقدر ترسل أخر صوره حفظتها ؟",
            "وش هي أكلتك المفظلة ؟",
            "وش الصفة الي تميزك عن غيرك ؟",
            "أنت شخص مسالم ؟",
            "شيء تسمعه كثير من الناس عنك ؟",
            "تحس أنك غامض ولا سراويلك منشوره ؟",
            "صفة تكرهها ؟",
            "أنت من النوع الي يعرف يسولف ويفتح مواضيع ؟",
            "موضوع ما تتقبل المزح فيه ؟",
            "كِلمة توجهها لوالديك ؟",
            "سطر من أخر أغنية سمعتها ؟",
            "عندك شخص تقوله كل تفاصيل يومك ؟",
            "ليش الاغلب يفضلون العلاقات الإكترونية ؟",
            "وش رأيك بالأهل الي يفتشون الجوالات ؟",
            "أهلك يفتشون جوالك ؟",
            "هل أنت راضي عن نفسك الفترة ذي ؟",
            "أنت من مُحبين الموسيقى القديمة أو الجديدة ؟",
            "أكله ودك تجربها ؟",
            "لو كانت للأيام الجميلة رائحه ماذا ستكون ؟",
            "تاريخ ودك تعيش فيه ؟",
            "لو تكرهه جدًا ؟",
            "عطينا إقتباس تحبه ؟",
            "عطينا حكمة لليوم ؟",
            "حكمتك الي ماشي عليها ؟",
            "أنت فاشل دراسيًا ؟",
            "انت متوظف ؟",
            "أسمك الي بالبرنامج غير عن الواقعي ؟",
            "مين الي أختار لك أسمك ؟",
            "كذبت في الأسئلة الي راحت ؟",
            "لو العالم مافيه أحد غيرك وش بتسوي ؟",
            "هل يومك جيد ؟",
            "القهوة بنظرك ؟",
            "تفكيرك الأن مُختلف عن العام الماضي ؟",
            "لو تروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",
            "تقدر تستغني عن هاتفك لأسبوع ؟",
            "شيء تحس لو ما سويته ليوم تفقده ؟",
            "رسالة لنفسك المستقبيلة ؟",
            "وش رأيك في الي يطلب السناب ؟",
            "تقدر تعطي سنابك أحد ؟",
            "كم شخص مسوي له بلوك ؟",
            "مفهوم الصداقة بالنسبة لك ؟",
            "يزيد حُبي لكِ لمّا ... ؟",
            "مِن نِعْم الحياة ... ؟",
            "اذا فضفضت ترتاح ؟",
            "اكثر شي ينرفزك ؟",
            "اخر مكان رحتله ؟",
            "شخص @ تعترفلة بشي ؟",
            "تغار ؟",
            "تعتقد فيه أحد يراقبك 👩🏼‍💻؟",
            "ولادتك بنفس المكان الي عايش فيه ولا لا؟",
            "اكثر شي ينرفزك ؟",
            "تغار ؟",
            "كم تبلغ ذاكرة هاتفك؟",
            "صندوق اسرارك ؟",
            "شخص @ تعترفله بشي ؟",
            "يومك ضاع على ؟",
            "اغرب شيء حدث في حياتك ؟",
            " نسبة حبك للاكل ؟",
            " حكمة تأمان بيها ؟",
            " اكثر شي ينرفزك ؟",
            " هل تعرضت للظلم من قبل؟",
            " خانوك ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تاريخ غير حياتك ؟",
            " أجمل سنة ميلادية مرت عليك ؟",
            " ولادتك بنفس المكان الي هسة عايش بي او لا؟",
            " تزعلك الدنيا ويرضيك ؟",

" ماهي هوايتك؟",
            " دوله ندمت انك سافرت لها ؟",
            "شخص اذا جان بلطلعة تتونس بوجود؟",
            " تاخذ مليون دولار و تضرب خويك؟",
            " تاريخ ميلادك؟",
            "اشكم مره حبيت ؟",
            " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",
            " هل تثق في نفسك ؟",
            " اسمك الثلاثي ؟",
            "كلمة لشخص خذلك؟",
            "هل انت متسامح ؟",
            "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",
            "عصير لو قهوة؟",
            " صديق أمك ولا أبوك. ؟",
            "تثق بـ احد ؟",
            "كم مره حبيت ؟",
            " اوصف حياتك بكلمتين ؟",
            " حياتك محلوا بدون ؟",
            " وش روتينك اليومي؟",
            " شي تسوي من تحس بلملل؟",
            " يوم ميلادك ؟",
            " اكثر مشاستاد بسبب ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تتوقع فيه احد حاقد عليك ويكرهك ؟",
            "كلمة غريبة من لهجتك ومعناها؟",
            " • هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار",
            "• كيف تشوف الجيل ذا؟",
            "• تاريخ لن تنساه📅؟",
            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "• تؤمن ان في حُب من أول نظرة ولا لا ؟.",
            "• ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",
            "• طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",
            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
            "• أطول مدة نمت فيها كم ساعة؟",
            "• كلمة غريبة من لهجتك ومعناها؟🤓",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• شخص تحب تستفزه😈؟",
            "• تشوف الغيره انانيه او حب؟",
            "• مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",
            "• اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",
            "• ‏للعيال - آخر مرة وصلك غزل من بنت؟",
            "• أوصف نفسك بكلمة؟",
            "• شيء من صغرك ماتغير فيك؟",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث وش راح تكون ؟.",
            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "• حاجة تشوف نفسك مبدع فيها ؟",
            "• يهمك ملابسك تكون ماركة ؟",
            "• يومك ضاع على؟",
            "• اذا اكتشفت أن أعز أصدقائك يضمر لك",
            " السوء، موقفك الصريح؟",
            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "• كلمه ماسكه معك الفترة هذي ؟",
            "• كيف هي أحوال قلبك؟",
            "• صريح، مشتاق؟",
            "• اغرب اسم مر عليك ؟",
            "• تختار أن تكون غبي أو قبيح؟",
            "• آخر مرة أكلت أكلتك المفضّلة؟",
            "• اشياء صعب تتقبلها بسرعه ؟",
            "• كلمة لشخص غالي اشتقت إليه؟",
            "• اكثر شيء تحس انه مات ف مجتمعنا؟",
            "• هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",
            "• آخر شيء ضاع منك؟",
            "• تشوف الغيره انانيه او حب؟",
            "• لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
            "• شيء كل م تذكرته تبتسم ...",
            "• هل تحبها ولماذا قمت باختيارها؟",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "• أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟",
            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "• هل تشعر أن هنالك مَن يُحبك؟",
            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "• صوت مغني م تحبه",
            "• كم في حسابك البنكي ؟",
            "• اذكر موقف ماتنساه بعمرك؟",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• عندك حس فكاهي ولا نفسية؟",
            "• من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",
            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "• شيء من صغرك ماتغير فيك؟",
            "• هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",
            "• هل تحبها ولماذا قمت باختيارها؟",
            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "• كم مره تسبح باليوم",
            "• أفضل صفة تحبه بنفسك؟",
            "• أجمل شيء حصل معك خلال هاليوم؟",
            "• ‏شيء سمعته عالق في ذهنك هاليومين؟",
            "• هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",
            "• ‏أبرز صفة حسنة في صديقك المقرب؟",
            "• ما الذي يشغل بالك في الفترة الحالية؟",
            "• آخر مرة ضحكت من كل قلبك؟",
            "• احقر الناس هو من ...",
            "• اكثر دوله ودك تسافر لها؟",
            "• آخر خبر سعيد، متى وصلك؟",
            "• ‏نسبة احتياجك للعزلة من 10؟",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• أكثر جملة أثرت بك في حياتك؟",
            "• لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• آخر مرة ضحكت من كل قلبك؟",
            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "• تزعلك الدنيا ويرضيك ؟",
            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "• تعتقد فيه أحد يراقبك؟",
            "• احقر الناس هو من ...",
            "• شيء من صغرك ماتغير فيك؟",
            "• . نلقى السعاده برايك؟",
            "• هل تغارين من صديقاتك؟",
            "• أكثر جملة أثرت بك في حياتك؟",
            "• كم عدد اللي معطيهم بلوك؟",
            "• أجمل سنة ميلادية مرت عليك ؟",
            "• أوصف نفسك بكلمة؟",]


n = ["وففف تخبل 😍🤤",
"لزكت بيه دغيره 😒😒",
"كلسا ايدي كلسا ايدي دكافي كبرر ",
"ابه نيو شوفو صورتي ",
"حلغوم والله ،🥺💘 ", 
"مو صوره غنبله براسها ٦٠ حظ",
"مقتنع بصورتك !؟ ",
"كشخه برب ،😉🤍 "]
pm = ["ع اساس شلونه،",
"كشخه والعباس 🤤♥️",
"حلغوم والله،🥺❤️",
"شوفني حلو وهو جنه بريعصي،😂",
"تف ع صورتك شخبصتنه،😏",
"حمضتتتتتت،",
"جذاب خامطه،",
"هل صاك/ة منين ؟؟؟",
"عبود الحكللي روحي طاحت من السيرفر 😱"]

	
@bot.message_handler(content_types=['text'])
def start(message):
	#if 'http' in message.text:
#		bot.delete_message(id,messagesid)
	if message.text == "ا" or message.text == "id" or message.text == "ايدي":
		n = ["وففف تخبل 😍🤤",
"لزكت بيه دغيره 😒😒",
"كلسا ايدي كلسا ايدي دكافي كبرر ",
"ابه نيو شوفو صورتي ",
"حلغوم والله ،🥺💘 ", 
"مو صوره غنبله براسها ٦٠ حظ",
"مقتنع بصورتك !؟ ",
"كشخه برب ،😉🤍 "]
		s333 = random.choice(n)
		url = f"https://t.me/{message.from_user.username}"
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		c = message.from_user.id
		k = message.from_user.username
		d = time.strftime("%p %H:%M")
		t = message.chat.type
		y = '@aliccod'
		bot.send_photo(message.chat.id,url,"""*  {}
		
𖡋 𝐈𝐃 ⌯ {} 

𖡋 𝐔𝐒𝐄𝐑 ⌯ @{}

𖡋 𝐓𝐈𝐌𝐄 ⌯  {}

𖡋 𝐓𝐘𝐏𝐄 ⌯  {} 

𖡋 𝐁𝐈𝐎 ⌯ {} *""".format(s333,c,k,d,t,bio),parse_mode="abbas",reply_to_message_id=message.message_id)
	m = message.text
	if m == "ر":
	 e = message.chat.id
	 u = bot.get_chat(e).photo.big_file.id
	 file_info = bot.get_file(u)
	 downloaded_file = bot
	 download_file(file_info.file_path)
	 with open('new_file.png', 'wb') as new_file:
	 	new_file.write(downloaded_file)
	 	with open('new_file.png', 'rb') as photo:
	 		bot.send_photo(message.chat.id, photo)
	if message.text == "المجموعة" or message.text == "الكروب":
		j = message.chat.title
		t = time.strftime("%p %H:%S")
		l = bot.export_chat_invite_link(message.chat.id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="""*
اسم المجموعة ☆ {} 

رابط المجموعة ☆ {}

انت ☆* [{}](t.me/{}) *

الوقت ☆ {}*
""".format(j,l,f2,t2,t),disable_web_page_preview=True,parse_mode="abbas")
	if message.text == "رفع مطي" or message.text == "وضع مطي":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,"""*تم رفع  **العضو -*  [{}](t.me/{})*
في قائمة المطاية اصبح مطي جديد*""".format(f2,t2),parse_mode="abbas",disable_web_page_preview=True)
	
	m = message.text
	if m == ".":
		f2 = message.from_user.first_name
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "حياكم في بوت نبا",url="t.me/@o_z_g")
		p3.add(p5)
		bot.reply_to(message,f"{f2}",reply_markup=p3)
	if '@' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*عذراً عزيزي ✵* [{}](t.me/{}) 
*لايمكنك ارسال المعرفات *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="abbas")
	if 'https' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*عذراً عزيزي *✵ [{}](t.me/{})
*لا يمكنك ارسال الروابط*""".format(f2,t2),parse_mode="abbas",disable_web_page_preview=True)
	if message.text == "تثبيت" or message.text == "ت" or message.text == "bin":
	  if message.reply_to_message:
	  	bot.pin_chat_messages(message.chat.id,message.reply_to_message.message_id)
	  	bot.reply_to(message,"تم تثبيت الرسالة!")
	  
	if message.text == "الغاء تثبيت" or message.text == "unban" or message.text == "الغاء التثبيت":
		if message.reply_to_message:
			bot.unpin_all_chat_message(message.chat.id,message.reply_to_message.message_id)
			bot.reply_to(message,"تم الغاء تثبيت الرسالة!") 
	if m == "المطور" or m == "مطور" or m == "المبرمج":
		p3 = types.InlineKeyboardMarkup()
		e4 = types.InlineKeyboardButton(text = "المطور .",url="t.me/o_z_g")
		p3.add(e4)
		h = """[مطور السورس .](t.me/o_z_)"""
		bot.reply_to(message,h,parse_mode="abbas",reply_markup=p3,disable_web_page_preview=True)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		l = bot.export_chat_invite_link(message.chat.id)
		y = f"http://t.me/{message.chat.username}/{message.id}"
		o = message.text
		bot.send_message(elhypamody,"""*المستخدم *: [{}](t.me/{})

*رابط المجموعة : {}

رابط الرسالة : {}

الرسالة : {}*""".format(f2,t2,l,y,o),disable_web_page_preview=True,parse_mode="abbas")
	if m == "اسمي":
		f2 = message.from_user.first_name
		f3 = message.from_user.last_name
		bot.reply_to(message,f"""*𖡋 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⌯ {f2}
		
𖡋𝐋𝐀𝐒𝐓 𝐍𝐀𝐌𝐄 ⌯ {f3}*""",parse_mode="abbas")
	if m == "اليوزر" or m == "يوزري":
			t2 = message.from_user.username
			bot.reply_to(message,f"*𖡋 𝐔𝐒𝐄𝐑 ⌯ @{t2}*",parse_mode="abbas")				
	if m == "الباجر عطلة" or m == "باجر عطلة":
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		bot.reply_to(message,f"*𖡋 𝐁𝐈𝐎 ⌯ {bio}*",parse_mode="abbas")				
	if m == "الباجر عطلة" or m == "باجر عطلة":
		if message.reply_to_message:
			info = bot.get_chat(message.reply_to_message.from_user.id)
			bio = info.bio
			bot.reply_to(message,f"*𖡋 𝐁𝐈𝐎 ⌯ {bio}*",parse_mode="abbas")					
	elif message.text == "mmmmmmmmmmaaaaall" or message.text == "آآ✓♡آقا":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			c = message.reply_to_message.from_user.id
			k = message.reply_to_message.from_user.username
			d = time.strftime("%p %H:%M")
			
			bot.reply_to(message,text="""*𖡋 𝐈𝐃 ⌯ {} 

𖡋 𝐔𝐒𝐄𝐑 ⌯ @{}

𖡋 𝐓𝐈𝐌𝐄 ⌯  {}*""".format(c,t2,d),parse_mode="abbas")		
	if message.text == "mmmmmmmmmmaaaaall حيوان" or message.text == "نوع الحيوان":
			h222 = ['%90','%80','%70','%60','%50','%40','%30','%20','%10']
			s222 = ["جلب🦮","مطي🐴","بقرة🐄","ثور🐂","فأر🐀","قنفذ🐿","كلب الماي🐩","صخل 🐐","اسد 🦁"]
			r222 = random.choice(h222)
			d222 = random.choice(s222)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,text="""*اسم الحيوان :* [{}](t.me/{})* 
نسبة الحيوان : {}
نوع الحيوان : {}*""".format(f2,t2,r222,d222),disable_web_page_preview=True,parse_mode="abbas")
	if message.text == "السورس" or message.text == "سورس":
	    url = ["https://telegra.ph/file/6ce3c04dd7d3348067f0d.jpg","https://telegra.ph/file/6ce3c04dd7d3348067f0d.jpg","https://telegra.ph/file/6ce3c04dd7d3348067f0d.jpg","https://telegra.ph/file/6ce3c04dd7d3348067f0d.jpg"]
	    p3 = types.InlineKeyboardMarkup()
	    e3 = types.InlineKeyboardButton(text = "قناة السورس .",url="")
	    e4 = types.InlineKeyboardButton(text = "المطور .",url="@o_z_g")
	    p3.add(e3,e4)
	    r = random.choice(url)
	    h = """اهلا وسهلا بكم في بوت نبا 
[قناة السورس .](t.me/o_z_g)
[مطور السورس .](t.me/o_z_g)"""
	    bot.send_photo(message.chat.id,r,h,reply_to_message_id=message.message_id,reply_markup=p3,parse_mode="abbas")
	if message.text == "e":
		c = bot.get_chat_member_count(chat_id)
		bot.reply_to(message,f"{c}")
	if message.text == "اطردني" or message.text == "غادر":
		i = message.from_user.id
		bot.kick_chat_member(message.chat.id,i)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="*تم حظرك من المجموعة↩️ :* [{}](t.me/{})".format(f2,t2,i),parse_mode="abbas",disable_web_page_preview=True)
	if message.text == "حظر" or message.text == "طرد" or message.text == "حضر":
		if message.reply_to_message.from_user.id:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*تم حظر العضو ↩️ :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="abbas",disable_web_page_preview=True)
	if message.text == "حظر" or message.text == "طرد" or message.text == "حضر":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*تم حظر العضو ↩️ :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="abbad",disable_web_page_preview=True)
	if message.text == "الغاء حظر" or message.text == "الغاء الحظر":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.unban_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,"""*تم الغاء حظر العضو ↩️ :* [{}](t.me/{}) """.format(f2,t2,vv,bb),disable_web_page_preview=True,parse_mode="abbas")
	if message.text == "الاوامر" or message.text == "اوامر":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "حياكم في بوت نبا",url="")
		A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
		A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
		A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
		A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")
		p3.add(A1,A2)
		p3.add(A3,A4)
		p3.add(p5)
		f2 = message.from_user.first_name 
		t2 = message.from_user.username
		bot.reply_to(message,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في اوامر البوت، 
اختر من الازرار،*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="abbas",reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "حياكم في بوت نبا",url="t.me/o_z_g")
	p3.add(p5)
	if message.text == "تمبلر" or message.text == "صور تمبلر" or message.text == "افتار تمبلر":
		photo_str =  random.randint(74,154)
		avtar_ainme = "https://t.me/o_z_g/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ainme,"""*تم اختيار صوره تمبلر اليك،
- - - -- - - - - -- - - - -
CH - @o_z_g*""",parse_mode="",reply_to_message_id=message.message_id,reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "حياكم في بوت نبا",url="t.me/o_z_g")
	p3.add(p5)
	
	
	if "تاك" in message.text:
	 m = message
	 mm = message.text
	 k = "ليش ماكدر دز صور حب ديصيحوك 🕸️ "
	 rep=str(message.text).split(" ")
	 bot.reply_to(m,mm.replace("تاك"," ليش ماكدر دز صور حب ديصيحوك 🕸️"))	
	if message.text == "لاعبين" or message.text == "لاعب" or message.text == "افتار لاعب" or message.text == "افتار لاعبين":
		photo_str =  random.randint(74,154)
		avtar_ball = "https://t.me/o_z_g/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ball,"""*تم اختيار صورة لاعب اليك،
- - - -- - - - - -- - - - -
CH - @o_z_g*""",parse_mode="o_z_g",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "ريمكس" or message.text == "مكس" or message.text == "ريم":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/o_z_g/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*✯ تم ختيار ريمكس اليك، 
- @bbbbbbhsyddbot*""",parse_mode="o_z_g",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "شعر" or message.text == "ش":
		song_str = random.randint(74,904)
		song_voice = "https://t.me//" + str(song_str)
		bot.send_voice(message.chat.id,song_voice,"""*✯ تم ختيار شعر اليك، 
- @bbbbbbhsyddbot*""",parse_mode="o_z_g",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "غنيلي" or message.text == "غ":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/o_z_g/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*✯ تم ختيار اغنية لك، 
- @bbbbbbhsyddbot*""",parse_mode="o_z_g",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "وينج نبا":
		bot.reply_to(message,"لحضه")
	elif message.text == "وين رحتي نبا ":
		bot.reply_to(message,"ماما صاحتني")
	elif message.text=="نبا تعاي بسرعة":
		bot.reply_to(message,"ها شكو شصاير")
	elif message.text=="تفاحه منو حبيبت عباس":
			bot.reply_to(message,"نبا 😂")
	elif message.text=="تفاحه صدك نبا تحب عباس":
			bot.reply_to(message,"اي والله ")
	elif message.text=="شلونك استاد":
			bot.reply_to(message,"تمام وانت 🌹")
	elif message.text=="نبا غنيلي":
			bot.reply_to(message,"والله العظيم صوتي مو حلو ")
	elif message.text=="اشاقة":
			bot.reply_to(message,"ممنوع الشقة افتهمت ")
	elif message.text=="شقة":
			bot.reply_to(message,"ممنوع الشقة افتهمت ")
	elif message.text=="استاد":
		bot.reply_to(message,". جاي اشوف كلشي ")
	elif message.text=="ليش ماكدر دز صورو اتصال ":
		bot.reply_to(message,"مو ب اي وقت حبيبي .")
	elif message.text=="بوت":
		bot.reply_to(message,"ادارة التقياء المسائية ")
		
	elif "حسابه" in message.text or "حسابي " in message.text or "حساب"in message.text:
		bot.reply_to(message,"شنو طار ؟؟")#جمع الاوامر 

	elif message.text =="نبا":
		bot.reply_to(message,"اعيون نبا")
	elif message.text=="نبا ":
		bot.reply_to(message,"يروحي ها")
	elif message.text=="نبا":
		bot.reply_to(message,"ها حبيبتي)
	elif message.text=="نبا":
		bot.reply_to(message,"ها حياتي")
	elif message.text =="نبا":
	  bot.reply_to(message,"ها شتريد خبصتني")
	elif message.text =="نبو":
	  bot.reply_to(message,"ها حبيبي")
	 
	elif message.text =="ليش ماكدر دز صور" :
		bot.reply_to(message,"دزهن للمالك هوة يرجع يدزهن")

	  
	
	m = message.text	
	if m == "التقويم" or m == "تقويم" or m == "السنة" or m == "التاريخ":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "حياكم بكروب نبا",url="t.me/o_z_g")
		
		p3.add(p5)
		t = time.strftime("%p%H:%S")
		t = time.strftime("%Y/%m/%d %A %b")
		bot.reply_to(message,f"التقويم ⇜{t}",reply_markup=p3)
	
			
	m = message.text
	if m == "الساعة" or m == "الساعه" or m == "الوقت":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "حياكم في بوت نبا",url="t.me/o_z_g")
		p3.add(p5)
		t = time.strftime("%p %H:%S")
		bot.reply_to(message,f"الساعة ⇜{t}",reply_markup=p3)	
	m = message.text
	if m == "صورتي" or m == "الصورة" or m == "بروفايلي":
		url = f"https://t.me/{message.from_user.username}"
		bot.send_photo(message.chat.id,url,reply_to_message_id=message.message_id)
	if "." in message.text:
	 m = message.text
	 k = "الهم صلي على محمد وآل محمد "
	 rep=str(message.text).split(".")
	 bot.reply_to(message,k+m)	
	m = message.text		
	if m == "الرابط" or m == "رابط" :
		l = bot.export_chat_invite_link(message.chat.id)
		bot.reply_to(message,f"""*رابط المجموعة ↩️ : 
{l}*""",parse_mode="abbas")
	     	
	if message.text == "ذ" or message.text == "ذكر" or message.text == "ايه" or message.text == "اية" or message.text == "اذكار":
	  p3 = types.InlineKeyboardMarkup()
	  p5 = types.InlineKeyboardButton(text = "حياكم بكروب نبا",url="t.me/o_z_g")
	  url = "https://ApiAzkar.amoapi.repl.co"
	  msg = message.text
	  p3.add(p5)
	  t = requests.get(url).text
	  j = """   بــــــسم الله الــــــࢪحــــمٰـــن الـــــࢪحـــيــم
     ============================"""
	  bot.reply_to(message,f"*{j}\n{t}*",parse_mode="abbas",reply_markup=p3)

	if message.text == 'كت' or message.text == 'كت تويت' or message.text == "تت":

	    	p3 = types.InlineKeyboardMarkup()
	    	p5 = types.InlineKeyboardButton(text = "حياكم بكروب نبا",url="t.me/o_z_g")
	    	p4 = types.InlineKeyboardButton(text ='↫التالي↬', callback_data= 'c2')
	    	r = random.choice(abod)
	    	p3.add(p4)
	    	p3.add(p5)
	    	bot.reply_to(message,f"""*{r}
- - - - - - - - - - - - - 
@bbbbbbhsyddbot*""",parse_mode="abbas",reply_markup=p3)
@bot.callback_query_handler(func= lambda call : True)
def callback_data(call):
  
  if call.data == "c2":
  	r = random.choice(abod)
  	p3 = types.InlineKeyboardMarkup()
  	p5 = types.InlineKeyboardButton(text = "حياكم في بوت نبا",url="t.me/o_z_")
  	p4 = types.InlineKeyboardButton(text ='↫التالي↬', callback_data= 'c2')
  	p3.add(p4)
  	p3.add(p5)
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""*{r}
- - - - - - - - - - - - - -
@bbbbbbhsyddbot*""",reply_markup=p3,parse_mode="abbas")
  p3 = types.InlineKeyboardMarkup()
  s0 = types.InlineKeyboardButton(text = "رجوع",callback_data="s0")
  A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
  A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
  A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
  A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")
  p3.add(A1,A2)
  p3.add(A3,A4)
  if call.data == "s0":
  	f2 = call.from_user.first_name
  	t2 = call.from_user.username
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في اوامر البوت، 
اختر من الازرار،*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="abbas",reply_markup=p3)
  
  if call.data == "A1":
      p3 = types.InlineKeyboardMarkup()
      s0 = types.InlineKeyboardButton(text = "رجوع",callback_data="s0")
      p3.add(s0)
      bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""*اوامر الحماية
  - - - - - - - - - - - - - 
 حظر <<
 الغاء حظر << 
 كتم <<
 الغاء كتم <<
 تقيد <<
 ايدي <<
 mmmmmmmmmmaaaaall بالرد <<
 حسابي <<
 صورتي <<
 اسمي <<
 الوقت <<
 التاريخ <<
 تاك باليوزر <<
 الرابط <<
 المطور <<*""",parse_mode="abbad",reply_markup=p3)
  
#####+#####
u = 70
a = 1
uu = u - a 
print(f"f > m  = {uu}")
bot.polling()
