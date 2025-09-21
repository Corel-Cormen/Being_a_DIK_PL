init -1:
    python:
        def chat_append_reply_josy():
            global chat_reply
            global chat_josy_history_is_them
            global chat_josy_history
            if chat_reply != None and chat_reply != "":
                chat_josy_history_is_them.append(False)
                chat_josy_history.append(chat_reply)
            chat_reply = ""
            return
        def chat_get_replies_josy():
            global chat_reply_array
            global chat_next_state_array
            global chat_josy_state
            global phone_chat_josy_new
            if phone_chat_josy == 1:
                if chat_josy_state == "1":
                    chat_reply_array = ["Nie mogę się doczekać dzisiejszego wieczoru!","Co tam u Ciebie? Czekasz na wieczór?",""]
                    chat_next_state_array = ["h2a","h2b",""]
                elif chat_josy_state == "2a" or chat_josy_state == "2b":
                    chat_reply_array = ["Cokolwiek wybierzesz, na pewno będzie Ci pasować.","Ja też stoję tu półnago.",""]
                    chat_next_state_array = ["h3a","h3b",""]
                elif chat_josy_state == "3b":
                    chat_reply_array = ["Haha! Myślę, że tak. Do zobaczenia wkrótce!","Kłamiesz. Ale niezła próba.",""]
                    chat_next_state_array = [" ","h4a",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 2:
                if chat_josy_state == "1":
                    chat_reply_array = ["You look very pretty in that, Josy.","Looks great! Can I see the backside, too?",""]
                    chat_next_state_array = ["h2a","h2b",""]
                elif chat_josy_state == "2b":
                    chat_reply_array = ["Haha, I know! Not that I do that myself...","Well, I still liked it.",""]
                    chat_next_state_array = [" "," ",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 3:
                if chat_josy_state == "1":
                    chat_reply_array = ["Hey! Weekend's almost here. I can't wait to see you again.","",""]
                    chat_next_state_array = ["h2a","",""]
                elif chat_josy_state == "2a":
                    chat_reply_array = ["That's not a stupid question. I like beer. Why do you ask?","That's not a stupid question. I like wine. Why do you ask?",""]
                    chat_next_state_array = ["h3a","h3b",""]
                elif chat_josy_state == "3a" or chat_josy_state == "3b":
                    chat_reply_array = ["What about you, then? Do you prefer flowers or chocolate?","",""]
                    chat_next_state_array = ["h4a","",""]
                elif chat_josy_state == "4a":
                    chat_reply_array = ["You'll see this weekend.","",""]
                    chat_next_state_array = ["h5a","",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 5:
                if chat_josy_state == "1":
                    chat_reply_array = ["Hey, are you ok? I've tried calling you a few times.","",""]
                    chat_next_state_array = [" ","",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 6:
                if chat_josy_state == "1":
                    chat_reply_array = ["Please, let me be alone. I need to think.","What do you want from me?",""]
                    chat_next_state_array = ["h2a","h2b",""]
                elif chat_josy_state == "2a":
                    chat_reply_array = ["No there aren't. I understand it perfectly, Josy.","I'm sick of being lied to!",""]
                    chat_next_state_array = ["h3a","h3b",""]
                elif chat_josy_state == "2b":
                    chat_reply_array = ["Then what am I to you?","Please, let me be alone. I need to think.",""]
                    chat_next_state_array = ["h3c","h2a",""]
                elif chat_josy_state == "3a" or chat_josy_state == "4a" or chat_josy_state == "4b":
                    chat_reply_array = ["This is too much for me right now. I need to think.","",""]
                    chat_next_state_array = [" ","",""]
                elif chat_josy_state == "3b":
                    chat_reply_array = ["Like I told you before, this is not all about you. It's about Maya, too.","This is too much for me right now. I need to think.",""]
                    chat_next_state_array = ["h4a"," ",""]
                elif chat_josy_state == "3c":
                    chat_reply_array = ["Right. You sure went fast from wanting to leave everything behind to being with her again.","This is too much for me right now. I need to think.",""]
                    chat_next_state_array = ["h4b"," ",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 7:
                if chat_josy_state == "1":
                    chat_reply_array = ["How did she take it?","I thought about it too before going to bed and I agree, let's not hide things like that from each other.",""]
                    chat_next_state_array = ["h2a","h2b",""]
                elif chat_josy_state == "2a":
                    chat_reply_array = ["We should talk about this when we're together.","Ok, I understand that. This relationship, or what you can call it, is tricky.",""]
                    chat_next_state_array = ["h3a","h3b",""]
                elif chat_josy_state == "2b":
                    chat_reply_array = ["Good. We should talk about this when we're together.","I'm still thinking about how great that sex was with you.",""]
                    chat_next_state_array = ["h3a","h3c",""]
                elif chat_josy_state == "3a" or chat_josy_state == "3b" or chat_josy_state == "3c":
                    chat_reply_array = ["I'll probably find some time to drop by soon.","",""]
                    chat_next_state_array = ["h4a","",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 8:
                if chat_josy_state == "1":
                    chat_reply_array = ["Something wrong?","",""]
                    chat_next_state_array = ["h2","",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            elif phone_chat_josy == 9:
                if chat_josy_state == "1":
                    chat_reply_array = ["Thanks, Josy.","",""]
                    chat_next_state_array = [" ","",""]
                else:
                    chat_reply_array = ["","",""]
                    chat_next_state_array = ["","",""]
                    phone_chat_josy_new = False
            return
        def chat_them_replies_josy():
            global chat_josy_state
            global chat_josy_history_is_them
            global chat_josy_history
            global phone_chat_josy_new
            global dtype
            global ep1_josy_chat1_state
            global RPjosy
            global ep1_josy_prefer_beer
            global ep1_josy_prefer_wine
            global ep2_fuckedJosy
            global ep1_josy_prefer_flowers
            global phone_call_josy
            if chat_josy_state[0] == "h":
                chat_josy_history_is_them.append(True)
                chat_josy_state = chat_josy_state[1:]
                if phone_chat_josy == 1:
                    if chat_josy_state == "2a":
                        chat_josy_history.append("Och! Ja też! Właśnie wyszłam spod prysznica. Nie mogę się zdecydować, co założyć...")
                    elif chat_josy_state == "2b":
                        chat_josy_history.append("Tak! Właśnie wyszłam spod prysznica. Nie mogę się zdecydować, co założyć...")
                    elif chat_josy_state == "3a":
                        chat_josy_history.append("Ok! No to piżama! Lol, żartuję!")
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                    elif chat_josy_state == "3b":
                        chat_josy_history.append("Lol! Tylko półnagi? W takim razie cię pokonałam.")
                    elif chat_josy_state == "4a":
                        if dtype < 1:
                            chat_josy_history_is_them.append(True)
                            ep1_josy_chat1_state = 2
                            chat_josy_history.append("chat_josy_pic1_thumb")
                            chat_josy_history.append("Czy to wygląda dla ciebie jak kłamstwo?")
                        else:
                            chat_josy_history.append("Gdybyś tylko widział... Dobra, muszę znaleźć coś do ubrania. Do zobaczenia wkrótce!")
                            ep1_josy_chat1_state = 1
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                elif phone_chat_josy == 2:
                    if chat_josy_state == "1":
                        chat_josy_history.append("Hey, look at what I bought today!")
                        chat_josy_history.append("chat_josy_pic2_thumb")
                        chat_josy_history_is_them.append(True)
                    elif chat_josy_state == "2a":
                        chat_josy_history.append("Aw... Thank you! You're the first one who's seen me in it.")
                        RPjosy += 1
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                    elif chat_josy_state == "2b":
                        chat_josy_history.append("Sure!")
                        chat_josy_history.append("chat_josy_pic3_thumb")
                        chat_josy_history.append("Lol! I just saw that pic. It's hard taking pictures of my back.")
                        chat_josy_history_is_them.append(True)
                        chat_josy_history_is_them.append(True)
                elif phone_chat_josy == 3:
                    if chat_josy_state == "2a":
                        chat_josy_history.append("Me too. Stupid question... Do you like wine or beer better?")
                    elif chat_josy_state == "3a":
                        chat_josy_history.append("Haha! You'll see this weekend.")
                        ep1_josy_prefer_beer = True
                    elif chat_josy_state == "3b":
                        chat_josy_history.append("Haha! You'll see this weekend.")
                        ep1_josy_prefer_wine = True
                    elif chat_josy_state == "4a":
                        chat_josy_history.append("Oh, flowers, for sure. Why?")
                        ep1_josy_prefer_flowers = True
                    elif chat_josy_state == "5a":
                        chat_josy_history.append("Haha! You're such a TEASE!")
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                elif phone_chat_josy == 6:
                    if chat_josy_state == "1":
                        chat_josy_history.append("I'm sorry, [name]. This isn't how I imagined it would be. Can we talk?")
                    elif chat_josy_state == "2a":
                        chat_josy_history.append("Ok... But there are things to be explained, you know? Things that need more time to be explained than over a heated chat in a bathroom stall.")
                    elif chat_josy_state == "2b":
                        chat_josy_history.append("It's so hard to put words to my feelings. I may have been too harsh by saying that I don't know what you are to me.")
                    elif chat_josy_state == "3a":
                        chat_josy_history.append("How could you!? You only see what's in front of you. There's no way that you could understand what it's been like for me and Maya without us telling you.")
                    elif chat_josy_state == "3b":
                        chat_josy_history.append("I'm not a liar. I'm really not. I just couldn't tell you about her. I told you that I was in a relationship and that wasn't a lie.")
                    elif chat_josy_state == "3c":
                        chat_josy_history.append("You're someone more than just a friend...")
                        chat_josy_history.append("...but so is Maya.")
                        chat_josy_history_is_them.append(True)
                    elif chat_josy_state == "4a":
                        chat_josy_history.append("That's exactly why we should talk.")
                    elif chat_josy_state == "4b":
                        chat_josy_history.append("Maya and I talked last night. We fought, too... But talking to her like that again, it changed things for us.")
                elif phone_chat_josy == 7:
                    if chat_josy_state == "1":
                        chat_josy_history.append("Morning, [name]. I told Maya about what we did last night. I kind of felt weird, as if we did that behind her back or something. I don't know if you agree or not.")
                    elif chat_josy_state == "2a":
                        chat_josy_history.append("Don't worry, she took it well. She asked a lot of questions. I think she felt a bit insecure since she's not experienced with boys.")
                    elif chat_josy_state == "2b":
                        chat_josy_history.append("I'm happy you said that. We both agree.")
                    elif chat_josy_state == "3a":
                        chat_josy_history.append("Yes! And in a sober state! Haha! I think that will be good for everyone.")
                        chat_josy_history.append("You're dropping by later?")
                        chat_josy_history_is_them.append(True)
                    elif chat_josy_state == "3b":
                        chat_josy_history.append("It is. But like I told you last night, we'll take it slow and see what happens. And communication is so important!")
                        chat_josy_history.append("You're dropping by later?")
                        chat_josy_history_is_them.append(True)
                    elif chat_josy_state == "3c":
                        chat_josy_history.append("[name]... You're making me blush right now. And yeah, I can't stop smiling when I think about it.")
                        if ep2_fuckedJosy:
                            chat_josy_history.append("And no parents walking in on us this time! Haha!")
                            chat_josy_history_is_them.append(True)
                        chat_josy_history.append("You're dropping by later?")
                        chat_josy_history_is_them.append(True)
                    elif chat_josy_state == "4a":
                        chat_josy_history.append("Great, see you later then.")
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                elif phone_chat_josy == 8:
                    if chat_josy_state == "1":
                        chat_josy_history.append("Call us when you see this!")
                    elif chat_josy_state == "2":
                        if phone_call_josy == "NONE":
                            chat_josy_history.append("Haha! I sent this before you called me. Ignore it.")
                        else:
                            chat_josy_history.append("No, but call me!")
                        chat_josy_state = " "
                        phone_chat_josy_new = False
                elif phone_chat_josy == 9:
                    if chat_josy_state == "1":
                        chat_josy_history.append("I saw that your birthday was yesterday. Happy birthday! I hope it was a good one. XO")
            elif chat_josy_state[0] == " ":
                chat_reply_array = ["","",""]
                chat_next_state_array = ["","",""]
                phone_chat_josy_new = False
            return

return