label ep1_freeroam_home_label:

if persistent.ep1_card15:
    $ brawler_render_available = False
$ phone_chat_josy = 1
$ chat_josy_state = "1"
$ phone_chat_josy_new = True
$ loopMusic = True
$ queueChanCallback()
$ updateDikScore()
label ep1_freeroam_kitchen_label:

if not persistent.ep1_card1:
    scene d0_kitchen_bg_card with fade
else:
    scene d0_kitchen_bg with fade
label ep1_freeroam_kitchen_label_nofx:

if not persistent.ep1_card1:
    scene d0_kitchen_bg_card
else:
    scene d0_kitchen_bg
$ currentFreeRoamLabel = "ep1_freeroam_kitchen_label_nofx"
if firstTimeFreeRoam:
    $ firstTimeFreeRoam = False
    $ bios_name_josy = True
    $ bios_name_dad = True
    $ bios_name_mc = True
    $ bios_name_steve = True
    if tutorials:
        show white_screen with dissolve
        show text "{color=#ffffff}Podczas gry będą miały miejsce wydarzenia, podczas których będzie można eksplorować określone obszary. Potraktuj to jako swobodną wędrówkę.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Wydarzenia te zawsze określają zadania, które musisz wykonać, aby kontynuować fabułę. Podczas wydarzeń w trybie swobodnej rozgrywki możesz znaleźć specjalne rendery i pieniądze, jeśli dobrze się rozejrzysz.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Zobacz swoje odblokowane specjalne rendery w aplikacji Rewards na swoim telefonie.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show screen scoremsg
        show text "{color=#ffffff}Twój {size=+3}{size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size}{/size} wynik uległ zmianie w wyniku dokonanych wyborów.\nSprawdź aplikację Stats na swoim telefonie, aby zobaczyć swój wynik.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide screen scoremsg
        hide text
        show text "{color=#ffffff}Aby uzyskać dostęp do telefonu, należy kliknąć przycisk telefonu w lewym górnym rogu ekranu.{/color}" with dissolve:
            ypos 0.825
        $ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
        if notifications:
            play sound "sound_effects/message.mp3"
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Możesz również uzyskać dostęp do telefonu i zamknąć wszystkie menu w nim zawarte, klikając środkowym przyciskiem myszy.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Twój telefon jest na bieżąco aktualizowany podczas gry. Jeśli zapomnisz o jakiejś ważnej decyzji, którą podjąłeś, możesz przeczytać o niej w aplikacji Bios.{/color}" with dissolve:
            ypos 0.825
        $ renpy.pause()
        hide text
        show text "{color=#ffffff}Podczas swobodnego poruszania się po świecie gry możesz zmieniać muzykę za pomocą telefonu lub klikając przycisk pomijania utworu w prawym górnym rogu ekranu.{/color}" with dissolve:
            ypos 0.825
        $ ui.imagebutton("skip_song_button_hover", "skip_song_button_hover", clicked=ui.returns("OK"), xalign=0.99, yalign=0.01)
        $ renpy.pause()
        hide text
        hide white_screen
    else:
        show screen scoremsg
        $ renpy.pause(2)
        hide screen scoremsg
    mc "(Ugh... To była dobra sesja sparingowa, ale cholernie śmierdzę...)"
    mc "(Nie mogę spotkać się z Josy, pachnąc w ten sposób.)"
    show white_screen with dissolve
    $ current_task = "Przygotuj się na randkę."
    $ chat_new_tasks = True
    show text "{size=+40}{color=#fe961b}Zadanie:{/color} Przygotuj się na randkę.{/size}":
        ypos 0.825
        xpos 0.5
    $ ui.imagebutton("invisible_viewport", "invisible_viewport", clicked=ui.returns("OK"), xpos=0, ypos=0)
    $ result = ui.interact()
    if result == "OK":
        hide text "{size=+40}{color=#fe961b}Zadanie:{/color} Przygotuj się na randkę.{/size}"
        hide white_screen with dissolve
    $ phone_call_enabled = True
    show screen phone_screen
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
if not ep1_dad_college and not ep1_dad_women:
    $ ui.imagebutton("d0_kitchen_bg_dad_idle", "d0_kitchen_bg_dad_hover", clicked=ui.returns("fr_ep1_dad"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card1:
    $ ui.imagebutton("fr_ep1_hidden1", "fr_ep1_hidden1_hover", clicked=ui.returns("fr_ep1_hidden1"), xpos=1300, ypos=614)
$ ui.imagebutton("d0_kitchen_bg_stove_idle", "d0_kitchen_bg_stove_hover", clicked=ui.returns("fr_ep1_stove"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    jump fr_ep1_hall_label
elif result == "fr_ep1_stove":
    $ phone_call_enabled = False
    mc "(Haha. Nadal śmieję się, gdy widzę tą przemysłową kuchenkę...)"
    mc "(Nie mogę uwierzyć, że tata naprawdę przyniósł to do domu po remoncie restauracji...)"
    mc "(Na boku kuchenki wyryto cyfrę {color=#00ff00}1{/color}.)"
    $ phone_call_enabled = True
    jump ep1_freeroam_kitchen_label_nofx
elif result == "fr_ep1_dad":
    $ phone_call_enabled = False
    stop music fadeout 3
    $ loopMusic = False
    scene fr_ep1_dad_talk with dissolve
    dad "Szykujesz się na dzisiejszy wieczór?"
    play music "music/ep1/someways.mp3"
    scene fr_ep1_dad_listen with dissolve
    mc "Tak... Dzisiaj jest ten wieczór."
    scene fr_ep1_dad_talk with dissolve
    dad "Dasz radę, synu."
    label ep1_fr_dad_label:
    scene fr_ep1_dad_listen with dissolve
    menu:
        "Uczelnia" if not ep1_dad_college:
            $ ep1_dad_college = True
            mc "Czy dasz sobie radę sam, kiedy się wyprowadzę i zacznę studia?"
            scene fr_ep1_dad_talk2 with dissolve
            dad "Oczywiście! Będę tęsknił za tobą, ale wiedziałem, że ten dzień prędzej czy później nadejdzie."
            scene fr_ep1_dad_listen with dissolve
            mc "Dziwnie się czuję, zostawiając cię tu samego."
            scene fr_ep1_dad_talk with dissolve
            dad "Nie mów tak. Mam kolegów z pracy, nie jestem sam."
            scene fr_ep1_dad_talk2 with dissolve
            dad "Chociaż mógłbym przyjechać i zatrzymać się u ciebie w akademiku, jeśli to sprawiłoby, że poczułabyś się lepiej?"
            scene fr_ep1_dad_listen with dissolve
            mc "Haha! Odmówię, dziękuję."
            jump ep1_fr_dad_label
        "Kobiety" if not ep1_dad_women:
            $ ep1_dad_women = True
            mc "Tato... czy w młodości cieszyłeś się popularnością wśród kobiet?"
            scene fr_ep1_dad_talk2 with dissolve
            dad "Hehe, zanim poznałem twoją mamę, miałem sporo sukcesów. Nie mogę temu zaprzeczyć."
            scene fr_ep1_dad_talkc with dissolve
            dad "Niektóre związki były poważne, a inne... niekoniecznie."
            dad "Gdybym mógł cofnąć się w czasie i udzielić sobie rady..."
            dad "Powiedziałbym sobie, żeby nigdy nie wątpić w swoje przeczucia."
            scene fr_ep1_dad_talk3 with dissolve
            dad "...to oszczędziłoby mi trochę... problemów."
            scene fr_ep1_dad_talk with dissolve
            dad "Och! Powiedziałbym sobie też, żeby zawsze używać prezerwatyw."
            scene fr_ep1_dad_listen with dissolve
            mc "...dzięki, tato."
            scene fr_ep1_dad_talk4 with dissolve
            dad "Nie miałem tego na myśli..."
            dad "Nie przejmuj się, synu, po prostu tak sobie gadam."
            dad "Chyba jestem dziś zmęczony."
            jump ep1_fr_dad_label
        "Odejdź":
            mc "Muszę lecieć, tato."
            scene fr_ep1_dad_talk with dissolve
            dad "Śmiało, synu. Spóźnisz się na randkę."
    $ phone_call_enabled = True
    $ loopMusic = True
    $ queueChanCallback()
    jump ep1_freeroam_kitchen_label
elif result == "fr_ep1_hidden1":
    $ renpy.block_rollback()
    $ persistent.ep1_card1 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene d0_kitchen_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_kitchen_label_nofx
label fr_ep1_hall_label:

scene d0_hall_bg with dissolve
label fr_ep1_hall_label_nofx:

scene d0_hall_bg
$ currentFreeRoamLabel = "fr_ep1_hall_label_nofx"
$ renpy.block_rollback()
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("d0_hall_bg_right_idle", "d0_hall_bg_right_hover", clicked=ui.returns("fr_ep1_room"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("d0_hall_bg_left_idle", "d0_hall_bg_left_hover", clicked=ui.returns("fr_ep1_bathroom"), xpos=0, ypos=0, focus_mask=True)
$ result = ui.interact()
if result == "go_down":
    jump ep1_freeroam_kitchen_label
elif result == "fr_ep1_room":
    jump ep1_freeroam_room_label
elif result == "fr_ep1_bathroom":
    jump ep1_freeroam_bathroom_label
label ep1_freeroam_bathroom_label:

$ renpy.block_rollback()
if not persistent.ep1_card2:
    scene d0_bathroom_bg_card with fade
else:
    scene d0_bathroom_bg with fade
if firstTimeShower:
    $ phone_call_enabled = False
    $ firstTimeShower = False
    mc "(Tata naprawdę świetnie wyremontował łazienkę.)"
    mc "(Jasne, większość materiałów zdobył za darmo w pracy, ale...)"
    mc "(.. jest utalentowany...)"
    mc "(... gdyby tylko stać go było na remont reszty domu.)"
    mc "(Byłby wtedy taki szczęśliwy...)"
    $ phone_call_enabled = True
label ep1_freeroam_bathroom_label_nofx:

if not persistent.ep1_card2:
    scene d0_bathroom_bg_card
else:
    scene d0_bathroom_bg
$ currentFreeRoamLabel = "ep1_freeroam_bathroom_label_nofx"
$ renpy.block_rollback()
$ ui.imagebutton("arrow_invis", "fr_ep1_go_down", clicked=ui.returns("go_down"), xpos=0, ypos=840)
$ ui.imagebutton("d0_bathroom_bg_toilet_idle", "d0_bathroom_bg_toilet_hover", clicked=ui.returns("fr_ep1_toilet"), xpos=0, ypos=0, focus_mask=True)
if not ep1_showered:
    $ ui.imagebutton("d0_bathroom_bg_shower_idle", "d0_bathroom_bg_shower_hover", clicked=ui.returns("fr_ep1_shower"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card2:
    $ ui.imagebutton("fr_ep1_hidden2", "fr_ep1_hidden2_hover", clicked=ui.returns("fr_ep1_hidden2"), xpos=695, ypos=466)
$ result = ui.interact()
if result == "go_down":
    $ renpy.block_rollback()
    jump fr_ep1_hall_label
elif result == "fr_ep1_toilet":
    $ phone_call_enabled = False
    mc "(To brzydka toaleta, chociaż...)"
    $ phone_call_enabled = True
    jump ep1_freeroam_bathroom_label_nofx
elif result == "fr_ep1_shower":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    $ loopMusic = False
    stop music fadeout 3
    $ ep1_showered = True
    mc "(Mam mnóstwo czasu, żeby wziąć długi prysznic.)"
    $ renpy.music.set_volume(1, delay=0, channel="sfx1")
    $ renpy.sound.play("sound_effects/shower.mp3", channel="sfx1", loop=True)
    play music "music/ep1/slow_day_blues.mp3"
    scene fr_ep1_shower with wipeleft
    mc "(Nie mogę się doczekać dzisiejszego spotkania z Josy...)"
    mc "(Ciekawe, co powie...)"
    scene fr_ep1_shower_thought
    js "Kochasz mnie? Oszalałeś?"
    scene fr_ep1_shower_thought2
    js "HAHAHA! To po prostu smutne!"
    scene fr_ep1_shower_thought3
    js "Ekhm... ok... muszę lecieć..."
    scene fr_ep1_shower_thought4
    js "Ty jesteś zakochany we mnie?"
    scene fr_ep1_shower_thought4b with dissolve
    js "No to czemu nie zerżniesz mnie tutaj?"
    js "Tak, zgadza się... Chcę, żebyś we mnie wszedł, [mc_josy]."
    scene fr_ep1_shower_thought4d with dissolve
    js "Byłam niegrzeczną dziewczynką..."
    scene fr_ep1_shower_thought5
    stop music
    $ renpy.music.stop(channel="sfx1", fadeout=0)
    $ renpy.sound.play("sound_effects/shower_low.mp3", channel="sfx1", loop=True)
    play sound "sound_effects/door_knock.mp3"
    dad "*{i}Pukanie do drzwi{/i}* Synu, kończysz już?"
    scene fr_ep1_shower_thought6 with dissolve
    mc "Weź mojego kutasa, Josy!"
    scene fr_ep1_shower_thought5b with dissolve
    dad "Co takiego, synu?"
    scene fr_ep1_shower_thought6 with dissolve
    mc "Tak, już dochodzę... Cholera! Już prawie skończyłem, tato!"
    scene fr_ep1_shower_thought5c with dissolve
    dad "Zostaw mi trochę gorącej wody, dobrze?"
    scene fr_ep1_shower_thought7 with dissolve
    $ renpy.music.stop(channel="sfx1", fadeout=5)
    mc "(I minęła ta chwila...)"
    mc "(Czas się przebrać, jak sądzę.)"
    $ loopMusic = True
    $ queueChanCallback()
    $ phone_call_enabled = True
    jump ep1_freeroam_bathroom_label
elif result == "fr_ep1_hidden2":
    $ renpy.block_rollback()
    $ persistent.ep1_card2 = True
    $ persistent.rew_riona_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene d0_bathroom_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_bathroom_label_nofx
label ep1_freeroam_room_label:

$ renpy.block_rollback()
if not persistent.ep1_card3:
    scene ep1_fr_room_bg_card with fade
else:
    scene ep1_fr_room_bg with fade
label ep1_freeroam_room_label_nofx:

$ currentFreeRoamLabel = "ep1_freeroam_room_label_nofx"
if not persistent.ep1_card3:
    scene ep1_fr_room_bg_card
else:
    scene ep1_fr_room_bg
$ renpy.block_rollback()
$ ui.imagebutton("ep1_fr_room_bg_door_idle", "ep1_fr_room_bg_door_hover", clicked=ui.returns("fr_ep1_hall3"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_fr_room_bg_desk_idle", "ep1_fr_room_bg_desk_hover", clicked=ui.returns("fr_ep1_closet"), xpos=0, ypos=0, focus_mask=True)
$ ui.imagebutton("ep1_fr_room_bg_guitar_idle", "ep1_fr_room_bg_guitar_hover", clicked=ui.returns("fr_ep1_guitar"), xpos=0, ypos=0, focus_mask=True)
if not persistent.ep1_card3:
    $ ui.imagebutton("fr_ep1_hidden3", "fr_ep1_hidden3_hover", clicked=ui.returns("fr_ep1_hidden3"), xpos=1610, ypos=593)
$ result = ui.interact()
if result == "fr_ep1_hall3":
    $ renpy.block_rollback()
    jump fr_ep1_hall_label
elif result == "fr_ep1_guitar":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    mc "(Mój tata kupił mi tę gitarę na moje 12. urodziny. Od tamtej pory ją uwielbiam.)"
    mc "(Nie mam pojęcia, skąd wziął na nią pieniądze...)"
    scene ep1_fr_guitar_play with dissolve
    $ loopMusic = False
    stop music fadeout 3
    mc "(Musiała go kosztować fortunę.)"
    mc "(Jest to najcenniejsza rzecz, jaką posiadam.)"
    play music "music/ep1/trow.mp3"
    scene ep1_fr_guitar_play_dyn with dissolve
    $ renpy.pause(8)
    show text "Kliknij, aby kontynuować" with dissolve:
        xpos 0.5
        ypos 0.9
    $ renpy.pause(2)
    hide text "Kliknij, aby kontynuować" with dissolve
    $ renpy.pause()
    stop music
    scene ep1_fr_guitar_play with dissolve
    mc "(Tak bardzo kocham muzykę...)"
    if not persistent.ep1_card3:
        scene ep1_fr_room_bg_card with dissolve
    else:
        scene ep1_fr_room_bg with dissolve
    $ loopMusic = True
    $ queueChanCallback()
    $ phone_call_enabled = True
    jump ep1_freeroam_room_label_nofx
elif result == "fr_ep1_closet":
    $ phone_call_enabled = False
    $ renpy.block_rollback()
    if not ep1_showered:
        mc "(Śmierdzę, nie mogę iść na randkę, pachnąc w ten sposób...)"
        mc "(Najpierw muszę wziąć prysznic.)"
        $ phone_call_enabled = True
        jump ep1_freeroam_room_label_nofx
    menu:
        "Ubierz się":
            scene fr_ep1_clothes with dissolve
        "Nie jestem jeszcze gotowy":
            $ phone_call_enabled = True
            jump ep1_freeroam_room_label_nofx
    stop music fadeout 3
    $ loopMusic = False
    mc "(Idealnie...)"
    mc "(Czas pojechać po Josy.)"
    $ phone_clear_jump_label = "ep1_date_label"
    jump clear_phone_chat
elif result == "fr_ep1_hidden3":
    $ renpy.block_rollback()
    $ persistent.ep1_card3 = True
    $ persistent.rew_josy_unlocked += 1
    $ chat_new_rewards = True
    $ calcRenders()
    scene ep1_fr_room_bg with dissolve
    hide screen phone_screen
    show screen srmsg
    $ renpy.pause(4)
    hide screen srmsg
    show screen phone_screen
    jump ep1_freeroam_room_label_nofx
return