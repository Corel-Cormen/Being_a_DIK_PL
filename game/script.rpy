label ep1_start_label:

if steamConfig:
    $ state = "ep1_steam"
else:
    $ state = "ep1"
window hide
call rpc from _call_rpc_5
stop music fadeout 5
scene black with fade
$ randInt = renpy.random.randint(0, 9)
show screen keymap_screen
$ brawler_question = True
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
#show text "{i}There are mini-games in this game.\nThe mini-games are optional but they offer you rewards such as special renders and money to spend.{/i}"
show text "{i}W tej grze są minigry.\nMinigry są opcjonalne, ale oferują nagrody, takie jak specjalne rendery i pieniądze do wydania.{/i}"
$ renpy.pause()
hide text
#show text "{i}If you choose to skip mini-games, you may miss out on minor special events that happen during, or as a result of, the mini-game.{/i}"
show text "{i}Jeśli zdecydujesz się pominąć minigry, możesz przegapić drobne specjalne wydarzenia, które mają miejsce podczas minigry lub w jej wyniku.{/i}"
$ renpy.pause()
hide text
#show text "{i}Special renders won from mini-games can still be acquired in other ways.{/i}"
show text "{i}Specjalne rendery wygrane z minigier można zdobyć na inne sposoby.{/i}"
$ renpy.pause()
hide text
#show text "{i}Do you want to skip mini-games?{/i}"
show text "{i}Czy chcesz pominąć minigry?{/i}"
menu:
#    "Play mini-games":
    "Graj w minigry":
        hide text
        $ dollar = 1
        $ minigames = True
#        show text "{i}Done! You will always have to play the mini-games.\nIf you change your mind, you must restart the game.{/i}"
        show text "{i}Gotowe! Zawsze będziesz musiał grać w minigry.\nJeśli zmienisz zdanie, musisz ponownie uruchomić grę.{/i}"
        $ renpy.pause()
        hide text
#    "Skip all mini-games":
    "Pomiń wszystkie minigry":
        hide text
        $ dollar = 2
        $ minigames = False
#        show text "{i}You will never be asked to play a mini-game during this playthrough again.\nIf you change your mind, you must restart the game.{/i}"
        show text "{i}Już nigdy nie zostaniesz poproszony o zagranie w minigrę podczas tej gry.\nJeśli zmienisz zdanie, musisz ponownie uruchomić grę.{/i}"
        $ renpy.pause()
        hide text
#        show text "{i}To compensate for the loss of money, from not playing mini-games, you'll get double the money tokens from finding in-game money.{/i}"
        show text "{i}Aby zrekompensować stratę pieniędzy spowodowaną nie graniem w minigry, otrzymasz podwójne żetony pieniędzy za znalezienie pieniędzy w grze.{/i}"
        $ renpy.pause()
        hide text
play music "music/ep1/apra_hyde.mp3" fadein 3
#"Family."
"Rodzina."
#"My dad once told me that a family is more than blood relations."
"Mój tata powiedział mi kiedyś, że rodzina to coś więcej niż więzy krwi."
#"Being related doesn't necessarily make you family."
"Bycie spokrewnionym niekoniecznie czyni cię rodziną."
#"Family are the people who support you in your choices."
"Rodzina to ludzie, którzy wspierają Cię w dokonywaniu wyborów."
#"Family will help you grow."
"Rodzina pomoże Ci się rozwijać."
#"Family doesn't give up on you in times of need."
"Rodzina nie porzuca cię w potrzebie."
#"Family are the ones who love you for you..."
"Rodzina to ci, którzy kochają Cię za to, kim jesteś..."
#"...whoever that may be."
"...kimkolwiek by to nie było."
#"Even if you lose your family..."
"Nawet jeśli stracisz rodzinę..."
#"...or if your family loses you."
"...albo jeśli twoja rodzina cię straci."
#"Don't stop."
"Nie przestawaj."
#"Find new ones to love and somewhere else to call home."
"Znajdź nowych, których pokochasz i znajdź inne miejsce, które nazwiesz domem."
scene d_intro with fade:
    linear 30 zoom 1.02
#"That's me and my dad."
"To ja i mój tata."
#"We took that photo the day I got my driver's license."
"Zrobiliśmy to zdjęcie w dniu, w którym otrzymałem prawo jazdy."
#"He was so happy that it looks like he is trying to swallow a coat hanger."
"Był tak szczęśliwy, że wyglądało to tak, jakby próbował połknąć wieszak na ubrania."
#"Back then, it was just me and him."
"Wtedy byliśmy tylko ja i on."
#"My mother died shortly after giving birth to me."
"Moja matka zmarła niedługo po urodzeniu mnie."
#"It's a shame that I never got to meet her."
"Szkoda, że nigdy jej nie poznałem."
#"I would have loved hearing stories from her past and truly getting to know her."
"Bardzo chciałbym usłyszeć historie z jej przeszłości i naprawdę ją poznać."
#"Sure, my dad told me stories growing up...but his memory sucked."
"Jasne, tata opowiadał mi historie, jak dorastałem...ale jego pamięć była do bani."
#"He would always forget the punchline. Not surprising, since he would talk so long before reaching the point where the punchline was supposed to be."
"Zawsze zapominał puenty. Nic dziwnego, skoro mówił tak długo, zanim dotarł do punktu, w którym miała być puenta."
#"Either way, I was happy back then. We didn't have much, we...erm..."
"Tak czy inaczej, byłem wtedy szczęśliwy. Nie mieliśmy wiele, my...hm..."
#"...we had enough."
"Miałyśmy tego dość."
#"We had each other."
"Mieliśmy siebie."
#"As for now?"
"Jak na razie?"
stop music fadeout 3
#"Let me tell you what happened."
"Opowiem ci, co się stało."
$ guideSuggestedPage = 27
scene d0_intro with Fade(1.5,1,0.5)
play music "music/ep1/windswept.mp3"
#js "Haha! You're so silly!"
js "Haha! Jesteś taki głupi!"
#js "You wanna know something...?"
js "Chcesz coś wiedzieć...?"
#js "I've always had a crush on you..."
js "Zawsze mi się podobałeś. "
scene d0_intro1 with dissolve
#js "What?"
js "Co?"
#js "You've been in love with me all this time, too?"
js "Ty też byłeś we mnie zakochany przez cały ten czas?"
scene d0_intro2 with dissolve
#js "You're so sweet..."
js "Jesteś taki słodki..."
scene d0_intro3 with dissolve
#js "Come closer..."
js "Podejdź bliżej..."
scene d0_intro4 with dissolve
#js "I wanna feel your soft lips pressed against mine..."
js "Chcę poczuć twoje miękkie usta przyciśnięte do moich..."
#js "Kiss me..."
js "Pocałuj mnie."
play sound "sound_effects/shove.mp3"
stop music
scene d0_intro5 with hpunch
$ renpy.pause()
play music "music/ep1/roadtrip.mp3"
scene d0_intro5b with dissolve
#cl "Hey, fuckface!"
st "Hej, pojebie!"
#cl "I said, stop daydreaming and get back to work!"
st "Powiedziałem, przestań marzyć i wracaj do pracy!"
scene d0_intro5c with dissolve
#mc "My name is not fuckface!"
mc "Nie nazywaj mnie pojebem!"
#mc "It's..."
mc "Jestem..."
label getPlayerName:

$ name = renpy.input("Jak masz na imię?", length=15)
$ name = name.strip()
if name == "":
    jump getPlayerName
$ tmpname = name
$ persistent.name = name
$ mc_josy = name
$ mc_maya = name
$ mc_sage = name
$ mc_isabella = name
$ mc_jill = name
$ mc_quinn = "pervert"
$ mc_riona = name
$ mc_jade = name
$ mc_cathy = name
$ mc_camila = name
if persistent.mc_josy == None:
    $ persistent.mc_josy = name
if persistent.mc_maya == None:
    $ persistent.mc_maya = name
if persistent.mc_sage == None:
    $ persistent.mc_sage = name
if persistent.mc_isabella == None:
    $ persistent.mc_isabella = name
if persistent.mc_jill == None:
    $ persistent.mc_jill = name
if persistent.mc_quinn == None:
    $ persistent.mc_quinn = name
if persistent.mc_riona == None:
    $ persistent.mc_riona = name
if persistent.mc_jade == None:
    $ persistent.mc_jade = name
if persistent.mc_cathy == None:
    $ persistent.mc_cathy = name
if persistent.mc_camila == None:
    $ persistent.mc_camila = name
if name == "fuckface" or name == "Fuckface":
#    mc "Oh, wait...it is..."
    mc "Och, czekaj...tak jest..."
else:
#    mc "...[name]!"
    mc "...[name]!"
scene d0_intro5d with dissolve
#cl "Whatever! Get back to work, or I'll tell my dad, ok!?"
st "Nieważne! Wracaj do pracy, bo powiem tacie, ok!?"
if tutorials:
    show white_screen with dissolve
    show screen majorChoiceScale
#    show text "{color=#ffffff}During the game, your choices will affect a {size=+3}{size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size}{/size} score.\nGenerally, nice reactions will decrease your {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score and vice versa.\nThe {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score will affect how characters perceive you and unlock certain actions, events and even lewd scenes.{/color}" with dissolve:
    show text "{color=#ffffff}Podczas gry Twoje wybory będą miały wpływ na wynik {size=+3}{size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size}{/size}.\nOgólnie rzecz biorąc, miłe reakcje zmniejszą Twój wynik {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} i odwrotnie.\nWynik {size=+3}{color=#ffb052}{font=collegiate.ttf}dik{/font}{/color}{/size} wpłynie na to, jak postrzega Cię postać i odblokuje określone działania, wydarzenia, a nawet sprośne sceny.{/color}" with dissolve:
        ypos 0.83
    $ renpy.pause()
    hide text
#    show text "{color=#ffffff}Having a high or low {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score may also lock certain actions, events or lewd scenes.\nThe girls will respond differently to how you treat them and who you are based on the {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} score.\nThe score is updated at specific checkpoints during the game; you will be notified when this happens.{/color}" with dissolve:
    show text "{color=#ffffff}Wysoki lub niski wynik {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} może również zablokować pewne działania, wydarzenia lub sprośne sceny.\nDziewczyny będą reagować inaczej na to, jak je traktujesz i kim jesteś na podstawie wyniku {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}.\nWynik jest aktualizowany w określonych punktach kontrolnych podczas gry; otrzymasz powiadomienie, gdy tak się stanie.{/size}" with dissolve:
        ypos 0.83
    $ renpy.pause()
    hide text
    hide screen majorChoiceScale
    hide white_screen with dissolve
menu:
#    "Get mad":
    "Wścieknij się":
#        mc "(You fucking cunt...)"
        mc "Ty pieprzona cipo!"
        $ dk(1)
#    "Shrug it off":
    "Nie przejmuj się tym":
#        mc "(Typical Steve...)"
        mc "(Typowy Steve...)"
        $ dk(-1)
scene d0_intro8b with dissolve
#mc "(Josy...)"
mc "(Josy...)"
#mc "(I've been in love with her since I first saw her two months ago.)"
mc "(Zakochałem się w niej od pierwszego spotkania dwa miesiące temu.)"
#mc "(If it wasn't for her, I never would have stayed at this crappy summer job.)"
mc "(Gdyby nie ona, nigdy nie zostałbym w tej gównianej letniej pracy.)"
scene d0_intro8c with dissolve
#mc "(She's so beautiful...)"
mc "(Jest taka piękna...)"
#mc "(I could watch her smile all day long...)"
mc "(Mogłbym patrzeć, jak się uśmiecha przez cały dzień...)"
scene d0_intro9 with dissolve
#cl "Hey Josephine..."
st "Hej, Josephine..."
#cl "What are you doing later?"
st "Co robisz później?"
scene d0_intro10 with dissolve
#js "It's Josy..."
js "Jestem Josy..."
#js "...and that's none of your business, Steve."
js "...i to nie twoja sprawa, Steve."
scene d0_intro9 with dissolve
#st "Come on, Josephine. Don't be like that."
st "Daj spokój, Josephine. Nie bądź taka."
#st "I was thinking we could get together and maybe take a ride in my Ford Mustang."
st "Pomyślałem, że moglibyśmy się spotkać i może wybrać się na przejażdżkę moim Fordem Mustangiem."
menu:
#    "Think a bad thought":
    "Pomyśl o czymś złym":
        $ dk(1)
#        mc "(You mean your {b}dad's{/b} Ford Mustang...)"
        mc "(Masz na myśli Forda Mustanga swojego {b}ojca{/b}?)"
#    "Ignore it":
    "Nie zwracaj na to uwagi.":
        $ dk(-1)
#        mc "(Josy would never go for someone like Steve...)"
        mc "(Josy nigdy nie polubiłaby kogoś takiego jak Steve...)"
#        mc "(She's not that kind of a girl.)"
        mc "(Ona nie jest taką dziewczyną.)"
scene d0_intro10 with dissolve
#js "How many times do I have to turn you down before you take a hint?"
js "Ile razy muszę cię odrzucić, zanim zrozumiesz aluzję?"
#js "I'm not interested!"
js "nie jestem zainteresowana"
scene d0_intro9 with dissolve
#st "You're interested; you just don't know it yet."
st "Jesteś zainteresowana, tylko jeszcze o tym nie wiesz."
stop music fadeout 3
#st "Live a little, won't ya?"
st "Zacznij żyć, dobrze?"
scene d0_intro11 with vpunch
play sound "sound_effects/slap.mp3"
$ renpy.pause()
scene d0_intro12 with vpunch
play sound "sound_effects/slap.mp3"
#js "Fuck off!"
js "Odpierdol się! "
play music "music/ep1/golden_alley.mp3"
scene d0_lunchroom with fade
#mc "So, Josy..."
mc "Więc, Josy..."
#mc "I was wondering if you'd like to hang out sometime..."
mc "Zastanawiałem się, czy nie chciałabyś czasem gdzieś wyskoczyć..."
#mc "...maybe we could take a stroll along the river and get to know each other better?"
mc "...może moglibyśmy wybrać się na spacer wzdłuż rzeki i lepiej się poznać?"
scene d0_lunchroom1 with dissolve
#mc "Nah! Too corny."
mc "Nie! Zbyt banalne."
scene d0_lunchroom with dissolve
#mc "Hey, Josy!"
mc "Hej, Josy!"
#mc "Is that a new top?"
mc "Czy to nowa koszulka?"
#mc "You look radiant today!"
mc "Wyglądasz dziś olśniewająco!"
#mc "...was that better?"
mc "...tak lepiej?"
scene d0_lunchroom2 with dissolve
#mc "Hey, Josy!"
mc "Hej, Josy!"
#js "Hey, [name]."
js "Hej, [name]"
#mc "(!!!)"
mc "(!!!)"
scene d0_lunchroom4 with dissolve
#mc "Oh! Ah..."
mc "Och! Ach..."
#mc "Is that a new top?"
mc "Czy to nowa koszulka?"
scene d0_lunchroom5 with dissolve
#js "Erm...these are my work clothes."
js "Eee...to moje ubranie robocze."
scene d0_lunchroom6 with dissolve
#mc "I mean, you look like a radiator today."
mc "To znaczy, wyglądasz dzisiaj jak grzejnik."
#js "Like a what?"
js "Jak co?"
#mc "Shit...no, I mean..."
mc "Cholera...nie, to znaczy..."
scene d0_lunchroom9 with dissolve
#bs "Josephine?"
bs "Josephine"
#js "Yes, boss?"
js "Tak, szefie!"
#bs "Did you finish restocking the apple sauce in aisle 9?"
bs "Czy skończyłaś uzupełniać sos jabłkowy w alejce 9?"
#js "Steve told me he would do it."
js "Steve powiedział mi, że to zrobi."
#bs "*{i}Sigh{/i}*"
bs "*{i}Westchnienie{/i}*"
#bs "Fine."
bs "Dobrze."
scene d0_lunchroom9b with dissolve
#bs "Hm..."
bs "Hm..."
scene d0_lunchroom9c with dissolve
#bs "Why does this frame keep tilting?"
bs "Dlaczego ta rama ciągle się przechyla?"
scene d0_lunchroom9d with dissolve
#mc "*{i}Whispers{/i}* I know why."
mc "*{i}Szept{/i}* Wiem dlaczego."
scene d0_lunchroom9e with dissolve
#js "You do?"
js "Ty to robisz?"
scene d0_lunchroom9f with dissolve
#mc "Yeah. I use that picture to make Tina laugh when we have our lunch breaks together."
mc "Tak. Używam tego zdjęcia, aby rozśmieszyć Tinę, kiedy mamy razem przerwę na lunch."
scene d0_lunchroom9g with dissolve
#js "Ok, now you have to show me!"
js "Dobra, teraz musisz mi to pokazać!"
scene d0_lunchroom9j with dissolve
#mc "Hi! I'm Steve! When I'm not busy stocking the shelves in my dad's store, I'm postponing going to the barber."
mc "Cześć! Jestem Steve! Kiedy nie jestem zajęty uzupełnianiem zapasów w sklepie taty, odkładam wizytę u fryzjera."
#js "HAHA! That is SO funny!"
js "HAHA! To takie śmieszne!"
#mc "How about this one?"
mc "Co powiesz na to? "
menu:
#    "Nasty joke":
    "Paskudny żart":
        $ dk(1)
        $ RPjosy += 1
        scene d0_lunchroom9i with dissolve
#        mc "\nHey, Josephine! What's pink, brown, and fits like a glove?"
        mc "\n Hej, Josephine! Co jest różowe, brązowe i pasuje jak rękawiczka?"
#        js "\nHaha! No! That's enough!"
        js "\n Haha! Nie! Wystarczy!"
#    "Corny joke":
    "Banalny żart":
        $ dk(-1)
        scene d0_lunchroom9h with dissolve
#        mc "Hey, Josephine. I call you Josephine, because you-so-fine."
        mc "Hej, Josephine. Nazywam cię Josephine, bo jesteś taka dobra."
#        js "Oh my god! CRINGE!!!"
        js "O mój Boże! ŻENADA!!!"
scene d0_lunchroom9k with dissolve
#js "Haha, that was so good, [name]!"
js "Haha, to było takie dobre, [name]!"
#mc "Thanks! I'm glad you liked it."
mc "Cieszę się, że ci się podoba!"
scene d0_lunchroom9l with dissolve
#mc "Employee of the month...pff..."
mc "Pracownik miesiąca... pff..."
#js "He's such an ass..."
js "Ale z niego dupek..."
#mc "He looks like one, too."
mc "On też tak wygląda."
#js "Are you thinking what I'm thinking?"
js "Czy myślisz o tym samym, co ja?"
#mc "What?"
mc "Co?"
scene d0_lunchroom9m with dissolve
#mc "Oh, wow!"
mc "Och, wow! "
menu:
#    "Draw dicks":
    "Narysuj penisy":
#        $ bios_history_steve = "I drew dicks on Steve's employee of the month picture.\n\n"
        $ bios_history_steve = "Narysowałem kutasy na zdjęciu pracownika miesiąca Steve'a.\n\n"
        $ RPjosy += 1
        $ dk(2)
        $ stevePainting = 2
        scene d0_lunchroom9n with dissolve
#        mc "I'm not the best at drawing, but I think I can convey the message..."
        mc "Nie jestem najlepszy w rysowaniu, ale myślę, że mogę przekazać przesłanie..."
        scene d0_lunchroom9n2 with dissolve
#        mc "There!"
        mc "Tam!"
#        js "Hahaha! I meant you should draw a funny face or something..."
        js "Hahaha! Chodziło mi o to, że powinieneś narysować śmieszną twarz czy coś..."
#        mc "Oh..."
        mc "Och..."
#    "Draw a funny face":
    "Narysuj zabawną twarz":
#        $ bios_history_steve = "I drew a funny face on Steve's employee of the month picture.\n\n"
        $ bios_history_steve = "Narysowałem zabawną twarz na zdjęciu pracownika miesiąca Steve'a.\n\n"
        $ RPjosy += 1
        $ dk(1)
        $ stevePainting = 1
        scene d0_lunchroom9n with dissolve
#        mc "It will be hard to make this picture uglier, but I can try."
        mc "Ciężko będzie sprawić, że ten obraz będzie brzydszy, ale mogę spróbować."
        scene d0_lunchroom9n3 with dissolve
#        js "That's perfect! That's just what I see when I look at him."
        js "Doskonale! Właśnie to widzę, kiedy na niego patrzę."
#        mc "Yeah, I think I nailed it."
        mc "Tak, chyba mi się udało."
#    "Don't draw":
    "Nie rysuj":
#        $ bios_history_steve = "I resisted the urge to draw something on Steve's employee of the month picture.\n\n"
        $ bios_history_steve = "Oparłem się chęci narysowania czegoś na zdjęciu pracownika miesiąca Steve'a.\n\n"
        $ dk(-2)
        $ stevePainting = 0
        scene d0_lunchroom9l with dissolve
#        mc "Sorry... I don't think it's a good idea."
        mc "Przepraszam... Myślę, że to nie jest dobry pomysł."
#        js "Fine, I just thought it would be fun."
        js "Dobra, po prostu pomyślałam, że będzie fajnie."
scene d0_lunchroom14 with fade
#js "Whatcha reading?"
js "Co czytasz?"
scene d0_lunchroom15 with dissolve
#mc "Oh, this?"
mc "Oh, to?"
#mc "It's just a pamphlet...for college."
mc "To tylko broszura... na studia."
scene d0_lunchroom16 with dissolve
#js "Oh! Burgmeister & Royce!"
js "Oh! Burgmeister i Royce!"
#js "Did you apply too?"
js "Ty też aplikowałeś?"
scene d0_lunchroom17 with dissolve
#mc "Yeah, I did."
mc "Tak, zrobiłem."
#mc "But I don't think I got accepted..."
mc "Ale chyba mnie nie przyjęli..."
#mc "Everyone I know already got their letter of acceptance in the mail."
mc "Wszyscy, których znam, otrzymali już list akceptacyjny pocztą."
#mc "Right now, I'm just waiting for something to happen, I guess."
mc "W tej chwili po prostu czekam, aż coś się wydarzy, tak myślę."
scene d0_lunchroom17b with dissolve
#js "I know that feeling. I got put on the waiting list."
js "Znam to uczucie. Wpisali mnie na listę oczekujących."
#js "It sucks because I really wanna go!"
js "Jest do bani, bo naprawdę chcę iść!"
#js "I know people who go there already, and even my moron stepbrother got accepted!"
js "Znam ludzi, którzy już tam chodzą, a nawet mój debilny przyrodni brat został przyjęty!"
scene d0_lunchroom18 with dissolve
#mc "Maybe people will drop off and a spot opens up for you?"
mc "Może ludzie odpadną i zwolni się dla Ciebie miejsce?"
scene d0_lunchroom17b with dissolve
#js "I'm number 14 in line..."
js "Jestem numerem 14 w kolejce..."
scene d0_lunchroom18 with dissolve
#mc "That sucks... It must be a popular degree."
mc "Do bani... To musi być popularny kierunek studiów."
scene d0_lunchroom20 with dissolve
#js "Yeah, it's for a business degree. My dad really wanted me to go, since he went there too."
js "Tak, to na studia biznesowe. Tata bardzo chciał, żebym tam studiowała, bo on też tam studiował."
scene d0_lunchroom17c with dissolve
#js "He was so happy when my stepbrother got accepted."
js "Był taki szczęśliwy, kiedy mój przyrodni brat został przyjęty."
#js "And he's not going there to study..."
js "I nie zamierza tam studiować..."
#js "He's just there for the frat life and parties."
js "Jest tam tylko dla życia bractwa i imprez."
#js "I'm pretty sure that he cheated his way through high school..."
js "Jestem prawie pewna, że oszukiwał przez całe liceum..."
scene d0_lunchroom20 with dissolve
#js "What about you?"
js "A ty?"
scene d0_lunchroom17 with dissolve
#mc "I guess I'm going for a little bit of both."
mc "Myślę, że wybieram jedno i drugie."
#mc "I don't really know what I want to be...but science is pretty cool, so I think I'm going for a bachelor's degree."
mc "Naprawdę nie wiem, kim chcę być...ale nauka jest całkiem fajna, więc myślę, że pójdę na studia licencjackie."
scene d0_lunchroom24 with dissolve
#js "You think?"
js "Tak myślisz? "
scene d0_lunchroom17 with dissolve
#mc "Well...I haven't really figured it out yet, but I will eventually."
mc "Cóż... tak naprawdę jeszcze tego nie rozgryzłem, ale w końcu to zrobię."
#mc "In the first couple of years, the classes are more or less the same for most students, with the general education classes and all."
mc "W ciągu pierwszych kilku lat zajęcia są mniej więcej takie same dla większości studentów, obejmują przedmioty ogólnokształcące i inne."
#mc "It probably doesn't matter, though..."
mc "Ale to nie ma znaczenia. "
#mc "With my luck, I'll have to stay at this place until I retire."
mc "Przy odrobinie szczęścia będę musiał zostać w tym miejscu do emerytury."
scene d0_lunchroom42 with dissolve
#js "That makes two of us, then."
js "No to jest nas dwoje. "
#js "Hey..."
js "Hej..."
#js "When do you quit work today?"
js "Kiedy dzisiaj kończysz pracę?"
scene d0_lunchroom17 with dissolve
#mc "At 4 p.m."
mc "O 16:00."
scene d0_lunchroom42c with dissolve
#js "Sweet! Me too!"
js "Słodko! Ja też!"
#js "My dad was going to pick me up but he texted me saying he has to work overtime."
js "Mój tata miał mnie odebrać, ale napisał do mnie, że musi pracować w nadgodzinach."
#js "He has some big client meeting or something..."
js "Ma jakieś ważne spotkanie z klientem czy coś..."
#js "Can you give me a ride home?"
js "Podwieziesz mnie do domu?"
scene d0_lunchroom24b with dissolve
#mc "Sure...but I ride a bike."
mc "Jasne...ale jeżdżę jednośladem."
scene d0_lunchroom42 with dissolve
#js "Oh, that will be awesome!"
js "Och, to będzie niesamowite!"
scene d0_lunchroom42c with dissolve
stop music fadeout 3
#js "My break is over."
js "Moja przerwa się skończyła."
#js "Talk to you later, [name]."
js "Później porozmawiamy. "
play music "music/ep1/never_give_up.mp3"
scene d0_goinghome with Fade(1.5, 1, 0.5)
#js "There you are!"
js "Tu jesteś!"
#js "I've been waiting for you."
js "…czekałam na ciebie. "
scene d0_goinghome1 with dissolve
#mc "Sorry for being late."
mc "Przepraszam za spóźnienie."
#mc "Steve forced me to clean the grill."
mc "Steve zmusił mnie do wyczyszczenia grilla."
scene d0_goinghome with dissolve
#js "No problemo."
js "No trudno."
#js "Where's your ride?"
js "Gdzie masz transport?"
scene d0_goinghome3 with dissolve
#mc "You're standing next to it."
mc "Stoisz obok niego."
scene d0_goinghome4 with dissolve
#js "Hahaha!"
js "Hahaha!"
#mc "What's wrong?"
mc "Co jest?"
scene d0_goinghome6 with dissolve
#js "Sorry, [name]!"
js "Przepraszam, [name]!"
#js "When you said bike, I thought you meant a motorcycle."
js "Kiedy powiedziałeś jednoślad, myślałam, że masz na myśli motocykl."
scene d0_goinghome7 with dissolve
#mc "Oh..."
mc "Och..."
#mc "Well, this is what I ride."
mc "Cóż, to jest to, na czym jeżdżę."
scene d0_goinghome7b with dissolve
#js "Well, hop on and give me a lift, then."
js "No to wskakuj i mnie podwieź."
scene d0_goinghome9 with dissolve
#mc "Are you ready?"
mc "Gotowa?"
scene d0_goinghome10 with dissolve
#js "Yeah. Don't do a wheelie now."
js "Tak. Nie jedź tylko na jednym kole."
#mc "Don't worry; I won't."
mc "Nie martw się, nie zrobię tego."
scene d0_goinghome12 with dissolve
#js "Ok, that was a joke, but sure."
js "Dobra, to był żart, ale jasne."
scene d0_goinghome12a with dissolve
$ renpy.pause()
scene d0_goinghome12b with fade
#mc "(The way she's holding her arms around me...)"
mc "(Sposób, w jaki mnie obejmuje...)"
#mc "(...it feels like the warmest hug.)"
mc "(...wydaje się, że to najcieplejszy uścisk.)"
scene d0_goinghome13 with dissolve
#mc "(She smells so good.)"
mc "(Ładnie pachnie.)"
#mc "(Just like strawberries.)"
mc "(Tak jak truskawki.)"
#mc "Are you comfortable back there?"
mc "Jest ci wygodnie z tyłu?"
scene d0_goinghome16 with dissolve
#js "Yes, I'm fine, thanks."
js "Czuję się dobrze, dzięki."
#js "We can switch if it's too tiresome for you."
js "Możemy się zamienić, jeśli jest to dla Ciebie zbyt męczące."
scene d0_goinghome13 with dissolve
#mc "No, I'm good."
mc "Nie, nie trzeba. "
scene d0_goinghome17b with dissolve
#js "I bet you give chicks rides home all the time on this thing."
js "Założę się, że cały czas podwozisz laski do domu."
scene d0_goinghome17 with dissolve
#mc "No, not really."
mc "Nie, nie bardzo."
scene d0_goinghome17b with dissolve
#js "So, [name]. We haven't really talked much to each other before."
js "Więc, [name]. Tak naprawdę nie rozmawialiśmy ze sobą zbyt wiele wcześniej."
#js "Besides work stuff, I mean."
js "Poza sprawami związanymi z pracą."
scene d0_goinghome17 with dissolve
#mc "Yeah, I've meant to talk more to you but never found the right opportunity for it."
mc "Tak, chciałem z Tobą porozmawiać, ale nigdy nie znalazłem na to odpowiedniej okazji."
scene d0_goinghome17b with dissolve
#js "What are you saying? We've been working together for almost two months now!"
js "Co chcesz przez to powiedzieć? Pracujemy razem już prawie dwa miesiące!"
#js "Are you a shy guy or something?"
js "Jesteś nieśmiały, czy co?"
scene d0_goinghome17 with dissolve
#mc "No, not really. But you're always talking to others at work."
mc "Nie, nie do końca. Ale zawsze rozmawiasz z innymi w pracy."
#mc "I don't want to interrupt..."
mc "Nie chcę przeszkadzać..."
#mc "...besides, I generally like to listen more than I like to talk."
mc "…poza tym generalnie bardziej lubię słuchać niż rozmawiać."
$ guideSuggestedPage = 28
scene d0_goinghome18 with dissolve
#js "Haha, yeah, I tend to talk a lot."
js "Haha, tak, często mówię."
#js "Some people find it annoying."
js "Niektórzy ludzie uważają to za irytujące."
scene d0_goinghome17 with dissolve
menu:
#    "I don't mind it":
    "Nie przeszkadza mi.":
#        mc "I don't mind it. Talk all you want."
        mc "Nie przeszkadza mi to. Mów, co chcesz."
#    "I really like it":
    "Bardzo mi się to podoba.":
        $ RPjosy += 1
#        mc "Well, I really like that about you."
        mc "Cóż, naprawdę mi się to w tobie podoba."
#        mc "You're very easy-going; I guess that's why people are drawn to you."
        mc "Jesteś bardzo wyluzowana. Myślę, że dlatego przyciągasz ludzi."
        scene d0_goinghome20 with dissolve
#        js "(He's really sweet.)"
        js "(Jest naprawdę słodki.)"
        scene d0_goinghome17b with dissolve
#        js "Thanks."
        js "Dziękuję."
scene d0_goinghome26 with fade
#js "This is me."
js "To mój."
#mc "Ok."
mc "Ok."
scene d0_goinghome27 with dissolve
#js "So...thanks for the ride, [name]."
js "Więc...dzięki za podwiezienie, [name]."
scene d0_goinghome28 with dissolve
#mc "You're welcome."
mc "Nie ma sprawy."
#js "..."
js "..."
#mc "..."
mc "..."
#mc "So..."
mc "Więc..."
#mc "See you tomorrow?"
mc "Widzimy się jutro?"
scene d0_goinghome29 with dissolve
#js "All right..."
js "Jasne."
#js "Bye."
js "Pa."
stop music fadeout 5
scene d0_goinghome30 with dissolve
menu:
#    "Check out her ass":
    "Obczaj jej tyłek":
        $ dk(1)
        scene d0_goinghome31 with dissolve
        $ renpy.pause()
#    "Check out her boobs":
    "Zobacz jej cycki":
        $ dk(1)
        scene d0_goinghome32 with dissolve
        $ renpy.pause()
#    "Leave":
    "Opuść":
        $ dk(-1)
scene d0_goinghome33 with dissolve
play music "music/patched/track_previous.mp3"
#mc "(...)"
mc "(...)"
#mc "(Oh no...)"
mc "Och, nie..."
#mc "(Was that a cue for me to kiss her?)"
mc "(Czy to była wskazówka, żebym ją pocałował?)"
#mc "(I'm such a loser!)"
mc "Jestem nieudacznikiem. "
scene dik_title
$ renpy.pause(8)
show title_ol with dissolve
$ renpy.pause()
hide title_ol with dissolve
stop music fadeout 7
scene black with dissolve
show screen ep6_title_screen
$ renpy.pause(5)
scene d0_home with fade
#mc "Dad! I'm home."
mc "Tato! Jestem w domu."
scene d0_home1 with dissolve
play music "music/ep1/golden_alley.mp3"
#dad "Hey, son."
dad "Cześć, synu."
#dad "You're home later than usual."
dad "Jesteś w domu później niż zwykle."
scene d0_home2b with dissolve
#mc "Yeah, I was giving Josy a ride home on my bike."
mc "Tak, odwoziłem Josy do domu rowerem."
scene d0_home2 with dissolve
#dad "I didn't realize I raised such a charmer."
dad "Nie zdawałam sobie sprawy, że wychowałam takiego czarusia."
scene d0_home2b with dissolve
menu:
#    "Get annoyed":
    "Daj się zirytować":
        $ dk(1)
#        mc "Stop it, dad..."
        mc "Przestań, tato..."
#    "Humor him":
    "Rozbaw go":
        $ dk(-1)
#        mc "The apple doesn't fall far from the tree."
        mc "Niedaleko pada jabłko od jabłoni."
scene d0_home3 with dissolve
#dad "I'm proud of you, son, and I know your mother would have been, too."
dad "Jestem z ciebie dumny, synu, i wiem, że twoja matka też byłaby dumna."
scene d0_home3b with dissolve
#mc "Thanks, dad."
mc "Dzięki, Tato. "
scene d0_home5 with dissolve
#mc "What's this?"
mc "Co to?"
#dad "Open it."
dad "Otwórz."
scene d0_home6 with dissolve
#mc "Dear [name]...your application was..."
mc "Szanowny Pan [name]...Pana wniosek był..."
#mc "...you are hereby accepted..."
mc "... niniejszym przyjmujemy..."
#mc "I GOT IN!"
mc "Dostałam się!"
scene d0_home7 with dissolve
#dad "You did!?"
dad "Naprawdę!?"
#mc "Dad, I got accepted to college!!!"
mc "Tato, dostałam się na studia!!!"
scene d0_home9 with dissolve
#dad "This calls for a celebration!"
dad "Czas na świętowanie!"
scene d0_home10 with dissolve
#dad "My son...a college freshman."
dad "Mój syn...student pierwszego roku."
#dad "How does that feel?"
dad "Jak się czujesz? "
#mc "It's just unimaginable!"
mc "To po prostu niewyobrażalne!"
scene d0_home12 with dissolve
#dad "Son, I want you to take the jar from the closet."
dad "Synu, chcę, żebyś wyjął słoik z szafy."
#dad "It's yours."
dad "Jest cały Twój."
scene d0_home13 with dissolve
#mc "No, dad. That's not my money."
mc "Nie, tato. To nie moje pieniądze."
scene d0_home14 with dissolve
#dad "Stop it! I know that I can't afford to pay for your tuition, but at least let me help you with as much as I can."
dad "Przestań! Wiem, że nie stać mnie na opłacenie twojego czesnego, ale przynajmniej pozwól, że pomogę ci w jak największym stopniu."
show screen moneymsg
if tutorials:
    show white_screen with dissolve
#    show text "{color=#ffffff}This game uses a simplistic money system.\nYou can carry up to five ({color=#36ca2b}$$$$${/color}) money tokens; this is your pocket money.{/color}" with dissolve:
    show text "{color=#ffffff}Ta gra wykorzystuje uproszczony system pieniężny.\nMożesz nosić do pięciu ({color=#36ca2b}$ $$$${/color}) żetonów pieniężnych; to są Twoje kieszonkowe.{/color}" with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
#    show text "{color=#ffffff}Money is used to purchase items on special occasions and useful during certain events.\nMoney can be earned through various actions during the game. Spend your pocket money wisely.{/color}" with dissolve:
    show text "{color=#ffffff}Pieniądze są wykorzystywane do zakupu przedmiotów na specjalne okazje i są przydatne podczas niektórych wydarzeń.\nPieniądze można zarobić poprzez różne akcje podczas gry. Mądrze wydawaj kieszonkowe.{/color}" with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
scene d0_home13 with dissolve
$ money = 0
$ earnedMoney = 0
$ spentMoney = 0
menu:
#    "Accept money":
    "Akceptuj pieniądze":
#        $ bios_history_dad = "Dad gave me money from his personal savings.\n\n"
        $ bios_history_dad = "Tata dał mi pieniądze ze swoich oszczędności.\n\n"
        $ acceptedMoneyFromDad = True
        $ mny(1)
#        "{i}Received {color=#36ca2b}${/color}{/i}"
        "{i}Odebrano {color=#36ca2b}${/color}{/i}"
#        mc "Thank you, dad!"
        mc "Dziękuję, tato!"
#        mc "I love you."
        mc "Kocham cię."
        hide screen moneymsg
        scene d0_home16 with dissolve
#        dad "I love you too, son."
        dad "Ja też Cię kocham."
        scene d0_home13 with dissolve
#    "Ask for more money":
    "Poproś o więcej pieniędzy":
#        $ bios_history_dad = "Dad gave me money from his personal savings and I even got some more when I asked him.\n\n"
        $ bios_history_dad = "Tata dał mi pieniądze ze swoich oszczędności, a ja dostałam nawet więcej, kiedy go o to poprosiłam.\n\n"
        $ dk(1)
        $ acceptedMoneyFromDad = True
#        mc "Didn't you get your paycheck today?"
        mc "Nie dostałeś dzisiaj wypłaty?"
        scene d0_home16b with dissolve
#        dad "Oh, yeah. I did..."
        dad "Oh, jasne, dostałem..."
#        dad "I think I can throw in a little bit extra for you."
        dad "Myślę, że mogę dorzucić trochę więcej."
        $ mny(2)
#        "{i}Received {color=#36ca2b}$${/color}{/i}"
        "{i}Odebrano {color=#36ca2b}$${/color}{/i}"
        scene d0_home16 with dissolve
#        dad "I love you, son."
        dad "Kocham cię, mój synu"
        scene d0_home13 with dissolve
        hide screen moneymsg
#    "Reject money":
    "Odrzuć pieniądze":
#        $ bios_history_dad = "Dad tried to give me money from his personal savings, but that's his money, he earned that.\n\n"
        $ bios_history_dad = "Tata próbował dać mi pieniądze ze swoich osobistych oszczędności, ale to są jego pieniądze, zarobił je.\n\n"
        $ dk(-1)
        $ acceptedMoneyFromDad = False
#        mc "I'm sorry, dad, but no."
        mc "Przykro mi, tato, ale nie."
        hide screen moneymsg
#        mc "I can't accept this. I'll take a student loan and will find a way to earn some extra pocket money."
        mc "Nie mogę tego przyjąć. Wezmę pożyczkę studencką i znajdę sposób, aby zarobić trochę dodatkowych pieniędzy."
        scene d0_home16 with dissolve
#        dad "I love you, son."
        dad "Kocham cię, mój synu"
#        dad "You make me so proud."
        dad "Sprawiasz, że jestem taki dumny."
        scene d0_home13 with dissolve
#        mc "I love you too, dad."
        mc "Ja też Cię kocham."
$ bios_name_dad = True
#mc "It will feel great to tell my boss I'm quitting tomorrow."
mc "Fajnie będzie powiedzieć szefowi, że jutro odchodzę."
scene d0_home12 with dissolve
#dad "I bet he will miss having you as an employee, son."
dad "Założę się, że będzie mu cię brakowało jako pracownika, synu."
stop music
$ guideSuggestedPage = 29
scene d0_boss2
#bs "Great! That saves me the trouble of firing you."
bs "Świetnie! To oszczędza mi kłopotu zwalniania cię."
scene d0_boss2b with dissolve
#mc "Oh..."
mc "Och..."
play music "music/ep1/someways.mp3"
scene d0_boss3 with dissolve
#bs "College, huh?"
bs "Studia, co?"
scene d0_boss3b with dissolve
#mc "Yeah, I start on Monday."
mc "Tak, zaczynam w poniedziałek."
scene d0_boss with dissolve
#bs "What!? Already? You're supposed to give me two weeks' notice."
bs "Co!? Już? Miałeś mi dać dwutygodniowe wypowiedzenie."
scene d0_bossb with dissolve
#mc "Yeah...I know. But I didn't think I would be accepted and I got the letter of acceptance yesterday."
mc "Tak...Wiem, ale nie sądziłem, że zostanę przyjęty i wczoraj dostałem list akceptacyjny."
scene d0_boss with dissolve
#bs "Mhm..."
bs "..."
scene d0_bossb with dissolve
#mc "So, what about my pay slip?"
mc "A co z moim odcinkiem wypłaty?"
scene d0_boss with dissolve
#bs "Well, the way I see it..."
bs "Z mojej perspektywy wydaje mi się,"
#bs "I think it's only fair that you get less than agreed upon."
bs "Myślę, że to sprawiedliwe, że dostajesz mniej niż uzgodniono."
scene d0_bossb with dissolve
menu:
#    "Push him for more":
    "Poproś go o więcej":
        $ dk(1)
#        mc "That's not fair at all. I'm pretty sure it's illegal, too."
        mc "To w ogóle niesprawiedliwe. Jestem prawie pewien, że to też nielegalne."
        scene d0_boss with dissolve
        if stevePainting > 0:
#            bs "Vandalizing company property is also illegal, buddy. I saw what you did to Steve's photo on the security cam."
            bs "Wandalizacja mienia firmy jest również nielegalna, kolego. Widziałem, co zrobiłeś ze zdjęciem Steve'a na kamerze bezpieczeństwa."
#            bs "You know what? I changed my mind. I'm keeping your pay as compensation for the damages."
            bs "Wiesz co, zmieniłem zdanie. Zatrzymuję Twoją wypłatę jako rekompensatę za szkody."
        else:
#            bs "Fine, I'll meet you halfway. That's me being generous, ok?"
            bs "Dobra, spotkamy się w połowie drogi. To moja szczodrość, ok?"
            $ mny(2)
            show screen moneymsg
#            "{i}Received {color=#36ca2b}$${/color}{/i}"
            "{i}Odebrano {color=#36ca2b}$${/color}{/i}"
            hide screen moneymsg
#    "Accept less":
    "Akceptuj mniej":
        $ dk(-1)
        show screen moneymsg
#        mc "Ok, that's fair."
        mc "Ok, to uczciwe."
        $ mny(1)
        scene d0_boss with dissolve
#        "{i}Received {color=#36ca2b}${/color}{/i}"
        "{i}Odebrano {color=#36ca2b}${/color}{/i}"
#        bs "That's only because I'm generous. Make sure you remember that."
        bs "To tylko dlatego, że jestem hojny. Pamiętaj o tym."
        hide screen moneymsg
stop music fadeout 3
#bs "Wash your clothes and return them to me by the end of the week."
bs "Wypierz swoje ubrania i zwróć mi je do końca tygodnia."
play music "music/ep1/winter_sunshine.mp3"
scene d0_js with wipeleft
#mc "Hi, Josy."
mc "Cześć, Josy."
#js "Hey, [name]!"
js "Hej, [name]!"
#js "Everything good?"
js "Wszystko ok?"
scene d0_js2 with dissolve
#mc "It's better than good, actually."
mc "Właściwie to lepiej niż dobrze."
#mc "I got my letter of acceptance yesterday!"
mc "Wczoraj otrzymałem list akceptacyjny!"
scene d0_js3 with dissolve
#js "You did!? Wow, that's awesome!"
js "Tak!? Wow, to niesamowite!"
scene d0_js3b with dissolve
#js "Congratulations!!!"
js "Gratulacje!"
#js "I'm so jealous!"
js "Jestem taka zazdrosna!"
scene d0_js4 with dissolve
#js "So, you're leaving me here, huh?"
js "Więc zostawiasz mnie tutaj, co?"
scene d0_js4b with dissolve
menu:
#    "Yes, sorry":
    "Tak, przepraszam.":
#        mc "Yeah... I'm sorry for that..."
        mc "Tak... Przepraszam za to..."
        scene d0_js6 with dissolve
#        js "Hey, don't feel sorry for me."
        js "Hej, nie współczuj mi."
#        js "I only need 13 people to decline, and I'm golden."
        js "Wystarczy, że 13 osób odmówi i się dostanę."
        scene d0_js4b with dissolve
#        mc "Haha! I'm glad that you're staying positive."
        mc "Haha! Cieszę się, że masz pozytywne nastawienie."
        scene d0_js6b with dissolve
#    "I can stay if you want":
    "Mogę zostać, jeśli chcesz":
#        mc "I can stay if you want..."
        mc "Mogę zostać, jeśli chcesz..."
        scene d0_js7 with dissolve
#        js "Are you crazy? You got in!"
        js "Oszalałeś? Dostałeś się!"
#        js "Go chase your dream!"
        js "Idź gonić swoje marzenia!"
        scene d0_js6b with dissolve
#js "But I will miss you."
js "Będzie mi Cię brakowało."
if dtype < 0:
    scene d0_js8 with dissolve
#    "*{i}Smack{/i}*"
    "*{i}Cmoknięcie{/i}*"
scene d0_js9 with dissolve
#mc "I'll come back and visit once in a while, you know."
mc "Wpadnę cię odwiedzić raz na jakiś czas, wiesz."
#mc "I mean, it's not far from here, and my dad still lives here."
mc "To znaczy, to niedaleko stąd, a mój tata nadal tu mieszka."
scene d0_js10 with dissolve
#js "I'd love that..."
js "Z przyjemnością! "
#js "When are you leaving?"
js "Kiedy wyjeżdżasz?"
scene d0_js9 with dissolve
#mc "I start on Monday."
mc "Zaczynam w poniedziałek."
scene d0_js10 with dissolve
#js "No way! This Monday?"
js "Co!? W ten poniedziałek?"
scene d0_js9 with dissolve
#mc "Yeah, afraid so."
mc "Obawiam się, że tak."
scene d0_js12b with dissolve
#js "Hey, I know!"
js "Hej, wiem!"
#js "We should do something fun this weekend!"
js "Powinniśmy zrobić coś fajnego w ten weekend!"
#js "You know, to celebrate!"
js "Wiesz, żeby to uczcić!"
scene d0_js13 with dissolve
#mc "Well, all right. What do you have in mind?"
mc "No dobra. Co masz na myśli?"
scene d0_js10 with dissolve
#js "Pick me up tomorrow night on that {i}sweet ride{/i} of yours, and I'll show you!"
js "Przyjdź po mnie jutro wieczorem na tę swoją {i}słodką przejażdżkę{/i}, a ja Ci pokażę!"
scene d0_js9 with dissolve
menu:
#    "Ok":
    "OK":
#        mc "Ok. I will."
        mc "OK, będę."
#    "It's a date!":
    "To jest randka!":
        $ RPjosy += 1
#        mc "It's a date!"
        mc "To jest randka!"
        scene d0_js16 with dissolve
#        js "Haha..."
        js "Haha"
stop music fadeout 3
scene d0_js17 with dissolve
#st "Back to work, Josy."
st "Wracaj do pracy, Josy."
play music "music/ep1/roadtrip.mp3"
if stevePainting >0:
    scene d0_js17b with dissolve
#    st "So, you think you're pretty funny, huh?"
    st "Myślisz, że jesteś zabawny, co?"
    scene d0_js17c with dissolve
    menu:
#        "Trigger him":
        "Sprowokuj go":
            $ dk(1)
#            mc "I've been known to tell a joke or two."
            mc "Jestem znany z tego, że opowiadam dowcipy."
#            mc "Knock knock."
            mc "Puk, puk."
            scene d0_js17d with dissolve
#            st "Fuck you!"
            st "Pierdol się!"
            scene d0_js17c with dissolve
#            mc "You're supposed to say \"Who's there?\", Steve. Didn't your imaginary friends teach you that one?"
            mc "Powinieneś powiedzieć \"Kto tam?\", Steve. Czy twoi wymyśleni przyjaciele cię tego nie nauczyli?"
#        "What do you mean?":
        "O co ci chodzi?":
            $ dk(-1)
#            mc "What do you mean?"
            mc "O co ci chodzi?"
    scene d0_js17d2 with dissolve
    if stevePainting == 2:
#        st "Drawing dicks on my face is not funny, you asshole!"
        st "Rysowanie kutasów na mojej twarzy nie jest śmieszne, dupku!"
        scene d0_js17c with dissolve
#        mc "I strongly disagree."
        mc "Zdecydowanie się nie zgadzam"
        scene d0_js17d2 with dissolve
    else:
#        st "Why the fuck did you draw on my picture!?"
        st "Dlaczego, do kurwy nędzy, rysowałeś na moim zdjęciu!?"
#    st "I earned that award!"
    st "Zasłużyłem na tę nagrodę!"
    scene d0_js18 with dissolve
#    st "Dad just told me that you're quitting."
    st "Tata właśnie mi powiedział, że odchodzisz."
#    st "Thank fuck for that. I knew this job was too hard for you."
    st "Dzięki kurwa za to. Wiedziałem, że ta praca jest dla ciebie za trudna."
    scene d0_js19 with dissolve
#    mc "Not really. I can't work here and go to B&R."
    mc "Niezupełnie. Nie mogę tu pracować i chodzić do B&R."
else:
    scene d0_js18 with dissolve
#    st "Dad just told me that you're quitting."
    st "Tata właśnie mi powiedział, że odchodzisz."
#    st "That was the best news I've heard in a long time."
    st "To była najlepsza wiadomość, jaką słyszałem od dłuższego czasu."
    scene d0_js19 with dissolve
#    mc "Well, I can't work here and go to B&R."
    mc "Cóż, nie mogę tu pracować i chodzić do B&R."
scene d0_js18 with dissolve
#st "*{i}Snorts{/i}* B&R, the poor man's college."
st "*{i}Prycha{/i}* B&R, uczelnia biedaka."
scene d0_js19 with dissolve
#mc "What are you talking about? It's not a bad college."
mc "O czym ty mówisz? To nie jest zła uczelnia."
scene d0_js18 with dissolve
#st "Aside from that preppy, silver spoon in their asses frat house..."
st "Oprócz tego eleganckiego, bogatego bractwa studenckiego..."
#st "...yeah, people who go there are trash."
st "...tak, ludzie, którzy tam chodzą, są śmieciami."
scene d0_js19 with dissolve
menu:
#    "Retort":
    "Stanowcza odpowiedź":
        $ dk(1)
#        mc "You're one to talk!"
        mc "Jesteś jednym z tych, którzy mówią!"
#        mc "If it wasn't for your dad, you and your 50's haircut would be picking up litter in the park for a living."
        mc "Gdyby nie twój tata, ty i twoja fryzura po pięćdziesiątce zarabialibyście na życie zbierając śmieci w parku."
        scene d0_js17d2 with dissolve
#        st "Watch your mouth!"
        st "Uważaj, co mówisz!"
        scene d0_js19 with dissolve
#        mc "Or what? Will you have your dad fire me?"
        mc "Albo co? Czy twój tata mnie zwolni?"
#        mc "Oh, wait... That's right, I already quit."
        mc "A, czekaj... No tak, już zrezygnowałam."
        scene d0_js22b with dissolve
#        st "I'll be the owner of this place one day, you know!"
        st "Pewnego dnia będę właścicielem tego miejsca, wiesz!"
        stop music fadeout 10
#        st "Remember that when you come crawling back."
        st "Pamiętaj o tym, gdy wrócisz czołgając się z powrotem."
        scene d0_js22c with dissolve
#        mc "Good luck with the family business, Steve. Call me when you do something without daddy's help."
        mc "Powodzenia w rodzinnym biznesie, Steve. Zadzwoń do mnie, kiedy zrobisz coś bez pomocy tatusia."
#    "Ignore him":
    "Ignoruj go.":
        $ dk(-1)
#        mc "Whatever, Steve. Enjoy working here."
        mc "Nieważne, Steve. Ciesz się pracą tutaj."
        scene d0_js22b with dissolve
        stop music fadeout 10
#        st "I'll be the owner of this place one day, you know!"
        st "Pewnego dnia będę właścicielem tego miejsca, wiesz!"
#        st "Remember that when you come crawling back."
        st "Pamiętaj o tym, gdy wrócisz czołgając się z powrotem."
#$ bios_history_steve += "Steve tried to pick a fight with me when he heard that I was quitting my job.\n\n"
$ bios_history_steve += "Steve próbował się ze mną kłócić, gdy usłyszał, że odchodzę z pracy.\n \n"
play music "music/ep1/food_chain_short.mp3"
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight1 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
scene d0_fight2 with dissolve
#dad "Great! Don't stop now!"
dad "Świetnie! Teraz nie przestawaj!"
#dad "High kick!"
dad "Wysokie kopnięcie!"
play sound "sound_effects/hit.mp3"
scene d0_fight3 with vpunch
$ renpy.pause(0.5)
#dad "Perfect!"
dad "Idealnie!"
scene d0_fight2 with dissolve
#dad "Flurry!"
dad "Nawałnica"
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight1 with vpunch
$ renpy.pause(0.5)
play sound "sound_effects/hit.mp3"
scene d0_fight0 with vpunch
$ renpy.pause(0.5)
scene d0_fight3b with dissolve
stop music fadeout 10
#dad "Great, son! That will do for today."
dad "Świetnie, synu! To wystarczy na dzisiaj."
scene d0_fight4 with dissolve
#dad "So, how did it go with your boss?"
dad "Jak poszło z szefem?"
scene d0_fight5 with dissolve
play music "music/ep1/never_give_up.mp3"
#mc "It went ok. It could've gone better, but I'm done with that place now."
mc "Poszło dobrze. Mogło pójść lepiej, ale skończyłem z tym miejscem."
scene d0_fight5b with dissolve
#dad "The next step in your life is a big one, son."
dad "Następny krok w twoim życiu jest duży, synu."
#dad "As I never went to college, I can't imagine how exciting this must feel for you."
dad "Ponieważ nigdy nie poszłam na studia, nie wyobrażam sobie, jakie to musi być dla ciebie ekscytujące."
scene d0_fight6 with dissolve
#mc "Yeah..."
mc "Tak"
#dad "Something the matter?"
dad "Coś się stało?"
scene d0_fight8 with dissolve
#mc "Well, there's this girl...Josy."
mc "No jest taka dziewczyna... Josy."
#mc "I have a crush on her, and now I'm moving away from here."
mc "Zakochałem się w niej, a teraz się stąd wyprowadzam."
#mc "I feel pretty bad about it."
mc "Czuję się z tym bardzo źle."
scene d0_fight9 with dissolve
#dad "Uh-huh. I see."
dad "Mhm. Rozumiem."
#dad "Let me tell you something I've learned."
dad "Powiem ci coś, czego się nauczyłem."
scene d0_fight10 with dissolve
#dad "As you know, I already worked in construction when I met your mom."
dad "Jak wiesz, pracowałam już na budowie, kiedy poznałam twoją mamę."
#dad "Her dad, who was filthy rich, hired me to help him build a hotel."
dad "Jej ojciec, który był obrzydliwie bogaty, zatrudnił mnie, żebym pomógł mu zbudować hotel."
scene d0_fight11 with fade
#dad "Your mom was a very beautiful woman. I was 24, and she had just turned 18."
dad "Twoja mama była bardzo piękną kobietą. Miałem 24 lata, a ona właśnie skończyła 18."
#dad "Her dad disapproved of me being with his daughter. In his eyes, I was of a lower class."
dad "Jej tata nie pochwalał tego, że jestem z jego córką. W jego oczach należałem do niższej klasy."
scene d0_fight12 with dissolve
#dad "Your mother didn't see it that way. She looked past all that, and we fell in love."
dad "Twoja mama nie widziała tego w ten sposób. Spojrzała poza to wszystko i zakochaliśmy się."
scene d0_fight13 with dissolve
#dad "To her father's dismay, he couldn't get her to stop seeing me."
dad "Ku rozczarowaniu jej ojca, nie udało mu się powstrzymać jej przed spotkaniami ze mną."
#dad "But he knew that once the hotel was built, there was no reason for me to stay and work in that town."
dad "Ale wiedział, że po wybudowaniu hotelu nie było powodu, abym został i pracował w tym mieście."
scene d0_fight14 with dissolve
#dad "And when that day came, I left. I had to make a living after all."
dad "A kiedy ten dzień nadszedł, odszedłem. W końcu musiałem zarabiać na życie."
#dad "So, with a heavy heart, I left Lynette."
dad "Więc z ciężkim sercem opuściłem Lynette."
scene d0_fight15 with dissolve
#dad "But before doing so, I gave her the best kiss I ever could have given her."
dad "Ale zanim to zrobiłem, dałem jej najlepszy pocałunek, jaki mogłem jej dać."
scene d0_fight16 with dissolve
#dad "To me...that was it."
dad "Dla mnie... to było to."
#dad "The last time I would ever gaze upon her."
dad "Ostatni raz, kiedy na nią spojrzałem."
scene black with fade
#dad "But your mom, stubborn as a mule, didn't give up that easily."
dad "Ale twoja mama, uparta jak osioł, nie poddała się tak łatwo."
scene d0_fight18 with dissolve
#dad "It took her three days to run away from home and track me down."
dad "Ucieczka z domu i wyśledzenie mnie zajęło jej trzy dni."
#dad "No...wait...five days?"
dad "Nie... czekaj... pięć dni?"
#dad "Hm...maybe it was something along the lines of a week?"
dad "Hm... może to było coś w stylu tygodnia?"
#mc "Are you seriously asking {b}me{/b} that?"
mc "Naprawdę {b}mnie{/b} o to pytasz?"
#dad "No, well, it was something like that."
dad "Nie, no to było coś takiego."
#dad "Either way...where was I?"
dad "Tak czy inaczej... na czym stanołem?"
#dad "Oh yeah!"
dad "O tak!"
#dad "She didn't want her dad's life or his money..."
dad "Nie chciała życia jak tata ani jego pieniędzy..."
#dad "She wanted me."
dad "Chciała mnie."
scene d0_fight10 with dissolve
#dad "If something's meant to be, it will happen, son."
dad "Jeśli coś ma się wydarzyć, to się wydarzy, synu."
#dad "But make sure that you give it your best try and that you leave without regrets."
dad "Ale upewnij się, że dajesz z siebie wszystko i że odchodzisz bez żalu."
#dad "Because regrets can come back to haunt you later in life."
dad "Ponieważ żale mogą powrócić, aby prześladować Cię w późniejszym życiu."
scene d0_fight8 with dissolve
#mc "I regret never meeting mom."
mc "Żałuję, że nigdy nie spotkałem mamy."
scene d0_fight21 with dissolve
#dad "Hey now, you can't regret things out of your control."
dad "Hej, nie możesz żałować rzeczy, na które nie masz wpływu."
#dad "And you did meet her briefly before she passed away."
dad "I poznałeś ją na krótko, zanim zmarła."
scene d0_fight10 with dissolve
#dad "She said \"He's so beautiful\". Those were her exact words about you."
dad "Powiedziała: „Jest taki piękny”. To były dokładnie jej słowa o tobie."
stop music fadeout 10
#dad "Tell Josy how you feel, son. That's my advice."
dad "Powiedz Josy, jak się czujesz, synu. Taka jest moja rada."
#dad "Don't keep your emotions locked up."
dad "Nie trzymaj swoich emocji pod kluczem."
$ guideSuggestedPage = 30
jump ep1_freeroam_home_label
label ep1_date_label:

$ current_task = "None"
$ chat_new_tasks = False
$ renpy.block_rollback()
scene d0_date with Fade(1.5, 1, 0.5)
play music "music/ep1/scrapbook.mp3"
#mc "(I wonder what Josy has planned for us.)"
mc "(Zastanawiam się, co Josy dla nas zaplanowała.)"
#mc "(It sure feels like a date...)"
mc "(Z pewnością czuję się jak na randce...)"
#mc "(A Saturday night, starry sky...)"
mc "(Sobotnia noc, rozgwieżdżone niebo...)"
#mc "(This is my only shot if I want to make a move on her.)"
mc "(To moja jedyna szansa, jeśli chcę się do niej zbliżyć.)"
scene d0_date_1 with dissolve
#js "Hey [name]!"
js "Hej!"
#mc "Hi Josy!"
mc "Cześć Josy!"
#js "Were you too scared to ring the doorbell, or what?"
js "Za bardzo się bałeś, żeby zadzwonić do drzwi, czy co?"
scene d0_date_2 with dissolve
#mc "Oh, sorry. I thought we were supposed to meet out here."
mc "Przepraszam. Myślałem, że mieliśmy się tu spotkać."
scene d0_date_3 with dissolve
#js "Haha, it's ok."
js "Haha, już dobrze."
if ep1_josy_chat1_state > 0:
    scene d0_date_2 with dissolve
#    mc "I see that you found something to wear."
    mc "Widzę, że znalazłeś coś do ubrania."
    scene d0_date_3 with dissolve
#    js "Yeah, I did."
    js "Tak, zrobiłem."
    scene d0_date_2 with dissolve
    if ep1_josy_chat1_state == 2:
        menu:
#            "I like it":
            "Lubię ten środek transportu":
                $ RPjosy += 1
                if dtype > 0:
#                    mc "You look hot in it."
                    mc "Wyglądasz w nim seksownie."
                else:
#                    mc "I like it! You look very pretty."
                    mc "Podoba mi się! Wyglądasz bardzo ładnie."
                scene d0_date_4 with hpunch
#                js "Stop it..."
                js "Przestań."
                scene d0_date_3 with dissolve
#            "It's better than wearing nothing.":
            "Lepsze to niż nic.":
                $ RPjosy += 1
#                mc "It's better than wearing nothing."
                mc "Lepsze to niż nic."
                scene d0_date_3 with dissolve
#                js "Still thinking about that, huh?"
                js "Wciąż o tym myślisz, co?"
#            "Let's go":
            "Zaczynajmy":
#                mc "Ok, let's go."
                mc "No dobra, to jedziemy dalej."
                scene d0_date_3 with dissolve
    else:
        menu:
#            "I like it":
            "Lubię ten środek transportu":
                $ RPjosy += 1
                if dtype > 0:
#                    mc "You look hot in it."
                    mc "Wyglądasz w nim seksownie."
                else:
#                    mc "I like it! You look very pretty."
                    mc "Podoba mi się! Wyglądasz bardzo ładnie."
                scene d0_date_4 with hpunch
#                js "Stop it..."
                js "Przestań."
                scene d0_date_3 with dissolve
#            "Let's go":
            "Zaczynajmy":
#                mc "Ok, let's go."
                mc "No dobra, to jedziemy dalej."
                scene d0_date_3 with dissolve
$ guideSuggestedPage = 31
#js "Scoot forward and make space for my cute butt."
js "Przesuń się do przodu i zrób miejsce na mój słodki tyłek."
scene d0_date_2 with dissolve
menu:
#    "Flirt with her":
    "Flirtuj z nią":
        if dtype > 0:
#            $ bios_history_josy = "I flirted with Josy, but I think she took it the wrong way.\n\n"
            $ bios_history_josy = "Flirtowałam z Josy, ale chyba źle to odebrała.\n \n"
            $ bios_name_josy = True
            $ chat_new_bios = True
#            mc "I think you meant cute and sexy butt."
            mc "Myślę, że miałeś na myśli słodki i seksowny tyłek."
            scene d0_date_4b with dissolve
#            js "[name]... Really?"
            js "Serio?"
            $ RPjosy -= 1
#            js "You sound like Steve."
            js "Brzmisz jak Steve."
        else:
#            $ bios_history_josy = "I flirted with Josy and I think she liked it.\n\n"
            $ bios_history_josy = "Flirtowałam z Josy i myślę, że jej się spodobało.\n \n"
            $ bios_name_josy = True
            $ RPjosy += 1
            $ chat_new_bios = True
#            mc "It is very cute."
            mc "To jest bardzo urocze."
            scene d0_date_4 with hpunch
#            js "Haha, [name]..."
            js "Haha"
#    "Don't push your luck":
    "--- ":
#        mc "Ok."
        mc "Ok."
scene d0_date_5 with fade
#mc "Where am I taking us?"
mc "Dokąd nas zabieram?"
scene d0_date_6 with dissolve
#js "Just a bit further..."
js "Jeszcze troszkę..."
#js "You see that road to the right over there? Go that way."
js "Widzisz tamtą drogę na prawo? Idź tędy."
scene d0_date_5 with dissolve
stop music fadeout 5
#mc "I think that's a dead end."
mc "Myślę, że to ślepy zaułek."
scene d0_date_6 with dissolve
#js "Trust me; it's the right way."
js "Zaufaj mi; to właściwa droga."
scene d0_date_7 with fade
$ renpy.sound.play("sound_effects/crickets.mp3", channel="sfx1", loop=True)
#js "Here we are!"
js "No to jesteśmy!"
play music "music/ep1/windswept.mp3"
menu:
    "Check her out ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color} or {color=#ffffff}{size=-1}{font=collegiate.ttf}CHICK{/font}{/size}{/color})" if dtype != 0:
        if dik > 5:
            scene d0_date_7b with dissolve
        else:
            scene d0_date_7c with dissolve
        $ renpy.pause()
#    "Don't push your luck":
    "--- ":
        $ renpy.pause(0.2)
scene d0_date_7 with dissolve
if dik > 5:
#    mc "This is a pretty cool place!"
    mc "Niepewność:  To całkiem fajne miejsce!"
else:
#    mc "Such a beautiful place."
    mc "Pi?kne miejsce."
scene d0_date_8 with dissolve
#js "Yes! This is my little sanctuary."
js "Tak! To moje małe sanktuarium."
#js "I've never seen anyone come here before."
js "Nigdy wcześniej nie widziałem, żeby ktoś tu przychodził."
#js "I found this place one day when I was out running and got lost."
js "Znalazłem to miejsce pewnego dnia, kiedy biegałem i zgubiłem się."
#js "Since then, I have come here once in a while to think."
js "Od tego czasu przychodzę tu raz na jakiś czas, żeby pomyśleć."
scene d0_date_8b with dissolve
#mc "What do you think about?"
mc "O czym wtedy myślisz? "
scene d0_date_8 with dissolve
#js "You know, about life and the future."
js "No wiesz, o życiu i przyszłości."
scene d0_date_10 with dissolve
#js "Come, sit with me."
js "Chodź, usiądź ze mną."
scene d0_date_10a with dissolve
#js "I'm gonna try to let you do the talking for a while."
js "Postaram się pozwolić ci mówić przez jakiś czas."
#js "Otherwise, I'll just blabber on."
js "W przeciwnym razie po prostu się wygadam."
scene d0_date_10aa with dissolve
#js "Did you like working at the minimart this summer?"
js "Czy podobała Ci się praca w minimarcie tego lata?"
#mc "It was all right. The pay was decent."
mc "Wszystko było w porządku. Płaca była przyzwoita."
scene d0_date_10b with dissolve
#js "Yeah, I guess you're going to need it if you're going to B&R."
js "Tak, myślę, że będziesz go potrzebować, jeśli wybierasz się do B&R."
scene d0_date_10c with dissolve
#mc "Sure, but I'm taking a student loan, just like most students."
mc "Jasne, ale biorę pożyczkę studencką, tak jak większość studentów."
#mc "Aren't you?"
mc "Prawda? "
scene d0_date_10d with dissolve
#js "No, my dad has saved up for my tuition."
js "Nie, mój tata zaoszczędził na moje czesne."
#js "Didn't your parents do the same?"
js "Czy twoi rodzice nie zrobili tego samego?"
scene d0_date_10g with dissolve
#mc "My mom passed away shortly after I was born, so it's just been me and my dad."
mc "Moja mama zmarła niedługo po moich narodzinach, więc zostaliśmy tylko ja i mój tata."
scene d0_date_10h with dissolve
#js "Oh, I'm so sorry!"
js "Och, przepraszam! "
scene d0_date_10g with dissolve
#mc "Don't worry; you couldn't have known that."
mc "Nie martw się; nie mogłeś tego wiedzieć."
scene d0_date_10i with dissolve
#mc "He takes very good care of me, but no...he can't afford my college tuition."
mc "Bardzo dobrze się mną opiekuje, ale nie... nie stać go na moje czesne."
scene d0_date_10j with dissolve
#mc "But it doesn't matter. I love my dad."
mc "Ale to nie ma znaczenia. Kocham mojego tatę."
#mc "He's taught me everything I know..."
mc "Nauczył mnie wszystkiego, co wiem..."
#mc "...well, it's mostly \"man stuff\", like carpentry and martial arts."
mc "...cóż, to głównie \"męskie rzeczy\", takie jak stolarka i sztuki walki."
scene d0_date_10k with dissolve
#js "Haha! \"Man stuff\"? Listen to you."
js "Haha! \"Męskie rzeczy\"? Posłuchaj siebie."
#js "I know someone who would hate you for saying that."
js "Znam kogoś, kto by cię za to znienawidził."
#js "Women know about that, too, you know."
js "Kobiety też o tym wiedzą, wiesz."
scene d0_date_10l with dissolve
#mc "I didn't mean it that way. Of course, women know about it..."
mc "Nie to miałam na myśli. Oczywiście kobiety o tym wiedzą..."
#mc "...all I'm saying is that my dad teaches me what he knows, and it's often of that nature."
mc "... mówię tylko, że mój tata uczy mnie tego, co wie, i to często z tej natury."
scene d0_date_10k with dissolve
#js "The man stuff nature?"
js "Mężczyzna wypycha naturę?"
scene d0_date_10l with dissolve
#mc "Haha, sorry. I don't know how to describe it differently."
mc "Haha, przepraszam. Nie wiem, jak to inaczej opisać."
#mc "I try to teach myself stuff too. For instance, I've been playing guitar since I was twelve years old."
mc "Ja też staram się czegoś nauczyć. Na przykład gram na gitarze od dwunastego roku życia."
scene d0_date_10k with dissolve
#js "Oh, I'd love to hear you play for me sometime!"
js "Och, chciałbym kiedyś usłyszeć, jak dla mnie grasz!"
scene d0_date_10l with dissolve
#mc "Yeah, maybe..."
mc "Tak, być może."
#mc "So, you know a lot about carpentry and martial arts, then?"
mc "Więc dużo wiesz o stolarce i sztukach walki?"
scene d0_date_10m with dissolve
#js "Haha, no! I didn't mean that {b}I{/b} knew about it."
js "Haha, nie! Nie miałem na myśli, że {b}ja{/b} o tym wiedziałem."
#js "But I guess it could be fun to take a self-defense class or something."
js "Ale myślę, że fajnie byłoby wziąć udział w zajęciach z samoobrony."
scene d0_date_10l with dissolve
#mc "Hey, I can teach you that!"
mc "Hej, mogę cię tego nauczyć!"
scene d0_date_10o with dissolve
#js "Really?"
js "Serio?"
scene d0_date_10p with dissolve
#mc "Stand up. We can start small."
mc "Wstań. Możemy zacząć od czegoś małego."
#js "Haha, ok!"
js "Haha, ok!"
scene d0_date_10q with dissolve
#mc "Put your palms up like this."
mc "Podnieś dłonie w ten sposób."
#js "Uh-huh."
js "Yhm."
#mc "Now, strike with your left-hand palm against mine."
mc "Teraz uderz lewą dłonią o moją."
play sound "sound_effects/hit.mp3"
scene d0_date_10s with vpunch
#js "Ah!!!"
js "Ach. "
scene d0_date_10t with dissolve
#mc "Are you ok!?"
mc "Are you OK
"
#js "Hahaha! Sorry, I slipped!"
js "Hahaha! Przepraszam, poślizgnąłem się!"
#js "Did I hurt you?"
js "Czy zraniłem cię?"
#mc "Haha, no, I'm fine."
mc "Nie, trzymam się. "
if dtype < 1:
    scene d0_date_10u2 with dissolve
    $ RPjosy += 1
#    mc "Here, let me help you up."
    mc "- Pozwól, że pomogę."
scene d0_date_10v with dissolve
#mc "Yeah, this isn't the best place to teach you this."
mc "Tak, to nie jest najlepsze miejsce, aby Cię tego nauczyć."
#mc "Let's sit down again instead."
mc "Usiądźmy ponownie."
scene d0_date_11c with dissolve
#js "Say cheese!"
js "Uśmiech!"
#mc "Oh, ok. Cheese!"
mc "O, ok. Ser!"
scene white
play sound "sound_effects/camera_shutter.mp3"
$ renpy.pause(0.5)
scene d0_date_11c with dissolve
#js "Haha! Thanks."
js "Haha! Dzięki."
scene d0_date_11 with dissolve
#js "I can send it to you later."
js "Wyślę ci go później."
#js "But now..."
js "Ale teraz..."
#js "...I got us something for tonight."
js "...Mam coś dla nas na wieczór."
scene d0_date_11b with dissolve
#js "Tada!"
js "Ta-dam!"
#mc "Oh wow, you got booze?"
mc "Łał, masz gorzałę?"
#js "Haha, yup! I told you that I wanted to celebrate with you!"
js "Haha, tak! Mówiłem ci, że chcę świętować z tobą!"
scene d0_date_12b with dissolve
#mc "Where did you even get this?"
mc "Skąd pani to ma?"
scene d0_date_12c with dissolve
#js "I swiped it from my dad's cabinet."
js "Ukradłam go z szafki taty."
scene d0_date_12b with dissolve
#mc "Let me guess. You're hoping he will blame your brother for it?"
mc "Niech zgadnę. Masz nadzieję, że obwini o to twojego brata?"
scene d0_date_12c with dissolve
#js "Haha, maybe."
js "Haha, może."
scene d0_date_13 with dissolve
$ renpy.pause()
scene d0_date_14 with dissolve
#js "Here, have a sip!"
js "Masz, napij się!"
if dtype < 0:
#    mc "It's pure vodka!"
    mc "To czysta wódka!"
#    js "Haha, I know."
    js "Haha, wiem."
scene d0_date_15 with dissolve
$ renpy.pause()
scene d0_date_16 with dissolve
stop music fadeout 5
#mc "That's some strong stuff!"
mc "To naprawdę mocna rzecz!"
#js "Haha, yeah!"
js "Haha, tak!"
label ep1_josy_lewd:

if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
play music "music/ep1/lonely.mp3"
scene d0_date_17 with Fade(1.5, 1, 0.5)
#mc "It's so nice of you to do this for me. I really appreciate it!"
mc "To bardzo miłe z twojej strony, że to dla mnie robisz. Naprawdę to doceniam!"
scene d0_date_18 with dissolve
#js "I really wish we did this back when we started working together and not during your last weekend here."
js "Naprawdę żałuję, że nie zrobiliśmy tego, kiedy zaczęliśmy razem pracować, a nie podczas waszego ostatniego weekendu tutaj."
#mc "Yeah, me too."
mc "Tak, ja też."
scene d0_date_20 with dissolve
#js "I'm starting to get kind of tipsy over here."
js "Zaczynam się tu trochę podniecać."
#mc "We should've bought some sodas to mix the vodka with."
mc "Powinniśmy byli kupić jakieś napoje do mieszania wódki."
scene d0_date_22 with dissolve
#js "Haha, you're cute."
js "Haha, jesteś słodki."
#mc "(Did I say something?)"
mc "(Czy ja coś powiedziałem?)"
scene d0_date_23 with dissolve
#mc "(Oh, ok...)"
mc "Oh, ok."
#mc "(Wow, she's really hugging me tightly.)"
mc "(Wow, naprawdę mocno mnie przytula.)"
scene d0_date_23b with dissolve
#mc "(There's that wonderful smell of strawberries again...)"
mc "(Znowu ten cudowny zapach truskawek...)"
#mc "(This is it, [name]. It's now or never.)"
mc "(To jest to, [name]. Teraz albo nigdy.)"
#mc "(I'm just gonna put it out there.)"
mc "(Po prostu to wyłożę.)"
#mc "Josy?"
mc "Josy?"
scene d0_date_24 with dissolve
#js "Yeah?"
js "Tak?"
scene d0_date_23b with dissolve
#mc "I know this may sound a bit weird, but I just have to say it..."
mc "Wiem, że to może zabrzmieć trochę dziwnie, ale muszę to powiedzieć..."
#mc "This summer, working with you has been really awesome."
mc "Tego lata praca z Tobą była naprawdę niesamowita."
#mc "Even though I haven't really shown it..."
mc "Chociaż tak naprawdę tego nie pokazałem..."
#mc "...I've had a crush on you since the start of this summer."
mc "...Podkochiwałem się w tobie od początku tego lata."
scene d0_date_26b with dissolve
#js "You have?"
js "– Widziałaś?"
#mc "Yeah, I just wanted to tell you, so I don't regret it later on."
mc "Tak, chciałam ci tylko powiedzieć, żeby później tego nie żałować."
scene d0_date_28 with dissolve
#js "[name]... That's so sweet..."
js "To takie słodkie!” "
scene d0_date_29 with dissolve
$ renpy.pause()
init 500 image anim_josy_kiss_01_ep1 = Movie(channel="anim_josy_kiss_01_ep1", play="images/movies/ep1/anim_josy_kiss_01_ep1.webm")
scene anim_josy_kiss_01_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
init 500 image anim_josy_kiss_02_ep1 = Movie(channel="anim_josy_kiss_02_ep1", play="images/movies/ep1/anim_josy_kiss_02_ep1.webm")
scene anim_josy_kiss_02_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
if _in_replay:
    if persistent.ep1_josy_lewd_full or persistent.ep1_josy_lewd_chick:
        init 500 image anim_josy_kiss_03_ep1 = Movie(channel="anim_josy_kiss_03_ep1", play="images/movies/ep1/anim_josy_kiss_03_ep1.webm")
        scene anim_josy_kiss_03_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    if persistent.ep1_josy_lewd_full or persistent.ep1_josy_lewd_dik:
        init 500 image anim_josy_kiss_04_ep1 = Movie(channel="anim_josy_kiss_04_ep1", play="images/movies/ep1/anim_josy_kiss_04_ep1.webm")
        scene anim_josy_kiss_04_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
else:
    if dik < -5:
        init 500 image anim_josy_kiss_03_ep1 = Movie(channel="anim_josy_kiss_03_ep1", play="images/movies/ep1/anim_josy_kiss_03_ep1.webm")
        scene anim_josy_kiss_03_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
    elif dik > 5:
        init 500 image anim_josy_kiss_04_ep1 = Movie(channel="anim_josy_kiss_04_ep1", play="images/movies/ep1/anim_josy_kiss_04_ep1.webm")
        scene anim_josy_kiss_04_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
scene d0_date_30 with dissolve
#mc "I've wanted to do that for so long, Josy..."
mc "Tak długo chciałem to zrobić, Josy..."
$ renpy.end_replay()
if dtype > 0:
    $ persistent.ep1_josy_lewd_dik = True
else:
    $ persistent.ep1_josy_lewd_chick = True
if persistent.ep1_josy_lewd_dik and persistent.ep1_josy_lewd_chick:
    $ persistent.ep1_josy_lewd_full = True
$ calcScenes()
#js "[name]... I'm sorry..."
js "Przepraszam…"
#js "I shouldn't have done that..."
js "Nie powinienem był tego robić."
#mc "What? Why?"
mc "Co? Dlaczego?"
scene d0_date_32 with dissolve
#js "I'm already in a relationship..."
js "Jestem już w związku..."
scene d0_date_33 with dissolve
#mc "You're what?"
mc "Co ty jesteś?"
scene d0_date_30 with dissolve
#js "I'm so sorry..."
js "- Patrycja, przepraszam."
#js "It's complicated..."
js "To skomplikowane"
#js "I didn't mean for {i}this{/i} to happen..."
js "Nie chciałem, żeby do tego{i}doszło{/i}..."
scene d0_date_32 with dissolve
#js "But you're so..."
js "Ale ty jesteś taki..."
scene d0_date_33 with dissolve
#js "..."
js "..."
scene d0_date_30 with dissolve
#js "I've had a crush on you too."
js "Ja też się w tobie podkochiwałem."
#mc "Really? Wow..."
mc "Naprawdę? Wow..."
#mc "That's great!"
mc "To świetnie! "
scene d0_date_32 with dissolve
#js "It's not great, [name]..."
js "Nie jest wspaniale, Jess. "
#js "By doing this right now, I'm cheating..."
js "Robiąc to teraz, oszukuję..."
scene d0_date_38 with dissolve
#js "Fuck... I gotta go..."
js "Muszę lecieć."
#js "Please... Take me home..."
js "Proszę weź mnie. "
scene d0_date_38b with dissolve
#js "..."
js "..."
#mc "Are you cold?"
mc "Zimno ci?"
scene d0_date_38c with dissolve
#js "Just a tad..."
js "Tylko troszkę..."
#mc "Here..."
mc "W tym przypadku"
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene d0_date_39 with fade
#mc "(She's holding me even tighter than she did before...)"
mc "(Trzyma mnie jeszcze mocniej niż wcześniej...)"
#mc "(I can't believe this is happening...)"
mc "Nie dowierzam, że to się dzieje. "
#mc "(We have crushes on each other...)"
mc "(Podkochujemy się w sobie...)"
#mc "(...but we still can't be together.)"
mc "(...ale nadal nie możemy być razem.)"
scene d0_date_40 with dissolve
#mc "(She must be in an unhappy relationship to do something like this...)"
mc "(Musi być w nieszczęśliwym związku, żeby zrobić coś takiego...)"
#mc "(Maybe it's for the best, though?)"
mc "(Może jednak tak będzie lepiej?)"
#mc "(I'm still leaving for college, and she is likely staying here.)"
mc "(Nadal wyjeżdżam na studia, a ona prawdopodobnie zostanie tutaj.)"
#mc "(...)"
mc "(...)"
#mc "(Even so, it still hurts.)"
mc "(Mimo to nadal boli.)"
#mc "(At least I don't have to regret never telling her how I feel.)"
mc "(Przynajmniej nie muszę żałować, że nie powiedziałem jej, co czuję.)"
scene d0_date_41 with Fade(1.5, 1, 0.5)
#mc "Thanks for the night, Josy..."
mc "Dzięki za noc, Josy..."
#mc "I guess this is where we say farewell."
mc "Myślę, że tutaj się żegnamy."
scene d0_date_42 with dissolve
#js "Farewell? You're still coming back to visit, right?"
js "Pożegnanie? Nadal wracasz z wizytą, prawda?"
scene d0_date_43 with dissolve
#mc "I just thought...with what happened and all..."
mc "Po prostu pomyślałam... po tym, co się stało i w ogóle..."
#mc "Maybe it's just best to leave it like this?"
mc "Może po prostu najlepiej zostawić to tak?"
scene d0_date_44 with dissolve
#js "Ok..."
js "Dobrze..."
#js "What about your sweatshirt?"
js "A co z twoją bluzą?"
#mc "You can keep it."
mc "Możesz go zatrzymać."
#js "..."
js "..."
#js "Farewell, then."
js "W takim razie żegnaj."
scene d0_date_45 with dissolve
#mc "(Fuck...)"
mc "Kurwa…"
#mc "(This doesn't feel very good.)"
mc "(To nie jest zbyt przyjemne.)"
#mc "(Will this huge pain in my chest go away already.)"
mc "(Czy ten ogromny ból w klatce piersiowej już zniknie.)"
#js "[name]!!!"
js "[name]!!!"
scene d0_date_46 with dissolve
#js "Wait!"
js "Poczekaj!"
scene d0_date_48 with dissolve
#js "It's goodbye."
js "To pożegnanie!"
#js "Do you understand me?"
js "Czy Ty mnie rozumiesz?"
#js "Goodbye...not farewell..."
js "Żegnaj...nie żegnaj..."
scene d0_date_49 with dissolve
#mc "Goodbye, it is."
mc "Do widzenia, tak jest."
#$ bios_history_josy += "I went out on a date with Josy. It started out great, but after we made out I learned that she's in a relationship and was cheating by being with me. That hurt like hell to hear...\n\n"
$ bios_history_josy += "Poszłam na randkę z Josy. Zaczęło się świetnie, ale po tym, jak się poznaliśmy, dowiedziałem się, że jest w związku i oszukuje, będąc ze mną. To bolało jak cholera...\n \n"
$ bios_name_josy = True
$ chat_new_bios = True
scene d0_after_date with Fade(1.5, 1, 0.5)
#mc "(She's in a relationship...?)"
mc "(Ona jest w związku...?)"
#mc "(I should've known. She's way too perfect to be single.)"
mc "(Powinienem był się domyślić. Jest zbyt doskonała, by być singielką.)"
#mc "(Why did she lead me on, though?)"
mc "(Dlaczego mnie jednak zwodziła?)"
scene d0_after_date1 with dissolve
#mc "(She's been so forward with me...hugging me...)"
mc "(Była ze mną taka bezpośrednia...przytulała mnie...)"
#mc "(...kissing my cheek.)"
mc "(...całując mnie w policzek.)"
#mc "(I feel like such an idiot.)"
mc "(Czuję się jak idiotka.)"
#mc "(Not farewell...?)"
mc "(Nie pożegnanie...?)"
#mc "(What am I supposed to do with that?)"
mc "I co mam z tym niby zrobić?"
#mc "(Am I supposed to cling to hope?)"
mc "(Mam się trzymać nadziei?)"
scene d0_after_date2 with dissolve
#mc "(...or maybe just distance myself?)"
mc "(...a może po prostu się zdystansować?)"
stop music fadeout 10
#mc "(I'm going away to college...how much more can I distance myself from her?)"
mc "(Wyjeżdżam na studia... o ile bardziej mogę się od niej zdystansować?)"
#mc "(I'm going away...and her boyfriend is not.)"
mc "(Wyjeżdżam...a jej chłopak nie.)"
#mc "(Fuck... I need to find a way to get over her...)"
mc "(Kurwa... muszę znaleźć sposób, żeby o niej zapomnieć...)"
scene black with Fade(1.5, 1, 0.5)
init 500:
    image ep1_bg_scroll:
#        "images/ep1/car/car_scrolling_bg.jpg"
        "images/ep1/car/car_scrolling_bg.jpg"
        xalign 0.0
        linear 1 xalign 1.0
        repeat
show black
show ep1_bg_scroll
show d1_drive
hide black
play music "music/ep1/someways.mp3"
#dad "The first day of college..."
dad "I pierw-szy dzień na studiach."
#dad "I wonder what that feels like..."
dad "Zastanawiam się, jakie to uczucie..."
#dad "How does it feel, son?"
dad "Co o nim myślisz? "
hide d1_drive
show d1_drive1
menu:
#    "I feel excited":
    "Jestem podekscytowany":
#        mc "I feel pretty excited, dad."
        mc "Jestem bardzo podekscytowana, tato."
        hide d1_drive1
        show d1_drive
#        dad "That's the spirit!"
        dad "No, to mi się podoba."
#    "I'm nervous":
    "Jestem zdenerwowany, Jake.":
#        mc "I'm kind of nervous..."
        mc "Trochę się denerwuję..."
        hide d1_drive1
        show d1_drive
#        dad "I'm sure you'll be fine."
        dad "Na pewno sobie poradzisz!"
hide d1_drive
show d1_drive1
#mc "You really didn't have to rent a car for this..."
mc "Naprawdę nie musiałeś wynajmować na to samochodu..."
#mc "I would have been fine taking the train."
mc "Nie miałbym nic przeciwko, jadąc pociągiem."
hide d1_drive1
show d1_drive
#dad "Nonsense! This is a big day for both of us!"
dad "Bzdura! To wielki dzień dla nas obojga!"
hide d1_drive
show d1_drive4
#dad "Now, I've heard what college is like."
dad "Słyszałem, jak to jest w college 'u."
#dad "There will be a lot of...uh...temptations that you'll face as a freshman."
dad "Będzie wiele...uh...pokus, które napotkasz jako student pierwszego roku."
#dad "I just want you to know that it's ok to say no, son."
dad "Chcę tylko, żebyś wiedział, że możesz odmówić, synu."
hide d1_drive4
show d1_drive5
#mc "Do you mean to say no to drinking alcohol?"
mc "Czy masz na myśli odmowę picia alkoholu?"
hide d1_drive5
show d1_drive
#dad "Well, you're a grown man now."
dad "Cóż, jesteś już dorosłym mężczyzną."
#dad "Alcohol won't kill you..."
dad "Alkohol cię nie zabije..."
#dad "...unless you overdo it, of course."
dad "...chyba że przesadzasz, oczywiście."
#dad "But it's not just alcohol that may be tempting you."
dad "Ale nie tylko alkohol może Cię kusić."
hide d1_drive
show d1_drive4
#dad "You might come in contact with drugs."
dad "Możesz mieć kontakt z narkotykami."
#dad "I want you to be safe, son."
dad "Chcę, żebyś był bezpieczny, synu."
hide d1_drive4
show d1_drive5
#mc "Don't worry, dad. I don't have any interest in doing drugs."
mc "Nie martw się, tato. Nie interesują mnie narkotyki."
#mc "I'm going to college to educate myself."
mc "Idę na studia, żeby się kształcić."
hide d1_drive5
show d1_drive4
#dad "Also..."
dad "..."
#dad "I know that I haven't really talked to you about the birds and the bees yet..."
dad "Wiem, że nie rozmawialiśmy jeszcze o ptaszkach i pszczółkach..."
hide d1_drive4
show d1_drive5
#mc "You don't have to, dad."
mc "Nie musisz, tato."
#mc "I'm well aware of how that works."
mc "Zdaję sobie sprawę, jak to działa."
hide d1_drive5
show d1_drive4
#dad "Please know that there's no shame in putting on a condom."
dad "Pamiętaj, że nie ma wstydu w zakładaniu prezerwatywy."
hide d1_drive4
show d1_drive5
#mc "I know, dad!"
mc "Wiem, tato!"
hide d1_drive5
show d1_drive
#dad "Hey... I know that your date didn't go as you hoped it would."
dad "Hej... Wiem, że twoja randka nie poszła tak, jak się spodziewałeś."
#dad "But, chin up! Heartbreak is a natural thing."
dad "Ale głowa do góry! Złamane serce to naturalna rzecz."
scene d1_drive13 with fade:
    linear 10 zoom 1.1
#dad "Here we are."
dad "Oto ona."
#dad "Burgmeister & Royce."
dad "Burgmeister & Royce."
#dad "It sounds so fancy!"
dad "Brzmi tak fantazyjnie!"
#mc "It's not that big of a college, dad."
mc "To nie jest taki duży college, tato."
#dad "Ah! An elitist college, then!"
dad "Ach! W takim razie elitarna uczelnia!"
scene d1_drive16 with dissolve
#dad "Take care, son!"
dad "Trzymaj się, synu!"
#dad "Don't forget to call."
dad "Nie zapomnij zadzwonić."
scene d1_drive17 with dissolve
#mc "Thanks, dad! I won't forget."
mc "Dzięki, tato! Nie zapomnę."
scene d1_drive16 with dissolve
#dad "Come, give your old man a hug."
dad "Chodź, przytul staruszka."
scene d1_drive19 with dissolve
#jc "GAY ALERT!!!"
jc "ALERT DLA GEJÓW!!!"
scene d1_drive20 with dissolve
#jc "Why don't you grab his dick while you're at it!?"
jc "Może przy okazji złapiesz go za kutasa!?"
scene d1_college with wipeleft
#mc "Excuse me..."
mc "Przepraszam"
scene d1_college1 with dissolve
#rc "Hi, how may I help you?"
rc "W czym mogę pomóc? "
scene d1_college2 with dissolve
#mc "I'm a freshman...I have no clue where I'm supposed to be."
mc "Jestem na pierwszym roku... nie mam pojęcia, gdzie mam być."
scene d1_college1 with dissolve
#rc "ID, please."
rc "Poproszę dokument tożsamości."
scene d1_college3 with dissolve
#rc "You're late, you know?"
rc "Spóźniłeś się, wiesz?"
scene d1_college4 with dissolve
#mc "Am I?"
mc "Czy ja jestem? "
scene d1_college3 with dissolve
#rc "Yeah, you were supposed to be here one hour ago."
rc "Tak, miałaś tu być godzinę temu."
scene d1_college4 with dissolve
#mc "So...what should I do?"
mc "Więc co mam zrobić?"
scene d1_college1 with dissolve
#rc "Today is orientation; freshmen are walking around campus, visiting the different fraternities and the sorority."
rc "Dziś jest orientacja; pierwszoroczniaki chodzą po kampusie, odwiedzając różne bractwa i bractwa."
#rc "I suggest that you find your dorm quickly and then join the campus tour."
rc "Proponuję szybko znaleźć swój akademik, a następnie dołączyć do wycieczki po kampusie."
#rc "I take it that you've already signed up for a B&R ID online?"
rc "Rozumiem, że masz już zarejestrowany identyfikator B&R online?"
scene d1_college2 with dissolve
#mc "I have."
mc "Tak. "
scene d1_college10 with dissolve
#rc "That's great."
rc "Pięknie. "
#rc "Here's the key to your shared dorm, you're in the eastern wing. The dorm number is 66."
rc "Oto klucz do Twojego wspólnego akademika, jesteś we wschodnim skrzydle. Numer akademika to 66."
stop music fadeout 5
scene d1_college2 with dissolve
menu:
#    "Thank her":
    "Podziękuj jej":
        $ dk(-1)
#        mc "Thank you!"
        mc "Dziękujemy. Twój komentarz oczekuje na zatwierdzenie i niedługo powinien być dostępny."
        scene d1_college1 with dissolve
#        rc "You're most welcome."
        rc "Zapraszam."
#    "Just leave":
    "Po prostu wyjdź":
        $ dk(1)
        scene d1_college1 with dissolve
#        rc "...you're welcome."
        rc "Proszę bardzo."
play music "music/ep1/funk_rock.mp3"
scene d1_dorm0 with fade
#mc "(Is this the right corridor?)"
mc "(Czy to właściwy korytarz?)"
#mc "(Everything looks the same here...)"
mc "(Tutaj wszystko wygląda tak samo...)"
#mc "(Would it be the worst thing to put up comprehensible signs?)"
mc "(Czy umieszczenie zrozumiałych znaków byłoby najgorszą rzeczą?)"
scene d1_dorm with dissolve
#mc "(Dorm 66...this is it.)"
mc "(Akademik 66...to jest to.)"
#mc "(Hah. That's cute.)"
mc "(Hah. To urocze.)"
scene d1_dormc with dissolve
#troy "Hey hey hey! You can't just barge in here!"
troy "Hej, hej, hej! Nie możesz tu tak wpadać!"
#troy "Who the fuck are you!?"
troy "Kim ty, kurwa, jesteś?"
scene d1_dorm1 with dissolve
menu:
#    "Be confident":
    "Bądź pewny siebie":
        $ dk(1)
#        mc "Settle down. This is my dorm, too."
        mc "Uspokój się. To też mój akademik."
        scene d1_dorm2 with dissolve
#    "Be friendly":
    "Bądź miła.":
        $ dk(-1)
#        mc "Hi, I'm [name]."
        mc "Cześć, jestem (imię). "
#        mc "I believe I'm your dorm buddy."
        mc "Wierzę, że jestem twoim kumplem z akademika."
        scene d1_dorm2 with dissolve
#        troy "Not another one! I fucking told them yesterday..."
        troy "Ani jednego! Wczoraj im, kurwa, powiedziałem..."
#troy "I don't want to share this dorm!"
troy "Nie chcę dzielić się tym akademikiem!"
#troy "Find somewhere else to sleep."
troy "Znajdź sobie inne miejsce do spania."
scene d1_dorm1 with dissolve
#mc "I don't think it works that way..."
mc "Nie sądzę, żeby to działało w ten sposób..."
scene d1_dormc with dissolve
#troy "Hey, shithead!"
troy "Hej, zasrańcu!"
#troy "I'm not going to live here with you."
troy "Nie będę tu z tobą mieszkać."
scene d1_dorm1 with dissolve
$ guideSuggestedPage = 32
menu:
#    "Be rude":
    "Bądź niegrzeczny":
        $ dk(1)
#        mc "Well, then maybe you should leave. Because I'm not."
        mc "No to może powinieneś już iść. Bo nie jestem."
#    "Be friendly":
    "Bądź miła.":
        $ dk(-1)
#        mc "Come on, don't be like that."
        mc "&lt;i&gt;Daj spokój, nie złość się!&lt;/i&gt;"
#        mc "I'm sure we can get along."
        mc "Na pewno się dogadamy."
scene d1_dorm5 with dissolve
#troy "Fucking morons are running this place."
troy "Jebani kretyni rządzą tym miejscem."
scene d1_dorm6 with dissolve
#troy "If I have to share this dorm with you, here's the deal..."
troy "Jeśli będę musiał podzielić się z tobą tym akademikiem, umowa jest taka..."
#troy "You're allowed to sleep on that bed."
troy "Możesz spać na tym łóżku."
#troy "But daytime, when I'm in here, you're not."
troy "Ale w dzień, kiedy ja tu jestem, ciebie nie ma."
#troy "Got it!?"
troy "Zrobione"
#mc "I guess."
mc "Pewnie tak."
scene d1_dorm9 with dissolve
#troy "Good. Now drop your shit off and get out before I change my mind."
troy "Dobrze. A teraz rzuć to gówno i wynoś się, zanim zmienię zdanie."
scene d1_dorm9b with dissolve
#mc "Can we start over and try to get along?"
mc "Czy możemy zacząć od nowa i spróbować się dogadać?"
#mc "I could use someone to help me find the campus tour group."
mc "Przydałby mi się ktoś, kto pomógłby mi znaleźć grupę wycieczkową po kampusie."
scene d1_dorm9b2 with dissolve
stop music fadeout 5
#troy "Oh, you could?"
troy "Och, mogłabyś?"
play sound "sound_effects/door_slam.mp3"
scene d1_dorm with hpunch
#mc "..."
mc "..."
$ bios_troy = True
#$ bios_history_troy = "I just met Troy and he's an asshole. It will be difficult to share a dorm with someone who doesn't want me there.\n\n"
$ bios_history_troy = "Dopiero co poznałam Troya, a on jest dupkiem. Trudno będzie dzielić akademik z kimś, kto mnie tam nie chce.\n \n"
$ bios_name_troy = True
$ chat_new_bios = True
#mc "(What a shitty start this has been...)"
mc "(Co za gówniany początek...)"
play music "music/ep1/fresh_air.mp3"
scene d1_corridor with fade
#mc "(Where did everybody go?)"
mc "(Gdzie wszyscy poszli?)"
#mc "(Should I go back to the reception and ask for help?)"
mc "(Czy powinienem wrócić do recepcji i poprosić o pomoc?)"
scene d1_corridor1 with dissolve
#mc "Ah!!!"
mc "Ach. "
scene d1_corridor2 with hpunch
#mc "Dammit..."
mc "- Cholera! "
#uk "Haha. Do you need a hand?"
uk "Haha. Potrzebujesz pomocy?"
scene maya_intro with fade
$ renpy.pause()
scene d1_corridor3 with dissolve
#mc "Oh, hi..."
mc "Och, cześć! "
menu:
#    "Sure":
    "Pewnie":
#        mc "Sure."
        mc "Dobrze."
        scene d1_corridor4 with dissolve
        menu:
            "Check her panties ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
#                $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up.\nWhile helping me up I got a good look at her panties, she noticed and didn't seem to like it.\n\n"
                $ bios_history_maya = "Spotkałem dziś Mayę, kiedy leżałem na podłodze; zaproponowała, że pomoże mi wstać.\nPomagając mi wstać, dobrze przyjrzałem się jej majtkom, zauważyła i nie spodobało jej się to.\n \n"
                $ bios_name_maya = True
                $ chat_new_bios = True
                $ RPmaya -= 1
                $ dk(1)
                scene d1_corridor4b with dissolve
#                mc "(Holy shit...)"
                mc "Cholera"
                scene d1_corridor4c with dissolve
#                uk "Hey..."
                uk "Hej"
#                mc "Sorry..."
                mc "Przepraszam..."
#            "Check her out":
            "Patrz na nią. ":
#                $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up.\nWhile helping me up I kind of checked her out, she noticed and seemed flattered.\n\n"
                $ bios_history_maya = "Spotkałem dziś Mayę, kiedy leżałem na podłodze; zaproponowała, że pomoże mi wstać.\nPomagając mi wstać, tak jakby ją sprawdziłem, zauważyła i wydawała się zaszczycona.\n \n"
                $ bios_name_maya = True
                $ chat_new_bios = True
                $ RPmaya += 1
                scene d1_corridor4d with dissolve
#                mc "(Yum...)"
                mc "Mniam"
#            "Don't push your luck":
            "--- ":
                $ dk(-1)
#                $ bios_history_maya = "I met Maya today while I was lying on the floor; she helped me get back up.\n\n"
                $ bios_history_maya = "Spotkałem dziś Mayę, kiedy leżałem na podłodze; pomogła mi wstać.\n \n"
                $ bios_name_maya = True
                $ chat_new_bios = True
#    "No thanks":
    "Nie, dziękuję":
#        $ bios_history_maya = "I met Maya today while I was lying on the floor; she offered to help me get back up but I declined.\n\n"
        $ bios_history_maya = "Spotkałem dziś Mayę, kiedy leżałem na podłodze; zaproponowała, że pomoże mi wstać, ale odmówiłem.\n \n"
        $ bios_name_maya = True
        $ chat_new_bios = True
#        mc "No thanks."
        mc "Nie, dzięki."
scene d1_corridor5 with dissolve
#uk "That was quite a fall. Are you ok?"
uk "To był niezły upadek. Wszystko w porządku?"
scene d1_corridor7 with dissolve
#mc "Yeah, I was too busy figuring out where I was going."
mc "Tak, byłam zbyt zajęta rozgryzaniem, dokąd idę."
scene d1_corridor9 with dissolve
#uk "Ah, that must mean that you're a freshman?"
uk "Ach, to musi oznaczać, że jesteś na pierwszym roku?"
scene d1_corridor7 with dissolve
#mc "Yeah, that's right. I'm [name], by the way."
mc "Tak, zgadza się. Przy okazji, jestem [name]."
scene d1_corridor8 with dissolve
#my "Cool. I'm Maya."
my "Super. Jestem Maya."
scene d1_corridor9 with dissolve
#my "So, what are you doing in here?"
my "Co ty tu robisz? "
#my "Today's orientation day!"
my "Dzisiejszy dzień wprowadzający!"
scene d1_corridor10 with dissolve
#mc "Yeah, I know...but I arrived too late and missed the tour."
mc "Tak, wiem...ale przyjechałem za późno i przegapiłem wycieczkę."
scene d1_corridor11 with dissolve
#my "Well, that sucks."
my "No to huj. "
scene d1_corridor10 with dissolve
#mc "Yeah..."
mc "Tak"
scene d1_corridor9 with dissolve
#my "Shit, now I feel bad for you."
my "Cholera, teraz ci współczuję."
#my "How about I show you around, instead?"
my "Może zamiast tego cię oprowadzę?"
scene d1_corridor10 with dissolve
#mc "Would you do that?"
mc "Po co w ogóle to robić? "
scene d1_corridor15 with dissolve
#my "Sure, follow me."
my "Jasne, chodź za mną."
scene d1_corridor16 with dissolve
#mc "I take it you're not a freshman yourself?"
mc "Rozumiem, że też nie jesteś pierwszoroczniakiem?"
scene d1_corridor17 with dissolve
#my "Actually, I am. But I'm also a local, so I've been here at high school events."
my "Właściwie to jestem. Ale jestem też tutejsza, więc byłam tutaj na imprezach w liceum."
#my "It's not a big campus, really."
my "To nie jest duży kampus, naprawdę."
scene d1_corridor18 with dissolve
#mc "What are you going to study?"
mc "Co zamierzasz studiować?"
scene d1_corridor19 with dissolve
#my "I've applied for a social work degree."
my "Złożyłem wniosek o dyplom z pracy socjalnej."
scene d1_corridor18 with dissolve
#mc "Ok...I don't really know what that means."
mc "Ok... Nie bardzo wiem, co to znaczy."
scene d1_corridor19 with dissolve
#my "Hah, that's ok."
my "Hah, w porządku."
#my "Besides, I think most freshmen have the same general education classes the first year anyway."
my "Poza tym myślę, że większość studentów pierwszego roku i tak ma te same zajęcia ogólnokształcące na pierwszym roku."
scene d1_corridor18 with dissolve
#mc "The selection was pretty poor..."
mc "Wybór był dość kiepski..."
stop music fadeout 5
scene d1_corridor20 with dissolve
#my "That's small colleges for you."
my "To małe uczelnie dla ciebie."
play music "music/ep1/dont_count_on_me.mp3"
scene d1_campus with fade
#my "How much do you know about this place?"
my "Co wiesz o tym miejscu?"
#mc "I know the history of the campus, but not much else."
mc "Znam historię kampusu, ale niewiele więcej."
#my "Cool. So, on this campus, we have four fraternities and one sorority; the rest of the students live in co-ed dorms."
my "Super. Więc na tym kampusie mamy cztery bractwa i jedno bractwo; reszta studentów mieszka w akademikach."
scene d1_campus3 with dissolve
#my "There's the nerd fraternity, the tri-betas..."
my "Jest bractwo kujonów, tri-beta..."
#mc "The nerds?"
mc "Kujony?"
#my "Yeah, I know it's kind of insensitive, but they're very smart."
my "Tak, wiem, że to trochę niewrażliwe, ale są bardzo mądre."
scene d1_campus3b with dissolve
#my "I think they take pride in being called nerds, too."
my "Myślę, że oni też są dumni z bycia nazywanymi kujonami."
#my "Anyway, they don't have a house. They just hang around the library most of the time."
my "W każdym razie nie mają domu. Przez większość czasu po prostu kręcą się po bibliotece."
#my "Not having a house helps a lot with their expenses, too."
my "Brak domu również bardzo pomaga w wydatkach."
scene d1_campus4 with dissolve
#my "Over there, you have the rich kids' club, \"the preps\", or whatever you want to call them."
my "Tam znajduje się klub dla bogatych dzieci, \"przygotowujący\" lub jakkolwiek chcesz je nazwać."
#my "They go by the acronym Alpha Nu Omega."
my "Używa się ich pod akronimem Alpha Nu Omega."
#mc "Alpha and Omega...that's clever. Is it a biblical fraternity?"
mc "Alfa i Omega...to sprytne. Czy to biblijne bractwo?"
#my "Haha, no way. I think it means that they put themselves first and last, with no room for others."
my "Haha, nie ma mowy. Myślę, że to oznacza, że stawiają siebie na pierwszym i ostatnim miejscu, bez miejsca dla innych."
scene d1_campus4b with dissolve:
    linear 10 zoom 1.02
#my "That guy over there is Tybalt, their fraternity president."
my "Tamten facet to Tybalt, ich prezes bractwa."
#my "Every year, his family donates a lot of money to B&R. It's always a big deal in the local newspapers."
my "Każdego roku jego rodzina przekazuje wiele pieniędzy na rzecz B&R. To zawsze wielka sprawa w lokalnych gazetach."
$ bios_tybalt = True
$ bios_name_tybalt = True
$ chat_new_bios = True
scene d1_campus5 with dissolve
#my "Then we have the jocks, the tri-alphas."
my "Potem mamy sportowców, tri-alfy."
#my "A bunch of meatheads in that house."
my "Banda półgłówków w tym domu."
scene d1_campus5b with dissolve
#my "Unless you're a jock..."
my "Chyba że jesteś sportowcem..."
#my "...you should probably stay away from them."
my "...powinieneś chyba trzymać się od nich z daleka."
#my "They get nasty."
my "Robią się nieprzyjemne."
#mc "Noted."
mc "To naprawdę ważne!"
scene d1_campus6 with dissolve
#my "That house over there is the only sorority on campus."
my "Tamten dom to jedyne bractwo w kampusie."
#my "The Eta Omicron Tau or HOT for short."
my "Eta Omicron Tau lub w skrócie HOT."
#my "The jocks and the HOTs have a long history; they usually party together."
my "Sportowcy i HOT-y mają długą historię; zwykle imprezują razem."
scene d1_campus6b2 with dissolve
#mc "What are they like?"
mc "Jakie są te osoby? "
scene d1_campus6b3 with dissolve
#my "A bunch of sluts, if you ask me."
my "Banda zdzir, jeśli o mnie chodzi."
scene d1_campus6b4 with dissolve
#my "Well, we all have our vices, and I'm still gonna pledge their house."
my "Cóż, wszyscy mamy swoje wady i nadal zamierzam zastawić ich dom."
scene d1_campus6b with dissolve
#mc "Huh? It sounds like you don't like them. Why would you want to pledge?"
mc "Hę? Wygląda na to, że ich nie lubisz. Dlaczego chcesz udzielić wsparcia finansowego?"
scene d1_campus6c with dissolve
#my "It's kind of unofficial, but rumor has it that they pay for your entire tuition if you fit their criteria."
my "To trochę nieoficjalne, ale plotka głosi, że płacą za całe Twoje czesne, jeśli spełniasz ich kryteria."
scene d1_campus6d with dissolve
menu:
#    "Really?":
    "Serio?":
#        mc "Wow, are you serious?"
        mc "Naprawdę?"
        scene d1_campus6c with dissolve
#        my "Yeah, I really need that money."
        my "Tak, naprawdę potrzebuję tych pieniędzy."
#    "Tell a joke":
    "powiedz kawał":
        $ RPmaya += 1
#        mc "Can I pledge, too?"
        mc "Czy ja też mogę złożyć obietnicę?"
        scene d1_campus6d2 with dissolve
#        my "Haha! I'd like to see you try!"
        my "No ciekawe czy by ci się to udało!"
        scene d1_campus6c with dissolve
#        my "I really need that money..."
        my "Naprawdę potrzebuję tych pieniędzy..."
#my "My dad was going to pay for my tuition, but he gave me an ultimatum that I..."
my "Mój tata miał zapłacić za moje czesne, ale postawił mi ultimatum, że ja..."
scene d1_campus6e with dissolve
#my "You know what...? We just met."
my "Wiesz co... dopiero się poznaliśmy."
scene d1_campus6d with dissolve
#mc "It's ok. I understand."
mc "W porządku. Rozumiem."
#mc "It's common to take student loans, though."
mc "Powszechne jest jednak zaciąganie kredytów studenckich."
scene d1_campus6g with dissolve
#my "Yeah, I'm doing that, but it's not that simple... I need that money."
my "Tak, robię to, ale to nie takie proste... Potrzebuję tych pieniędzy."
#$ bios_history_maya += "Maya said she wants to pledge the HOTs. Apparently they offer to pay the tuition for their sorority sisters. She seems to have some sort of issues with her dad.\n\n"
$ bios_history_maya += "Maya powiedziała, że chce przyłączyć się do HOTów. Podobno oferują opłacenie czesnego dla swoich sióstr z bractwa. Wygląda na to, że ma jakieś problemy z tatą.\n \n"
$ bios_name_maya = True
$ chat_new_bios = True
scene d1_campus7 with dissolve
#mc "You mentioned there being four fraternities...which is the fourth one?"
mc "Wspomniałeś, że są cztery bractwa...które jest czwarte?"
scene d1_campus6d2 with dissolve
#my "Oh right! I almost forgot about them."
my "Ach tak! Prawie o nich zapomniałem."
#my "It's a new frat house, called the DIKs. It's right over there."
my "To nowy dom bractwa, zwany DIK-ami. Jest tam."
scene d1_campus9 with dissolve
#mc "Delta Iota Kappa?"
mc "Delta Iota Kappa?"
#my "Yeah, you got it."
my "Tak, masz to jak w banku."
#my "They have only been around for a couple of years, and their name goes hand in hand with their personalities."
my "Żyją dopiero od kilku lat, a ich imię idzie w parze z ich osobowością."
#mc "That's a huge mansion, though!"
mc "To jednak ogromna rezydencja!"
#my "Yeah, I have no clue how they can afford that place. You'll have to ask them about it."
my "Tak, nie mam pojęcia, jak mogą sobie na to pozwolić. Będziesz musiał ich o to zapytać."
scene d1_campus6d2 with dissolve
#my "So...that's about it."
my "To tyle na ten temat."
#my "Are you thinking of pledging a frat house?"
my "Myślisz o założeniu bractwa?"
scene d1_campus7 with dissolve
#mc "I'm not sure... I didn't really think about it before coming here."
mc "Nie jestem pewna... tak naprawdę nie myślałam o tym przed przyjazdem tutaj."
scene d1_campus6g with dissolve
#my "Yeah, I hear ya."
my "Tak, słyszę cię."
#my "You can do like the rest and just stay in your shared dorm."
my "Możesz polubić resztę i po prostu zatrzymać się we wspólnym akademiku."
scene d1_campus7 with dissolve
#mc "Yeah... I'd rather not."
mc "Wolałbym nie."
#mc "My dorm...guy...doesn't like me."
mc "Mój chłopak z akademika... mnie nie lubi."
scene d1_campus6d2 with dissolve
#my "Haha! Damn, [name]."
my "Haha! Cholera, [name]."
#my "You've barely been here an hour and are already making enemies?"
my "Jesteś tu zaledwie godzinę i już narobiłeś sobie wrogów?"
scene d1_campus7 with dissolve
#mc "Yeah..."
mc "Tak"
scene d1_campus16 with dissolve
#my "Well, you can consider me a friend at least."
my "Cóż, przynajmniej możesz mnie uważać za przyjaciela."
scene d1_campus17 with dissolve
menu:
#    "Cool":
    "Fajna":
#        mc "Cool."
        mc "Fajnie."
#    "Compliment her":
    "Praw jej komplementy":
#        $ bios_history_maya += "I complimented Maya, she liked it.\n\n"
        $ bios_history_maya += "Pochwaliłem Mayę, spodobało jej się to.\n \n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ RPmaya += 1
        $ dk(-1)
#        mc "I really appreciate that, Maya."
        mc "Na prawdę to doceniam..."
#        mc "You seem like a fun person."
        mc "Wydajesz się zabawną osobą."
scene d1_campus18 with dissolve
#my "Oh, look! I think I see the tour guide by the entrance! I think you should go tag along and meet some new people."
my "O, patrzcie! Chyba widzę przewodnika przy wejściu! Myślę, że powinieneś pójść i poznać nowych ludzi."
scene d1_campus7 with dissolve
#mc "What about you?"
mc "A ty?"
scene d1_campus16 with dissolve
#my "I'll join you for the first class after lunch. I need to chat with the HOTs."
my "Dołączę do ciebie na pierwsze zajęcia po obiedzie. Muszę porozmawiać z gorącymi."
scene d1_campus17 with dissolve
menu:
    "Hug her ({color=#ffffff}{size=-1}{font=collegiate.ttf}CHICK{/font}{/size}{/color})" if dtype < 0:
#        $ bios_history_maya += "I hugged Maya, she liked it.\n\n"
        $ bios_history_maya += "Przytuliłem Mayę, podobało jej się to.\n \n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ RPmaya += 1
        scene d1_campus20b with dissolve
#        mc "Thank you for the help."
        mc "Dziękuję za pomoc."
#        my "Aw! You're welcome!"
        my "Nie ma za co! "
#    "Bye":
    "Cześć.":
#        mc "Bye, Maya."
        mc "Pa, Maya."
scene d1_campus20 with dissolve
$ bios_maya = True
$ bios_name_maya = True
$ chat_new_bios = True
#my "Later!"
my "Do później! "
scene d1_tour with wiperight
#ca "Professors Castor Burgmeister and Sigmond Royce founded this college in 1921."
ca "Profesorowie Castor Burgmeister i Sigmond Royce założyli tę uczelnię w 1921 roku."
#ca "Their vision was that everyone can become who they want to be."
ca "Ich wizją było to, że każdy może stać się tym, kim chce."
scene d1_tourb with dissolve
#ca "Much like the students before you and the students to come, you will learn to love it here at B&R!"
ca "Podobnie jak uczniowie przed Tobą i przyszli uczniowie, tutaj w B&R nauczysz się to kochać!"
#ca "So, see each day as a new opportunity and study hard to fulfill your dreams."
ca "Postrzegaj więc każdy dzień jako nową szansę i ucz się ciężko, aby spełnić swoje marzenia."
stop music fadeout 5
#ca "Any questions?"
ca "Czy masz jakieś pytania?"
scene d1_tour1 with dissolve
#ca "Yes, you again...the shirtless one..."
ca "Tak, znowu ty...ten bez koszuli..."
play music "music/ep1/energetic.mp3"
scene d1_tour5 with dissolve
#de "When does this tour get interesting?"
de "Kiedy ta wycieczka staje się interesująca?"
scene d1_tour3 with dissolve
#ca "Young man, you are free to leave if you don't wish to hear about the campus history."
ca "Młody człowieku, możesz odejść, jeśli nie chcesz słuchać o historii kampusu."
scene d1_tour5 with dissolve
#de "It just seems so weird that you would spend all this time talking about some dead dudes..."
de "Po prostu wydaje się to takie dziwne, że spędzasz cały ten czas rozmawiając o jakichś martwych kolesiach..."
#de "...when you could tell us where to buy liquor and where the best parties are at."
de "...kiedy możesz nam powiedzieć, gdzie kupić alkohol i gdzie są najlepsze imprezy."
scene d1_tour3 with dissolve
#ca "Alcohol is strictly forbidden on campus grounds!"
ca "Alkohol jest surowo zabroniony na terenie kampusu!"
scene d1_tour5 with dissolve
#de "Define campus grounds."
de "Zdefiniuj teren kampusu."
scene d1_tour5b with dissolve
#ca "This is campus grounds. Where you live and study."
ca "To teren kampusu. Gdzie mieszkasz i studiujesz."
scene d1_tour5c with dissolve
#de "You really should put that in the brochure."
de "Naprawdę powinieneś umieścić to w broszurze."
#de "I feel cheated."
de "Czuję się oszukana."
scene d1_tour6 with dissolve
#de "Don't you feel cheated?"
de "Nie czujesz się oszukany?"
scene d1_tour3 with dissolve
#ca "If we find you in possession of alcohol or narcotics on campus grounds, there will be repercussions."
ca "Jeśli znajdziemy Cię w posiadaniu alkoholu lub narkotyków na terenie kampusu, poniesiesz konsekwencje."
#de "Narcotics, too!?"
de "Narkotyki też!?"
stop music fadeout 3
scene d1_tour7b with dissolve
$ bios_derek = True
$ bios_cathy = True
$ bios_name_derek = True
$ bios_name_cathy = True
$ chat_new_bios = True
#ca "And we're walking!"
ca "I idziemy!"
play music "music/ep1/art_nouveau.mp3"
scene d1_tour8 with wipeleft
#ca "In this building you'll find each lecture hall and classroom; there are maps on the walls if you ever get lost."
ca "W tym budynku znajdziesz każdą salę wykładową i klasę; na ścianach znajdują się mapy, jeśli kiedykolwiek się zgubisz."
#mc "(The maps suck...)"
mc "(Mapy są do bani...)"
#ca "And this college is filled with helpful students."
ca "A ta uczelnia jest pełna pomocnych studentów."
play sound "sound_effects/hit.mp3"
scene d1_tour9 with hpunch
$ renpy.pause()
scene d1_tour9b with dissolve
#dw "Eat shit, Cathy!"
dw "Jedz gówno, Cathy!"
scene d1_tour10 with dissolve
#sec "Stop right there!"
sec "Stój!"
scene d1_tour11 with dissolve
#ca "Ah, yes. Our campus security is always vigilant and close by to help you if you need it."
ca "Ach, tak. Nasza ochrona kampusu jest zawsze czujna i w pobliżu, aby pomóc Ci, jeśli tego potrzebujesz."
scene d1_tour12 with wiperight
$ renpy.sound.set_volume(0.7,channel='sfx1')
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
#ca "Here is the campus cafeteria."
ca "Tutaj znajduje się stołówka kampusowa."
#ca "Most students come here to buy their lunch or afternoon snack."
ca "Większość uczniów przyjeżdża tutaj, aby kupić lunch lub popołudniową przekąskę."
scene d1_tour13 with dissolve
#ca "And that is the end of our tour."
ca "I to jest koniec naszej wycieczki."
#ca "Just in time for lunch."
ca "W samą porę na lunch."
#ca "I suggest that you eat your lunch here and then we'll meet up in classroom 5K, at 1 p.m."
ca "Sugeruję, abyś zjadł lunch tutaj, a następnie spotkamy się w klasie 5K, o 13:00."
$ guideSuggestedPage = 33
scene d1_lunch with dissolve
#mc "(Students already seem to be bonding.)"
mc "(Uczniowie już wydają się zacieśniać więzi.)"
#mc "(I hate this...)"
mc "Nienawidzę tego!"
#mc "(I'm not good at initiating chats with new people...)"
mc "(Nie jestem dobry w inicjowaniu rozmów z nowymi ludźmi...)"
#mc "(Maybe I'll sit down over there.)"
mc "(Może usiądę tam.)"
scene d1_lunch1b with dissolve
#mc "(This food looks disgusting...)"
mc "(To jedzenie wygląda obrzydliwie...)"
#mc "(It's like someone put minimal effort into making it...)"
mc "(To tak, jakby ktoś włożył w to minimalny wysiłek...)"
scene d1_lunch2 with dissolve
$ renpy.pause()
scene d1_lunch2b with dissolve
menu:
#    "Introduce yourself":
    "Przedstawiamy się":
        $ introducedSage = True
        $ dk(-1)
#        mc "Hi! I'm [name]."
        mc "Cześć, jestem (imię). "
#    "Say nothing":
    "# Nic nie mów. ":
        $ introducedSage = False
#        mc "..."
        mc "..."
stop music fadeout 3
scene d1_lunch3 with dissolve
#sa "..."
sa "..."
$ renpy.sound.stop(channel="sfx1", fadeout=None)
play music "music/ep1/food_chain_short.mp3"
scene d1_lunch4 with vpunch
#ch "What the fuck, Sage!"
ch "Co do kurwy, Sage!"
#ch "I wasn't done talking to you!"
ch "Nie skończyłem z tobą rozmawiać!"
#mc "(Whoa, that's a huge dude.)"
mc "(Wow, to wielki koleś.)"
scene d1_lunch5 with dissolve
#sa "For the last time, Chad..."
sa "Po raz ostatni, Chad..."
#sa "FUCK OFF!!!"
sa "Odpieprz się"
menu:
#    "Intervene":
    "Interweniować":
        $ intervenedChad = True
        $ RPjocks -= 1
        $ RPsage += 1
        scene d1_lunch7 with dissolve
        if dtype > 0:
#            mc "Hey, juicehead! Let go of her."
            mc "Hej, głąbie! Puść ją."
        else:
#            mc "Hey, let go of her! You're hurting her."
            mc "Hej, puść ją! Krzywdzisz ją."
        scene d1_lunch8 with dissolve
#        ch "This doesn't concern you."
        ch "To mnie nie dotyczy."
        menu:
            "Shove him ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
                $ dk(1)
#                $ bios_history_chad = "I shoved Chad to defend Sage.\n\n"
                $ bios_history_chad = "Popchnąłem Chada, by bronił Sage.\n \n"
                $ bios_name_chad = True
                $ chat_new_bios = True
                play sound "sound_effects/shove.mp3"
                scene d1_lunch9c with vpunch
                $ renpy.pause()
#                jc "FRESHY FIGHT!"
                jc "FRESHY FIGHT!"
                scene d1_lunch10d with dissolve
#                ch "WHAT THE FUCK!?"
                ch "Co do kurwy?"
#            "Call security":
            "Wezwij ochronę. ":
                $ dk(-1)
#                $ bios_history_chad = "I called campus security on Chad to defend Sage.\n\n"
                $ bios_history_chad = "Zadzwoniłem do ochrony kampusu w Czadzie, aby bronić Sage.\n \n"
                $ bios_name_chad = True
                $ chat_new_bios = True
#                mc "Hey, security!"
                mc "Hej, ochrona!"
        scene d1_lunch9b with dissolve
#        sec "What is going on here?"
        sec "Co się tu dzieje?"
        if dtype>0:
#            mc "Ask this asshole that question?"
            mc "Zadać temu dupkowi to pytanie?"
        else:
#            mc "Ask this guy that question?"
            mc "Zadać temu facetowi to pytanie?"
        scene d1_lunch10 with dissolve
#        ch "Pff..."
        ch "Pff..."
#    "Keep quiet":
    "Siedzieć cicho.":
#        $ bios_history_chad = "I didn't intervene when Chad argued with Sage.\n\n"
        $ bios_history_chad = "Nie interweniowałem, gdy Chad pokłócił się z Sage.\n \n"
        $ bios_name_chad = True
        $ chat_new_bios = True
        $ intervenedChad = False
#        mc "..."
        mc "..."
        scene d1_lunch9 with dissolve
#        sec "What is going on here?"
        sec "Co się tu dzieje?"
        scene d1_lunch10b with dissolve
#        ch "Pff..."
        ch "Pff..."
stop music fadeout 3
scene d1_lunch11 with dissolve
#sa "..."
sa "..."
$ renpy.sound.set_volume(0.7,channel='sfx1')
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
play music "music/ep1/funk_rock.mp3"
if intervenedChad:
    scene d1_lunch11b with dissolve
    if introducedSage:
#        sa "Thanks, [name]."
        sa "Dziękujemy,"
    else:
#        sa "Thanks..."
        sa "Dzięki!"
else:
#    mc "Are you ok?"
    mc "Wszystko dobrze?"
    scene d1_lunch11c with dissolve
#    sa "Found your voice?"
    sa "Znalazłeś swój głos?"
    scene d1_lunch11b with dissolve
#    sa "...I'm fine."
    sa "Nic mi nie jest. "
scene d1_lunch11 with dissolve
#mc "Sage, huh?"
mc "Szałwia, co?"
menu:
#    "Joke about her name":
    "Żart o jej imieniu":
        $ dk(1)
#        mc "As in the herb or the color?"
        mc "Jak w ziole czy w kolorze?"
        scene d1_lunch11d with dissolve
#        sa "Ugh..."
        sa "Umm..."
        scene d1_lunch11 with dissolve
#        mc "Just trying to cheer you up..."
        mc "Próbuję cię tylko rozweselić..."
#    "Pretty name":
    "Ładne imię.":
        $ dk(-1)
#        mc "That's a pretty name."
        mc "Piękne imię. "
if not introducedSage:
#    mc "I'm [name]."
    mc "i. m."
#mc "What was that about?"
mc "Uh, o co chodziło?"
scene d1_lunch14 with dissolve
#sa "Just a stupid argument with my even stupider boyfriend."
sa "Tylko głupia kłótnia z moim jeszcze głupszym chłopakiem."
scene d1_lunch14b with dissolve
#sa "He thinks he's so fucking smart that he can hide that he's cheating on me!"
sa "Myśli, że jest tak cholernie mądry, że może się ukryć, że mnie zdradza!"
scene d1_lunch15 with dissolve
#sa "I fucking found the panties in his gym bag!"
sa "Kurwa, znalazłem majtki w jego torbie na siłownię!"
#sa "And he told me that he bought them for me."
sa "I powiedział mi, że kupił je dla mnie."
#sa "Can you believe that?"
sa "Uwierzycie?"
scene d1_lunch11 with dissolve
menu:
#    "Maybe he did?":
    "Może to zrobił?":
#        mc "Maybe he's telling the truth?"
        mc "Może mówi prawdę?"
        scene d1_lunch11c with dissolve
#        sa "New panties don't reek of perfume."
        sa "Nowe majtki nie cuchną perfumami."
#        mc "Oh..."
        mc "Och..."
#    "That's bullshit":
    "Gówno prawda!":
        $ dk(-1)
#        mc "It does sound like a bullshit story."
        mc "Brzmi to jak gówniana historia."
scene d1_lunch11d with dissolve
#sa "He's so full of shit."
sa "Pieprzy bzdury."
scene d1_lunch11 with dissolve
#$ bios_history_sage = "I met Sage today. She seems to have relationship issues with her jock boyfriend Chad.\n\n"
$ bios_history_sage = "Spotkałem dziś Sage. Wygląda na to, że ma problemy ze swoim sportowym chłopakiem Chadem.\n \n"
$ bios_name_sage = True
$ chat_new_bios = True
menu:
#    "Tell a joke":
    "powiedz kawał":
        if dtype > 0:
#            mc "And steroids. Evidently, they shrink both dick and brains."
            mc "I sterydy. Najwyraźniej kurczą zarówno penisa, jak i mózg."
            scene d1_lunch17b with dissolve
#            sa "Haha..."
            sa "Haha"
            $ RPsage += 1
#            $ bios_history_sage += "I told her a joke and she laughed.\n\n"
            $ bios_history_sage += "Opowiedziałem jej dowcip, a ona się zaśmiała.\n \n"
            $ bios_name_sage = True
            $ chat_new_bios = True
        else:
#            mc "Full of shit? Well, he does smell worse than the lunch at this place."
            mc "Pełen gówna? Cóż, śmierdzi gorzej niż lunch w tym miejscu."
            scene d1_lunch17c
#            ll "RUDE!!!"
            ll "Nieprawidłowy"
            $ ep1_insulted_cafeteria_worker = True
#            $ bios_history_sage += "I told her a joke but ended up insulting the cafeteria workers.\n\n"
            $ bios_history_sage += "Opowiedziałem jej dowcip, ale skończyło się na tym, że obraziłem pracowników stołówki.\n \n"
#            $ bios_history_beth += "I told Sage a joke but ended up insulting Beth.\n\n"
            $ bios_history_beth += "Opowiedziałem Sage dowcip, ale skończyłem obrażając Beth.\n \n"
            $ bios_name_sage = True
            $ chat_new_bios = True
#    "Don't push it":
    "Dobra, nie przeginaj.":
        $ renpy.pause(0.2)
$ guideSuggestedPage = 34
scene d1_lunch11 with dissolve
menu:
#    "Why do you date him?":
    "Dlaczego się z nim spotykasz?":
#        mc "Then why do you date him?"
        mc "To dlaczego się z nim spotykasz?"
        scene d1_lunch19 with dissolve
#        sa "Mind your own fucking business."
        sa "Pilnuj swojego pieprzonego nosa."
        if dtype > 0:
            scene d1_lunch19b with dissolve
#            mc "Drop that fucking attitude; I was only caring."
            mc "Odpuść sobie tę pieprzoną postawę; ja tylko się troszczyłem."
            scene d1_lunch11 with dissolve
#            sa "..."
            sa "..."
            scene d1_lunch19d with dissolve
#            sa "Sorry."
            sa "Przepraszamy. Aby zapobiec spamowi, URL są niedozwolone w wiadomościach."
            scene d1_lunch11 with dissolve
            $ RPsage += 1
#            $ bios_history_sage += "I was dominant with her when she got offended. She liked that.\n\n"
            $ bios_history_sage += "Dominowałem nad nią, kiedy poczuła się urażona. Spodobało jej się to.\n \n"
            $ bios_name_sage = True
            $ chat_new_bios = True
        else:
            $ RPsage -= 1
#            $ bios_history_sage += "She got offended when I asked her about Chad.\n\n"
            $ bios_history_sage += "Obraziła się, gdy zapytałem ją o Chada.\n \n"
            $ bios_name_sage = True
            $ chat_new_bios = True
            scene d1_lunch11 with dissolve
#    "Don't inquire":
    "Nie pytaj":
        scene d1_lunch11 with dissolve
#sa "..."
sa "..."
scene d1_lunch19d with dissolve
#sa "I haven't seen you around before. So, what are you? A freshman?"
sa "Nie widziałem cię wcześniej. Więc kim jesteś? Pierwszoroczniakiem?"
scene d1_lunch11 with dissolve
#mc "What gave it away?"
mc "Co go zdradziło?"
scene d1_lunch19d with dissolve
#sa "You sit here and eat all alone, but you don't look like someone who would."
sa "Siedzisz tu i jesz sam, ale nie wyglądasz na kogoś, kto by to zrobił."
scene d1_lunch11 with dissolve
menu:
#    "That's superficial":
    "To powierzchowne":
        $ RPsage -= 1
#        $ bios_history_sage += "She got offended when I called her superficial.\n\n"
        $ bios_history_sage += "Obraziła się, gdy nazwałem ją powierzchowną.\n \n"
        $ bios_name_sage = True
        $ chat_new_bios = True
#        mc "That's very superficial."
        mc "To bardzo powierzchowne."
        scene d1_lunch11d with dissolve
#        sa "Whatever."
        sa "Kogo to obchodzi."
        scene d1_lunch23 with dissolve
#    "No friends yet":
    "Nie ma jeszcze znajomych":
#        mc "Yeah, I haven't made any friends yet."
        mc "Tak, jeszcze się nie zaprzyjaźniłam."
        scene d1_lunch23 with dissolve
#        sa "Well, that sucks."
        sa "No to huj. "
#sa "Which frat are you pledging?"
sa "Do którego bractwa przystępujesz?"
scene d1_lunch23b with dissolve
#mc "Oh...I don't know if I will pledge."
mc "Och... nie wiem, czy się przyrzeknę."
scene d1_lunch23c with dissolve
#sa "Come on, you gotta pledge!"
sa "No dalej, musisz się zobowiązać!"
#sa "You're going to miss out on a lot of parties otherwise."
sa "W przeciwnym razie ominie Cię wiele imprez."
scene d1_lunch23b with dissolve
#mc "Well, I came here to study."
mc "Cóż, przyjechałem tu studiować."
scene d1_lunch11d with dissolve
#sa "Ugh. Then you should pledge the tri-betas; that's all they do."
sa "Ugh. Więc powinieneś zadeklarować tri-beta; to wszystko, co robią."
scene d1_lunch11 with dissolve
#mc "(Hm...it could be worth checking them out at least.)"
mc "(Hm...warto je przynajmniej sprawdzić.)"
#mc "Since you seem to like parties..."
mc "Ponieważ wydaje się, że lubisz imprezy..."
#mc "I'm guessing you're in the Eta Omicron Tau sorority."
mc "Zgaduję, że jesteś w bractwie Eta Omicron Tau."
scene d1_lunch31 with dissolve
#sa "In it? I'm the sorority president."
sa "W nim? Jestem prezesem bractwa."
#sa "You do know that we just call it HOT, right?"
sa "Wiesz, że nazywamy to po prostu GORĄCYM, prawda?"
scene d1_lunch11 with dissolve
#mc "Ok..."
mc "Dobrze..."
scene d1_lunch33 with dissolve
$ bios_chad = True
$ bios_sage = True
$ bios_name_sage = True
$ bios_name_chad = True
$ chat_new_bios = True
if intervenedChad:
#    sa "I gotta run. Thanks for the help back there."
    sa "Muszę lecieć. Dzięki za pomoc."
else:
#    sa "I gotta run. Bye."
    sa "Muszę lecieć. Pa."
menu:
#    "Check her out":
    "Patrz na nią. ":
        $ dk(1)
        stop music fadeout 3
        scene d1_lunch33b with dissolve
        if dtype > 0:
#            mc "(Nice ass...)"
            mc "wodna dupa"
        else:
#            mc "(She's very pretty.)"
            mc "(Jest bardzo ładna.)"
#    "Don't push your luck":
    "--- ":
        $ dk(-1)
        stop music fadeout 3
scene d1_derek1 with dissolve
#de "Holy fuck!"
de "- O kurwa! "
play music "music/ep1/energetic.mp3"
scene d1_derek2 with dissolve
#de "Hey, bro! Did you see the tits on that one?"
de "Hej, brachu! Widziałeś na tym cycki?"
scene d1_derek2b with dissolve
#$ bios_history_derek = "Derek seems to be a party guy. Dude seems to have lost his shirt somewhere.\n\n"
$ bios_history_derek = "Derek wydaje się być imprezowiczem. Wygląda na to, że koleś gdzieś zgubił koszulkę.\n \n"
$ bios_name_derek = True
$ chat_new_bios = True
menu:
#    "Banter":
    "Drażnić":
        $ dk(1)
        $ assman = True
#        mc "Tits? I was looking at her ass."
        mc "Cycki? Patrzyłem na jej tyłek."
        scene d1_derek4 with dissolve
#        de "Aha! An ass man."
        de "Aha! Człowiek-dupek."
#        de "I would never have guessed."
        de "Nigdy bym tego nie zgadła. "
#        $ bios_history_derek += "Derek started calling me ass man, today... I don't know if I like that nickname.\n\n"
        $ bios_history_derek += "Derek zaczął mnie dzisiaj nazywać dupkiem... Nie wiem, czy podoba mi się ta ksywka.\n \n"
        $ bios_name_derek = True
        $ chat_new_bios = True
#    "Defend her":
    "Bronić jej":
        $ dk(-1)
        $ assman = False
#        mc "That's pretty rude, dude."
        mc "To było niegrzeczne, stary."
        scene d1_derek4b with dissolve
#        de "Thanks!"
        de "Dziękujemy! Twój komentarz został wysłany."
scene d1_derek2b with dissolve
#mc "..."
mc "..."
#mc "Where's your shirt?"
mc "Gdzie twoja koszulka?&#10;"
scene d1_derek6 with dissolve
#de "I know! Right?"
de "I know, right?"
#de "I probably lost it."
de "Pewnie mi odbiło."
scene d1_derek2 with dissolve
if intervenedChad:
#    de "You almost gave it to that jock, huh?"
    de "Prawie dałeś go temu sportowcowi, co?"
else:
#    de "Man, I gotta say I wished for you to stand up to that Belgian Blue lookin' motherfucker."
    de "Człowieku, muszę powiedzieć, że chciałem, żebyś przeciwstawił się temu skurwysynowi wyglądającemu na Belgian Blue."
scene d1_derek2b with dissolve
if intervenedChad:
#    mc "Yeah...almost."
    mc "Tak...prawie."
    scene d1_derek2 with dissolve
#    de "He would have crushed you, though."
    de "Ale i tak by cię zmiażdżył."
    scene d1_derek2b with dissolve
else:
#    mc "Did you see the size of him?"
    mc "Widziałeś jego rozmiar?"
#mc "I know how to fight, but I really don't want to make enemies."
mc "Wiem, jak walczyć, ale naprawdę nie chcę robić sobie wrogów."
scene d1_derek7 with dissolve
#de "Come on, don't say that! Beating up a jock would grant you instant access to join the DIKs!"
de "Daj spokój, nie mów tak! Pobicie atleta dałoby Ci natychmiastowy dostęp do dołączenia do DIK!"
scene d1_derek8 with dissolve
#mc "Yeah, I don't think I want to join the DIKs."
mc "Tak, chyba nie chcę dołączyć do DIK-ów."
scene d1_derek9 with dissolve
#de "Dude, are you crazy!? I just talked to some students..."
de "Koleś, zwariowałeś!? Właśnie rozmawiałem z kilkoma studentami..."
#de "The DIKs is where it's at, bro! They throw the best parties, and lately, they've been partying a lot with the HOTs."
de "DIK jest tam, gdzie jest, brachu! Urządzają najlepsze imprezy, a ostatnio dużo imprezują z HOTami."
scene d1_derek8 with dissolve
#mc "Really? I thought the HOTs were tri-alpha's sorority."
mc "Naprawdę? Myślałem, że hot to bractwo tri-alfa."
scene d1_derek9 with dissolve
#de "And that's why you would have gotten that golden ticket to the DIKs by beating that jock up."
de "I dlatego zdobyłbyś ten złoty bilet do DIK-ów, bijąc tego dżokeja."
scene d1_derek8 with dissolve
#mc "Well, if you wanna be in that fraternity so much, why don't you beat up a jock?"
mc "Cóż, jeśli tak bardzo chcesz być w tym bractwie, dlaczego nie pobijesz sportowca?"
scene d1_derek7 with dissolve
#de "Dude...look at me. I'm not a fighter."
de "Stary...spójrz na mnie. Nie jestem wojownikiem."
#de "I'm a lover and a gentleman."
de "Jestem kochankiem i dżentelmenem."
scene d1_derek13 with dissolve
#de "Holy fuck! Would you look at the milk machines on that one!"
de "Jasna cholera! Spójrzcie na te automaty z mlekiem!"
scene d1_derek_jade1 with dissolve
$ renpy.pause()
scene d1_derek_jade with dissolve
#de "What do you say, bro!?"
de "Co ty na to, brachu!?"
menu:
#    "Just my type":
    "W moim typie":
#        $ bios_history_derek += "I told him that I like busty women.\n\n"
        $ bios_history_derek += "Powiedziałam mu, że lubię cycate kobiety.\n \n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ preferredmilf = 0
        scene d1_derek_jade2 with dissolve
        if dtype > 0:
#            mc "Yeah, that's just how I like them."
            mc "Tak, po prostu tak lubię."
#            de "{i}Them{/i} as in titties or women?"
            de "{i}Oni{/i} jak w cyckach czy kobietach?"
#            mc "Why not both?"
            mc "Dlaczego nie jedno i drugie?"
            if assman:
#                de "Haha! So, you're not just an ass man, then?"
                de "Haha! Więc nie jesteś tylko dupkiem?"
            else:
#                de "Haha!"
                de "Ha, ha!"
        else:
#            mc "She sure is beautiful."
            mc "Z pewnością jest piękna."
#    "I prefer Cathy":
    "Wolę Cathy":
#        $ bios_history_derek += "I told him that I prefer women like Cathy.\n\n"
        $ bios_history_derek += "Powiedziałam mu, że wolę kobiety takie jak Cathy.\n \n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        scene d1_derek_cathy with dissolve
        $ preferredmilf = 1
        if dtype > 0:
#            mc "Nah, milfs like Cathy are much more my style."
            mc "Nie, mamuśki takie jak Kasia są bardziej w moim stylu."
            if assman:
#                de "An ass man and a dyke lover, huh?"
                de "Dupowłaz i miłośnik lesb, co?"
#                mc "Haha, fuck you!"
                mc "Haha, pierdol się!"
        else:
#            mc "For older women, I'd prefer someone like Cathy."
            mc "Dla starszych kobiet wolałbym kogoś takiego jak Kasia."
#            de "Flat and boring, huh? Got it."
            de "Płaski i nudny, co? Jasne."
scene d1_derek10 with dissolve
#de "Anyway, so you're not planning on pledging the DIKs?"
de "W każdym razie, więc nie planujesz wspierać DIK-ów?"
#de "Think about it! Their parties are next level!"
de "Pomyśl o tym! Ich imprezy są na wyższym poziomie!"
scene d1_derek8 with dissolve
#mc "Well, as I said to Sage just now, I came here to study, not to party."
mc "Cóż, jak powiedziałem przed chwilą Sage, przyjechałem tu się uczyć, a nie imprezować."
scene d1_derek10b with dissolve
#de "Oh yeah. Sure, sure. Me too."
de "O tak. Jasne, jasne. Ja też."
scene d1_derek8 with dissolve
#mc "Really?"
mc "Serio?"
scene d1_derek10b with dissolve
#de "No."
de "l.p."
#de "I'm just here for the pussy."
de "Jestem tu tylko dla cipki."
scene d1_derek8 with dissolve
#mc "At least you're honest."
mc "Przynajmniej jesteś szczery."
scene d1_derek14 with dissolve
$ number_derek = True
#de "Here take my number."
de "Proszę, weź mój numer."
#de "Hit me up if you change your mind!"
de "Odezwij się, jeśli zmienisz zdanie!"
$ renpy.sound.stop(channel="sfx1", fadeout=3)
stop music fadeout 3
if assman:
#    de "See ya later, ass man!"
    de "Do zobaczenia, dupku!"
else:
#    de "See ya later, dude!"
    de "Na razie, stary!"
#$ bios_history_derek += "Derek wants me to pledge the DIKs with him.\n\n"
$ bios_history_derek += "Derek chce, żebym dołączył do DIK-ów.\n \n"
$ bios_name_derek = True
$ chat_new_bios = True
play music "music/ep1/someways.mp3"
scene d1_class with wipeleft
#de "So, you're going to do it or what?"
de "To co, zrobisz to czy nie?"
scene d1_class_b with dissolve
#my "In your dreams!"
my "W Twoich snach!"
$ renpy.sound.set_volume(1.0,channel='sfx1')
scene d1_class_c with dissolve
#de "Aw, come on! Why not?"
de "Och, daj spokój! Dlaczego nie?"
scene d1_class_b with dissolve
#my "Just because I'm pledging, I'm not going to hook you up with HOT chicks."
my "Tylko dlatego, że jestem kandydatką, nie będę cię umawiać z GORĄCYMI laskami."
scene d1_class_c with dissolve
#de "Not cool. Not cool at all."
de "Niefajnie. Niefajnie."
scene d1_class_e with dissolve
#de "Hey, bro. Don't try your luck with that one. Total cockblock."
de "Hej, brachu. Nie próbuj szczęścia z tym. Totalny chuj."
menu:
#    "Get mad":
    "Wściekaj się":
#        $ bios_history_derek += "I called Derek out when he called Maya a cockblock.\n\n"
        $ bios_history_derek += "Wyzwałem Dereka, kiedy nazwał Mayę kutasem.\n \n"
        $ bios_name_derek = True
        $ chat_new_bios = True
        $ RPderek -= 1
        scene d1_class_g with dissolve
#        mc "Don't fucking talk about her like that!"
        mc "Nie mów tak o niej!"
#        de "Bro...relax. It's cool."
        de "Stary...wyluzuj. Spoko."
        scene d1_class_i with dissolve
#    "Ignore him":
    "Ignoruj go.":
        scene d1_class_i with dissolve
$ guideSuggestedPage = 35
menu:
#    "Check her out":
    "Patrz na nią. ":
        $ dk(1)
        $ RPmaya -= 1
        scene d1_class_j2 with dissolve
        $ renpy.pause()
        scene d1_class_j3 with dissolve
#        $ bios_history_maya += "Maya caught me staring at her panties... I'm sure she didn't appreciate that.\n\n"
        $ bios_history_maya += "Maya przyłapała mnie na gapieniu się na jej majtki... Jestem pewien, że nie doceniła tego.\n \n"
        $ chat_new_bios = True
#        my "Hey, [name]..."
        my "Hej... "
        scene d1_class_j4 with dissolve
#        mc "Hey!"
        mc "Hej!"
#    "Say hi":
    "Przywitaj się":
        $ dk(-1)
#        mc "Hey, Maya. Thanks again for the tour."
        mc "Hej, Maya. Jeszcze raz dzięki za oprowadzenie."
        scene d1_class_j with dissolve
#        my "No sweat."
        my "No sweat."
        scene d1_class_l with dissolve
#mc "What have you been up to?"
mc "Coś robił do tej pory?"
scene d1_class_j with dissolve
#my "I went to the HOTs and chatted with Quinn about pledging."
my "Poszedłem do HOTs i rozmawiałem z Quinn o składaniu deklaracji."
#my "She wasn't totally against it."
my "Nie była temu całkowicie przeciwna."
#my "So, now I'll have to wait for her to call on me."
my "Więc teraz będę musiał poczekać, aż mnie odwiedzi."
scene d1_class_l with dissolve
#mc "Who's Quinn?"
mc "Kim jest Quinn?"
scene d1_class_j with dissolve
#my "The vice president of HOT. A total hardass."
my "Wiceprezes HOT. Twarda sztuka."
scene d1_class_l with dissolve
#mc "I see you've met Derek..."
mc "Widzę, że poznałaś Dereka..."
scene d1_class_n with dissolve
#my "Haha, met him? No, we-"
my "Haha, spotkałaś go? Nie, my-"
#ca "Simmer down, students. It's time to start."
ca "Uspokójcie się uczniowie. Czas zacząć."
#$ bios_history_derek += "Maya and Derek seem to have a history.\n\n"
$ bios_history_derek += "Wydaje się, że Maya i Derek mają wspólną historię.\n \n"
#$ bios_history_maya += "Maya and Derek seem to have a history.\n\n"
$ bios_history_maya += "Wydaje się, że Maya i Derek mają wspólną historię.\n \n"
$ bios_name_derek = True
$ bios_name_maya = True
$ chat_new_bios = True
scene d1_class_j with dissolve
#my "Let's chat later, ok?"
my "Pogadamy później, dobrze?"
scene d1_class_p with dissolve
#ca "Welcome to your first class."
ca "Witamy na pierwszych zajęciach."
#ca "During your freshman year, there are a lot of courses that we recommend you take."
ca "Na pierwszym roku nauki polecamy wiele kursów."
#ca "Most courses are general education courses and, well...our selection is...limited."
ca "Większość kursów to kursy ogólnokształcące i, no...nasz wybór jest...ograniczony."
$ englishPresented = True
show screen skillmsg
#ca "For the English credits, most students sign up for this class, named \"Writing and Communication\"..."
ca "Aby uzyskać punkty w języku angielskim, większość uczniów zapisuje się na te zajęcia o nazwie \"Pisanie i komunikacja\"..."
#ca "...and for the mathematics credits, \"Gen. Ed. Mathematics\" is the most common choice."
ca "...oraz za zaliczenia z matematyki, \"Gen. Ed. Matematyka\" jest najczęstszym wyborem."
#ca "In both of which, I'm the teacher."
ca "W obu przypadkach jestem nauczycielem."
hide screen skillmsg
scene d1_class1bb with dissolve
#ca "If you haven't signed up for all classes yet, I'd recommend you all to do it this week."
ca "Jeśli nie zapisaliście się jeszcze na wszystkie zajęcia, polecam zrobić to w tym tygodniu."
#ca "But today, we're here to start mastering the English language in writing and communication."
ca "Ale dzisiaj jesteśmy tutaj, aby zacząć opanowywać język angielski na piśmie i w komunikacji."
scene d1_class2 with dissolve
#ca "As a standard, I start each freshman year with a couple of tests."
ca "Standardowo zaczynam każdy pierwszy rok od kilku testów."
#de "BOOH!!!"
de "BOOH!!!"
scene d1_class1bb with dissolve
#ca "Now, now. Don't be scared."
ca "Nie bój się."
#ca "These tests will not count toward your final grades."
ca "Testy te nie będą wliczane do Twoich ocen końcowych."
#ca "They're just tests that will show me what level you all are on."
ca "To tylko testy, które pokażą mi, na jakim poziomie jesteście."
scene d1_class2 with dissolve
#ca "You may begin."
ca "Możesz zaczynać. "
#$ bios_history_cathy = "Cathy is going to be my English and Math teacher.\n\n"
$ bios_history_cathy = "Cathy będzie moją nauczycielką angielskiego i matematyki.\n \n"
$ bios_name_cathy = True
$ chat_new_bios = True
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep1_after_english_test
if tutorials:
    scene english_tutorial1 with wipeleft
    $ renpy.pause()
    scene english_tutorial2 with dissolve
    $ renpy.pause()
    scene english_tutorial3 with dissolve
    $ renpy.pause()
else:
    stop music fadeout 3
    $ renpy.pause(3)
play music "music/ep3/sing_along_with_jim.mp3"
scene english_test_board
jump english101_test1
label ep1_after_english_test:

$ renpy.block_rollback()
if minigames:
    scene d1_class2 with wiperight
    stop music fadeout 3
else:
    scene d1_class2 with fade
#ca "Pencils down, class."
ca "Ołówki w dół, klasa."
#ca "Please turn in your tests."
ca "Zwróć swoje testy."
scene d1_class1bb with dissolve
if minigames:
    play music "music/ep1/someways.mp3"
#ca "We're done for today."
ca "Skończyliśmy na dzisiaj."
#ca "Please spend the remainder of the day getting acquainted with each other."
ca "Prosimy o spędzenie reszty dnia na zapoznawaniu się ze sobą."
#ca "For those of you who are taking Gen. Ed. Mathematics, we'll meet here again tomorrow morning."
ca "Dla tych z was, którzy biorą Gen. Ed. Matematyka, spotkamy się tu ponownie jutro rano."
#ca "Class dismissed."
ca "Klasa zwolniona."
scene d1_class8 with dissolve
#mc "Hey, Maya. How did it go?"
mc "Hej, Maya. Jak poszło?"
#my "I think it went all right."
my "Myślę, że poszło dobrze."
#my "So, what are you up to?"
my "- Co porabiasz?"
scene d1_class9 with dissolve
#mc "I'm going to check out the tri-beta fraternity."
mc "Sprawdzę bractwo tri-beta."
#mc "Wanna come with me?"
mc "Chcesz iść ze mną?"
scene d1_class10 with dissolve
#my "Sorry, I can't. I need to call my boyfriend."
my "Przepraszam, nie mogę. Muszę zadzwonić do mojego chłopaka."
menu:
#    "Ask about boyfriend":
    "Zapytaj o chłopaka":
#        mc "Oh, you have a boyfriend?"
        mc "Aha, masz chłopaka?"
        scene d1_class13 with dissolve
#        my "Yes. I gotta go."
        my "Muszę lecieć."
#    "Leave it alone":
    "Zostaw ją!":
#        mc "Ok, have fun."
        mc "Ok, baw się dobrze."
#mc "(That was weird...)"
mc "To było dziwne."
#$ bios_history_maya += "Maya told me she has a boyfriend. Everyone seems to be spoken for around here...\n\n"
$ bios_history_maya += "Maja powiedziała mi, że ma chłopaka. Wydaje się, że wszyscy są tu przemawiani...\n \n"
$ bios_name_maya = True
$ chat_new_bios = True
stop music fadeout 3
scene d1_tribeta with fade
#mc "(If I recall correctly, the library is this way...)"
mc "(Jeśli dobrze pamiętam, biblioteka jest w tę stronę...)"
scene d1_tribetab with dissolve
#dw "Hey, Chad, there he is!"
dw "Jest."
#an "So, what are you going to do?"
an "To co zrobicie?"
if intervenedChad:
    play music "music/ep1/credits.mp3"
    play sound "sound_effects/hit.mp3"
    scene d1_tribetac with hpunch
    jcs "Hahaha!"
    scene d1_tribetad with dissolve
#    mc "Hey, what the hell!?"
    mc "Co do cholery?"
#    ch "You got a problem there, tattletale?"
    ch "Jakiś problem, donosicielu?"
#    an "Hehe. Yeah!"
    an "Hehe. Tak!"
    scene d1_tribeta3 with dissolve
#    ch "Shut up, Anthony!"
    ch "Zamknij się, Anthony!"
    scene d1_tribeta3b with dissolve
    menu:
#        "Mock him":
        "Nabijaj się z niego":
            $ dk(1)
            $ RPjocks -= 1
#            mc "Tattletale? What are you? In kindergarten?"
            mc "Tattletale? Kim jesteś? W przedszkolu?"
            scene d1_tribeta4 with dissolve
#            an "No, in college!"
            an "Na uczelni nie ma broni! "
#            ch "..."
            ch "..."
            scene d1_tribeta7 with dissolve
#            ch "It seems to me like you're trying to make a move on my girl."
            ch "Wydaje mi się, że próbujesz zaatakować moją dziewczynę."
#        "Calm him down":
        "Uspokój go":
            $ dk(-1)
#            mc "Relax, I have no beef with you."
            mc "Wyluzuj, nic do ciebie nie mam."
            scene d1_tribeta7 with dissolve
#            ch "Really? No beef, he says!"
            ch "Naprawdę? Nie ma wołowiny, mówi!"
#            ch "Because it seems to me like you're trying to make a move on my girl."
            ch "Bo wydaje mi się, że próbujesz poderwać moją dziewczynę."
    $ guideSuggestedPage = 36
    scene d1_tribeta3b with dissolve
#    mc "Who? Sage? You've got it all wrong."
    mc "Kto? Mędrzec? Mylisz się."
    scene d1_tribeta7 with dissolve
#    ch "You do know that campus security can't always be around to save your pretty little ass?"
    ch "Wiesz, że ochrona kampusu nie zawsze może być w pobliżu, aby uratować twój śliczny tyłeczek?"
    scene d1_tribeta3b with dissolve
    menu:
#        "Mock him":
        "Nabijaj się z niego":
            $ dk(1)
            $ RPjocks -= 1
#            mc "Do you think I have a pretty little ass? How gay are you?"
            mc "Myślisz, że mam ładny tyłeczek? Jak bardzo jesteś gejem?"
            scene d1_tribeta11 with dissolve
#            an "Hehe. That sounded pretty gay to me."
            an "Hehe. Dla mnie to brzmiało dość gejowsko."
            play sound "sound_effects/hit.mp3"
            scene d1_tribeta12 with hpunch
#            mc "(Holy shit!)"
            mc "Cholera"
            scene d1_tribeta13 with dissolve
#        "Calm him down":
        "Uspokój go":
            $ dk(-1)
#            mc "Come on; I'm not looking for a fight."
            mc "Daj spokój, nie szukam bójki."
            scene d1_tribeta7 with dissolve
else:
    play music "music/ep1/credits.mp3"
    play sound "sound_effects/hit.mp3"
    scene d1_tribetac with hpunch
    jcs "Hahaha!"
    scene d1_tribetad with dissolve
#    mc "Hey, what the hell!?"
    mc "Co do cholery?"
#    ch "You got a problem there, Prince Charming?"
    ch "Jakiś problem, książę z bajki?"
#    an "Hehe. Yeah! We got a fucking Romeo or something over here."
    an "Hehe. Tak! Mamy tu pieprzonego Romea czy coś."
    scene d1_tribeta3 with dissolve
#    ch "Shut up, Anthony!"
    ch "Zamknij się, Anthony!"
    scene d1_tribeta3b with dissolve
    menu:
#        "Mock him":
        "Nabijaj się z niego":
            $ dk(1)
            $ RPjocks -= 1
#            mc "Did I charm your panties off?"
            mc "Czy oczarowałem twoje majtki?"
            scene d1_tribeta4 with dissolve
#            an "Chad doesn't wear panties."
            an "Chad nie nosi majtek."
#            ch "..."
            ch "..."
            scene d1_tribeta7 with dissolve
#            ch "It seems to me like you're trying to make a move on my girl."
            ch "Wydaje mi się, że próbujesz zaatakować moją dziewczynę."
#        "Calm him down":
        "Uspokój go":
            $ dk(-1)
#            mc "Relax, I have no beef with you."
            mc "Wyluzuj, nic do ciebie nie mam."
            scene d1_tribeta7 with dissolve
#            ch "Really? No beef, he says!"
            ch "Naprawdę? Nie ma wołowiny, mówi!"
#            ch "Because it seems to me like you're trying to make a move on my girl."
            ch "Bo wydaje mi się, że próbujesz poderwać moją dziewczynę."
    scene d1_tribeta3b with dissolve
#    mc "Who? Sage? You've got it all wrong."
    mc "Kto? Mędrzec? Mylisz się."
    $ guideSuggestedPage = 36
    scene d1_tribeta7 with dissolve
#    ch "That's not what Dawe told me. Apparently, you were getting ready to fuck her right there in the cafeteria."
    ch "Dawe powiedział mi co innego. Najwyraźniej przygotowywałeś się do przelecenia jej w stołówce."
    scene d1_tribeta3b with dissolve
    menu:
#        "Mock him":
        "Nabijaj się z niego":
            $ dk(1)
            $ RPjocks -= 1
#            mc "Funny how that is. I could've sworn that it was you trying to fuck her up."
            mc "Zabawne, jak to jest. Mogłabym przysiąc, że to ty próbowałeś ją spierdolić."
            scene d1_tribeta11 with dissolve
#            an "Hehe. That's kind of funny."
            an "Hehe. To trochę śmieszne."
            play sound "sound_effects/hit.mp3"
            scene d1_tribeta12 with hpunch
#            mc "(Holy shit!)"
            mc "Cholera"
            scene d1_tribeta13 with dissolve
#        "Calm him down":
        "Uspokój go":
            $ dk(-1)
#            mc "Come on; I'm not looking for a fight."
            mc "Daj spokój, nie szukam bójki."
            scene d1_tribeta7 with dissolve
#ch "I'll be watching you, freshy."
ch "Będę cię obserwował, świeżutka."
scene d1_tribeta_sage with dissolve
#ch "Stay the fuck away from Sage!"
ch "Trzymaj się z dala od Sage!"
scene d1_tribeta14 with dissolve
#ch "Dawe, here, will show you what happens when you mess with the tri-alphas."
ch "Dawe pokaże ci, co się dzieje, gdy zadzierasz z tri-alfami."
#mc "Huh?"
mc "Hm?"
play sound "sound_effects/wedgie.mp3"
scene d1_tribeta15 with vpunch
#dw "Take this, bitch!"
dw "Weź to, suko!"
#dw "Hehehe!"
dw "He, he, he, he!"
$ bios_anthony = True
$ bios_dawe = True
$ bios_name_anthony = True
$ bios_name_dawe = True
if RPjocks < 0:
#    $ bios_history_chad += "I got into an argument with the jocks over Sage. I didn't get off to a good start with them.\n\n"
    $ bios_history_chad += "Pokłóciłem się ze sportowcami o Sage. Nie zacząłem z nimi dobrze.\n \n"
else:
#    $ bios_history_chad += "I got into an argument with the jocks over Sage. I managed to keep my cool.\n\n"
    $ bios_history_chad += "Pokłóciłem się ze sportowcami o Sage. Udało mi się zachować spokój.\n \n"
#$ bios_history_dawe = "Dawe's an ass. He gave me a wedgie today. I'll remember this.\n\n"
$ bios_history_dawe = "Dawe to dupek. Dał mi dziś koturna. Zapamiętam to.\n \n"
#$ bios_history_anthony = "It's a wonder that this guy got accepted to college, he seems to be a new kind of stupid.\n\n"
$ bios_history_anthony = "To dziwne, że ten facet został przyjęty do college 'u, wydaje się być nowym rodzajem głupka.\n \n"
$ bios_name_chad = True
$ chat_new_bios = True
scene d1_tribeta16 with dissolve
stop music fadeout 5
#mc "(Fucking jocks!)"
mc "(Jebani sportowcy!)"
#uk "Hey! Stop that! You bullies!"
uk "Hej! Przestańcie! Wy łobuzy!"
play music "music/ep1/they_say.mp3"
scene d1_tribeta17 with dissolve
#uk "Are you hurt?"
uk "- Jesteś ranna?"
#mc "No, I'm-"
mc "Nie, ja..."
scene d1_tribeta19
#ty "Jill, we're going to be late."
ty "Spóźnimy się.  "
#ji "Give me a second, Tybalt."
ji "Daj mi chwilę, Tybalt."
scene d1_tribeta21 with dissolve
#mc "I'm ok. Thanks."
mc "Nic mi nie jest. Dzięki."
#mc "This is not the first time in my life I got a wedgie. Haha."
mc "To nie pierwszy raz w moim życiu, kiedy mam ochotę na kotlet. Haha."
#mc "But it's the first time in my adult life."
mc "Ale to pierwszy raz w moim dorosłym życiu."
scene d1_tribeta18 with dissolve
#ji "Argh! I can't stand bullies. Some boys never grow up."
ji "Nie znoszę tyranów. Niektórzy chłopcy nigdy nie dorastają."
scene d1_tribeta22 with dissolve
menu:
#    "Compliment her":
    "Praw jej komplementy":
        if dtype < 1:
            $ RPjill += 1
#            mc "So, Jill... That's a pretty name."
            mc "Więc, Jill... Ładne imię."
            scene d1_tribeta23 with dissolve
#            ji "Thanks. And you are...?"
            ji "Dzięki. A ty jesteś...?"
            scene d1_tribeta22 with dissolve
#            mc "[name]."
            mc "[name]."
        else:
            $ RPjill -= 1
#            mc "Jill, huh. I'm [name]."
            mc "Jill, co? Jestem [name]."
#            mc "You're pretty hot."
            mc "Jesteś całkiem seksowna."
            scene d1_tribeta23b with dissolve
#            ji "Erm...ok."
            ji "Erm...ok."
#    "Introduce yourself":
    "Przedstawiamy się":
#        mc "I'll be fine, Jill. I'm [name], by the way."
        mc "Nic mi nie będzie, Jill. Przy okazji, jestem [name]."
scene d1_tribeta22b with dissolve
#ji "I think you got some dirt on your clothes."
ji "Myślę, że masz trochę brudu na ubraniu."
scene d1_tribeta22 with dissolve
#mc "Ah... Well, nothing that some good old saliva won't get rid of."
mc "Ach… no nic, czego jakaś dobra stara ślina by się nie pozbyła."
scene d1_tribeta22d with dissolve
#ji "Haha! Euw!"
ji "Haha! Euuu!"
scene d1_tribeta21b with dissolve
#ji "I'm glad you're not hurt."
ji "Cieszę się, że nic ci się nie stało."
scene d1_tribeta24 with dissolve
#ty "Jill, what's the hold-up?"
ty "Jill, co się dzieje?"
scene d1_tribeta24b with dissolve
#ji "Oh! This is Tybalt. Tybalt, this is-"
ji "Och! To jest Tybalt. Tybalt, to jest-"
scene d1_tribeta24c with dissolve
#ty "We're going to be late for our economics lecture, and I want to exchange some words with you before that."
ty "Spóźnimy się na wykład z ekonomii i wcześniej chcę zamienić z Wami kilka słów."
scene d1_tribeta24d with dissolve
#ji "Sorry, [name]. I have to go."
ji "Przepraszam, muszę iść!"
scene d1_tribeta24e with dissolve
#mc "That's ok. I need to go dislodge something from my ass anyway."
mc "W porządku. I tak muszę coś wyjąć z tyłka."
#mc "(Why did I say that...?)"
mc "&lt;em&gt;Dlaczego tak powiedziałem? "
scene d1_tribeta24f with dissolve
#ji "Hahaha!"
ji "Ha!Ha!"
scene d1_tribeta24g with dissolve
#ji "Stay safe, [name]."
ji ". . ."
scene d1_tribeta24h with dissolve
stop music fadeout 3
#mc "(What a beauty...)"
mc "Co za piękno!"
play music "music/ep1/your_smile.mp3"
$ bios_name_jill = True
$ bios_name_tybalt = True
$ bios_jill = True
#$ bios_history_jill = "I met Jill today. She was upset to see the jocks bully me.\n\n"
$ bios_history_jill = "Poznałem dziś Jill. Była zdenerwowana, widząc, jak dręczą mnie sportowcy.\n \n"
#$ bios_history_tybalt = "Tybalt totally ignored me when I was talking to Jill. Was it because of me or Jill?\n\n"
$ bios_history_tybalt = "Tybalt całkowicie mnie zignorował, kiedy rozmawiałem z Jill. Czy to przeze mnie czy Jill?\n \n"
$ chat_new_bios = True
scene d1_tribeta25 with dissolve
#mg "Oh, the wedgie. If ass cracks could get callouses, mine would be hard as marble by now."
mg "Och, wedżi. Gdyby pęknięcia tyłka mogły mieć kalusy, mój byłby teraz twardy jak marmur."
#mg "I feel for you. I really do."
mg "Współczuję Ci. Naprawdę."
#mc "I'll be fine..."
mc "Dam sobie radę."
scene d1_tribeta25b with dissolve
#mc "Hey, you... You wouldn't happen to know someone who can tell me more about the tri-betas."
mc "Hej, ty... Nie znasz przypadkiem kogoś, kto może mi powiedzieć więcej o tri-beta."
scene d1_tribeta25c with dissolve
#mg "Why would I know about that? Because of my glasses?"
mg "Skąd miałbym o tym wiedzieć? Z powodu moich okularów?"
#mc "..."
mc "..."
scene d1_tribeta25c2 with dissolve
#mg "Just pulling your leg."
mg "Po prostu ciągnę cię za nogę."
#mg "You're in luck. I'm the current tri-beta president."
mg "Masz szczęście. Jestem obecnym prezesem tri-bety."
#mg "The name's Magnar."
mg "Nazywam się Magnar."
scene d1_tribeta25c3 with dissolve
#mc "[name]."
mc "[name]."
scene d1_tribeta25c2 with dissolve
#mg "Are you thinking of pledging our friendly fraternity?"
mg "Myślisz o dołączeniu do naszego przyjaznego bractwa?"
scene d1_tribeta25c3 with dissolve
#mc "I don't know, to be honest."
mc "- Też nie kojarzę szczerze mówiąc. "
#mc "I wasn't really going to pledge any fraternity, but I didn't want to say no before checking them out."
mc "Tak naprawdę nie zamierzałem ślubować żadnemu bractwu, ale nie chciałem odmówić, zanim ich nie sprawdzę."
scene d1_tribeta25c2 with dissolve
stop music fadeout 3
#mg "Mhm. Follow me."
mg "Leć za mną. "
scene d1_tribeta25d with wiperight
$ renpy.sound.play("sound_effects/library_ambience.mp3", channel="sfx1", loop=True)
#mg "This is the campus library. Where we tri-betas usually spend our free time."
mg "To jest biblioteka kampusu. Tam, gdzie tri-beta zazwyczaj spędzamy wolny czas."
#mg "It's pretty small, but within these walls, you'll find a vast amount of knowledge."
mg "Jest dość mały, ale w tych ścianach znajdziesz ogromną ilość wiedzy."
scene d1_tribeta26 with dissolve
#mg "Please, be seated."
mg "Proszę spocząć."
scene d1_tribeta27 with dissolve
#mg "To join our fraternity, you must love to study, but it must also show on your grades."
mg "Aby dołączyć do naszego bractwa, musisz kochać naukę, ale musi ona również być widoczna na Twoich ocenach."
#mg "Tell me, how did you do in high school?"
mg "Powiedz mi, jak ci poszło w liceum?"
scene d1_tribeta27b with dissolve
#mc "I did ok. Look, I'm not the smartest guy, but I got into college here."
mc "Zrobiłem dobrze. Słuchaj, nie jestem najmądrzejszym facetem, ale dostałem się tutaj na studia."
scene d1_tribeta27 with dissolve
#mg "Yeah, sorry. That's not enough to qualify you."
mg "Tak, przepraszam. To nie wystarczy, aby się zakwalifikować."
#mg "I don't want to insinuate that you're stupid, but we do have a reputation to keep."
mg "Nie chcę insynuować, że jesteś głupia, ale musimy dbać o reputację."
scene d1_tribeta30 with dissolve
#mg "But it doesn't mean that you're not allowed to come here and study with us."
mg "Ale to nie znaczy, że nie możesz tu przychodzić i uczyć się z nami."
#mg "We'll gladly provide our services...for a price."
mg "Chętnie zapewnimy nasze usługi...za odpowiednią cenę."
#mc "A price?"
mc "Cena"
scene d1_tribeta31b with dissolve
#mg "Sally, would you mind giving us a moment?"
mg "Sally, dasz nam chwilę?"
scene d1_tribeta31c with dissolve
$ renpy.pause()
scene d1_tribeta30b with dissolve
#mg "Even if you're a snooty prep, college is expensive for all fraternities and sororities..."
mg "Nawet jeśli jesteś snobistycznym przygotowaniem, studia są drogie dla wszystkich bractw i bractw..."
#mg "All I'm saying is that we can share a few study techniques and notes with you if you pay us."
mg "Mówię tylko, że możemy podzielić się z Tobą kilkoma technikami badawczymi i notatkami, jeśli nam zapłacisz."
#mg "That will make classes a lot easier for you."
mg "To znacznie ułatwi Ci zajęcia."
if not minigames:
    scene d1_tribeta30b2 with dissolve
#    mc "Thanks, but I'm not interested."
    mc "Dzięki, ale nie jestem zainteresowany."
    jump d1_mg_afterloop
if tutorials:
    scene d1_tribeta30b2 with dissolve
    show white_screen with dissolve
#    show text "{color=#ffffff}Magnar sells items that make the mini-games easier to pass. The items are permanent bonuses. You can buy boosters that lower the requirement to pass a test and get lewd renders by 5% per level.{/color}" with dissolve:
    show text "{color=#ffffff}Magnar sprzedaje przedmioty, które sprawiają, że minigry są łatwiejsze do przejścia. Pozycje są stałymi bonusami. Możesz kupić wzmacniacze, które obniżają wymóg zdania testu i otrzymują sprośne rendery o 5% na poziom.{/color}" with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
scene d1_tribeta30b2 with dissolve
#mc "I'm actually in need of money, too."
mc "Ja też potrzebuję pieniędzy."
scene d1_tribeta30b with dissolve
#mg "Hm..."
mg "Hm..."
#mg "I guess that we could use someone to take notes for us during class."
mg "Myślę, że przyda nam się ktoś do robienia notatek podczas zajęć."
#mg "I'll tell you what. If you pay me {color=#36ca2b}$$${/color}, I'll let you earn money from passing classes."
mg "Powiem ci coś. Jeśli zapłacisz mi {color=#36ca2b}$$${/color}, pozwolę Ci zarabiać pieniądze na zaliczeniu zajęć."
scene d1_tribeta30b2 with dissolve
$ afterMagnarShopLabel = "d1_mg_afterloop"
$ talkMagnarShopLabel = "d1_mg_talk"
$ listenMagnarShopLabel = "d1_mg_listen"
show screen moneymsg
show screen magnar_shop_screen
label d1_mg_loop:

$ renpy.pause()
jump d1_mg_loop
label d1_mg_talk:

scene d1_tribeta30b with dissolve
#mg "Thank you!{w=2}{nw}"
mg "Dziękujemy "
jump d1_mg_listen
label d1_mg_listen:

scene d1_tribeta30b2 with dissolve
jump d1_mg_loop
label d1_mg_afterloop:

scene d1_tribeta30b with dissolve
if minigames:
#    mg "Here, take my number."
    mg "Masz, weź mój numer."
#    mg "Call me if you want to buy something in the future, pal."
    mg "Zadzwoń, jeśli będziesz chciał coś kupić w przyszłości, kolego."
else:
#    mg "All right..."
    mg "W porządku... "
#    mg "Here, take my number."
    mg "Masz, weź mój numer."
#    mg "Just in case you would change your mind."
    mg "Na wypadek, gdybyś zmienił zdanie."
$ number_magnar = True
scene d1_tribeta33 with dissolve
stop music fadeout 10
#mg "Well, this was fun, [name]. I hope I'll be seeing you around."
mg "No to było fajnie, [name]. Mam nadzieję, że się jeszcze zobaczymy."
#mg "I need to make haste. We are playing Dungeons and Gremlins this evening."
mg "Muszę się spieszyć. Dziś wieczorem gramy w Lochy i Gremliny."
$ bios_magnar = True
#$ bios_history_magnar = "Magnar's a nice guy, maybe a tad arrogant. It's weird that people around here like to flaunt that they are smart. Where I come from, that got you beat up.\n\n"
$ bios_history_magnar = "Magnar to miły facet, może trochę arogancki. To dziwne, że ludzie tutaj lubią afiszować się, że są mądrzy. Tam, skąd pochodzę, to cię pobiło.\n \n"
#$ bios_history_magnar += "Magnar offered to sell me tests and to teach me study techniques. I can call him to buy his services.\n\n"
$ bios_history_magnar += "Magnar zaproponował, że sprzeda mi testy i nauczy technik nauczania. Mogę zadzwonić do niego, aby kupić jego usługi.\n \n"
$ bios_name_magnar = True
$ bios_sally = True
$ bios_name_sally = True
$ chat_new_bios = True
$ renpy.music.stop(channel="sfx1", fadeout=3)
#mg "Come, I'll walk you out."
mg "Chodź, odprowadzę Cię."
scene d1_tribeta34 with dissolve
play music "music/ep1/apra_hyde.mp3"
#mc "Who is that?"
mc "Kto to jest? "
#mg "Ah! I see that you've spotted {i}the Ice Queen{/i}."
mg "Ach! Widzę, że zauważyłeś {i}Królową Lodu{/i}."
#mg "She's our librarian."
mg "Jest naszą bibliotekarką."
scene d1_tribeta44 with dissolve
#mc "The Ice Queen?"
mc "Królowa Lodu?"
#mg "Oh. You're not familiar with role-playing games, are you?"
mg "Och. Nie jesteś zaznajomiony z grami fabularnymi, prawda?"
#mg "Well, think of her as the protector of knowledge."
mg "Pomyśl o niej jak o obrończyni wiedzy."
#mg "For keeping our books and territory safe, I applaud her..."
mg "Za to, że nasze księgi i terytorium są bezpieczne, biję jej brawo..."
scene d1_tribeta45 with dissolve
#mg "...but I applaud her in silence."
mg "...ale biję jej brawo w milczeniu."
#mg "She has no tolerance for shenanigans, and if you don't keep quiet, she will scold you."
mg "Nie toleruje błazeństw, a jeśli nie będziesz milczeć, będzie cię karcić."
scene d1_tribeta46 with dissolve
#mg "Good afternoon, Isabella."
mg "Dzień dobry, Izabelo."
#isa "..."
isa "..."
scene d1_tribeta47 with dissolve
#mc "I should probably get a library card to check out books, right?"
mc "Prawdopodobnie powinienem dostać kartę biblioteczną, żeby wypożyczyć książki, prawda?"
scene d1_tribeta47b with dissolve
#mg "Yeah..."
mg "Tak"
#mg "Very smart idea. Go ahead."
mg "Bardzo mądry pomysł. Śmiało."
scene d1_tribeta49 with dissolve
#mg "*{i}Snickers{/i}*"
mg "Snickers"
#mc "(Pff... The Ice Queen? That's pretty mean.)"
mc "(Pff... Królowa Lodu? To dość wredne.)"
scene d1_isa1 with dissolve
#mc "Hi!"
mc "Siemanko!"
menu:
#    "Tell a joke":
    "powiedz kawał":
        if dtype < 1:
#            mc "What did the librarian say to the student?"
            mc "Co bibliotekarka powiedziała uczniowi?"
            scene d1_isa2 with dissolve
#            isa "Shhh!"
            isa "Ciii!"
            scene d1_isa1 with dissolve
#            mc "Oh, so you've heard that one already?"
            mc "Aha, więc już to słyszałeś?"
#            isa "..."
            isa "..."
#            mc "Sorry..."
            mc "Przepraszam..."
#            mc "I'm really here to apply for a library card."
            mc "Naprawdę jestem tutaj, aby ubiegać się o kartę biblioteczną."
        else:
            $ RPisabella -= 1
#            mc "Hey Isabella! Are you a book? Because I would like to check you out."
            mc "Hej Isabella! Jesteś książką? Bo chciałbym cię obejrzeć."
            scene d1_isa3 with dissolve
            $ renpy.pause()
            jump d1_thrown_out
#    "Ask about library card":
    "Zapytaj o kartę biblioteczną":
#        mc "I would like to apply for a library card."
        mc "Chciałbym złożyć wniosek o kartę biblioteczną."
#mc "..."
mc "..."
#mc "Can you help me with that?"
mc "Czy możesz mi z tym pomóc?"
scene d1_isa4 with dissolve
#isa "No."
isa "l.p."
scene d1_isa4b with dissolve
#mc "..."
mc "..."
#mc "Ok..."
mc "Dobrze..."
#mc "How does this work, then? I'm guessing I need a library card to check out books, right?"
mc "Jak to działa? Zgaduję, że potrzebuję karty bibliotecznej do wypożyczania książek, prawda?"
scene d1_isa4c with dissolve
#isa "You use your student ID."
isa "Korzystasz z legitymacji studenckiej."
scene d1_isa4b with dissolve
#mc "Oh, I haven't got one of those yet."
mc "Och, jeszcze takiego nie mam."
#mc "I think I'll get mine later this week."
mc "Myślę, że mój dostanę jeszcze w tym tygodniu."
#mc "..."
mc "..."
#mc "So...erm...I..."
mc "Więc...hmm...ja..."
stop music fadeout 3
#mc "Nice chatting with you."
mc "Miło się z Tobą rozmawiało."
jump d1_not_thrown_out
label d1_thrown_out:

stop music
play sound "sound_effects/shove.mp3"
scene d1_after_library with hpunch
$ renpy.pause()
scene d1_after_library1 with dissolve
#mc "That wasn't really what I thought would happen."
mc "Nie sądziłem, że tak się stanie."
label d1_not_thrown_out:

$ guideSuggestedPage = 37
jump ep1_freeroam_dorm_label
label ep1_college_day2_label:

$ current_task = "None"
$ chat_new_tasks = False
#$ bios_history_troy += "Troy left the dorm in the middle of the night. He's up to something.\n\n"
$ bios_history_troy += "Troy wyszedł z akademika w środku nocy. On coś knuje.\n \n"
$ bios_name_troy = True
$ chat_new_bios = True
if preferredmilf == 0:
    label ep1_jade_lewd:
    if _in_replay:
        hide screen phone_screen
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_jade == None:
            $ mc_jade = name
        else:
            $ mc_jade = persistent.mc_jade
        if persistent.jade == None:
            $ jade = "Jade"
        else:
            $ jade = persistent.jade
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_jade_dream2 with Fade(1.5, 1, 0.5)
#    ja "Hey, [mc_jade]..."
    ja "Hej... "
    scene ep1_jade_dream3 with dissolve
#    mc "OH MY GOD! Who are you!?"
    mc "O mój BOŻE! Kim ty jesteś!?"
    scene ep1_jade_dream2 with dissolve
#    ja "Come on; you overheard my name in the cafeteria...I'm Jade."
    ja "Daj spokój, podsłuchałeś moje imię w stołówce...Jestem Jade."
    scene ep1_jade_dream with dissolve
#    mc "Oh, yeah...but what are you doing?"
    mc "O tak...ale co ty robisz?"
    scene ep1_jade_dream1 with dissolve
#    ja "Take a look around, [mc_jade]...you're dreaming."
    ja "Rozejrzyj się, [mc_jade]...śnisz."
#    ja "That means you can do whatever you want...without any consequences..."
    ja "Oznacza to, że możesz robić, co chcesz...bez żadnych konsekwencji..."
#    mc "I can?"
    mc "Pozdrowienia. "
    scene ep1_jade_dream2 with dissolve
#    ja "Well, that's kind of why I'm kneeling here squeezing my big tits around your huge hard cock, [mc_jade]."
    ja "Cóż, właśnie dlatego klęczę tutaj, ściskając moje duże cycki wokół twojego ogromnego, twardego kutasa [mc_jade]."
#    ja "Let's not waste any more time...you might wake up."
    ja "Nie marnujmy więcej czasu...możesz się obudzić."
    init 500 image anim_jade_boobjob1_ep1 = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ja "Here we go..."
    ja "Zaczynamy!"
#    ja "Your cock feels so good between my tits, [mc_jade]..."
    ja "Twój kutas jest tak dobry między moimi cyckami, [mc_jade]..."
#    mc "Oh [jade], your tits are so soft..."
    mc "Och [jade], twoje cycki są takie miękkie..."
#    ja "I can squeeze them tighter if you want..."
    ja "Mogę ścisnąć je mocniej, jeśli chcesz..."
#    mc "No, [jade], this is perfect."
    mc "Nie, [jade], to jest idealne."
    pause
    init 500 image anim_jade_boobjob2_ep1 = Movie(channel="anim_jade_boobjob2_ep1", play="images/movies/ep1/anim_jade_boobjob2_ep1.webm")
    scene anim_jade_boobjob2_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "Tell me...do you prefer tits or asses?"
    ja "Powiedz mi...wolisz cycki czy tyłki?"
    menu:
#        "Tits":
        "Cycki":
#            mc "Oh, definitely tits, [jade]."
            mc "Och, zdecydowanie cycki, [jade]."
#            ja "Mhm...that's good to know..."
            ja "Warto to wiedzieć!"
#        "Asses":
        "Osły":
#            mc "Asses, [jade]. No question about it."
            mc "Osły, [jade]. Nie ma co do tego wątpliwości."
#            ja "Really? So, you don't like my tits, then?"
            ja "Naprawdę? Więc nie podobają ci się moje cycki?"
#            mc "No, I didn't say that."
            mc "I agree."
#            ja "Haha, I'm just teasing you, [mc_jade]..."
            ja "Haha, tylko ci dokuczam, [mc_jade]..."
    init 500 image anim_jade_boobjob1_ep1 = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "Would you like me to do something else? I can do anything you want, you know..."
    ja "Chcesz, żebym zrobił coś innego? Mogę zrobić, co tylko zechcesz, wiesz..."
#    mc "Wow...anything?"
    mc "Wow...cokolwiek?"
#    ja "Sure. I'm yours to fuck however you wish..."
    ja "Jasne. Możesz mnie pieprzyć, jak tylko zechcesz..."
#    ja "...the only thing you can't do, though, is to-"
    ja "...jedyną rzeczą, której nie możesz zrobić, jest…"
    $ persistent.ep1_jade_dream1 = True
    $ renpy.end_replay()
    $ calcScenes()
    stop music
    scene ep1_jade_dream_troy
#    troy "Wake up!"
    troy "Pobudka!"
#    $ bios_history_jade += "I had a sexy dream about Jade...\n\n"
    $ bios_history_jade += "Miałam seksowny sen o Jade...\n \n"
else:
    label ep1_cathy_lewd:
    if _in_replay:
        hide screen phone_screen
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_cathy == None:
            $ mc_cathy = name
        else:
            $ mc_cathy = persistent.mc_cathy
        if persistent.cathy == None:
            $ cathy = "Cathy"
        else:
            $ cathy = persistent.cathy
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_d2_wake with Fade(1.5, 1, 0.5)
#    ca "You did so well on your test, [mc_cathy]."
    ca "Świetnie Ci poszło na teście, [mc_cathy]."
    if failedEnglish != 0:
#        mc "What? But I failed the test..."
        mc "Co? Ale oblałem test..."
#    ca "I can't believe you know so much..."
    ca "Nie wierzę, że tyle wiesz..."
    if failedEnglish != 0:
#        mc "Oh, ok...this is a dream..."
        mc "Aha, okej...to jest sen..."
#    ca "I kind of feel like you should be the one teaching me things."
    ca "Czuję, że to ty powinieneś mnie czegoś uczyć."
    scene ep1_d2_wake1 with dissolve
#    ca "Would you like to teach me how to pronounce words like onomatopoeia?"
    ca "Czy chciałbyś mnie nauczyć, jak wymawiać słowa takie jak onomatopea?"
    scene ep1_d2_wake2 with dissolve
#    ca "Whoops! I already knew that word..."
    ca "Ups! Znałem już to słowo..."
    scene ep1_d2_wake3 with dissolve
#    ca "What about sarcoidosis?"
    ca "A co z sarkoidozą?"
    scene ep1_d2_wake2 with dissolve
#    ca "Oh, silly me! Again!"
    ca "Och, głupia ja! Znowu!"
    scene ep1_d2_wake3b with dissolve
#    ca "Well, I'm sure that there are other ways..."
    ca "Cóż, jestem pewien, że są inne sposoby..."
#    ca "...in which you can wake me up."
    ca "...w którym możesz mnie obudzić."
    scene ep1_d2_wake4 with dissolve
#    ca "Can you wake me up?"
    ca "Czy możesz mnie obudzić?"
    $ persistent.ep1_cathy_dream1 = True
    $ renpy.end_replay()
    $ calcScenes()
    scene ep1_d2_wake5
    stop music
#    troy "Wake up!"
    troy "Pobudka!"
#    $ bios_history_cathy += "I had a sexy dream about Cathy.\n\n"
    $ bios_history_cathy += "Miałam seksowny sen o Cathy.\n \n"
    $ bios_name_cathy = True
    $ chat_new_bios = True
$ guideSuggestedPage = 38
scene ep1_d2_wake6 with hpunch
#mc "AHHH!!!"
mc "Aaach!!! "
scene ep1_d2_wake7 with dissolve
#troy "What the fuck's the matter with you?"
troy "Co się z wami dzieje?"
play music "music/ep1/someways.mp3"
scene ep1_d2_wake8 with dissolve
#mc "Oh, nothing..."
mc "Och, nic, Jake. "
#mc "What do you want?"
mc "Czego chcesz?"
scene ep1_d2_wake7 with dissolve
#troy "You need to leave; I'm getting company."
troy "Musisz wyjść; Idę po towarzystwo."
scene ep1_d2_wake8 with dissolve
#mc "What? Now?"
mc "Co dalej?"
scene ep1_d2_wake7 with dissolve
#troy "Yes, now! Get out! Don't you have classes to go to or something?"
troy "Tak, teraz! Wynocha! Nie masz zajęć, na które musisz iść, czy coś?"
scene ep1_d2_wake8 with dissolve
menu:
#    "Fine":
    "Dobrze":
        $ dk(-1)
#        mc "Fine. Give me a second, will you?"
        mc "Dobrze. Daj mi chwilę, dobrze?"
#    "Don't you?":
    "A Ty? ":
        $ dk(1)
#        mc "Don't you?"
        mc "A Ty? "
play sound "sound_effects/shove.mp3"
scene ep1_d2_wake11 with hpunch
#mc "Dude!"
mc "Ziom. "
play sound "sound_effects/door_slam.mp3"
scene d1_dorm with hpunch
if dtype > 0:
#    mc "(I'm going to fucking snap soon...)"
    mc "(Niedługo, kurwa, pęknę...)"
else:
#    mc "(This is not sustainable...)"
    mc "To nie jest ekologiczne."
scene ep1_d2_sage with wipeleft
#sa "Hey, it's you again!"
sa "Hej, to znowu Ty!"
scene ep1_d2_sage1 with dissolve
#mc "Hey..."
mc "Hej"
menu:
#    "Sage, was it?":
    "Szałwia, prawda?":
        $ dk(-1)
        $ ep1_blank_on_name = False
#        mc "Sage, was it?"
        mc "Szałwia, prawda?"
        scene ep1_d2_sage2 with dissolve
#        sa "Right."
        sa "Dobrze."
#    "I'm blanking on your name":
    "Twoje imię jest puste":
        $ dk(1)
        $ ep1_blank_on_name = True
#        mc "I'm blanking on your name."
        mc "Twoje imię jest puste."
        scene ep1_d2_sage2b with dissolve
#        sa "It's Sage! Fucking learn to listen."
        sa "To Sage! Kurwa, naucz się słuchać."
        scene ep1_d2_sage2 with dissolve
$ guideSuggestedPage = 39
#sa "You hate Chad, right?"
sa "Nienawidzisz Chada, prawda?"
scene ep1_d2_sage1 with dissolve
menu:
#    "Yes":
    "Tak":
        if dtype > 0:
            $ RPsage += 1
#            mc "Who? Chad? Oh! You mean Mr. Juicebox!"
            mc "Kto? Czad? Och! Masz na myśli Pana Juicebox!"
            scene ep1_d2_sage2c with dissolve
#            sa "Mr. Juicebox?"
            sa "Panie Juicebox?"
            scene ep1_d2_sage6 with dissolve
#            mc "Yeah, you know, because he's juiced up and kind of looks like a juice box when he walks."
            mc "Tak, wiesz, bo jest naćpany i wygląda jak sok w kartonie, kiedy chodzi."
#            sa "HAHA! You're fucking mean!"
            sa "HAHA! Jesteś kurewsko wredny!"
#            $ bios_history_sage += "Sage liked my mean joke.\n\n"
            $ bios_history_sage += "Sage lubiła mój podły dowcip.\n \n"
            $ bios_name_sage = True
            $ chat_new_bios = True
            scene ep1_d2_sage2 with dissolve
#            sa "I like that."
            sa "Podoba mi się to."
        else:
#            mc "With a burning passion."
            mc "Z palącą pasją."
            scene ep1_d2_sage2 with dissolve
#            sa "Good!"
            sa "Znakomicie!"
#    "No":
    "Nie":
#        mc "No, I don't hate him."
        mc "Nie, nie nienawidzę go."
        scene ep1_d2_sage2 with dissolve
#        sa "Yes, you do."
        sa "Udało się! "
#sa "I saw what the jocks did to you yesterday."
sa "Widziałem, co wczoraj zrobili ci sportowcy."
scene ep1_d2_sage1 with dissolve
#mc "That was nothing."
mc "To było nic. "
scene ep1_d2_sage2d with dissolve
#sa "Nothing? Not even my G-strings go that high up."
sa "Nic? Nawet moje stringi nie sięgają tak wysoko."
menu:
    "Let me check ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        $ RPsage += 1
        scene ep1_d2_sage_ass with dissolve
#        mc "Really? Let me check."
        mc "Naprawdę? Pozwól, że sprawdzę."
#        mc "Hm...hard to tell from here."
        mc "Hmm...trudno powiedzieć stąd."
        scene ep1_d2_sage_ass1 with dissolve
#        sa "Hah. Stop it!"
        sa "Hah. Przestań!"
#    "If you say so":
    "Jeśli tak twierdzisz":
#        mc "If you say so."
        mc "Skoro tak mówisz."
scene ep1_d2_sage2 with dissolve
#sa "I have a proposition for you."
sa "Mam dla Ciebie propozycję."
scene ep1_d2_sage1 with dissolve
#mc "What's it about?"
mc "A o co chodzi? "
scene ep1_d2_sage2 with dissolve
#sa "It's simple, really. I want you to find out who Chad's been fucking behind my back."
sa "To naprawdę proste. Chcę, żebyś się dowiedział, kto pieprzył się z Chadem za moimi plecami."
scene ep1_d2_sage1 with dissolve
menu:
#    "What's in it for me?":
    "Co z tego będę mieć?":
        $ dk(1)
#        mc "What's in it for me?"
        mc "Co z tego będę mieć?"
#    "No way":
    "Nie ma mowy":
        $ dk(-1)
        if dtype > 0:
#            mc "Fat chance. Take care of your own dirty business. I'm not your errand boy."
            mc "Nie ma szans. Zajmij się swoimi brudnymi sprawami. Nie jestem twoim chłopcem na posyłki."
        else:
#            mc "Nope, not gonna happen. I'm not getting involved in your love life."
            mc "Nie, nic z tego. Nie angażuję się w twoje życie miłosne."
scene ep1_d2_sage2 with dissolve
#sa "Well..."
sa "Cóż..."
#sa "If you scratch my back, I'll scratch yours."
sa "Jeśli podrapiesz mnie po plecach, ja podrapie ciebie."
#mc "(What is she getting at?)"
mc "(Do czego ona zmierza?)"
scene ep1_d2_sage1 with dissolve
#mc "Yeah, I don't know..."
mc "Nie wiem"
scene ep1_d2_sage14 with dissolve
#sa "Think about it."
sa "Zastanów się nad tym. "
if ep1_blank_on_name:
#    sa "Talk to you later...erm..."
    sa "Później porozmawiamy. "
#    sa "Sorry, \"I'm blanking on your name\"."
    sa ", \„Puste miejsce na Twoim imieniu\”."
else:
#    sa "Talk to you later...[name], was it?"
    sa "Pogadamy później...[name], tak?"
scene ep1_d2_sage15 with dissolve
#$ bios_history_sage += "Sage proposed that I help her find out who Chad is fucking behind her back. If I accept, she said I would be rewarded somehow.\n\n"
$ bios_history_sage += "Sage zaproponowała, żebym pomógł jej dowiedzieć się, kto pieprzy Chada za jej plecami. Jeśli się zgodzę, powiedziała, że w jakiś sposób otrzymam nagrodę.\n \n"
$ bios_name_sage = True
$ chat_new_bios = True
#mc "(This girl is trouble...)"
mc "(Ta dziewczyna to kłopot...)"
if dtype > 0:
#    mc "(I think I like trouble.)"
    mc "(Myślę, że lubię kłopoty.)"
scene ep1_d2_math with wipeleft
#ca "Good morning, class. Are we ready for a math test today?"
ca "Dzień dobry, klaso. Czy jesteśmy dziś gotowi na test z matematyki?"
scene ep1_d2_math_de1 with dissolve
#de "Yes, I stayed up all night studying for it."
de "Tak, siedziałem całą noc, ucząc się do tego."
scene ep1_d2_math1 with dissolve
#ca "(He's such a smartass.)"
ca "(To taki mądrala.)"
scene ep1_d2_math with dissolve
stop music fadeout 3
#ca "Best of luck to you! You may begin."
ca "Powodzenia! Możesz zacząć."
if not minigames:
    scene black with Fade(1.5, 1, 0.5)
    jump ep1_after_math_test
scene desk_bg with wipeleft
play music "music/ep3/sing_along_with_jim.mp3"
if tutorials:
    scene desk_bg_tut with dissolve
    $ renpy.pause()
    scene desk_bg_tut1 with dissolve
    $ renpy.pause()
    scene desk_bg_tut2 with dissolve
    $ renpy.pause()
jump math101_test1
label ep1_after_math_test:

$ renpy.block_rollback()
if minigames:
    scene ep1_d2_math with wiperight
    stop music fadeout 3
else:
    scene ep1_d2_math with fade
#ca "Pencils down, class."
ca "Ołówki w dół, klasa."
#ca "Please turn in your tests."
ca "Zwróć swoje testy."
scene ep1_d2_math2 with dissolve
play music "music/ep1/art_nouveau.mp3"
#ca "That wasn't so bad, was it?"
ca "Teraz nie było tak źle, prawda?"
#ca "Tomorrow, there will be no more tests. I promise."
ca "Jutro nie będzie więcej testów. Obiecuję."
#ca "Instead, we'll start having lectures."
ca "Zamiast tego zaczniemy prowadzić wykłady."
scene ep1_d2_math with dissolve
#ca "Don't forget to sign up for other classes online, students."
ca "Nie zapomnij zapisać się na inne zajęcia online, studenci."
scene ep1_d2_math3 with dissolve
#mc "Hey, Maya. Did you sign up for any class yet?"
mc "Hej, Maya. Zapisałaś się już na jakieś zajęcia?"
scene ep1_d2_math4 with dissolve
#my "Yeah, I did. Gender Studies 101."
my "Tak. Gender Studies 101."
#my "How about you?"
my "A ty? "
scene ep1_d2_math5 with dissolve
#mc "No, nothing yet."
mc "Nie, żadnymi."
#mc "So...gender studies, huh? What's that about?"
mc "Więc...gender studies, co? O co chodzi?"
scene ep1_d2_math4 with dissolve
#my "Well, it's a-"
my "No to jest tam... "
scene ep1_d2_math6
if assman:
#    de "It's a fucking feminist class, ass man."
    de "To pieprzona klasa feministyczna, dupku."
#    my "Ass man?"
    my "Człowieku z tyłkiem?"
else:
#    de "It's a fucking feminist class, bro."
    de "To pieprzona klasa feministyczna, brachu."
#de "Trust me; it's bullshit."
de "Zaufaj mi, to bzdura."
scene ep1_d2_math7 with dissolve
#my "Shut up, Derek. It's not bullshit!"
my "Zamknij się, Derek. To nie bzdura!"
scene ep1_d2_math8 with dissolve
#my "*{i}Psst{/i}* It's easy credits."
my "*{i}Psst{/i}* Łatwe kredyty."
scene ep1_d2_math9 with dissolve
#de "Easy credits? For real?"
de "Łatwe kredyty? Naprawdę?"
scene ep1_d2_math10b with dissolve
#my "Yeah, if you're into that sort of stuff."
my "Tak, jeśli lubisz takie rzeczy."
scene ep1_d2_math11 with dissolve
#de "Define stuff."
de "Zdefiniuj rzeczy."
scene ep1_d2_math10 with dissolve
#my "Women's rights."
my "Women's rights"
scene ep1_d2_math12
#de "Nope."
de "Odmawiam."
scene ep1_d2_math10 with dissolve
#my "Gender equality."
my "równość płci."
scene ep1_d2_math12
#de "Couldn't care less."
de "Nic mnie to nie obchodzi."
scene ep1_d2_math10 with dissolve
#my "Vaginas."
my "Pochwa"
scene ep1_d2_math12
#de "No-"
de "Nie"
scene ep1_d2_math13 with dissolve
#de "Yes!"
de "Tak!"
scene ep1_d2_math14 with dissolve
#my "That was a test. You just failed."
my "To był test. Po prostu zawiodłeś."
scene ep1_d2_math15 with dissolve
#de "So, no vaginas?"
de "Więc nie ma wagin?"
scene ep1_d2_math10b with dissolve
#my "Well, probably some vaginas..."
my "No, pewnie jakieś waginy..."
scene ep1_d2_math17 with dissolve
#my "Wait, why are we discussing vaginas?"
my "Chwila, dlaczego rozmawiamy o waginach?"
#my "No, Derek, I don't think it's a class for you."
my "Nie, Derek, nie sądzę, żeby to były zajęcia dla ciebie."
scene ep1_d2_math18 with dissolve
#de "Yeah, whatever."
de "- Mam to gdzieś - "
scene ep1_d2_math19 with dissolve
#my "You, on the other hand... Are you up for it?"
my "Ty, z drugiej strony... jesteś na to gotowy?"
scene ep1_d2_math20 with dissolve
#mc "I don't think it's for me either..."
mc "To chyba nie dla mnie."
scene ep1_d2_math19 with dissolve
#my "Come on! It will be fun!"
my "No dalej! Będzie fajnie!"
#my "If you don't like it, you can just sit there and pretend to listen."
my "Jeśli Ci się to nie podoba, możesz po prostu siedzieć i udawać, że słuchasz."
scene ep1_d2_math22 with dissolve
#my "Like I said...easy credits."
my "Tak jak mówiłem...łatwe kredyty."
#my "Plus, it will look good on your resume."
my "Dodatkowo będzie dobrze wyglądać w Twoim CV."
scene ep1_d2_math20 with dissolve
$ genderPresented = True
show screen skillmsg
#mc "Ok, what the hell. I can give it a shot."
mc "Dobra, co mi tam. Mogę spróbować."
hide screen skillmsg
#$ bios_history_maya += "Maya convinced me to sign up for Gender Studies.\n\n"
$ bios_history_maya += "Maya przekonała mnie, żebym zapisała się na studia nad płcią.\n \n"
$ bios_name_maya = True
$ chat_new_bios = True
scene ep1_d2_math19 with dissolve
#my "Wanna eat lunch together?"
my "Chcesz zjeść razem lunch?"
scene ep1_d2_math20 with dissolve
#mc "Sure...but tell me..."
mc "Jasne...ale powiedz mi..."
#mc "Is there anything else to eat around here besides cafeteria food?"
mc "Czy jest tu coś jeszcze do jedzenia poza stołówką?"
scene ep1_d2_math19 with dissolve
#my "Ah, you want to eat healthier too!"
my "Ach, ty też chcesz zdrowiej się odżywiać!"
stop music fadeout 3
#my "We'll have to go outside of campus."
my "Będziemy musieli wyjść poza kampus."
#my "Are you up for it?"
my "Jesteś na to gotowy?"
scene ep1_d2_math20 with dissolve
#mc "Lead the way."
mc "Niech pan prowadzi! "
$ guideSuggestedPage = 40
play music "music/ep1/golden_alley.mp3"
$ renpy.sound.play("sound_effects/cafeteria.mp3", channel="sfx1", loop=True)
scene ep1_cafe_maya with wipeleft
#my "Oh, I've been there. It's very close!"
my "Och, już to przerabiałam. To bardzo blisko!"
scene ep1_cafe_maya1 with dissolve
#mc "Yeah, it's just 30 minutes by train."
mc "Tak, to tylko 30 minut pociągiem."
#mc "I will probably go back and visit my dad a lot."
mc "Prawdopodobnie będę często wracać i odwiedzać tatę."
scene ep1_cafe_maya2 with dissolve
#my "..."
my "..."
#mc "How about you? You said you're a local."
mc "A ty? Powiedziałeś, że jesteś stąd."
#mc "Do you live close by?"
mc "Mieszkasz w pobliżu?"
scene ep1_cafe_maya2b with dissolve
#my "I live on campus, stupid."
my "Mieszkam na kampusie, głupku."
scene ep1_cafe_maya2 with dissolve
#mc "Well, I kind of meant your parents."
mc "Cóż, miałem na myśli twoich rodziców."
scene ep1_cafe_maya2c with dissolve
#my "They live uptown; it's not far from here."
my "Mieszkają na przedmieściach; to niedaleko stąd."
scene ep1_cafe_maya2 with dissolve
#mc "(Hm...her tone has changed...)"
mc "(Hm...jej ton się zmienił...)"
if dtype < 1:
#    mc "(This is probably a sensitive issue...)"
    mc "(To chyba delikatna kwestia...)"
else:
#    mc "(I wonder why...)"
    mc "Bóg to sprawia."
scene ep1_cafe_maya6 with dissolve
#my "Enough family talk. Let me see what kind of person you really are!"
my "Dosyć gadania o rodzinie. Zobaczmy, jaką naprawdę jesteś osobą!"
scene ep1_cafe_maya7 with dissolve
#mc "Erm...ok? What do you have in mind?"
mc "Hmm...okej? Co masz na myśli?"
scene ep1_cafe_maya6 with dissolve
#my "I'll ask you a few questions, and after that, I'm going to figure you out."
my "Zadam ci kilka pytań, a potem cię rozgryzę."
scene ep1_cafe_maya7 with dissolve
#mc "I've never done such a thing before...but all right."
mc "Nigdy wcześniej czegoś takiego nie robiłem...ale w porządku."
#mc "Fire away."
mc "No to dawaj."
scene ep1_cafe_maya6 with dissolve
#my "Which do you prefer...being indoors or outdoors?"
my "Co wolisz...być w domu czy na zewnątrz?"
scene ep1_cafe_maya7 with dissolve
menu:
#    "Indoors":
    "W pomieszczeniach":
        $ ep1_maya_question_indoors = True
#        mc "I'm an indoors kind of guy."
        mc "Jestem typem faceta, który lubi przebywać w pomieszczeniach."
#    "Outdoors":
    "Krajobraz":
        $ ep1_maya_question_indoors = False
#        mc "Easy, definitely outdoors."
        mc "Łatwe, na pewno na świeżym powietrzu."
scene ep1_cafe_maya8 with dissolve
#my "Interesting..."
my "Ciekawe..."
scene ep1_cafe_maya6 with dissolve
#my "Which sounds nicer...?"
my "Co brzmi lepiej...?"
#my "Cuddling up with a blanket or taking a bubble bath?"
my "Przytulasz się kocem czy bierzesz kąpiel z bąbelkami?"
scene ep1_cafe_maya7 with dissolve
menu:
#    "Cuddling with a blanket":
    "Przytulanie się kocem":
        $ ep1_maya_question_blanket = True
        $ ep1_maya_question_bath = False
#        mc "Cuddling up with a blanket sounds nicer...but I'm not sure I would do that by myself."
        mc "Przytulanie się z kocem brzmi przyjemniej...ale nie jestem pewien, czy zrobiłbym to sam."
#    "Bubble bath":
    "Piana do kąpieli":
        $ ep1_maya_question_blanket = False
        $ ep1_maya_question_bath = True
#        mc "I'd have to say bubble baths...is that weird?"
        mc "Powiedziałbym, że kąpiele z bąbelkami...czy to dziwne?"
        scene ep1_cafe_maya8 with dissolve
#        my "I'm asking the questions here. You just answer them."
        my "Ja tu zadaję pytania. Po prostu odpowiadasz."
#    "Neither":
    "Żadna z opcji":
        $ ep1_maya_question_blanket = False
        $ ep1_maya_question_bath = False
#        mc "Nope, neither of those are for me."
        mc "Nie, żadne z nich nie jest dla mnie."
scene ep1_cafe_maya9 with dissolve
#my "Do you drink alcohol?"
my "Czy pije Pan/Pani alkohol ? "
scene ep1_cafe_maya7 with dissolve
#mc "Yeah, it happens."
mc "Tak, zdarza się."
#mc "But I haven't partied a lot in my life...yet."
mc "Ale nie imprezowałem zbyt wiele w moim życiu...jeszcze."
scene ep1_cafe_maya9 with dissolve
#my "Would you rather spend a night with friends getting drunk at a party or at home with a bottle of wine?"
my "Wolisz spędzić noc z przyjaciółmi upijając się na imprezie lub w domu z butelką wina?"
scene ep1_cafe_maya7 with dissolve
menu:
#    "At a party":
    "Impreza":
        $ ep1_maya_question_party = True
#        mc "At a party, of course!"
        mc "Oczywiście na imprezie!"
#    "At home":
    "W domu":
        $ ep1_maya_question_party = False
#        mc "I wouldn't be against partying, but I'd prefer just staying home chatting and casually drinking with them."
        mc "Nie byłbym przeciwny imprezowaniu, ale wolałbym po prostu siedzieć w domu i rozmawiać i swobodnie z nimi pić."
scene ep1_cafe_maya9 with dissolve
#my "Do you keep your promises?"
my "Czy dotrzymujesz obietnic?"
scene ep1_cafe_maya10 with dissolve
#mc "I think I do..."
mc "Myślę, że wiem."
scene ep1_cafe_maya9 with dissolve
#my "So, if I asked you to promise me something..."
my "Więc gdybym poprosił cię o obietnicę..."
#my "...would you?"
my "Zagrałabyś? "
scene ep1_cafe_maya10 with dissolve
#mc "For you? Sure."
mc "Dla ciebie? Jasne."
scene ep1_cafe_maya9 with dissolve
#my "Ok. Can you promise me to always be honest with me and to never lie?"
my "Ok. Czy możesz mi obiecać, że zawsze będziesz ze mną szczery i nigdy nie skłamiesz?"
scene ep1_cafe_maya11 with dissolve
#mc "I can do that."
mc "Mogę tak zrobić "
scene ep1_cafe_maya9 with dissolve
#my "Really? Say it!"
my "Serio? Powiedz to!"
scene ep1_cafe_maya11 with dissolve
#mc "I promise!"
mc "Obiecuję! "
#mc "Why wouldn't I be able to? I can be 100%% honest with you."
mc "Dlaczego miałbym nie być w stanie? Mogę być z Tobą w 100% szczery."
scene ep1_cafe_maya6 with dissolve
#my "Do you masturbate?"
my "Masturbujesz się?"
scene ep1_cafe_maya11 with dissolve
#mc "Ok, maybe 99%% honest with you."
mc "Ok, może 99% szczerości z Tobą."
scene ep1_cafe_maya11b with dissolve
#my "Haha! Come on, you promised!"
my "Haha! Daj spokój, obiecałeś!"
scene ep1_cafe_maya11 with dissolve
#mc "I thought you meant honesty like telling you if you looked fat in a dress or something."
mc "Myślałem, że masz na myśli szczerość, jak mówienie ci, czy wyglądasz grubo w sukience, czy coś."
#mc "Not something so personal."
mc "Nie coś tak osobistego."
scene ep1_cafe_maya11c with dissolve
#my "Yeah, sorry. I don't think I can trust you."
my "Tak, przepraszam. Chyba nie mogę ci ufać."
scene ep1_cafe_maya11 with dissolve
#mc "I can be 100%% honest, but then you would have to be that way too!"
mc "Mogę być w100% szczery, ale wtedy ty też musiałbyś być taki!"
scene ep1_cafe_maya11c with dissolve
#my "If you can prove to me that you are...yeah! I could do that."
my "Jeśli możesz mi udowodnić, że jesteś...tak! Mógłbym to zrobić."
#my "But you would REALLY have to prove it."
my "Ale NAPRAWDĘ musiałbyś to udowodnić."
scene ep1_cafe_maya11 with dissolve
#mc "Fine. Yes, I masturbate. Who doesn't?"
mc "Dobra. Tak, masturbuję się. A kto nie lubi?"
scene ep1_cafe_maya11c with dissolve
#my "I don't."
my "Ja nie."
scene ep1_cafe_maya11 with dissolve
#mc "What!?"
mc "Co?!"
scene ep1_cafe_maya11c with dissolve
#my "Yeah, there must be something seriously wrong with you."
my "Tak, musi być z Tobą coś nie tak."
scene ep1_cafe_maya11b with dissolve
#mc "Ok, now you're just fucking with me."
mc "Dobra, teraz sobie ze mnie pogrywasz."
#my "Hahaha!"
my "Ha!Ha!"
#mc "What about you?"
mc "A ty?"
scene ep1_cafe_maya9 with dissolve
#my "Nuh-uh! I'm still asking the questions here, remember?"
my "Nuh-uh! Nadal zadaję tu pytania, pamiętasz?"
#my "How many relationships have you been in?"
my "W ilu związkach byłeś?"
scene ep1_cafe_maya11 with dissolve
#mc "...just one. Listen, I don't want to talk about that."
mc "...tylko jeden. Słuchaj, nie chcę o tym rozmawiać."
scene ep1_cafe_maya11d with dissolve
#my "Ended poorly, huh?"
my "Źle się skończyło, co?"
scene ep1_cafe_maya11 with dissolve
#mc "Don't they all?"
mc "A nie wszyscy?"
scene ep1_cafe_maya11d with dissolve
#my "I wouldn't know."
my "- Nie znam."
scene ep1_cafe_maya11c with dissolve
#my "Ok, I'm not gonna push you on that, for now."
my "Ok, na razie na to nie będę naciskał."
#my "How many girls have you slept with?"
my "Z iloma dziewczynami spałeś?"
scene ep1_cafe_maya11 with dissolve
#mc "Wow, you're really going all-in on personal questions..."
mc "Wow, naprawdę dajesz z siebie wszystko w kwestiach osobistych..."
scene ep1_cafe_maya11d with dissolve
#my "Ok, don't answer that. I'll stop."
my "Ok, nie odpowiadaj na to. Przestanę."
scene ep1_cafe_maya with dissolve
#my "Wow, time really flies chatting with you!"
my "Wow, czas naprawdę szybko z Tobą gada!"
scene ep1_cafe_maya24 with dissolve
#my "Come, let's leave."
my "Chodź, wychodzimy."
show screen moneymsg
menu:
    "Pay for her meal ({color=#36ca2b}${/color})" if money > 0:
#        $ bios_history_maya += "I had a nice afternoon with Maya, I paid for her lunch.\n\n"
        $ bios_history_maya += "Spędziłem miłe popołudnie z Mayą, zapłaciłem za jej lunch.\n \n"
        $ ep1_maya_question_money = True
        $ money -= 1
        $ RPmaya += 1
#        mc "Hey, keep that. It's my treat."
        mc "Hej, zatrzymaj to. Ja stawiam."
        hide screen moneymsg
#        my "Are you sure?"
        my "Na pewno?"
#        mc "Yeah, I want to."
        mc "Tak, chcę."
        scene ep1_cafe_maya25 with dissolve
#        my "Thank you so much!"
        my "Dziękuję bardzo!"
#    "Don't pay for her meal":
    "Nie płać za jej posiłek":
#        $ bios_history_maya += "I had a nice afternoon with Maya.\n\n"
        $ bios_history_maya += "Spędziłem miłe popołudnie z Mayą.\n \n"
        hide screen moneymsg
        $ ep1_maya_question_money = False
        $ renpy.pause(0.5)
$ bios_name_maya = True
$ chat_new_bios = True
scene ep1_cafe_maya26 with dissolve
#my "Remember what I said in the beginning?"
my "Pamiętasz, co mówiłem na początku?"
scene ep1_cafe_maya27 with dissolve
#mc "Beginning of what?"
mc "Początek czego?"
scene ep1_cafe_maya26 with dissolve
#my "That I thought that I could figure you out."
my "Że myślałam, że cię rozgryzę."
scene ep1_cafe_maya27 with dissolve
#mc "Ah, yeah."
mc "YEAY !!"
scene ep1_cafe_maya26 with dissolve
#my "I just did."
my "Ja po prostu nie"
scene ep1_cafe_maya27 with dissolve
#mc "And?"
mc "I?"
scene ep1_cafe_maya28 with dissolve
#my "I'm not telling you."
my "Mówię ci. "
scene ep1_cafe_maya27 with dissolve
#mc "I don't know if that's good or bad..."
mc "Nie wiem, czy to dobrze, czy źle..."
scene ep1_cafe_maya28 with dissolve
#my "You're..."
my "Jesteś..."
#my "...different."
my "Dzięki różnym"
$ renpy.sound.stop(channel="sfx1", fadeout=3)
scene ep1_cafe_maya27 with dissolve
stop music fadeout 3
#mc "That doesn't make it any clearer."
mc "To nie czyni tego jaśniejszym."
scene ep1_cafe_maya30 with hpunch
#my "I'm different too."
my "jestem inny"
scene ep1_troy_fight with Fade(1.5,1,0.5)
play music "music/ep1/food_chain.mp3"
#mc "Hey. Safe to come in?"
mc "Hej. Możesz bezpiecznie wejść?"
#troy "..."
troy "..."
#mc "(What happened here...?)"
mc "Co się tu stało?"
scene ep1_troy_fight1 with dissolve
#mc "Are you ok?"
mc "Wszystko dobrze?"
#troy "Leave me alone."
troy "Zostaw mnie."
scene ep1_troy_fight2 with dissolve
#mc "Hey...where's my guitar?"
mc "Gdzie moja gitara?"
scene ep1_troy_fight1 with dissolve
#troy "..."
troy "..."
#troy "It's gone."
troy "wszystko zniknęło."
#mc "SAY WHAT!?"
mc "Że CO?"
scene ep1_troy_fight4 with dissolve
#troy "There was nothing I could do."
troy "Nie mogłam nic zrobić. "
scene ep1_troy_fight5 with dissolve
#mc "Are you fucking kidding me!? That's MY guitar!"
mc "Jaja sobie robisz!? TO moja gitara!"
#mc "Who the FUCK stole it!?"
mc "Kto to, KURWA, ukradł!?"
play sound "sound_effects/shove.mp3"
scene ep1_troy_fight6 with vpunch
#troy "Fuck off! I told you to leave me alone...you...you dick!"
troy "Spierdalaj! Mówiłem ci, żebyś zostawił mnie w spokoju...ty...ty kutasie!"
scene ep1_troy_fight7 with dissolve
#mc "TELL ME WHO STOLE IT!"
mc "POWIEDZ MI, KTO TO UKRADŁ!"
scene ep1_troy_fight8 with dissolve
#troy "Some fucking jocks stormed in and took it, ok!?"
troy "Jacyś pieprzeni sportowcy wpadli i go zabrali, ok!?"
scene ep1_troy_fight7 with dissolve
#mc "And you just let them do that!?"
mc "A ty im na to pozwalasz!?"
scene ep1_troy_fight8 with dissolve
#troy "You think I wanted this!?"
troy "Myślisz, że tego chciałem!?"
scene ep1_troy_fight7 with dissolve
#mc "You're a fucking asshole!!"
mc "Jesteś pieprzonym dupkiem!!"
play sound "sound_effects/shove.mp3"
scene ep1_troy_fight6 with vpunch
#troy "Get the fuck out!!! There's no fucking way that you're staying here anymore!"
troy "Wypierdalaj!!! Nie ma, kurwa, mowy, żebyś tu został!"
if tutorials:
    show white_screen with dissolve
    show screen majorChoiceScale
#    show text "{color=#ffffff}During the game, you will encounter major choices. These choices will shape your character with time.\nIf the choice you make is considered to be a {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} choice, one bar will be removed from the {size=+3}{color=#ffb052}{font=collegiate.ttf}CHICK{/font}{/color}{/size} side; vice versa.{/color}" with dissolve:
    show text "{color=#ffffff}Podczas gry napotkasz duże wybory. Te wybory ukształtują twoją postać z czasem.\nJeśli Twój wybór zostanie uznany za wybór {size=+3}{color=#ffb052}{font=collegiate.ttf}dik{/font}{/color}{/size}, jeden słupek zostanie usunięty ze strony {size=+3}{color=#ffb052}{font=collegiate.ttf}PISKLĘCIA{/font}{/color}{/size} i odwrotnie.{/color}" with dissolve:
        ypos 0.825
    $ renpy.pause()
#    show text "{color=#ffffff}After making several major {size=+3}{color=#ffb052}{font=collegiate.ttf}DIK{/font}{/color}{/size} or {size=+3}{color=#ffb052}{font=collegiate.ttf}CHICK{/font}{/color}{/size} choices you will be unable to progress on the opposite side past a certain point.\nBeware, eventually you may be forced to make good or bad decisions as a result of how you shaped your character.{/color}" with dissolve:
    show text "{color=#ffffff}Po dokonaniu kilku ważnych wyborów {size=+3}{color=#ffb052}{font=collegiate.ttf}dik{/font}{/color}{/size} lub {size=+3}{color=#ffb052}{font=collegiate.ttf}LASKA{/font}{/color}{/size} nie będziesz w stanie przejść po przeciwnej stronie poza pewien punkt.\nStrzeż się, w końcu możesz być zmuszony do podejmowania dobrych lub złych decyzji w wyniku tego, jak ukształtowałeś swoją postać.{/color}" with dissolve:
        ypos 0.825
    $ renpy.pause()
    hide text
    hide white_screen with dissolve
else:
    show screen majorChoiceScale
label makeChoice:
    menu:
#        "Beat him up":
        "Pobić go?":
#            $ bios_history_troy += "Because of Troy, my guitar got stolen. I lost my temper and punched him.\n\n"
            $ bios_history_troy += "Z powodu Troya moja gitara została skradziona. Straciłem panowanie nad sobą i uderzyłem go.\n \n"
            $ ep1_beat_up_troy = True
            $ bios_name_troy = True
            $ addCPenalty()
            $ renpy.pause(1)
            hide screen majorChoiceScale
            play sound "sound_effects/hit.mp3"
            scene ep1_troy_fight13 with hpunch
            $ renpy.pause()
            if minigames:
                $ brawlerStoryFight = "troy"
                $ brawlerStoryFightLabel = "ep1_after_troy_fight"
                jump app_brawler_label
                label ep1_after_troy_fight:
                $ sports_opponent_idx = 0
                $ brawlerStoryFight = ""
                $ brawlerStoryFightLabel = ""
                if ep1_beat_up_troy_won and brawler_difficulty == 3 and steamAchievements:
                    if not config.console and not config.developer:
                        $ achievement.grant("DORMMATEBEATDOWN")
                        init $ achievement.register("DORMMATEBEATDOWN")
                        $ achievement.Sync()
            else:
                $ ep1_beat_up_troy_won = True
            if ep1_beat_up_troy_won:
#                $ bios_history_mc += "I beat Troy up.\n\n"
                $ bios_history_mc += "Pobiłem Troję.\n \n"
                $ bios_name_mc = True
                $ chat_new_bios = True
                play sound "sound_effects/whoosh.mp3"
                scene ep1_troy_fight14 with dissolve
                $ renpy.pause(0.5)
                play sound "sound_effects/hit.mp3"
                scene ep1_troy_fight13 with hpunch
                $ renpy.pause(0.5)
                scene ep1_troy_fight16 with dissolve
#                mc "THIS IS FAR FROM FUCKING OVER, TROY!"
                mc "TO JESZCZE NIE KONIEC, TROY!"
                stop music fadeout 3
                scene ep1_troy_fight17b with dissolve
#                mc "I'LL GET YOU FOR THIS!!!"
                mc "DOPADNĘ CIĘ ZA TO!!!"
#                troy "..."
                troy "..."
            else:
#                $ bios_history_mc += "I tried to beat Troy up.\n\n"
                $ bios_history_mc += "Próbowałem pobić Troję.\n \n"
                $ bios_name_mc = True
                $ chat_new_bios = True
                play sound "sound_effects/hit.mp3"
                scene ep1_troy_fight14b with dissolve
                $ renpy.pause(0.5)
                scene ep1_troy_fight16b with dissolve
#                troy "I SAID GET THE FUCK OUT!!!"
                troy "POWIEDZIAŁEM WYPIERDALAJ!!!"
                scene ep1_troy_fight17b with dissolve
                stop music fadeout 3
#                mc "I'LL FUCKING GET YOU FOR THIS!!!"
                mc "DOPADNĘ CIĘ ZA TO!!!"
#                troy "..."
                troy "..."
#        "Storm out":
        "Storm out":
#            $ bios_history_mc += "I was angry, but I didn't beat Troy up.\n\n"
            $ bios_history_mc += "Byłem zły, ale nie pobiłem Troya.\n \n"
#            $ bios_history_troy += "Because of Troy, my guitar got stolen. I stormed out screaming when he told me.\n\n"
            $ bios_history_troy += "Z powodu Troya moja gitara została skradziona. Wybiegłam z krzykiem, kiedy mi powiedział.\n \n"
            $ ep1_beat_up_troy = False
            $ bios_name_mc = True
            $ bios_name_troy = True
            $ chat_new_bios = True
            $ addDPenalty()
            $ renpy.pause(1)
            hide screen majorChoiceScale
            stop music fadeout 3
            scene ep1_troy_fight17b with dissolve
#            mc "I'LL GET YOU FOR THIS, TROY!"
            mc "DOPADNĘ CIĘ ZA TO, TROY!"
#            troy "..."
            troy "..."
play music "music/ep1/unknown_power.mp3"
scene ep1_reception with fade
#mc "Hey, reception lady! Wait! I need help!"
mc "Hej, recepcjonistko! Czekaj! Potrzebuję pomocy!"
scene ep1_reception1 with dissolve
#rc "I'm going home for the day; you can come back tomorrow morning."
rc "Wracam do domu na jeden dzień; możesz wrócić jutro rano."
scene ep1_reception1b with dissolve
#mc "This is urgent! I need somewhere else to stay!"
mc "To pilne! Muszę się gdzieś zatrzymać!"
#mc "I got into a huge fight with my dorm mate, and there's just no way I can stay there any longer!"
mc "Pokłóciłem się z kolegą z akademika i nie ma mowy, żebym mógł tam dłużej zostać!"
scene ep1_reception1 with dissolve
#rc "Oh, I'm afraid it's not that simple. There's a whole process behind changing dorms that-"
rc "Obawiam się, że to nie takie proste. Istnieje cały proces zmiany akademika, który…"
scene ep1_reception1b with dissolve
#mc "Please! This is an emergency!"
mc "Proszę! To nagły wypadek!"
scene ep1_reception1 with dissolve
#rc "Calm down. There's nothing that can be done for you at the moment."
rc "Uspokój się. W tej chwili nic nie można dla Ciebie zrobić."
#rc "Try to get along with your dorm mate or maybe stay with a friend until we can get you a new dorm."
rc "Spróbuj dogadać się ze swoim kolegą z akademika lub zostań z przyjacielem, dopóki nie kupimy ci nowego akademika."
scene ep1_reception1b with dissolve
#mc "Really? That's all you can do!?"
mc "Naprawdę? To wszystko, co możesz zrobić!?"
scene ep1_reception1 with dissolve
#rc "For now...yes."
rc "Na razie tak."
#rc "Or...you could try talking to the different fraternities and see if they will help you."
rc "Albo...możesz spróbować porozmawiać z różnymi bractwami i zobaczyć, czy ci pomogą."
scene ep1_reception7 with dissolve
#mc "(The fraternities...really?)"
mc "(Bractwa...naprawdę?)"
#mc "(The nerds don't have a house...)"
mc "(Kujony nie mają domu...)"
#mc "(The jocks? Yeah, right...)"
mc "(Sportowcy? Tak, tak...)"
stop music fadeout 5
#mc "(The preps? Good luck getting close to that mansion...)"
mc "(Przygotowania? Powodzenia w zbliżeniu się do tej rezydencji...)"
#mc "(...)"
mc "(...)"
#mc "(The DIKs.)"
mc "(The DIKs.)"
play music "music/ep1/my_heart.mp3"
scene ep1_diks with wiperight
#dikc "CHUG! CHUG! CHUG!"
dikc "Do dna, do dna, do dna."
#dikc "YEAH!!!"
dikc "Tak"
scene ep1_diks1 with dissolve
#rs "Ladies and not-so-gentlemen!"
rs "Panie i nie tak dżentelmeni!"
#rs "The winner is the reigning Massive DIK..."
rs "Zwycięzcą zostaje panujący Massive DIK..."
#rs "TOMMY!!!"
rs "Tommy"
play sound "sound_effects/burp.mp3"
#tm "*{i}BURP{/i}*!!!"
tm "Odbijanie"
scene ep1_diks4 with dissolve
#tm "Fucking learn how to drink, Jacob!"
tm "Naucz się kurwa pić, Jacob!"
scene ep1_diks4b with dissolve
#jac "Man, fuck you. You probably were breastfed beer as a kid."
jac "Człowieku, pierdol się. Pewnie w dzieciństwie byłeś piwem karmionym piersią."
scene ep1_diks4c with dissolve
#tm "Get fucked! I get more tits in my mouth these days than I did back then."
tm "Pieprz się! W dzisiejszych czasach mam więcej cycków w ustach niż wtedy."
scene ep1_diks5 with dissolve
#tm "Hey! Hold the fuck up! Who's that!?"
tm "Hej! Stój, kurwa! Kto to jest!?"
#tm "Is that a jock!?"
tm "Czy to sportowiec!?"
scene ep1_diks6 with dissolve
#mc "Erm...hi, the door was open and I-"
mc "Erm...cześć, drzwi były otwarte i ja-"
scene ep1_diks6b with dissolve
#rs "Hm...doesn't look like a jock to me."
rs "Hm...nie wygląda mi na sportowca."
scene ep1_diks6c with dissolve
if intervenedChad:
    $ RPdiks += 1
#    jac "Nah! That's no jock!"
    jac "Nie! To nie jest sportowiec!"
#    jac "This is the freshy I was telling you about."
    jac "To jest ta świeża rzecz, o której ci mówiłem."
#    jac "He almost gave it to Chad in the cafeteria!"
    jac "Prawie dał go Czadowi w stołówce!"
    scene ep1_diks9b with dissolve
#    hg "Wow!"
    hg "Wow!"
#    tm "Almost, huh? That doesn't cut it."
    tm "Prawie, co? To nie wystarczy."
    scene ep1_diks10 with dissolve
#    rs "Dude, come on! It's not like you would have tried to go head-to-head with Chad."
    rs "Stary, daj spokój! Przecież nie próbowałbyś iść łeb w łeb z Czadem."
else:
#    jac "No, this is the freshy who got a wedgie from Dawe!"
    jac "Nie, to ten świeżak, który dostał kotleta od Dawe!"
    scene ep1_diks9c with dissolve
#    hg "Haha!"
    hg "Ha, ha!"
#    tm "Haha! Dawe's such a fucking cunt!"
    tm "Haha! Dawe to taka pieprzona cipa!"
scene ep1_diks11 with dissolve
#rs "Hey! Who are you?"
rs "Hej! Kim jesteś?"
#mc "[name]."
mc "[name]."
#rs "How do you feel about the jocks?"
rs "Co sądzisz o sportowcach?"
scene ep1_diks6 with dissolve
menu:
#    "I don't hate them":
    "Nie nienawidzę ich":
        $ RPdiks -= 1
#        mc "I don't hate them, but they did steal something very valuable from me."
        mc "Nie nienawidzę ich, ale ukradli mi coś bardzo cennego."
        scene ep1_diks9b with dissolve
#        tm "This fucking guy..."
        tm "Ten pieprzony facet..."
#        tm "He's either stupid or a jock...or both."
        tm "Albo jest głupcem, albo sportowcem...albo jednym i drugim."
        scene ep1_diks10 with dissolve
#        rs "Hm...maybe he's not been enlightened."
        rs "Hmm...może nie został oświecony."
        scene ep1_diks9b with dissolve
#        tm "Pff..."
        tm "Pff..."
#    "I hate them":
    "Nienawidzę ich.":
        $ RPdiks += 1
        if dtype > 0:
#            mc "I hate the fucking jocks!"
            mc "Nienawidzę jebanych sportowców!"
        else:
#            mc "I don't like them at all."
            mc "W ogóle mi się nie podobają."
#        mc "They stole something very valuable from me..."
        mc "Ukradli mi coś bardzo cennego..."
scene ep1_diks6b with dissolve
#rs "Yeah. He's not a jock...right?"
rs "Tak. On nie jest sportowcem...prawda?"
scene ep1_diks6 with dissolve
if dtype > 0:
#    mc "I may have the physique for it, but no, I'm not a jock."
    mc "Mogę mieć do tego odpowiednią sylwetkę, ale nie, nie jestem sportowcem."
else:
#    mc "No, I'm just me."
    mc "Nie, jestem tylko sobą."
    scene ep1_diks30 with dissolve
#    tm "How cute!"
    tm "O jak słodko!"
scene ep1_diks17 with dissolve
#ri "Yeah, he's not a jock."
ri "Tak, nie jest sportowcem."
#ri "This guy was hitting on Sage before."
ri "Ten facet wcześniej podrywał Sage."
$ guideSuggestedPage = 41
#ri "No jock would be stupid enough to do that."
ri "Żaden sportowiec nie byłby na tyle głupi, aby to zrobić."
scene ep1_diks6 with dissolve
menu:
#    "Play along":
    "Grać razem.":
        $ ep1_played_along = True
        $ RPdiks += 1
#        mc "Yeah, that's right."
        mc "Tak, akurat. "
        scene ep1_diks18 with dissolve
#        rs "HAHA! This guy is fucking DIK material!"
        rs "HAHA! Ten facet to pieprzony materiał na DIK!"
        scene ep1_diks21 with dissolve
#    "Deny":
    "Odmów":
        $ ep1_played_along = False
#        mc "No, that's just not true!"
        mc "To tylko żart."
        scene ep1_diks6b with dissolve
#        rs "Yeah, I don't know what to make of this guy."
        rs "Nie wiem co o tym myśleć."
        scene ep1_diks6 with dissolve
#mc "Here's the deal, I came here looking for some place to stay."
mc "Sprawa wygląda tak, że przyjechałem tu w poszukiwaniu miejsca na nocleg."
if ep1_beat_up_troy:
#    mc "I got into a fight with my dorm mate, and I can't stay there anymore."
    mc "Pokłóciłem się z kolegą z akademika i nie mogę już tam zostać."
else:
#    mc "I got into an argument with my dorm mate, and I can't stay there anymore."
    mc "Pokłóciłem się z kolegą z akademika i nie mogę już tam zostać."
scene ep1_diks11 with dissolve
#rs "Who's your dorm mate?"
rs "Kto jest twoim kumplem z akademika?"
scene ep1_diks6 with dissolve
if dtype > 0:
#    mc "Some fucking asshole named Troy."
    mc "Jakiś pieprzony dupek o imieniu Troy."
else:
#    mc "Just some guy named Troy."
    mc "Po prostu jakiś facet o imieniu Troy."
scene ep1_diks6c with dissolve
#jac "Long black hair?"
jac "Długie czarne włosy?"
#mc "Yeah."
mc "Tak."
scene ep1_diks18 with dissolve
if not ep1_played_along:
#    rs "See? This guy is DIK material!"
    rs "Widzisz? Ten facet jest materiałem DIK!"
else:
#    rs "That fucking seals the deal for me!"
    rs "To cholernie przypieczętowuje umowę dla mnie!"
#rs "That's another jock he's got issues with!"
rs "To kolejny sportowiec, z którym ma problemy!"
scene ep1_diks21 with dissolve
#mc "Wait, Troy's not a jock."
mc "Chwila, Troy nie jest sportowcem."
scene ep1_diks6c with dissolve
#jac "Former jock. He got kicked out."
jac "Dawny sportowiec. Wyrzucili go."
scene ep1_diks18 with dissolve
#rs "That's just semantics! A jock's a fucking jock!"
rs "To tylko semantyka! Sportowiec to pieprzony sportowiec!"
scene ep1_diks21b with dissolve
#tm "Yeah, I don't know. I say we test him."
tm "Tak, nie wiem. Myślę, że powinniśmy go przetestować."
scene ep1_diks21c with dissolve
#rs "You want to pledge our house, yes?"
rs "Chcesz zastawić nasz dom, tak?"
scene ep1_diks21 with dissolve
#mc "If that would get me a place to stay, then yes."
mc "Jeśli dzięki temu miałabym gdzie się zatrzymać, to tak."
scene ep1_diks27 with dissolve
#tm "Rusty...he must be tested."
tm "Rusty...musi zostać przetestowany."
scene ep1_diks18 with dissolve
#rs "Gah, this is tough. But rules are rules!"
rs "Gah, to jest trudne. Ale zasady to zasady!"
#rs "A test it is."
rs "To jest test."
scene ep1_diks21 with dissolve
#mc "What do I have to do?"
mc "Co muszę zrobić?"
scene ep1_diks30 with dissolve
#tm "Oh, it's really simple."
tm "To bardzo proste."
#tm "You need to bring us one small item from the HOTs, and we'll consider your pledge."
tm "Musisz dostarczyć nam jeden mały przedmiot z sekcji Hot, a my rozważymy Twoje wsparcie."
#mc "An item?"
mc "Elementu?"
scene ep1_diks6c with dissolve
#jac "A pair of panties, dude. We've all done it."
jac "Para majtek, stary. Wszyscy to zrobiliśmy."
#jac "Think of it as an...initiation."
jac "Potraktuj to jako...inicjację."
if dtype > 0:
    scene ep1_diks32 with dissolve
#    mc "Hey, you! How about you give me yours, and this will be all over?"
    mc "Hej, ty! A może oddasz mi swój i będzie po wszystkim?"
#    tm "Hah! No way it's that simple."
    tm "Hah! Nie ma mowy, żeby to było takie proste."
scene ep1_diks30 with dissolve
#tm "How you go about and do it, that's up to you."
tm "To, jak to zrobisz, zależy od Ciebie."
#tm "But you must enter their house and leave with a pair of panties. Those are the rules."
tm "Ale musisz wejść do ich domu i wyjść z parą majtek. Takie są zasady."
if dtype > 0:
#    mc "Fine, I'll be back in a minute."
    mc "Będę z powrotem za minutę!"
else:
#    mc "Ok...I'll try..."
    mc "Ok...spróbuję..."
stop music fadeout 3
scene ep1_diks36 with dissolve
#tm "Hey. Fresh bait on the hook."
tm "Hej. Świeża przynęta na haczyk."
jump ep1_freeroam_hots_label
label ep1_raid_panties_label:

scene ep1_panties with dissolve
$ renpy.block_rollback()
stop music fadeout 5
#mc "(Yes! These will do perfectly!)"
mc "(Tak! Te będą idealne!)"
#cam "Why do I have to do that?"
cam "Poważnie, dlaczego muszę to robić? "
#mc "(Shit! Someone's coming.)"
mc "(Cholera! Ktoś idzie.)"
scene ep1_panties1 with dissolve
play music "music/ep1/funk_rock.mp3"
#mc "(I'll hide in here...)"
mc "(Schowam się tutaj...)"
#qu "Think of it as a rite of passage or an initiation. Something we all do at least once."
qu "Pomyśl o tym jako o rytuale przejścia lub inicjacji. Coś, co wszyscy robimy przynajmniej raz."
scene ep1_panties3 with dissolve
#cam "If that's really the case...I'll do it."
cam "Jeśli naprawdę tak jest... to ja to zrobię."
#qu "Good girl."
qu "Dobra dziewczyna. "
scene ep1_panties4 with dissolve
#mc "(Holy shit! What an ass...)"
mc "(Jasna cholera! Co za dupek...)"
#mc "(I can't believe this...if they see me, I'm totally screwed.)"
mc "(Nie mogę w to uwierzyć...jeśli mnie zobaczą, mam totalnie przerąbane.)"
#qu "Just follow the instructions we give you, and you'll be fine."
qu "Postępuj zgodnie z podanymi przez nas instrukcjami, a wszystko będzie dobrze."
scene ep1_panties5 with dissolve
#qu "Huh!? Is somebody in there?"
qu "Co!? Czy ktoś tam jest?"
menu:
#    "Stay quiet":
    "Zachowaj ciszę":
#        mc "..."
        mc "..."
#        qu "You in the booth! Speak up!"
        qu "Ty w kabinie! Głośniej!"
#    "Act like a girl":
    "Zachowuj się jak dziewczyna":
#        mc "*{i}High voice{/i}* It's just me, girls."
        mc "*{i}Wysoki głos{/i}* To tylko ja, dziewczyny."
#        qu "And who would that be?"
        qu "A dokładniej?"
#        mc "Erm...Suzanne?"
        mc "Hmm...Suzanne?"
scene ep1_panties6 with dissolve
#qu "What do we have here? A fucking perv!"
qu "Co my tu mamy? Pierdolony zboczeniec!"
#mc "Please, I can explain!"
mc "Proszę, mogę to wyjaśnić!"
scene ep1_panties7 with dissolve
#qu "Yeah, go ahead and explain why you're standing here holding a pair of panties with a hard-on."
qu "Tak, śmiało, wyjaśnij, dlaczego tu stoisz, trzymając majtki z erekcją."
#mc "Oh shit..."
mc "---"
scene ep1_panties6 with dissolve
#qu "Please. I'm all ears."
qu "Proszę. Zamieniam się w słuch."
scene ep1_panties8 with dissolve
#qu "Were you enjoying yourself watching Camila getting naked in front of you?"
qu "Czy dobrze się bawiłeś, patrząc, jak Camila rozbiera się przed tobą?"
#qu "She's got a nice ass, huh?"
qu "Ma ładny tyłek, co?"
menu:
#    "Agree":
    "Zgadzam się":
        $ dk(1)
#        mc "Yeah, her ass is amazing."
        mc "Tak, jej tyłek jest niesamowity."
#    "Try to leave":
    "to leave":
        $ dk(-1)
#        mc "I'm so sorry; I'm leaving."
        mc "Tak mi przykro; wychodzę."
        scene ep1_panties9 with dissolve
#        qu "Whoa! Whoa! Not so fast there, [mc_quinn]!"
        qu "Whoa! Whoa! Nie tak szybko, [mc_quinn]!"
scene ep1_panties10 with dissolve
#qu "Show us what you hide in those shorts."
qu "Pokaż nam, co ukrywasz w tych szortach."
#qu "Strip!"
qu "Taśma"
scene ep1_panties12 with dissolve
#mc "Why would I do that?"
mc "Niby dlaczego?"
scene ep1_panties11 with dissolve
#qu "Strip, [mc_quinn], or I'll make sure that everyone hears about how you snuck into our showers trying to wank to us being naked!"
qu "Rozbierz się, [mc_quinn], albo upewnię się, że wszyscy usłyszą o tym, jak wślizgnąłeś się pod nasze prysznice, próbując walić konia, żebyśmy byli nadzy!"
scene ep1_panties12 with dissolve
#mc "Come on, that's not the truth!"
mc "Daj spokój, to nieprawda!"
scene ep1_panties11 with dissolve
stop music fadeout 3
#qu "It will be. Strip!"
qu "Będzie. Rozbieraj się!"
play sound "sound_effects/clothes.mp3"
label ep1_quinn_lewd:

if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_quinn == None:
        $ mc_quinn = "pervert"
    else:
        $ mc_quinn = persistent.mc_quinn
    if persistent.quinn == None:
        $ quinn = "Quinn"
    else:
        $ quinn = persistent.quinn
scene ep1_panties10 with dissolve
hide screen phone_screen
#mc "Fine! There! You've seen me too now. Can I leave?"
mc "Dobra! No proszę! Ty też mnie teraz widziałaś. Czy mogę wyjść?"
#qu "Camila. Come over here."
qu "Camila. Chodź tutaj."
play music "music/ep1/slow_day_blues.mp3"
scene ep1_panties13 with dissolve
#qu "Show him the goods."
qu "Pokaż mu towar."
scene ep1_panties14 with dissolve
#mc "Wait, what?"
mc "Znowu na chwilę otrzeźwiałem."
scene ep1_panties15 with dissolve
#mc "Oh my god..."
mc "O Boże."
scene ep1_panties16 with dissolve
#qu "See? I knew it. You are getting off to watching Camila naked."
qu "Widzisz? Wiedziałem. Zaczynasz oglądać nagą Camilę."
#qu "Look at that hard cock!"
qu "Spójrz na tego twardego kutasa!"
scene ep1_panties17 with dissolve
#qu "I bet this is what you really came to see..."
qu "Założę się, że to jest to, co naprawdę przyszedłeś zobaczyć..."
init 500 image anim_quinn_kiss_ep1 = Movie(channel="anim_quinn_kiss_ep1", play="images/movies/ep1/anim_quinn_kiss_ep1.webm")
scene anim_quinn_kiss_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
pause
menu:
#    "Get involved":
    "Zaangażuj się":
        $ ep1_lewd_camila_quinn = True
        $ dk(1)
        scene ep1_panties18 with dissolve
#        mc "Yeah, that looks really nice..."
        mc "Wygląda naprawdę nieźle!"
        scene ep1_panties19 with dissolve
#        qu "Grab his cock, Camila."
        qu "Chwyć jego kutasa, Camilo."
#        qu "Give this pervert what he really came for."
        qu "Daj temu zboczeńcowi to, po co naprawdę przyszedł."
        init 500 image anim_camila_hj_ep1 = Movie(channel="anim_camila_hj_ep1", play="images/movies/ep1/anim_camila_hj_ep1.webm")
        scene anim_camila_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Mmm...that's it. Can you feel how his cock is pulsating in your hand?"
        qu "Mmm...to wszystko. Czujesz, jak jego kutas pulsuje w Twojej dłoni?"
#        qu "I bet this guy's a virgin."
        qu "Założę się, że ten facet jest prawiczkiem."
#        qu "Coming in here trying to jack off to little girls. That's fucking disgusting!"
        qu "Przychodzę tu, próbując zwalić konia małym dziewczynkom. To kurewsko obrzydliwe!"
#        mc "(Wow...I've never gotten a handjob from two girls before...)"
        mc "(Łał...Nigdy wcześniej nie obciągały mi dwie dziewczyny...)"
#        mc "(This feels amazing. The way Camila is gripping my cock while Quinn is stroking the head...)"
        mc "(To niesamowite uczucie. Sposób, w jaki Camila chwyta mojego kutasa, podczas gdy Quinn głaszcze głowę...)"
        pause
        init 500 image anim_quinn_kiss_ep1 = Movie(channel="anim_quinn_kiss_ep1", play="images/movies/ep1/anim_quinn_kiss_ep1.webm")
        scene anim_quinn_kiss_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        mc "(They're really going at it... Fuck, this is just too hot...)"
        mc "(Naprawdę zaczynają... Kurwa, jest po prostu za gorąco...)"
        pause
        init 500 image anim_quinn_kiss2_ep1 = Movie(channel="anim_quinn_kiss2_ep1", play="images/movies/ep1/anim_quinn_kiss2_ep1.webm")
        scene anim_quinn_kiss2_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
        init 500 image anim_camila_hj_ep1 = Movie(channel="anim_camila_hj_ep1", play="images/movies/ep1/anim_camila_hj_ep1.webm")
        scene anim_camila_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Keep going, Camila... He isn't twitching yet."
        qu "Kontynuuj, Camila... Jeszcze nie drgnął."
#        qu "That means he's not ready to cum."
        qu "Oznacza to, że nie jest gotowy do orgazmu."
#        qu "Keep massaging that pervert's cock."
        qu "Masuj kutasa tego zboczeńca."
        pause
        init 500 image anim_camile_ass_ep1 = Movie(channel="anim_camile_ass_ep1", play="images/movies/ep1/anim_camile_ass_ep1.webm")
        scene anim_camile_ass_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        mc "(She has the softest ass I've ever felt...)"
        mc "(Ma najdelikatniejszy tyłek, jaki kiedykolwiek czułem...)"
        pause
#        cam "Quinn, he's touching my ass..."
        cam "Quinn, on dotyka mojego tyłka..."
#        qu "I fucking told you that he's a pervert!"
        qu "Mówiłem ci, że to zboczeniec!"
        scene ep1_panties19b with dissolve
#        qu "Hey! Did I say you could touch her, you pervy little cunt!?"
        qu "Hej! Powiedziałem, że możesz ją dotknąć, ty zboczona cipo!?"
        scene ep1_panties19c with dissolve
#        mc "Come on; I thought we were having fun..."
        mc "Daj spokój, myślałem, że dobrze się bawimy..."
        if _in_replay and not persistent.ep1_quinn_full:
            scene ep1_panties_leaving1 with hpunch
#            qu "PERVERT! SOMEBODY CALL SECURITY!!!"
            qu "ZBOCZENIEC! NIECH KTOŚ WEZWIE OCHRONĘ!!!"
            $ renpy.end_replay()
        elif dtype < 2 and not _in_replay:
            $ persistent.ep1_quinn = True
            $ calcScenes()
            stop music
            play sound "sound_effects/shove.mp3"
            scene ep1_panties_leaving1 with hpunch
#            qu "PERVERT! SOMEBODY CALL SECURITY!!!"
            qu "ZBOCZENIEC! NIECH KTOŚ WEZWIE OCHRONĘ!!!"
            play music "music/ep4/driving_rock.mp3"
            jump ep1_after_raid_label
        scene ep1_panties19d with dissolve
#        qu "Fun, huh?"
        qu "Fajnie, co?"
#        qu "Heh, I like your confidence."
        qu "Podoba mi się twoja pewność siebie."
        scene ep1_panties22 with dissolve
#        qu "But you're in no position to be calling the shots here."
        qu "Ale nie jesteś w sytuacji, w której możesz tu wydawać rozkazy."
#        qu "Do you understand?"
        qu "Czy rozumie Pan/i? "
#        mc "*{i}Muffled voice{/i}* Mhm."
        mc "*{i}Stłumiony głos{/i}* Mhm."
#        qu "Camila. You know what to do."
        qu "Camila. Wiesz, co robić."
        scene ep1_panties20 with dissolve
#        qu "Jack him off."
        qu "Zwal mu konia."
        scene ep1_panties21 with dissolve
#        qu "Let me know when the fucker starts twitching."
        qu "Daj mi znać, kiedy skurwiel zacznie się trząść."
        init 500 image anim_cam_hj_ep1 = Movie(channel="anim_cam_hj_ep1", play="images/movies/ep1/anim_cam_hj_ep1.webm")
        scene anim_cam_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Do you like that, [mc_quinn]?"
        qu "Lubisz to?"
#        qu "Do you like the way her soft hands rub your cock?"
        qu "Podoba ci się sposób, w jaki jej miękkie dłonie pocierają twojego kutasa?"
        pause
        scene ep1_panties22 with dissolve
#        qu "What's that? You want to watch her jerking you off?"
        qu "Co to jest? Chcesz popatrzeć, jak cię masturbuje?"
#        qu "That's not going to happen, you little shit!"
        qu "Tak się nie stanie, gnojku!"
        init 500 image anim_quinn_lick_ep1 = Movie(channel="anim_quinn_lick_ep1", play="images/movies/ep1/anim_quinn_lick_ep1.webm")
        scene anim_quinn_lick_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Mmm... You taste good..."
        qu "--- "
        pause
        scene ep1_panties22 with dissolve
#        qu "How's it going, Camila? Is he twitching yet?"
        qu "Jak leci, Camila? Czy on już się trzęsie?"
        init 500 image anim_cam_hj_ep1 = Movie(channel="anim_cam_hj_ep1", play="images/movies/ep1/anim_cam_hj_ep1.webm")
        scene anim_cam_hj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        cam "No...nothing yet."
        cam "Nie... jeszcze nic."
        pause
        scene ep1_panties22 with dissolve
#        qu "Put it in another gear, then."
        qu "W takim razie wrzuć inny bieg."
        scene ep1_panties23 with dissolve
#        cam "You mean faster?"
        cam "Masz na myśli szybszy?"
#        qu "No. Use your mouth and hands."
        qu "Nie. Użyj ust i rąk."
        init 500 image anim_cam_bj_ep1 = Movie(channel="anim_cam_bj_ep1", play="images/movies/ep1/anim_cam_bj_ep1.webm")
        scene anim_cam_bj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        cam "*{i}Mphff...{/i}*"
        cam "*{i}Mphff...{/i}*"
#        qu "That's it, girl. Suck that dick."
        qu "To jest to, dziewczyno. Ssij tego kutasa."
#        qu "You should see this, [mc_quinn]. She's really doing a fine job handling that cock."
        qu "Powinieneś to zobaczyć, [mc_quinn]. Naprawdę świetnie sobie radzi z tym kutasem."
#        qu "I can tell that she's done this many times before. Haven't you, Camila?"
        qu "Mogę powiedzieć, że robiła to już wiele razy. Prawda, Camilo?"
#        cam "*{i}Mphff...{/i}*"
        cam "*{i}Mphff...{/i}*"
        pause
        init 500 image anim_quinn_lick_ep1 = Movie(channel="anim_quinn_lick_ep1", play="images/movies/ep1/anim_quinn_lick_ep1.webm")
        scene anim_quinn_lick_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "You like having two warm tongues against your body, [mc_quinn]?"
        qu "Lubisz mieć dwa ciepłe języki na swoim ciele, [mc_quinn]?"
        pause
        init 500 image anim_cam_bj_var_ep1 = Movie(channel="anim_cam_bj_var_ep1", play="images/movies/ep1/anim_cam_bj_var_ep1.webm")
        scene anim_cam_bj_var_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Looks like she's enjoying that cock..."
        qu "Wygląda na to, że podoba jej się ten kutas..."
#        qu "She's such a slut. Aren't you Camila?"
        qu "Ona jest taką zdzirą. Czy ty nie jesteś Camila?"
#        cam "*{i}Mphff...{/i}*"
        cam "*{i}Mphff...{/i}*"
        pause
        init 500 image anim_cam_bj_ep1 = Movie(channel="anim_camila_bj_ep1", play="images/movies/ep1/anim_cam_bj_ep1.webm")
        scene anim_cam_bj_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        qu "Hm...he isn't getting closer..."
        qu "Hm...nie zbliża się..."
        pause
#        qu "What if he got to look into your eyes, Camila? Is this what you wanna see, you fucking pervert?"
        qu "Co jeśli spojrzy ci w oczy, Camilo? Czy to właśnie chcesz zobaczyć, pieprzony zboczeńcu?"
        init 500 image anim_cam_bj_long_ep1 = Movie(channel="anim_cam_bj_long_ep1", play="images/movies/ep1/anim_cam_bj_long_ep1.webm")
        scene anim_cam_bj_long_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
        pause
#        qu "Wow, she's good at that!"
        qu "Wow, jest w tym dobra!"
#        qu "I didn't know a freshy could suck cock that well..."
        qu "Nie wiedziałem, że świeżak może tak dobrze ssać kutasa..."
#        qu "You'll be a sorority sister in no time, Camila."
        qu "Niedługo zostaniesz siostrą z bractwa, Camilo."
#        qu "Hm...what was that? I think the pervert here twitched when I called her sister."
        qu "Hm...co to było? Myślę, że zboczeniec drgnął, kiedy zadzwoniłem do jej siostry."
#        qu "What's wrong with you?"
        qu "Co z tobą jest nie tak? "
#        mc "*{i}Mphff...{/i}*"
        mc "*{i}Mphff...{/i}*"
#        qu "Let's try that again..."
        qu "Spróbujmy jeszcze raz."
#        qu "Do you like when Sister Camila is sucking your cock?"
        qu "Lubisz, gdy siostra Camila ssała twojego kutasa?"
        pause
#        qu "Oh! Now he's twitching for sure!"
        qu "O! Teraz na pewno się trzęsie!"
        scene ep1_panties26 with dissolve
#        qu "Camila! Stop it!"
        qu "Camila! Przestań!"
        scene ep1_panties27 with dissolve
        stop music fadeout 3
#        qu "Here, take your fucking panties!"
        qu "Masz, weź swoje pieprzone majtki!"
#        qu "And get the fuck out of here!"
        qu "Wypierdalaj stąd!"
        play music "music/ep4/driving_rock.mp3"
#        mc "Huh? But what about my clothes?"
        mc "Ale co z moimi ubraniami?"
        play sound "sound_effects/shove.mp3"
        scene ep1_panties_leaving1 with hpunch
#        qu "PERVERT! SOMEBODY CALL SECURITY!!!"
        qu "ZBOCZENIEC! NIECH KTOŚ WEZWIE OCHRONĘ!!!"
        $ persistent.ep1_quinn = True
        $ persistent.ep1_quinn_full = True
        $ renpy.end_replay()
        $ calcScenes()
        jump ep1_after_raid_label
#    "Leave":
    "Opuść":
        $ renpy.end_replay()
        $ ep1_lewd_camila_quinn = False
        $ dk(-1)
#        mc "Nope, sorry. I'm leaving."
        mc "Nie, przepraszam. Wychodzę."
        scene ep1_panties_leaving with dissolve
#        qu "Leave the clothes."
        qu "Zostaw ubranie."
        play music "music/ep4/driving_rock.mp3"
#        mc "What!?"
        mc "Co?!"
        play sound "sound_effects/shove.mp3"
        scene ep1_panties_leaving1 with hpunch
#        qu "PERVERT! SOMEBODY CALL SECURITY!!!"
        qu "ZBOCZENIEC! NIECH KTOŚ WEZWIE OCHRONĘ!!!"
        jump ep1_after_raid_label
label ep1_after_raid_label:

play sound "sound_effects/door_slam.mp3"
scene ep1_raid2e with hpunch
play sound "sound_effects/door_lock.mp3"
#mc "(FUCK! FUCK! FUCK!)"
mc "Kurwa, kurwa, kurwa."
scene ep1_panties_leaving3 with dissolve
#hg "AHHH!!!"
hg "Aaach!!! "
#mc "I'M SO SORRY! FUCK!"
mc "Przepraszam! "
scene ep1_panties_leaving3b with dissolve
#hg "OH MY GOD! PERVERT!"
hg "O MÓJ BOŻE! ZBOCZENIEC!"
#mc "NO, I'M REALLY NOT!"
mc "NIE, NAPRAWDĘ NIE JESTEM!"
#mc "SORRY!"
mc "Niestety...."
scene ep1_panties_leaving4 with dissolve
#hg "Hahaha!"
hg "Ha!Ha!"
$ bios_camila = True
$ bios_quinn = True
if ep1_lewd_camila_quinn:
    if dtype >= 2:
#        $ bios_history_camila = "Camila gave me a handjob and a blowjob... If Quinn just would have let me finish, it would have been amazing.\n\n"
        $ bios_history_camila = "Camila zrobiła mi loda i zrobiła loda... Gdyby Quinn pozwolił mi dokończyć, byłoby niesamowicie.\n \n"
    else:
#        $ bios_history_camila = "Camila gave me a handjob... If Quinn just would have let me finish, it would have been amazing.\n\n"
        $ bios_history_camila = "Camila obciągnęła mi... Gdyby Quinn pozwolił mi dokończyć, byłoby niesamowicie.\n \n"
#    $ bios_history_quinn += "Quinn played me like a fiddle. I really thought I was going to fuck her and Camila in that bathroom...\nShe stole my clothes and the key to my dorm.\n\n"
    $ bios_history_quinn += "Quinn pogrywał ze mną jak na skrzypcach. Naprawdę myślałem, że przelecę ją i Camilę w łazience...\nUkradła moje ubrania i klucz do mojego akademika.\n \n"
else:
#    $ bios_history_camila = "I saw Camila naked today. She has a great body.\n\n"
    $ bios_history_camila = "Widziałam dziś nagą Camilę. Ma świetne ciało.\n \n"
#    $ bios_history_quinn += "I left as fast as I could when Quinn and Camila confronted me. She stole my clothes and the key to my dorm.\n\n"
    $ bios_history_quinn += "Wyszedłem tak szybko, jak mogłem, kiedy Quinn i Camila stanęły ze mną twarzą w twarz. Ukradła moje ubrania i klucz do mojego akademika.\n \n"
$ bios_name_camila = True
$ bios_name_quinn = True
$ chat_new_bios = True
$ current_task = "None"
$ chat_new_tasks = False
scene ep1_panties_leaving5 with fade
#mc "(I'm fucking freezing...)"
mc "(Kurwa marznę...)"
#mc "(I got the panties...they have to let me in!)"
mc "(Mam majtki...muszą mnie wpuścić!)"
play sound "sound_effects/door_bang.mp3"
scene ep1_panties_leaving7 with hpunch
#mc "Hey!!! Open up!"
mc "Hej, otwórz!... "
scene ep1_panties_leaving8 with dissolve
#tm "Haha! What the fuck is this!?"
tm "Haha! Co to kurwa jest!?"
scene ep1_panties_leaving9 with dissolve
#mc "Here, I got you the panties!"
mc "Masz, mam dla ciebie majtki!"
#mc "Can I come in? I'm freezing my balls off out here!"
mc "Czy mogę wejść? Odmrażam sobie jaja!"
scene ep1_panties_leaving10 with dissolve
#tm "HAHA! DIKS! RUSTY!"
tm "HAHA! DIKS! RUSTY!"
#tm "Come! You've got to see this!"
tm "Chodź! Musisz to zobaczyć!"
scene ep1_panties_leaving11 with dissolve
#rs "Hey, what's-"
rs "Hej, cojest..."
scene ep1_panties_leaving12 with dissolve
#rs "...up."
rs "Do góry."
#jac "Oh, hell naw."
jac "O, cholera nie."
#dikc "Ding dong!"
dikc "Dzyń, dzyń."
scene ep1_panties_leaving13 with dissolve
#mc "Hey, guys! I did what you told me; please let me in."
mc "Hej, chłopaki! Zrobiłem, co mi kazaliście; proszę, wpuśćcie mnie."
scene ep1_panties_leaving14 with dissolve
#rs "Well, the house is really for DIKs only, but since you got the panties, I guess-"
rs "Cóż, dom jest tak naprawdę tylko dla DIK-ów, ale skoro masz majtki, to chyba…"
scene ep1_panties_leaving15
#tm "No! Stop it right there, Rusty. You got the first part right."
tm "Nie! Zatrzymaj się, Rusty. Pierwsza część jest poprawna."
#tm "This is a DIKs only house, and this guy's neither a DIK, a pledge, or a hot girl."
tm "To jest dom tylko dla DIK-ów, a ten facet nie jest ani DIK-iem, ani nowicjuszem, ani gorącą laską."
#tm "He may stand there naked with panties, but that cock sticking out between his legs is what's wrong with that."
tm "Może stać tam nagi w majtkach, ale to ten kutas wystający między jego nogami jest w tym zły."
$ guideSuggestedPage = 42
scene ep1_panties_leaving13 with dissolve
menu:
#    "Joke around":
    "Żartuj sobie":
        if dtype > 0:
            $ RPdiks += 1
            scene ep1_panties_leaving17 with dissolve
#            mc "Look! Problem solved! Let me in!"
            mc "Spójrz! Problem rozwiązany! Wpuść mnie!"
#            dikc "HAHA! You like him better now, Tommy?"
            dikc "HAHA! Lubisz go teraz bardziej, Tommy?"
            scene ep1_panties_leaving17d with dissolve
#            tm "Fuck off! That's just fucking weird..."
            tm "Spierdalaj! To po prostu kurewsko dziwne..."
        else:
#            mc "Come on; it's just a dick. We all have them."
            mc "Daj spokój; to tylko kutas. Wszyscy je mamy."
#    "Get angry":
    "wpadam w gniew":
#        mc "For fuck's sake, guys, let me in! I can't walk around buck naked on campus with nowhere to go!"
        mc "Do kurwy nędzy, wpuśćcie mnie! Nie mogę chodzić nago po kampusie i nie mieć dokąd pójść!"
scene ep1_panties_leaving18 with dissolve
#tm "Thanks for the panties! We'll be in touch!"
tm "Dzięki za majtki! Będziemy w kontakcie!"
#rs "Sorry, dude... DIK code, you know."
rs "Sorry, stary... DIK code, wiesz."
#mc "Can I at least get something to wear?"
mc "Czy mogę przynajmniej dostać coś do ubrania?"
play sound "sound_effects/door_slam.mp3"
scene ep1_panties_leaving19 with hpunch
$ bios_tommy = True
$ bios_rusty = True
$ bios_jacob = True
$ bios_heather = True
$ bios_name_heather = True
$ bios_nick = True
$ bios_name_nick = True
$ bios_johnboy = True
$ bios_name_johnboy = True
$ bios_elena = True
$ bios_name_elena = True
#$ bios_history_tommy += "Tommy left me standing naked outside with nowhere to go.\n\n"
$ bios_history_tommy += "Tommy zostawił mnie nago na zewnątrz i nie miał dokąd pójść.\n \n"
#$ bios_history_rusty += "Rusty told me that DIK code prohibited him from helping me.\n\n"
$ bios_history_rusty += "Rusty powiedział mi, że kod DIK zabrania mu mi pomagać.\n \n"
#$ bios_history_jacob += "I have no clue who this guy is yet.\n\n"
$ bios_history_jacob += "Nie mam jeszcze pojęcia, kim jest ten facet.\n \n"
$ bios_name_tommy = True
$ bios_name_rusty = True
$ bios_name_jacob = True
$ chat_new_bios = True
#mc "(I fucking hate college!)"
mc "(Kurwa, nienawidzę college 'u!)"
#mc "(What the fuck am I supposed to do now?)"
mc "(Co ja, kurwa, mam teraz zrobić?)"
scene ep1_panties_leaving20 with wipeleft
stop music fadeout 5
#mc "(Troy has my other clothes... Quinn has my keys and phone...)"
mc "(Troy ma moje inne ubrania... Quinn ma moje klucze i telefon...)"
#mc "(I'm screwed...)"
mc "Przerąbane…"
scene ep1_panties_leaving21 with dissolve
#mc "(Maybe I just should call for a security guard?)"
mc "(Może powinienem wezwać ochroniarza?)"
#mc "(If I only could find one...)"
mc "(Gdybym tylko mógł znaleźć jedną...)"
$ renpy.sound.play("sound_effects/footsteps_outside.mp3", channel="sfx1", loop=False)
#"*{i}Footsteps{/i}*"
"Kroki."
scene ep1_panties_leaving21b
play sound "sound_effects/car_beep.mp3"
$ renpy.pause(0.5)
scene ep1_panties_leaving21
#mc "(Someone's coming! Shit...)"
mc "(Ktoś idzie! Cholera...)"
play music "music/ep1/fresh_air.mp3"
scene ep1_panties_leaving22 with dissolve
#mc "(Oh, it's the librarian...what was her name again?)"
mc "(Och, to bibliotekarka...jak miała na imię?)"
#mc "(Oh, yeah! Isabella!)"
mc "(O tak! Izabela!)"
#mc "*{i}Psst{/i}*"
mc "Psst."
#mc "Isabella?"
mc "Izabella"
scene ep1_panties_leaving23 with dissolve
#isa "Who's there?"
isa "Jest tam kto?"
scene ep1_panties_leaving23b with dissolve
#mc "Don't be alarmed...I don't want you to see me like this, but I need your help."
mc "Nie martw się... Nie chcę, żebyś mnie taką widziała, ale potrzebuję twojej pomocy."
scene ep1_panties_leaving23 with dissolve
#isa "What? Who is this?"
isa "Kto to jest?"
scene ep1_panties_leaving26
#mc "NO, DON'T!"
mc "Nie! Nie rób tego!"
scene ep1_panties_leaving27 with dissolve
#isa "What the hell, boy! Are you out of your mind!?"
isa "Co do cholery, chłopcze! Postradałeś zmysły!?"
#mc "Ouch! Ouch!!!"
mc "Auć! Auć!!!"
#isa "Why are you walking around naked outside!?"
isa "Dlaczego chodzisz nago na dworze!?"
scene ep1_panties_leaving29 with dissolve
#mc "Please, help me! A HOT girl took my clothes and threw me outside of their sorority house, naked."
mc "Proszę, pomóż mi! GORĄCA dziewczyna wzięła moje ubrania i wyrzuciła mnie nagą przed ich dom studencki."
#mc "My keys were in my pants, and I can't get back to my dorm..."
mc "Moje klucze były w spodniach i nie mogę wrócić do akademika..."
scene ep1_panties_leaving27 with dissolve
#isa "What!?"
isa "Co?!"
scene ep1_panties_leaving29 with dissolve
#mc "Please...help me..."
mc "Pomocy!"
scene ep1_panties_leaving31 with dissolve
#isa "Here..."
isa "W tym przypadku"
stop music fadeout 3
#isa "Cover yourself up and follow me."
isa "Zakryj się i chodź za mną."
#mc "Thank you!"
mc "Dziękujemy. Twój komentarz oczekuje na zatwierdzenie i niedługo powinien być dostępny."
scene ep1_bella_library with fade
#isa "There's no one here at this hour."
isa "O tej porze nikogo tu nie ma."
#mc "Oh, good."
mc "Och, dobrze. "
scene ep1_bella_library2 with dissolve
#isa "But don't get too comfortable. I'm not interested in seeing your penis again."
isa "Ale nie czuj się zbyt komfortowo. Nie jestem zainteresowany ponownym oglądaniem twojego penisa."
scene ep1_bella_library3 with dissolve
menu:
#    "Tease her":
    "Drażnij ją":
        $ dk(1)
#        mc "So, you did see it before, huh?"
        mc "Więc widziałeś to wcześniej, co?"
        $ RPisabella -= 1
#        $ bios_history_isabella += "She didn't appreciate my penis joke...\n\n"
        $ bios_history_isabella += "Nie spodobał jej się mój dowcip o penisie...\n \n"
        $ bios_name_isabella = True
        $ chat_new_bios = True
        scene ep1_bella_library3b with dissolve
        $ renpy.pause()
#    "Don't tease her":
    "Nie drażnij jej":
        $ dk(-1)
        $ RPisabella += 1
#        mc "Understood."
        mc "Zrozumiałem."
scene ep1_bella_library4 with dissolve
#isa "There's a lost and found back here."
isa "Z tyłu jest biuro rzeczy znalezionych."
#isa "I'm not sure if they will fit, but it's better than wearing nothing."
isa "Nie wiem, czy będą pasować, ale to lepsze niż nic nie nosić."
#mc "Really? How do people lose their clothes in here?"
mc "Naprawdę? Jak ludzie gubią tu swoje ubrania?"
scene ep1_bella_library4b with dissolve
#isa "...said the boy standing naked in front of me."
isa "...powiedział chłopak stojący przede mną nagi."
scene ep1_bella_library5 with dissolve
#mc "Thank you."
mc "Dziękuję."
#isa "TOWEL!"
isa "RĘCZNIK"
scene ep1_bella_library7 with dissolve
#mc "Sorry!"
mc "Przepraszam!"
scene ep1_bella_library10 with dissolve
#mc "Thank you for the clothes...really..."
mc "Dziękuję za ubrania...naprawdę..."
#mc "..."
mc "..."
#mc "Bye..."
mc "Żegnaj..."
scene ep1_bella_library11 with dissolve
#isa "Not so fast. Where do you think you're going?"
isa "Dokąd to?"
scene ep1_bella_library12 with dissolve
#mc "I thought I would try getting back to my dorm now."
mc "Pomyślałem, że spróbuję teraz wrócić do mojego akademika."
scene ep1_bella_library12b with dissolve
#isa "Where are your manners, boy?"
isa "Gdzie twoje maniery, chłopcze?"
scene ep1_bella_library12 with dissolve
#mc "Look, I said I'm sorry and thanked you. What else can I do?"
mc "Słuchaj, przeprosiłem i podziękowałem ci. Co jeszcze mogę zrobić?"
scene ep1_bella_library15 with dissolve
#isa "Over there! Sit!"
isa "Tam! Siadaj!"
scene ep1_bella_library12 with dissolve
#mc "Hey, I don't like how you boss me arou-"
mc "Hej, nie podoba mi się, jak mną rządzisz."
scene ep1_bella_library15
#isa "NOW!"
isa "-"
scene ep1_bella_library17 with dissolve
#mc "..."
mc "..."
scene ep1_bella_library18 with dissolve
#isa "Start from the beginning."
isa "Zacznij od początku"
scene ep1_bella_library17 with dissolve
#mc "The beginning of what?"
mc "Początek czego?"
scene ep1_bella_library18b with dissolve
#isa "Tell me why you ended up in that bush naked, boy."
isa "Powiedz mi, chłopcze, dlaczego wylądowałeś w tym krzaku nagi."
scene ep1_bella_library17 with dissolve
menu:
#    "Stop calling me boy":
    "Przestań nazywać mnie chłopcem":
#        mc "Can you stop calling me boy!? I'm a grown man!"
        mc "Możesz przestać nazywać mnie chłopcem!? Jestem dorosłym mężczyzną!"
        scene ep1_bella_library18b with dissolve
#        isa "A grown man, you say? Does a grown man sneak into young girls' dorms?"
        isa "Dorosły mężczyzna, powiadasz? Czy dorosły mężczyzna zakrada się do akademików młodych dziewcząt?"
        scene ep1_bella_library17 with dissolve
#        mc "That's not what I was doing in there!"
        mc "Nie to tam robiłem!"
        scene ep1_bella_library23 with dissolve
#        isa "Then tell me what you were doing in there...BOY!"
        isa "Więc powiedz mi, co tam robiłeś...CHŁOPCZE!"
#    "Don't call her out":
    "Nie wołaj jej":
#        mc "Ok..."
        mc "Dobrze..."
scene ep1_bella_library17 with dissolve
#mc "Look, I share a dorm with this asshole named Troy."
mc "Słuchaj, dzielę akademik z tym dupkiem o imieniu Troy."
#mc "I was trying to get along but, thanks to him, the jocks stole my guitar..."
mc "Próbowałem się dogadać, ale dzięki niemu sportowcy ukradli mi gitarę..."
#mc "...my father got me that guitar *{i}sobs{/i}*...and now it's gone..."
mc "...mój ojciec dał mi tę gitarę *{i}szloch{/i}*...a teraz jej nie ma..."
scene ep1_bella_library18 with dissolve
#isa "It's ok. Go on."
isa "W porządku. Mów dalej."
scene ep1_bella_library17 with dissolve
#mc "I had a falling out with him, and there's just no way I can live with him anymore."
mc "Pokłóciłam się z nim i nie ma mowy, żebym mogła z nim dłużej żyć."
#mc "I figured that I could move into a frat house to get away from him."
mc "Pomyślałam, że mogę się przeprowadzić do domu bractwa, żeby od niego uciec."
#mc "The tri-betas don't have a house, the jocks hate me, and I'm way too poor to ever be able to join the preppy frat, so I was left with the DIKs."
mc "Trójkąty nie mają domu, sportowcy mnie nienawidzą, a ja jestem zbyt biedny, żeby kiedykolwiek dołączyć do bractwa, więc zostałem z DIK-ami."
#mc "It was my only option."
mc "To była moja jedyna opcja."
#mc "They said I would get in if I went to the HOT sorority and stole a pair of panties from them."
mc "Powiedzieli, że wejdę, jeśli pójdę do GORĄCEGO bractwa i ukradnę im parę majtek."
scene ep1_bella_library23 with dissolve
#isa "You what!?"
isa "You what? "
#mc "Hey, at least let me explain before you scold me!"
mc "Hej, przynajmniej pozwól mi wyjaśnić, zanim mnie zbesztasz!"
scene ep1_bella_library23b with dissolve
#isa "..."
isa "..."
scene ep1_bella_library18 with dissolve
#isa "Go on."
isa "Dalej. "
scene ep1_bella_library17 with dissolve
#mc "So, I found the panties and was about to get out of there..."
mc "Więc znalazłam majtki i już miałam się stamtąd wydostać..."
#mc "...but these two girls came into the showers, and I had to hide."
mc "...ale te dwie dziewczyny weszły pod prysznic, a ja musiałam się schować."
#mc "They found me and..."
mc "Bo one wyszukiwały mnie i ja je."
#mc "The details don't matter; they stole my clothes and kicked me out, holding a pair of panties."
mc "Szczegóły nie mają znaczenia; ukradli moje ubrania i wyrzucili mnie, trzymając parę majtek."
scene ep1_bella_library18 with dissolve
#isa "They stole your clothes?"
isa "Ukradli twoje ubrania?"
scene ep1_bella_library17 with dissolve
#mc "Yes! I'm telling you the truth! I had to walk around campus naked, trying to get back to the DIKs."
mc "Tak! Mówię prawdę! Musiałem chodzić nago po kampusie, próbując wrócić do DIK-ów."
#mc "And when I got there, they laughed in my face...they even took the panties from me."
mc "A kiedy tam dotarłem, śmiali mi się w twarz...zabrali mi nawet majtki."
#mc "There! Go ahead and scold me again!"
mc "Nie krępuj się i jeszcze raz mnie zbesztaj!"
scene ep1_bella_library18b with dissolve
#isa "Are you some kind of a pervert?"
isa "Jesteś jakimś zboczeńcem?"
scene ep1_bella_library17 with dissolve
#mc "Great! I'm a pervert. Again!"
mc "Świetnie! Jestem zboczeńcem. Znowu!"
scene ep1_bella_library23 with dissolve
#isa "What's wrong with you, boy? Didn't your mother ever teach you that you don't go sneaking around in women's showers?"
isa "Co z tobą, chłopcze? Czy mama nigdy nie nauczyła cię, że nie skradasz się pod damskimi prysznicami?"
scene ep1_bella_library23b with dissolve
#mc "No!!! She-"
mc "Nie!!! Ona-"
#mc "..."
mc "..."
#mc "My mother passed away as I was born."
mc "Moja matka zmarła, gdy się urodziłem."
scene ep1_bella_library23c with dissolve
#mc "It's just been me and my dad."
mc "Zostałam tylko ja i mój tata."
#mc "And he didn't tell me that..."
mc "I nie powiedział mi, że..."
#mc "...explicitly."
mc "...wyraźnie."
scene ep1_bella_library36 with dissolve
#isa "Oh...I...erm..."
isa "Och...ja...hmm..."
#isa "..."
isa "..."
scene ep1_bella_library37b with dissolve
#isa "Yes, well, that would make quite a difference."
isa "Tak, cóż, to zrobiłoby sporą różnicę."
scene ep1_bella_library37 with dissolve
#mc "Well, there's not much I can do about that."
mc "Cóż, niewiele mogę na to poradzić."
scene ep1_bella_library37b with dissolve
#isa "You may leave."
isa "Może Pani opuścić."
scene ep1_bella_library37 with dissolve
#mc "Fine..."
mc "Dobrze..."
scene ep1_bella_library40 with dissolve
#isa "That shirt is too small for you."
isa "Ta koszula jest dla ciebie za mała."
scene ep1_bella_library41 with dissolve
#mc "..."
mc "..."
stop music fadeout 10
#mc "Thank you...Isabella."
mc "Dziękuję...Izabelo."
#mc "I'm [name], by the way."
mc "Tak przy okazji, jestem Fran. "
#$ bios_history_isabella += "I got to talk more to Isabella today. She helped me get clothes after standing naked outside. She scolded me for my actions, but something tells me that she cared about me more than she let on.\n\n"
$ bios_history_isabella += "Muszę dziś porozmawiać więcej z Isabellą. Pomogła mi się ubrać po tym, jak stanęłam naga na zewnątrz. Beształa mnie za moje czyny, ale coś mi mówi, że troszczyła się o mnie bardziej, niż się chwaliła.\n \n"
$ bios_name_isabella = True
$ chat_new_bios = True
scene ep1_bella_library42 with dissolve
$ renpy.pause()
scene ep1_dorm_aftermath with fade
#mc "..."
mc "..."
#mc "(Yeah...there's no way I'm going to get back in.)"
mc "(Tak... nie ma mowy, żebym wrócił.)"
play music "music/ep1/your_smile.mp3"
#mc "(If I had my phone, I could have called someone...)"
mc "(Gdybym miał telefon, mógłbym do kogoś zadzwonić...)"
#mc "(...you know what?)"
mc "Wiesz co... "
#mc "(Fuck this place, I'm going home.)"
mc "(Pieprzyć to miejsce, idę do domu.)"
scene ep1_dorm_aftermath2 with fade
#mc "(I'm not going to stay here. It's obvious that no one gives a fuck about me.)"
mc "(Nie zamierzam tu zostać. To oczywiste, że nikt się mną nie przejmuje.)"
#mc "(College sucks!)"
mc "(Studia są do bani!)"
#mc "(Dad...he'll understand...)"
mc "(Tata…zrozumie…)"
scene ep1_dorm_aftermath4
#mc "(FUCK! My wallet was in my pants!)"
mc "(KURWA! Portfel miałem w spodniach!)"
scene ep1_dorm_aftermath5 with dissolve
#mc "(NO! I'm so fucking stupid!)"
mc "(Nie! Jestem tak cholernie głupi!)"
play sound "sound_effects/running_gravel.mp3"
scene ep1_dorm_aftermath6 with dissolve
#sec "Hey, you! Have you seen a naked guy running around here?"
sec "Hej, ty! Widziałeś biegającego tu nagiego faceta?"
#mc "*{i}Gulp{/i}*"
mc "Połykanie"
#mc "No...or...maybe he went into the parking lot?"
mc "Nie…a…może wszedł na parking?"
#sec "Dammit!"
sec "- Cholera!"
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath8 with dissolve
#uk "Is he gone?"
uk "Nie ma go?"
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath10 with dissolve
#mc "Huh?"
mc "Hm?"
#de "That was a close one."
de "Mało brakowało!"
play sound "sound_effects/bushes.mp3"
scene ep1_dorm_aftermath11 with dissolve
#mc "Wait...you're the naked guy?"
mc "Chwila...ty jesteś tym nagim facetem?"
#de "Yeah! Fucking Quinn stole my clothes!"
de "Tak! Pieprzony Quinn ukradł moje ubrania!"
scene ep1_dorm_aftermath13 with dissolve
#mc "No way! Mine too!"
mc "Nie ma mowy! Ja też!"
#de "Haha! No way!"
de "Haha! Nie ma mowy!"
#mc "You want some clothes? I have my bag right here."
mc "Chcesz trochę ubrań? Mam tu swoją torbę."
scene ep1_dorm_aftermath15 with dissolve
#de "Nah, I'm good."
de "Nie, dziękuję."
#de "She fooled both of us, huh?"
de "Oszukała nas oboje, co?"
scene ep1_dorm_aftermath17 with dissolve
#mc "Looks like it..."
mc "Na to wygląda. "
scene ep1_dorm_aftermath18 with dissolve
#de "Don't worry! We'll get her back."
de "Nie martw się! Odzyskamy ją."
#de "What's up with the bag? Going somewhere?"
de "O co chodzi z tą torbą? Wybierasz się gdzieś?"
scene ep1_dorm_aftermath17 with dissolve
#mc "Actually...I was going home."
mc "Właściwie...wracałam do domu."
#mc "I've had enough of this place..."
mc "Mam już dość tego miejsca..."
scene ep1_dorm_aftermath18 with dissolve
#de "Are you crazy? You're giving up? You just got here!"
de "Oszalałeś? Poddajesz się? Dopiero przyszedłeś!"
scene ep1_dorm_aftermath17 with dissolve
#mc "Yeah, but it feels like everyone's against me."
mc "Tak, ale wydaje mi się, że wszyscy są przeciwko mnie."
#mc "Quinn tricked me, the DIKs fucked me over, the jocks hate me, and I got into a fight with my dorm mate..."
mc "Quinn mnie oszukał, DIK mnie wyruchali, sportowcy mnie nienawidzą, a ja wdałem się w bójkę z kolegą z akademika..."
#mc "...my former dorm mate, I should say."
mc "...mój były kolega z akademika, powinienem powiedzieć."
scene ep1_dorm_aftermath18 with dissolve
#de "So what? You were naked, everyone hates you, and you have no place to stay."
de "I co z tego? Byłaś naga, wszyscy cię nienawidzą i nie masz gdzie się zatrzymać."
#de "That's some cool fucking stories in the making there, bro!"
de "To dopiero zajebiste historie, brachu!"
#de "That's the real college experience if you ask me!"
de "To jest prawdziwe doświadczenie studenckie, jeśli o mnie chodzi!"
scene ep1_dorm_aftermath23 with dissolve
#de "And not everyone hates you. I like you!"
de "I nie wszyscy cię nienawidzą. Lubię cię!"
#mc "I'd feel much more comfortable if you put on some clothes..."
mc "Czułbym się o wiele bardziej komfortowo, gdybyś założyła jakieś ubranie..."
#my "What the fuck are you two doing!?"
my "Co ty odpierdalasz? "
scene ep1_dorm_aftermath25 with dissolve
#de "Hey! Sis! Come join us!"
de "Hej! Siostrzyczko! Dołącz do nas!"
#my "No way! I'm going!"
my "Nie ma mowy! Idę!"
#mc "Wait, what!? Sis?"
mc "Czekaj, co!? Siostrzyczko?"
scene ep1_dorm_aftermath25c with dissolve
#de "Didn't she tell you?"
de "Nie powiedziała ci?"
#mc "...no."
mc "l.p."
scene ep1_dorm_aftermath25 with dissolve
#de "[name] needs your help!"
de "Rex potrzebuje twojej pomocy!"
scene ep1_dorm_aftermath25c with dissolve
#mc "*{i}Whispers{/i}*What are you doing?"
mc "*{i}Szepty{/i}*Co robisz?"
#de "*{i}Whispers{/i}*Trust me."
de "*{i}Szepty{/i}*Zaufaj mi."
scene ep1_dorm_aftermath29 with dissolve
#my "Help with what?"
my "W czym pomóc?"
scene ep1_dorm_aftermath25 with dissolve
#de "Did that exchange student show up yet, or are you still living alone?"
de "Czy uczeń z wymiany już się pojawił, czy nadal mieszkasz sam?"
scene ep1_dorm_aftermath29 with dissolve
#my "No, not yet. Why?"
my "Nie, jeszcze nie. Dlaczego?"
scene ep1_dorm_aftermath25 with dissolve
#de "Awesome!"
de "Super!"
play sound "sound_effects/shove.mp3"
scene ep1_dorm_aftermath32 with vpunch
#de "Meet your new roommate!"
de "Poznaj swojego nowego współlokatora!"
scene ep1_dorm_aftermath31 with dissolve
#my "My new what?"
my "Moje nowe co?"
scene ep1_dorm_aftermath33 with dissolve
#de "He needs a place to stay, and you need someone to share your dorm with!"
de "On potrzebuje miejsca na pobyt, a Ty potrzebujesz kogoś, z kim możesz dzielić swój akademik!"
scene ep1_dorm_aftermath31 with dissolve
#my "No, I don't {b}need{/b} someone to share my dorm with."
my "Nie, nie potrzebuję {b}nikogo{/b}, z kim mogłabym dzielić swój akademik."
#my "You can share your dorm with him!"
my "Możesz podzielić się z nim swoim akademikiem!"
scene ep1_dorm_aftermath35 with dissolve
#de "Come on! You fucking owe me, and you know it!"
de "Daj spokój! Jesteś mi, kurwa, coś winien i dobrze o tym wiesz!"
scene ep1_dorm_aftermath36 with dissolve
#my "This again?"
my "„Znowu to?"
scene ep1_dorm_aftermath35 with dissolve
#de "After this, we're even."
de "Potem jesteśmy kwita."
scene ep1_dorm_aftermath36 with dissolve
#my "Only for one night..."
my "na jedną dobę"
scene ep1_dorm_aftermath35 with dissolve
#de "For one night!?"
de "na jedną dobę"
scene ep1_dorm_aftermath38
#de "No way!"
de "Jasne, że nie! "
scene ep1_dorm_aftermath36b
#my "Put some fucking clothes on, Derek!!!"
my "Załóż jakieś pieprzone ciuchy, Derek!!!"
scene ep1_dorm_aftermath39 with dissolve
#mc "I'll take it."
mc "Będę korzystać."
scene ep1_dorm_aftermath40 with dissolve
#my "Deal!"
my "Umowa! "
scene ep1_dorm_aftermath41 with dissolve
#de "Dude! I would have gotten you months!"
de "Stary! Kupiłbym ci miesiące!"
scene ep1_dorm_aftermath40b with dissolve
#my "The deal is done, Derek."
my "Umowa została zawarta, Derek."
scene ep1_dorm_aftermath40c with dissolve
stop music fadeout 3
#my "Ok, [name]. Follow me. I can sneak you in through the window."
my "Dobra, [name]. Za mną. Mogę cię przemycić przez okno."
scene ep1_maya_dorm with wiperight
#mc "Hngh..."
mc "Hngh...!"
scene ep1_maya_dorm1 with dissolve
#mc "There! Thanks!"
mc "Proszę! Dzięki!"
#my "Hahaha!"
my "Ha!Ha!"
#mc "Why are you laughing?"
mc "Czemu ty się śmiejesz?"
play music "music/ep1/trow.mp3"
scene ep1_maya_dorm3 with dissolve
#my "I was just fucking with you about the window. No one cares if you go through the door."
my "Jaja sobie robiłem z tego okna. Nikogo nie obchodzi, czy przejdziesz przez drzwi."
scene ep1_maya_dorm4 with dissolve
menu:
#    "Laugh":
    "Gest „Śmiech”":
        $ dk(-1)
        $ RPmaya += 1
#        mc "Oh, haha!"
        mc "Och, haha!"
#    "Get annoyed":
    "Daj się zirytować":
        $ dk(1)
#        mc "That's not funny! That's just mean."
        mc "To nie jest śmieszne! To jest po prostu wredne."
scene ep1_maya_dorm5 with dissolve
#my "Sorry."
my "Przepraszamy. Aby zapobiec spamowi, URL są niedozwolone w wiadomościach."
play sound "sound_effects/switch.mp3"
scene ep1_maya_dorm5b
#my "Anyway, welcome to my dorm."
my "W każdym razie witam w moim akademiku."
scene ep1_maya_dorm6 with dissolve
#mc "This dorm is a lot nicer than my old one."
mc "Ten akademik jest o wiele ładniejszy niż mój stary."
scene ep1_maya_dorm7 with dissolve
#my "Make yourself at home..."
my "Czuj się jak w domu ..."
#my "You know...for the night."
my "Wiesz...na noc."
$ guideSuggestedPage = 43
#$ bios_history_derek +="Derek was tricked by Quinn too. He convinced Maya to share her dorm with me.\n\nI found out that Derek and Maya are siblings.\n\n"
$ bios_history_derek +="Derek też został oszukany przez Quinna. Przekonał Mayę, żeby podzieliła się ze mną swoim akademikiem.\n\nDowiedziałam się, że Derek i Maya są rodzeństwem.\n \n"
#$ bios_history_maya +="Maya agreed to share her dorm with me for the night. Derek called in a favor that she owed him.\n\nI found out that Derek and Maya are siblings.\n\n"
$ bios_history_maya +="Majka zgodziła się podzielić ze mną swoim akademikiem na noc. Derek poprosił ją o przysługę, którą była mu winna.\n\nDowiedziałem się, że Derek i Maya są rodzeństwem.\n \n"
$ bios_name_derek = True
$ bios_name_maya = True
$ chat_new_bios = True
jump ep1_freeroam_maya_label
label ep1_maya_freeroam_sleep_label:

$ renpy.block_rollback()
$ phone_call_enabled = False
$ chat_new_tasks = False
$ loopMusic = False
stop music fadeout 3
scene ep1_frmdorm_sleep with dissolve
#my "Wanna go to bed?"
my "Chcesz iść spać?"
scene ep1_frmdorm_sleepb with dissolve
play music "music/ep1/fresh_air.mp3"
menu:
#    "Sure":
    "Pewnie":
#        mc "Sure, I'm pretty tired..."
        mc "Jasne, jestem zmęczona..."
#    "Together?":
    "Razem?":
        if dtype > 0:
            $ dk(1)
#            mc "Together with you? Of course."
            mc "Razem z tobą? Oczywiście."
            scene ep1_frmdorm_sleep2 with dissolve
#            my "You really need to work on your flirting skills. That just comes off as sleazy."
            my "Naprawdę musisz popracować nad umiejętnościami flirtowania. To po prostu wydaje się obskurne."
        else:
            $ dk(-1)
#            mc "What? Not together, right?"
            mc "Co? Nie razem, prawda?"
            scene ep1_frmdorm_sleep3 with dissolve
#            my "Haha! No, stupid."
            my "Haha! Nie, głupia."
        scene ep1_frmdorm_sleep4 with dissolve
#        my "To clarify, I'm sleeping over there..."
        my "Dla jasności, śpię tam..."
        scene ep1_frmdorm_sleep5 with dissolve
#        my "And you're sleeping all the way over there."
        my "A ty śpisz aż tam."
#        mc "Haha, ok."
        mc "Haha, ok."
scene ep1_maya_dorm5b with dissolve
$ renpy.pause(0.5)
play sound "sound_effects/switch.mp3"
scene ep1_maya_dorm5
$ renpy.pause(2)
scene ep1_frmdorm_sleep7 with dissolve
#my "Now turn around and close your eyes."
my "Teraz odwróć się i zamknij oczy."
scene ep1_frmdorm_sleep7b with dissolve
#mc "What for?"
mc "Czemuż to?"
scene ep1_frmdorm_sleep7 with dissolve
#my "Because I need to change, and I don't need you staring at me."
my "Bo muszę się przebrać i nie musisz się na mnie gapić."
if dtype > 0:
    scene ep1_frmdorm_sleep7b with dissolve
#    mc "You're no fun..."
    mc "Nie jesteś zabawny."
else:
    $ RPmaya += 1
    scene ep1_frmdorm_sleep7b with dissolve
#    mc "Is that what you think of me? That I would stare?"
    mc "Czy tak o mnie myślisz? Że będę się gapić?"
    scene ep1_frmdorm_sleep12b with dissolve
#    my "No...I..."
    my "Nie, ja... "
#    my "Sorry. You've been nothing but nice."
    my "Przepraszam. Byłaś tylko miła."
#    my "I just meant that I would be more comfortable that way."
    my "Chodziło mi tylko o to, że tak będzie mi wygodniej."
    scene ep1_frmdorm_sleep12 with dissolve
#    mc "Of course, I'll turn around."
    mc "Oczywiście, odwrócę się."
scene ep1_frmdorm_sleep15 with dissolve
menu:
    "Sneak a peek ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
        scene ep1_frmdorm_sleep16 with dissolve
#        mc "(Fuck me...)"
        mc "Pieprz mnie"
        scene ep1_frmdorm_sleep17 with dissolve
        $ renpy.pause()
        menu:
#            "Closer look at ass":
            "Bliższe spojrzenie na tyłek":
                scene ep1_frmdorm_sleep17c with dissolve
                $ renpy.pause()
                scene ep1_frmdorm_sleep17b with dissolve
                $ renpy.pause()
#            "Closer look at tits":
            "Bliższe spojrzenie na cycki":
                scene ep1_frmdorm_sleep17d with dissolve
                $ renpy.pause()
                scene ep1_frmdorm_sleep17e with dissolve
                $ renpy.pause()
        scene ep1_frmdorm_sleep15 with dissolve
#        mc "(Ok...that's enough...)"
        mc "(Ok...wystarczy...)"
#        my "Ok! I'm ready."
        my "Zgadzam się!"
#    "Wait until she's done":
    "Poczekaj, aż skończy":
#        my "Ok! I'm ready."
        my "Zgadzam się!"
$ guideSuggestedPage = 44
scene ep1_frmdorm_sleep18 with dissolve
menu:
#    "Compliment her":
    "Praw jej komplementy":
        if dtype > 0:
#            mc "You look hot in that."
            mc "Wyglądasz w tym seksownie."
            scene ep1_frmdorm_sleep18b with dissolve
#            my "Thanks. I guess."
            my "Eee, dzięki. "
            scene ep1_frmdorm_sleep18 with dissolve
        else:
            $ RPmaya += 1
#            mc "That's very beautiful on you."
            mc "To dla ciebie bardzo piękne."
            scene ep1_frmdorm_sleep18c with dissolve
#            my "[name]..."
            my "[name]..."
            scene ep1_frmdorm_sleep18 with dissolve
#    "Don't compliment her":
    "Nie komplementuj jej":
#        mc "Great!"
        mc "No i prawidłowo!"
#mc "My turn!"
mc "Moja kolej!"
scene ep1_frmdorm_sleep18d with dissolve
#my "Haha, all right."
my "Haha, w porządku."
scene ep1_frmdorm_sleep18 with dissolve
menu:
#    "Ask her to turn around":
    "Poproś ją, żeby się odwróciła":
#        mc "I think it's your turn to turn around, Maya..."
        mc "Myślę, że teraz twoja kolej, żeby się odwrócić, Maya..."
        if dtype > 0:
            scene ep1_frmdorm_sleep20b with dissolve
#            my "Now who's the fun one?"
            my "I kto teraz jest zabawny?"
        else:
            scene ep1_frmdorm_sleep20c with dissolve
#            my "Oh, of course!"
            my "Och, oczywiście! "
        scene ep1_frmdorm_sleep21 with dissolve
        menu:
#            "Check her out":
            "Patrz na nią. ":
                scene ep1_frmdorm_sleep21b with dissolve
                $ renpy.pause()
#            "Don't risk it":
            "Nie ryzykuj! ":
                $ renpy.pause(0.5)
        play sound "sound_effects/clothes.mp3"
#    "Undress while she looks":
    "Rozbierz się, gdy patrzy":
        play sound "sound_effects/clothes.mp3"
        scene ep1_frmdorm_sleep22 with dissolve
#        my "Haha! Whoa!"
        my "Haha! Whoa!"
#        my "I thought you would ask me to turn around!"
        my "Myślałam, że mnie poprosisz, żebym się odwróciła!"
        scene ep1_frmdorm_sleep23 with dissolve
        if dtype > 0:
#            mc "It's ok. I'm not ashamed of my body."
            mc "W porządku. Nie wstydzę się swojego ciała."
        else:
#            mc "Oh... Well, it doesn't matter to me."
            mc "To dla mnie bez znaczenia,"
        scene ep1_frmdorm_sleep24 with dissolve
#        my "Haha, you'll have to teach me how to be that comfortable with myself some time."
        my "Haha, będziesz musiała mnie kiedyś nauczyć, jak czuć się tak komfortowo ze sobą."
        if dtype < 0:
            $ RPmaya += 1
            scene ep1_frmdorm_sleep25 with dissolve
#            mc "Well, you should feel comfortable with your body."
            mc "Cóż, powinieneś czuć się komfortowo ze swoim ciałem."
#            mc "You're beautiful."
            mc "Jesteś młoda i piękna."
            scene ep1_frmdorm_sleep26 with dissolve
#            my "[name]..."
            my "[name]..."
scene ep1_frmdorm_sleep27 with dissolve
#my "Good night, [name]."
my "Dobranoc."
#mc "Good night. Thank you for letting me stay here tonight."
mc "Dobranoc. Dziękuję, że mogę tu zostać na noc."
#my "No worries. Hope you'll dream sweet dreams."
my "Nie martw się. Mam nadzieję, że śnisz słodkie sny."
scene ep1_frmdorm_sleep29 with dissolve
stop music fadeout 3
#mc "(I hope so too...)"
mc "(Też mam taką nadzieję...)"
scene black with fade
$ phone_clear_jump_label = "ep1_sleep_after_maya_freeroam_label"
jump clear_phone_chat
label ep1_sleep_after_maya_freeroam_label:

if preferredmilf == 0:
    label ep1_jade_lewd2:
    if _in_replay:
        $ currentEpisode = 1
        $ preferredmilf = 0
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_jade == None:
            $ mc_jade = name
        else:
            $ mc_jade = persistent.mc_jade
        if persistent.jade == None:
            $ jade = "Jade"
        else:
            $ jade = persistent.jade
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_jade_dream2 with Fade(1.5, 1, 0.5)
#    ja "Hey, [mc_jade]..."
    ja "Hej... "
    scene ep1_jade_dream3 with dissolve
#    mc "Oh! Jade! It's you again..."
    mc "Och! Jade! To znowu ty..."
    scene ep1_jade_dream2 with dissolve
#    ja "Yeah, it's me again...why did you leave me so early last time?"
    ja "Tak, to znowu ja...dlaczego ostatnim razem zostawiłeś mnie tak wcześnie?"
    scene ep1_jade_dream with dissolve
#    mc "I had to wake up..."
    mc "Musiałem się obudzić..."
#    mc "...but not this time, though!"
    mc "...ale nie tym razem!"
    scene ep1_jade_dream1 with dissolve
#    ja "Is that so? Let's take it from the beginning, then..."
    ja "Czy tak jest? Zacznijmy więc od początku..."
    scene ep1_jade_dream2 with dissolve
#    ja "Because [jade] is here for you now, [mc_jade]..."
    ja "Bo [jade] jest tu teraz dla Ciebie, [mc_jade]..."
#    ja "Let me take care of you..."
    ja "Teraz pozwól mi się tobą zająć."
    init 500 image anim_jade_boobjob1_ep1b = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
#    ja "Did you miss my soft breasts, [mc_jade]?"
    ja "Tęskniłeś za moimi miękkimi piersiami, [mc_jade]?"
#    mc "Mmm...I did..."
    mc "Mmm...Zrobiłem..."
    pause
    init 500 image anim_jade_boobjob2_ep1b = Movie(channel="anim_jade_boobjob2_ep1", play="images/movies/ep1/anim_jade_boobjob2_ep1.webm")
    scene anim_jade_boobjob2_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "Your cock is so hard, [mc_jade]..."
    ja "Twój kutas jest taki twardy, [mc_jade]..."
    init 500 image anim_jade_boobjob1_ep1c = Movie(channel="anim_jade_boobjob1_ep1", play="images/movies/ep1/anim_jade_boobjob1_ep1.webm")
    scene anim_jade_boobjob1_ep1c with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "What's the matter, [mc_jade]?"
    ja "O co chodzi?"
#    ja "You look a bit skeptical..."
    ja "Wyglądasz trochę sceptycznie..."
#    ja "Are you good?"
    ja "Jest ci dobrze? "
#    mc "..."
    mc "..."
#    mc "Yes! I think I am good this time!"
    mc "Tak! Myślę, że tym razem jestem dobry!"
    scene ep1_jade_dream5 with dissolve
#    ja "That's great to hear..."
    ja "Miło to słyszeć..."
#    ja "Because all I want right now..."
    ja "Bo wszystko, czego teraz chcę..."
#    ja "Is you [mc_jade]..."
    ja "to ty sam."
    scene ep1_jade_dream_6 with dissolve
#    ja "...and to have that big fat cock between your legs rubbing against my wet pussy."
    ja "...i mieć tego dużego grubego kutasa między nogami ocierającego się o moją mokrą cipkę."
#    ja "Mmm...can you feel how warm my pussy is against your dick?"
    ja "Mmm...czujesz, jak ciepła jest moja cipka na twoim penisie?"
#    mc "Yeah...I almost wished you didn't have panties for this..."
    mc "Tak... Prawie żałuję, że masz na to majtki..."
    scene ep1_jade_dream5 with dissolve
#    ja "I can arrange that...it's a dream after all..."
    ja "Mogę to zaaranżować…to przecież marzenie…"
    scene ep1_jade_dream7 with dissolve
#    ja "Mmm...good choice..."
    ja "Mmm...dobry wybór..."
#    ja "This feels so much better."
    ja "Tak jest o wiele lepiej."
    scene ep1_jade_dream8 with dissolve
#    mc "Wow, you're squeezing it just right, [jade]..."
    mc "Wow, wyciskasz to dokładnie tak, [jade]..."
    scene ep1_jade_dream9 with dissolve
#    ja "You're loving this, aren't you?"
    ja "Uwielbiasz to, prawda?"
#    mc "Yes, [jade]..."
    mc "Tak"
    scene ep1_jade_dream10 with dissolve
#    ja "So...what are you waiting for?"
    ja "Na co czekasz? "
#    mc "What?"
    mc "Co?"
    scene ep1_jade_dream11 with dissolve
#    ja "Get your hips moving..."
    ja "Ruszaj biodrami..."
#    ja "It's time to get you off for real, [mc_jade]..."
    ja "Nadszedł czas, aby wysiąść naprawdę, [mc_jade]..."
    init 500 image anim_jade_assjob1_ep1b = Movie(channel="anim_jade_assjob2_ep1b", play="images/movies/ep1/anim_jade_assjob1_ep1.webm")
    scene anim_jade_assjob1_ep1b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "Oh, yes!!! Just like that!"
    ja "Och, tak po prostu!"
    init 500 image anim_jade_assjob2_ep2b = Movie(channel="anim_jade_assjob2_ep2b", play="images/movies/ep1/anim_jade_assjob2_ep1.webm")
    scene anim_jade_assjob2_ep2b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "I'm soaking wet, [mc_jade]..."
    ja "Jestem cały mokry, [mc_jade]..."
#    ja "Keep moving those hips..."
    ja "Ruszaj biodrami..."
#    ja "I might actually be able to cum..."
    ja "Może uda mi się dojść..."
    init 500 image anim_jade_assjob3_ep3b = Movie(channel="anim_jade_assjob3b_ep1", play="images/movies/ep1/anim_jade_assjob3_ep1.webm")
    scene anim_jade_assjob3_ep3b with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "...no man has ever made me cum..."
    ja "...żaden mężczyzna nigdy mnie nie spuścił..."
#    mc "Really?"
    mc "Serio?"
#    ja "..."
    ja "..."
#    ja "Sure."
    ja "Dobrze."
    init 500 image anim_jade_assjob4_ep1 = Movie(channel="anim_jade_assjob4_ep1", play="images/movies/ep1/anim_jade_assjob4_ep1.webm")
    scene anim_jade_assjob4_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "Feel how my huge tits bounce on your chest..."
    ja "Poczuj, jak moje ogromne cycki odbijają się na twojej piersi..."
#    mc "Your tits are so big and soft, [jade]."
    mc "Twoje cycki są takie duże i miękkie, [jade]."
    init 500 image anim_jade_assjob5_ep1 = Movie(channel="anim_jade_assjob5_ep1", play="images/movies/ep1/anim_jade_assjob5_ep1.webm")
    scene anim_jade_assjob5_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ja "And your cock is so big and hard, [mc_jade]."
    ja "A twój kutas jest taki duży i twardy, [mc_jade]."
#    ja "Are you getting close?"
    ja "Zbliżasz się?"
#    mc "I don't know...maybe..."
    mc "– Nie wiem, może! "
#    ja "Take as long as you need..."
    ja "Poświęć tyle czasu, ile potrzebujesz..."
    $ currentSexLabel = "ep1_jade_lewd2b"
    $ lewd_jade_phase = 1
    jump jade_sex_scene_loop
    label ep1_jade_lewd2b:
#    ja "Mmm...that was amazing, [mc_jade]!"
    ja "Mmm...to było niesamowite, [mc_jade]!"
    stop music fadeout 3
#    ja "I'll see you soon again, in your dreams..."
    ja "Do zobaczenia wkrótce, w Twoich snach..."
    $ persistent.ep1_jade_dream2 = True
    $ renpy.end_replay()
    $ calcScenes()
#    $ bios_history_jade += "I had another sexy dream about Jade. This time it ended much better than the first one.\n\n"
    $ bios_history_jade += "Miałam kolejny seksowny sen o Jade. Tym razem skończyło się to znacznie lepiej niż pierwsze.\n \n"
    $ bios_name_jade = True
    $ chat_new_bios = True
else:
    label ep1_cathy_lewd2:
    if _in_replay:
        $ currentEpisode = 1
        $ preferredmilf = 1
        if persistent.name == None:
            $ name = "MC"
        else:
            $ name = persistent.name
        if persistent.mc_cathy == None:
            $ mc_cathy = name
        else:
            $ mc_cathy = persistent.mc_cathy
        if persistent.cathy == None:
            $ cathy = "Cathy"
        else:
            $ cathy = persistent.cathy
    hide screen phone_screen
    play music "music/ep1/slow_day_blues.mp3"
    scene ep1_d2_wakeb with Fade(1.5, 1, 0.5)
#    ca "You really don't know shit!"
    ca "- Naprawdę nie wiesz?"
#    ca "Can't you spell the word endocytosis?"
    ca "Nie umiesz przeliterować słowa endocytoza?"
    if failedEnglish == 0:
#        mc "But I do know how to spell it!"
        mc "Ale wiem, jak to przeliterować!"
#        mc "Oh...yeah, this is another dream..."
        mc "A...tak, to kolejny sen..."
    scene ep1_d2_wake1b with dissolve
#    ca "I feel like I should be teaching you how to spell simpler words."
    ca "Czuję, że powinienem Cię uczyć, jak przeliterować prostsze słowa."
#    ca "What about ball? B-A-L-L!"
    ca "A co z piłką? B-A-L-L!"
    scene ep1_d2_wake2b with dissolve
#    ca "Hello! It's a noun! Something you can play with."
    ca "Cześć! To rzeczownik! Coś, czym możesz się bawić."
    scene ep1_d2_wake1b with dissolve
#    ca "No, not your BALLS!"
    ca "Nie, nie twoje JAJA!"
    scene ep1_d2_wake3b2 with dissolve
#    ca "Would you want that? For me to play with your balls?"
    ca "Chciałbyś tego? Żebym bawił się twoimi jajami?"
#    ca "With your dick, too!?"
    ca "Swoim kutasem też!?"
#    ca "If that's what it will take for you to stay awake in class...FINE!"
    ca "Jeśli to jest to, czego potrzebujesz, aby nie zasnąć w klasie... w PORZĄDKU!"
    init 500 image anim_cathy_hj_ep1 = Movie(channel="anim_cathy_hj_ep1", play="images/movies/ep1/anim_cathy_hj_ep1.webm")
    scene anim_cathy_hj_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "This is ridiculous. Never have I had a student as bad as you!"
    ca "To niedorzeczne. Nigdy nie miałem tak złego ucznia jak ty!"
    pause
    init 500 image anim_cathy_hj2_ep1 = Movie(channel="anim_cathy_hj2_ep1", play="images/movies/ep1/anim_cathy_hj2_ep1.webm")
    scene anim_cathy_hj2_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "I seem to have gotten your attention now, haven't I?"
    ca "Wygląda na to, że zwróciłem twoją uwagę, prawda?"
#    ca "Oh yes! I definitely have your full attention!"
    ca "O tak! Zdecydowanie mam twoją pełną uwagę!"
    pause
    scene ep1_d2_wake3b3 with dissolve
#    ca "Are you going to behave in class, [mc_cathy]? Or will I have to do this every day!?"
    ca "Będziesz się zachowywał w klasie, [mc_cathy]? A może będę musiał to robić codziennie!?"
    init 500 image anim_cathy_hj_ep1 = Movie(channel="anim_cathy_hj_ep1", play="images/movies/ep1/anim_cathy_hj_ep1.webm")
    scene anim_cathy_hj_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "You like this, don't you?"
    ca "- Podoba ci się to, prawda? -"
#    ca "Having your teacher jack you off?"
    ca "Nauczyciel cię orżnął?"
#    mc "Yes, [cathy]..."
    mc "Tak"
    pause
    scene ep1_d2_wake3b4 with dissolve
#    ca "All that cum in your cock must be making you stupid!"
    ca "Cały ten wytrysk w twoim kutasie musi cię ogłupiać!"
    init 500 image anim_cathy_hj3_ep1 = Movie(channel="anim_cathy_hj3_ep1", play="images/movies/ep1/anim_cathy_hj3_ep1.webm")
    scene anim_cathy_hj3_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "I'll get all of it out for you..."
    ca "Zdobędę wszystko dla ciebie..."
#    ca "...every single drop..."
    ca "Każdy pojedynczy"
#    mc "Faster, [cathy]...please..."
    mc "Szybciej, [cathy]...proszę..."
    pause
    init 500 image anim_cathy_hj_fast_ep1 = Movie(channel="anim_cathy_hj_fast_ep1", play="images/movies/ep1/anim_cathy_hj_fast_ep1.webm")
    scene anim_cathy_hj_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "Faster, he says... Who do you think you are?"
    ca "Szybciej, mówi… Za kogo ty się masz?"
    pause
    init 500 image anim_cathy_hj2_fast_ep1 = Movie(channel="anim_cathy_hj2_fast_ep1", play="images/movies/ep1/anim_cathy_hj2_fast_ep1.webm")
    scene anim_cathy_hj2_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
#    ca "I'm the one in charge here, [mc_cathy]."
    ca "To ja tu rządzę, [mc_cathy]."
    pause
    scene ep1_d2_wake3b6 with dissolve
#    ca "Did you hear what I just said?"
    ca "Słyszysz co powiedziałem?"
#    mc "Yes, [cathy]...please don't stop now..."
    mc "Tak, [cathy]...proszę, nie przestawaj teraz..."
    init 500 image anim_cathy_hj3_fast_ep1 = Movie(channel="anim_cathy_hj3_fast_ep1", play="images/movies/ep1/anim_cathy_hj3_fast_ep1.webm")
    scene anim_cathy_hj3_fast_ep1 with dissolve:
        size (config.screen_width, config.screen_height)
    pause
#    ca "Are you going to cum soon or what!?"
    ca "Niedługo dojdziesz, czy co!?"
    $ currentSexLabel = "ep1_cathy_lewd2b"
    $ lewd_cathy_phase = 1
    jump cathy_sex_scene_loop
    label ep1_cathy_lewd2b:
#    ca "About time! I hope that you will stay awake in class from now on..."
    ca "Najwyższy czas! Mam nadzieję, że od teraz nie będziesz zasypiał w klasie..."
    stop music fadeout 3
#    ca "...or I will have to come visit you in your dreams again."
    ca "...albo będę musiał odwiedzić Cię ponownie w Twoich snach."
    $ persistent.ep1_cathy_dream2 = True
    $ renpy.end_replay()
    $ calcScenes()
#    $ bios_history_cathy += "I had another sexy dream about Cathy. This time it ended much better than the first one.\n\n"
    $ bios_history_cathy += "Miałam kolejny seksowny sen o Kasi. Tym razem skończyło się to znacznie lepiej niż pierwsze.\n \n"
    $ bios_name_cathy = True
    $ chat_new_bios = True
scene black with fade
#my "Erm...good morning, [name]."
my "Eee... dzień dobry, [name]."
play music "music/ep1/winter_sunshine.mp3"
scene ep1_maya_morning with fade
#mc "*{i}Yawns{/i}* Good morning..."
mc "*{i}Ziewanie{/i}* Dzień dobry..."
#my "So...uh...did you sleep well?"
my "Więc...spałeś dobrze?"
#mc "Yeah, I slept really well."
mc "Tak, spałem naprawdę dobrze."
scene ep1_maya_morning1 with dissolve
#my "Did you dream about...anything in particular?"
my "Czy śniło Ci się...coś szczególnego?"
scene ep1_maya_morning2b with dissolve
#mc "Erm...why do you ask?"
mc "A czemu pytasz?"
scene ep1_maya_morning3
#mc "Oh, shit!"
mc "Cholera! "
scene ep1_maya_morning with dissolve
#mc "Sorry! I don't know what to say..."
mc "Ja nie wiem co powiedzieć..."
#my "Don't worry. These things happen."
my "Nie martw się. Takie rzeczy się zdarzają."
scene ep1_maya_morning1 with dissolve
#my "Listen, I'm going out for a run before classes."
my "Słuchaj, idę pobiegać przed zajęciami."
#my "It was nice having a roommate for the evening."
my "Miło było mieć współlokatorkę na wieczór."
scene ep1_maya_morning4 with dissolve
#mc "Thank you for letting me stay here, Maya."
mc "Dziękuję, że pozwoliłaś mi tu zostać, Mayu."
#my "No worries."
my "Nie musisz się przejmować."
#my "I hope that everything gets sorted for you today."
my "Mam nadzieję, że wszystko się dziś ułoży."
scene ep1_maya_morning5 with dissolve
stop music fadeout 3
#mc "(Me too.)"
mc "Ja też."
#mc "(And I know just where to start.)"
mc "(I wiem, od czego zacząć.)"
scene ep1_quinn_confront with wiperight
play music "music/ep1/classicals_breakbeat.mp3"
#mc "Hey!!! Quinn!"
mc "Hej!!! Quinn!"
scene ep1_quinn_confront1 with dissolve
#qu "What's up, perv boy?"
qu "Co tam, zboczeńcu?"
#qu "I almost didn't recognize you with clothes."
qu "Prawie cię nie poznałam w ubraniach."
scene ep1_quinn_confront2 with dissolve
menu:
#    "Hostile approach":
    "Wrogie podejście":
        $ dk(1)
#        mc "Stop fucking with me! Give me back my clothes, wallet and phone!"
        mc "Przestań ze mną pogrywać! Oddaj mi moje ubrania, portfel i telefon!"
#    "Calm approach":
    "Spokojne podejście":
        $ dk(-1)
#        mc "Speaking of clothes. Can I have mine back? My phone and wallet were in there."
        mc "A propos ubrań. Czy mogę odzyskać swoje? Mój telefon i portfel tam były."
scene ep1_quinn_confront1 with dissolve
#qu "Oh, yeah! That's right; there was a phone in there."
qu "A, tak! No tak, był tam telefon."
#qu "Who's Josy?"
qu "Kim jest Josy?"
scene ep1_quinn_confront2 with dissolve
#mc "What?"
mc "Co?"
scene ep1_quinn_confront3 with dissolve
#qu "She called last night; we ended up chatting."
qu "Zadzwoniła wczoraj wieczorem; skończyło się na pogawędce."
scene ep1_quinn_confront5b with dissolve
#mc "Bullshit."
mc "Bzdura. "
scene ep1_quinn_confront5 with dissolve
#qu "Hah! You should have heard the quaver in her voice when she thought I was your booty call."
qu "Hah! Szkoda, że nie słyszałeś ósemki w jej głosie, kiedy myślała, że jestem twoim seks telefonem."
scene ep1_quinn_confront5b with dissolve
menu:
#    "Hostile approach":
    "Wrogie podejście":
        $ dk(1)
        scene ep1_quinn_confront6 with dissolve
#        mc "Not funny! Give it back!"
        mc "To nie jest śmieszne! Oddawaj!"
        scene ep1_quinn_confront6b with dissolve
#        qu "Oh! Perv boy got some anger issues. I like it."
        qu "Och! Zboczeniec ma problemy z gniewem. Podoba mi się."
#    "Calm approach":
    "Spokojne podejście":
        $ dk(-1)
#        mc "Ok, you had your fun. Please, give it back now."
        mc "Ok, dobrze się bawiłeś. Proszę, oddaj go teraz."
scene ep1_quinn_confront5 with dissolve
#qu "You'll have to talk with Sage. I got bored with it."
qu "Będziesz musiał porozmawiać z Sage. Znudziło mi się to."
scene ep1_quinn_confront8 with dissolve
stop music fadeout 3
#qu "Go on in. I'm sure you're familiar with our house already, pervert."
qu "Wejdź. Na pewno znasz już nasz dom, zboczeńcu."
#$ bios_history_quinn += "Quinn gave my belongings to Sage.\n\n"
$ bios_history_quinn += "Quinn przekazał moje rzeczy Sage.\n \n"
$ bios_name_quinn = True
$ chat_new_bios = True
play music "music/ep1/funk_rock.mp3"
scene ep1_quinn_confront9 with dissolve
#mc "Sage!"
mc "Szałwia"
scene ep1_quinn_confront10 with dissolve
#sa "Ah! I knew you would come, eventually."
sa "Ach! Wiedziałem, że w końcu przyjdziesz."
#sa "Follow me."
sa "Leć za mną. "
scene ep1_quinn_confront11 with dissolve
#sa "Ok, we can talk in here."
sa "Ok, możemy porozmawiać tutaj."
#sa "So, did you think about my proposition, yet?"
sa "Myślałeś już o mojej propozycji?"
scene ep1_quinn_confront12 with dissolve
#mc "That's not why I'm here."
mc "Nie po to tu dzisiaj jestem."
#mc "Give me my belongings back."
mc "Oddaj mi moje rzeczy."
scene ep1_quinn_confront12b with dissolve
#sa "Your belongings?"
sa "Twoje rzeczy?"
scene ep1_quinn_confront12c with dissolve
#mc "Yes! My clothes, wallet and phone..."
mc "Tak! Moje ubrania, portfel i telefon..."
scene ep1_quinn_confront24 with dissolve
#mc "...AND MY GUITAR!"
mc "...I MOJA GITARA!"
scene ep1_quinn_confront12 with dissolve
#mc "You're the one who stole it!!!"
mc "To ty go ukradłeś!!!"
scene ep1_quinn_confront17 with dissolve
#sa "Hey! Calm the fuck down!"
sa "Uspokój się kurwa!"
#sa "That's my guitar. It was a gift."
sa "To moja gitara. To był prezent."
scene ep1_quinn_confront18 with dissolve
#mc "A gift? What!?"
mc "Prezent? Co!?"
#mc "Just... Please. Give it back to me."
mc "Po prostu... Proszę, oddaj mi to."
scene ep1_quinn_confront18b with dissolve
#sa "What's it worth to you?"
sa "Ile jest dla Ciebie warta?"
scene ep1_quinn_confront18 with dissolve
#mc "What?"
mc "Co?"
scene ep1_quinn_confront18b with dissolve
#sa "Will you spy on Chad for me?"
sa "Czy będziesz szpiegować Chada dla mnie?"
scene ep1_quinn_confront18 with dissolve
#mc "..."
mc "..."
#mc "Ok... I will help you with Chad. Can I have it back?"
mc "Ok... Pomogę ci z Czadem. Czy mogę go odzyskać?"
scene ep1_quinn_confront22 with dissolve
#sa "Proof first. Guitar later."
sa "Najpierw dowód. Później gitara."
scene ep1_quinn_confront12 with dissolve
#mc "Please, Sage... I need it."
mc "Proszę, Sage... Potrzebuję tego."
#mc "My dad bought that for my 12th birthday..."
mc "Mój tata kupił to na moje 12 urodziny..."
#mc "I don't think you understand how much it means to me..."
mc "Chyba nie rozumiesz, ile to dla mnie znaczy..."
#sa "..."
sa "..."
scene ep1_quinn_confront12b with dissolve
#sa "You still promise to help me?"
sa "Nadal obiecujesz mi pomóc?"
scene ep1_quinn_confront12 with dissolve
#mc "I do."
mc "To prawda."
scene ep1_quinn_confront12b with dissolve
#sa "Ok... Take it."
sa "Ok... weź to."
scene ep1_quinn_confront12 with dissolve
#mc "What about the rest of my stuff?"
mc "A co z resztą moich rzeczy?"
scene ep1_quinn_confront15 with dissolve
#sa "Sure..."
sa "Jasne…"
menu:
#    "Look closer":
    "przyjrzeć się bliżej":
        $ dk(1)
        scene ep1_quinn_confront15b with dissolve
        $ renpy.pause()
#    "Don't risk it":
    "Nie ryzykuj! ":
        $ dk(-1)
scene ep1_quinn_confront15c with dissolve
#sa "Here. I didn't know they were yours."
sa "Tutaj. Nie wiedziałem, że są twoje."
$ updateDikScore()
show screen scoremsg
$ ui.imagebutton("phone_btn_alert", "phone_btn_alert", clicked=ui.returns("OK"), xalign=0.02, yalign=0.02)
if notifications:
    play sound "sound_effects/message.mp3"
$ renpy.pause(2)
hide screen scoremsg
show screen phone_screen
#sa "Quinn gave them to me, saying that she confiscated them from a pervert..."
sa "Quinn dała mi je, mówiąc, że skonfiskowała je zboczeńcowi..."
scene ep1_quinn_confront12c with dissolve
#mc "That was me."
mc "--- "
scene ep1_quinn_confront12b with dissolve
#sa "You're the pervert?"
sa "Ty jesteś zboczeńcem?"
scene ep1_quinn_confront12 with dissolve
#mc "I'm not a pervert!"
mc "Nie jestem zboczeńcem!"
scene ep1_quinn_confront29 with dissolve
#sa "Hey..."
sa "Hej"
#mc "What?"
mc "Co?"
scene ep1_quinn_confront30 with dissolve
stop music fadeout 3
#sa "Call me when you know more about the bitch Chad is fucking."
sa "Zadzwoń do mnie, kiedy dowiesz się więcej o suce, którą pieprzy Chad."
#$ bios_history_sage += "Sage had my guitar, but she gave it back to me. She wants me to find proof on who Chad is fucking behind her back.\n\n"
$ bios_history_sage += "Sage miała moją gitarę, ale mi ją oddała. Chce, żebym znalazł dowód na to, kogo Chad pieprzy za jej plecami.\n \n"
$ number_sage = True
$ bios_name_sage = True
$ chat_new_bios = True
scene ep1_quinn_confront31 with dissolve
play music "music/ep1/classicals_breakbeat.mp3"
#qu "Wow, she gave you your things back? She must really like you."
qu "Wow, oddała ci twoje rzeczy? Musi cię naprawdę lubić."
if dtype >  0:
#    mc "Fuck you."
    mc "Pieprz si˛e."
else:
#    mc "..."
    mc "..."
scene ep1_quinn_confront32 with dissolve
#qu "Hey, hold up."
qu "Hej, zaczekaj."
#mc "What is it?"
mc "Co to jest?"
scene ep1_quinn_confront34b with dissolve
#qu "I'm not going to say I'm sorry, because I'm not. What you did was a fucking scumbag thing to do."
qu "Nie powiem, że mi przykro, bo tak nie jest. To, co zrobiłeś, było pieprzoną szumowiną."
#mc "But I-"
mc "Ale ja"
scene ep1_quinn_confront35 with dissolve
#qu "Shh!"
qu "Cicho!"
scene ep1_quinn_confront34 with dissolve
#qu "I like to fuck with people. Some like that, some don't."
qu "Lubię pieprzyć się z ludźmi. Niektóre tak, inne nie."
#qu "So, no harsh feelings?"
qu "Więc, żadnych nieprzyjemnych uczuć?"
scene ep1_quinn_confront36 with dissolve
menu:
#    "No harsh feelings":
    "Brak nieprzyjemnych uczuć":
        $ dk(-1)
#        mc "No harsh feelings..."
        mc "Bez szorstkich uczuć..."
#    "Don't accept apology":
    "Nie przyjmuj przeprosin":
        $ dk(1)
#        mc "You'll have to do better than that."
        mc "Musisz się bardziej postarać."
scene ep1_quinn_confront34 with dissolve
#qu "You're a single guy, right?"
qu "Jesteś singlem, prawda?"
scene ep1_quinn_confront36 with dissolve
#mc "What if I am?"
mc "- Co jeśli tak właśnie jest?"
scene ep1_quinn_confront39 with dissolve
$ guideSuggestedPage = 45
#qu "Yeah, you're a single guy."
qu "Tak, jesteś singlem."
#qu "Do you get laid a lot?"
qu "Często się pieprzysz?"
scene ep1_quinn_confront36 with dissolve
menu:
#    "Yes":
    "Tak":
        $ dk(1)
        if dtype > 1:
#            mc "Of course. You interested?"
            mc "Oczywiście. Zainteresowany?"
            scene ep1_quinn_confront34 with dissolve
#            qu "Hah. Maybe."
            qu "Ha. Może."
        else:
#            mc "Yes, I do."
            mc "Tak, wiem."
            scene ep1_quinn_confront34b with dissolve
#            qu "That was a lie."
            qu "To było kłamstwo."
#    "No":
    "Nie":
        $ dk(-1)
#        mc "No, I don't."
        mc "Nie, nie wiem."
        scene ep1_quinn_confront34b with dissolve
#        qu "Really? Not even gonna lie about it?"
        qu "Naprawdę? Nawet o tym nie skłamiesz?"
#    "None of your business":
    "Gówno cię to interesuje!":
#        mc "That's really none of your business."
        mc "To nie są twoje sprawy, smarkaczu."
        scene ep1_quinn_confront34b with dissolve
#        qu "Ok, that's a no."
        qu "Ok, to znaczy nie."
#        qu "And it's kind of my business..."
        qu "I to jest jakby moja sprawa..."
scene ep1_quinn_confront40 with dissolve
#qu "What if I told you that there was a way for you to {i}have some fun{/i} in a noncommittal way?"
qu "Co jeśli powiem Ci, że istnieje sposób, aby {i}dobrze się bawić{/i} w niezobowiązujący sposób?"
scene ep1_quinn_confront41 with dissolve
#mc "What are you getting at?"
mc "O co ci chodzi?"
scene ep1_quinn_confront42 with dissolve
#qu "I'm saying that I...erm..."
qu "Mówię, że ja...hmm..."
scene ep1_quinn_confront40 with dissolve
#qu "Let's say you're hungry, but you don't want to cook the food yourself. What would you do?"
qu "Powiedzmy, że jesteś głodny, ale nie chcesz sam gotować. Co byś zrobił?"
scene ep1_quinn_confront41 with dissolve
#mc "Go buy food or order take out."
mc "Idź kupić jedzenie lub zamów jedzenie na wynos."
scene ep1_quinn_confront43 with dissolve
#qu "Ah! Exactly. Take out."
qu "Ach! No właśnie. Wyjmij."
#qu "What I'm saying is that you can think of me as a {i}fast-food restaurant{/i}."
qu "Chodzi mi o to, że możesz myśleć o mnie jako o {i}restauracji typu fast-food{/i}."
#qu "Just call me and order some food and I'll get it for you."
qu "Po prostu zadzwoń do mnie i zamów coś do jedzenia, a ja Ci to przyniosę."
scene ep1_quinn_confront40 with dissolve
#qu "My menu, for the time being, consists of {i}Japanese{/i} or {i}Spicy{/i} food."
qu "Moje menu na razie składa się z dań {i}japońskich{/i} lub {i}pikantnych{/i}."
#qu "It costs a bit, but most customers are very satisfied."
qu "Trochę kosztuje, ale większość klientów jest bardzo zadowolona."
#qu "Catch my drift?"
qu "Płyniemy z prądem? He, he!"
scene ep1_quinn_confront41 with dissolve
#mc "I think I do."
mc "Myślę, że wiem."
scene ep1_quinn_confront40 with dissolve
#qu "So? You want the number to my restaurant or not?"
qu "Więc chcesz numer do mojej restauracji, czy nie?"
scene ep1_quinn_confront36 with dissolve
show screen majorChoiceScale
menu:
#    "Accept her offer":
    "Zaakceptuj jej ofertę":
#        $ bios_history_mc += "I accepted Quinn's offer to buy \"food\" from her.\n\n"
        $ bios_history_mc += "Zaakceptowałem ofertę Quinn, aby kupić od niej\"jedzenie\".\n \n"
#        $ bios_history_quinn += "I accepted Quinn's offer to buy \"food\" from her.\n\n"
        $ bios_history_quinn += "Zaakceptowałem ofertę Quinn, aby kupić od niej\"jedzenie\".\n \n"
        $ bios_name_quinn = True
        $ chat_new_bios = True
        $ ep1_accepted_quinn_offer = True
        $ addCPenalty()
        $ renpy.pause(1)
#        mc "Sure."
        mc "Dobrze."
        hide screen majorChoiceScale
        scene ep1_quinn_confront46 with dissolve
#        qu "Here you go."
        qu "Proszę bardzo."
        $ number_quinn = True
#        qu "FYI. You pick up your food in the corner booth of the bathroom next to dorms 72 and 73."
        qu "Dla twojej informacji. Odbierasz jedzenie w narożnej kabinie łazienki obok akademików 72 i 73."
#    "Reject her offer":
    "Odrzuć jej ofertę":
#        $ bios_history_mc += "I rejected Quinn's offer to buy sexual favors through her.\n\n"
        $ bios_history_mc += "Odrzuciłem ofertę Quinn, aby kupić za jej pośrednictwem przysługi seksualne.\n \n"
#        $ bios_history_quinn += "I rejected Quinn's offer to buy sexual favors through her.\n\n"
        $ bios_history_quinn += "Odrzuciłem ofertę Quinn, aby kupić za jej pośrednictwem przysługi seksualne.\n \n"
        $ ep1_accepted_quinn_offer = False
        $ bios_name_quinn = True
        $ chat_new_bios = True
        $ addDPenalty()
        $ renpy.pause(1)
#        mc "No, I don't pay for sex, Quinn! What the hell is the matter with you!?"
        mc "Nie, nie płacę za seks, Quinn! Co się z tobą do cholery dzieje!?"
        hide screen majorChoiceScale
scene ep1_quinn_confront47 with dissolve
stop music fadeout 3
#qu "Bye, pervert!"
qu "Pa, zboczeńcu!"
scene ep1_lib_thank0 with wiperight
$ renpy.sound.play("sound_effects/library_ambience.mp3", channel="sfx1", loop=True)
#sb "Well, that settles it. Friday night it is."
sb "Cóż, to załatwia sprawę. Niech będzie piątek wieczór."
#sb "If you don't mind, you can bring a bottle of wine."
sb "Jeśli nie masz nic przeciwko, możesz przynieść butelkę wina."
if preferredmilf == 0:
#    mc "(Jade...)"
    mc "Jade"
#    mc "*{i}Gulp{/i}*"
    mc "Połykanie"
scene ep1_lib_thank1 with dissolve
#sb "Ah, enough chatting. We're keeping you from customers."
sb "Ach, dość gadania. Odciągamy Cię od klientów."
scene ep1_lib_thank2 with dissolve
#sb "Hey there, sport."
sb "Cześć, sportowcu."
menu:
#    "Say hey":
    "Powiedzcie: Hej! ":
        $ dk(-1)
#        mc "Hi."
        mc "Cześć."
#    "Retort":
    "Retorta":
        $ dk(1)
        if dtype > 0:
#            mc "What's up, gramps?"
            mc "Co słychać, dziadku?"
        else:
#            mc "Sport? I'm not a kid, mister."
            mc "Sport? Nie jestem dzieckiem, proszę pana."
        scene ep1_lib_thank3 with dissolve
#        sb "Ah..."
        sb "---"
$ bios_burke = True
#$ bios_history_burke = "I saw him chat with Jade and Isabella.\n\n"
$ bios_history_burke = "Widziałem, jak rozmawia z Jade i Isabellą.\n \n"
#$ bios_history_jade = "Call me crazy, but I think Jade checked me out in the library!\n\n"
$ bios_history_jade = "Nazwij mnie wariatką, ale myślę, że Jade sprawdziła mnie w bibliotece!\n \n"
$ bios_name_burke = True
$ bios_jade = True
$ bios_name_jade = True
$ chat_new_bios = True
scene ep1_lib_thank4 with dissolve
#isa "Yes?"
isa "Tak?"
scene ep1_lib_thank5 with dissolve
menu:
#    "Joke":
    "Dowcip":
#        mc "That's not how you start a conversation."
        mc "Nie tak się rozpoczyna rozmowę."
        scene ep1_lib_thank6 with dissolve
#        mc "Where are your manners, woman?"
        mc "Gdzie twoje maniery, kobieto?"
#        mc "...you know..."
        mc " że w ogóle."
#        mc "...because you told me that yesterday, remember?"
        mc "...bo powiedziałeś mi to wczoraj, pamiętasz?"
#    "Say hey":
    "Powiedzcie: Hej! ":
#        mc "Hi, Isabella."
        mc "Cześć, Isabella."
scene ep1_lib_thank4 with dissolve
#isa "What do you need?"
isa "Czego potrzebujesz?"
scene ep1_lib_thank5 with dissolve
#mc "I don't need anything, really."
mc "Niczego nie potrzebuję, naprawdę."
#mc "I came to thank you for helping me yesterday and to say that I'm sorry for the way I behaved."
mc "Przyszedłem podziękować za wczorajszą pomoc i przeprosić za to, jak się zachowałem."
#mc "I got my belongings back..."
mc "Odzyskałem swoje rzeczy..."
scene ep1_lib_thank4 with dissolve
#isa "Ok. Anything else?"
isa "Ok. Coś jeszcze?"
scene ep1_lib_thank5 with dissolve
#mc "No...I...ah..."
mc "Nie...ja...ah..."
#mc "..."
mc "..."
#mc "No. Nothing else."
mc "Nic więcej."
#mc "Bye, Isabella."
mc "Pa, Izabelo."
scene ep1_lib_thank6b with dissolve
#mc "(It doesn't feel like she accepted my apology...)"
mc "(Nie wydaje mi się, żeby przyjęła moje przeprosiny...)"
#mc "(Maybe I can help her around here somehow?)"
mc "(Może mogę jej tu jakoś pomóc?)"
scene ep1_lib_thank7 with dissolve
#mc "(That book cart is full.)"
mc "(Ten wózek na książki jest pełny.)"
scene ep1_lib_thank8 with wiperight
if dtype > 0:
#    mc "(Back into the shelves you go...)"
    mc "(Wracasz na półki...)"
else:
#    mc "(The good old Dewey Decimal system...)"
    mc "(Stary dobry system dziesiętny Deweya...)"
scene ep1_lib_thank8b with dissolve
#mc "(The myth of the male orgasm...)"
mc "(Mit męskiego orgazmu...)"
#mc "(Who would write this, let alone read it?)"
mc "(Kto by to napisał, a co dopiero przeczytał?)"
scene ep1_lib_thank10 with wiperight
#mc "(There. All done.)"
mc "(Gotowe.)"
scene ep1_lib_thank11 with dissolve
#mc "(Hey...isn't that Jill?)"
mc "(Hej...czy to nie Jill?)"
#mc "(She's here all alone? This could be my chance to talk to her some more.)"
mc "(Jest tu całkiem sama? To może być moja szansa, żeby jeszcze z nią porozmawiać.)"
scene ep1_lib_thank12 with dissolve
#mc "Hey! Jill, was it? Mind if I sit down?"
mc "Hej! Jill, tak? Mogę usiąść?"
scene ep1_lib_thank12b with dissolve
#ji "Please, go ahead."
ji "Proszę bardzo."
scene ep1_lib_thank14 with dissolve
if dtype > 0:
#    mc "Are you reading?"
    mc "Czytasz? "
    scene ep1_lib_thank15 with dissolve
#    ji "Yeah, that's mostly what people do in a library."
    ji "Tak, to głównie ludzie robią w bibliotece."
else:
    $ RPjill += 1
#    mc "I don't want to bother you if you're busy studying."
    mc "Nie chcę ci przeszkadzać, jeśli jesteś zajęta nauką."
    scene ep1_lib_thank15 with dissolve
#    ji "It's fine. Really. Although..."
    ji "W porządku. Naprawdę. Chociaż..."
scene ep1_lib_thank16 with dissolve
#ji "We're not supposed to be talking in here, you know."
ji "Wiesz, że nie powinniśmy tu rozmawiać."
scene ep1_lib_thank14 with dissolve
#mc "Oh, it's cool. Me and Isabella are friends now. I'm sure she doesn't mind us chatting."
mc "O, spoko. Ja i Izabela jesteśmy teraz przyjaciółkami. Na pewno nie przeszkadza jej, że rozmawiamy."
scene ep1_lib_thank16 with dissolve
#ji "Is that so?"
ji "Ach tak?"
scene ep1_lib_thank14 with dissolve
#mc "Yup."
mc "Tak."
scene ep1_lib_thank16b with dissolve
#ji "If you really were friends, you would know that she prefers to be called Bella and that she absolutely still would mind you talking in here..."
ji "Gdybyście naprawdę byli przyjaciółmi, wiedziałbyś, że wolałaby, żeby ją nazywać Bella i że nadal miałaby absolutnie coś przeciwko, żebyście tu porozmawiali..."
#ji "...friend or not."
ji "...przyjacielem czy nie."
scene ep1_lib_thank14 with dissolve
#mc "Oh... So, you're her friend, then."
mc "Och... Więc jesteś jej przyjaciółką."
scene ep1_lib_thank16 with dissolve
#ji "Yup."
ji "Tak."
scene ep1_lib_thank14 with dissolve
if dtype > 0:
#    mc "Ok. I'll leave you to it."
    mc "---"
else:
#    mc "Ok. I'm sorry. I'll leave you to it."
    mc "Ok. Przepraszam. Zostawię cię z tym."
scene ep1_lib_thank15 with dissolve
#ji "Wait. You don't have to go."
ji "Nie musisz iść "
#ji "I'm sure she won't mind, as long as we keep our voices down."
ji "Jestem pewien, że nie będzie miała nic przeciwko, o ile będziemy cicho."
scene ep1_lib_thank14 with dissolve
#mc "*{i}Inaudible whisper{/i}*"
mc "*{i}Szept niesłyszalny{/i}*"
scene ep1_lib_thank15 with dissolve
#ji "What?"
ji "Co?"
scene ep1_lib_thank14 with dissolve
menu:
#    "Whisper again":
    "Szepcz jeszcze raz":
#        mc "*{i}Inaudible whisper{/i}*"
        mc "*{i}Szept niesłyszalny{/i}*"
        scene ep1_lib_thank15 with dissolve
        $ guideSuggestedPage = 46
#        ji "Come sit down over here. I can't hear you."
        ji "Usiądź tutaj. Nie słyszę cię."
#    "Sit down closer to her":
    "Usiądź bliżej niej":
#        mc "Let me sit closer to you so you can hear me."
        mc "Usiądę bliżej ciebie, żebyś mnie usłyszał."
        scene ep1_lib_thank19 with dissolve
        $ guideSuggestedPage = 46
#        ji "Smooth move..."
        ji "Płynny ruch..."
        scene ep1_lib_thank19b with dissolve
        menu:
#            "Thanks":
            "Dziękujemy":
                $ RPjill -= 1
#                mc "Thanks."
                mc "Dzięki."
#            "It wasn't a move":
            "To nie był ruch":
#                mc "Oh, that wasn't a move."
                mc "Och, to nie był ruch."
scene ep1_lib_thank21 with dissolve
#mc "Do you come here often?"
mc "Czy ty to zbudowałeś?"
scene ep1_lib_thank22 with dissolve
#ji "As a matter of fact, I do. This is the only place where I get to be truly alone."
ji "Prawdę mówiąc, tak. To jedyne miejsce, w którym mogę być naprawdę sam."
scene ep1_lib_thank21 with dissolve
#mc "And here I am ruining that moment for you."
mc "I tutaj rujnuję ten moment dla ciebie."
scene ep1_lib_thank22b with dissolve
#ji "I didn't mean it like that."
ji "Nie to miałam na myśli."
#ji "How can I explain it?"
ji "Jak mogę to wyjaśnić?"
#ji "..."
ji "..."
#ji "Ah, never mind. I just like this place a lot."
ji "Ach, nieważne. Po prostu bardzo lubię to miejsce."
#ji "It's much more cozy and comfortable than the library in the Alpha Nu Omega mansion, too."
ji "Jest znacznie bardziej przytulny i wygodny niż biblioteka w rezydencji Alpha Nu Omega."
scene ep1_lib_thank21 with dissolve
#mc "Wow, they even have their own library in there?"
mc "Wow, mają tam nawet własną bibliotekę?"
scene ep1_lib_thank22 with dissolve
#ji "Yeah."
ji "Tak."
scene ep1_lib_thank22c with dissolve
#ji "So...I hope you've been doing okay since last time."
ji "Więc...mam nadzieję, że dobrze sobie radzisz od ostatniego razu."
scene ep1_lib_thank21 with dissolve
#mc "Ah, I'm guessing you're alluding to the wedgie?"
mc "Ach, zgaduję, że nawiązujesz do wedżi?"
#mc "There've been some minor wardrobe malfunctions, but overall...I'm ok."
mc "Wystąpiły drobne awarie garderoby, ale ogólnie... nic mi nie jest."
scene ep1_lib_thank22 with dissolve
#ji "You seem to take it pretty well..."
ji "Wygląda na to, że dobrze to znosisz..."
scene ep1_lib_thank22c with dissolve
#ji "I don't want to pry, but...that's not the first time you've dealt with bullies, huh?"
ji "Nie chcę się wtrącać, ale...to nie pierwszy raz, kiedy masz do czynienia z łobuzami, co?"
scene ep1_lib_thank21 with dissolve
#mc "Erm...I-"
mc "Erm...ja-"
scene ep1_lib_thank25 with dissolve
#mc "H-Hey Bella!"
mc "H-Hej Bella!"
scene ep1_lib_thank26 with dissolve
#isa "Bella?"
isa "Bella"
scene ep1_lib_thank26b with dissolve
#isa "What did you tell him?"
isa "--- "
#ji "Just that friends call you Bella."
ji "Tylko to, że przyjaciele nazywają cię Bellą."
scene ep1_lib_thank26c with dissolve
#isa "You know that a library is for reading and studying, [name]."
isa "Wiesz, że biblioteka służy do czytania i nauki, [name]."
#isa "Not for hitting on girls."
isa "Nie za podrywanie dziewczyn."
#ji "Bella!"
ji "Bella"
scene ep1_lib_thank31 with dissolve
if dtype > 0:
#    mc "Gah. You seem to have a personal vendetta with me. I'm leaving..."
    mc "Wygląda na to, że masz ze mną osobistą wendettę. Wychodzę..."
else:
#    mc "All right... I'm leaving."
    mc "Dobra... wychodzę."
#mc "Bye, Jill."
mc "Pa, Jill."
#ji "I...ah...bye."
ji "Ja...ach...pa."
#$ bios_history_isabella +="I tried apologizing to Bella, but she doesn't seem to like me at all.\n\n"
$ bios_history_isabella +="Próbowałem przeprosić Bellę, ale wydaje się, że w ogóle mnie nie lubi.\n \n"
#$ bios_history_jill +="I got a chance to talk more to Jill. She's really nice...and a friend of Bella....which is kind of weird.\n\n"
$ bios_history_jill +="Miałem okazję porozmawiać więcej z Jill. Jest naprawdę miła...i przyjaciółką Belli...co jest trochę dziwne.\n \n"
$ bios_name_jill = True
$ bios_name_isabella = True
$ chat_new_bios = True
scene ep1_lib_thank33 with dissolve
#ji "That was kind of rude."
ji "To było trochę niegrzeczne."
scene ep1_lib_thank34 with dissolve
#isa "Trust me. I know that boy. You should stay away from him."
isa "Zaufaj mi. Znam tego chłopca. Trzymaj się od niego z daleka."
scene ep1_lib_thank33 with dissolve
#ji "What? Why?"
ji "Co? Dlaczego?"
scene ep1_lib_thank34 with dissolve
#isa "Let's just say that he has a habit of getting into trouble."
isa "Powiedzmy, że ma zwyczaj wpadania w kłopoty."
scene ep1_lib_thank35 with dissolve
#ji "More trouble?"
ji "Więcej kłopotów?"
scene ep1_lib_thank36 with dissolve
#isa "What do you mean {b}more{/b} trouble!? What trouble do you know of!?"
isa "Jak to {b}więcej{/b} kłopotów!? O jakich kłopotach wiesz!?"
scene ep1_lib_thank35 with dissolve
#ji "I saw him get bullied by the tri-alphas yesterday."
ji "Widziałem, jak wczoraj znęcały się nad nim tri-alfy."
#ji "They were ganging up on him and pulled his underwear up."
ji "Spięli się na nim i podciągnęli jego bieliznę."
scene ep1_lib_thank37 with dissolve
#isa "Oh..."
isa "Och..."
scene ep1_lib_thank35 with dissolve
#ji "Yeah, I couldn't help but feel sorry for him."
ji "Tak, nie mogłem przestać mu współczuć."
scene ep1_lib_thank37 with dissolve
#isa "Where you're coming from...I understand."
isa "Stamtąd, skąd pochodzisz...rozumiem."
scene ep1_lib_thank35b with dissolve
#ji "Also, I don't think he's such a bad guy."
ji "Poza tym nie sądzę, żeby był taki zły."
#ji "I saw him spend like 10 minutes putting books from your cart back into their shelves."
ji "Widziałem, jak spędzał jakieś 10 minut, odkładając książki z twojego wózka z powrotem na półki."
scene ep1_lib_thank37c with dissolve
$ renpy.pause()
scene ep1_lib_thank37b with dissolve
#isa "..."
isa "..."
scene ep1_lib_thank35b with dissolve
#ji "And he's been nothing but nice to me."
ji "I był dla mnie tylko miły."
scene ep1_lib_thank34 with dissolve
#isa "Is there something going on between the two of you?"
isa "Czy coś się dzieje między wami?"
scene ep1_lib_thank33 with dissolve
#ji "What? No! I just..."
ji "Co? Nie! Ja tylko..."
#ji "We've barely talked to each other..."
ji "Ledwo ze sobą rozmawialiśmy..."
scene ep1_lib_thank35b with dissolve
#ji "...but I have to admit that it's nice to socialize with someone who doesn't talk about their successful parents or economics every single minute."
ji "...ale muszę przyznać, że miło jest spotykać się z kimś, kto w każdej minucie nie mówi o swoich odnoszących sukcesy rodzicach czy ekonomii."
scene ep1_lib_thank37 with dissolve
#isa "Just...be careful, Jill. You know I want what's best for you."
isa "Tylko...bądź ostrożna, Jill. Wiesz, że chcę dla ciebie jak najlepiej."
scene ep1_lib_thank42 with dissolve
#ji "I know, Bella. I love you for that."
ji "Wiem, Bella. Kocham cię za to."
scene ep1_lib_thank43 with dissolve
#ji "So, you think I shouldn't socialize with him?"
ji "Więc myślisz, że nie powinnam się z nim spotykać?"
$ renpy.music.stop(channel="sfx1", fadeout=3)
scene ep1_lib_thank44 with dissolve
#isa "..."
isa "..."
play music "music/ep1/golden_alley.mp3"
scene ep1_mdorm with wipeleft
#mc "Hey! Where have you been?"
mc "Co słychać?"
scene ep1_mdorm3 with dissolve
#my "Out...doing stuff..."
my "Wychodzę...robię rzeczy..."
#my "Wait...why are you still here?"
my "Czemu wciąż tu jesteś?"
scene ep1_mdorm2 with dissolve
#mc "I was thinking that maybe...just maybe..."
mc "Myślałem, że może...tylko może..."
#mc "...you would let me stay here until I find another dorm?"
mc "...pozwolisz mi tu zostać, dopóki nie znajdę innego akademika?"
scene ep1_mdorm3 with dissolve
#my "Wow...really?"
my "Wow, naprawdę?!"
scene ep1_mdorm8b with dissolve
#mc "Listen, I went to the reception earlier, but it's not simple to change dorms all of a sudden."
mc "Słuchaj, poszedłem wcześniej na przyjęcie, ale nie jest łatwo nagle zmienić akademik."
#mc "There's this big process behind it..."
mc "Stoi za tym wielki proces..."
scene ep1_mdorm4 with dissolve
#my "Well, fuck it. It's not like I was going to let you live outdoors anyway."
my "Cóż, pieprzyć to. I tak nie zamierzałem pozwolić ci mieszkać na świeżym powietrzu."
scene ep1_mdorm5 with dissolve
#mc "Really!?"
mc "Serio. "
scene ep1_mdorm4 with dissolve
#my "Yes, but only until you find yourself another place to stay!"
my "Tak, ale tylko do czasu, aż znajdziesz sobie inne miejsce pobytu!"
#my "Or until I get a new dorm mate."
my "Albo dopóki nie dostanę nowego kolegi z akademika."
scene ep1_mdorm5 with dissolve
#mc "About that, why don't I ask them if I can just share this dorm with you?"
mc "Co do tego, dlaczego nie zapytam ich, czy mogę po prostu podzielić się z wami tym akademikiem?"
scene ep1_mdorm8 with dissolve
#my "You didn't tell them that, did you!?"
my "Nie powiedziałeś im tego, prawda!?"
scene ep1_mdorm8b with dissolve
#mc "That your dorm mate is a no-show? No, I didn't."
mc "Że twój kolega z akademika się nie pojawił? Nie, nie zrobiłem tego."
scene ep1_mdorm10 with dissolve
#my "*{i}Phew{/i}* Good!"
my "*{i}Uff{/i}* Dobrze!"
#my "It's just that I hit the jackpot for once, and I don't want to lose the privilege of having my own room here."
my "Po prostu choć raz trafiłem w dziesiątkę i nie chcę stracić przywileju posiadania tutaj własnego pokoju."
scene ep1_mdorm10b with dissolve
#mc "Anyway...thanks! I'll try not to annoy you."
mc "W każdym razie...dzięki! Postaram się cię nie denerwować."
scene ep1_mdorm10 with dissolve
#my "Don't worry. You're cool."
my "Nie martw się. Jesteś spoko."
#my "You got your phone back yet?"
my "Odzyskałeś już telefon?"
scene ep1_mdorm10b with dissolve
#mc "Yeah, I did!"
mc "Tak, zrobiłem."
scene ep1_mdorm15 with dissolve
#my "You should take my number in case you get locked out or something."
my "Weź mój numer na wypadek, gdybyś się zatrzasnął."
$ number_maya = True
jump ep1_freeroam_movie_maya_label
label ep1_maya_movie_label:

scene fr_ep1_movie with dissolve
menu:
    "Sneak a peek ({color=#ffffff}{size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 0:
        scene fr_ep1_movieb with dissolve
#        mc "(Damn, that's sexy...)"
        mc "(Cholera, to jest seksowne...)"
        if assman:
#            mc "(Derek's right...I am the ass man.)"
            mc "(Derek ma rację...to ja jestem dupkiem.)"
        scene fr_ep1_movie with dissolve
#    "Ask her what she's doing":
    "Zapytaj ją, co robi":
        $ renpy.pause(0.5)
#mc "What are you up to?"
mc "Co porabiasz?"
#my "Just watching a movie."
my "Po prostu oglądam film."
#mc "On your phone?"
mc "Na telefonie?"
scene fr_ep1_movie2 with dissolve
#my "Yeah, do you see a TV in here?"
my "Tak, widzisz tu telewizor?"
scene fr_ep1_movie2b with dissolve
#mc "It's just that the screen is so small."
mc "Po prostu ekran jest taki mały."
scene fr_ep1_movie2 with dissolve
#my "You get used to it. Besides, I couldn't give up watching movies."
my "Przyzwyczajasz się do tego. Poza tym nie mogłem zrezygnować z oglądania filmów."
scene fr_ep1_movie2b with dissolve
#mc "Ah, so you're a movie buff then?"
mc "Ach, więc jesteś miłośnikiem filmów?"
scene fr_ep1_movie3 with dissolve
#my "Big time! How about you?"
my "Wielkie dzięki! A ty?"
scene fr_ep1_movie2b with dissolve
#mc "No, growing up, we didn't have..."
mc "Nie, dorastając, nie mieliśmy..."
#mc "No, I'm not into movies."
mc "Nie, nie kręcą mnie filmy."
scene fr_ep1_movie4 with dissolve
#my "What was that first part?"
my "Co to była za pierwsza część?"
scene fr_ep1_movie2b with dissolve
#mc "I was going to say that we didn't have a TV when I grew up..."
mc "Chciałem powiedzieć, że nie mieliśmy telewizora, kiedy dorastałem..."
#mc "...but I stopped because it's both personal and embarrassing..."
mc "...ale przestałem, bo to jest zarówno osobiste, jak i żenujące..."
scene fr_ep1_movie2 with dissolve
#my "You don't have to feel embarrassed about that."
my "Nie musisz się tego wstydzić."
#my "Look at me! I don't have a TV now."
my "Spójrz na mnie! Nie mam teraz telewizora."
scene fr_ep1_movie2b with dissolve
#mc "Yeah..."
mc "Tak"
scene fr_ep1_movie2 with dissolve
#my "Hey, I'm glad you told me."
my "Hej, cieszę się, że mi powiedziałeś."
scene fr_ep1_movie3 with dissolve
#my "Maybe you're a movie nerd too. You just don't know it yet."
my "Może też jesteś maniakiem filmowym. Po prostu jeszcze o tym nie wiesz."
scene fr_ep1_movie2b with dissolve
#mc "Haha, maybe."
mc "Haha, może."
scene fr_ep1_movie8 with dissolve
#my "Come."
my "Podejdź."
scene fr_ep1_movie9 with dissolve
#mc "What?"
mc "Co?"
scene fr_ep1_movie8 with dissolve
#my "Lie next to me, stupid. We can watch it together."
my "Połóż się obok mnie, głupia. Możemy to obejrzeć razem."
scene fr_ep1_movie9 with dissolve
#mc "Oh, ok."
mc "Oh, ok."
scene fr_ep1_movie10 with dissolve
$ guideSuggestedPage = 47
#mc "(Her vanilla perfume smells amazing on her...)"
mc "(Jej waniliowe perfumy pachną niesamowicie...)"
menu:
#    "Look closer":
    "przyjrzeć się bliżej":
        $ dk(1)
        scene fr_ep1_movie10b with dissolve
        if dtype > 0:
#            mc "(Fuck me...)"
            mc "Pieprz mnie"
        else:
#            mc "(I shouldn't be looking...but I just can't resist.)"
            mc "(Nie powinnam patrzeć...ale po prostu nie mogę się oprzeć.)"
        scene fr_ep1_movie10 with dissolve
#    "Don't look closer":
    "Nie przyglądaj się":
        $ dk(-1)
        $ renpy.pause(0.5)
#mc "What are we watching?"
mc "Dlaczego mamy czuwać?”."
#my "An old horror movie called \"The Secret in His Closet\"."
my "Stary horror zatytułowany „Sekret w jego szafie”."
#my "It's one of my all-time favorites!"
my "To jeden z moich ulubionych!"
#my "It's about this older man living alone who has a routine of always going into his closet every night."
my "Chodzi o tego starszego mężczyznę mieszkającego samotnie, który ma rutynę ciągłego wchodzenia do swojej szafy każdej nocy."
scene fr_ep1_movie12 with dissolve
#mc "Into it?"
mc "Wchodzisz w to?"
scene fr_ep1_movie11b with dissolve
#my "Yeah! The kids next door watch him through their bedroom window every night and become obsessed with it."
my "Tak! Dzieciaki z sąsiedztwa obserwują go co wieczór przez okno sypialni i mają na jego punkcie obsesję."
#my "Like, why would he go into a closet?"
my "Na przykład, dlaczego miałby wejść do szafy?"
#my "So, they sneak into his house when he leaves to run an errand and try to find out what's in there."
my "Więc zakradają się do jego domu, kiedy wychodzi coś załatwić i próbują dowiedzieć się, co tam jest."
scene fr_ep1_movie12 with dissolve
#mc "That sounds really interesting."
mc "To brzmi naprawdę interesująco."
stop music fadeout 3
scene fr_ep1_movie11b with dissolve
#my "Yeah, let's watch! I'm not going to spoil what happens for you."
my "Tak, obejrzyjmy! Nie zamierzam zepsuć tego, co się z tobą dzieje."
play music "music/ep1/lost_souls.mp3"
scene fr_ep1_movie13 with fade
#mc "(This movie is fucking scary!)"
mc "(Ten film jest kurewsko przerażający!)"
#kid "Jonathan! Hide! He's coming back home!"
kid "Jonatan! Schowaj się! Wraca do domu!"
#mc "(Oh shit!)"
mc "---"
scene fr_ep1_movie14 with dissolve
#my "Are you ok there, [name]?"
my "Wszystko w porządku, [name]?"
scene fr_ep1_movie15 with dissolve
#mc "Yeah, I just haven't watched a lot of scary movies..."
mc "Tak, po prostu nie oglądałem zbyt wielu strasznych filmów..."
scene fr_ep1_movie14 with dissolve
#my "It's the best feeling, huh?"
my "To najlepsze uczucie, co?"
scene fr_ep1_movie13 with dissolve
#kid "Quick! Hide under the bed!"
kid "Szybko! Schowaj się pod łóżkiem!"
scene fr_ep1_movie13b with dissolve
#kid "NO!!!! JONATHAN!!!"
kid "NIE!!!! JONATHAN!!!"
scene black
#my "Hey! You're missing the best part!"
my "Hej! Przegapisz najlepszą część!"
scene fr_ep1_movie15 with dissolve
#mc "Sorry, it's just too scary for me."
mc "Przepraszam, po prostu mnie to przeraża."
scene fr_ep1_movie14 with dissolve
#my "Aw..."
my "AW"
#my "Here, hold the phone."
my "Trzymaj telefon."
scene fr_ep1_movie15 with dissolve
stop music fadeout 3
#mc "How is that going to help?"
mc "Jak to ma pomóc?"
scene fr_ep1_movie17 with dissolve
#mc "(Oh...)"
mc "Och..."
play music "music/ep1/windswept.mp3"
#mc "What are you doing?"
mc "Co robisz? "
scene fr_ep1_movie19 with dissolve
#my "I'm comforting you."
my "Pocieszam cię."
#my "Feeling better?"
my "Czuje się lepiej"
scene fr_ep1_movie17 with dissolve
#mc "Yeah..."
mc "Tak"
scene fr_ep1_movie21 with dissolve
#mc "(Why is she doing this?)"
mc "Dlaczego ona to robi?"
#mc "(Maybe she likes me?)"
mc "(Może mnie lubi?)"
scene fr_ep1_movie21b with dissolve
#mc "(Oh my God... Those are the strings of her panties I feel...)"
mc "(O mój Boże... To są sznurki jej majtek, które czuję...)"
scene fr_ep1_movie21c with dissolve
#mc "(She doesn't mind that I have my hand here?)"
mc "(Nie przeszkadza jej, że trzymam tu rękę?)"
#my "This part is so scary!"
my "Ta część jest taka przerażająca!"
#mc "(She has the softest skin...)"
mc "(Ma najdelikatniejszą skórę...)"
scene fr_ep1_movie21 with dissolve
menu:
#    "Smell her hair":
    "Powąchaj jej włosy":
        scene fr_ep1_movie24 with dissolve
#        mc "*{i}Inhales deeply{/i}*"
        mc "Głęboko nabiera powietrza. "
        scene fr_ep1_movie25 with dissolve
#        my "Are you...smelling my hair?"
        my "Czy ty...wąchasz moje włosy?"
        scene fr_ep1_movie26 with dissolve
        if dtype > 0:
            $ RPmaya-=1
#            mc "Yeah, you smell good."
            mc "Ładnie pachniesz."
            scene fr_ep1_movie26b with dissolve
#            my "Please, stop that..."
            my "Proszę, przestań..."
        else:
#            mc "No...I was just breathing. This is so scary!"
            mc "Nie... po prostu oddychałam. To takie straszne!"
            scene fr_ep1_movie27 with dissolve
#            my "Yeah!"
            my "Tak jest!"
#    "Don't risk it":
    "Nie ryzykuj! ":
        $ dk(-1)
scene fr_ep1_movie28 with dissolve
#mc "(She has her leg over mine! How am I supposed to focus now?)"
mc "(Ona trzyma nogę nad moją! Jak mam się teraz skupić?)"
scene fr_ep1_movie29 with dissolve
#my "Wow, your heart is beating like really fast!"
my "Wow, Twoje serce bije jak szalone!"
#my "I had no idea that you were this scared."
my "Nie miałam pojęcia, że tak się boisz."
scene fr_ep1_movie30 with dissolve
#mc "Yeah, this is horrifying."
mc "To przerażające."
scene fr_ep1_movie27 with dissolve
#my "Aw..."
my "AW"
scene fr_ep1_movie32 with dissolve
#mc "(She moved it even higher up!)"
mc "(Przesunęła go jeszcze wyżej!)"
#mc "(Fuck! I'm going to get a boner from this...not good...)"
mc "(Kurwa! Staną mi od tego...niedobrze...)"
menu:
#    "Push her leg down":
    "Popchnij jej nogę w dół":
        $ RPmaya += 1
        scene fr_ep1_movie30 with dissolve
#        mc "Maya...your leg is a bit too high up..."
        mc "Maya...twoja noga jest trochę za wysoko..."
        scene fr_ep1_movie33 with dissolve
#        my "Oh! I wasn't touching...you know?"
        my "Och! Nie dotykałem...wiesz?"
        scene fr_ep1_movie30 with dissolve
#        mc "No, it's fine."
        mc "W porządku."
        scene fr_ep1_movie27 with dissolve
#        my "Ok. Thanks for telling me."
        my "Dzięki, że mi powiedziałaś/-eś"
#    "Linger longer":
    "Dłuższy czas oczekiwania":
        scene fr_ep1_movie31 with dissolve
#        my "(Hm...I think my thigh is touching his dick...)"
        my "(Hm...myślę, że moje udo dotyka jego penisa...)"
        scene fr_ep1_movie36 with dissolve
#        my "(Why isn't he saying anything?)"
        my "(Dlaczego on nic nie mówi?)"
        scene fr_ep1_movie31b with dissolve
        if dtype > 0:
#            mc "(Damn...)"
            mc "Potępienie"
        else:
#            mc "(Phew...)"
            mc "Uff... "
scene fr_ep1_movie30 with dissolve
#mc "Maybe this is weird to ask but..."
mc "Może to dziwne pytanie, ale..."
#mc "...didn't you say that you have a boyfriend?"
mc "...nie mówiłaś, że masz chłopaka?"
scene fr_ep1_movie29 with dissolve
#my "Erm...yeah...I..."
my "Hmm...tak...ja..."
#my "Why?"
my "Dlaczego?"
scene fr_ep1_movie30 with dissolve
#mc "I just think that it's a bit weird lying like this with you if that's the case..."
mc "Po prostu myślę, że to trochę dziwne tak z tobą kłamać, jeśli o to chodzi..."
scene fr_ep1_movie33 with dissolve
#my "Well...it's...complicated...I..."
my "No...to...skomplikowane...ja..."
#my "Can you keep a secret?"
my "Czy potrafisz dochować tajemnicy?"
scene fr_ep1_movie30 with dissolve
#mc "Yes, of course."
mc "Oczywiście, że tak.&amp;nbsp;"
scene fr_ep1_movie33 with dissolve
#my "...and promise me that you won't ask any more questions if I tell you this?"
my "...i obiecaj mi, że nie będziesz zadawać więcej pytań, jeśli ci to powiem?"
scene fr_ep1_movie30 with dissolve
#mc "Sure..."
mc "Jasne…"
scene fr_ep1_movie33 with dissolve
#my "I don't have a boyfriend."
my "Nie mam chłopaka."
#my "I tell guys I have a boyfriend because I'm not interested in attracting them."
my "Mówię chłopakom, że mam chłopaka, bo nie jestem zainteresowana ich przyciąganiem."
#my "It may sound weird...but that's the only way that seems to work."
my "Może to zabrzmi dziwnie...ale to jedyny sposób, który wydaje się działać."
scene fr_ep1_movie30 with dissolve
#mc "Ok, so you don't want me to be attracted to you?"
mc "Ok, więc nie chcesz, żebym była dla ciebie atrakcyjna?"
scene fr_ep1_movie26b with dissolve
#my "Hey...you promised not to ask any more questions..."
my "Hej...obiecałeś nie zadawać więcej pytań..."
#my "..."
my "..."
scene fr_ep1_movie33 with dissolve
#my "...but yeah..."
my "ale tak. "
#my "...it would probably be for the best if you weren't."
my "... prawdopodobnie byłoby lepiej, gdybyś tego nie robił."
scene fr_ep1_movie21 with dissolve
menu:
#    "Too late for that":
    "Na to już za późno":
#        $ bios_history_maya += "I had a movie night with Maya. I told her I'm attracted to her.\n\n"
        $ bios_history_maya += "Miałem noc filmową z Mayą. Powiedziałem jej, że mi się podoba.\n \n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ ep1_maya_attracted = True
        $ RPmaya+=1
#        mc "..."
        mc "..."
#        mc "I think it's too late for that."
        mc "Myślę, że już na to za późno."
        scene fr_ep1_movie25 with dissolve
#        my "Oh..."
        my "Och..."
        scene fr_ep1_movie26 with dissolve
        if dtype > 0:
#            mc "Yeah..."
            mc "Tak"
            scene fr_ep1_movie27 with dissolve
#            my "Let's focus on the movie instead..."
            my "Skupmy się na filmie..."
        else:
#            mc "But don't worry...I'll be respectful."
            mc "Ale nie martw się...będę okazywać szacunek."
            scene fr_ep1_movie27 with dissolve
#            my "Thank you, [name]..."
            my "Dziękujemy,"
#    "Ok. I'll try.":
    "Spróbuję.":
#        $ bios_history_maya += "I had a movie night with Maya.\n\n"
        $ bios_history_maya += "Miałem noc filmową z Mayą.\n \n"
        $ bios_name_maya = True
        $ chat_new_bios = True
        $ ep1_maya_attracted = False
#        mc "Ok, I'll try."
        mc "Ok, spróbuję."
scene fr_ep1_movie36b with Fade(1.5,1,0.5)
#my "Tell me! Did you like the movie?"
my "Powiedz mi! Podobał ci się film?"
scene fr_ep1_movie37 with dissolve
menu:
#    "I liked it":
    "I liked it.":
        if dtype > 0:
#            mc "Yeah. It was scary, but I liked it."
            mc "Tak. To było straszne, ale podobało mi się."
            scene fr_ep1_movie36b with dissolve
#            my "Right!?"
            my "Prawo"
        else:
            $ RPmaya += 1
#            mc "It was scary, but watching it with you made it fun."
            mc "To było straszne, ale oglądanie tego z tobą sprawiało, że było zabawnie."
            scene fr_ep1_movie36b with dissolve
#            my "Yeah, this was really nice."
            my "Tak, to było naprawdę miłe."
#    "It wasn't for me":
    "nie dla mnie.":
#        mc "No...that movie wasn't for me at all."
        mc "Nie...ten film w ogóle nie był dla mnie."
#        mc "It was way too scary!"
        mc "To było zbyt straszne!"
        scene fr_ep1_movie36b with dissolve
#        my "Haha, you're cute."
        my "Haha, jesteś słodki."
#my "Maybe next time we can watch something more lighthearted?"
my "Może następnym razem obejrzymy coś bardziej beztroskiego?"
scene fr_ep1_movie37 with dissolve
#mc "I'd love that."
mc "Z przyjemnością! "
scene fr_ep1_movie40 with dissolve
#my "Now, unless you wanna sleep in my bed, get out."
my "Teraz, jeśli nie chcesz spać w moim łóżku, wynoś się."
scene fr_ep1_movie37 with dissolve
menu:
#    "Thanks for the movie":
    "Dzięki za film":
        stop music fadeout 3
#        mc "Thanks for the movie, Maya."
        mc "Dzięki za film, Maya."
#    "Was that an offer?":
    "Czy to była oferta?":
#        mc "Was that an offer?"
        mc "Czy to była oferta?"
        scene fr_ep1_movie36b with dissolve
        stop music fadeout 3
#        my "Haha, no, it was a joke, stupid."
        my "Haha, nie, to był żart, głupku."
$ guideSuggestedPage = 48
scene ep1_gender with Fade(1.5,1,0.5)
play music "music/ep1/dont_count_on_me.mp3"
#mc "(Gender Studies 101...this will be interesting...)"
mc "(Gender Studies 101...to będzie ciekawe...)"
#mc "(Wow, there's a lot of girls in this class...)"
mc "(Wow, w tej klasie jest dużo dziewczyn...)"
#mc "(Derek's going to regret that he didn't sign up for-)"
mc "(Derek pożałuje, że się nie zapisał…)"
scene ep1_gender1
if assman:
#    de "ASS MAN! OVER HERE!"
    de "DUPKU! TUTAJ!"
else:
#    de "BRO! OVER HERE!"
    de "BRACIE! TUTAJ!"
#mc "(...oh.)"
mc "Och..."
scene ep1_gender2 with dissolve
#de "I'm loving this class, bro!"
de "Uwielbiam te zajęcia, brachu!"
#de "Look at all the girls!"
de "Spójrz na te wszystkie dziewczyny!"
#de "Sure, some look like peacocks that escaped from the zoo-"
de "Jasne, niektóre wyglądają jak pawie, które uciekły z zoo."
play sound "sound_effects/table_slam.mp3"
scene ep1_gender2b with vpunch
#fem "Oh my God! You did not just say that!!!"
fem "O mój Boże! Nie powiedziałeś tego!!!"
scene ep1_gender3 with dissolve
#de "But there are several who actually are packing some serious front and back load."
de "Ale jest kilka osób, które faktycznie mają poważny ładunek przedni i tylny."
scene ep1_gender3b with dissolve
#de "NO WAY! That's our teacher!"
de "Nie ma MOWY! To nasz nauczyciel!"
scene ep1_gender4 with dissolve
#de "Mrs. Milk machine!"
de "Pani Mleczarka!"
if preferredmilf == 0:
#    de "She's the one you found hotter than Cathy, right!?"
    de "To ją uważałeś za seksowniejszą od Cathy, prawda?"
scene ep1_gender4b with dissolve
#mc "*{i}Whispers{/i}*Dude, chill! She can hear you."
mc "*{i}Szepcze{/i}*Koleś, wyluzuj! Ona cię słyszy."
#de "Seriously! Look at her!"
de "Serio! Spójrz na nią!"
#ja "(Hm...well, this is a first.)"
ja "(Hmm...cóż, to pierwszy raz.)"
#ja "(It should be interesting having boys in this class...)"
ja "(Powinno być ciekawie mieć chłopców w tej klasie...)"
scene ep1_gender5 with dissolve
#ja "(If they are here for the right reasons that is...)"
ja "(Jeśli są tu z właściwych powodów...)"
scene ep1_gender6 with dissolve
#ja "(Hmph...bummer.)"
ja "(Hmph...pech.)"
scene ep1_gender8 with dissolve
#ja "(*{i}Sigh{/i}* I should've doubled up on espresso for this...)"
ja "(*{i}Westchnienie{/i}* Powinienem był podwoić espresso...)"
#ja "(Every year, it's the same group of girls...)"
ja "(Co roku jest to ta sama grupa dziewcząt...)"
scene ep1_gender9 with dissolve
#ja "(I wonder why feminism always attracts the most hardcore women.)"
ja "(Zastanawiam się, dlaczego feminizm zawsze przyciąga najbardziej hardcorowe kobiety.)"
#ja "(There are rarely any girls here who understand what it's really about.)"
ja "(Rzadko są tu dziewczyny, które rozumieją, o co naprawdę chodzi.)"
scene ep1_gender10
#my "Derek!? No...don't tell me you signed up."
my "Derek!? Nie...nie mów mi, że się zapisałeś."
#de "You weren't lying about the vaginas, Maya!"
de "Nie kłamałaś o waginach, Maya!"
scene ep1_gender12 with dissolve
#my "Give me strength..."
my "Daj mi siłę..."
#mc "Hey, Maya."
mc "Hej, Maya."
scene ep1_gender13 with dissolve
#my "Hey, [name]."
my "Hej. "
scene ep1_gender14 with dissolve
#ja "Ok, my clock is on the dot. Let us begin."
ja "Ok, mój zegar jest na bieżąco. Zaczynajmy."
#ja "Welcome to Gender Studies 101. I'm Dr. Jade-"
ja "Witamy na kursie Gender Studies 101. Jestem dr Jade-"
#de "Females can be doctors?"
de "Czy kobiety mogą być lekarzami?"
#fem "Hey, shut up!"
fem "Hey ty, zamknij się!"
scene ep1_gender16 with dissolve
#ja "During this course, we will learn about gender equality, feminism, sexism..."
ja "Podczas tego kursu dowiemy się o równości płci, feminizmie, seksizmie..."
#ja "...and the difference between sex and gender."
ja "...a różnica między płcią a płcią."
scene ep1_gender17
#de "Maya, you didn't tell me there will be sex talk, too!"
de "Maya, nie mówiłaś mi, że będą też rozmowy o seksie!"
#fem "Shh!"
fem "Cicho!"
scene ep1_gender18 with dissolve
#ja "You two."
ja "Wy dwoje! "
#ja "I'm happy to see two male students in my class."
ja "Cieszę się, że widzę dwóch uczniów płci męskiej w mojej klasie."
#ja "That's a first-time occurrence."
ja "To pierwsze takie zdarzenie."
scene ep1_gender20 with dissolve
#de "You're welcome!"
de "Nie ma za co! "
#fem "Ugh..."
fem "Umm..."
scene ep1_gender18 with dissolve
#ja "I'm going to have to ask you to put on at least a t-shirt next time, though."
ja "Następnym razem będę jednak musiał poprosić Cię o założenie co najmniej koszulki."
#de "...fine."
de "Dobrze."
#ja "But, I'm curious, why did you sign up for this class?"
ja "Ale ciekawi mnie, dlaczego zapisałeś się na te zajęcia?"
#ja "What was it that piqued your interests?"
ja "Co wzbudziło twoje zainteresowanie?"
scene ep1_gender20 with dissolve
#de "Easy credits and vagin-"
de "Łatwe kredyty i pochwy"
scene ep1_gender22
#my "No!"
my "Nie!"
scene ep1_gender23 with dissolve
#ja "How about you?"
ja "A ty? "
scene ep1_gender24 with dissolve
menu:
    "Easy credits and vaginas ({color=#ffffff}Huge {size=-1}{font=collegiate.ttf}DIK{/font}{/size}{/color})" if dtype > 1:
        $ dk(1)
#        mc "Easy credits and vaginas."
        mc "Łatwe kredyty i pochwy."
        $ RPmaya -= 1
        $ RPderek += 1
        scene ep1_gender17 with dissolve
#        de "That's what I was going to say!"
        de "To właśnie chciałem powiedzieć!"
        scene ep1_gender24b with dissolve
#        ja "Hmph."
        ja "Hm."
#    "Learn more about women":
    "Dowiedz się więcej o kobietach":
        $ dk(-1)
        $ RPmaya += 1
        if dtype > 0:
#            mc "You know...to learn more about women and their issues."
            mc "Wiesz...żeby dowiedzieć się więcej o kobietach i ich problemach."
            scene ep1_gender23 with dissolve
#            ja "Welcome to the class...?"
            ja "Witamy na zajęciach plastycznych. "
            scene ep1_gender24 with dissolve
#            mc "[name]."
            mc "[name]."
        else:
#            mc "I would like to learn more about women's struggles in real life and the real meaning of feminism."
            mc "Chciałbym dowiedzieć się więcej o zmaganiach kobiet w prawdziwym życiu i prawdziwym znaczeniu feminizmu."
            scene ep1_gender24c with dissolve
#            ja "(What the...?)"
            ja "Co jest…?! "
#            ja "The real meaning of feminism? A very interesting point!"
            ja "Prawdziwe znaczenie feminizmu? Bardzo ciekawa uwaga!"
            scene ep1_gender23 with dissolve
#            ja "Welcome to the class...?"
            ja "Witamy na zajęciach plastycznych. "
            scene ep1_gender24 with dissolve
#            mc "[name]."
            mc "[name]."
            scene ep1_gender23 with dissolve
            $ ep1_jade_pleased = True
#            ja "Welcome, [name]."
            ja "Witamy,"
#    "Nothing special":
    "Nic specjalnego":
#        mc "Nothing special, really."
        mc "Nic specjalnego, naprawdę."
        scene ep1_gender23 with dissolve
#        ja "Well, hopefully, you'll be more motivated soon."
        ja "Cóż, miejmy nadzieję, że wkrótce będziesz bardziej zmotywowany."
scene ep1_gender14 with dissolve
#ja "These classes will consist of a lot of topical discussions, and participation in the discussions is mandatory."
ja "Zajęcia te będą składać się z wielu dyskusji tematycznych, a udział w nich jest obowiązkowy."
#ja "I would like you all to find someone you don't know in here and get to know each other better."
ja "Chciałbym, żebyście wszyscy znaleźli tu kogoś, kogo nie znacie i lepiej się poznali."
if not minigames:
    jump ep1_after_gender_test1
scene ep1_gender30 with dissolve
stop music fadeout 3
#stu "Hey, do you wanna pair up?"
stu "Hej, chcesz się sparować?"
#mc "Sure..."
mc "Jasne…"
jump gender101_test1
label ep1_after_gender_test1:

if minigames:
    scene ep1_gender31 with wiperight
    play music "music/ep1/dont_count_on_me.mp3"
else:
    scene ep1_gender31 with Fade(1.5, 1, 0.5)
#fem "Why are you even here!? You're like the worst person I've ever met!"
fem "Po co w ogóle tu jesteś!? Jesteś najgorszą osobą, jaką kiedykolwiek spotkałem!"
scene ep1_gender32 with dissolve
#de "Not a PERSON! It's called a MAN, Wendy!"
de "To się nazywa MĘŻCZYZNA, Wendy!"
#de "Men have penises; women have vaginas."
de "Mężczyźni mają penisy; kobiety mają pochwy."
#de "What the fuck does X-gender even mean!?"
de "Co do kurwy nędzy oznacza X-gender!?"
#de "What do its genitals look like!?"
de "Jak wyglądają jego genitalia!?"
scene ep1_gender34 with dissolve
#fem "I HATE YOU!"
fem "NIENAWIDZĘ CIĘ."
scene ep1_gender35 with dissolve
#de "Women...am I right?"
de "Kobiety...mam rację?"
$ bios_jade = True
#$ bios_history_jade += "Dr. Jade teaches Gender Studies 101.\n\n"
$ bios_history_jade += "Dr Jade uczy podstaw gender studies.\n \n"
$ bios_name_jade = True
#$ bios_history_derek += "Even though Derek and Maya are twins, they are very unalike. The Gender Studies class proved that.\n\n"
$ bios_history_derek += "Mimo że Derek i Maya są bliźniakami, są bardzo niepodobni. Udowodniła to klasa Gender Studies.\n \n"
$ bios_name_derek = True
$ bios_dany = True
$ bios_name_dany = True
$ bios_wendy = True
$ bios_name_wendy = True
$ bios_minny = True
$ bios_name_minny = True
$ chat_new_bios = True
scene ep1_gender36
#my "I don't know about you, but I just can't sit with him in that class."
my "Nie wiem jak ty, ale ja po prostu nie mogę siedzieć z nim w tej klasie."
#my "I know I said it's easy credits, but I also want to learn something from it."
my "Wiem, że powiedziałem, że to łatwe, ale też chcę się czegoś z tego nauczyć."
scene ep1_gender37 with dissolve
if dtype > 0:
#    mc "I know, but I gotta admit that he's pretty fun to be around."
    mc "Wiem, ale muszę przyznać, że fajnie się z nim przebywa."
else:
    $ RPmaya += 1
#    mc "I don't blame you."
    mc "Nie winię ciebie."
scene ep1_gender38 with dissolve
#my "Ok...I'll see you later. Don't wait up; I'll probably be very late tonight."
my "Dobra... to do zobaczenia. Nie czekaj na mnie, pewnie się dziś spóźnię."
scene ep1_gender39 with dissolve
#mc "Where are you going?"
mc "Dokąd się wybierasz?"
scene ep1_gender38 with dissolve
#my "Home to shower and change..."
my "Dom do kąpieli i przebierania się..."
#my "Then...you know...pledge stuff..."
my "W takim razie... no wiesz...zaprzysiężenie..."
scene ep1_gender39 with dissolve
#mc "Oh, so Quinn got back to you?"
mc "Och, więc Quinn odezwał się do ciebie?"
scene ep1_gender38 with dissolve
#my "Yeah..."
my "Tak"
scene ep1_gender39 with dissolve
#mc "I get it... Well, good luck."
mc "Rozumiem... No to powodzenia."
stop music fadeout 3
$ guideSuggestedPage = 49
jump ep1_freeroam_maya_dorm_label
label ep1_ending_scene:

stop music fadeout 3
scene ep1_end0 with fade
#mc "(This is weird...)"
mc "„To dziwne. "
#mc "(Why hasn't she come back home yet? It's getting very late.)"
mc "(Dlaczego jeszcze nie wróciła do domu? Robi się bardzo późno.)"
scene ep1_end1 with dissolve
play sound "sound_effects/dial_tone.mp3"
#mc "(Hm...)"
mc "Hm..."
#mc "(Nope. No answer...)"
mc "(Nie. Brak odpowiedzi...)"
scene ep1_end2 with dissolve
#mc "(Nothing else I can do.)"
mc "(Nic więcej nie mogę zrobić.)"
#mc "(She told me not to wait up...)"
mc "(Powiedziała mi, żebym nie czekała...)"
#mc "(...)"
mc "(...)"
#mc "(Bedtime it is.)"
mc "(Czas spać.)"
scene ep1_ending0 with fade
play sound "sound_effects/door_lock.mp3"
$ renpy.pause(0.5)
$ renpy.sound.play("sound_effects/door_close.mp3", channel="sfx2", loop=False)
$ renpy.pause()
scene ep1_ending0b with dissolve
#my "(Yup...he's asleep...)"
my "(Yup...śpi...)"
label ep1_maya_lewd:

if _in_replay:
    hide screen phone_screen
    if persistent.name == None:
        $ name = "MC"
    else:
        $ name = persistent.name
    if persistent.mc_maya == None:
        $ mc_maya = name
    else:
        $ mc_maya = persistent.mc_maya
    if persistent.maya == None:
        $ maya = "Maya"
    else:
        $ maya = persistent.maya
scene ep1_ending0 with dissolve
play sound "sound_effects/clothes.mp3"
$ renpy.pause()
play music "music/ep1/windswept.mp3"
scene ep1_ending1 with dissolve
$ renpy.pause()
scene ep1_ending2 with dissolve
#my "(You can do this, Maya...)"
my "(Możesz to zrobić, Maya...)"
scene ep1_ending3 with dissolve
$ renpy.pause()
scene ep1_ending4 with dissolve
#my "(Wait...)"
my "Moment..."
#my "(...why is it hard?)"
my "(...dlaczego jest to trudne?)"
scene ep1_ending5 with dissolve
#my "(Holy fuck! It's huge!)"
my "(O kurwa! Jest ogromny!)"
#my "*{i}Gulp{/i}*"
my "Połykanie"
scene ep1_ending6 with dissolve
#my "(Ok... Careful now...)"
my "(Ok... uważaj teraz...)"
#my "(This feels so wrong...)"
my "(To jest takie złe...)"
scene ep1_ending7 with dissolve
#my "(Am I really doing this?)"
my "Nie wierzę, że to robię."
scene ep1_ending6b with dissolve
$ renpy.pause()
scene ep1_ending7 with dissolve
#my "(This feels...weird...)"
my "(Czuję się...dziwnie...)"
#my "(But his skin is so warm...)"
my "(Ale jego skóra jest taka ciepła...)"
#my "(That's kind of nice...)"
my "(To miłe...)"
scene ep1_ending8 with dissolve
#my "(Who are you kidding, Maya? All you're feeling right now is that hard thing poking you...)"
my "(Kogo chcesz oszukać, Maya? Wszystko, co teraz czujesz, to ta twarda rzecz, która cię szturcha...)"
#my "(It's kind of like my dildo...I guess...but...)"
my "(To trochę jak moje dildo... tak myślę...ale...)"
#my "(Huh! Is he waking up? No turning back now.)"
my "(Hm! Czy on się budzi? Teraz już nie ma odwrotu.)"
scene ep1_ending10 with dissolve
#mc "Huh, [maya]? What are you-"
mc "Hm, [maya]? Co ty..."
scene ep1_ending11 with dissolve
#my "Shh!"
my "Cicho!"
#my "*{i}Whispers{/i}* Don't say a word."
my "*{i}Szepty{/i}* Nie mów ani słowa."
scene ep1_ending13 with dissolve
#mc "(Is this another dream, or is she really lying on top of me...)"
mc "(Czy to kolejny sen, czy ona naprawdę leży na mnie...)"
#mc "(Shit...she's pressing herself against my dick...)"
mc "(Cholera...przyciska się do mojego penisa...)"
scene ep1_ending14 with dissolve
#mc "(Oh my God! That's her nipple...)"
mc "(O mój Boże! To jej sutek...)"
#mc "(Damn, my mouth is all dry...)"
mc "(Cholera, moje usta są całe suche...)"
#mc "(I guess I can put my hand here...)"
mc "(Chyba mogę tu położyć rękę...)"
scene ep1_ending15 with dissolve
#mc "(Her ass is both firm and soft at the same time.)"
mc "(Jej tyłek jest jednocześnie jędrny i miękki.)"
#my "(Is he pushing me harder down...)"
my "(Czy popycha mnie mocniej...)"
#my "(Damn...I'm getting that tingling feeling...)"
my "(Cholera...mam to uczucie mrowienia...)"
#my "*{i}Softly moans{/i}*"
my "*{i}Cicho jęczy{/i}*"
init 500 image anim_maya_grind2_ep1 = Movie(channel="anim_maya_grind2_ep1", play="images/movies/ep1/anim_maya_grind2_ep1.webm")
scene anim_maya_grind2_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#my "(Ok, let's begin...)"
my "(Dobrze, zaczynajmy...)"
#my "Hngh..."
my "Hngh...!"
#my "(Am I doing it too hard?)"
my "(Czy robię to zbyt mocno?)"
#mc "Mmm..."
mc "Mmm..."
#my "(No...he seems to like it...)"
my "(Nie... wydaje się, że mu się podoba...)"
pause
init 500 image anim_maya_grind_ep1 = Movie(channel="anim_maya_grind_ep1", play="images/movies/ep1/anim_maya_grind_ep1.webm")
scene anim_maya_grind_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#my "(It feels...kind of nice...)"
my "(To miłe uczucie...)"
#my "(No, it doesn't! Stop it...)"
my "(Nie, nie ma! Przestań...)"
#my "(It's wrong...)"
my "To jest niewłaściwe. "
pause
scene ep1_ending13 with dissolve
#my "*{i}Breathes heavily{/i}*"
my "*{i}Ciężki oddech{/i}*"
#my "(Shit...I'm starting to get hot...)"
my "(Cholera... Robi mi się gorąco...)"
#my "(I can feel his warm breath against my face...)"
my "(Czuję jego ciepły oddech na mojej twarzy...)"
scene ep1_ending16 with dissolve
#my "(No...)"
my "Nr"
#my "(This is better...I think...)"
my "(Tak jest lepiej...myślę...)"
init 500 image anim_maya_grind3_ep1 = Movie(channel="anim_maya_grind3_ep1", play="images/movies/ep1/anim_maya_grind3_ep1.webm")
scene anim_maya_grind3_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#mc "(Oh fuck...her body's fucking amazing...)"
mc "(O kurwa...jej ciało jest zajebiste...)"
#mc "(Look at those hips moving...)"
mc "(Spójrz na te poruszające się biodra...)"
pause
init 500 image anim_maya_grind_closer_ep1 = Movie(channel="anim_maya_grind_closer_ep1", play="images/movies/ep1/anim_maya_grind_closer_ep1.webm")
scene anim_maya_grind_closer_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#my "*{i}Softly moans{/i}* Oh...[mc_maya]..."
my "*{i}Cicho jęczy{/i}* Och...[mc_maya]..."
#mc "[maya]..."
mc "[maya]..."
#my "(Oh no...)"
my "Och, nie..."
init 500 image anim_maya_grind3b_ep1 = Movie(channel="anim_maya_grind3b_ep1", play="images/movies/ep1/anim_maya_grind3b_ep1.webm")
scene anim_maya_grind3b_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#my "(I'm...enjoying this?)"
my "(Podoba misię to?)"
#my "(No! Stop thinking about it.)"
my "(Nie! Przestań o tym myśleć.)"
#my "(Focus! It's almost over now...)"
my "(Skup się! Już prawie koniec...)"
pause
init 500 image anim_maya_grind_long_ep1 = Movie(channel="anim_maya_grind_long_ep1", play="images/movies/ep1/anim_maya_grind_long_ep1.webm")
scene anim_maya_grind_long_ep1 with dissolve:
    size (config.screen_width, config.screen_height)
#my "*{i}Moans{/i}*"
my "*{i}Jęki{/i}*"
#my "(I'm so fucking hot right now...)"
my "(Jestem teraz tak cholernie gorąca...)"
#mc "(Damn, she has the angle just right...)"
mc "(Cholera, ona ma odpowiedni kąt...)"
#mc "(Her warm pussy is grinding so tightly against the head of my dick...)"
mc "(Jej ciepła cipka tak mocno ociera się o głowę mojego penisa...)"
#my "(Fuck, I'm so wet....this wasn't supposed to happen.)"
my "(Kurwa, jestem taka mokra....to nie miało się wydarzyć.)"
pause
if _in_replay:
    menu:
        "Massage her clit" if persistent.ep1_maya_dik:
            init 500 image anim_maya_clit_ep1 = Movie(channel="anim_maya_clit_ep1", play="images/movies/ep1/anim_maya_clit_ep1.webm")
            scene anim_maya_clit_ep1 with dissolve:
                size (config.screen_width, config.screen_height)
#            my "*{i}Moans loudly{/i}*"
            my "*{i}Głośne jęki{/i}*"
#            my "(OH FUCK!)"
            my "O kurwa! "
#            my "(What's he doing!? This...this...)"
            my "(Co on robi!? To...to...)"
#            my "*{i}Moans loudly{/i}* Oh, [mc_maya]!"
            my "*{i}Głośne jęki{/i}* Och, [mc_maya]!"
            pause
        "Kiss her" if persistent.ep1_maya_chick:
            init 500 image anim_maya_kiss_ep1 = Movie(channel="anim_maya_kiss_ep1", play="images/movies/ep1/anim_maya_kiss_ep1.webm")
            scene anim_maya_kiss_ep1 with dissolve:
                size (config.screen_width, config.screen_height)
#            my "(Shit! He's kissing me...)"
            my "(Cholera! Całuje mnie...)"
#            my "(God...his lips are so soft...)"
            my "(Boże...jego usta są takie miękkie...)"
#            my "(Just...a little bit longer...)"
            my "(Tylko... jeszcze trochę...)"
            pause
else:
    if dtype > 0:
        $ ep1_kissed_maya = False
        init 500 image anim_maya_clit_ep1 = Movie(channel="anim_maya_clit_ep1", play="images/movies/ep1/anim_maya_clit_ep1.webm")
        scene anim_maya_clit_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        my "*{i}Moans loudly{/i}*"
        my "*{i}Głośne jęki{/i}*"
#        my "(OH FUCK!)"
        my "O kurwa! "
#        my "(What's he doing!? This...this...)"
        my "(Co on robi!? To...to...)"
#        my "*{i}Moans loudly{/i}* Oh, [mc_maya]!"
        my "*{i}Głośne jęki{/i}* Och, [mc_maya]!"
        pause
    else:
        $ ep1_kissed_maya = True
        init 500 image anim_maya_kiss_ep1 = Movie(channel="anim_maya_kiss_ep1", play="images/movies/ep1/anim_maya_kiss_ep1.webm")
        scene anim_maya_kiss_ep1 with dissolve:
            size (config.screen_width, config.screen_height)
#        my "(Shit! He's kissing me...)"
        my "(Cholera! Całuje mnie...)"
#        my "(God...his lips are so soft...)"
        my "(Boże...jego usta są takie miękkie...)"
#        my "(Maybe if I close my eyes and pretend that he's- NO!)"
        my "(Może jak zamknę oczy i będę udawał, że jest... nie!)"
#        my "(Just...a little bit longer...)"
        my "(Tylko... jeszcze trochę...)"
scene ep1_ending_shock with dissolve
if _in_replay:
#    mc "[maya]... Take your panties off..."
    mc "[maya]... Zdejmij majtki..."
    $ renpy.end_replay()
elif dtype > 0:
#    mc "[maya]... Take your panties off..."
    mc "[maya]... Zdejmij majtki..."
    $ persistent.ep1_maya_dik = True
    $ ep1_dik_end = True
else:
#    mc "[maya]... What are we doing?"
    mc "Czym się zajmujemy?"
    $ ep1_dik_end = False
    $ persistent.ep1_maya_chick = True
if persistent.ep1_maya_dik and persistent.ep1_maya_chick:
    $ persistent.ep1_maya_full = True
$ calcScenes()
hide screen phone_screen
stop music
play sound "sound_effects/zap.mp3"
scene ep1_ending_shock1 with hpunch
$ renpy.pause(0.5)
scene black
$ renpy.pause(2)
$ updateDikScore()
if steamAchievements and persistent.vault1 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER1")
    init $ achievement.register("VAULTLOOTER1")
    $ achievement.Sync()
if steamAchievements and persistent.vault1 and persistent.vault2 and persistent.vault3 and persistent.vault4 and not config.console and not config.developer:
    $ achievement.grant("VAULTLOOTER")
    init $ achievement.register("VAULTLOOTER")
    $ achievement.Sync()
if steamAchievements and preferredmilf == 0 and not config.console and not config.developer:
    $ achievement.grant("MILKMACHINE")
    init $ achievement.register("MILKMACHINE")
    $ achievement.Sync()
if steamAchievements and preferredmilf == 1 and not config.console and not config.developer:
    $ achievement.grant("FLATANDBORING")
    init $ achievement.register("FLATANDBORING")
    $ achievement.Sync()
if steamAchievements and not config.console and not config.developer:
    $ achievement.grant("EPISODE1")
    init $ achievement.register("EPISODE1")
    $ achievement.Sync()
if persistent.current_episode == 1:
    scene ep1_episode_end
    play music "music/patched/track_previous.mp3"
    $ renpy.pause()
else:
    scene ep1_episode_endb
    $ renpy.pause()
scene black with fade
play music "music/ep1/unknown_power.mp3"
show screen scoremsg
$ calcRenders()
$ renpy.pause(2)
hide screen scoremsg
$ episodeIsEnding = True
show screen endingScreen
show screen majorChoiceScale
$ renpy.pause()
$ episodeIsEnding = False
hide screen endingScreen
hide screen majorChoiceScale
if RPjosy >= 0:
    $ josyScore = RPjosy / 10.0
else:
    $ josyScore = RPjosy / 1.0
if RPmaya >= 0:
    $ mayaScore = RPmaya / 15.0
else:
    $ mayaScore = RPmaya / 3.0
if RPsage >=0:
    $ sageScore = RPsage / 6.0
else:
    $ sageScore = RPsage / 2.0
if RPisabella >= 0:
    $ isabellaScore = RPisabella / 1.0
else:
    $ isabellaScore = RPisabella / 2.0
if RPjill >= 0:
    $ jillScore = RPjill / 2.0
else:
    $ jillScore = RPjill / 2.0
$ episodeContLabel = "ep1EndLabel"
jump ep1_report_jill_label
$ renpy.pause()
label ep1EndLabel:

stop music fadeout 3
$ renpy.pause(2)
$ persistent.tutorials = True
scene black with dissolve
if not persistent.pet_app_unlocked:
    $ persistent.pet_app_unlocked = True
    show phone_app_pet_new:
        xalign 0.5
        yalign 0.4
#    show text "Congratulations! You just unlocked the Pet names app on your phone.\nThis app lets you give the girls pet names and have them call you pet names, too."
    show text "Gratulacje! Właśnie odblokowałeś aplikację do nadawania imion zwierzakom na swoim telefonie.\nTa aplikacja umożliwia nadawanie dziewczynom imion zwierzakom i przezywanie ich."
    $ renpy.pause()
#    show text "This feature will remain unlocked if you decide to restart the game."
    show text "Ta funkcja pozostanie odblokowana, jeśli zdecydujesz się ponownie uruchomić grę."
    $ renpy.pause()
#$ bios_history_maya += "Unbelievable! Maya woke me up in the middle of the night and started grinding on my cock. Why did she do that?\n\n"
$ bios_history_maya += "Niewiarygodne! Majka obudziła mnie w środku nocy i zaczęła ocierać się o mojego kutasa. Dlaczego to zrobiła?\n \n"
$ bios_name_maya = True
$ chat_new_bios = True
$ guideSuggestedPage = 51
if renpy.loadable("update2.rpyc"):
    jump startUpdate2
else:
    jump endOfVersion
label endOfVersion:

scene black
show spr_bg
show spr_mid
show spr_top
show massive_diks
$ renpy.pause()
hide massive_diks
show acknowledgements
$ renpy.pause()
hide acknowledgements
show music_credits
$ renpy.pause()
hide music_credits
show version_end
$ renpy.pause()
hide version_end
scene episode2_polls
$ renpy.pause()
scene patreon_promo
$ renpy.pause()
return
return