init:
    style episode_number_title_style:
        color "#ffffff"
        font "cabin-regular.ttf"
        size 50
init:
    style episode_title_style:
        color "#ffffff"
        font "cabin-regular.ttf"
        size 150
screen ep6_title_screen:
    modal True
    tag ep6_title_screen
    timer 5 action Hide("ep6_title_screen")
    if currentEpisode == 1:
        $ episode_title_name = "Inicjacja"
    elif currentEpisode == 2:
        $ episode_title_name = "Bractwo Maggot"
    elif currentEpisode == 3:
        $ episode_title_name = "     100%"
    elif currentEpisode == 4:
        $ episode_title_name = "{size=-30}Kiedy Światy się Zderzają{/size}"
    elif currentEpisode == 5:
        $ episode_title_name = "Gorąco Głowy"
    elif currentEpisode == 6:
        $ episode_title_name = "Kontrola Uszkodzeń"
    elif currentEpisode == 7:
        $ episode_title_name = "Prawdziwe kolory"
    elif currentEpisode == 8:
        $ episode_title_name = "Rozdroże"
    imagebutton at title_white_line_anim4 xoffset -2200 idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.28
    imagebutton at title_white_line_anim3 xoffset 2920 idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.32
    imagebutton at title_orange_line_anim xoffset -5030 idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.36
    imagebutton at title_orange_line_anim xoffset -1750 idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.36
    text "Odcinek %d" % currentEpisode style "episode_number_title_style" at episode_number_anim xoffset -2000 yalign 0.35
    text "[episode_title_name]" style "episode_title_style" at episode_title_anim xoffset 2000 yalign 0.45
    imagebutton at title_orange_line_anim2 xoffset 2000 idle "title_ol_orange_line" hover "title_ol_orange_line" yalign 0.57
    imagebutton at title_white_line_anim2 xoffset -4000 idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.61
    imagebutton at title_white_line_anim xoffset 1700 idle "title_ol_white_line" hover "title_ol_white_line" yalign 0.65
init:
    transform title_orange_line_anim:
        easein 1.0 xpos 2500
        easein 3.0 xpos 2600
        easein 1.0 xpos 8000
init:
    transform title_orange_line_anim2:
        easein 0.5 xpos -2000
        easein 3.5 xpos -2100
        easein 1.0 xpos -8000
init:
    transform title_white_line_anim:
        easein 1.0 xpos -4400
        easein 0.5 xpos -4450
        easein 0.5 xpos -4350
        easein 0.5 xpos -4400
        easein 0.5 xpos -4420
        easein 0.5 xpos -4450
        easein 0.5 xpos -4400
        easein 0.5 xpos -6000
init:
    transform title_white_line_anim2:
        easein 1.0 xpos 1400
        easein 0.5 xpos 1450
        easein 0.75 xpos 1350
        easein 0.25 xpos 1400
        easein 0.5 xpos 1455
        easein 0.5 xpos 1350
        easein 0.5 xpos 1400
        easein 1.0 xpos 6000
init:
    transform title_white_line_anim3:
        easein 1.0 xpos -1400
        easein 0.5 xpos -1450
        easein 0.5 xpos -1350
        easein 0.5 xpos -1400
        easein 0.5 xpos -1420
        easein 0.5 xpos -1450
        easein 0.5 xpos -1400
        easein 0.5 xpos -7000
init:
    transform title_white_line_anim4:
        easein 1.0 xpos 3600
        easein 0.5 xpos 3650
        easein 0.75 xpos 3550
        easein 0.25 xpos 3600
        easein 0.5 xpos 3655
        easein 0.5 xpos 3550
        easein 0.5 xpos 3600
        easein 1.0 xpos 6000
init:
    transform episode_number_anim:
        easein 1.0 xpos 2500
        easein 3.0 xpos 2600
        easein 1.0 xpos 8000
init:
    transform episode_title_anim:
        easein 1.0 xpos -1300
        easein 3.0 xpos -1400
        easein 1.0 xpos -7000
return