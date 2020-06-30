# Стандартные Python-библиотеки
import asyncio	# Модуль для ассинхронного ввода/вывода
import sqlite3	# Модуль для работы с базами данных 

# Библиотека для создания Discord-бота
import discord
from discord.ext import commands

# Конфигурации бота
import config
from config import TOKEN 

PREFIX = '!'

# Создаем переменную для управления ботом и 'устанавливаем' префикс
bot = commands.Bot( command_prefix = PREFIX)
bot.remove_command('help')	# Удаляем команду help

# Создаем класс игрока, объектами которого будут каждые участники игры
class Player:
	pass
	# Здесь будет код :)

@bot.event
async def on_ready():
	print(" SUCCESS! ")

@bot.event
async def on_member_join(member:discord.Member):
	CountChannel = bot.get_channel(727401938001461298)

	await CountChannel.edit(
			name = "Участников: {}".format(len(member.guild.members))
		)

@bot.event
async def on_member_remove(member:discord.Member):
	CountChannel = bot.get_channel(727401938001461298)

	await CountChannel.edit(
			name = "Участников: {}".format(len(member.guild.members))
		)

# Подключение бота
bot.run(TOKEN)