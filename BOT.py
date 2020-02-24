import random as r
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


Bot = commands.Bot(command_prefix='!')

del_msg = ['лалка', 'лох', 'lalka', 'дурачок', 'дурачёк', 'блять', 'хуй', 'нахуй', 'охуеть', 'мах', 'max' 'бадан', 'кучка',
	'вонючка', '~', 'писька', 'писюн', 'писка', 'ебал', 'ебать', 'ебу', 'бля', 'пизд', 'piska', 'ахуеть', 'ахуел', 'охуел', 'ебанутый', 
	'ёбнулся', 'ебнулся', 'ебобо', 'дурак']

kl_slova = ['выполнил1', 'не выполнил2']
apptemps = 0
 
@Bot.event
async def on_ready():
	channel = Bot.get_channel(677525223410630676)
	print('Бот запущен. \n Version 3.7')
	await channel.send('Духи не знают усталости!')
	await Bot.change_presence(status=discord.Status.online,activity=discord.Game('🐟'))

@Bot.event
async def on_member_join( member ):
	role = discord.utils.get( member.guild.roles, id=677534143994658873)
	await member.add_roles( role )


@Bot.event
async def on_message(message):
	await Bot.process_commands(message)
	rolePROG = discord.utils.get(message.guild.roles,id=676522408840003613)
	roleIZB = discord.utils.get(message.guild.roles,id=679360497077977109)
	bot_role = discord.utils.get(message.guild.roles,id =676532058348322856)
	rand = r.randint(1, 10)
	if rand == 1:
		fraza = 'Не пиши так, пожалуйста'
	elif rand == 2:
		fraza = 'Зато я умею кикать =)'
	elif rand == 3:
		fraza = 'Ну не надо так выражаться'
	elif rand == 4:
		fraza = 'деньги не портят человека'
	elif rand == 5:
		fraza = 'Банить я ещё, конечно, не умею, но умею кикать!'
	elif rand == 6:
		fraza = 'Используешь запрещённые слова? я сейчас тебя запрещу.'
	elif rand == 7:
		fraza = 'ты меня испытываешь?'
	elif rand == 8:
		fraza = 'всё это глупости'
	elif rand == 9:
		fraza = 'хочешь притчу расскажу?'
	elif rand == 10:
		fraza = 'сегодня ты использовал запрещённое слова, а завтра у тебя стоит роль \'не участвует\' '
	msg = message.content.lower()
	
	channel = Bot.get_channel( 677525223410630676 )

		

	for i in del_msg:
		if i in msg: 
			if rolePROG in message.author.roles or roleIZB in message.author.roles:
				print(f'{message.author.name} сказал: ' + msg)
			else:
				await message.delete()
				await message.author.send( f'{ message.author.name },' + fraza)
				if rand == 2 or rand == 5 and i in msg:
					await message.author.kick()

	
	for i in kl_slova:
		if i in msg:
			if i == 'выполнил1':
				await message.author.send(f' {message.author.name}, молодчина! Получай +1 уровень!')
			elif i == 'не выполнил2':
				await message.author.send(f' {message.author.name}, печально! Понижай свой уровень!')

@Bot.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def role(ctx, member: discord.Member = None, role: discord.Role = None):
	await member.add_roles(role)


@Bot.command( pass_context = True )
async def news(ctx):
	emb = discord.Embed( title = 'Новости', colour = discord.Colour.blue())
	emb.add_field(name = 'Обновлено 24.02(23:14)', value = '-Бот поставлен на бесплатный хостинг. \n-Удалена команда !generate \n-Казино вновь работает только на 1 ур. \n-Команда kazino полностью обновлена, как и команды !lvl_up и !lvl_down.')

	await ctx.send( embed = emb )

@Bot.command( pass_context = True )
async def lvl_up(ctx):
	channel = ctx.channel
	channel_ = Bot.get_channel(676521035247517730)
	if channel == channel_:
		for pos in range(7,56):
			role_lvlup = discord.utils.get(ctx.guild.roles, position = pos)
			if role_lvlup in ctx.author.roles:
				role_lvlup = discord.utils.get(ctx.guild.roles, position = pos+1 )
				await ctx.author.add_roles(role_lvlup)
				role_lvldown = discord.utils.get(ctx.guild.roles, position = pos )
				await ctx.author.remove_roles(role_lvldown)
				break


@Bot.command()
async def lvl_down(ctx):
	for pos in range(7,57):
			role_lvldown = discord.utils.get(ctx.guild.roles, position = pos)
			if role_lvldown in ctx.author.roles:
				role_lvldown = discord.utils.get(ctx.guild.roles, position = pos-1 )
				await ctx.author.add_roles(role_lvlup)
				role_lvldown = discord.utils.get(ctx.guild.roles, position = pos )
				await ctx.author.remove_roles(role_lvldown)
				break
	


@Bot.command( pass_context = True)
@commands.has_permissions( administrator = True )
async def rem_role(ctx, member: discord.Member = None, role: discord.Role = None):
	await member.remove_roles(role)


@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )
async def clear(ctx, amount = 500):
	await ctx.channel.purge( limit = amount )

@Bot.command( pass_context = True)
async def лисик(ctx):
	await ctx.send("ГоТоВ ЛиЗаТь :tongue:")


@Bot.command()
async def kazino(ctx, member: discord.Member = None):
	role1l = discord.utils.get(ctx.guild.roles, id = 677534141289463843)
	if ctx.author.name in member.name:
		await ctx.send('аъхахъахъахъ сыграть в казино с самим собой))?')
	else:
		if role1l in ctx.author.roles or role1l in member.roles:
			await ctx.send('И что, мне теперь нужно нулевые уровни выдавать?') 
		else:
			sogl_role = discord.utils.get(ctx.message.guild.roles, name = 'Согласен')
			if sogl_role in member.roles:
				player1 = r.randint(0,9)
				player2 = r.randint(0,9)
				while player1 == player2:
					player1 = r.randint(0,9)
					player2 = r.randint(0,9)
				await ctx.send('Игрок 1 - ' + str(player1) + '\nИгрок 2 - ' + str(player2))
				await member.remove_roles(sogl_role)
				if player1 > player2:
					guild = ctx.guild
					men = ctx.author
					for pos in range(7,56):
						role_lvldown = discord.utils.get(guild.roles, position = pos)
						if role_lvldown in men.roles:
							role_lvldown = discord.utils.get(guild.roles, position = pos+1 )
							await men.add_roles(role_lvldown)
							role_lvldown = discord.utils.get(guild.roles, position = pos )
							await men.remove_roles(role_lvldown)
							break	
					guild = member.guild
					men = member
					for pos in range(7,57):
						role_lvldown = discord.utils.get(guild.roles, position = pos)
						if role_lvldown in men.roles:
							role_lvldown = discord.utils.get(guild.roles, position = pos-1 )
							await men.add_roles(role_lvldown)
							role_lvldown = discord.utils.get(guild.roles, position = pos )
							await men.remove_roles(role_lvldown)
							break
				
				elif player2 > player1:
					guild = member.guild
					men = member
					for pos in range(7,56):
						role_lvldown = discord.utils.get(guild.roles, position = pos)
						if role_lvldown in men.roles:
							role_lvldown = discord.utils.get(guild.roles, position = pos+1 )
							await men.add_roles(role_lvldown)
							role_lvldown = discord.utils.get(guild.roles, position = pos )
							await men.remove_roles(role_lvldown)
							break	
					guild = ctx.guild
					men = ctx.author
					for pos in range(7,57):
						role_lvldown = discord.utils.get(guild.roles, position = pos)
						if role_lvldown in men.roles:
							role_lvldown = discord.utils.get(guild.roles, position = pos-1 )
							await men.add_roles(role_lvldown)
							role_lvldown = discord.utils.get(guild.roles, position = pos )
							await men.remove_roles(role_lvldown)
							break
			else:
				await ctx.send(f'{member.name} не соглашался.')

@Bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel.id
    await Bot.get_channel(int(channel)).connect()

@Bot.command()
async def leave(ctx):
    await ctx.voice_Bot.disconnect()


@Bot.command()
async def kick_me_please(ctx):
	await ctx.send('Ты будешь кикнут через...')
	sec = 11
	while sec >= 0:
		sec -= 1
		await ctx.send(str(sec))
		await asyncio.sleep(1)
		if sec == 0:
			await ctx.send('Но я немогу просто взять и кикнуть тебя...')
			await asyncio.sleep(3)
			await ctx.send('Я немогу этого сделать...')
			await asyncio.sleep(3)
			await ctx.send('В мире есть столько всего прекрасного...')
			break



@Bot.command(pass_context = True)
async def ready(ctx):
	global apptemps
	roleIZB = discord.utils.get(ctx.guild.roles, id = 679360497077977109)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')
	randper = r.randint(-1, 370)
	eknuty = discord.utils.get(ctx.guild.roles, id = 680882916825628713)
	if ctx.author.name == 'Прокрастинация':
		await ctx.send('Я готов на все ' + str(randper) + '\%')
		if randper == -1:
			if eknuty in ctx.author.roles:
				await ctx.send('Хотя не, не чёкнутый.')
				await ctx.author.remove_roles(eknuty)
			else:
				await ctx.send('Ты чёкнутый?')
				await ctx.author.add_roles(eknuty)
		elif randper == 0:
			await ctx.send('Вот бы никогда больше не быть готовым.')
		elif randper <= 10 and randper > 1:
			await ctx.send('Возможно ли перейти рубеж дивергенции в 1\%?')
		elif randper == 1:
			await ctx.send( str(randper) + ' раз можно и забанить....')
		elif randper > 10 and randper <=30:
			await ctx.send('Для получения 20 уровня необходимо ввести команду: !kick_me_please')
		elif randper >= 31 and randper <=40:
			await ctx.send('Сколько бы ты не падал, однажды ты взлетишь.')
		elif randper >= 41 and randper < 50:
			await ctx.send(':snake: Python one love :heart:')
		elif randper >= 50 and randper <= 68:
			await ctx.send('Это всего лишь рандомные числа.. Какой в этом смысл?')
		elif randper == 59 and randper == 68:
			await ctx.send('Кстати, почти 69')
		elif randper == 69:
			await ctx.author.send('Это же запрещено... Получай мут.')
			await ctx.author.add_roles(mute_role)
			await ctx.send(f'{ctx.author.name}  захотел помолчать.')
		elif randper > 69 and randper <= 80:
			await ctx.send('ОЙ НЕ БУДУ ГОРЕВАТЬ, БУДУ Я рыдать...')
		elif randper > 80 and randper <=99:
			await ctx.send('!лисик')
		elif randper == 100:
			await ctx.send('А ты ничё такой. Чёткий так сказать.')
		elif randper >100 and randper <=150:
			await ctx.send('stav like esli smog pro4itat')
		elif randper > 150 and randper <= 200:
			await ctx.send('Пошли в бравлхаллаааааааааа')
		elif randper >= 201 and randper <= 250:
			rand_formula = r.randint(1, 5)
			if rand_formula == 1:
				await ctx.send('Прослушайте текст и напишите сжатое изложение.')
			elif rand_formula == 2:
				await ctx.send('RussianMnogonoska')
			elif rand_formula == 3:
				await ctx.send('падавать па членику')
			elif rand_formula == 4:
				await ctx.send('!туцы - это мой страх и ужас и кошмар и пипец я что общаюсь как стасик бот которого создал безумный животный макс привет который смотрит хика спидранита')
			else:
				await ctx.send('Сейчас 0:34, я скоро спать пойду..')
		elif randper >= 251 and randper <= 367:
			await ctx.send('Мы все уже знаем максимальное число...')
		elif randper == 368:
			await ctx.send('Старайся лучше.')
		elif randper == 370:
			await ctx.send('Поздравляю! вы дошли до числа 370! А максимальное число теперь AJHfu hwnfjsdnbfv7w3rJUHDFISuifiuh8rfr.')
		else:
			if roleIZB in ctx.author.roles:
				await ctx.send('А теперь заберу роль избранного.')
				await ctx.author.remove_roles(roleIZB)
			else:
				await ctx.send('Теперь ты избранный...')
				await ctx.author.add_roles(roleIZB)
	else:
		apptemps += 1
		if apptemps == 1:
			await ctx.send("I'm ready =)")
		elif apptemps == 2:
			await ctx.send("I'm ready =).")
		elif apptemps == 3:
			await ctx.send('Ай. Эм. Рэди. -_-')
		elif apptemps == 4:
			while apptemps == 4:
				await asyncio.sleep(1)
				await ctx.send("I'M READY >=(")
		elif apptemps == 5:
			await ctx.send('Надоел(((')
		elif apptemps == 6:
			await ctx.send('Не советую меня злить...')


@Bot.command()
async def shop(ctx):
	emb = discord.Embed(title = 'Магазин', colour = discord.Colour.purple())
	emb.add_field(name='Статус боту',value='')


@Bot.command(pass_context = True)
async def Стасик(ctx):
	await ctx.send('Стасик - это я')


@Bot.command(pass_context = True)
async def info(ctx):
	emb = discord.Embed( title = 'Команды общего доступа.', colour = discord.Colour.red())
	emb.add_field(name = '!ready', value = '-Проверить бота на готовность.')
	emb.add_field(name = '!news', value = '-Бот покажет последние новости и когда их обновили.')
	emb.add_field(name = '!лисик', value = '-Всегда готов =).')
	emb.add_field(name = '!Стасик', value = '-Кто тут Стасик??')
	emb.add_field(name = '!lvl_up', value = '-Увеличит ваш уровень на 1(не доступно участникам с ролью "не участвует").(работает только на текстовом канале #Отчёт)')
	emb.add_field(name = '!lvl_down', value = '-Понижает ваш уровень на 1(также не доступно тем, кто не участвует)')
	emb.add_field(name = '!random (наименьшее число) (наибольшее число)', value = '-Вернёт рандомное число по запросу. По умолчанию будут использованны значения 1 и 100.')
	emb.add_field(name = '!kick_me_please', value = '-Command not found.')
	emb.add_field(name = '!kazino (@упоминание)', value = '-Запустит казино на 1 уровень.(чтобы согласиться пропишите !YES в чат.)')
	await ctx.send( embed = emb)


@Bot.command()
async def ball(ctx, *, arg):
	message = ['Нет','Да','Возможно','Опредленно нет','Спроси позже','Немогу определиться...','Бонда подскажет...'] 
	s = r.choice(message)
	await ctx.send(embed = discord.Embed(description = f'**:crystal_ball: Знаки говорят:** {s}', color=0x0c0c0c))
	return

@ball.error 
async def ball_error(ctx, error):

	if isinstance( error, commands.MissingRequiredArgument ): 
		await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите сообщение.', color=0x0c0c0c))  


@Bot.command()
async def YES(ctx):
	role_yes = discord.utils.get(ctx.guild.roles, id = 680409583377711154)
	await ctx.author.add_roles(role_yes)

@Bot.command()
@commands.has_permissions( administrator = True )
async def warning(ctx):
	emb = discord.Embed( title = 'ВНИМАНИЕ', colour = discord.Colour.red())
	emb.add_field(name = 'Обращение к Косте', value = 'Если до 23:00 не будет отчёта, то значит ты его не выполнил =( Твой уровень будет понижен до 4.')
	await ctx.send( embed = emb )

@Bot.command(pass_context = True)
@commands.has_permissions( administrator = True )
async def say(ctx):
	emb = discord.Embed( title = 'Version 3.7', colour = discord.Colour.green())
	emb.add_field(name = 'Информация', value = '\n-Обновлено 24.02 \nДля того, чтобы посмотреть список команд пропишите !info в чат. \nНе забудьте в начале отёта написать команду !lvl_up или !lvl_down.(в соответствии с выполнением или наоборот). В конце своего отчёта написать следующие из ключевых слов: выполнил1, не выполнил2 . \nУ бота есть фильтрация чата. Использовав запертные слова, есть возможность, что бот вас кикнет(она составляет 20 процентов). Роли, которые могу использовать запрещённые слова: Программист, Избранный.')
	await ctx.send( embed = emb)

@Bot.command()
async def random(ctx, rand1=1, rand2=100):
	random = r.randint(int(rand1), int(rand2))
	await ctx.send(str(random))

@Bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member, amount: int):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')
	minuts = amount*60
	await member.add_roles(mute_role)
	await ctx.send(f'{member.mention} доигрался и получил мут. Время: ' + str(amount) + 'мин')
	await asyncio.sleep(minuts)
	await member.remove_roles(mute_role)

Bot.run("Njc2NTI4MjUzMzc2MTM1MjE4.XlQ-YQ.mE_1LBu4Pdia60Z7OLvhaMrPbXY")
