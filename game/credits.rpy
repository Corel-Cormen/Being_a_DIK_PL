screen cred_thanks:
    tag cred_thanks
    add "black"
    if steamConfig or nonPatreonConfig:
        text "Ta gra powstała wyłącznie dzięki hojnym darowiznom\ni wsparciu tysięcy Patronów\n\nOgromne podziękowania dla wszystkich moich Patronów,\nprzeszłych, obecnych i przyszłych. Dziękuje za zaufanie.\n\nDziękuje za udział w grze!\nCzekajcie na kolejny sezon.\nDołączcie do mojego serwera Discord,\,aby uzyskać więcej informacji." text_align 0.5 font "candara.ttf" size 40 yalign 0.5 xalign 0.5
    else:
        text "Ta gra powstała wyłącznie dzięki hojnym darowiznom\ni wsparciu tysięcy Patronów\n\nOgromne podziękowania dla wszystkich moich Patronów,\nprzeszłych, obecnych i przyszłych. Dziękuje za zaufanie.\n\nDziękuje za udział w grze!\nCzekajcie na kolejny sezon.\nDołączcie do mojego serwera Discord,\,aby uzyskać więcej informacji.\nWesprzyj rozwój gry na {color=#e51475}patreon.com/DrPinkCake{/color}" text_align 0.5 font "candara.ttf" size 40 yalign 0.5 xalign 0.5
    imagebutton idle "pinkcake_logo_btn" xalign 0.98 yalign 0.95 action NullAction()
screen skipCreditsScreen:
    tag skipCreditsScreen
    imagebutton idle "credits_invis_button" hover "credits_invis_button" action Jump("skipped_credits_label") xpos 0 ypos 0
label game_credits:
    play music "music/ep6/licensed_music/track28.mp3" noloop
    queue music "music/ep8/licensed_music/track79.mp3"
    $ qM = quick_menu
    $ quick_menu = 0
    $ credits_speed = 60
    $ credits_speed2 = 73
    $ credits_speed3 = 173
    $ credits_speed_bg = credits_speed3/10
    $ credits_isPlaying = True
    scene black
    show credits_long_intro with dissolve
    $ renpy.pause(1.5)
    hide credits_long_intro with dissolve
    show screen skipCreditsScreen
    show cred
    show cred2
    show cred3
    show cred4
    show cred_ext3
    show cred_ext4
    show cred_ext5
    show cred_isabella_bg with dissolve
    $ renpy.pause(credits_speed_bg)
    hide cred_isabella_bg with dissolve
    show cred_riona_bg with dissolve
    $ renpy.pause(credits_speed_bg)
    hide cred_riona_bg with dissolve
    show cred_josy_bg with dissolve
    $ renpy.pause(credits_speed_bg-1)
    hide cred_josy_bg with dissolve
    show cred_jade_bg with dissolve
    $ renpy.pause(credits_speed_bg-1)
    hide cred_jade_bg with dissolve
    show cred_cathy_bg with dissolve
    $ renpy.pause(credits_speed_bg-1)
    hide cred_cathy_bg with dissolve
    show cred_camila_bg with dissolve
    $ renpy.pause(credits_speed_bg-2)
    hide cred_camila_bg with dissolve
    show cred_maya_bg with dissolve
    $ renpy.pause(credits_speed_bg-1)
    hide cred_maya_bg with dissolve
    show cred_sage_bg with dissolve
    $ renpy.pause(credits_speed_bg-1)
    hide cred_sage_bg with dissolve
    show cred_quinn_bg with dissolve
    $ renpy.pause(credits_speed_bg)
    hide cred_quinn_bg with dissolve
    show cred_jill_bg with dissolve
    $ renpy.pause(credits_speed_bg)
    hide cred_jill_bg with dissolve
    hide cred
    hide cred2
    hide cred3
    hide cred4
    hide cred_ext3
    hide cred_ext4
    hide cred_ext5
    label skipped_credits_label:
    $ credits_isPlaying = False
    hide screen skipCreditsScreen
    hide credits_long_intro
    hide cred
    hide cred2
    hide cred3
    hide cred4
    hide cred_ext3
    hide cred_ext4
    hide cred_ext5
    hide cred_isabella_bg
    hide cred_riona_bg
    hide cred_josy_bg
    hide cred_jade_bg
    hide cred_cathy_bg
    hide cred_maya_bg
    hide cred_camila_bg
    hide cred_sage_bg
    hide cred_quinn_bg
    hide cred_jill_bg
    show screen cred_thanks with dissolve
    $ renpy.pause()
    hide screen cred_thanks with dissolve
    stop music fadeout 10
    if not steamConfig and not nonPatreonConfig:
        show version_end
        $ renpy.pause()
        hide version_end
    scene twitter_promo
    $ renpy.pause()
    if not steamConfig:
        if not nonPatreonConfig:
            scene patreon_promo
            $ renpy.pause()
        if renpy.loadable("season2/scripts/update8.rpyc"):
            scene interlude_teaser with dissolve
            $ renpy.pause()
    else:
        if renpy.loadable("season2/scripts/update8.rpyc"):
            scene interlude_teaser with dissolve
            $ renpy.pause()
        $ game_is_ending = True
        show screen dlc
        pause
        $ game_is_ending = False
    $ quick_menu = qM
    return
init:
    python:
        credits = ("Stworzone przez", "Dr PinkCake"), ("Korekta językowa", "Ignatz"), ("Testerzy wersji beta", "DparX\nZangs"), ("Zespół Discord", "N7\nDawe\nTommybuns\nDasati\ndAAAMN313\nDorian Rast"), ("Tłumaczenie PL", "PopCornel"), ("Grafika 2D autorstwa Jacoba wykonana na zlecenie","FlowerXL"),("Modele Arieth/Ellie dzięki uprzejmości","Dawe3DArts"),\
        ("","{size=40}{color=#fe9416}Muzyka {/color}{color=#ffffff}(licencja Creative Commons w celach komercyjnych){/color}{/size}"),\
        ("","Slow day blues - A to Z guitars"),\
        ("","03 Three’s a crowd- Absentrealities"),\
        ("","04 Surf punk rock - Absentrealities"),\
        ("","Adventure - Alexander Nakarada"),\
        ("","Blood And Steel - Alexander Nakarada"),\
        ("","[[Classical] Freedom - Alexander Nakarada"),\
        ("","[[Rock n Roll] Jack the Lumberer - Alexander Nakarada"),\
        ("","[[Acoustic] Journey Of Hope - Alexander Nakarada"),\
        ("","Medieval Loop One - Alexander Nakarada"),\
        ("","Medieval Loop Two - Alexander Nakarada"),\
        ("","Medieval Loop Three - Alexander Nakarada"),\
        ("","[[Melodic Piano] Reaching the sky - Alexander Nakarada"),\
        ("","[[Acoustic] Relaxing Ballad - Alexander Nakarada"),\
        ("","[[Acoustic Ballad] Rustic Ballad - Alexander Nakarada"),\
        ("","[[Acoustic & Ballad] Simple Ballad - Alexander Nakarada"),\
        ("","Uplifting Ballad - Alexander Nakarada"),\
        ("","Skeleton Keys - Alexander Nakarada"),\
        ("","[[Piano] Spring in Russia - Alexander Nakarada"),\
        ("","The crown - Alexander Nakarada"),\
        ("","[[Piano Improvisation] Winter - Alexander Nakarada"),\
        ("","STRYV Surge (Ivory Remix) - Arlindo Detomi"),\
        ("","Driving Rock - AShamaluevMusic"),\
        ("","Energetic - AShamaluevMusic"),\
        ("","Inspirational Piano Ambient - AShamaluevMusic"),\
        ("","Inspiring Acoustic - AShamaluevMusic"),\
        ("","Inspiring Acoustic Guitar and Choir - AShamaluevMusic"),\
        ("","Optimistic - AShamaluevMusic"),\
        ("","Piano Cinematic - AShamaluevMusic"),\
        ("","Romantic Piano- AShamaluevMusic"),\
        ("","Cosmos - Bare Weed"),\
        ("","Just Peachy (original) - Bellsmarie"),\
        ("","Art Nouveau - Chriszornstudios"),\
        ("","Metal - Chrys Guth"),\
        ("","Lonely - Chukura"),\
        ("","Wise old river (Acoustic version) - Daniel Couper"),\
        ("","Adventure - DarkMoloko"),\
        ("","Feel bad - Desert sharks"),\
        ("","Jingle - Ds’Air"),\
        ("","All of the pieces - Emily Ventre"),\
        ("","Metal - Free Royalty Free Music"),\
        ("","Merry Bay - Ghostrifter Official"),\
        ("","Midnight Stroll - Ghostrifter Official"),\
        ("","Morning Routine - Ghostrifter Official"),\
        ("","Subtle Break - Ghostrifter Official"),\
        ("","Unknown power [[Deep Bass track] - HodgeY"),\
        ("","Apra - Hyde"),\
        ("","60s & 70s Rock Fleetwood Mac Inspired Instrumental - Hyde"),\
        ("","Drum&Bass Rock Pendulum Inspired Instrumental - Hyde"),\
        ("","Mumford & Sons Inspired - Hyde"),\
        ("","Good old days - Jantrax"),\
        ("","Rio - Jantrax"),\
        ("","Second Chance - Jantrax"),\
        ("","Roads (Original Mix) - Jet Voon"),\
        ("","Anachronist - Kevin MacLeod"),\
        ("","First call - Kevin MacLeod"),\
        ("","Fluffing a Duck - Kevin MacLeod"),\
        ("","Marty Gots A Plan - Kevin MacLeod"),\
        ("","Octoblues - Kevin MacLeod"),\
        ("","Radio Martini - Kevin MacLeod"),\
        ("","Sing Along with Jim - Kevin MacLeod"),\
        ("","Windswept - Kevin MacLeod"),\
        ("","Chill - Loudtech"),\
        ("","Acoustic - Mason Carter Music"),\
        ("","Fallen Colors (Original mix) - Meizong"),\
        ("","Night Lights (Original mix) - Meizong"),\
        ("","No Comments (Original mix) - Meizong"),\
        ("","Phate (Original mix) - Meizong"),\
        ("","Raveyard (Original Mix) - Meizong"),\
        ("","Reaching Halo - Meizong & Yeeflex"),\
        ("","Skyline (Original mix) - Meizong [[Argofox]"),\
        ("","Starfire (Original Mix) - Meizong"),\
        ("","The Heat (Original Mix) - Meizong"),\
        ("","Don’t Count On Me - Melodic In Fusion"),\
        ("","EmptyV - Melodic In fusion"),\
        ("","This silence - Melodic In Fusion"),\
        ("","Time goes by - Melodic In Fusion"),\
        ("","Funk rock instrumental - Mironov Sound"),\
        ("","The Unbound Inn - Nerdy Metalhead"),\
        ("","By your side - Nicolai Heidlas"),\
        ("","Golden alley - Nicolai Heidlas"),\
        ("","Let’s begin - Nicolai Heidlas"),\
        ("","Lost souls - Nicolai Heidlas"),\
        ("","Never give up - Nicolai Heidlas"),\
        ("","Roadtrip - Nicolai Heidlas"),\
        ("","Rockin’ Riff - Nicolai Heidlas"),\
        ("","Someways - Nicolai Heidlas"),\
        ("","Sunny acoustic rock - Nicolai Heidlas"),\
        ("","Wings - Nicolai Heidlas"),\
        ("","Winter sunshine - Nicolai Heidlas"),\
        ("","The Sound Of Summer - Oskar Hill & Meizong"),\
        ("","Guitar Gentle - PeriTune"),\
        ("","Guitar Melancholy - PeriTune"),\
        ("","Guitar Melancholy2 - PeriTune"),\
        ("","Gentle Theme2 Guitar - PeriTune"),\
        ("","Gentle Theme2 MusicBox - PeriTune"),\
        ("","Gentle Theme2 Piano - PeriTune"),\
        ("","Suspense5 - PeriTune"),\
        ("","Classicals breakbeat - Punk rock mashed up"),\
        ("","Heavy - Ryan Pollard TK-473 "),\
        ("","Credits - Ryansyah R. Poetra"),\
        ("","Food chain - Sean Danielsen"),\
        ("","Black box - Silent Partner"),\
        ("","DC Love Go-Go - Silent Partner"),\
        ("","Get back - Silent Partner"),\
        ("","Let her in - Silent Partner"),\
        ("","Scrapbook - Silent Partner"),\
        ("","Some obsession - Silent Partner"),\
        ("","Hot Mustard - S Strong"),\
        ("","Slavic Battle Theme - Steven O’Brien"),\
        ("","My heart - Summertime"),\
        ("","Down - The Night"),\
        ("","Medicate me - The Night"),\
        ("","Relax - The Sisonpyh"),\
        ("","Acoustic guitar arrangement for song - TRow"),\
        ("","Your smile - Valtteri Kujala"),\
        ("","Fresh Air Original Instrumental Indie rock/pop - Wayne John Bradley"),\
        ("","They Say - Wowa"),\
        ("","\n{size=40}{color=#fe9416}Szczególne podziękowania dla patronów sezonu 1 i 2{/color}{/size}")
        credits2 = ("","PervDog"),\
        ("","Furuichi Imadori"),\
        ("","Matteo Z. Sylar"),\
        ("","Pip"),\
        ("","Lord Wibble"),\
        ("","Markus K."),\
        ("","NobunagaKira"),\
        ("","moviebuff3000"),\
        ("","Da_Mogwai "),\
        ("","Takesito"),\
        ("","Jared Hawke"),\
        ("","Ryan D"),\
        ("","Skully"),\
        ("","Xor"),\
        ("","April"),\
        ("","Cico"),\
        ("","Hexagon"),\
        ("","Aren"),\
        ("","Cinder Jameson"),\
        ("","Patrick Ryan"),\
        ("","Nuno Martyns"),\
        ("","SirQuailman"),\
        ("","Broker_17"),\
        ("","Wolvy"),\
        ("","Alexey Koroluk aka Ky6ac"),\
        ("","Javlo"),\
        ("","Fauxplayer"),\
        ("","Mike L"),\
        ("","scarzy"),\
        ("","Rystmoose"),\
        ("","ksp"),\
        ("","MisterEmotion"),\
        ("","Ilfenis "),\
        ("","Moneygreen932"),\
        ("","GhostPhil"),\
        ("","Teron Gorefiend (Nikolai)"),\
        ("","DrackDrap"),\
        ("","Zalavier "),\
        ("","Jack Chonko"),\
        ("","Toufas"),\
        ("","Drake"),\
        ("","puter98"),\
        ("","ClearanceClarence"),\
        ("","Kubiac68"),\
        ("","Stèwart"),\
        ("","Alexi Olivares"),\
        ("","Kravza"),\
        ("","Ya boii Krunch"),\
        ("","Laaitie"),\
        ("","Hcobrie"),\
        ("","Fresh Prince"),\
        ("","R. B."),\
        ("","Dirtyscoe "),\
        ("","The Captain Gnome"),\
        ("","Flips"),\
        ("","Konterina"),\
        ("","Saiiixo"),\
        ("","Crapaya"),\
        ("","Manuel"),\
        ("","Scott"),\
        ("","Mark Glukhov"),\
        ("","Danny Delgado Rivera"),\
        ("","JB"),\
        ("","Max Axe"),\
        ("","Koskesh (D.I.F)"),\
        ("","JD Dog Zone"),\
        ("","Jason"),\
        ("","Alex"),\
        ("","BizarroShiz"),\
        ("","StonedGamer"),\
        ("","MathiasIkit "),\
        ("","Jamie"),\
        ("","king4bear"),\
        ("","Baba Yaga"),\
        ("","Rob The Panty Sniffer Johnson"),\
        ("","JSmith"),\
        ("","CJay"),\
        ("","WhiteWolf619"),\
        ("","Stoya"),\
        ("","Hats"),\
        ("","YameteKudasai"),\
        ("","ArcTrooper390"),\
        ("","Jokoh"),\
        ("","Mck AlpHard"),\
        ("","Shadowclone7890"),\
        ("","Reilcas"),\
        ("","Eternal President Kim Il-sung"),\
        ("","Phantasystar14"),\
        ("","Moonman08"),\
        ("","CowboyJones"),\
        ("","LucienM"),\
        ("","Abe"),\
        ("","Rucifie"),\
        ("","JediMindFreek"),\
        ("","Maple"),\
        ("","Andy Johnson"),\
        ("","BoAsimo"),\
        ("","Mellodis"),\
        ("","Mirrifer"),\
        ("","Sanction\'s Charge"),\
        ("","Rob \"Wrecki\" Price"),\
        ("","Redguard153"),\
        ("","SpotlessSniper"),\
        ("","DRiiNK"),\
        ("","Epicreed"),\
        ("","TheBloodmaster"),\
        ("","The Floor Tank"),\
        ("","Eynark"),\
        ("","Dahbobapanda"),\
        ("","Abukz89"),\
        ("","The Hue"),\
        ("","Pacarnya Maya"),\
        ("","Yennefer"),\
        ("","CasterXD"),\
        ("","Exadoow"),\
        ("","H. Magnolie"),\
        ("","TripleisAwesome")
        credits3 = ("","Arrid"),\
        ("","Enfernuz"),\
        ("","Parkwaychris"),\
        ("","RJK"),\
        ("","SlipperyFrog"),\
        ("","Ralcen"),\
        ("","FkT"),\
        ("","InfamousGuy"),\
        ("","Paragon627"),\
        ("","Emulate Life"),\
        ("","Igni"),\
        ("","Varcy"),\
        ("","Mike Fesko"),\
        ("","Umbradeus"),\
        ("","VasWolf"),\
        ("","Ersin Günay"),\
        ("","AtomKraftwerk2074"),\
        ("","KStorm"),\
        ("","Der Dude aka Tim"),\
        ("","AdamB"),\
        ("","Pezz"),\
        ("","Sebastian D"),\
        ("","Joseph M.A."),\
        ("","xcopy"),\
        ("","pierogi_warfare"),\
        ("","Ryan (Chimera512)"),\
        ("","Big Binouchky"),\
        ("","Xander Kross"),\
        ("","bourneagain"),\
        ("","Sebastian"),\
        ("","Dudemandavid23  "),\
        ("","klems2111"),\
        ("","Stefan Olwmoon"),\
        ("","minuteman102"),\
        ("","Nick \"Hikleberry\" Ebert"),\
        ("","soultiger "),\
        ("","Tensa"),\
        ("","Larry Braglin"),\
        ("","J.M. Burri"),\
        ("","0w0"),\
        ("","Carl Larsson"),\
        ("","Ozzyman"),\
        ("","DirtyWes"),\
        ("","Jerry Cochrane"),\
        ("","Chris Lopez"),\
        ("","Sir Loopy"),\
        ("","xJuliusCaesar"),\
        ("","S. Viperidae"),\
        ("","FinTheFastMan"),\
        ("","Angel Mendez"),\
        ("","StRiKeR.SvK aka Martin"),\
        ("","BWR24"),\
        ("","Officer Olive Oil"),\
        ("","Exempt"),\
        ("","xerphus"),\
        ("","staticaxe007"),\
        ("","Donar"),\
        ("","Al Jefferson"),\
        ("","anonymous18"),\
        ("","The One and Only Monks"),\
        ("","Alberto Marques"),\
        ("","Brendan Shanower"),\
        ("","Herro"),\
        ("","Sean"),\
        ("","Michael Shepp4rd"),\
        ("","Waynew91"),\
        ("","DRanger1291"),\
        ("","DreadLocJ"),\
        ("","Matt K"),\
        ("","N7Lover"),\
        ("","Bragan Benigaris"),\
        ("","Chus El Grande"),\
        ("","Mcp"),\
        ("","Skammer22"),\
        ("","Ji Woo Lee"),\
        ("","Gillian Ferber"),\
        ("","Drizzy"),\
        ("","XxROBOTICSxX"),\
        ("","NonTruce"),\
        ("","Relaxed4"),\
        ("","Kinka91"),\
        ("","Grim"),\
        ("","ToddlerfromHell"),\
        ("","Trbaneblade"),\
        ("","MGotzex"),\
        ("","Xiniz"),\
        ("","Andy Enterprise"),\
        ("","Fitzy"),\
        ("","Ransted"),\
        ("","Prince Albert"),\
        ("","Jely Carr"),\
        ("","Germanic_DIK"),\
        ("","DormantPsyche"),\
        ("","Red T Basco"),\
        ("","Erik Sarfert (ZaferiX)"),\
        ("","Nightmare47"),\
        ("","Elijer"),\
        ("","ZePolarBearr"),\
        ("","Atola"),\
        ("","Luca Gambit"),\
        ("","Kristian Rasmussen"),\
        ("","Sifzero"),\
        ("","CaptainRosh"),\
        ("","Chris65687"),\
        ("","Nero Lei"),\
        ("","CrazyTheBiker"),\
        ("","Ota9Nipp0n"),\
        ("","PandaDrummer"),\
        ("","Xalubis"),\
        ("","Xindama"),\
        ("","Lunaruss"),\
        ("","Kirin"),\
        ("","Rooks54"),\
        ("","Starki"),\
        ("","Saltzpyre"),\
        ("","Oliver Pehrsson"),\
        ("","Peridot"),\
        ("","ForOnce"),\
        ("","Benjamin Hawkwood"),\
        ("","Sir_Weast"),\
        ("","Templar366"),\
        ("","Lordblade03"),\
        ("","Ryno"),\
        ("","Wang Wilson"),\
        ("","Nour Parker Wayne"),\
        ("","ExhaileLife"),\
        ("","Mark Brundish"),\
        ("","Whitezilla"),\
        ("","Dyviant"),\
        ("","Leo"),\
        ("","BunnyRabbir"),\
        ("","G<3C"),\
        ("","D•R•K"),\
        ("","iiNFaMoUsZv2"),\
        ("","StrangerCamus"),\
        ("","Ricky Giovagnoli"),\
        ("","Blazehunterx "),\
        ("","mcjr"),\
        ("","AzeyusXV"),\
        ("","welldone"),\
        ("","Richard royston"),\
        ("","Michael Maimone"),\
        ("","UngodlyCutty"),\
        ("","Immentale"),\
        ("","Exses"),\
        ("","Chief Solo"),\
        ("","Resoric"),\
        ("","Jon Wick"),\
        ("","WardogMe"),\
        ("","Obeze Ducc"),\
        ("","GetTrickdM8"),\
        ("","Patrick Williams"),\
        ("","Double0Beard"),\
        ("","ZackNero03"),\
        ("","Nate Eaton"),\
        ("","ForceLord"),\
        ("","Aydwen"),\
        ("","Heavy Cy"),\
        ("","demcro"),\
        ("","Llyandra"),\
        ("","Jimmy Provolone"),\
        ("","Zexial"),\
        ("","HowdyPartner"),\
        ("","Rumirion"),\
        ("","iPertis"),\
        ("","Nitroalex"),\
        ("","XannyPacquiao"),\
        ("","Sam Castle"),\
        ("","MrSnugles"),\
        ("","Cousin Havoc"),\
        ("","liamb19"),\
        ("","Jaiden"),\
        ("","Soulshade84"),\
        ("","MrNyxt"),\
        ("","CieJe"),\
        ("","MisterKrause"),\
        ("","Blacksky003"),\
        ("","Davidion"),\
        ("","DrJosh"),\
        ("","Velkdom"),\
        ("","Ian K."),\
        ("","Jinpeng Y."),\
        ("","Camino"),\
        ("","MFA"),\
        ("","Ryan A."),\
        ("","Kenan Kenway"),\
        ("","Ross D"),\
        ("","Richard T"),\
        ("","Lacey Robbins"),\
        ("","MineHack"),\
        ("","Cimpala"),\
        ("","DMaple"),\
        ("","Ritteru"),\
        ("","Barbatos"),\
        ("","Touhara"),\
        ("","Scotty Doesn't Know"),\
        ("","Shuddermania"),\
        ("","Kellan"),\
        ("","Kleantes"),\
        ("","Nobuddy"),\
        ("","KingJimbob"),\
        ("","itsSenapai415"),\
        ("","DJ_Mo_G"),\
        ("","Christopher M Zdenek"),\
        ("","ElderLichJoe"),\
        ("","Nicholas Gowen"),\
        ("","Zachary Barker"),\
        ("","Ramdur"),\
        ("","Remy"),\
        ("","RogueRat"),\
        ("","Sophia Colson"),\
        ("","Ateo"),\
        ("","BuDz"),\
        ("","Jasukoon"),\
        ("","Cali"),\
        ("","Draxxa"),\
        ("","SorrowxD"),\
        ("","BLB"),\
        ("","Ross B.KJak"),\
        ("","Sky.HH.Lasop"),\
        ("","R0GUE C0BRA"),\
        ("","degreebound205"),\
        ("","DSeb"),\
        ("","Gratosch Kalligo"),\
        ("","GH2020"),\
        ("","ablur"),\
        ("","Lubartus Sijbom"),\
        ("","enigma"),\
        ("","JewestOne"),\
        ("","afterlife69"),\
        ("","jhammer81"),\
        ("","Waffles"),\
        ("","oreochipsmokey"),\
        ("","Craggin"),\
        ("","Venøm"),\
        ("","Tomato"),\
        ("","Caz1"),\
        ("","Mizorestalker"),\
        ("","GrantB"),\
        ("","Admiral392"),\
        ("","Sirugate"),\
        ("","AlbaGamer82"),\
        ("","BlackyTGC"),\
        ("","Shaggy Greenz"),\
        ("","Bartleby Finch"),\
        ("","Rei'esl"),\
        ("","Latvian"),\
        ("","Affluent"),\
        ("","Vaff"),\
        ("","OneEyedKing24"),\
        ("","Mugiwara1501"),\
        ("","AntWarrior"),\
        ("","Vaclio"),\
        ("","DamonBekmos"),\
        ("","Wendor"),\
        ("","Admiral Clitty$"),\
        ("","Antdud"),\
        ("","RazorSaber"),\
        ("","LegendaryKodak"),\
        ("","Zani"),\
        ("","kentyrr"),\
        ("","WOLPHBYTE"),\
        ("","Professor Hackett"),\
        ("","WhiskTob"),\
        ("","Vegematic"),\
        ("","Coolcats682"),\
        ("","PureTerror"),\
        ("","Batt1eCry15"),\
        ("","Sharkyinferno"),\
        ("","Moratyr"),\
        ("","Juska"),\
        ("","Perdogo"),\
        ("","Alaratt")
        credits4 = ("","Watson710"),\
        ("","Moy56"),\
        ("","JohnnyG1440"),\
        ("","AdamZZ"),\
        ("","MoZZi"),\
        ("","Exponict"),\
        ("","JoeyDaKilla"),\
        ("","greeN7bean"),\
        ("","GrizzWolf82"),\
        ("","NeericIsaad"),\
        ("","Connor"),\
        ("","Beroya182"),\
        ("","Banesfury"),\
        ("","Jonathan Cook / Angeldustz"),\
        ("","ElderDarkWolf666"),\
        ("","Tem and FroggySitty"),\
        ("","Irifec"),\
        ("","Aanon"),\
        ("","Amart0369"),\
        ("","Minnow"),\
        ("","Tsqrrl"),\
        ("","MrToeknee"),\
        ("","Barrac Fawkes"),\
        ("","DeuxMille"),\
        ("","Regin"),\
        ("","Ruthless"),\
        ("","bigAsianDIK"),\
        ("","DakotaRobo"),\
        ("","Syn"),\
        ("","ChrisSwe"),\
        ("","DrThic"),\
        ("","TregGimmons"),\
        ("","Raub Resa"),\
        ("","Chiss"),\
        ("","Carrilla"),\
        ("","Murrey"),\
        ("","BigDaddyW"),\
        ("","TheCaliChris"),\
        ("","Jack Mendoza"),\
        ("","Mo Gor"),\
        ("","Valkyrie65.."),\
        ("","ViPo"),\
        ("","Chase Oppliger"),\
        ("","Hithrand"),\
        ("","drEan"),\
        ("","Jorgisven"),\
        ("","Jerry Trainor / Dylan Desaulniers"),\
        ("","Vic"),\
        ("","Ramon Borja"),\
        ("","Mike Roch"),\
        ("","SykO"),\
        ("","Konradikal"),\
        ("","Albert R"),\
        ("","djz"),\
        ("","Ian Smith"),\
        ("","Beast"),\
        ("","Windfury"),\
        ("","Nathaniel B."),\
        ("","Martin K."),\
        ("","Brad Dargusch"),\
        ("","Mad$an"),\
        ("","Andresen"),\
        ("","KBC"),\
        ("","Matt Wagen"),\
        ("","Michael Meier (SirBlackwings)"),\
        ("","A'Jax Burd!ck"),\
        ("","Aëran"),\
        ("","Philippe Hache"),\
        ("","Larvayne"),\
        ("","PandaGuy"),\
        ("","Mike O"),\
        ("","Gig"),\
        ("","Steven Hagen"),\
        ("","Spyderwilk"),\
        ("","JohnnyJ"),\
        ("","Elke"),\
        ("","Schinhofen"),\
        ("","Kyle Macias"),\
        ("","Mclovin004"),\
        ("","Quentin Compson"),\
        ("","Opetox"),\
        ("","Shia Fall"),\
        ("","seahawks4ever"),\
        ("","Jayke"),\
        ("","Angreh Llama"),\
        ("","MonksV1"),\
        ("","Nudal"),\
        ("","Dr. Matt Wagen"),\
        ("","Cold Flame"),\
        ("","Fallen1o9"),\
        ("","Rebel Leader"),\
        ("","Dayjyyyyy"),\
        ("","David Gaither"),\
        ("","Mika Graven"),\
        ("","Prawnhub Premium"),\
        ("","Chasslo"),\
        ("","19albi99"),\
        ("","CarrotRae"),\
        ("","Erich G."),\
        ("","Raymond O."),\
        ("","Mike K"),\
        ("","Nick Cannon"),\
        ("","Sehiri"),\
        ("","SleekShadow gaming"),\
        ("","Ryan After Dark"),\
        ("","Savo"),\
        ("","Philippe P."),\
        ("","Uriel L."),\
        ("","FERKILL"),\
        ("","Dorian Rast"),\
        ("","Rew"),\
        ("","Pat90"),\
        ("","Son Goku"),\
        ("","Ryan-Patrick Lavarias"),\
        ("","SGTJarhead"),\
        ("","DDA80"),\
        ("","EdwardS"),\
        ("","Nathan Keo"),\
        ("","SamuelDC"),\
        ("","Stuart ainslie"),\
        ("","Xero"),\
        ("","TaxView"),\
        ("","WoozyMess"),\
        ("","sultanoft"),\
        ("","RobertM"),\
        ("","Michael M."),\
        ("","Marcus Johnson"),\
        ("","Mahani"),\
        ("","TheNavigator"),\
        ("","Reboot"),\
        ("","Storm"),\
        ("","Jevbleidd"),\
        ("","Toaster"),\
        ("","Harry Slink C"),\
        ("","Bootcolonel"),\
        ("","Stryker67"),\
        ("","Rokkamina"),\
        ("","Nico Re"),\
        ("","Slived"),\
        ("","Derek DS343"),\
        ("","Spleez0rz"),\
        ("","prodbyfig"),\
        ("","Sheriff \"Big DIK\" Turner"),\
        ("","CeeJay Joslet"),\
        ("","Siru"),\
        ("","Hatch Malone"),\
        ("","thanksboss"),\
        ("","TomuK"),\
        ("","CIRLEUF"),\
        ("","Light"),\
        ("","Alexir"),\
        ("","Z3N-K0"),\
        ("","Jerry048"),\
        ("","dirtymic"),\
        ("","CloutGoggle"),\
        ("","Melody's Guitar"),\
        ("","Hazel"),\
        ("","deBil"),\
        ("","Grayson1509"),\
        ("","Knochey"),\
        ("","Furai"),\
        ("","Botland"),\
        ("","Buckeyerard"),\
        ("","Wildman"),\
        ("","Lectiuss"),\
        ("","Riff Raff"),\
        ("","Jaybee"),\
        ("","SirWong"),\
        ("","Ozymandias"),\
        ("","FedeNico"),\
        ("","TYTY8109"),\
        ("","Boy Cook"),\
        ("","Edrick1976"),\
        ("","godfather48"),\
        ("","WarPig"),\
        ("","kingdonger"),\
        ("","KrazyCooter52"),\
        ("","Masi"),\
        ("","Nicko"),\
        ("","General Cornwallis"),\
        ("","riceball"),\
        ("","Jaye Mills"),\
        ("","Lucas"),\
        ("","Fyrtue"),\
        ("","ReggieVK"),\
        ("","TheOverSeer"),\
        ("","JrhawkKU"),\
        ("","Amir Naseri"),\
        ("","Pat"),\
        ("","Ass Man Aprox"),\
        ("","RyAlex"),\
        ("","Dragon_King269"),\
        ("","Maladapted"),\
        ("","Saev"),\
        ("","Rev. Goober"),\
        ("","Aussie Heathen "),\
        ("","Turtle"),\
        ("","Polaris"),\
        ("","Unhappy Camper"),\
        ("","Misabu"),\
        ("","GrindingGamer"),\
        ("","NekoPhile"),\
        ("","Shonuff"),\
        ("","S. Mana"),\
        ("","NicoElton"),\
        ("","Brandon Royce"),\
        ("","Maximoffspring"),\
        ("","TemporaVectis"),\
        ("","KratoStoop"),\
        ("","Bound2Patience")
        credits5 = ("","Jamison"),\
        ("","Crxkey"),\
        ("","Kincey"),\
        ("","Ol3_Andr3"),\
        ("","Dsaw"),\
        ("","Simoon-F"),\
        ("","JohnFKramer "),\
        ("","Toyota AE86"),\
        ("","V"),\
        ("","Matt Kessler"),\
        ("","Hargmenrar"),\
        ("","J"),\
        ("","Justin14237"),\
        ("","SpoonzCoop"),\
        ("","Ilpallazzo"),\
        ("","CautionRamen"),\
        ("","Kujo Nakayama"),\
        ("","KessY"),\
        ("","Black Superman"),\
        ("","Krelock"),\
        ("","Edline"),\
        ("","Timeo"),\
        ("","Jokra"),\
        ("","Lunatik"),\
        ("","KARASIA"),\
        ("","SigShooter"),\
        ("","Talon"),\
        ("","Dillard"),\
        ("","Borat"),\
        ("","Fecooo"),\
        ("","Kørvüs"),\
        ("","AggieSlimer02"),\
        ("","Straiser"),\
        ("","Monium"),\
        ("","genestarwind"),\
        ("","ATG"),\
        ("","Shmee"),\
        ("","Heissin"),\
        ("","Justus"),\
        ("","Shrike4242"),\
        ("","Eroc"),\
        ("","Darkby"),\
        ("","Kireelad"),\
        ("","SleviMedic"),\
        ("","D3ltaTon"),\
        ("","Endro"),\
        ("","RussianFPS :3"),\
        ("","Liborex"),\
        ("","SergeantGamer"),\
        ("","Valkyr"),\
        ("","Ark Daniels"),\
        ("","ItsMuri"),\
        ("","Poadiup"),\
        ("","Scarps"),\
        ("","Mrbazuco"),\
        ("","Ratzinger"),\
        ("","lduke1990"),\
        ("","VNwhiteknight"),\
        ("","V Alonzo"),\
        ("","Chillhelm"),\
        ("","Tyler R"),\
        ("","Beast of Bray"),\
        ("","LatinoDude"),\
        ("","Aasirion"),\
        ("","StragglyTunic7"),\
        ("","Ludabreez"),\
        ("","Cautionss"),\
        ("","DaddyGordo"),\
        ("","C. Eric"),\
        ("","Thomas B."),\
        ("","Manhunlo6699"),\
        ("","Rotirail"),\
        ("","DarkwolfLord11"),\
        ("","RamsesV"),\
        ("","TsunamiKata"),\
        ("","Sedriq"),\
        ("","Rocky"),\
        ("","ToeBae C"),\
        ("","Ruvik"),\
        ("","Chance C."),\
        ("","Zyaan"),\
        ("","Samuel M. A."),\
        ("","Laureline"),\
        ("","JoBe"),\
        ("","Psychedelic"),\
        ("","Pnut"),\
        ("","James B."),\
        ("","Scotty D"),\
        ("","Andres R"),\
        ("","Peerless Girl"),\
        ("","Jamie Todd Howard"),\
        ("","James McMurphy"),\
        ("","Michael Espanner"),\
        ("","Shab Gaungoo"),\
        ("","stanley925"),\
        ("","Guicho E"),\
        ("","GnotGnap"),\
        ("","Hang Y"),\
        ("","Grim Nova"),\
        ("","Dark Repulsor"),\
        ("","Nick P"),\
        ("","Jonathan Vakarian"),\
        ("","Raidin"),\
        ("","DrEvil666"),\
        ("","KnightWolves"),\
        ("","DoerflerN256"),\
        ("","Omni Omega1"),\
        ("","Knightly"),\
        ("","Mischl"),\
        ("","Calypso"),\
        ("","ShadowMeta4259"),\
        ("","Grivori"),\
        ("","Knightwalker"),\
        ("","R4MPZY"),\
        ("","OfficialyEddie"),\
        ("","Draco aka GodOfStrengthX"),\
        ("","NotDrPinkCake"),\
        ("","FrenzyFire000"),\
        ("","RainyNoir"),\
        ("","LovesSorrows"),\
        ("","Godslayer"),\
        ("","DiabloKaiser"),\
        ("","CocoPebbles"),\
        ("","Nightly"),\
        ("","Lollipappy"),\
        ("","Nandobabata"),\
        ("","KnightRider"),\
        ("","Hamish C"),\
        ("","Tickle Me DIK"),\
        ("","HeyJoji"),\
        ("","6dreamsofvelvet"),\
        ("","Jonas Jalapeños"),\
        ("","Hamez"),\
        ("","Mr.Slothy"),\
        ("","DoritoMan"),\
        ("","Malus"),\
        ("","jurkinit"),\
        ("","LowBar"),\
        ("","DIKccav"),\
        ("","DIKmented"),\
        ("","DIKFrost"),\
        ("","Sundell"),\
        ("","MadMedic171"),\
        ("","Hootenanee"),\
        ("","Chaotic"),\
        ("","CatatonicPrince"),\
        ("","HONDA"),\
        ("","JamieSadistic"),\
        ("","ScottNeptune"),\
        ("","Dark_Gnark"),\
        ("","Imcharliebrown"),\
        ("","Rain"),\
        ("","Xenophasa"),\
        ("","Isolation"),\
        ("","DarkwatchNOLA"),\
        ("","SatanNick"),\
        ("","Rikaza"),\
        ("","Layne Lowe"),\
        ("","Dino Spumoni"),\
        ("","Thor von Fiddle"),\
        ("","LymanLyme"),\
        ("","Dew"),\
        ("","ALLiseeisGOLD"),\
        ("","Adrijus"),\
        ("","Eren1993"),\
        ("","MrCamox"),\
        ("","BulbasaurRave"),\
        ("","Thodekke"),\
        ("","Errol"),\
        ("","Grarah"),\
        ("","VacaPaca"),\
        ("","Alex Rotherham"),\
        ("","PratorX"),\
        ("","KELLY CAL"),\
        ("","GZuluB"),\
        ("","TossBoyP"),\
        ("","iTs Manueh"),\
        ("","Courage Wolf"),\
        ("","Tyler Hoover"),\
        ("","MrHaas"),\
        ("","BulgariaFirst"),\
        ("","nycxrascal"),\
        ("","Godfather48"),\
        ("","Nighthawwk"),\
        ("","Skumduff"),\
        ("","Juicey954"),\
        ("","WeirdScienceX"),\
        ("","Shanto"),\
        ("","Jamikari"),\
        ("","Tesseract109"),\
        ("","Hebonjour"),\
        ("","McCringle"),\
        ("","Stoo`"),\
        ("","yuriblacki"),\
        ("","Up"),\
        ("","Zolexius"),\
        ("","VerliZero"),\
        ("","Big Bad Booby Cat"),\
        ("","Tiggy of Tiggington"),\
        ("","1Yares1"),\
        ("","Anders Jensen"),\
        ("","PyroPyotr"),\
        ("","PiConte"),\
        ("","xX_BACKLASH_Xx"),\
        ("","Raptures Demise"),\
        ("","Sammy"),\
        ("","LoopyRoopy"),\
        ("","Inhuman"),\
        ("","ProfessorBoeing"),\
        ("","Jelle Slaets"),\
        ("","Yahyah i am Lorde Lorde Lorde"),\
        ("","Richard \"Big Sexy\""),\
        ("","Song Nai"),\
        ("","Apple DiK-Louang"),\
        ("","Robert Brannan"),\
        ("","Kelmate"),\
        ("","VDubs"),\
        ("","TONI"),\
        ("","Chris Damrel"),\
        ("","JeremySolo"),\
        ("","Muredok"),\
        ("","TunableDavis"),\
        ("","DigBickBrandon"),\
        ("","Dadusmaximus"),\
        ("","EvilGregy"),\
        ("","Bender"),\
        ("","Nivek"),\
        ("","Deathnick"),\
        ("","Matous Panek"),\
        ("","Superchat"),\
        ("","MysticMX"),\
        ("","TheHobbitG"),\
        ("","Michael"),\
        ("","Neeric I'saad"),\
        ("","[[UV] SevenS"),\
        ("","axelfoli1"),\
        ("","Bruce XIE"),\
        ("","iCrusade"),\
        ("","zay"),\
        ("","RozeEnzo999"),\
        ("","ToniLMM90"),\
        ("","Forseythe"),\
        ("","BADI-GIULI"),\
        ("","GothicSalad"),\
        ("","Garithian"),\
        ("","-Barlow"),\
        ("","Anton."),\
        ("","Thomas Kain"),\
        ("","LYRYKAL"),\
        ("","Conrad"),\
        ("","David Oliveira"),\
        ("","DLXB"),\
        ("","MrAug360"),\
        ("","Joshua Proctor"),\
        ("","Kayin & Astaribs"),\
        ("","Ben Telometo"),\
        ("","Ryo69"),\
        ("","Diophantus"),\
        ("","Pope Poe"),\
        ("","Mistress Elemental"),\
        ("","Jutter"),\
        ("","Eyox76"),\
        ("","Not Max"),\
        ("","Daniel Mendoza"),\
        ("","Kira Shinza"),\
        ("","Cursed_Impact"),\
        ("","MB89"),\
        ("","Blaineo Pilkinton"),\
        ("","BoxerBlake"),\
        ("","Chamber691"),\
        ("","False Equipment"),\
        ("","Ceez"),\
        ("","RedJester"),\
        ("","Szinister"),\
        ("","Wolfegrimm"),\
        ("","IronTank"),\
        ("","Captain4Head"),\
        ("","Kontonix"),\
        ("","DeckyMoore"),\
        ("","Majulla"),\
        ("","ChaosiumX"),\
        ("","Komplex"),\
        ("","MrRage67"),\
        ("","ChristianMingle"),\
        ("","xjacobadobo"),\
        ("","GallivantingGlobetrotter"),\
        ("","Acidsphere"),\
        ("","SmokeyGrey"),\
        ("","Fabloo"),\
        ("","Basil Midnight"),\
        ("","Cum Cube"),\
        ("","frogwearingvans"),\
        ("","Chandlerbing"),\
        ("","Bing!"),\
        ("","Mr Peepers"),\
        ("","MrLerm"),\
        ("","The Other Corey"),\
        ("","Oiram"),\
        ("","Damian Kenin"),\
        ("","Travis Dunnivan"),\
        ("","Bubba1017"),\
        ("","IstvanT"),\
        ("","xJoaco27"),\
        ("","Odofondas"),\
        ("","Lesleythekid"),\
        ("","JParty"),\
        ("","Darkenel"),\
        ("","Wildo"),\
        ("","Erebeus988"),\
        ("","PeterSy"),\
        ("","Adrian A"),\
        ("","Kayruhb"),\
        ("","PainTrainPanda"),\
        ("","AmericanGulp"),\
        ("","MonSe75"),\
        ("","Lukas J"),\
        ("","C4P7AIN_SCHoRNi"),\
        ("","Black58a"),\
        ("","Jesse G"),\
        ("","SelectiveRisk"),\
        ("","Keith C"),\
        ("","6LA-Flacco"),\
        ("","CE-Shin Kaiju"),\
        ("","MPA- Michael P"),\
        ("","DLGG"),\
        ("","RL"),\
        ("","Codes"),\
        ("","HoodieGreedy"),\
        ("","Papapud"),\
        ("","Nirvanacst"),\
        ("","Kacaronte"),\
        ("","Merlin"),\
        ("","MusicalPenguino"),\
        ("","Mitede"),\
        ("","Brando Meatstick"),\
        ("","Valdur90"),\
        ("","Denseer20"),\
        ("","Drexxlo"),\
        ("","Ploumploum"),\
        ("","Diver"),\
        ("","Vas"),\
        ("","Spiderwilk"),\
        ("","Sava"),\
        ("","Gtxaurel"),\
        ("","BlackSteve"),\
        ("","Keith Schlumbrecht"),\
        ("","Coco"),\
        ("","Peter Sy"),\
        ("","Lay Low"),\
        ("","Qweasdf1"),\
        ("","Bunny"),\
        ("","The Metal Dr"),\
        ("","Lukas Pasko"),\
        ("","Demented Reaper"),\
        ("","GingerAvenger51"),\
        ("","Jeff from Work"),\
        ("","Nico90"),\
        ("","AlJi"),\
        ("","Wortharr"),\
        ("","The Exception"),\
        ("","MV916"),\
        ("","Kristofer Engstrom"),\
        ("","Matthew Just"),\
        ("","TortillaJackson"),\
        ("","Messiah01"),\
        ("","KingBWIII"),\
        ("","Saev."),\
        ("","Snips51"),\
        ("","Miňa"),\
        ("","devarius2005"),\
        ("","Bibedibabediboo"),\
        ("","John Vayas"),\
        ("","SirDhyne"),\
        ("","Boris Xanovavych"),\
        ("","FamineBoik"),\
        ("","DCMSTech"),\
        ("","BobrBilbo"),\
        ("","SmileyYo"),\
        ("","Siege Monkey"),\
        ("","J."),\
        ("","Yepod"),\
        ("","Roxas"),\
        ("","Blind Cat"),\
        ("","Steve from Accounting"),\
        ("","D1pstick"),\
        ("","Scarmaster19"),\
        ("","IronTank120"),\
        ("","TheQuietWolf"),\
        ("","J Finnerty"),\
        ("","Beck"),\
        ("","Snowman"),\
        ("","Terry Griffin"),\
        ("","UnckieV"),\
        ("","Lil_Dish (Goofy Gamer)"),\
        ("","Prizmanza"),\
        ("","Nici"),\
        ("","Mixxy"),\
        ("","Gapesy"),\
        ("","Geralt Of Ashkelon"),\
        ("","CBA ANDERS"),\
        ("","Graffis"),\
        ("","Eaglenez"),\
        ("","Δ _Issam Choukairi"),\
        ("","Stark"),\
        ("","Pancakes"),\
        ("","MikeP"),\
        ("","Dr.McLickertitty"),\
        ("","KungFury"),\
        ("","DevlynD"),\
        ("","Goofy Wolverine"),\
        ("","thuganomics85"),\
        ("","InsanePyrDragon"),\
        ("","Mr Bubbless"),\
        ("","Cave Johnson"),\
        ("","Kaine Scott Francis"),\
        ("","PhantasyStar14"),\
        ("","Michael Ortiz"),\
        ("","Bob Malks"),\
        ("","Exorikk"),\
        ("","NoOneEls"),\
        ("","Sleepy"),\
        ("","Milasecond"),\
        ("","Bishnu Kumari Sahu"),\
        ("","RTKMason"),\
        ("","Aussiegaming94"),\
        ("","Black Heart Valentine"),\
        ("","Panzerdk"),\
        ("","Viperidae"),\
        ("","Ksteelwall"),\
        ("","Sainaiver"),\
        ("","Mordekki"),\
        ("","ItzVJhayy"),\
        ("","Anonymous donors")
        credits_s = "{font=candara.ttf}"
        c1 = ""
        for c in credits:
            if not c1==c[0]:
                credits_s += "\n{size=40}{color=#fe9416}" + c[0] + "{/color}{/size}\n"
                credits_s += "{size=40}" + c[1] + "{/size}\n"
            else:
                credits_s += "{size=30}" + c[1] + "{/size}\n"
            c1=c[0]
        credits_s += "{/font}"
        credits_s2 = "{font=candara.ttf}{size=30}"
        credits_s3 = "{font=candara.ttf}{size=30}"
        credits_s4 = "{font=candara.ttf}{size=30}"
        credits_ext3 = "{font=candara.ttf}{size=30}"
        credits_ext4 = "{font=candara.ttf}{size=30}"
        credits_ext5 = "{font=candara.ttf}{size=30}"
        c1 = ""
        tmpCount = 0
        for c in credits2:
            if tmpCount == 0:
                credits_s2 += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_s3 += c[1] + "\n"
                tmpCount += 1
            else:
                credits_s4 += c[1] + "\n"
                tmpCount = 0
        if tmpCount == 1:
            credits_s3 += " \n"
            credits_s4 += " \n"
        elif tmpCount == 2:
            credits_s4 += " \n"
        credits_s2 += "{/size}{/font}"
        credits_s3 += "{/size}{/font}"
        credits_s4 += "{/size}{/font}"
        tmpCount = 0
        for c in credits3:
            if tmpCount == 0:
                credits_ext3 += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_ext4 += c[1] + "\n"
                tmpCount += 1
            else:
                credits_ext5 += c[1] + "\n"
                tmpCount = 0
        if tmpCount == 1:
            credits_ext4 += " \n"
            credits_ext5 += " \n"
        elif tmpCount == 2:
            credits_ext5 += " \n"
        tmpCount = 0
        for c in credits4:
            if tmpCount == 0:
                credits_ext3 += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_ext4 += c[1] + "\n"
                tmpCount += 1
            else:
                credits_ext5 += c[1] + "\n"
                tmpCount = 0
        if tmpCount == 1:
            credits_ext4 += " \n"
            credits_ext5 += " \n"
        elif tmpCount == 2:
            credits_ext5 += " \n"
        tmpCount = 0
        for c in credits5:
            if tmpCount == 0:
                credits_ext3 += c[1] + "\n"
                tmpCount += 1
            elif tmpCount == 1:
                credits_ext4 += c[1] + "\n"
                tmpCount += 1
            else:
                credits_ext5 += c[1] + "\n"
                tmpCount = 0
        if tmpCount == 1:
            credits_ext4 += " \n"
            credits_ext5 += " \n"
        elif tmpCount == 2:
            credits_ext5 += " \n"
        credits_ext3 += "{/size}{/font}"
        credits_ext4 += "{/size}{/font}"
        credits_ext5 += "{/size}{/font}"

init:
    image cred = Text(credits_s, text_align=0.5)
    image cred2 = Text(credits_s2, text_align=0.5)
    image cred3 = Text(credits_s3, text_align=0.5)
    image cred4 = Text(credits_s4, text_align=0.5)
    image cred_ext3 = Text(credits_ext3, text_align=0.5)
    image cred_ext4 = Text(credits_ext4, text_align=0.5)
    image cred_ext5 = Text(credits_ext5, text_align=0.5)
    image cred_isabella_bg = "credits_isabella_bg"
    image cred_jill_bg = "credits_jill_bg"
    image cred_sage_bg = "credits_sage_bg"
    image cred_josy_bg = "credits_josy_bg"
    image cred_maya_bg = "credits_maya_bg"
    image cred_quinn_bg = "credits_quinn_bg"
    image cred_riona_bg = "credits_riona_bg"
    image cred_camila_bg = "credits_camila_bg"
    image cred_cathy_bg = "credits_cathy_bg"
    image cred_jade_bg = "credits_jade_bg"
return