import discord
async def sendEmbed(args: str, Context):
    from Aoipy.Classes.AoiPyClient import bots
    split = args.split(";")
    try:
        channel_id = split[0]
        title = split[1]
        message = split[2]
        color = split[3]
        footer = split[4]
        channel = await bots.fetch_channel(int(channel_id))
        embed = eval(f"discord.Embed(title=title, description=message, color=discord.Color.{color}())")
        embed.set_footer(text=footer)
        await channel.send(embed=embed)
    except discord.ClientException:
        raise SyntaxError("Can't send empty message!")
    except IndexError:
        raise SyntaxError("Not enough arguments in $sendEmbed")
    except SyntaxError:
        channel_id = split[0]
        title = split[1]
        message = split[2]
        footer = split[4]
        channel = await bots.fetch_channel(int(channel_id))
        embed = eval(f"discord.Embed(title=title, description=message)")
        embed.set_footer(text=footer)
        await channel.send(embed=embed)
    return