import discord, asyncio, random


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("완료")
    game = discord.Game("노동 당")
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
async def on_message(message, discord=None):

    if message.content == "ㅎㅇ" or message.content == "안녕":
        await message.channel.send("👋")

    if message.content.startswith("ㅗ"):
        await message.channel.send("🖕")

    if message.content.startswith("몇살이니"):
        await message.channel.send("ㅋ")

    if message.content.startswith == "잔다" or message.content.startswith == "잘게":
        await message.channel.send("🌜굿나잇")

    if message.content.startswith("우하하하"):
        await message.channel.send("빵빠레")

    if message.content.startswith("닭이 옷을 입을때 내는 소리는?"):
        await message.channel.send("꼭끼오")

    if message.content.startswith("세상에서 가장 착한사자는?"):
        await message.channel.send("자원봉사자")

    if message.content.startswith("토끼털을 빗어주는 빗은?"):
        await message.channel.send("래빗")

    if message.content.startswith("미안한 동물은?"):
        await message.channel.send("오소리")

    if message.content.startswith("오이가 도망가면?"):
        await message.channel.send("오...이런")

    if message.content.startswith("잉"):
        await message.channel.send("기모링")

    if message.content == "헤이 자비스" or message.content == "야 자비스" or message.content == "비서" or message.content == "헤이" or message.content == "자비스":
        await message.channel.send("예스 마수터")

    if message.content == "ㅇㅇㄴㅇ" or message.content == "응 아니야":
        await message.channel.send("응 니얼굴")

    if message.content.startswith(".짤"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("용가리"):
        await message.channel.send("🐉")

    if message.content.startswith("꼬앵이"):
        await message.channel.send("```∧__∧\n(  ･ω･)\n(っ▄︻▇〓▄︻┻┳═一　　*  *  *  *  *  *  *  *  *\n/　   )\n( /￣∪\n```")

    if message.content.startswith("댄스"):
        await message.channel.send("```∧__∧\n(  ･ω･) 댄su\n(っ  っ)  댄su\n/　 x  )\n( /￣∪\n```")

    if message.content.startswith("둠칫"):
        await message.channel.send("⊂ヽ\n　 ＼＼ Λ＿Λ\n　　 ＼( ‘ㅅ’ )\n　　　 >　⌒ヽ\n　　　/ 　 へ＼\n　　 /　　/　＼＼\n　　 ﾚ　ノ　　 ヽつ\n　　/　/\n　 /　/|\n　(　(ヽ\n　|　|、＼\n　| 丿 ＼ ⌒)\n　| |　　) /\n`ノ )　　Lﾉ\n")


    if message.content == "야":
        await message.channel.send("🤔무슨일이신가요?")

    if message.content.startswith("랜덤"):
        for i in range(1, 5):
            await message.channel.send(random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9']))

    if message.content.startswith("10초 타이머"):
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났습니다")

    if message.content == "투명댓글" or message.content == "은신모드":
        await message.channel.send("﻿")

    if message.content.startswith("if"):
        await message.channel.send("뭐냐 코드냐?")

    if message.content.startswith("ㅇㅈ"):
        await message.channel.send("요정")

    if message.content.startswith("@ㅐ"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("느그"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("너가 좋아하는 게임은 뭐니"):
        await message.channel.send("뭘까")

    if message.content.startswith("밀크초코 레시피"):
        await message.channel.send("```밀크초코 레시피```")
        await message.channel.send("```1 블럭형 밀크커버춰는 칼로 잘게 다져서 준비해주세요.```")
        await message.channel.send("```2 설탕과 꿀을 이용해서 카라멜화 해줄꺼예요. 설탕, 꿀을 냄비에 넣고 중약불로 가열해줍니다.```")
        await message.channel.send("```3 카라멜을 만들기 위해서 생크림도 나중에 섞어줄건데요, 설탕을 카라멜화 하는 동안 생크림도 따로 뜨겁게 데워주세요.```")
        await message.channel.send("```4 설탕과 꿀이 바글바글 끓어 색이 갈색으로 변할때까지 가열해주다가, 뜨겁게 데운 생크림을 조금씩 부어가면서 섞어주세요. 생크림을 넣으면 갑자기 끓어오르기 때문에 조심하셔야 해요!```")
        await message.channel.send("```5 한참을 끓여주다보면 부풀어 올랐던 거품이 조금 사그라들고, 색이 좀 진해져서 카라멜의 색으로 변할꺼예요. 그때까지 끓여주시면 되요. (약 115℃ 정도까지 끓이다가 불에서 내려주시면 되어요.)```")
        await message.channel.send("```6 다져둔 밀크초콜릿을 넣어서 고루 섞어 초콜릿을 녹여줍니다. 초콜릿이 다 녹으면 실온에 두었던 버터를 넣어서 녹여주세요.```")
        await message.channel.send("```7 유산지를 깔아둔 틀에 초콜릿카라멜을 부어주고, 시원한 곳에 놓아두어 단단해지게 해줍니다.```")
        await message.channel.send("```8 완전히 식어서 카라멜이 굳으면 원하는 크기로 썰어서 포장해주시면 되어요.```")

    if message.content.startswith("삐쓰까또레부르쥬미첼라햄페스츄리치즈나쵸스트링스파게티"):
        await message.channel.send("```검색결과```")
        await message.channel.send("```이름 : 삐쓰까또레부르쥬미첼라햄페스츄리치즈나쵸스트링스파게티```")
        await message.channel.send("```설명: 어느 음식대회에서 그 오묘한 맛으로 우승을 했다는 스파게티!!```")
        await message.channel.send("```가격 : 2000원```")
        await message.channel.send("```출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jjoda3&logNo=80004708896```")

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("시발"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("ㄳㄲ"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("개새끼"):
        await message.channel.send("어허 떽!!!!!!!!!!!")

    if message.content.startswith("ㅡㅡ"):
        await message.channel.send("쩦....어디 불편한거 있남?;;")

    if message.content.startswith("ㅠ"):
        await message.channel.send("쩦....울고싶으면 딴데에서 울으삼;;")

    if message.content.startswith(".play"):
        await message.channel.send("쩦....뭐 좋은노래 없남?;;")

    if message.content.startswith("이시키야"):
        await message.channel.send("저기그... 없나?")

    if message.content.startswith("ㅋ"):
        await message.channel.send("나도 같이 웃자 핳핳하핳하핳하하ㅏ하하하ㅏ하ㅏ하ㅏ하")

    if message.content == "넌 누구니" or message.content == "누구냐넌":
        await message.channel.send("저는 엄서버에서 태어난 자비스 입니다.")


    if message.content == "방송":
        await message.channel.send("")


    if message.content.startswith("도지"):
        await message.channel.send("🐕")

    if message.content == "검색":
        await message.channel.send("```검색결과 입니다.```")
        await message.channel.send("https://www.google.com")
        await message.channel.send("https://www.naver.com")
        await message.channel.send("https://www.youtube.com")

    if message.content.startswith("용돈"):
        await message.channel.send("7777019015391 카카오뱅크 이곳으로 보내주시면 됩니다.")

    if message.content.startswith(".추가"):
        await message.channel.send("7777019015391 카카오뱅크 이곳으로 100원을 보내주시면 원하는 것을 추가해 드립니다.")


client.run("ODQxOTUxNjczMjE5OTQwMzYz.YJuOmQ.vcx-xm-TxTabW4w_GO3I0aoYEA0")