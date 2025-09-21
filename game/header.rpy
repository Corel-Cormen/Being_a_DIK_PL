label splashscreen:
    if steamConfig:
        $ persistent.steam_owns_al = is_subscribed_app_al()
        $ persistent.steam_owns_guide_s1 = is_subscribed_app_guide_s1()
        $ persistent.steam_owns_s2 = is_subscribed_app_s2()
        $ persistent.steam_owns_guide_s2 = is_subscribed_app_guide_s2()
    if not steamConfig and not nonPatreonConfig:
        scene black
        play sound "gui/pinkcake_sound.mp3"
        $ renpy.movie_cutscene("gui/pinkcake_video.webm")
        stop sound
        scene black with dissolve
    if not persistent.default_text_box_mode:
        $ style.window.background = Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)
        $ style.say_dialogue.xsize = 950
        $ style.say_dialogue.xpos = 498
        $ style.say_dialogue.xalign = 0.5
        $ style.say_dialogue.text_align = 0.5
        $ style.say_dialogue.xoffset = 0
        $ style.namebox.xalign=0.5
        $ style.say_label.xoffset = 0
        $ style.say_label.text_align = 0.5
        $ style.say_label.xalign = 0.5
        $ style.rebuild()
    window hide
    $ persistent.current_episode = 8
    if persistent.firstTimePlaying:
        play music "music/patched/track_previous.mp3"
        if not steamConfig and not nonPatreonConfig:
            scene black with Pause(1)
        show game_warning with dissolve
        $ renpy.pause(2)
        scene black
        stop music
        dpc "Czekaj! Czekaj! Zatrzymać muzykę!"
        dpc "Jill, Twoja kolej."
        scene disclaimer2 with dissolve
        $ renpy.music.set_volume(0.5,channel='music')
        play music "music/ep1/anachronist.mp3"
        $ renpy.sound.set_volume(1.0,channel='jill')
        $ renpy.sound.play("voice/jill_intro/intro_jill.mp3", channel="jill", loop=False)
        ji "Cześć tam!"
        $ renpy.sound.play("voice/jill_intro/intro_jill_2.mp3", channel="jill", loop=False)
        ji "{color=#ff7ffa}Dr PinkCake{/color} poprosił mnie, abym przed rozpoczęciem porozmawiała z Tobą."
        $ renpy.sound.play("voice/jill_intro/intro_jill_3.mp3", channel="jill", loop=False)
        ji "Wiesz, tylko kilka formalności."
        $ renpy.sound.play("voice/jill_intro/intro_jill_4.mp3", channel="jill", loop=False)
        ji "Masz ponad 18 lat, prawda?"
        scene disclaimer5 with dissolve
        menu:
            "Tak":
                scene disclaimer3 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_5.mp3", channel="jill", loop=False)
                ji "To świetnie!"
            "Tak (skłam)":
                scene disclaimer3 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_6.mp3", channel="jill", loop=False)
                ji "Haha, ok! {color=#ff7ffa}Dr PinkCake{/color} przeszukiwał magazynki porno swojego ojca, gdy miał 10 lat; wszystko będzie dobrze."
                scene black
                dpc "Nie tak powinnaś mówić, Jill. Powinnaś im powiedzieć, że muszą być pełnoletni, żeby w to grać."
                $ renpy.sound.play("voice/jill_intro/intro_jill_7.mp3", channel="jill", loop=False)
                ji "To ich nie powstrzyma."
                dpc "Chcesz mieć kłopoty prawne? Ja nie chcę!"
                $ renpy.sound.play("voice/jill_intro/intro_jill_8.mp3", channel="jill", loop=False)
                ji "Dobrze..."
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_9.mp3", channel="jill", loop=False)
                ji "Nie wolno grać w tę grę, jeśli nie osiągnąłeś pełnoletności. Proszę ją natychmiast zamknąć."
                scene disclaimer5 with dissolve
                dpc "Oni nadal tam są, prawda?"
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_10.mp3", channel="jill", loop=False)
                ji "Tak."
                scene disclaimer5 with dissolve
                dpc "Cóż, próbowaliśmy."
            "Nie":
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_11.mp3", channel="jill", loop=False)
                ji "W takim razie naprawdę powinieneś teraz wyłączyć grę."
                $ renpy.sound.play("voice/jill_intro/intro_jill_12.mp3", channel="jill", loop=False)
                ji "Śmiało."
                scene disclaimer5 with dissolve
                dpc "Oni nadal tam są, prawda?"
                scene disclaimer2 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_10.mp3", channel="jill", loop=False)
                ji "Tak."
                scene disclaimer5 with dissolve
                dpc "Cóż, próbowaliśmy."
        scene disclaimer3 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_13.mp3", channel="jill", loop=False)
        ji "Zanim zaczniemy, zadam ci kilka pytań."
        $ renpy.sound.play("voice/jill_intro/intro_jill_14.mp3", channel="jill", loop=False)
        ji "Czy znasz poprzednie gry {color=#ff7ffa}Dr PinkCake's{/color}?"
        scene disclaimer5 with dissolve
        menu:
            "Tak":
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_15.mp3", channel="jill", loop=False)
                ji "Uh-huh. Świetnie."
                $ renpy.sound.play("voice/jill_intro/intro_jill_16.mp3", channel="jill", loop=False)
                ji "W takim razie na pewno masz pewne oczekiwania lub z góry przyjęte wyobrażenia na temat tej gry."
            "Nie":
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_17.mp3", channel="jill", loop=False)
                ji "Ok, w porządku. W 2018 roku stworzył grę o nazwie Acting Lessons, w którą być może zechcesz zagrać."
                $ renpy.sound.play("voice/jill_intro/intro_jill_18.mp3", channel="jill", loop=False)
                ji "Chciał, żebym powiedziała, że jego... hm... styl i podejście do pisania tych gier są inne."
        $ renpy.sound.play("voice/jill_intro/intro_jill_19.mp3", channel="jill", loop=False)
        ji "Chciałabym skorzystać z okazji, aby ostrzec Cię przed treściami zawartymi w tej grze."
        $ renpy.sound.play("voice/jill_intro/intro_jill_20.mp3", channel="jill", loop=False)
        ji "Możesz tu przyjść, oczekując zabawnej i radosnej historii miłosnej z dużą ilością treści seksualnych."
        scene black
        dpc "Powiedz im, że będzie mnóstwo seksu, Jill!!!"
        $ renpy.sound.play("voice/jill_intro/intro_jill_21.mp3", channel="jill", loop=False)
        ji "Naprawdę? Myślałem, że chciałeś zostać poważnym pisarzem dla dorosłych?"
        dpc "Ahh!"
        scene disclaimer6 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_22.mp3", channel="jill", loop=False)
        ji "W każdym razie ta gra nie polega wyłącznie na zabawie i radości."
        $ renpy.sound.play("voice/jill_intro/intro_jill_23.mp3", channel="jill", loop=False)
        ji "Czy przeżywasz trudny okres w swoim życiu?"
        scene disclaimer7 with dissolve
        menu:
            "Tak":
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_24.mp3", channel="jill", loop=False)
                ji "To fatalnie. Wszyscy przez to przechodziliśmy lub przejdziemy w pewnym momencie."
                scene disclaimer7 with dissolve
                dpc "Życie to nieunikniona droga ku śmierci, Jill!"
            "Nie":
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_25.mp3", channel="jill", loop=False)
                ji "Ok! Dobrze wiedzieć."
                scene disclaimer7 with dissolve
                dpc "Szczęśliwy gracz, co? Tęsknię za czasami, kiedy byłem szczęśliwy..."
        scene disclaimer6 with dissolve
        $ renpy.sound.play("voice/jill_intro/intro_jill_26.mp3", channel="jill", loop=False)
        ji "Nie słuchaj go..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_27.mp3", channel="jill", loop=False)
        ji "Czy łatwo Cię urazić?"
        scene disclaimer7 with dissolve
        menu:
            "Tak":
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_28.mp3", channel="jill", loop=False)
                ji "W takim razie ta gra zdecydowanie nie jest dla Ciebie."
            "Nie":
                dpc "Świetnie słyszeć, ty pieprzona cipo!"
                dpc "Czy on, ona lub ono poczuło się urażone?"
                scene disclaimer6 with dissolve
                $ renpy.sound.play("voice/jill_intro/intro_jill_29.mp3", channel="jill", loop=False)
                ji "Nie, myślę, że wszystko jest w porządku."
        $ renpy.sound.play("voice/jill_intro/intro_jill_30.mp3", channel="jill", loop=False)
        ji "Przed rozpoczęciem gry zadaj sobie następujące pytanie..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_31.mp3", channel="jill", loop=False)
        ji "Czy nie mam nic przeciwko graniu w grę, która może wywołać u mnie złość lub smutek?"
        $ renpy.sound.play("voice/jill_intro/intro_jill_32.mp3", channel="jill", loop=False)
        ji "Jeśli odpowiedź brzmi „nie”, zrób sobie przysługę i przestań już teraz."
        $ renpy.sound.play("voice/jill_intro/intro_jill_33.mp3", channel="jill", loop=False)
        ji "Nie chciałbym, żebyś dotarł do momentu w tej historii, który by cię zdenerwował."
        scene disclaimer7 with dissolve
        dpc "Nie zrobiłbym tego, ale chciałem zamieścić zastrzeżenie przed całym tym narzekaniem i innymi formami pieprzonych bzdur..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_34.mp3", channel="jill", loop=False)
        scene black
        ji "Hej, rozmawiasz z graczem i potencjalnym fanem. Bądź miły!"
        scene disclaimer9 with dissolve
        $ persistent.firstTimePlaying = False
        $ renpy.sound.play("voice/jill_intro/intro_jill_35.mp3", channel="jill", loop=False)
        ji "Cóż, to wszystko, czym zamierzam cię teraz zawracać głowę."
        $ renpy.sound.play("voice/jill_intro/intro_jill_36.mp3", channel="jill", loop=False)
        ji "Nie martw się, ta rozmowa jest jednorazowa. Przy następnym uruchomieniu gry nie zobaczysz jej."
        if not steamConfig and not nonPatreonConfig:
            $ renpy.sound.play("voice/jill_intro/intro_jill_37.mp3", channel="jill", loop=False)
            ji "Baw się dobrze i ciesz się!"
            scene black
            dpc "Powiedz im, żeby przekazali pieniądze! Potrzebuję ich pieniędzy!"
            scene disclaimer9 with dissolve
            $ renpy.sound.play("voice/jill_intro/intro_jill_38.mp3", channel="jill", loop=False)
            ji "Jeśli gra przypadnie Ci do gustu, każda darowizna przekazana na stronie {color=#ff7ffa}Dr PinkCake's{/color} Patreon pomoże mu w dalszym rozwoju gry."
            $ renpy.sound.play("voice/jill_intro/intro_jill_39.mp3", channel="jill", loop=False)
            ji "Jest niezależnym twórcą, który pracuje nad tym projektem samodzielnie. Twoje wsparcie sprawi, że ta gra stanie się rzeczywistością."
        scene disclaimer10 with dissolve
        stop music fadeout 3
        $ renpy.sound.play("voice/jill_intro/intro_jill_40.mp3", channel="jill", loop=False)
        ji "Dość gadania. Bez dalszych ceregieli..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_41.mp3", channel="jill", loop=False)
        ji "Z dumą przedstawiam - {font=collegiate.ttf}Being a DIK{/font}."
        scene black with fade
        dpc "Pokazałaś im swoje cycki, Jill?"
        $ renpy.sound.play("voice/jill_intro/intro_jill_42.mp3", channel="jill", loop=False)
        ji "Czy nie wystarczyło, że musiałam założyć ten wyzywający strój?"
        dpc "Miałaś pokazać im swoje cycki..."
        $ renpy.sound.play("voice/jill_intro/intro_jill_43.mp3", channel="jill", loop=False)
        ji "Ty wyjdź i pokaż im swoje cycki!"
        dpc "Cóż, zrobiłbym to, ale wtedy byłaby to zupełnie inna gra, a owłosione piersi nie są popularnym fetyszem..."
        $ renpy.music.set_volume(1,channel='music')
        dpc "Cholera, czy to nadal działa?"
    play music "music/patched/track_previous.mp3"
    if not steamConfig and not nonPatreonConfig:
        scene black with Pause(1)
    show game_warning with dissolve
    $ renpy.pause()
    if steamConfig:
        show legal_info_steam_version with dissolve
    elif nonPatreonConfig:
        show legal_info with dissolve
        $ renpy.pause()
        show gog_screen with dissolve
        hide legal_info with dissolve
    else:
        show legal_info_patreon_version with dissolve
    $ renpy.pause()
    scene black with dissolve
    with Pause(0.5)
    return
init:
    python:
        import math
        def name_func(newstring):
            store.name = newstring
            renpy.restart_interaction()
        def sname_func(newstring):
            store.name = newstring
            renpy.restart_interaction()

init:
    python:
        def badik_chapter_save(d):
            d["badik_chapter"] = badik_chapter
        config.save_json_callbacks = [badik_chapter_save]
        def steamConfig_save(d):
            d["steamConfig"] = steamConfig
        config.save_json_callbacks = [steamConfig_save]
        achievement.Sync()

init:
    python:
        g = Gallery()
        g.transition = dissolve
        loopMusic = False
        loopFightMusic = False
        loopPartyMusic = False
        loopMansionMusic = False
        loopMorningMusic = False
        loopLibraryMusic = False
        def queueChanCallback():
            if loopPartyMusic:
                randomswamp = renpy.random.choice(
                    ("music/ep4/reaching_halo.mp3", "music/ep4/the_heat.mp3", "music/ep3/raveyard.mp3", "music/ep3/roads.mp3", "music/ep2/fallen_colors.mp3", "music/ep2/night_lights.mp3", "music/ep2/phate.mp3", "music/ep2/skyline.mp3", "music/ep2/sound_of_summer.mp3", "music/ep2/stryv.mp3"))
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
            elif loopLibraryMusic:
                randomswamp = renpy.random.choice(
                    ("music/ep5/licensed_music/track11.mp3", "music/ep5/licensed_music/track14.mp3", "music/ep5/licensed_music/track5.mp3"))
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
            elif loopMusic:
                if renpy.loadable("season2/scripts/update5.rpyc"):
                    randomswamp = renpy.random.choice( ("music/ep1/slow_day_blues.mp3","music/ep1/surf_punk_rock.mp3","music/ep1/threes_a_crowd.mp3","music/ep1/energetic.mp3","music/ep1/art_nouveau.mp3","music/ep1/apra_hyde.mp3","music/ep1/mumford.mp3","music/ep1/windswept.mp3","music/ep1/funk_rock.mp3","music/ep1/golden_alley.mp3","music/ep1/never_give_up.mp3","music/ep1/roadtrip.mp3","music/ep1/someways.mp3","music/ep1/winter_sunshine.mp3","music/ep1/classicals_breakbeat.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/scrapbook.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3","music/ep1/trow.mp3","music/ep1/fresh_air.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep2/acoustic.mp3" ,"music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep1/they_say.mp3", "music/ep1/unknown_power.mp3", "music/ep1/your_smile.mp3", "music/ep2/by_your_side.mp3","music/ep2/wings.mp3", "music/ep2/freedom.mp3", "music/ep2/journey_of_hope.mp3", "music/ep2/relaxing_ballad.mp3", "music/ep2/winter.mp3", "music/ep2/rockin_riff.mp3", "music/ep2/simple_ballad.mp3", "music/ep2/jingle.mp3", "music/ep2/feel_bad.mp3", "music/ep3/get_back.mp3", "music/ep3/dc_love_go_go.mp3", "music/ep3/sunny_acoustic_rock.mp3", "music/ep3/lets_begin.mp3", "music/ep3/chill.mp3", "music/ep5/licensed_music/track5.mp3","music/ep5/licensed_music/track7.mp3","music/ep5/licensed_music/track11.mp3","music/ep5/licensed_music/track14.mp3","music/ep5/licensed_music/track17.mp3","music/ep5/medicate_me.mp3","music/ep5/down.mp3","music/ep5/inspiring.mp3") )
                else:
                    randomswamp = renpy.random.choice( ("music/ep1/slow_day_blues.mp3","music/ep1/surf_punk_rock.mp3","music/ep1/threes_a_crowd.mp3","music/ep1/energetic.mp3","music/ep1/art_nouveau.mp3","music/ep1/apra_hyde.mp3","music/ep1/mumford.mp3","music/ep1/windswept.mp3","music/ep1/funk_rock.mp3","music/ep1/golden_alley.mp3","music/ep1/never_give_up.mp3","music/ep1/roadtrip.mp3","music/ep1/someways.mp3","music/ep1/winter_sunshine.mp3","music/ep1/classicals_breakbeat.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/scrapbook.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3","music/ep1/trow.mp3","music/ep1/fresh_air.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep2/acoustic.mp3" ,"music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep1/they_say.mp3", "music/ep1/unknown_power.mp3", "music/ep1/your_smile.mp3", "music/ep2/by_your_side.mp3","music/ep2/wings.mp3", "music/ep2/freedom.mp3", "music/ep2/journey_of_hope.mp3", "music/ep2/relaxing_ballad.mp3", "music/ep2/winter.mp3", "music/ep2/rockin_riff.mp3", "music/ep2/simple_ballad.mp3", "music/ep2/jingle.mp3", "music/ep2/feel_bad.mp3", "music/ep3/get_back.mp3", "music/ep3/dc_love_go_go.mp3", "music/ep3/sunny_acoustic_rock.mp3", "music/ep3/lets_begin.mp3", "music/ep3/chill.mp3") )
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
            elif loopFightMusic:
                randomswamp = renpy.random.choice( ("music/ep1/anachronist.mp3","music/ep1/energetic.mp3","music/ep1/credits.mp3","music/ep1/food_chain.mp3","music/ep1/my_heart.mp3","music/patched/track_previous.mp3", "music/ep1/time_goes_by.mp3", "music/ep1/this_silence.mp3", "music/ep1/dont_count_on_me.mp3", "music/ep1/emptyv.mp3", "music/ep2/metal.mp3") )
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
            elif loopMansionMusic:
                randomswamp = renpy.random.choice( ("music/ep5/licensed_music/track4.mp3", "music/ep2/freedom.mp3","music/ep2/marty.mp3", "music/ep5/licensed_music/track3.mp3") )
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
            elif loopMorningMusic:
                randomswamp = renpy.random.choice( ("music/ep5/licensed_music/track5.mp3","music/ep5/licensed_music/track7.mp3","music/ep5/licensed_music/track11.mp3","music/ep5/licensed_music/track14.mp3","music/ep5/licensed_music/track17.mp3") )
                renpy.music.queue(randomswamp, channel="music", loop=False, fadein=0, tight=True)
        renpy.music.set_queue_empty_callback(queueChanCallback, channel='music')
        def skipSongFunc():
            renpy.music.stop('music')

init -1:
    python:
        if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
            renpy.display.get_info().oldmenu = renpy.exports.menu
        def menu_override(items, set_expr, args, kwargs, item_arguments):
            items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                          for label, condition, value in items ]
            return renpy.display.get_info().oldmenu(items, set_expr)
        renpy.exports.menu = menu_override

init define config.image_cache_size_mb = 300
label start:
    init default badik_chapter = "1"
    init default dtype = 0
    init default dik = 0
    init default tmpdik = 0
    init default majordik = 0
    init default majorchick = 0
    init default dpenalty = 0
    init default cpenalty = 0
    init default tmpParty = False
    init default tmpLibrary = False
    init default tmpMusic = False
    init default name = ""
    init default money = 0
    init default failedEnglish = 0
    init default failedMath = 0
    init default failedGender = 0
    init default maxedEnglish = 0
    init default maxedMath = 0
    init default maxedGender = 0
    init default nerdNotes = False
    init default tutorials = True
    init default RPnerds = 0
    init default RPjocks = 0
    init default RPpreps = 0
    init default RPdiks = 0
    init default RPhot = 0
    init default RPmaya = 0
    init default RPjosy = 0
    init default RPsage = 0
    init default RPisabella = 0
    init default RPjill = 0
    init default RPderek = 0
    init default josyScore = 0
    init default mayaScore = 0
    init default sageScore = 0
    init default isabellaScore = 0
    init default jillScore = 0
    init default currentEpisode = 1
    init default vault_ep1 = False
    init default vault_ep5 = False
    init default safe_new_renders = True
    init default notifications = True
    init default brawlerStoryFight = ""
    init default brawlerStoryFightLabel = ""
    init default episodeIsEnding = False
    init default totalChickChoices = 0
    init default totalDikChoices = 0
    init default stevePainting = 0
    init default acceptedMoneyFromDad = False
    init default ep1_josy_chat1_state = 0
    init default intervenedChad = False
    init default introducedSage = False
    init default assman = False
    init default preferredmilf = 0
    init default ep1_dad_college = False
    init default ep1_dad_women = False
    init default ep1_showered = False
    init default ep1_troy_talk = False
    init default ep1_studied_d1 = False
    init default ep1_called_josy = False
    init default ep1_played_guitar = False
    init default ep1_fr_talked_to_derek = False
    init default ep1_fr_quinn = False
    init default ep1_blank_on_name = False
    init default ep1_bought_student_soda = False
    init default ep1_insulted_cafeteria_worker = False
    init default ep1_lewd_camila_quinn = False
    init default ep1_played_along = False
    init default ep1_kissed_maya = False
    init default ep1_jade_pleased = False
    init default ep1_beat_up_troy_won = False
    init default ep1_maya_attracted = False
    init default ep1_maya_question_indoors = False
    init default ep1_maya_question_blanket = False
    init default ep1_maya_question_bath = False
    init default ep1_maya_question_party = False
    init default ep1_maya_question_money = False
    init default ep1_dik_end = False
    init default ep1_josy_prefer_beer = False
    init default ep1_josy_prefer_wine = False
    init default ep1_josy_prefer_flowers = False
    init default ep1_beat_up_troy = False
    init default ep1_accepted_quinn_offer = False
    init default lewd_scene_selection_hover = False
    init default lewd_pussy_available = False
    init default lewd_ass_available = False
    init default lewd_tits_available = False
    init default lewd_lips_available = False
    init default lewd_hand_available = False
    init default lewd_fingers_available = False
    init default lewd_jade_phase = 0
    init default lewd_cathy_phase = 0
    init default lewd_riona_phase = 0
    init default lewd_camila_phase = 0
    init default lewd_quinn_phase = 0
    init default lewd_sage_phase = 0
    init default lewd_jill_phase = 0
    init default lewd_maya_phase = 0
    init default lewd_josy_phase = 0
    init default lewd_isabella_phase = 0
    init default current_lewd_cum_label = ""
    init default current_lewd_pussy_label = ""
    init default current_lewd_ass_label = ""
    init default current_lewd_tits_label = ""
    init default current_lewd_lips_label = ""
    init default current_lewd_hand_label = ""
    init default current_lewd_fingers_label = ""
    init default freeRoamID = 1
    init default firstTimeFreeRoam = True
    init default firstTimeShower = True
    init default firstTimeFreeRoamMCDormEp1 = True
    init default ep1_fr_dad = False
    init default ep1_first_time_closet = True
    init default ep1_first_time_shower = True
    init default ep1_hallway_state = 0
    init default firstTimeBathroom = True
    init default ep1_saw_glory_hole = False
    init default ep1_maya_talk = False
    init default found_money = False
    init default ep1_raid_quinn_room = False
    init default seen_josy_pic = False
    init default seen_derek_pic = False
    init default seen_sage_pic = False
    init default seen_isabella_pic = False
    init default seen_jill_pic = False
    init default seen_maya_pic = False
    init default seen_quinn_pic = False
    init default seen_magnar_pic = False
    init default seen_dad_pic = False
    init default phone_call_enabled = False
    init default phone_call_josy = "NONE"
    init default phone_call_dad = "NONE"
    init default phone_call_maya = "NONE"
    init default phone_call_sage = "NONE"
    init default phone_call_jill = "NONE"
    init default phone_call_isabella = "NONE"
    init default phone_call_derek = "NONE"
    init default phone_call_magnar = "NONE"
    init default phone_call_quinn = "NONE"
    init default phone_bg = 0
    init default phone_chat_josy = 0
    init default phone_chat_dad = 0
    init default phone_chat_maya = 0
    init default phone_chat_jill = 0
    init default phone_chat_sage = 0
    init default phone_chat_isabella = 0
    init default phone_chat_derek = 0
    init default phone_chat_magnar = 0
    init default phone_chat_quinn = 0
    init default viewing_image = False
    init default phone_clear_jump_label = ""
    init default safe_digit_1 = 0
    init default safe_digit_2 = 0
    init default safe_digit_3 = 0
    init default safe_digit_4 = 0
    init default studied = False
    init default english_cheat = False
    init default minigames = True
    init default phone_label_offset = 0.845
    init default englishPresented = False
    init default genderPresented = False
    init default passedEnglish = 0
    init default passedMath = 0
    init default passedGender = 0
    init default mathTestScore = 0
    init default englishTestScore = 0
    init default bonusPercentageEnglish = 0
    init default bonusPercentageMath = 0
    init default bonusPercentageGender = 0
    init default afterMagnarShopLabel = ""
    init default talkMagnarShopLabel = ""
    init default listenMagnarShopLabel = ""
    init default afterDerekShopLabel = ""
    init default talkDerekShopLabel = ""
    init default listenDerekShopLabel = ""
    init default afterQuinnShopLabel = ""
    init default talkQuinnShopLabel = ""
    init default listenQuinnShopLabel = ""
    init default firstTimeGloryHole = True
    init default quinn_shop_freebie = False
    init default quinn_shop_spicy_lvl = 0
    init default quinn_shop_japanese_lvl = 0
    init default quinn_shop_special_lvl = 0
    init default quinn_shop_special_available = False
    init default englishBoost = 0
    init default mathBoost = 0
    init default genderBoost = 0
    init default englishCheatBoost = 0
    init default mathCheatBoost = 0
    init default genderCheatBoost = 0
    init default bios_anthony = False
    init default bios_camila = False
    init default bios_cathy = False
    init default bios_chad = False
    init default bios_dawe = False
    init default bios_derek = False
    init default bios_isabella = False
    init default bios_jacob = False
    init default bios_jade = False
    init default bios_jill = False
    init default bios_magnar = False
    init default bios_maya = False
    init default bios_quinn = False
    init default bios_riona = False
    init default bios_rusty = False
    init default bios_sage = False
    init default bios_tommy = False
    init default bios_troy = False
    init default bios_tybalt = False
    init default bios_burke = False
    init default bios_arieth = False
    init default bios_ashley = False
    init default bios_elena = False
    init default bios_heather = False
    init default bios_jamie = False
    init default bios_johnboy = False
    init default bios_leon = False
    init default bios_lily = False
    init default bios_melanie = False
    init default bios_mona = False
    init default bios_nick = False
    init default bios_ron = False
    init default bios_sally = False
    init default bios_sarah = False
    init default bios_zoey = False
    init default bios_txt_arieth = "To dziewczyna Dawe'a, Arieth. Jest seksowną członkinią stowarzyszenia HOT i wydaje się być rozwiązła."
    init default bios_txt_ashley = "Ashley też jest pierwszoklasistką. Chodzi do mojej klasy. Derek często z nią rozmawia."
    init default bios_txt_elena = "Elena lubi imprezować nago ze swoim chłopakiem, Johnem Boyem. Jest seksowną członkinią stowarzyszenia HOT."
    init default bios_txt_heather = "Heather jest dziewczyną Tommy'ego. Należy do stowarzyszenia HOT."
    init default bios_txt_jamie = "Jamie jest w stowarzyszeniu DIK, a Leon był jego Maggot Bratem. Zwykle trzymają się razem."
    init default bios_txt_johnboy = "John Boy jest w stowarzyszeniu DIK i był przyrodnim bratem Jacoba. Lubi imprezować nago ze swoją seksowną dziewczyną Eleną."
    init default bios_txt_leon = "Leon jest w stowarzyszeniu DIK, a Jamie był jego Maggot Bratem. Zwykle trzymają się razem."
    init default bios_txt_lily = "Lily jest studentką pierwszego roku, która również pracuje w The Pink Rose. Wydaje się, że wszyscy członkowie DIK bardzo ją lubią."
    init default bios_txt_melanie = "Melanie jest seksowną członkinią stowarzyszenia HOT. Jest najlepszą przyjaciółką Sarah."
    init default bios_txt_mona = "Mona jest studentką pierwszego roku, która zgłasza się do stowarzyszenia HOT."
    init default bios_txt_nick = "Nick jest w stowarzyszeniu DIK. Fajny i miły gość."
    init default bios_txt_ron = "Ron jest członkiem stowarzyszenia Tri-Beta i trochę dupkiem..."
    init default bios_txt_sally = "Myślę, że Sally może być dziewczyną Magnara. Wygląda na to, że bardzo go lubi."
    init default bios_txt_sarah = "Sarah jest seksowną członkinią stowarzyszenia HOT. Jest najlepszą przyjaciółką Melanie."
    init default bios_txt_zoey = "Zoey... Moja pierwsza najlepsza przyjaciółka, która na krótko została moją dziewczyną, zanim wyjechała do San Diego, aby zostać surferem."
    init default bios_history_arieth = ""
    init default bios_history_ashley = ""
    init default bios_history_elena = ""
    init default bios_history_heather = ""
    init default bios_history_jamie = ""
    init default bios_history_johnboy = ""
    init default bios_history_leon = ""
    init default bios_history_lily = ""
    init default bios_history_melanie = ""
    init default bios_history_mona = ""
    init default bios_history_nick = ""
    init default bios_history_ron = ""
    init default bios_history_sally = ""
    init default bios_history_sarah = ""
    init default bios_history_zoey = ""
    init default bios_name_arieth = True
    init default bios_name_ashley = True
    init default bios_name_elena = True
    init default bios_name_heather = True
    init default bios_name_jamie = True
    init default bios_name_johnboy = True
    init default bios_name_leon = True
    init default bios_name_lily = True
    init default bios_name_melanie = True
    init default bios_name_mona = True
    init default bios_name_nick = True
    init default bios_name_ron = True
    init default bios_name_sally = True
    init default bios_name_sarah = True
    init default bios_name_zoey = True
    init default bios_alex = False
    init default bios_bert = False
    init default bios_beth = False
    init default bios_brandi = False
    init default bios_dany = False
    init default bios_envy = False
    init default bios_eugene = False
    init default bios_jimmy = False
    init default bios_john = False
    init default bios_lynette = True
    init default bios_minny = False
    init default bios_rose = False
    init default bios_stanley = False
    init default bios_wendy = False
    init default bios_txt_alex = "Członek stowarzyszenia Tri-Alpha.."
    init default bios_txt_bert = "Bert jest współlokatorem Dereka i członkiem stowarzyszenia Tri-Beta."
    init default bios_txt_beth = "Pracuje w szkolnej stołówce. Widziałem ją na imprezach DIK."
    init default bios_txt_brandi = "Brandi pracuje w klubie The Pink Rose jako striptizerka."
    init default bios_txt_dany = "Dany jest w mojej grupie na zajęciach z gender. Jamie jest jego dziewczyną."
    init default bios_txt_envy = "Envy pracuje w klubie The Pink Rose jako striptizerka."
    init default bios_txt_eugene = "Eugene jest członkiem stowarzyszenia Tri-Beta."
    init default bios_txt_jimmy = "Członek stowarzyszenia Tri-Alpha."
    init default bios_txt_john = "Członek stowarzyszenia Tri-Alpha."
    init default bios_txt_lynette = "Moja mama zmarła, kiedy się urodziłem. Poznałem ją tylko przez opowieści taty."
    init default bios_txt_minny = "Minny chodzi ze mną na zajęcia z gender. Wygląda na zagorzałą feministkę."
    init default bios_txt_rose = "Rose pracuje w klubie The Pink Rose jako striptizerka."
    init default bios_txt_stanley = "Stanley pracuje jako bramkarz w klubie The Pink Rose."
    init default bios_txt_wendy = "Wendy chodzi ze mną na zajęcia z gender. Wygląda na zagorzałą feministkę."
    init default bios_history_alex = ""
    init default bios_history_bert = ""
    init default bios_history_beth = ""
    init default bios_history_brandi = ""
    init default bios_history_dany = ""
    init default bios_history_envy = ""
    init default bios_history_eugene = ""
    init default bios_history_jimmy = ""
    init default bios_history_john = ""
    init default bios_history_lynette = ""
    init default bios_history_minny = ""
    init default bios_history_rose = ""
    init default bios_history_stanley = "Stanley wydaje się pomagać Rusty'emu w organizowaniu imprez w klubie.\n\n"
    init default bios_history_wendy = ""
    init default bios_name_alex = True
    init default bios_name_bert = True
    init default bios_name_beth = True
    init default bios_name_brandi = True
    init default bios_name_dany = True
    init default bios_name_envy = True
    init default bios_name_eugene = True
    init default bios_name_jimmy = True
    init default bios_name_john = True
    init default bios_name_lynette = True
    init default bios_name_minny = True
    init default bios_name_rose = True
    init default bios_name_stanley = True
    init default bios_name_wendy = True
    init default bios_caleb = False
    init default bios_gordon = False
    init default bios_christian = False
    init default bios_lucas = False
    init default bios_rich = False
    init default bios_trent = False
    init default bios_txt_caleb = "Wielki i przerażający facet, który wstąpił do stowarzyszenia Tri-Alpha."
    init default bios_txt_gordon = "Zobowiązany członek stowarzyszenia Alpha Nu Omega."
    init default bios_txt_christian = "Zobowiązany członek stowarzyszenia Alpha Nu Omega."
    init default bios_txt_lucas = "Zobowiązany członek stowarzyszenia Alpha Nu Omega."
    init default bios_txt_rich = "Wiceprezes stowarzyszenia Alpha Nu Omega."
    init default bios_txt_trent = "Członek stowarzyszenia Alpha Nu Omega."
    init default bios_history_caleb = ""
    init default bios_history_gordon = ""
    init default bios_history_christian = ""
    init default bios_history_lucas = ""
    init default bios_history_rich = ""
    init default bios_history_trent = ""
    init default bios_name_caleb = True
    init default bios_name_gordon = True
    init default bios_name_christian = True
    init default bios_name_lucas = True
    init default bios_name_rich = True
    init default bios_name_trent = True
    init default bios_txt_mc = "To ja. Zwykły 18-latek, którego ulubionymi hobby są sztuki walki i muzyka. Dorastając, nie cieszyłem się zbytnią popularnością wśród dziewczyn, głównie dlatego, że byłem prześladowany za to, że byłem biedny. Ale ostatnio sprawy mają się dla mnie coraz lepiej."
    init default bios_txt_dad = "Kocham mojego tatę. Zawsze był przy mnie. Pracuje na budowie, ale z powodu pewnych problemów prawnych z przeszłości ma trudności z wiązaniem końca z końcem."
    init default bios_txt_josy = "Josy. Nie minęło dużo czasu, zanim się w niej zakochałem. Ma ciepłą osobowość i potrafi zawsze przyciągnąć uwagę wszystkich w pomieszczeniu, w którym się znajduje."
    init default bios_txt_steve = "Steve... Syn szefa z mojej letniej pracy. Ma aroganckie podejście i widać, że uważa się za lepszego od wszystkich, bo jego tata jest właścicielem minimarketu. Daj spokój... nie jesteś aż tak bogaty, Steve!"
    init default bios_txt_anthony = "Głupi sportowiec. Nie wydaje się, żeby byli rzadkością na uczelni."
    init default bios_txt_camila = "Camila. Ona też jest studentką pierwszego roku. Pytanie brzmi, czy jest ona ogólnie osobą uległą, czy też jest coś innego, co sprawia, że się do tego dostosowuje?"
    init default bios_txt_cathy = "Cathy jest moją nauczycielką języka angielskiego i matematyki. Opisałabym ją jako surową, ale sprawiedliwą."
    init default bios_txt_chad = "Prezes Tri-Alphas i chłopak Sage. Wolałabym trzymać się od niego z daleka, ale wygląda na to, że już mnie zauważył."
    init default bios_txt_dawe = "Dawe... co za dupek. Nie wiem o nim zbyt wiele, ale w moich oczach nie różni się niczym od innych sportowców."
    init default bios_txt_derek = "Ten facet nie wydaje się traktować niczego poważnie. Wygląda na palanta, ale jest w nim coś dziwnego, co sprawia, że chcę go polubić. Nie potrafię tego dokładnie określić."
    init default bios_txt_isabella = "Bibliotekarka w szkolnej bibliotece. Uczniowie nadali jej przydomek „Królowa Lodu”. To złośliwa ksywka, ale w pewnym sensie rozumiem, skąd się wzięła. Ma takie złowrogie spojrzenie... przeraża mnie."
    init default bios_txt_jacob = "Członek stowarzyszenia DIK. Nic specjalnego."
    init default bios_txt_jade = "Patrząc na Jade, nigdy bym nie zgadła, że jest feministką... przepraszam... chciałam powiedzieć, że jest nauczycielką gender studies. Nawet jeśli jej zajęcia są do bani, wydaje się całkiem fajna."
    init default bios_txt_jill = "Jill. Piękna, miła i bogata. Wydaje się mieć wszystko... Musi być w niej coś nie tak... prawda?"
    init default bios_txt_magnar = "Magnar, prawdziwy kujon o dziwnym skandynawskim imieniu. Może załatwić mi materiały do nauki na zajęcia. Posiadanie takiego przyjaciela może się naprawdę opłacić."
    init default bios_txt_maya = "Maya jest uroczą i miłą dziewczyną. Wydaje się być bardzo ułożona i spokojna."
    init default bios_txt_quinn = "Hm... nie ma nic, co wskazywałoby na to, że Quinn jest delikatna lub słodka. Wygląda niezwykle seksownie, ale sprawia wrażenie osoby o dość wybuchowym charakterze."
    init default bios_txt_riona = "Seksowna dziewczyna, która ubiera się bardzo wyzywająco... eee... swobodnie. Nie wygląda na zbyt szczęśliwą."
    init default bios_txt_rusty = "Prezes stowarzyszenia DIK. Wydaje się być całkiem fajnym facetem, zdecydowanie milszym niż jego wiceprezes, Tommy."
    init default bios_txt_sage = "Ognista rudowłosa dziewczyna z charakterem. Sage jest prezesem HOT i dziewczyną Chada, prezesa Tri-Alphas. Wydaje się być przekonana, że Chad zdradza ją z kimś innym."
    init default bios_txt_tommy = "Wiceprezes stowarzyszenia DIK. Totalny dupek, przynajmniej dla osób spoza stowarzyszenia DIK."
    init default bios_txt_troy = "Dupek, z którym dzielę pokój w akademiku. Nie wiem, dlaczego od razu przyjmuje postawę bojową. Nie ma sposobu, żebym go przekonał, że nie jestem złym człowiekiem."
    init default bios_txt_tybalt = "Prezes stowarzyszenia studenckiego Alpha Nu Omega. Wydaje się być obrzydliwie bogaty."
    init default bios_txt_burke = "Profesor Stephen Burke. Profesor ekonomii i wykładowca kilku przedmiotów związanych z biznesem. Jest elegancko ubrany i czarujący."
    init default bios_history_mc = ""
    init default bios_history_dad = ""
    init default bios_history_burke = ""
    init default bios_history_josy = ""
    init default bios_history_steve = ""
    init default bios_history_anthony = ""
    init default bios_history_camila = ""
    init default bios_history_cathy = ""
    init default bios_history_chad = ""
    init default bios_history_dawe = ""
    init default bios_history_derek = ""
    init default bios_history_isabella = ""
    init default bios_history_jacob = ""
    init default bios_history_jade = ""
    init default bios_history_jill = ""
    init default bios_history_magnar = ""
    init default bios_history_maya = ""
    init default bios_history_quinn = ""
    init default bios_history_riona = ""
    init default bios_history_rusty = ""
    init default bios_history_sage = ""
    init default bios_history_tommy = ""
    init default bios_history_troy = ""
    init default bios_history_tybalt = ""
    init default bios_name_mc = True
    init default bios_name_dad = True
    init default bios_name_burke = True
    init default bios_name_josy = True
    init default bios_name_steve = True
    init default bios_name_anthony = True
    init default bios_name_camila = True
    init default bios_name_cathy = True
    init default bios_name_chad = True
    init default bios_name_dawe = True
    init default bios_name_derek = True
    init default bios_name_isabella = True
    init default bios_name_jacob = True
    init default bios_name_jade = True
    init default bios_name_jill = True
    init default bios_name_magnar = True
    init default bios_name_maya = True
    init default bios_name_quinn = True
    init default bios_name_riona = True
    init default bios_name_rusty = True
    init default bios_name_sage = True
    init default bios_name_tommy = True
    init default bios_name_troy = True
    init default bios_name_tybalt = True
    init default current_bios_txt = ""
    init default current_bios_history = ""
    init default current_bios_name = ""
    init default current_bios_avatar = ""
    init default current_task = "None"
    init default number_derek = False
    init default number_isabella = False
    init default number_maya = False
    init default number_sage = False
    init default number_jill = False
    init default number_quinn = False
    init default number_magnar = False
    init default pet_reset = ""
    init default josy = "Josy"
    init default maya = "Maya"
    init default sage = "Sage"
    init default isabella = "Isabella"
    init default jill = "Jill"
    init default quinn = "Quinn"
    init default riona = "Riona"
    init default jade = "Jade"
    init default cathy = "Cathy"
    init default camila = "Camila"
    init default gameBoost = 0
    init default phone_chat_josy_new = False
    init default phone_chat_dad_new = False
    init default phone_chat_maya_new = False
    init default phone_chat_isabella_new = False
    init default phone_chat_sage_new = False
    init default phone_chat_jill_new = False
    init default phone_chat_quinn_new = False
    init default phone_chat_magnar_new = False
    init default phone_chat_derek_new = False
    init default game_money_available = True
    init default brawler_render_available = True
    init default brawler_money_available = True
    init default brawler_skillpoint_available = True
    init default currentFreeRoamLabel = ""
    init default currentSexLabel = ""
    init default music_new_songs = True
    init default chat_new_bg = True
    init default chat_new_bios = True
    init default chat_new_rewards = False
    init default chat_new_tasks = True
    init default chat_new_names = True
    init default chat_new_stats = True
    init default chat_ySize = 0.068
    init default new_cluck = False
    init default rooster_app_enabled = False
    init default roosterState = "ep3_1"
    init default bonusPointsSports = 1
    init default bonusPointsSportsDerek = 0
    init default sports_heal_skill = False
    init default sports_roundhouse_skill = False
    init default sports_store_sp1 = False
    init default sports_store_sp2 = False
    init default sports_store_sp3 = False
    init default sports_pow = 0
    init default sports_dex = 0
    init default sports_hp = 0
    init default sports_mov = 0
    init default sports_tutorial = False
    init default sports_opponent_idx = 0
    init default sports_counter_skill = False
    init default brawler_hard_mode = False
    init default brawler_question = False
    init default brawler_difficulty = 0
    init default sports_opponents = ["Kujon", "#c700dd", "sports_avatar_nerd", "Prep", "#87fa5a", "sports_avatar_prep", "Jock", "#23b4fc", "sports_avatar_jock", "Chad", "#23b4fc", "sports_avatar_chad", "Troy", "#ff0000", "sports_avatar_troy"]
    init default sports_opponents_tiles = ["sports_nerd_tile", "sports_nerd_tile_attackable","sports_prep_tile", "sports_prep_tile_attackable", "sports_jock_tile","sports_jock_tile_attackable", "sports_chad_tile", "sports_chad_tile_attackable", "sports_troy_tile", "sports_troy_tile_attackable"]
    init default sports_opponents_stats = [1, 1, 3, 1, 2, 2, 2, 2, 4, 4, 2, 2, 4, 4, 4, 4, 1, 1, 2, 3, 3, 3, 2, 2]
    init default sports_skillpointsleft = 0
    init default cpu_name = sports_opponents[sports_opponent_idx*3]
    init default cpu_color = sports_opponents[sports_opponent_idx*3+1]
    init default cpu_avatar = sports_opponents[sports_opponent_idx*3+2]
    init default sports_cpu_hp = sports_opponents_stats[sports_opponent_idx*4]
    init default sports_cpu_pow = sports_opponents_stats[sports_opponent_idx*4 + 1]
    init default sports_cpu_dex = sports_opponents_stats[sports_opponent_idx*4 + 2]
    init default sports_cpu_mov = sports_opponents_stats[sports_opponent_idx*4 + 3]
    init default cpu_hp_state = 1
    init default sports_pc_hp = 90 + 10 * sports_hp
    init default sports_rounded_player_hp = sports_pc_hp
    init default sports_rounded_cpu_hp = sports_cpu_hp
    init default sports_pow_multi = [0.0, 1.0, 1.25 ,1.5, 2.0]
    init default sports_victory = False
    init default bg_ok_choice = False
    init default menuGalleryOpen = False
    init default unlockedScenes = 0
    init default affinity = "NEUTRAL"
    init default swyper_app_enabled = False
    init default newSwypeMsgNicole = 0
    init default newSwypeMsgCatrin = 0
    init default newSwypeMsgCathy = 0
    init default newSwypeMsgEllie = 0
    init default newSwypeMsgArieth = 0
    init default newSwypeMsgNora = 0
    init default chat_reply = ""
    init default chat_reply_array = ["","",""]
    init default drunk_reply_array = ["","",""]
    init default chat_next_state_array = ["","",""]
    init default chat_mc_avatar = "swyper_chat_mc1_avatar"
    init default chat_dad_state = "1"
    init default chat_derek_state = "1"
    init default chat_isabella_state = "1"
    init default chat_jill_state = "1"
    init default chat_josy_state = "1"
    init default chat_magnar_state = "1"
    init default chat_maya_state = "1"
    init default chat_quinn_state = "1"
    init default chat_sage_state = "1"
    init default chat_dad_history = []
    init default chat_derek_history = []
    init default chat_isabella_history = []
    init default chat_jill_history = []
    init default chat_josy_history = []
    init default chat_magnar_history = []
    init default chat_maya_history = []
    init default chat_quinn_history = []
    init default chat_sage_history = []
    init default chat_dad_history_is_them = []
    init default chat_derek_history_is_them = []
    init default chat_isabella_history_is_them = []
    init default chat_jill_history_is_them = []
    init default chat_josy_history_is_them = []
    init default chat_magnar_history_is_them = []
    init default chat_maya_history_is_them = []
    init default chat_quinn_history_is_them = []
    init default chat_sage_history_is_them = []
    init default newMessageIntJosy = 0
    init default newMessageIntSage = 0
    init default newMessageIntDerek = 0
    init default newMessageIntDad = 0
    init default newMessageIntIsabella = 0
    init default newMessageIntJill = 0
    init default newMessageIntMagnar = 0
    init default newMessageIntQuinn = 0
    init default newMessageIntMaya = 0
    init default roosterPostsArray = []
    init default roosterLikesArray = []
    init default roosterLikedArray = []
    init default roosterAvatarArray = []
    init default roosterNickArray = []
    init default roosterTextArray = []
    init default roosterPhotoArray = []
    init default roosterCommentSectionArray = []
    init default roosterCurrentIdx = 0
    init default mc_avatar = "rooster_mini_mc1"
    init default bios_avatar_mc = "bios_avatar_mc1"
    init default mbios_mc = "mbios_mc1"
    init default mbios_mc_new_hover = "mbios_mc1_new_hover"
    init default mbios_mc_new = "mbios_mc1_new"
    init default mbios_mc_hover = "mbios_mc1_hover"
    init default roosterNickMCCustom = "Tremolo"
    init default roosterNickMC = "[name]@[roosterNickMCCustom]"
    init default swyperNickMCCustom = "Tremolo"
    init default tmpname = ""
    init default tmpnameRooster = "Tremolo"
    init default tmpnameSwyper = "Tremolo"
    init default roosterNickAlex = "Alex@OnePunchAlex"
    init default roosterNickAnthony = "Anthony@BigA"
    init default roosterNickArieth = "Arieth@AriethPassword1234"
    init default roosterNickAshley = "Ashley@JustAsh"
    init default roosterNickBert = "Bert@Thalidomide"
    init default roosterNickBeth = "Beth@MoreThanJustAWaitress"
    init default roosterNickBrandi = "Brandi@MochaLatte"
    init default roosterNickBurke = "Burke@ProfessorStephenBurke"
    init default roosterNickCaleb = "Caleb@FeelThePump"
    init default roosterNickCamila = "Camila@Cammy"
    init default roosterNickCathy = "Cathy@CathyJones79"
    init default roosterNickChad = "Chad@MadLadChad"
    init default roosterNickChristian = "Christian@PlayOnPlayer"
    init default roosterNickDany = "Dany@BunnyHop"
    init default roosterNickDawe = "Dawe@BigDickDawe"
    init default roosterNickDerek = "Derek@BigBootyLover"
    init default roosterNickDik = "DIKsOfficial@DIKsOfficial"
    init default roosterNickElena = "Elena@CuteButt"
    init default roosterNickEnvy = "Nicole@TwoToTango"
    init default roosterNickEugene = "Eugene@MrDynamite"
    init default roosterNickGordon = "Gordon@Diamonds"
    init default roosterNickHeather = "Heather@HOTHeather"
    init default roosterNickIsabella = "Isabella@IsabellaRoberts"
    init default roosterNickJacob = "Jacob@DIKJacob"
    init default roosterNickJade = "Jade@DrJadeBurke"
    init default roosterNickJamie = "Jamie@DIKJam"
    init default roosterNickJill = "Jill@EbonyAndIvory"
    init default roosterNickJimmy = "Jimmy@Chevy69"
    init default roosterNickJohn = "John@MilkMan"
    init default roosterNickJohnBoy = "JohnBoy@DIKJB"
    init default roosterNickJosy = "Josy@MsSunshine"
    init default roosterNickLeon = "Leon@DIKLeon"
    init default roosterNickLily = "Lily@LikeTheFlower"
    init default roosterNickLucas = "Lucas@TheThird"
    init default roosterNickMagnar = "Magnar@SirMagnar"
    init default roosterNickMaya = "Maya@MayaTheMoviebuff"
    init default roosterNickMelanie = "Melanie@CaraMel"
    init default roosterNickMinny = "Minny@FemGirlPower"
    init default roosterNickMona = "Mona@MonaLisa"
    init default roosterNickNick = "Nick@DIKNick"
    init default roosterNickOliver = "Oliver@Buttons"
    init default roosterNickQuinn = "Quinn@QuinnOfHearts"
    init default roosterNickRich = "Rich@IAmRich"
    init default roosterNickRiona = "Riona@HOTRiona"
    init default roosterNickRon = "Ron@MegatRon"
    init default roosterNickRose = "Rose@GinAndTonic"
    init default roosterNickRusty = "Rusty@DIKPresidentRusty"
    init default roosterNickSage = "Sage@HOTPresidentSage"
    init default roosterNickSally = "Sally@Sallycylic"
    init default roosterNickSarah = "Sarah@HOTSarah"
    init default roosterNickTommy = "Tommy@DIKTommyTheDestroyer"
    init default roosterNickTrent = "Trent@LordTrent"
    init default roosterNickTroy = "Troy@FingerRoll"
    init default roosterNickTybalt = "Tybalt@PresidentTybaltBurke"
    init default roosterNickWendy = "Wendy@TheRealestWoman"
    init default roosterNickAlt = "Tyballs@PresidentTyballs"
    init default rooster_jump_label = ""
    init default rooster_reply = ""
    init default roosterHistory_text_JillEp3 = []
    init default roosterHistory_text_RustyEp3 = []
    init default roosterHistory_text_MayaEp3 = []
    init default roosterHistory_text_QuinnEp3 = []
    init default roosterHistory_text_CathyEp3 = []
    init default roosterHistory_text_RionaEp3 = []
    init default roosterHistory_text_SageEp3 = []
    init default roosterHistory_text_DaweEp4 = []
    init default roosterHistory_text_JillEp4 = []
    init default roosterHistory_text_SageEp4 = []
    init default roosterHistory_text_DerekEp4 = []
    init default roosterHistory_text_IsabellaEp4 = []
    init default roosterHistory_text_Sage2Ep4 = []
    init default roosterHistory_text_TybaltEp4 = []
    init default roosterHistory_text_CamilaEp4 = []
    init default roosterHistory_text_CathyEp4 = []
    init default roosterHistory_avatar_JillEp3 = []
    init default roosterHistory_avatar_RustyEp3 = []
    init default roosterHistory_avatar_MayaEp3 = []
    init default roosterHistory_avatar_QuinnEp3 = []
    init default roosterHistory_avatar_CathyEp3 = []
    init default roosterHistory_avatar_SageEp3 = []
    init default roosterHistory_avatar_RionaEp3 = []
    init default roosterHistory_avatar_DaweEp4 = []
    init default roosterHistory_avatar_JillEp4 = []
    init default roosterHistory_avatar_SageEp4 = []
    init default roosterHistory_avatar_DerekEp4 = []
    init default roosterHistory_avatar_IsabellaEp4 = []
    init default roosterHistory_avatar_Sage2Ep4 = []
    init default roosterHistory_avatar_TybaltEp4 = []
    init default roosterHistory_avatar_CamilaEp4 = []
    init default roosterHistory_avatar_CathyEp4 = []
    init default roosterHistory_nick_JillEp3 = []
    init default roosterHistory_nick_RustyEp3 = []
    init default roosterHistory_nick_MayaEp3 = []
    init default roosterHistory_nick_RionaEp3 = []
    init default roosterHistory_nick_QuinnEp3 = []
    init default roosterHistory_nick_CathyEp3 = []
    init default roosterHistory_nick_SageEp3 = []
    init default roosterHistory_nick_DaweEp4 = []
    init default roosterHistory_nick_JillEp4 = []
    init default roosterHistory_nick_SageEp4 = []
    init default roosterHistory_nick_DerekEp4 = []
    init default roosterHistory_nick_IsabellaEp4 = []
    init default roosterHistory_nick_Sage2Ep4 = []
    init default roosterHistory_nick_TybaltEp4 = []
    init default roosterHistory_nick_CamilaEp4 = []
    init default roosterHistory_nick_CathyEp4 = []
    init default roosterHistory_likes_JillEp3 = []
    init default roosterHistory_likes_RustyEp3 = []
    init default roosterHistory_likes_MayaEp3 = []
    init default roosterHistory_likes_RionaEp3 = []
    init default roosterHistory_likes_QuinnEp3 = []
    init default roosterHistory_likes_CathyEp3 = []
    init default roosterHistory_likes_SageEp3 = []
    init default roosterHistory_likes_DaweEp4 = []
    init default roosterHistory_likes_JillEp4 = []
    init default roosterHistory_likes_SageEp4 = []
    init default roosterHistory_likes_DerekEp4 = []
    init default roosterHistory_likes_IsabellaEp4 = []
    init default roosterHistory_likes_Sage2Ep4 = []
    init default roosterHistory_likes_TybaltEp4 = []
    init default roosterHistory_likes_CamilaEp4 = []
    init default roosterHistory_likes_CathyEp4 = []
    init default roosterHistory_liked_JillEp3 = []
    init default roosterHistory_liked_RustyEp3 = []
    init default roosterHistory_liked_MayaEp3 = []
    init default roosterHistory_liked_RionaEp3 = []
    init default roosterHistory_liked_QuinnEp3 = []
    init default roosterHistory_liked_CathyEp3 = []
    init default roosterHistory_liked_SageEp3 = []
    init default roosterHistory_liked_DaweEp4 = []
    init default roosterHistory_liked_JillEp4 = []
    init default roosterHistory_liked_SageEp4 = []
    init default roosterHistory_liked_DerekEp4 = []
    init default roosterHistory_liked_IsabellaEp4 = []
    init default roosterHistory_liked_Sage2Ep4 = []
    init default roosterHistory_liked_TybaltEp4 = []
    init default roosterHistory_liked_CamilaEp4 = []
    init default roosterHistory_liked_CathyEp4 = []
    init default roosterChoices_JillEp3 = []
    init default roosterChoices_RustyEp3 = []
    init default roosterChoices_MayaEp3 = []
    init default roosterChoices_RionaEp3 = []
    init default roosterChoices_QuinnEp3 = []
    init default roosterChoices_CathyEp3 = []
    init default roosterChoices_SageEp3 = []
    init default roosterChoices_DaweEp4 = []
    init default roosterChoices_JillEp4 = []
    init default roosterChoices_SageEp4 = []
    init default roosterChoices_DerekEp4 = []
    init default roosterChoices_IsabellaEp4 = []
    init default roosterChoices_Sage2Ep4 = []
    init default roosterChoices_TybaltEp4 = []
    init default roosterChoices_CamilaEp4 = []
    init default roosterChoices_CathyEp4 = []
    init default ep4_cluckDaweState = 0
    init default ep4_cluckSage2State = 0
    init default ep4_cluckJillState = 0
    init default rooster_liked_tybalt_post_ep4 = False
    init default rooster_liked_tybalt2_post_ep4 = False
    init default new_rooster_int = 0
    init default state = "df"
    init default e_time = 0
    init default c_time = 0
    init default t_time = 0
    init default maxedMath_s2 = 0
    init default maxedEnglish_s2 = 0
    init default maxedGender_s2 = 0
    init default map_fast_travel_enabled = True
    init default map_system_list = []
    init default permanent_affinity = False
    init default phone_opened = False
    init default wallet_lvl = 0
    init default mphone_current_input = ""
    init default dollar = 1
    init default mc_camila = ""
    init default mc_cathy = ""
    init default mc_isabella = ""
    init default mc_jade = ""
    init default mc_jill = ""
    init default mc_josy = ""
    init default mc_maya = ""
    init default mc_quinn = ""
    init default mc_riona = ""
    init default mc_sage = ""
    init default failedGame = False
    init default earnedMoney = 0
    init default spentMoney = 0
    init default maxedPaths = 0
    $ achievement.register("MAGAZINECOLLECTOR")
    $ achievement.register("ALLSCENES")
    $ achievement.register("NOTSOPOORAFTERALL")
    $ achievement.register("POORAGAIN")
    $ achievement.register("JAILBREAK")
    init default steamAchievements = False
    init default steamConfig = False
    init default nonPatreonConfig = True
    init default foundCards = 0
    init default foundCards_s2 = 0
    init default unlockedScenes_s2 = 0
    init default game_is_ending = False
    init default randInt = 0
    init default guideSuggestedPage = 1
    init define max_page_walkthrough = 162
    init default guideCurrentPage = 1
    init default rewards_renders_list = []
    init default tmpBool = False
    init default tmpBool2 = False
    init default tmpInt = 0
    init default tmpInt2 = 0
    init default toggled_2d_mode = 1
    init default episode_title_name = "Inicjacja"
    init default laptop_wallpapers = ["default_wallpaper","default_wallpaper1","default_wallpaper2","default_wallpaper3","default_wallpaper4","default_wallpaper5","default_wallpaper6","default_wallpaper7","default_wallpaper8","default_wallpaper9","default_wallpaper10","default_wallpaper11","default_wallpaper12","default_wallpaper13","default_wallpaper14","default_wallpaper15","default_wallpaper16","default_wallpaper17"]
    init default currentWallpaperPreview = 0
    init default currentWallpaperPage = 0
    init default laptop_wallpapers_criteria_met = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    init default laptop_wallpapers_unlocked = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    init default mphone_bios_chars = []
    init default mphone_current_bios_char = 0
    init default mphone_bios_sort_by = ["Alphabetical","Girls","Guys","DIKs","HOTs","Jocks","Preps","Nerds","Staff/Teachers"]
    init default mphone_bios_sort_by_idx = 0
    init default mphone_triple_tile_is_playing = False
    init default triple_tile_new_highscore = 0
    init default triple_tile_score = 0
    init default triple_tile_turn = 0
    init default triple_turn_to_beat = 15
    init default triple_card_number_of_cards = 6
    init default triple_tile_chosen_tile = -1
    init default triple_tile_game_over = False
    init default triple_tile_show_numbers = False
    init default triple_tile_easy_mode = False
    init default triple_tile_new_high_score = 0
    init default triple_tile_hovered_tile = [-1,-1]
    init default triple_tile_hs_checked = False
    init default triple_tile_spr = [[False,False,False],[False,False,False],[False,False,False]]
    init default triple_tile_sets = [[0,0,0],[0,0,0],[0,0,0]]
    init default triple_tile_grid = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
    init default triple_tile_grid_spr = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
    jump ep1_start_label
init:
    $ config.debug_image_cache = True
    if renpy.loadable("season2/scripts/update5.rpyc"):
        $ spr_mm_quinn_s2 = ["gui/main_menu_sprites/season2/spr_quinn_alley.jpg", 1.07, "gui/main_menu_sprites/season2/spr_quinn.png", 1.18,"gui/main_menu_sprites/season2/spr_quinn_rain.png", 1.5]
        $ spr_mm_jocks_s2 = ["spr_jock_bg", 1.07, "spr_jock_ant", 1.15, "spr_jock_dawe", 1.28]
        $ spr_mm_derek_s2 = ["gui/main_menu_sprites/season2/spr_derek_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_derek_wendy.png", 1.08,"gui/main_menu_sprites/season2/spr_derek_derek.png", 1.12]
        $ spr_mm_jb_s2 = ["gui/main_menu_sprites/season2/spr_jb_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_jb_jill.png", 1.08,"gui/main_menu_sprites/season2/spr_jb_bella.png", 1.12]
        $ spr_mm_rc_s2 = ["gui/main_menu_sprites/season2/spr_rc_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_rc_trees.png", 1.07,"gui/main_menu_sprites/season2/spr_rc_riona.png", 1.12]
        $ spr_mm_hots_s2 = ["gui/main_menu_sprites/season2/spr_hots_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_hots_melanie.png", 1.07,"gui/main_menu_sprites/season2/spr_hots_lily.png", 1.12]
        $ spr_mm_sage_s2 = ["gui/main_menu_sprites/season2/spr_sage_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_sage_sage.png", 1.07,"gui/main_menu_sprites/season2/spr_sage_steam.png", 1.12]
        $ spr_mm_jm_s2 = ["gui/main_menu_sprites/season2/spr_jm_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_jm_jetty.png", 1.07,"gui/main_menu_sprites/season2/spr_jm_josy.png", 1.12]
        $ spr_mm_jade_s2 = ["gui/main_menu_sprites/season2/spr_jade_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_jade_jade.png", 1.12]
        $ spr_mm_tybalt_s2 = ["gui/main_menu_sprites/season2/spr_tybalt_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_tybalt_trent.png", 1.07,"gui/main_menu_sprites/season2/spr_tybalt_tybalt.png", 1.12]
        $ spr_mm_nerds_s2 = ["gui/main_menu_sprites/season2/spr_nerds_bg.jpg", 1.02, "gui/main_menu_sprites/season2/spr_nerds_sally.png", 1.07,"spr_nerds_glowing", 1.12]
        $ spr_mm_mc_s2 = ["gui/main_menu_sprites/season2/spr_mc_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_mc_mc.png", 1.08]
        $ spr_mm_rose_s2 = ["gui/main_menu_sprites/season2/spr_rose_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_rose_rose.png", 1.08]
        $ spr_mm_diks_s2 = ["gui/main_menu_sprites/season2/spr_diks_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_diks_elena.png", 1.08]
        $ spr_mm_diks2_s2 = ["gui/main_menu_sprites/season2/spr_diks2_bg.jpg", 1.02, "gui/main_menu_sprites/season2/empty.png", 1.07,"gui/main_menu_sprites/season2/spr_diks2_vinny.png", 1.09]
        $ spr_mm_arr_s2 = [spr_mm_quinn_s2, spr_mm_jocks_s2, spr_mm_jb_s2, spr_mm_rc_s2, spr_mm_hots_s2, spr_mm_sage_s2, spr_mm_jm_s2, spr_mm_jade_s2, spr_mm_derek_s2, spr_mm_tybalt_s2, spr_mm_nerds_s2, spr_mm_mc_s2, spr_mm_rose_s2, spr_mm_diks_s2, spr_mm_diks2_s2]
        $ renpy.random.shuffle(spr_mm_arr_s2)
    $ spr_mm_sage = ["gui/main_menu_sprites/spr_sage_dorm.jpg",1.03,"gui/main_menu_sprites/spr_sage_lamp.png",1.05,"gui/main_menu_sprites/spr_sage.png",1.1]
    $ spr_mm_jocks = ["gui/main_menu_sprites/spr_jocks.jpg", 1.07, "gui/main_menu_sprites/spr_anthony.png", 1.15,"gui/main_menu_sprites/spr_dawe.png", 1.28]
    $ spr_mm_hots = ["gui/main_menu_sprites/spr_hots.jpg", 1.07, "gui/main_menu_sprites/spr_quinn.png", 1.15,"gui/main_menu_sprites/spr_quinn_lolly.png", 1.28]
    $ spr_mm_maya = ["gui/main_menu_sprites/spr_maya_bed.jpg", 1.07, "gui/main_menu_sprites/spr_maya.png", 1.1,"gui/main_menu_sprites/spr_maya_basket.png", 1.15]
    $ spr_mm_josy = ["gui/main_menu_sprites/spr_forest.jpg", 1.03, "gui/main_menu_sprites/spr_josy_tree.png", 1.04,"gui/main_menu_sprites/spr_josy.png", 1.05]
    $ spr_mm_jill = ["gui/main_menu_sprites/spr_mansion.jpg", 1.03, "gui/main_menu_sprites/spr_jill.png", 1.12, "gui/main_menu_sprites/spr_gates.png", 1.07]
    $ spr_mm_bella = ["gui/main_menu_sprites/spr_bella_home.jpg", 1.05, "gui/main_menu_sprites/spr_bella.png", 1.08, "gui/main_menu_sprites/spr_bella_table.png", 1.3]
    $ spr_mm_tommy = ["gui/main_menu_sprites/spr_tommy_bg.jpg", 1.05, "gui/main_menu_sprites/spr_tommy.png", 1.08,"gui/main_menu_sprites/spr_tommy_coin.png", 1.2]
    $ spr_mm_jade = ["gui/main_menu_sprites/spr_jade_bg.jpg", 1.05, "gui/main_menu_sprites/spr_derek.png", 1.08, "gui/main_menu_sprites/spr_jade.png", 1.1]
    $ spr_mm_magnar = ["gui/main_menu_sprites/spr_magnar_bg.jpg",1.05, "gui/main_menu_sprites/spr_magnar.png", 1.15, "gui/main_menu_sprites/spr_books.png",1.3]
    $ spr_mm_cathy = ["gui/main_menu_sprites/spr_cathy_bg.jpg",1.05, "gui/main_menu_sprites/spr_cathy_main.png", 1.15, "gui/main_menu_sprites/spr_cathy_desk.png",1.3]
    $ spr_mm_hots2 = ["gui/main_menu_sprites/spr_hots_bg.jpg",1.05, "gui/main_menu_sprites/spr_hots_main.png", 1.09, "gui/main_menu_sprites/spr_hots_girls.png",1.2]
    $ spr_mm_rose = ["gui/main_menu_sprites/spr_rose_bg.jpg",1.05, "gui/main_menu_sprites/spr_rose_main.png", 1.08, "gui/main_menu_sprites/spr_rose_girls.png",1.2]
    $ spr_mm_arr = [spr_mm_sage, spr_mm_jocks, spr_mm_hots, spr_mm_maya, spr_mm_josy, spr_mm_jill, spr_mm_bella, spr_mm_tommy, spr_mm_jade, spr_mm_magnar, spr_mm_cathy, spr_mm_rose, spr_mm_hots2]
    $ renpy.random.shuffle(spr_mm_arr)
    $ musicCreditsOpen = False
    $ renpy.music.register_channel("sfx1", "sfx")
    $ renpy.music.register_channel("sfx2", "sfx")
    $ renpy.music.register_channel("music1", "music")
    $ renpy.music.register_channel("jill", "voice")
    $ renpy.music.register_channel("bella", "voice")
    if persistent.current_episode == None:
        $ persistent.current_episode = 1
    if persistent.tutorials == None:
        $ persistent.tutorials = False
    if persistent.pet_app_unlocked == None:
        $ persistent.pet_app_unlocked = False
    if persistent.firstTimePlaying == None:
        $ persistent.firstTimePlaying = True
    if persistent.josy == None:
        $ persistent.josy = "Josy"
    if persistent.maya == None:
        $ persistent.maya = "Maya"
    if persistent.sage == None:
        $ persistent.sage = "Sage"
    if persistent.isabella == None:
        $ persistent.isabella = "Isabella"
    if persistent.jill == None:
        $ persistent.jill = "Jill"
    if persistent.quinn == None:
        $ persistent.quinn = "Quinn"
    if persistent.riona == None:
        $ persistent.riona = "Riona"
    if persistent.jade == None:
        $ persistent.jade = "Jade"
    if persistent.cathy == None:
        $ persistent.cathy = "Cathy"
    if persistent.camila == None:
        $ persistent.camila = "Camila"
    if persistent.ep1_card1 == None:
        $ persistent.ep1_card1 = False
    if persistent.ep1_card2 == None:
        $ persistent.ep1_card2 = False
    if persistent.ep1_card3 == None:
        $ persistent.ep1_card3 = False
    if persistent.ep1_card4 == None:
        $ persistent.ep1_card4 = False
    if persistent.ep1_card5 == None:
        $ persistent.ep1_card5 = False
    if persistent.ep1_card6 == None:
        $ persistent.ep1_card6 = False
    if persistent.ep1_card7 == None:
        $ persistent.ep1_card7 = False
    if persistent.ep1_card8 == None:
        $ persistent.ep1_card8 = False
    if persistent.ep1_card9 == None:
        $ persistent.ep1_card9 = False
    if persistent.ep1_card10 == None:
        $ persistent.ep1_card10 = False
    if persistent.ep1_card11 == None:
        $ persistent.ep1_card11 = False
    if persistent.ep1_card12 == None:
        $ persistent.ep1_card12 = False
    if persistent.ep1_card13 == None:
        $ persistent.ep1_card13 = False
    if persistent.ep1_card14 == None:
        $ persistent.ep1_card14 = False
    if persistent.ep1_card15 == None:
        $ persistent.ep1_card15 = False
    if persistent.ep1_card16 == None:
        $ persistent.ep1_card16 = False
    if persistent.ep1_card17 == None:
        $ persistent.ep1_card17 = False
    if persistent.ep1_card18 == None:
        $ persistent.ep1_card18 = False
    if persistent.rew_josy_unlocked == None:
        $ persistent.rew_josy_unlocked = 0
    if persistent.rew_maya_unlocked == None:
        $ persistent.rew_maya_unlocked = 0
    if persistent.rew_isa_unlocked == None:
        $ persistent.rew_isa_unlocked = 0
    if persistent.rew_sage_unlocked == None:
        $ persistent.rew_sage_unlocked = 0
    if persistent.rew_quinn_unlocked == None:
        $ persistent.rew_quinn_unlocked = 0
    if persistent.rew_jade_unlocked == None:
        $ persistent.rew_jade_unlocked = 0
    if persistent.rew_jill_unlocked == None:
        $ persistent.rew_jill_unlocked = 0
    if persistent.rew_riona_unlocked == None:
        $ persistent.rew_riona_unlocked = 0
    if persistent.rew_camila_unlocked == None:
        $ persistent.rew_camila_unlocked = 0
    if persistent.rew_mixed_unlocked == None:
        $ persistent.rew_mixed_unlocked = 0
    if persistent.rew_cathy_unlocked == None:
        $ persistent.rew_cathy_unlocked = 0
    if persistent.default_text_box_mode == None:
        $ persistent.default_text_box_mode = True
    if persistent.text_box_tutorial == None:
        $ persistent.text_box_tutorial = False
    if persistent.map_fast_travel == None:
        $ persistent.map_fast_travel = True
    if persistent.steam_owns_al == None:
        $ persistent.steam_owns_al = False
    if persistent.steam_owns_guide_s1 == None:
        $ persistent.steam_owns_guide_s1 = False
    if persistent.walkthrough_tutorial == None:
        $ persistent.walkthrough_tutorial = False
    if persistent.walkthrough_tutorial_s2 == None:
        $ persistent.walkthrough_tutorial_s2 = False
    if persistent.steam_owns_s2 == None:
        $ persistent.steam_owns_s2 = False
    $ config.autosave_on_choice = False
    $ _preferences.gl_powersave = False
    if persistent.autosave == None:
        $ persistent.autosave = True
    if persistent.autosave == None:
        $ persistent.autosave = True
    $ config.has_autosave = persistent.autosave
    if persistent.rewards_screen_on_hover == None:
        $ persistent.rewards_screen_on_hover = False
    if persistent.chat_new_rewards == None:
        $ persistent.chat_new_rewards = False
init:
    python:
        def is_subscribed_app_al():
            return is_subscribed_app(1045520)
        def is_subscribed_app_guide_s1():
            return is_subscribed_app(1223490)
        def activate_overlay_to_store_al():
            activate_overlay_to_store(1045520, 0)
        def activate_overlay_to_store_badik():
            activate_overlay_to_store(1126320, 0)
        def activate_overlay_to_store_badik_s1_guide():
            activate_overlay_to_store(1223490, 0)
        def activate_overlay_to_store_badik_s2():
            activate_overlay_to_store(1215820, 0)
        def activate_overlay_to_store_badik_s2_guide():
            activate_overlay_to_store(1631620, 0)
        def is_subscribed_app_s2():
            return is_subscribed_app(1215820)
        def is_subscribed_app_guide_s2():
            return is_subscribed_app(1631620)

return