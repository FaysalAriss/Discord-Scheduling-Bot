def handleResponses(message):
    message = message.lower()

    if message == "hello":
        return "Hi"
    
    return "I am online"

async def sendMessage(message, strMessage, isPrivate):
    try:
        response = rs.handleResponses(strMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)