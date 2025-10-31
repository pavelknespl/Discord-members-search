import discord
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

TOKEN = os.getenv("TOKEN_DISCORD")

if len(sys.argv) < 3:
    raise SystemExit("Usage: python main.py <FirstServerId> <SecondServerId>")
try:
    FIRSTSERVERID = int(sys.argv[1])
    SECONDSERVERID = int(sys.argv[2])
except ValueError:
    raise SystemExit("FirstServerId and SecondServerId must be integers (Discord guild IDs).")

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in {client.user}')

    source_guild = client.get_guild(FIRSTSERVERID)
    target_guild = client.get_guild(SECONDSERVERID)

    if not source_guild or not target_guild:
        print("Server not found or unavailable")
        await client.close()
        return

    await source_guild.chunk()
    await target_guild.chunk()

    source_ids = {member.id for member in source_guild.members}
    target_ids = {member.id for member in target_guild.members}

    common_ids = source_ids & target_ids
    common_members = [member for member in source_guild.members if member.id in common_ids]

    print(f"Members on both servers: {len(common_members)}")
    for member in common_members:
        print(f"{member.name}#{member.discriminator}")

    await client.close()

client.run(TOKEN)
