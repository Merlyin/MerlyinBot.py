import hikari
import lightbulb
import random

bot = lightbulb.BotApp(
    token='[BOT TOKEN]',
    default_enabled_guilds=([guilds go here])
)


@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

print(hikari.channels.GuildTextChannel.id)


@bot.command
@lightbulb.command('quit', 'Puts a sudden end to the bot!')
@lightbulb.implements(lightbulb.SlashCommand)
async def quit(ctx):
    await ctx.respond(kill_text_command())
    await bot.close()


def kill_text_command():
    return random.choice(['You killed me... master...',
                          'Avenge me...!', 'Goodbye cruel world...',
                          'beep... beep... beeeeeeep',
                          'No, wait please don\'t-'])


bot.run()
