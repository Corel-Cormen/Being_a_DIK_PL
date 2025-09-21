screen app_chat_josy:
    modal True
    tag app_chat_josy
    add "phone_chat_gui"
    $ renpy.block_rollback()
    if chat_reply != "":
        $ chat_append_reply_josy()
    $ chat_them_replies_josy()
    imagebutton idle "chat_return_idle" hover "chat_return_hover" focus_mask True action Hide("app_chat_josy")
    imagebutton focus_mask True idle Transform("phone_app_off") hover Transform("phone_app_off_hover") action Hide("app_chat_josy") xpos 917 ypos 958
    key "mouseup_2" action Hide("app_chat_josy")
    imagebutton idle "avatar_josy" hover "avatar_josy" action NullAction() xalign 0.45 yalign 0.131
    if phone_chat_josy != 0 and freeRoamID != "ep3_1":
        text "Josy\nDostępna" style "chat_text_style" xalign 0.495 yalign 0.137
    else:
        text "Josy\nNiedostępna" style "chat_text_style" xalign 0.495 yalign 0.137
    if phone_chat_josy != 0 and chat_josy_state != " ":
        imagebutton idle Transform("chat_text_pulse") hover Transform("chat_text_field_hover") action (Function(chat_get_replies_josy),Show("chat_text_selection_josy")) focus_mask True
        text "{size=+5}Wiadomość{/size}" style "swyper_he_text" xalign 0.5 yalign 0.852
    else:
        imagebutton idle Transform("chat_text_field_idle") hover Transform("chat_text_field_idle") action NullAction() focus_mask True
    vpgrid:
        ypos 0.19
        xoffset -1
        yoffset 1
        yminimum 668
        ymaximum 668
        xmaximum 434
        xminimum 434
        cols 1
        spacing 5
        draggable False
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.503
        if len(chat_josy_history_is_them)<10:
            yinitial 0.0
        else:
            yinitial 1.0
        vbox:
            xalign 0.503
            yalign 0.05
            spacing 5
            xoffset 5
            yoffset 5
            ymaximum 668
            xmaximum 434
            xminimum 434
            $ count = 0
            for x in chat_josy_history_is_them:
                if x != None and chat_josy_history[count] != None and chat_josy_history[count] != "":
                    if count > 0 and count == newMessageIntJosy:
                        hbox:
                            frame:
                                xoffset 25
                                xmaximum 360
                                xminimum 360
                                yminimum 40
                                background Frame("chat_new_msg_frame",10,10)
                                text "Nowa wiadomość" style "swyper_he_text" xoffset 115
                    if x == True:
                        hbox:
                            vbox:
                                yalign 0.5
                                frame background "chat_avatar_josy" xmaximum 48 ymaximum 48
                            frame:
                                xoffset 5
                                xmaximum 320
                                background Frame("chat_them_box",10,10)
                                if chat_josy_history[count][0:5] != "chat_":
                                    text chat_josy_history[count] style "swyper_them_text"
                                else:
                                    imagebutton idle chat_josy_history[count] hover chat_josy_history[count]+"_hover" action (Show(chat_josy_history[count].split("_thumb")[0]+"_screen"))
                    elif x == False:
                        hbox:
                            xminimum 360
                            xmaximum 360
                            frame:
                                xalign 1.0
                                background Frame("chat_mc_box",10,10)
                                xmaximum 320
                                xoffset 40
                                if chat_josy_history[count][0:5] != "chat_":
                                    text chat_josy_history[count] style "swyper_he_text"
                                else:
                                    imagebutton idle chat_josy_history[count] hover chat_josy_history[count]+"_hover" action (Show(chat_josy_history[count].split("_thumb")[0]+"_screen"))
                $ count += 1
            text "\n\n\n\n" style "swyper_he_text"
            if len(chat_josy_history_is_them)<10:
                for x in range(0,10-len(chat_josy_history_is_them)):
                    text "\n" style "swyper_he_text"
screen chat_text_selection_josy:
    modal True
    tag chat_text_selection_josy
    vbox:
        xalign 0.78
        yalign 0.75
        spacing 5
        xoffset 5
        yoffset 5
        hbox:
            vbox:
                yalign 0.5
                frame background chat_mc_avatar xmaximum 48 ymaximum 48
            frame:
                background Frame("chat_mc_box",10,10)
                if chat_reply_array[0][0:5] != "chat_":
                    xmaximum 320
                    xminimum 320
                    textbutton "[chat_reply_array[0]]" action (SetVariable("chat_reply", chat_reply_array[0]), SetVariable("chat_josy_state", chat_next_state_array[0]), Hide("chat_text_selection_josy")) text_style "swyper_choice_text"
                else:
                    xmaximum 140
                    xminimum 140
                    imagebutton idle chat_reply_array[0] hover chat_reply_array[0]+"_hover" action (SetVariable("chat_reply", chat_reply_array[0]), SetVariable("chat_josy_state", chat_next_state_array[0]), Hide("chat_text_selection_josy"))
        if chat_reply_array[1] != "":
            hbox:
                vbox:
                    yalign 0.5
                    frame background chat_mc_avatar xmaximum 48 ymaximum 48
                frame:
                    background Frame("chat_mc_box",10,10)
                    if chat_reply_array[1][0:5] != "chat_":
                        xmaximum 320
                        xminimum 320
                        textbutton "[chat_reply_array[1]]" action (SetVariable("chat_reply", chat_reply_array[1]), SetVariable("chat_josy_state", chat_next_state_array[1]), Hide("chat_text_selection_josy")) text_style "swyper_choice_text"
                    else:
                        xmaximum 140
                        xminimum 140
                        imagebutton idle chat_reply_array[1] hover chat_reply_array[1]+"_hover" action (SetVariable("chat_reply", chat_reply_array[1]), SetVariable("chat_josy_state", chat_next_state_array[1]), Hide("chat_text_selection_josy"))
        if chat_reply_array[2] != "":
            hbox:
                vbox:
                    yalign 0.5
                    frame background chat_mc_avatar xmaximum 48 ymaximum 48
                frame:
                    background Frame("chat_mc_box",10,10)
                    if chat_reply_array[2][0:5] != "chat_":
                        xmaximum 320
                        xminimum 320
                        textbutton "[chat_reply_array[2]]" action (SetVariable("chat_reply", chat_reply_array[2]), SetVariable("chat_josy_state", chat_next_state_array[2]), Hide("chat_text_selection_josy")) text_style "swyper_choice_text"
                    else:
                        xmaximum 140
                        xminimum 140
                        imagebutton idle chat_reply_array[2] hover chat_reply_array[2]+"_hover" action (SetVariable("chat_reply", chat_reply_array[2]), SetVariable("chat_josy_state", chat_next_state_array[2]), Hide("chat_text_selection_josy"))
return