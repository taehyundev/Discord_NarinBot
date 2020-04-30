import discord
import asyncio
import openpyxl
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("식사")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!기억 초기화") or message.content.startswith("!기억초기화"):
        file = openpyxl.load_workbook("memory.xlsx")
        sheet = file.active
        for i in range(1, 251):
            sheet["A"+str(i)].value = "-"
        await client.send_message(message.channel, "기억초기화 완료")
        file.save("memory.xlsx")

    if message.content.startswith("!학습"):
        file = openpyxl.load_workbook('memory.xlsx')
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 201):
            if sheet["A"+str(i)].value == "-":
              #  await client.send_message(message.channel, "기억되었습니당")
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                break
        file.save("memory.xlsx")
    if message.content.startswith("!리스트"):
        await message.channel.send("<현재 학습리스트>")
        file = openpyxl.load_workbook('memory.xlsx')
        sheet = file.active
        for i in range(1, 201):
            if sheet["A"+str(i)].value == "-":
                await message.channel.send("끗")
                break
            else:
                await message.channel.send(sheet["A"+str(i)].value+", "+ sheet["B" + str(i)].value)
        print("Good ! ")
    if message.content.startswith("+ "):
        file = openpyxl.load_workbook('memory.xlsx')
        sheet = file.active
        memory = message.content.split(" ")
        search = False
        for i in range(1, 201):
            if sheet["A" + str(i)].value == memory[1]:
                await message.channel.send(sheet["B" + str(i)].value)
                search = True
                break
        
        if search == False:
            await message.channel.send("무슨 뜻인지 모르겠어요..")
        else:
            search = False



client.run('token')
