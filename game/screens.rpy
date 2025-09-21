init python:
    import datetime
    
    MONTHS_PL = {
        "January": "Styczeń",
        "February": "Luty",
        "March": "Marzec",
        "April": "Kwiecień",
        "May": "Maj",
        "June": "Czerwiec",
        "July": "Lipiec",
        "August": "Sierpień",
        "September": "Wrzesień",
        "October": "Październik",
        "November": "Listopad",
        "December": "Grudzień"
    }

    def FileTimePL(slot):
        t = FileTime(slot, format="%d %B %Y, %H:%M", empty=None)
        if t is None:
            return _("Puste miejsce")
        
        for en, pl in MONTHS_PL.items():
            if en in t:
                t = t.replace(en, pl)
                break
        
        return t

init -1:
    style slot_text_custom:
        color "#ffffff"
        xmaximum 320
        text_align 0.5
        yoffset 5
        font "candara.ttf"
        outlines [(4, "#330000", 0, 0)]
        hover_outlines [(4, "#330000", 0, 0)]
        size 40
init -1:
    style default:
        properties gui.text_properties()
        language gui.language
init -1:
    style input:
        properties gui.text_properties("input", accent=True)
        adjust_spacing False
init -1:
    style hyperlink_text:
        hover_underline True
        properties gui.text_properties("hyperlink", accent=True)
init -1:
    style gui_text:
        properties gui.text_properties("interface")
init -1:
    style button:
        properties gui.button_properties("button")
init -1:
    style button_text is gui_text:
        properties gui.text_properties("button")
        yalign 0.5
init -1:
    style label_text is gui_text:
        properties gui.text_properties("label", accent=True)
init -1:
    style prompt_text is gui_text:
        properties gui.text_properties("prompt")
init -1:
    style bar:
        left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        ysize gui.bar_size
        right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
init -1:
    style vbar:
        bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
        top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        xsize gui.bar_size
init -1:
    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style vscrollbar:
        base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        xsize gui.scrollbar_size
        thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
init -1:
    style slider:
        ysize gui.slider_size
        base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/slider/horizontal_[prefix_]thumb.png"
init -1:
    style vslider:
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        xsize gui.slider_size
        thumb "gui/slider/vertical_[prefix_]thumb.png"
init -1:
    style frame:
        padding gui.frame_borders.padding
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
init -1 define persistent.say_window_alpha = 0.3
init -501:
    screen say(who, what):
        style_prefix "say"
        window:
            background Transform(style.window.background, alpha=persistent.say_window_alpha)
            id "window"
            if who is not None:
                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"
            text what id "what"
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0
init -1:
    python:
        config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue
init -1 style namebox is default
init -1 style namebox_label is say_label
init -1:
    style window:
        xalign 0.5
        ysize gui.textbox_height
        background Image("gui/textbox_new.png", xalign=0.5, yalign=1.0)
        yalign gui.textbox_yalign
        xfill True
init -1:
    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        xsize gui.namebox_width
        ysize gui.namebox_height
        ypos gui.name_ypos
        padding gui.namebox_borders.padding
        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
init -1:
    style say_label:
        xalign gui.name_xalign
        properties gui.text_properties("name", accent=True)
        yalign 0.5
init -1:
    style say_dialogue:
        xpos gui.dialogue_xpos
        properties gui.text_properties("dialogue")
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos
init -501:
    screen input(prompt):
        style_prefix "input"
        window:
            vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos
                text prompt style "input_prompt"
                input id "input"
init -1 style input_prompt is default
init -1:
    style input_prompt:
        xalign 0.5
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
        properties gui.text_properties("input_prompt")
init -1:
    style input:
        xalign 0.5
        xmaximum gui.dialogue_width
init -2:
    style menu_sex_style is default
    style menu_sex_style is button_text:
        color "#ffcc66"
        drop_shadow [(2, 2)]
        yoffset 5
        hover_outlines [(1, "#660066", 0, 0)]
        hover_color "#ffffff"
        font "Audrey-Bold.otf"
        drop_shadow_color "#663300"
        outlines [(1, "#330000", 0, 0)]
        xoffset 55
        size 30
    style menu_sex_style_disabled is button_text:
        color "#ffffff"
        drop_shadow [(2, 2)]
        yoffset 5
        hover_color "#ffffff"
        font "Audrey-Bold.otf"
        drop_shadow_color "#663300"
        xoffset 55
        size 30
    style menu_sex_style_button is button:
        ymaximum 70
        ypadding 10
        xmaximum int(config.screen_width * 0.3)
        xpadding 15
        xminimum int(config.screen_width * 0.3)
        background Frame("images/gui/buttons/sex_buttons/sex_choices_idle.png",0,0)
        yminimum 70
        hover_background Frame("images/gui/buttons/sex_buttons/sex_choices_hover.png",0,0)
    style menu_sex_style_button_disabled is button:
        ymaximum 70
        ypadding 10
        xmaximum int(config.screen_width * 0.3)
        xpadding 15
        xminimum int(config.screen_width * 0.3)
        background Frame("images/gui/buttons/sex_buttons/sex_choices_disabled.png",0,0)
        yminimum 70
        hover_background Frame("images/gui/buttons/sex_buttons/sex_choices_disabled.png",0,0)
init -501:
    screen choice:
        style_prefix "choice"
        vbox:
            xalign 1.0
            yalign 0.8
            style "menu"
            spacing 2
            for _sl2_i in items:
                $ caption, action, chosen  = _sl2_i
                if action:
                    if " (disabled)" in caption:
                        button:
                            style "menu_sex_style_button_disabled"
                            text caption.replace(" (disabled)", "") style "menu_sex_style_disabled"
                    else:
                        button:
                            action action
                            style "menu_sex_style_button"
                            text caption style "menu_sex_style"
                else:
                    text caption style "menu_sex_style"
init -1 define config.autosave_slots = 12
init -1 define config.narrator_menu = True
init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1:
    style choice_vbox:
        xalign 0.5
        spacing gui.choice_spacing
        ypos 900
        yanchor 0.5
init -1:
    style choice_button is default:
        properties gui.button_properties("choice_button")
init -1:
    style choice_button_text is default:
        properties gui.button_text_properties("choice_button")
init -1:
    style quick_btn_style:
        color "#FFFFFF"
        hover_color "#fe9416"
        outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
        size 20
init -501:
    screen quick_menu():
        zorder 100
        if not phone_opened:
            mousearea area (0, 980, 720, 100) hovered SetVariable("quick_menu_hovered", True) unhovered SetVariable("quick_menu_hovered", False)
            if quick_menu > 0:
                if (quick_menu_hovered and quick_menu == 1) or (quick_menu == 2):
                    hbox:
                        style_prefix "quick"
                        xalign 0.0
                        yalign 1.0
                        if persistent.qm_back:
                            textbutton _("Powrót") action Rollback() text_style "quick_btn_style"
                        if persistent.qm_history:
                            textbutton _("Historia") action ShowMenu('history') text_style "quick_btn_style"
                        if persistent.qm_skip:
                            textbutton _("Pomiń") action Skip() text_style "quick_btn_style"
                        if persistent.qm_auto:
                            textbutton _("Autogra") action Preference("auto-forward", "toggle") text_style "quick_btn_style"
                        if persistent.qm_save:
                            textbutton _("Zapisz") action ShowMenu('save') text_style "quick_btn_style"
                        if persistent.qm_qsave:
                            textbutton _("S.Zapis") action QuickSave() text_style "quick_btn_style"
                        if persistent.qm_qload:
                            textbutton _("S.Wczyt") action QuickLoad() text_style "quick_btn_style"
                        if persistent.qm_prefs:
                            textbutton _("Preferencje") action ShowMenu('preferences') text_style "quick_btn_style"
                        if persistent.qm_guide and (steamConfig or nonPatreonConfig) and ((currentEpisode < 5 and renpy.loadable("walkthrough/season1/walkthrough_season1.rpyc")) or ((currentEpisode > 4 and renpy.loadable("walkthrough/season2/walkthrough_season2.rpyc")))):
                            textbutton _("Przewodnik") action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0),Function(show_guide_func)) text_style "quick_btn_style"
init -1:
    python:
        config.overlay_screens.append("quick_menu")

init -1 default quick_menu_hovered = False
init -1 default quick_menu = 2
init -1 default tmpMenu = 2
init -1 default tmpMenu2 = 2
init -1 default persistent.qm_back = True
init -1 default persistent.qm_history = True
init -1 default persistent.qm_skip = True
init -1 default persistent.qm_auto = True
init -1 default persistent.qm_save = True
init -1 default persistent.qm_qsave = True
init -1 default persistent.qm_qload = True
init -1 default persistent.qm_prefs = True
init -1 default persistent.qm_guide = True
init -1 style quick_button is default
init -1 style quick_button_text is button_text
init -1 define quick_button.choice_text_hover_color = '#0066cc'
init -1:
    style quick_button:
        properties gui.button_properties("quick_button")
init -1:
    style quick_button_text:
        properties gui.button_text_properties("quick_button")
init -501:
    screen navigation:
        vbox:
            xalign 0.01
            yalign 0.01
            spacing 5
            textbutton _("MENU GŁÓWNE") action MainMenu() text_style "custom_menu_style_header_btn"
            textbutton _("WYJDŹ") action Quit(confirm=not main_menu) text_style "custom_menu_style_header_btn"
        hbox:
            xalign 0.5
            yalign 0.08
            spacing 30
            textbutton _("ZAPISZ") action ShowMenu("save") text_style "custom_menu_style_header_btn"
            imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() yoffset -2
            textbutton _("WCZYTAJ") action ShowMenu("load") text_style "custom_menu_style_header_btn"
            imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() yoffset -2
            textbutton _("DŹWIĘK") action ShowMenu("audio") text_style "custom_menu_style_header_btn"
            imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() yoffset -2
            textbutton _("DIALOGI") action ShowMenu("dialogue") text_style "custom_menu_style_header_btn"
            imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() yoffset -2
            textbutton _("USTAWIENIA") action ShowMenu("preferences") text_style "custom_menu_style_header_btn"
init -1:
    style custom_menu_style_header_btn:
        color "#ffffff"
        insensitive_color "#808080"
        selected_color "#fe9416"
        hover_color "#fe9416"
        font "candara.ttf"
        size 35
init -1:
    style custom_menu_style_footer_btn:
        color "#ffffff"
        hover_color "#fe9416"
        selected_color "#fe9416"
        size 35
init -1:
    style custom_menu_style_text:
        color "#ffffff"
        font "candara.ttf"
        size 32
init -1:
    style custom_menu_style_text3:
        color "#00a0e6"
        font "candara.ttf"
        size 32
init -1:
    style custom_menu_style_text2:
        color "#636363"
        hover_color "#fe9416"
        font "candara.ttf"
        size 32
init -1:
    style custom_menu_style_text2_enabled:
        color "#fe9416"
        hover_color "#fe9416"
        font "candara.ttf"
        size 32
init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text
init -1:
    style navigation_button:
        size_group "navigation"
        properties gui.button_properties("navigation_button")
init -1:
    style navigation_button_text:
        properties gui.button_text_properties("navigation_button")
init 499:
    image spr_bg_s2:
        spr_mm_arr_s2[0][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[0][1]
        spr_mm_arr_s2[1][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[0][1]
        spr_mm_arr_s2[2][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[2][1]
        spr_mm_arr_s2[3][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[3][1]
        spr_mm_arr_s2[4][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[4][1]
        spr_mm_arr_s2[5][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[5][1]
        spr_mm_arr_s2[6][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[6][1]
        spr_mm_arr_s2[7][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[7][1]
        spr_mm_arr_s2[8][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[8][1]
        spr_mm_arr_s2[9][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[9][1]
        spr_mm_arr_s2[10][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[10][1]
        spr_mm_arr_s2[11][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[11][1]
        spr_mm_arr_s2[12][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[12][1]
        spr_mm_arr_s2[13][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[13][1]
        spr_mm_arr_s2[14][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[14][1]
        repeat
init 499:
    image spr_mid_s2:
        spr_mm_arr_s2[0][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[0][3]
        spr_mm_arr_s2[1][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[1][3]
        spr_mm_arr_s2[2][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[2][3]
        spr_mm_arr_s2[3][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[3][3]
        spr_mm_arr_s2[4][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[4][3]
        spr_mm_arr_s2[5][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[5][3]
        spr_mm_arr_s2[6][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[6][3]
        spr_mm_arr_s2[7][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[7][3]
        spr_mm_arr_s2[8][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[8][3]
        spr_mm_arr_s2[9][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[9][3]
        spr_mm_arr_s2[10][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[10][3]
        spr_mm_arr_s2[11][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[11][3]
        spr_mm_arr_s2[12][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[12][3]
        spr_mm_arr_s2[13][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[13][3]
        spr_mm_arr_s2[14][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[14][3]
        repeat
init 499:
    image spr_top_s2:
        spr_mm_arr_s2[0][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[0][5]
        spr_mm_arr_s2[1][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[1][5]
        spr_mm_arr_s2[2][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[2][5]
        spr_mm_arr_s2[3][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[3][5]
        spr_mm_arr_s2[4][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[4][5]
        spr_mm_arr_s2[5][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[5][5]
        spr_mm_arr_s2[6][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[6][5]
        spr_mm_arr_s2[7][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[7][5]
        spr_mm_arr_s2[8][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[8][5]
        spr_mm_arr_s2[9][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[9][5]
        spr_mm_arr_s2[10][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[10][5]
        spr_mm_arr_s2[11][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[11][5]
        spr_mm_arr_s2[12][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[12][5]
        spr_mm_arr_s2[13][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[13][5]
        spr_mm_arr_s2[14][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr_s2[14][5]
        repeat
init 499:
    image spr_bg:
        spr_mm_arr[0][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][1]
        spr_mm_arr[1][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][1]
        spr_mm_arr[2][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][1]
        spr_mm_arr[3][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][1]
        spr_mm_arr[4][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][1]
        spr_mm_arr[5][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][1]
        spr_mm_arr[6][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][1]
        spr_mm_arr[7][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][1]
        spr_mm_arr[8][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][1]
        spr_mm_arr[9][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][1]
        spr_mm_arr[10][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][1]
        spr_mm_arr[11][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][1]
        repeat
init 499:
    image spr_mid:
        spr_mm_arr[0][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][3]
        spr_mm_arr[1][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[1][3]
        spr_mm_arr[2][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][3]
        spr_mm_arr[3][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][3]
        spr_mm_arr[4][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][3]
        spr_mm_arr[5][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][3]
        spr_mm_arr[6][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][3]
        spr_mm_arr[7][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][3]
        spr_mm_arr[8][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][3]
        spr_mm_arr[9][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][3]
        spr_mm_arr[10][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][3]
        spr_mm_arr[11][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][3]
        repeat
init 499:
    image spr_top:
        spr_mm_arr[0][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][5]
        spr_mm_arr[1][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[1][5]
        spr_mm_arr[2][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][5]
        spr_mm_arr[3][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][5]
        spr_mm_arr[4][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][5]
        spr_mm_arr[5][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][5]
        spr_mm_arr[6][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][5]
        spr_mm_arr[7][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][5]
        spr_mm_arr[8][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][5]
        spr_mm_arr[9][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][5]
        spr_mm_arr[10][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][5]
        spr_mm_arr[11][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][5]
        repeat
init 499:
    image spr_bg_ep3:
        spr_mm_arr[0][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][1]
        spr_mm_arr[1][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][1]
        spr_mm_arr[2][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][1]
        spr_mm_arr[3][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][1]
        spr_mm_arr[4][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][1]
        spr_mm_arr[5][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][1]
        spr_mm_arr[6][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][1]
        spr_mm_arr[7][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][1]
        spr_mm_arr[8][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][1]
        spr_mm_arr[9][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][1]
        spr_mm_arr[10][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][1]
        spr_mm_arr[11][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][1]
        spr_mm_arr[12][0] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[12][1]
        repeat
init 499:
    image spr_mid_ep3:
        spr_mm_arr[0][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][3]
        spr_mm_arr[1][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[1][3]
        spr_mm_arr[2][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][3]
        spr_mm_arr[3][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][3]
        spr_mm_arr[4][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][3]
        spr_mm_arr[5][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][3]
        spr_mm_arr[6][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][3]
        spr_mm_arr[7][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][3]
        spr_mm_arr[8][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][3]
        spr_mm_arr[9][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][3]
        spr_mm_arr[10][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][3]
        spr_mm_arr[11][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][3]
        spr_mm_arr[12][2] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[12][3]
        repeat
init 499:
    image spr_top_ep3:
        spr_mm_arr[0][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[0][5]
        spr_mm_arr[1][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[1][5]
        spr_mm_arr[2][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[2][5]
        spr_mm_arr[3][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[3][5]
        spr_mm_arr[4][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[4][5]
        spr_mm_arr[5][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[5][5]
        spr_mm_arr[6][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[6][5]
        spr_mm_arr[7][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[7][5]
        spr_mm_arr[8][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[8][5]
        spr_mm_arr[9][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[9][5]
        spr_mm_arr[10][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[10][5]
        spr_mm_arr[11][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[11][5]
        spr_mm_arr[12][4] with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 10.0 zoom spr_mm_arr[12][5]
        repeat
init 499:
    image spr_title:
        "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
        pause 1.5
        "gui/main_menu_sprites/spr_badik.png" with Dissolve(1, alpha=True)
        pause 7
        "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
init 499:
    image spr_title2:
        "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
        pause 3.5
        "gui/main_menu_sprites/spr_badik2.png" with Dissolve(1, alpha=True)
        pause 5
        "gui/main_menu_sprites/spr_blank.png" with Dissolve(1, alpha=True)
init -1:
    style main_menu_btn_style:
        color "ffffff"
        hover_color "ffaa46"
init -501:
    screen main_menu():
        style_prefix "main_menu"
        tag menu
        if persistent.ep4_completed and renpy.loadable("season2/scripts/update5.rpyc"):
            add "spr_bg_s2"
            add "spr_mid_s2"
            add "spr_top_s2"
            add "gui/main_menu_sprites/spr_bottom_border.png"
            add "spr_title"
            add "spr_title2"
        else:
            add "spr_bg_ep3"
            add "spr_mid_ep3"
            add "spr_top_ep3"
            add "gui/main_menu_sprites/spr_bottom_border.png"
            add "spr_title"
            add "spr_title2"
        if not steamConfig and not nonPatreonConfig:
            hbox:
                spacing 50
                xalign 0.5
                yalign 0.97

                imagebutton focus_mask None idle Transform ("images/gui/buttons/new_game_btn.png") hover Transform ("images/gui/buttons/new_game_btn_hover.png") action (Start(), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/continue_btn.png") hover Transform ("images/gui/buttons/continue_btn_hover.png") action (ShowMenu("load"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/options_btn.png") hover Transform ("images/gui/buttons/options_btn_hover.png") action (ShowMenu("preferences"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                if menuGalleryOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Hide("menu_gallery"), Hide("music_credits"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Show("menu_gallery"), Hide("music_credits"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
                if musicCreditsOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Show("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
        elif nonPatreonConfig:
            hbox:
                spacing 50
                xalign 0.5
                yalign 0.97

                imagebutton focus_mask None idle Transform ("images/gui/buttons/new_game_btn.png") hover Transform ("images/gui/buttons/new_game_btn_hover.png") action (Start(), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/continue_btn.png") hover Transform ("images/gui/buttons/continue_btn_hover.png") action (ShowMenu("load"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/options_btn.png") hover Transform ("images/gui/buttons/options_btn_hover.png") action (ShowMenu("preferences"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                if menuGalleryOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Hide("menu_gallery"), Hide("music_credits"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Show("menu_gallery"), Hide("music_credits"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
                if musicCreditsOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Show("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/quit_btn.png") hover Transform ("images/gui/buttons/quit_btn_hover.png") action Quit()

        else:
            hbox:
                spacing 50
                xalign 0.5
                yalign 0.97

                imagebutton focus_mask None idle Transform ("images/gui/buttons/new_game_btn.png") hover Transform ("images/gui/buttons/new_game_btn_hover.png") action (Start(), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/continue_btn.png") hover Transform ("images/gui/buttons/continue_btn_hover.png") action (ShowMenu("load"), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/dlc_btn.png") hover Transform ("images/gui/buttons/dlc_btn_hover.png") action (ShowMenu("dlc"), Hide("music_credits"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/options_btn.png") hover Transform ("images/gui/buttons/options_btn_hover.png") action (ShowMenu("preferences"), Hide("music_credits"), Hide("dlc"), Hide("menu_gallery"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen", False), SetVariable("menuGalleryOpen",False))
                if menuGalleryOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Hide("menu_gallery"), Hide("music_credits"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/menu_gallery_btn.png") hover Transform ("images/gui/buttons/menu_gallery_btn_hover.png") action (Show("menu_gallery"), Hide("music_credits"), Hide("dlc"),SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",True))
                if musicCreditsOpen:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Hide("music_credits"), Hide("menu_gallery"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"), SetVariable("musicCreditsOpen",False), SetVariable("menuGalleryOpen",False))
                else:
                    imagebutton focus_mask None idle Transform ("images/gui/buttons/music_credits_btn.png") hover Transform ("images/gui/buttons/music_credits_btn_hover.png") action (Show("music_credits"), Hide("menu_gallery"), Hide("dlc"),Hide("menu_gallery_left"), Hide("menu_gallery_right"),SetVariable("musicCreditsOpen",True), SetVariable("menuGalleryOpen",False))
                imagebutton focus_mask None idle Transform ("images/gui/buttons/quit_btn.png") hover Transform ("images/gui/buttons/quit_btn_hover.png") action Quit()
        if steamConfig or nonPatreonConfig:
            vbox:
                xalign 0.03
                yalign 0.05
                spacing 10
                imagebutton idle Transform ("images/gui/buttons/discord_btn_new.png") hover Transform ("images/gui/buttons/discord_btn_new_hover.png") action OpenURL("https://discord.gg/kESb9Dh")
                if nonPatreonConfig:
                    imagebutton idle Transform ("images/gui/buttons/gog_btn.png") hover Transform ("images/gui/buttons/gog_btn_hover.png") action OpenURL("https://www.gog.com/game/being_a_dik")
        else:
            vbox:
                xalign 0.03
                yalign 0.08
                spacing 10
                imagebutton at mm_zoom idle Transform ("images/gui/buttons/patreon_btn_new.png") hover Transform ("images/gui/buttons/patreon_btn_new_hover.png") action OpenURL("https://www.patreon.com/DrPinkCake")
                imagebutton at mm_zoom idle Transform ("images/gui/buttons/discord_btn_new.png") hover Transform ("images/gui/buttons/discord_btn_new_hover.png") action OpenURL("https://discord.gg/KyCc5E4")
                imagebutton at mm_zoom idle Transform ("images/gui/buttons/steam_new_btn.png") hover Transform ("images/gui/buttons/steam_new_btn_hover.png") action OpenURL("https://store.steampowered.com/app/1126320/Being_a_DIK__Season_1/")
        imagebutton at twitter_zoom xalign 0.99 yalign 0.01 idle Transform ("images/gui/buttons/twitter_btn_new.png") hover Transform ("images/gui/buttons/twitter_btn_new_hover.png") action OpenURL("https://twitter.com/DrPinkCake")
        if not steamConfig and not nonPatreonConfig:
            vbox:
                style_prefix "help"
                yalign 0.999
                yoffset 30
                xalign 0.999
                spacing -40
                text _("{size=-15}{font=collegiate.ttf}{color=#ffffff}Wersja [config.version!t]{/color}{/font}{/size}\n")
        frame
init -1:
    transform mm_zoom:
        zoom 0.8
init -1:
    transform twitter_zoom:
        zoom 0.1
init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text
init -1:
    style main_menu_frame:
        yfill True
        xsize 420
init -1:
    style main_menu_vbox:
        xalign 1.0
        xmaximum 1200
        yalign 1.0
        xoffset -30
        yoffset -30
init -1:
    style main_menu_text:
        properties gui.text_properties("main_menu", accent=True)
init -1:
    style main_menu_title:
        properties gui.text_properties("title")
init -1:
    style main_menu_version:
        properties gui.text_properties("version")
init -501:
    screen game_menu(title, scroll=None, yinitial=0.0):
        style_prefix "game_menu"
        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background
        frame:
            style "game_menu_outer_frame"
            hbox:
                frame style "game_menu_navigation_frame"
                frame:
                    style "game_menu_content_frame"
                    if scroll == "viewport":
                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            vbox:
                                transclude
                    elif scroll == "vpgrid":
                        vpgrid:
                            cols 1
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True
                            side_yfill True
                            transclude
                    else:
                        transclude
        use navigation
        if _in_replay:
            vbox:
                xalign 0.01
                yalign 0.94
                textbutton _("KONIEC POWTÓRKI") action EndReplay(confirm=True) text_style "custom_menu_style_header_btn"
        vbox:
            xalign 0.01
            yalign 0.99
            textbutton _("POWRÓT") text_style "custom_menu_style_header_btn" action Return()
        label title
        if main_menu:
            key "game_menu" action ShowMenu("main_menu")
init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text
init -1:
    style game_menu_outer_frame:
        top_padding 180
        bottom_padding 45
        background "gui/overlay/game_menu.png"
init -1:
    style game_menu_navigation_frame:
        yfill True
        xsize 420
init -1:
    style game_menu_content_frame:
        right_margin 30
        top_margin 15
        left_margin 60
init -1:
    style game_menu_viewport:
        xsize 1380
init -1:
    style game_menu_vscrollbar:
        unscrollable gui.unscrollable
init -1:
    style game_menu_side:
        spacing 15
init -1:
    style game_menu_label:
        xpos 75
        ysize 180
init -1:
    style game_menu_label_text:
        color gui.accent_color
        yalign 0.5
        size gui.title_text_size
init -1:
    style return_button:
        xpos gui.navigation_xpos
        yalign 1.0
        yoffset -65
init -1 define gui.about = ""
init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text
init -1:
    style about_label_text:
        size gui.label_text_size
init -501:
    screen save():
        tag menu
        use file_slots(_("Save"))
        if FilePageName() == u'a' or FilePageName() == u'q':
            timer 0.001 action FilePage(1)
init -501:
    screen load():
        tag menu
        use file_slots(_("Load"))
init -1:
    style badik_input_style:
        background "#ffffff"
init -1:
    style badik_input_style2:
        color "#00a0e6"
        font "candara.ttf"
        size 20
init -501:
    screen file_slots(title):
        default page_name_value = FilePageNameInputValue(pattern=_("Strona {}"), auto=_("Automatyczne zapisy"), quick=_("Szybkie zapisy"))
        use game_menu(""):
            if title == "Save":
                textbutton _("Zapisz przedmioty") action (Function(savePersistentData), Show("saveMsg")) text_style "custom_menu_style_header_btn" xalign 0.0 yalign 1.0 xoffset -170 yoffset -20
            fixed:
                order_reverse True
                ypos -30
                button:
                    style "custom_menu_style_header_btn"
                    key_events True
                    xalign 0.99
                    yalign 0.99
                    yoffset 65
                    xoffset 20
                    action page_name_value.Toggle()
                    input style "custom_menu_style_header_btn" length 30 value page_name_value
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"
                    xpos -250
                    yalign 0.1
                    spacing gui.slot_spacing
                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        $ bad_chapter = FileJson(slot, "badik_chapter", empty="0", missing="-1")
                        $ startedChapter = FileJson(slot, "badik_started_chapter", empty="1", missing="1")
                        $ compatibleSave = FileJson(slot, "steamConfig", empty=False, missing=False)
                        button:
                            if bad_chapter == "0" or bad_chapter == "-1" or bad_chapter == "1":
                                if title == "Load" and compatibleSave==steamConfig:
                                    action (FileAction(slot))
                                elif title == "Save":
                                    action (FileAction(slot))
                                else:
                                    action NullAction()
                            elif startedChapter == "1" and bad_chapter == "2":
                                if title == "Load" and compatibleSave==steamConfig:
                                    action FileAction(slot)
                                elif title == "Save":
                                    action (FileAction(slot))
                                else:
                                    action NullAction()
                            else:
                                if title == "Save":
                                    action (FileAction(slot))
                                else:
                                    action NullAction()
                            vbox:
                                add FileScreenshot(slot) xalign 0.5
                                if bad_chapter == "0" or bad_chapter == "1" or bad_chapter == "-1":
                                    if compatibleSave==steamConfig or FileTimePL(slot) == "Puste miejsce":
                                        text FileTimePL(slot) style "slot_time_text" font "candara.ttf"
                                        $ sname_ok = True
                                        for c in FileSaveName(slot):
                                            if not c.isalnum() and c != " " and c != "_":
                                                $ sname_ok = False
                                        if sname_ok:
                                            text FileSaveName(slot) font "candara.ttf" size 21 xalign 0.5 yoffset 2 color "#00a0e6"
                                    else:
                                        text "{color=#ff0000}Niezgodny zapis{/color}" style "slot_time_text" yoffset -70
                                elif startedChapter == "1" and bad_chapter == "2":
                                    if compatibleSave==steamConfig or FileTimePL(slot) == "Puste miejsce":
                                        text FileTimePL(slot) style "slot_time_text" font "candara.ttf"
                                    else:
                                        text "{color=#ff0000}Niezgodny zapis{/color}" style "slot_time_text" font "candara.ttf" yoffset -70
                                else:
                                    text "{color=#ff0000}Niezgodny zapis{/color}" style "slot_time_text" font "candara.ttf" yoffset -70
                                $ bad_chapter = FileJson(slot, "badik_chapter", empty="1", missing="1")
                                if bad_chapter == "0" or bad_chapter == "2" or bad_chapter == "-1":
                                    $ sname_ok = True
                                    for c in FileSaveName(slot):
                                        if not c.isalnum() and c != " " and c != "_":
                                            $ sname_ok = False
                                    if sname_ok:
                                        text FileSaveName(slot) style "slot_name_text"
                                key "save_delete" action FileDelete(slot)
                if title == "Save":
                    hbox:
                        style_prefix "page"
                        yoffset 10
                        xoffset 20
                        xalign 0.99
                        yalign 0.99
                        spacing 10
                        text "{font=candara.ttf}{size=-5}Zapisz nazwę {/size}{/font}"
                        frame:
                            style "badik_input_style"
                            ymaximum 26
                            xmaximum 385
                            add "gui/preferences/custom_input_ol.png"
                            if mphone_current_input == "save_name":
                                input size 20 default "[save_name]" font "candara.ttf" color "#00a0e6" value VariableInputValue('save_name') length 23 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _1234567890" yoffset 4
                            else:
                                if save_name.strip() == "":
                                    textbutton "Kliknij, aby nadać nazwę zapisanej grze" text_style "badik_input_style2" action SetVariable("mphone_current_input","save_name") text_align 0.5 xalign 0.5 yoffset -1
                                else:
                                    textbutton "[save_name]" text_style "badik_input_style2" action SetVariable("mphone_current_input","save_name") text_align 0.5 xalign 0.5 yoffset -1
                vbox:
                    xalign 0.5
                    yalign 1.05
                    yoffset 30
                    xoffset -200
                    hbox:
                        xalign 0.5
                        style_prefix "page"
                        spacing gui.page_spacing
                        if config.has_autosave and title == "Load":
                            textbutton _("{font=Museo500.otf}{#auto_page}A{/font}") action FilePage("auto") text_style "custom_menu_style_footer_btn"
                        if config.has_quicksave and title == "Load":
                            textbutton _("{font=Museo500.otf}{#quick_page}Q{/font}") action FilePage("quick") text_style "custom_menu_style_footer_btn"
                        for page in range(1, 10):
                            textbutton "{font=Museo500.otf}[page]{/font}" action FilePage(page) text_style "custom_menu_style_footer_btn"
                    hbox:
                        xalign 0.5
                        spacing 25
                        if FilePageName() != u'a' and FilePageName() != u'q' and int(FilePageName()) > 1:
                            textbutton _("{font=candara.ttf}<<{/font}") action FilePage(max(int(FilePageName())-5,1)) text_style "custom_menu_style_footer_btn"
                        else:
                            textbutton _("{font=candara.ttf}<<{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
                        if FilePageName() != u'a' and FilePageName() != u'q' and int(FilePageName()) > 1:
                            textbutton _("{font=candara.ttf}<{/font}") action FilePagePrevious() text_style "custom_menu_style_footer_btn"
                        else:
                            textbutton _("{font=candara.ttf}<{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
                        if FilePageName() != u'a' and FilePageName() != u'q':
                            textbutton _("{font=candara.ttf}>{/font}") action FilePageNext() text_style "custom_menu_style_footer_btn"
                        else:
                            textbutton _("{font=candara.ttf}>{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
                        if FilePageName() != u'a' and FilePageName() != u'q':
                            textbutton _("{font=candara.ttf}>>{/font}") action FilePage(int(FilePageName())+5) text_style "custom_menu_style_footer_btn"
                        else:
                            textbutton _("{font=candara.ttf}>>{/font}") action NullAction() text_style "custom_menu_style_footer_btn"
init -1 default tmp_page = "1"
init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text
init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text
init -1:
    style page_label:
        ypadding 5
        xpadding 75
init -1:
    style page_label_text:
        hover_color gui.hover_color
        layout "subtitle"
        text_align 0.5
init -1:
    style page_button:
        properties gui.button_properties("page_button")
init -1:
    style page_button_text:
        properties gui.button_text_properties("page_button")
init -1:
    style slot_button:
        properties gui.button_properties("slot_button")
init -1:
    style slot_button_text:
        properties gui.button_text_properties("slot_button")
init -501:
    screen menu_gallery_left:
        modal False
        tag menu_gallery_left
        add "images/gui/episode_ol/menu_gallery_bg_rewards.png"
init -501:
    screen menu_gallery_right:
        modal False
        tag menu_gallery_right
        add "images/gui/episode_ol/menu_gallery_bg_scenes.png"
init -501:
    screen menu_gallery():
        modal False
        tag menu_gallery
        add "menu_gallery_bg"
        mousearea area (0, 0, 960, 937) hovered Show("menu_gallery_left") unhovered Hide("menu_gallery_left")
        mousearea area (961, 0, 1920, 937) hovered Show("menu_gallery_right") unhovered Hide("menu_gallery_right")
        imagebutton focus_mask True idle Transform("menu_gallery_button") hover Transform("menu_gallery_button") action (Hide("menu_gallery"), Hide("menu_gallery_right"), Hide("menu_gallery_left"), ShowMenu("rewards")) xpos 0 ypos 0
        imagebutton focus_mask True idle Transform("menu_gallery_button") hover Transform("menu_gallery_button") action (Hide("menu_gallery"), Hide("menu_gallery_right"), Hide("menu_gallery_left"), ShowMenu("scenes")) xpos 955 ypos 0
init -1:
    style my_bar:
        right_bar Frame("gui/slider/horizontal_idle_bar.png", gui.bar_borders, tile=gui.bar_tile)
        ysize gui.bar_size
        thumb "gui/slider/horizontal_[prefix_]thumb.png"
        left_bar Frame("gui/slider/horizontal_idle_bar_full.png", gui.bar_borders, tile=gui.bar_tile)
init -501:
    screen audio():
        tag menu
        use game_menu(_("")):
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                xoffset 70
                yoffset 100
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    label _("Głośność muzyki") text_style "custom_menu_style_text" xminimum 260 xmaximum 260
                    bar value Preference("music volume") style "my_bar"
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    label _("Głośność") text_style "custom_menu_style_text" xminimum 260 xmaximum 260
                    bar value Preference("sound volume") style "my_bar"
                vpgrid:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    cols 2
                    rows 2
                    label _("Wycisz wszystko") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        action Preference("all mute", "toggle")
                        xoffset -40
                        if preferences.get_mute("music") and preferences.get_mute("sfx"):
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                    label _("Powiadomienia telefoniczne") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        xoffset -40
                        if notifications:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                            action (SetVariable("notifications",False))
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                            action (SetVariable("notifications",True))
init -501:
    screen dialogue():
        tag menu
        use game_menu(_("")):
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                xoffset 70
                yoffset 40
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 10
                    label _("Strona cofania") text_style "custom_menu_style_text" yoffset 5
                    imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() xoffset -15
                    if preferences.desktop_rollback_side == "disable":
                        textbutton _("Wyłączone") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                        textbutton _("Lewy") action Preference("rollback side", "left") text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Prawy") action Preference("rollback side", "right") text_style "custom_menu_style_text2" xoffset -5
                    elif preferences.desktop_rollback_side == "left":
                        textbutton _("Wyłączone") action Preference("rollback side", "disable") text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Lewy") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                        textbutton _("Prawy") action Preference("rollback side", "right") text_style "custom_menu_style_text2" xoffset -5
                    else:
                        textbutton _("Wyłączone") action Preference("rollback side", "disable") text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Lewy") action Preference("rollback side", "left") text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Prawy") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    label _("Szybkość dialogów") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                    bar value Preference("text speed") style "my_bar" xoffset -20
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    label _("Czas auto-przejścia") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                    bar value Preference("auto-forward time") style "my_bar" xoffset -20
                hbox:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    label _("Widoczność pola tekstowego") text_style "custom_menu_style_text" xminimum 280 xmaximum 280
                    bar value FieldValue(persistent, "say_window_alpha", range=1.0, style="slider") style "my_bar" xoffset -20
                vpgrid:
                    xminimum 800
                    xmaximum 800
                    spacing 50
                    cols 2
                    rows 4
                    label _("Pole tekstowe") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        xoffset -40
                        if persistent.default_text_box_mode:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                            action (SetVariable("persistent.default_text_box_mode",False),Function(pick_style_centered))
                        else:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                            action (SetVariable("persistent.default_text_box_mode",True),Function(pick_style_default))
                    label _("Pomiń niewidoczny tekst") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        action Preference("skip", "toggle")
                        xoffset -40
                        if preferences.skip_unseen:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                    label _("Pomiń po wyborze") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        action Preference("after choices", "toggle")
                        xoffset -40
                        if preferences.skip_after_choices:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                    label _("Pomiń przejścia") text_style "custom_menu_style_text" xminimum 300
                    imagebutton:
                        action Preference("transitions", "toggle")
                        xoffset -40
                        if preferences.transitions:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
init -1:
    style qm_custom_style:
        color "#fe9416"
        yoffset 7
        font "candara.ttf"
        outlines [ (0, "#2b2b2b", 1, 1) ]
        xoffset 5
        size 23
init -1:
    style qm_custom_style_text_disabled:
        color "#636363"
        yoffset 7
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [ (0, "#2b2b2b", 1, 1) ]
        xoffset 5
        size 23
init -501:
    screen preferences():
        tag menu
        use game_menu(_("")):
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 50
                xoffset 70
                yoffset 20
                hbox:
                    xminimum 500
                    xmaximum 500
                    spacing 10
                    yoffset -20
                    label _("Tryb ekranu") text_style "custom_menu_style_text" yoffset 5
                    imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction()
                    if preferences.fullscreen:
                        textbutton _("Okno") action Preference("display", "window") text_style "custom_menu_style_text2"
                        textbutton _("Pełen ekran") action Preference("display", "fullscreen") text_style "custom_menu_style_text2_enabled"
                    else:
                        textbutton _("Okno") action Preference("display", "window") text_style "custom_menu_style_text2_enabled"
                        textbutton _("Pełen ekran") action Preference("display", "fullscreen") text_style "custom_menu_style_text2"
                vpgrid:
                    xminimum 800
                    xmaximum 800
                    spacing 75
                    cols 2
                    if renpy.loadable("season2/scripts/update6.rpyc"):
                        rows 4
                    else:
                        rows 3
                    label _("Porady") text_style "custom_menu_style_text" xminimum 500
                    imagebutton:
                        action (SetVariable("tutorials",not tutorials))
                        xoffset -40
                        if tutorials:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                    if renpy.loadable("season2/scripts/update6.rpyc"):
                        label _("Przycisk szybkiej podróży") text_style "custom_menu_style_text" xminimum 500
                        imagebutton:
                            action (SetVariable("persistent.map_fast_travel", not persistent.map_fast_travel))
                            xoffset -40
                            if persistent.map_fast_travel:
                                idle "gui/preferences/custom_menu_box_idle.png"
                                hover "gui/preferences/custom_menu_box_hover.png"
                            else:
                                idle "gui/preferences/custom_menu_box_empty_idle.png"
                                hover "gui/preferences/custom_menu_box_empty_hover.png"
                    if persistent.autosave:
                        label _("Autozapis (możliwe krótkie opóźnienia)") text_style "custom_menu_style_text" xminimum 500
                    else:
                        label _("Autozapis (bez skoków opóźnień)") text_style "custom_menu_style_text" xminimum 500
                    imagebutton:
                        xoffset -40
                        if persistent.autosave:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                            action (SetVariable("persistent.autosave",False),SetVariable("config.has_autosave",False))
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                            action (SetVariable("persistent.autosave",True),SetVariable("config.has_autosave",True))
                    label _("Obejrzyj prezentację Jill przy starcie") text_style "custom_menu_style_text" xminimum 500
                    imagebutton:
                        action (Function(resetIntro,not persistent.firstTimePlaying))
                        xoffset -40
                        if persistent.firstTimePlaying:
                            idle "gui/preferences/custom_menu_box_idle.png"
                            hover "gui/preferences/custom_menu_box_hover.png"
                        else:
                            idle "gui/preferences/custom_menu_box_empty_idle.png"
                            hover "gui/preferences/custom_menu_box_empty_hover.png"
                hbox:
                    xminimum 400
                    spacing 10
                    yoffset 20
                    label _("Przyciski z nagrodami") text_style "custom_menu_style_text" xminimum 350
                    imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() xoffset -10
                    if not persistent.rewards_screen_on_hover:
                        textbutton _("Włączone") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                        textbutton _("Ukryte") action SetVariable("persistent.rewards_screen_on_hover",True) text_style "custom_menu_style_text2" xoffset -5
                    else:
                        textbutton _("Włączone") action SetVariable("persistent.rewards_screen_on_hover",False) text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Ukryte") action NullAction() text_style "custom_menu_style_text2_enabled" xoffset -5
                hbox:
                    xminimum 400
                    spacing 10
                    yoffset 20
                    label _("Szybkie menu") text_style "custom_menu_style_text" xminimum 350
                    imagebutton idle "gui/preferences/custom_menu_separator.png" hover "gui/preferences/custom_menu_separator.png" action NullAction() xoffset -10
                    if quick_menu == 2:
                        textbutton _("Włączone") action SetVariable("quick_menu",2) text_style "custom_menu_style_text2_enabled" xoffset -5
                        textbutton _("Ukryte") action SetVariable("quick_menu",1) text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Wyłączone") action SetVariable("quick_menu",0) text_style "custom_menu_style_text2" xoffset -5
                    elif quick_menu == 1:
                        textbutton _("Włączone") action SetVariable("quick_menu",2) text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Ukryte") action SetVariable("quick_menu",1) text_style "custom_menu_style_text2_enabled" xoffset -5
                        textbutton _("Wyłączone") action SetVariable("quick_menu",0) text_style "custom_menu_style_text2" xoffset -5
                    else:
                        textbutton _("Włączone") action SetVariable("quick_menu",2) text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Ukryte") action SetVariable("quick_menu",1) text_style "custom_menu_style_text2" xoffset -5
                        textbutton _("Wyłączone") action SetVariable("quick_menu",0) text_style "custom_menu_style_text2_enabled" xoffset -5
                hbox:
                    spacing 20
                    text "Dostosuj szybkie menu" style "custom_menu_style_text"
                    if persistent.qm_back:
                        textbutton _("Powrót") action (SetVariable("persistent.qm_back",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Powrót") action (SetVariable("persistent.qm_back",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_history:
                        textbutton _("Historia") action (SetVariable("persistent.qm_history",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Historia") action (SetVariable("persistent.qm_history",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_skip:
                        textbutton _("Pomiń") action (SetVariable("persistent.qm_skip",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Pomiń") action (SetVariable("persistent.qm_skip",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_auto:
                        textbutton _("Autogra") action (SetVariable("persistent.qm_auto",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Autogra") action (SetVariable("persistent.qm_auto",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_save:
                        textbutton _("Zapisz") action (SetVariable("persistent.qm_save",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Zapisz") action (SetVariable("persistent.qm_save",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_qsave:
                        textbutton _("S.Zapis") action (SetVariable("persistent.qm_qsave",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("S.Zapis") action (SetVariable("persistent.qm_qsave",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_qload:
                        textbutton _("S.Wczyt") action (SetVariable("persistent.qm_qload",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("S.Wczyt") action (SetVariable("persistent.qm_qload",True)) text_style "qm_custom_style_text_disabled"
                    if persistent.qm_prefs:
                        textbutton _("Preferencje") action (SetVariable("persistent.qm_prefs",False)) text_style "qm_custom_style"
                    else:
                        textbutton _("Preferencje") action (SetVariable("persistent.qm_prefs",True)) text_style "qm_custom_style_text_disabled"
                    if (steamConfig or nonPatreonConfig) and ((currentEpisode < 5 and renpy.loadable("walkthrough/season1/walkthrough_season1.rpyc")) or ((currentEpisode > 4 and renpy.loadable("walkthrough/season2/walkthrough_season2.rpyc")))):
                        if persistent.qm_guide:
                            textbutton _("Przewodnik") action (SetVariable("persistent.qm_guide",False)) text_style "qm_custom_style"
                        else:
                            textbutton _("Przewodnik") action (SetVariable("persistent.qm_guide",True)) text_style "qm_custom_style_text_disabled"
init -1:
    style pref_custom_style:
        color "#858585"
        font "candara.ttf"
        size 30
init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox
init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox
init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox
init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox
init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text
init -1:
    style pref_label:
        bottom_margin 3
        top_margin gui.pref_spacing
init -1:
    style pref_label_text:
        yalign 1.0
init -1:
    style pref_vbox:
        xsize 338
init -1:
    style radio_vbox:
        spacing gui.pref_button_spacing
init -1:
    style radio_button:
        foreground "gui/button/check_[prefix_]foreground.png"
        properties gui.button_properties("radio_button")
init -1:
    style radio_button_text:
        properties gui.button_text_properties("radio_button")
init -1:
    style check_vbox:
        spacing gui.pref_button_spacing
init -1:
    style check_button:
        foreground "gui/button/check_[prefix_]foreground.png"
        properties gui.button_properties("check_button")
init -1:
    style check_button_custom_selected:
        foreground "gui/button/check_selected_foreground.png"
        properties gui.button_properties("check_button")
init -1:
    style check_button_custom_deselected:
        foreground "gui/button/check_foreground.png"
        properties gui.button_properties("check_button")
init -1:
    style check_button_text:
        properties gui.button_text_properties("check_button")
init -1:
    style slider_slider:
        xsize 525
init -1:
    style slider_button:
        properties gui.button_properties("slider_button")
        yalign 0.5
        left_margin 15
init -1:
    style slider_button_text:
        properties gui.button_text_properties("slider_button")
init -1:
    style slider_vbox:
        xsize 675
init -501:
    screen history():
        predict False
        tag menu
        use game_menu(_(""), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
            style_prefix "history"
            for h in _history_list:
                window:
                    fixed:
                        yfit True
                        if h.who:
                            label h.who:
                                style "history_name"
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what color "#FFFFFF" style "custom_menu_style_text" xmaximum 1050 xoffset 300 yoffset 4
            if not _history_list:
                label _("Historia rozmów jest pusta.") style "custom_menu_style_text"
init -1 define gui.history_allow_tags = set()
init -1 style history_window is empty
init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text
init -1 style history_text is gui_text
init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text
init -1:
    style history_window:
        ysize gui.history_height
        xfill True
init -1:
    style history_name:
        xpos gui.history_name_xpos
        xanchor gui.history_name_xalign
        ypos gui.history_name_ypos
        xsize gui.history_name_width
init -1:
    style history_name_text:
        min_width gui.history_name_width
        text_align gui.history_name_xalign
init -1:
    style history_text:
        xpos gui.history_text_xpos
        xanchor gui.history_text_xalign
        ypos gui.history_text_ypos
        text_align gui.history_text_xalign
        xsize gui.history_text_width
        min_width gui.history_text_width
        layout ("subtitle" if gui.history_text_xalign else "tex")
init -1:
    style history_label:
        xfill True
init -1:
    style history_label_text:
        xalign 0.5
init 499:
    image dlc_season1_btn:
        "season1_dlc_idle"
        on selected_idle:
            "season1_dlc_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "season1_dlc_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "season1_dlc_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "season1_dlc_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_season2_btn:
        "season2_dlc2_idle"
        on selected_idle:
            "season2_dlc2_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "season2_dlc2_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "season2_dlc2_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "season2_dlc2_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_season2_installed_btn:
        "season2_dlc_idle"
        on selected_idle:
            "season2_dlc_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "season2_dlc_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "season2_dlc_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "season2_dlc_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_guide_season1_btn:
        "guide_season1_dlc_idle2"
        on selected_idle:
            "guide_season1_dlc_idle2" with Dissolve(0.1, alpha=True)
        on idle:
            "guide_season1_dlc_idle2" with Dissolve(0.1, alpha=True)
        on hover:
            "guide_season1_dlc_hover2" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "guide_season1_dlc_hover2" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_guide_season1_installed_btn:
        "guide_season1_dlc_idle"
        on selected_idle:
            "guide_season1_dlc_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "guide_season1_dlc_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "guide_season1_dlc_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "guide_season1_dlc_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_guide_season2_btn3:
        "guide_season2_dlc_idle3"
        on selected_idle:
            "guide_season2_dlc_idle3" with Dissolve(0.1, alpha=True)
        on idle:
            "guide_season2_dlc_idle3" with Dissolve(0.1, alpha=True)
        on hover:
            "guide_season2_dlc_hover3" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "guide_season2_dlc_hover3" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_guide_season2_btn2:
        "guide_season2_dlc_idle2"
        on selected_idle:
            "guide_season2_dlc_idle2" with Dissolve(0.1, alpha=True)
        on idle:
            "guide_season2_dlc_idle2" with Dissolve(0.1, alpha=True)
        on hover:
            "guide_season2_dlc_hover2" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "guide_season2_dlc_hover2" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_guide_season2_installed_btn:
        "guide_season2_dlc_idle"
        on selected_idle:
            "guide_season2_dlc_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "guide_season2_dlc_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "guide_season2_dlc_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "guide_season2_dlc_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_seasonx_btn:
        "seasonx_dlc_idle"
        on selected_idle:
            "seasonx_dlc_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "seasonx_dlc_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "seasonx_dlc_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "seasonx_dlc_hover" with Dissolve(0.1, alpha=True)
init 499:
    image dlc_seasonX_btn:
        "seasonx_dlc_idle"
init 499:
    image al_game_btn:
        "al_game_idle"
        on selected_idle:
            "al_game_idle" with Dissolve(0.1, alpha=True)
        on idle:
            "al_game_idle" with Dissolve(0.1, alpha=True)
        on hover:
            "al_game_hover" with Dissolve(0.1, alpha=True)
        on selected_hover:
            "al_game_hover" with Dissolve(0.1, alpha=True)
init 499:
    image seasonx_dlc_idle:
        "seasonx_dlc_idle1" with Dissolve(1, alpha=True)
        pause 1
        "seasonx_dlc_idle2" with Dissolve(1, alpha=True)
        pause 1
        repeat
init 499:
    image seasonx_dlc_hover:
        "seasonx_dlc_hover1" with Dissolve(1, alpha=True)
        pause 1
        "seasonx_dlc_hover2" with Dissolve(1, alpha=True)
        pause 1
        repeat
init -1:
    style dlc_style_text:
        color "#ffffff"
        drop_shadow [(2, 2)]
        hover_color "#ffffff"
        font "Museo500.otf"
        drop_shadow_color "#000000"
        outlines [(1, "#000000", 0, 0)]
        hover_outlines [(1, "#000000", 0, 0)]
        size 50
init -1:
    style dlc_style_text_installed:
        color "#fe9416"
        drop_shadow [(2, 2)]
        hover_color "#fe9416"
        font "Museo500.otf"
        drop_shadow_color "#000000"
        outlines [(1, "#ffffff", 0, 0)]
        hover_outlines [(1, "#ffffff", 0, 0)]
        size 50
init -501:
    screen dlc():
        modal True
        tag dlc
        add "spr_bg_ep3"
        add "spr_mid_ep3"
        add "spr_top_ep3"
        add "dlc_bg"
        if game_is_ending:
            imagebutton xalign 0.98 yalign 0.02 idle "dlc_x_idle" hover "dlc_x_hover" action (Hide("dlc"), Return())
        else:
            imagebutton xalign 0.98 yalign 0.02 idle "dlc_x_idle" hover "dlc_x_hover" action (Hide("dlc"), Show("main_menu"))
        vpgrid:
            ypos 0.06
            draggable False
            mousewheel False
            scrollbars "horizontal"
            rows 1
            hbox:
                yalign 0.65
                xalign 0.5
                vbox:
                    button:
                        focus_mask True
                        action Function(activate_overlay_to_store_badik)
                        xalign 0.5
                        add "dlc_season1_btn"
                    text "Zainstalowane" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                vbox:
                    button:
                        focus_mask True
                        action Function(activate_overlay_to_store_badik_s1_guide)
                        xalign 0.5
                        if persistent.steam_owns_guide_s1:
                            add "dlc_guide_season1_installed_btn"
                        else:
                            add "dlc_guide_season1_btn"
                    if persistent.steam_owns_guide_s1 and renpy.loadable("walkthrough/season1/walkthrough_season1.rpyc"):
                        text "Zainstalowane" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                    elif persistent.steam_owns_guide_s1:
                        text "Nie zainstlowane" style "dlc_style_text" xalign 0.5 yoffset -60
                    else:
                        text "Dostępne teraz" style "dlc_style_text" xalign 0.5 yoffset -60
                if persistent.ep4_completed:
                    vbox:
                        button:
                            focus_mask True
                            action Function(activate_overlay_to_store_badik_s2)
                            xalign 0.5
                            if persistent.steam_owns_s2:
                                add "dlc_season2_installed_btn"
                            else:
                                add "dlc_season2_btn"
                        if persistent.steam_owns_s2 and renpy.loadable("season2/scripts/update5.rpyc"):
                            text "Zainstalowane" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                        elif persistent.steam_owns_s2:
                            text "Nie zainstlowane" style "dlc_style_text" xalign 0.5 yoffset -60
                        else:
                            text "Nie posiadane" style "dlc_style_text" xalign 0.5 yoffset -60
                    vbox:
                        button:
                            focus_mask True
                            action Function(activate_overlay_to_store_badik_s2_guide)
                            xalign 0.5
                            if persistent.steam_owns_guide_s2:
                                add "dlc_guide_season2_installed_btn"
                            else:
                                add "dlc_guide_season2_btn2"
                        if persistent.steam_owns_guide_s2 and renpy.loadable("walkthrough/season2/walkthrough_season2.rpyc"):
                            text "Zainstalowane" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                        elif persistent.steam_owns_guide_s2:
                            text "Nie zainstlowane" style "dlc_style_text" xalign 0.5 yoffset -60
                        else:
                            text "Nie posiadane" style "dlc_style_text" xalign 0.5 yoffset -60
                vbox:
                    button:
                        focus_mask True
                        action Function(activate_overlay_to_store_al)
                        xalign 0.5
                        add "al_game_btn"
                    if persistent.steam_owns_al:
                        text "W bibliotece" style "dlc_style_text_installed" xalign 0.5 yoffset -60
                    else:
                        text "Inne gry" style "dlc_style_text" xalign 0.5 yoffset -60
init -501:
    screen music_credits():
        modal False
        tag music_credits
        add "music_credits_bg"
        imagebutton focus_mask True idle Transform("music_credits_header") hover Transform("music_credits_header") action NullAction() xpos 570 ypos 10
        imagebutton focus_mask None idle Transform("license_btn") hover Transform("license_btn_hover") action OpenURL("https://creativecommons.org/licenses/by-sa/3.0/deed.pl") xpos 1100 ypos 93
        vpgrid:
            xpos 900
            yfill True
            xmaximum 600
            xminimum 600
            ypos 170
            ymaximum 750
            yminimum 750
            cols 4
            spacing 15
            draggable False
            mousewheel True
            scrollbars "vertical"
            side_xalign 0.502
            vbox:
                xalign 0
                yalign 0
                textbutton "A to Z guitars - Slow day blues" text_style "music_button_text2" action Play('music',"music/ep1/slow_day_blues.mp3", True)
                textbutton "Absentrealities - 03 Three's a crowd" text_style "music_button_text2" action Play('music',"music/ep1/threes_a_crowd.mp3", True)
                textbutton "Absentrealities - 04 Surf punk rock" text_style "music_button_text2" action Play('music',"music/ep1/surf_punk_rock.mp3", True)
                if renpy.loadable("season2/scripts/update6.rpyc"):
                    textbutton "Alexander Nakarada - Adventure" text_style "music_button_text2" action Play('music',"music/ep6/adventure2.mp3", True)
                    textbutton "Alexander Nakarada - Blood And Steel" text_style "music_button_text2" action Play('music',"music/ep6/blood_and_steel.mp3", True)
                textbutton "Alexander Nakarada - Freedom" text_style "music_button_text2" action Play('music',"music/ep2/freedom.mp3", True)
                textbutton "Alexander Nakarada - Journey of hope" text_style "music_button_text2" action Play('music',"music/ep2/journey_of_hope.mp3", True)
                textbutton "Alexander Nakarada - Jack the Lumberer" text_style "music_button_text2" action Play('music',"music/ep4/jack_the_lumberer.mp3", True)
                if renpy.loadable("season2/scripts/update6.rpyc"):
                    textbutton "Alexander Nakarada - Medieval Loop One" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_one.mp3", True)
                    textbutton "Alexander Nakarada - Medieval Loop Two" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_two.mp3", True)
                    textbutton "Alexander Nakarada - Medieval Loop Three" text_style "music_button_text2" action Play('music',"music/ep6/medieval_loop_three.mp3", True)
                textbutton "Alexander Nakarada - Reaching the sky" text_style "music_button_text2" action Play('music',"music/ep2/reaching_the_sky.mp3", True)
                textbutton "Alexander Nakarada - Relaxing ballad" text_style "music_button_text2" action Play('music',"music/ep2/relaxing_ballad.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "Alexander Nakarada - Rustic ballad" text_style "music_button_text2" action Play('music',"music/ep5/rustic_ballad.mp3", True)
                textbutton "Alexander Nakarada - Simple Ballad" text_style "music_button_text2" action Play('music',"music/ep2/simple_ballad.mp3", True)
                if renpy.loadable("season2/scripts/update6.rpyc"):
                    textbutton "Alexander Nakarada - Skeleton Keys" text_style "music_button_text2" action Play('music',"music/ep6/skeleton_keys.mp3", True)
                textbutton "Alexander Nakarada -  Spring in Russia" text_style "music_button_text2" action Play('music',"music/ep3/spring_in_russia.mp3", True)
                if renpy.loadable("season2/scripts/update6.rpyc"):
                    textbutton "Alexander Nakarada - The crown" text_style "music_button_text2" action Play('music',"music/ep6/the_crown.mp3", True)
                    textbutton "Alexander Nakarada - Uplifting ballad" text_style "music_button_text2" action Play('music',"music/ep6/uplifting_ballad.mp3", True)
                textbutton "Alexander Nakarada - Winter" text_style "music_button_text2" action Play('music',"music/ep2/winter.mp3", True)
                textbutton "Arlindo Detomi - STRYV Surge (Ivory Remix)" text_style "music_button_text2" action Play('music',"music/ep2/stryv.mp3", True)
                textbutton "AShamaluevMusic - Driving Rock" text_style "music_button_text2" action Play('music',"music/ep4/driving_rock.mp3", True)
                textbutton "AShamaluevMusic - Energetic" text_style "music_button_text2" action Play('music',"music/ep1/energetic.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "AShamaluevMusic - Inspiring Acoustic Guitar and Choir" text_style "music_button_text2" action Play('music',"music/ep5/inspiring.mp3", True)
                textbutton "AShamaluevMusic - Inspirational Piano Ambient" text_style "music_button_text2" action Play('music',"music/ep4/inspirational_piano_ambient.mp3", True)
                textbutton "AShamaluevMusic - Inspiring Acoustic" text_style "music_button_text2" action Play('music',"music/ep4/inspiring_acoustic.mp3", True)
                textbutton "AShamaluevMusic - Optimistic" text_style "music_button_text2" action Play('music',"music/ep4/optimistic.mp3", True)
                textbutton "AShamaluevMusic - Piano Cinematic" text_style "music_button_text2" action Play('music',"music/ep4/piano_cinematic.mp3", True)
                textbutton "AShamaluevMusic - Romantic Piano" text_style "music_button_text2" action Play('music',"music/ep4/romantic_piano.mp3", True)
                textbutton "Bare weed - Cosmos" text_style "music_button_text2" action Play('music',"music/ep4/cosmos.mp3", True)
                textbutton "Bellsmarie - Just Peachy (Original)" text_style "music_button_text2" action Play('music',"music/ep4/just_peachy.mp3", True)
                textbutton "Chriszornstudios - Art nouveau" text_style "music_button_text2" action Play('music',"music/ep1/art_nouveau.mp3", True)
                textbutton "Chrys Guth - Metal" text_style "music_button_text2" action Play('music',"music/ep2/metal.mp3", True)
                textbutton "Chukura - Lonely" text_style "music_button_text2" action Play('music',"music/ep1/lonely.mp3", True)
                if renpy.loadable("season2/scripts/update6.rpyc"):
                    textbutton "Daniel Couper - Wise old river (Acoustic version)" text_style "music_button_text2" action Play('music',"music/ep6/wise_old_river.mp3", True)
                    textbutton "DarkMoloko - Adventure" text_style "music_button_text2" action Play('music',"music/ep6/adventure.mp3", True)
                textbutton "Desert sharks - Feel bad" text_style "music_button_text2" action Play('music',"music/ep2/feel_bad.mp3", True)
                textbutton "Ds'Air - Jingle" text_style "music_button_text2" action Play('music',"music/ep2/jingle.mp3", True)
                textbutton "Emily Ventre - All of the pieces" text_style "music_button_text2" action Play('music',"music/ep4/all_of_the_pieces.mp3", True)
                textbutton "HodgeY - Unknown power" text_style "music_button_text2" action Play('music',"music/ep1/unknown_power.mp3", True)
                textbutton "Free Royalty Free Music - Metal" text_style "music_button_text2" action Play('music',"music/ep2/metal2.mp3", True)
                textbutton "Ghostrifter Official - Merry Bay" text_style "music_button_text2" action Play('music',"music/ep4/merry_bay.mp3", True)
                textbutton "Ghostrifter Official - Midnight Stroll" text_style "music_button_text2" action Play('music',"music/ep4/midnight_stroll.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "Ghostrifter Official - Morning Routine" text_style "music_button_text2" action Play('music',"music/ep7/morning_routine.mp3", True)
                    textbutton "Ghostrifter Official - Subtle Break" text_style "music_button_text2" action Play('music',"music/ep5/subtle_break.mp3", True)
                textbutton "Hyde - Acoustic/Pop/Rock/Alternative" text_style "music_button_text2" action Play('music',"music/ep1/apra_hyde.mp3", True)
                textbutton "Hyde - 60s & 70s Rock Fleetwood Mac Inspired Instrumental" text_style "music_button_text2" action Play('music',"music/ep4/fleetwood.mp3", True)
                textbutton "Hyde - Drum&Bass Rock Pendulum Inspired Instrumental" text_style "music_button_text2" action Play('music',"music/ep4/drum_bass.mp3", True)
                textbutton "Hyde - Mumford & Sons Inspired" text_style "music_button_text2" action Play('music',"music/ep1/mumford.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "Jantrax - Good old days" text_style "music_button_text2" action Play('music',"music/ep7/good_old_days.mp3", True)
                    textbutton "Jantrax - Rio" text_style "music_button_text2" action Play('music',"music/ep5/rio.mp3", True)
                    textbutton "Jantrax - Second chance" text_style "music_button_text2" action Play('music',"music/ep5/second_chance.mp3", True)
                textbutton "Jet Voon - Roads (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep3/roads.mp3", True)
                textbutton "Kevin Macleod - Anachronist" text_style "music_button_text2" action Play('music',"music/ep1/anachronist.mp3", True)
                textbutton "Kevin Macleod - First call" text_style "music_button_text2" action Play('music',"music/ep2/first_call.mp3", True)
                textbutton "Kevin Macleod - Fluffing a Duck" text_style "music_button_text2" action Play('music',"music/ep4/fluffing_a_duck.mp3", True)
                textbutton "Kevin Macleod - Marty Gots A Plan" text_style "music_button_text2" action Play('music',"music/ep2/marty.mp3", True)
                textbutton "Kevin Macleod - Octoblues" text_style "music_button_text2" action Play('music',"music/ep1/octoblues.mp3", True)
                textbutton "Kevin Macleod - Radio Martini" text_style "music_button_text2" action Play('music',"music/ep1/radio_martini.mp3", True)
                textbutton "Kevin Macleod - Sing along with Jim" text_style "music_button_text2" action Play('music',"music/ep3/sing_along_with_jim.mp3", True)
                textbutton "Kevin Macleod - Windswept" text_style "music_button_text2" action Play('music',"music/ep1/windswept.mp3", True)
                textbutton "Loudtech - Chill" text_style "music_button_text2" action Play('music',"music/ep3/chill.mp3", True)
                textbutton "Mason Carter Music - Acoustic" text_style "music_button_text2" action Play('music',"music/ep2/acoustic.mp3", True)
                textbutton "Melodic In Fusion - Don't count on me" text_style "music_button_text2" action Play('music',"music/ep1/dont_count_on_me.mp3", True)
                textbutton "Melodic In Fusion - EmptyV" text_style "music_button_text2" action Play('music',"music/ep1/emptyv.mp3", True)
                textbutton "Melodic In Fusion - This silence" text_style "music_button_text2" action Play('music',"music/ep1/this_silence.mp3", True)
                textbutton "Melodic In Fusion - Time goes by" text_style "music_button_text2" action Play('music',"music/ep1/time_goes_by.mp3", True)
                textbutton "Meizong - Fallen Colors (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/fallen_colors.mp3", True)
                textbutton "Meizong - Night Lights (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/night_lights.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "Meizong - No Comments (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep8/no_comments.mp3", True)
                textbutton "Meizong - Phate (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/phate.mp3", True)
                textbutton "Meizong - Raveyard (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep3/raveyard.mp3", True)
                textbutton "Meizong & Yeeflex - Reaching Halo" text_style "music_button_text2" action Play('music',"music/ep4/reaching_halo.mp3", True)
                textbutton "Meizong (Argofox) - Skyline (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep2/skyline.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "Meizong - Starfire (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep8/starfire.mp3", True)
                textbutton "Meizong - The heat (Original Mix)" text_style "music_button_text2" action Play('music',"music/ep4/the_heat.mp3", True)
                textbutton "Mironov Sound - Funk rock instrumental" text_style "music_button_text2" action Play('music',"music/ep1/funk_rock.mp3", True)
                textbutton "Nicolai Heidlas - By your side" text_style "music_button_text2" action Play('music',"music/ep2/by_your_side.mp3", True)
                textbutton "Nicolai Heidlas - Golden Alley" text_style "music_button_text2" action Play('music',"music/ep1/golden_alley.mp3", True)
                textbutton "Nicolai Heidlas - Let's Begin" text_style "music_button_text2" action Play('music',"music/ep3/lets_begin.mp3", True)
                textbutton "Nicolai Heidlas - Lost Souls" text_style "music_button_text2" action Play('music',"music/ep1/lost_souls.mp3", True)
                textbutton "Nicolai Heidlas - Never give up" text_style "music_button_text2" action Play('music',"music/ep1/never_give_up.mp3", True)
                textbutton "Nicolai Heidlas - Roadtrip" text_style "music_button_text2" action Play('music',"music/ep1/roadtrip.mp3", True)
                textbutton "Nicolai Heidlas - Rockin' Riff" text_style "music_button_text2" action Play('music',"music/ep2/rockin_riff.mp3", True)
                textbutton "Nicolai Heidlas - Someways" text_style "music_button_text2" action Play('music',"music/ep1/someways.mp3", True)
                textbutton "Nicolai Heidlas - Sunny acoustic rock" text_style "music_button_text2" action Play('music',"music/ep3/sunny_acoustic_rock.mp3", True)
                textbutton "Nicolai Heidlas - Wings" text_style "music_button_text2" action Play('music',"music/ep2/wings.mp3", True)
                textbutton "Nicolai Heidlas - Winter Sunshine" text_style "music_button_text2" action Play('music',"music/ep1/winter_sunshine.mp3", True)
                textbutton "Oskar Hill & Meizong - The Sound Of Summer" text_style "music_button_text2" action Play('music',"music/ep2/sound_of_summer.mp3", True)
                textbutton "PeriTune - Gentle theme2 Guitar" text_style "music_button_text2" action Play('music',"music/ep4/gentle_theme_guitar.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "PeriTune - Gentle theme2 MusicBox" text_style "music_button_text2" action Play('music',"music/ep7/musicbox.mp3", True)
                textbutton "PeriTune - Gentle theme2 Piano" text_style "music_button_text2" action Play('music',"music/ep3/gentle_theme_piano.mp3", True)
                textbutton "PeriTune - Guitar gentle" text_style "music_button_text2" action Play('music',"music/ep3/guitar_gentle.mp3", True)
                textbutton "PeriTune - Guitar melancholy" text_style "music_button_text2" action Play('music',"music/ep4/guitar_melancholy.mp3", True)
                textbutton "PeriTune - Guitar melancholy2" text_style "music_button_text2" action Play('music',"music/ep3/guitar_melancholy2.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "PeriTune - Suspense5" text_style "music_button_text2" action Play('music',"music/ep5/suspense5.mp3", True)
                textbutton "Punk rock mashed up - Classicals breakbeat" text_style "music_button_text2" action Play('music',"music/ep1/classicals_breakbeat.mp3", True)
                textbutton "Ryan Pollard TK-473 - Heavy" text_style "music_button_text2" action Play('music',"music/ep2/heavy.mp3", True)
                textbutton "Ryansyah R. Poetra - Credits" text_style "music_button_text2" action Play('music',"music/ep1/credits.mp3", True)
                textbutton "Sean Danielsen - Food chain" text_style "music_button_text2" action Play('music',"music/ep1/food_chain.mp3", True)
                textbutton "Silent Partner - Black box" text_style "music_button_text2" action Play('music',"music/ep3/black_box.mp3", True)
                textbutton "Silent Partner - DC love Go-Go" text_style "music_button_text2" action Play('music',"music/ep3/dc_love_go_go.mp3", True)
                textbutton "Silent Partner - Get back" text_style "music_button_text2" action Play('music',"music/ep3/get_back.mp3", True)
                textbutton "Silent Partner - Let her in" text_style "music_button_text2" action Play('music',"music/ep4/let_her_in.mp3", True)
                textbutton "Silent Partner - Scrapbook" text_style "music_button_text2" action Play('music',"music/ep1/scrapbook.mp3", True)
                textbutton "Silent Partner - Some obsession" text_style "music_button_text2" action Play('music',"music/ep3/some_obsession.mp3", True)
                textbutton "S Strong - Hot mustard" text_style "music_button_text2" action Play('music',"music/ep3/hot_mustard.mp3", True)
                textbutton "Summertime - My heart" text_style "music_button_text2" action Play('music',"music/ep1/my_heart.mp3", True)
                textbutton "Steven O'Brien - Slavic battle theme" text_style "music_button_text2" action Play('music',"music/ep3/slavic_battle_theme.mp3", True)
                if renpy.loadable("season2/scripts/update8.rpyc"):
                    textbutton "The Night - Down" text_style "music_button_text2" action Play('music',"music/ep5/down.mp3", True)
                    textbutton "The Night - Medicate me" text_style "music_button_text2" action Play('music',"music/ep5/medicate_me.mp3", True)
                textbutton "The Sisonpyh - Relax" text_style "music_button_text2" action Play('music',"music/ep4/relax.mp3", True)
                textbutton "TRow - Acoustic guitar arrangement" text_style "music_button_text2" action Play('music',"music/ep1/trow.mp3", True)
                textbutton "Valtteri Kujala - Your Smile" text_style "music_button_text2" action Play('music',"music/ep1/your_smile.mp3", True)
                textbutton "Wayne John Bradley - Fresh Air" text_style "music_button_text2" action Play('music',"music/ep1/fresh_air.mp3", True)
                textbutton "Wova - They Say" text_style "music_button_text2" action Play('music',"music/ep1/they_say.mp3", True)
init -501:
    screen help():
        tag menu
        default device = "keyboard"
        use game_menu(_(""), scroll="viewport"):
            style_prefix "help"
            vbox:
                spacing 23
                hbox:
                    textbutton _("Klawiatura") action SetScreenVariable("device", "keyboard") text_style "custom_menu_style_header_btn"
                    textbutton _("Mysz") action SetScreenVariable("device", "mouse") text_style "custom_menu_style_header_btn"
                    if GamepadExists():
                        textbutton _("Kontroler") action SetScreenVariable("device", "gamepad") text_style "custom_menu_style_header_btn"
                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help
init -1:
    style keyboard_help_style:
        color "#ffffff"
        font "candara.ttf"
init -501:
    screen keyboard_help():
        hbox:
            label _("Enter") text_style "custom_menu_style_text3"
            text _("Przesuwa okno dialogowe i aktywuje interfejs.") style "keyboard_help_style"
        hbox:
            label _("Spacja") text_style "custom_menu_style_text3"
            text _("Przesuwa dialog bez wybierania opcji.") style "keyboard_help_style"
        hbox:
            label _("Klawisze strzałek") text_style "custom_menu_style_text3"
            text _("Poruszaj się po interfejsie.") style "keyboard_help_style"
        hbox:
            label _("Escape") text_style "custom_menu_style_text3"
            text _("Dostęp do menu gry.") style "keyboard_help_style"
        hbox:
            label _("Ctrl") text_style "custom_menu_style_text3"
            text _("Pomija dialog podczas przytrzymania.") style "keyboard_help_style"
        hbox:
            label _("Tab") text_style "custom_menu_style_text3"
            text _("Włącza lub wyłącza pomijanie dialogów.") style "keyboard_help_style"
        hbox:
            label _("Page Up") text_style "custom_menu_style_text3"
            text _("Powrót do poprzedniego dialogu.") style "keyboard_help_style"
        hbox:
            label _("Page Down") text_style "custom_menu_style_text3"
            text _("Przechodzi do następnego dialogu.") style "keyboard_help_style"
        hbox:
            label "H" text_style "custom_menu_style_text3"
            text _("Ukrywa interfejs użytkownika.") style "keyboard_help_style"
        hbox:
            label "S" text_style "custom_menu_style_text3"
            text _("Wykonuje zrzut ekranu.") style "keyboard_help_style"
        hbox:
            label "V" text_style "custom_menu_style_text3"
            text _("Przełącznik wspomagający {a=https://www.renpy.org/l/voicing}samodzielne czytanie{/a}.") style "keyboard_help_style"
init -501:
    screen mouse_help():
        hbox:
            label _("Lewy przycisk") text_style "custom_menu_style_text3"
            text _("Przesuwa okno dialogowe i aktywuje interfejs.") style "keyboard_help_style"
        hbox:
            label _("Środkowy przycisk") text_style "custom_menu_style_text3"
            text _("Otwiera i zamyka telefon w grze.") style "keyboard_help_style"
        hbox:
            label _("Prawy przycisk") text_style "custom_menu_style_text3"
            text _("Dostęp do menu gry.") style "keyboard_help_style"
        hbox:
            label _("Kółko myszy w górę") text_style "custom_menu_style_text3"
            text _("Powrót do poprzedniego dialogu.") style "keyboard_help_style"
        hbox:
            label _("Kółko myszy w dół") text_style "custom_menu_style_text3"
            text _("Przechodzi do następnego dialogu.") style "keyboard_help_style"
init -501:
    screen gamepad_help():
        hbox:
            label _("Prawy spust (RT)") text_style "custom_menu_style_text3"
            text _("Przesuwa okno dialogowe i aktywuje interfejs.") style "keyboard_help_style"
        hbox:
            label _("Lewy spust (LT)\nLewy bumper (RB)") text_style "custom_menu_style_text3"
            text _("Powrót do poprzedniego dialogu.") style "keyboard_help_style"
        hbox:
            label _("Prawy bumper (RB)") text_style "custom_menu_style_text3"
            text _("Przechodzi do następnego dialogu.") style "keyboard_help_style"
        hbox:
            label _("Przyciski kierunkowe\nGałki analogowe") text_style "custom_menu_style_text3"
            text _("Poruszaj się po interfejsie.") style "keyboard_help_style"
        hbox:
            label _("Start, Przycisk główny") text_style "custom_menu_style_text3"
            text _("Dostęp do menu gry.") style "keyboard_help_style"
        hbox:
            label _("Przycisk Y") text_style "custom_menu_style_text3"
            text _("Ukrywa interfejs użytkownika.") style "keyboard_help_style"
        textbutton _("Kalibruj") action GamepadCalibrate() text_style "custom_menu_style_header_btn"
init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text
init -1:
    style help_button:
        properties gui.button_properties("help_button")
        xmargin 12
init -1:
    style help_button_text:
        properties gui.button_text_properties("help_button")
init -1:
    style help_label:
        right_padding 30
        xsize 375
init -1:
    style help_label_text:
        xalign 1.0
        text_align 1.0
        size gui.text_size
init -1:
    style custom_frame_style:
        idle_color "#ffffff"
        hover_color "#fe9416"
        font "candara.ttf"
        size 32
init -501:
    screen confirm(message, yes_action, no_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45
                label _(message) text_style "custom_menu_style_text" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 150
                    textbutton _("Tak") action yes_action text_style "custom_frame_style"
                    textbutton _("Nie") action no_action text_style "custom_frame_style"
        key "game_menu" action no_action
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1:
    style confirm_frame:
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
init -1:
    style confirm_prompt_text:
        layout "subtitle"
        text_align 0.5
init -1:
    style confirm_button:
        properties gui.button_properties("confirm_button")
init -1:
    style confirm_button_text:
        properties gui.button_text_properties("confirm_button")
init -501:
    screen skip_indicator():
        zorder 100
        style_prefix "skip"
        frame:
            xalign 0.
            yalign 0.03
            hbox:
                spacing 0
                imagebutton idle "gui/skip_dik.png" action NullAction() at delayed_blink(0.0, 1.0)
init -1:
    transform delayed_blink(delay, cycle):
        alpha .5
        pause delay
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text
init -1:
    style skip_frame:
        padding gui.skip_frame_borders.padding
        ypos gui.skip_ypos
init -1:
    style skip_text:
        size gui.notify_text_size
init -1:
    style skip_triangle:
        font "DejaVuSans.ttf"
init -501:
    screen notify(message):
        zorder 100
        style_prefix "notify"
        frame:
            at notify_appear
            text "[message!tq]"
        timer 3.25 action Hide('notify')
init -1:
    transform notify_appear:
        on hide:
            linear .5 alpha 0.0
        on show:
            alpha 0
            linear .25 alpha 1.0
init -1 style notify_frame is empty
init -1 style notify_text is gui_text
init -1:
    style notify_frame:
        padding gui.notify_frame_borders.padding
        ypos gui.notify_ypos
        background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
init -1:
    style notify_text:
        properties gui.text_properties("notify")
init -501:
    screen nvl(dialogue, items=None):
        window:
            style "nvl_window"
            vbox:
                spacing gui.nvl_spacing
                if gui.nvl_height:
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        use nvl_dialogue(dialogue)
                else:
                    use nvl_dialogue(dialogue)
                for i in items:
                    textbutton i.caption action i.action style "nvl_button"
        add SideImage() xalign 0.0 yalign 1.0
init -501:
    screen nvl_dialogue(dialogue):
        for d in dialogue:
            window:
                id d.window_id
                fixed:
                    yfit gui.nvl_height is None
                    if d.who is not None:
                        text d.who id d.who_id
                    text d.what id d.what_id
init -1 define config.nvl_list_length = gui.nvl_list_length
init -1 style nvl_window is default
init -1 style nvl_entry is default
init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue
init -1 style nvl_button is button
init -1 style nvl_button_text is button_text
init -1:
    style nvl_window:
        padding gui.nvl_borders.padding
        yfill True
        background "gui/nvl.png"
        xfill True
init -1:
    style nvl_entry:
        ysize gui.nvl_height
        xfill True
init -1:
    style nvl_label:
        yanchor 0.0
        xpos gui.nvl_name_xpos
        xanchor gui.nvl_name_xalign
        ypos gui.nvl_name_ypos
        text_align gui.nvl_name_xalign
        xsize gui.nvl_name_width
        min_width gui.nvl_name_width
init -1:
    style nvl_dialogue:
        xpos gui.nvl_text_xpos
        xanchor gui.nvl_text_xalign
        ypos gui.nvl_text_ypos
        text_align gui.nvl_text_xalign
        xsize gui.nvl_text_width
        min_width gui.nvl_text_width
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_thought:
        xpos gui.nvl_thought_xpos
        xanchor gui.nvl_thought_xalign
        ypos gui.nvl_thought_ypos
        text_align gui.nvl_thought_xalign
        xsize gui.nvl_thought_width
        min_width gui.nvl_thought_width
        layout ("subtitle" if gui.nvl_text_xalign else "tex")
init -1:
    style nvl_button:
        xpos gui.nvl_button_xpos
        xanchor gui.nvl_button_xalign
        properties gui.button_properties("nvl_button")
init -1:
    style nvl_button_text:
        properties gui.button_text_properties("nvl_button")
init -1:
    style pref_vbox:
        xsize 675
        variant "medium"
init -501:
    screen quick_menu():
        variant "touch"
        zorder 100
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Powrót") action Rollback()
            textbutton _("Pomić") action Skip()
            textbutton _("Autogra") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()
init -1:
    style window:
        background "gui/phone/textbox.png"
        variant "small"
init -1:
    style radio_button:
        foreground "gui/phone/button/check_[prefix_]foreground.png"
        variant "small"
init -1:
    style check_button:
        foreground "gui/phone/button/check_[prefix_]foreground.png"
        variant "small"
init -1:
    style nvl_window:
        background "gui/phone/nvl.png"
        variant "small"
init -1:
    style main_menu_frame:
        background "gui/phone/overlay/main_menu.png"
        variant "small"
init -1:
    style game_menu_outer_frame:
        background "gui/phone/overlay/game_menu.png"
        variant "small"
init -1:
    style game_menu_navigation_frame:
        xsize 510
        variant "small"
init -1:
    style game_menu_content_frame:
        top_margin 0
        variant "small"
init -1:
    style pref_vbox:
        xsize 600
        variant "small"
init -1:
    style bar:
        left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
        ysize gui.bar_size
        right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
        variant "small"
init -1:
    style vbar:
        bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
        top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        xsize gui.bar_size
        variant "small"
init -1:
    style scrollbar:
        ysize gui.scrollbar_size
        base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
        variant "small"
init -1:
    style vscrollbar:
        base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        xsize gui.scrollbar_size
        thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        variant "small"
init -1:
    style slider:
        ysize gui.slider_size
        base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
        thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"
        variant "small"
init -1:
    style vslider:
        base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        xsize gui.slider_size
        thumb "gui/phone/slider/vertical_[prefix_]thumb.png"
        variant "small"
init -1:
    style slider_pref_vbox:
        xsize None
        variant "small"
init -1:
    style slider_pref_slider:
        xsize 900
        variant "small"
init -501:
    screen phone_screen_scold:
        modal False
        tag phone_screen
        imagebutton at show_hide_dissolve idle "phone_proximity_btn" hover "phone_proximity_btn_hover" xalign 0.021 yalign 0.022 action NullAction()
        if ep2_CathyScoldScreen:
            imagebutton at show_hide_dissolve idle "phone_btn" hover "phone_btn_hover" xalign 0.02 yalign 0.02 action Jump("ep2_scold_label_main")
init -501:
    screen phone_screen:
        modal False
        tag phone_screen
        if not _in_replay and currentEpisode < 7:
            imagebutton at show_hide_dissolve idle "phone_proximity_btn" hover "phone_proximity_btn_hover" xalign 0.021 yalign 0.022 action NullAction()
            imagebutton at show_hide_dissolve idle "phone_btn" hover "phone_btn_hover" xalign 0.02 yalign 0.02 action (SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Show("phone_menu"))
            key "mouseup_2" action (SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Show("phone_menu"))
            if phone_call_enabled:
                imagebutton at show_hide_dissolve idle "skip_song_proximity_button" hover "skip_song_proximity_button_hover" xalign 0.99 yalign 0.01 action NullAction()
                imagebutton at show_hide_dissolve idle "skip_song_button" hover "skip_song_button_hover" xalign 0.99 yalign 0.01 action Function(skipSongFunc)
init -501:
    screen srmsg:
        modal False
        tag srmsg
        timer 3 action Hide('srmsg')
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Odblokowałeś specjalny render!{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -501:
    screen skillmsg:
        modal False
        tag skillmsg
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Twoje umiejętności zostały zaktualizowane.{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -501:
    screen specialmsg:
        modal False
        tag specialmsg
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        text "{size=+3}{font=collegiate.ttf}{color=#ffffff}[specialMessage]{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -1:
    style affinitymsgstyle:
        color "#fe9416"
        font "cabin-regular.ttf"
        outlines [(2, "#ffffff", 0, 0)]
        size 40
init -501:
    screen affinitymsg:
        modal False
        tag affinitymsg
        timer 2 action Hide('affinitymsg')
        text "[specialMessage]" style "affinitymsgstyle" at show_hide_dissolve xalign 0.5 yalign 0.16
init -501:
    screen moneymsg:
        modal False
        tag moneymsg
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        if money == 5:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 4:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 3:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 2:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 1:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        else:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}Brak pieniędzy{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -501:
    screen scoremsg:
        modal False
        tag toprightmsg
        timer 3 action Hide('scoremsg')
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Twój wynik DIK został zaktualizowany!{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -1:
    transform show_hide_dissolve:
        on hide:
            alpha 1.0
            linear 1.0 alpha .0
        on show:
            alpha .0
            linear 1.0 alpha 1.0
init -501:
    screen majorChoiceScale:
        modal False
        tag majorChoiceScale
        if not permanent_affinity:
            if not episodeIsEnding:
                add "dikscale_white_bg"
            if dpenalty < 4 and cpenalty < 20:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.236 yalign 0.0 action NullAction()
            if dpenalty < 8 and cpenalty < 16:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.36825 yalign 0.0 action NullAction()
            if dpenalty < 11 and cpenalty < 13:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.4675 yalign 0.0 action NullAction()
            if dpenalty < 13 and cpenalty < 11:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.5325 yalign 0.0 action NullAction()
            if dpenalty < 16 and cpenalty < 8:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.63175 yalign 0.0 action NullAction()
            if dpenalty < 20 and cpenalty < 4:
                imagebutton at show_hide_dissolve idle "dik_bar" xalign 0.764 yalign 0.0 action NullAction()
            if dpenalty < 4 and cpenalty < 24:
                imagebutton at show_hide_dissolve idle "massivedik" xalign 0.14 yalign 0.05 action NullAction()
            if dpenalty < 8 and cpenalty < 20:
                imagebutton at show_hide_dissolve idle "hugedik" xalign 0.29 yalign 0.05 action NullAction()
            if dpenalty < 11 and cpenalty < 16:
                imagebutton at show_hide_dissolve idle "dik" xalign 0.413 yalign 0.05 action NullAction()
            if dpenalty < 16 and cpenalty < 11:
                imagebutton at show_hide_dissolve idle "chick" xalign 0.588 yalign 0.05 action NullAction()
            if dpenalty < 20 and cpenalty < 8:
                imagebutton at show_hide_dissolve idle "hugechick" xalign 0.71 yalign 0.05 action NullAction()
            if dpenalty < 24 and cpenalty < 4:
                imagebutton at show_hide_dissolve idle "massivechick" xalign 0.86 yalign 0.05 action NullAction()
            if dpenalty == 0 and cpenalty < 24:
                imagebutton at show_hide_dissolve idle "d0" xalign 0.112 yalign 0.0 action NullAction()
            if dpenalty < 2 and cpenalty < 23:
                imagebutton at show_hide_dissolve idle "d1" xalign 0.143 yalign 0.0 action NullAction()
            if dpenalty < 3 and cpenalty < 22:
                imagebutton at show_hide_dissolve idle "d2" xalign 0.177 yalign 0.0 action NullAction()
            if dpenalty < 4 and cpenalty < 21:
                imagebutton at show_hide_dissolve idle "d3" xalign 0.211 yalign 0.0 action NullAction()
            if dpenalty < 5 and cpenalty < 20:
                imagebutton at show_hide_dissolve idle "d4" xalign 0.245 yalign 0.0 action NullAction()
            if dpenalty < 6 and cpenalty < 19:
                imagebutton at show_hide_dissolve idle "d5" xalign 0.279 yalign 0.0 action NullAction()
            if dpenalty < 7 and cpenalty < 18:
                imagebutton at show_hide_dissolve idle "d6" xalign 0.313 yalign 0.0 action NullAction()
            if dpenalty < 8 and cpenalty < 17:
                imagebutton at show_hide_dissolve idle "d7" xalign 0.347 yalign 0.0 action NullAction()
            if dpenalty < 9 and cpenalty < 16:
                imagebutton at show_hide_dissolve idle "d8" xalign 0.381 yalign 0.0 action NullAction()
            if dpenalty < 10 and cpenalty < 15:
                imagebutton at show_hide_dissolve idle "d9" xalign 0.415 yalign 0.0 action NullAction()
            if dpenalty < 11 and cpenalty < 14:
                imagebutton at show_hide_dissolve idle "d10" xalign 0.449 yalign 0.0 action NullAction()
            if dpenalty < 12 and cpenalty < 13:
                imagebutton at show_hide_dissolve idle "d11" xalign 0.483 yalign 0.0 action NullAction()
            if dpenalty < 13 and cpenalty < 12:
                imagebutton at show_hide_dissolve idle "c11" xalign 0.517 yalign 0.0 action NullAction()
            if dpenalty < 14 and cpenalty < 11:
                imagebutton at show_hide_dissolve idle "c10" xalign 0.551 yalign 0.0 action NullAction()
            if dpenalty < 15 and cpenalty < 10:
                imagebutton at show_hide_dissolve idle "c9" xalign 0.585 yalign 0.0 action NullAction()
            if dpenalty < 16 and cpenalty < 9:
                imagebutton at show_hide_dissolve idle "c8" xalign 0.619 yalign 0.0 action NullAction()
            if dpenalty < 17 and cpenalty < 8:
                imagebutton at show_hide_dissolve idle "c7" xalign 0.653 yalign 0.0 action NullAction()
            if dpenalty < 18 and cpenalty < 7:
                imagebutton at show_hide_dissolve idle "c6" xalign 0.687 yalign 0.0 action NullAction()
            if dpenalty < 19 and cpenalty < 6:
                imagebutton at show_hide_dissolve idle "c5" xalign 0.721 yalign 0.0 action NullAction()
            if dpenalty < 20 and cpenalty < 5:
                imagebutton at show_hide_dissolve idle "c4" xalign 0.755 yalign 0.0 action NullAction()
            if dpenalty < 21 and cpenalty < 4:
                imagebutton at show_hide_dissolve idle "c3" xalign 0.789 yalign 0.0 action NullAction()
            if dpenalty < 22 and cpenalty < 3:
                imagebutton at show_hide_dissolve idle "c2" xalign 0.823 yalign 0.0 action NullAction()
            if dpenalty < 23 and cpenalty < 2:
                imagebutton at show_hide_dissolve idle "c1" xalign 0.857 yalign 0.0 action NullAction()
            if dpenalty < 24 and cpenalty == 0:
                imagebutton at show_hide_dissolve idle "c0" xalign 0.89 yalign 0.0 action NullAction()
init 499:
    image spr_ending_ep1:
        "ep1_maya3_freeroam_bg3" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep2:
        "ep1_maya_freeroam_bg3b" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep3:
        "ep3_maya2_freeroam_bg3b" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep4_sage:
        "ep4_sage_freeroam_dorm" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep4_derek:
        "ep4_derek_freeroam2_bg" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep4_isabella:
        "ep4_fr_bella_longue" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep5_dik:
        "ep5_ending_screen" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep6_dik:
        "ep6_freeroam_diks_libraryb_nocard" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep7_dik:
        "ep7_freeroam_diks_library2" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init 499:
    image spr_ending_ep8_dik:
        "ep8_final_diks_library2" with Dissolve(0.2, alpha=True)
        zoom 1.0
        xalign 0.0 yalign 0.0
        linear 15.0 zoom 1.08
        linear 15.0 zoom 1.00
        repeat
init -501:
    screen endingScreen:
        modal False
        tag endingScreen
        $ episodeIsEnding = True
        if currentEpisode == 1:
            add "spr_ending_ep1"
        elif currentEpisode == 2:
            add "spr_ending_ep2"
        elif currentEpisode == 3:
            add "spr_ending_ep3"
        elif currentEpisode == 4:
            if ep3_choseDerek:
                add "spr_ending_ep4_derek"
            elif ep3_choseSage:
                add "spr_ending_ep4_sage"
            else:
                add "spr_ending_ep4_isabella"
        elif currentEpisode == 5:
            add "spr_ending_ep5_dik"
        elif currentEpisode == 6:
            add "spr_ending_ep6_dik"
        elif currentEpisode == 7:
            add "spr_ending_ep7_dik"
        elif currentEpisode == 8:
            add "spr_ending_ep8_dik"
        if permanent_affinity:
            add "report_box_ol" yoffset -100
        else:
            add "report_box_ol"
        if not permanent_affinity:
            if dtype == 3:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.155 yalign 0.18 action NullAction()
            elif dtype == 2:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.288 yalign 0.18 action NullAction()
            elif dtype == 1:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.412 yalign 0.18 action NullAction()
            elif dtype == 0:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.5 yalign 0.18 action NullAction()
            elif dtype == -1:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.588 yalign 0.18 action NullAction()
            elif dtype == -2:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.71 yalign 0.18 action NullAction()
            elif dtype == -3:
                imagebutton at show_hide_dissolve idle "scale_arrow" xalign 0.845 yalign 0.18 action NullAction()
        if currentEpisode >= 7:
            if money > 0:
                $ mny = "{color=#36ca2b}$%d{/color}" % money
            else:
                $ mny = "{color=#36ca2b}Brak pieniędzy{/color}"
        else:
            if money == 5:
                $ mny = "{color=#36ca2b}$$$$${/color}"
            elif money == 4:
                $ mny = "{color=#36ca2b}$$$${/color}"
            elif money == 3:
                $ mny = "{color=#36ca2b}$$${/color}"
            elif money == 2:
                $ mny = "{color=#36ca2b}$${/color}"
            elif money == 1:
                $ mny = "{color=#36ca2b}${/color}"
            elif money == 0:
                $ mny = "{color=#36ca2b}Brak pieniędzy{/color}"
        $ totalPassedClasses = passedEnglish + passedMath + passedGender
        $ totalPerfectClasses = maxedEnglish + maxedMath + maxedGender
        $ totalFailedClasses = failedEnglish + failedMath + failedGender
        if affinity == "DIK":
            $ affinityStr = "{color=#fe9416}{font=collegiate.ttf}DIK{/font}{/color} affinity"
        elif affinity == "CHICK":
            $ affinityStr = "{color=#00a0e6}{font=collegiate.ttf}SIMP{/font}{/color} affinity"
        else:
            $ affinityStr = "{color=#91f360}{font=collegiate.ttf}Neutral{/font}{/color} affinity"
        if currentEpisode < 6:
            if permanent_affinity:
                if minigames:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nStała ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]\nZaliczone zajęcia: [totalPassedClasses]\nZajęcia na piątkę: [totalPerfectClasses]\nNiezaliczone zajęcia: [totalFailedClasses]{/size}{/font}" at show_hide_dissolve yalign 0.75 xalign 0.98 text_align 0.0 yoffset -100 size 40 hover_outlines [(1, "#660066", 0, 0)]
                else:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nStała ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]{/size}{/font}" at show_hide_dissolve yalign 0.6 xalign 0.98 text_align 0.0 yoffset -100 size 40 hover_outlines [(1, "#660066", 0, 0)]
            else:
                if minigames:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nObecna ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]\nZaliczone zajęcia: [totalPassedClasses]\nZajęcia na piątkę: [totalPerfectClasses]\nNiezaliczone zajęcia: [totalFailedClasses]{/size}{/font}" at show_hide_dissolve yalign 0.75 xalign 0.98 text_align 0.0 size 40 hover_outlines [(1, "#660066", 0, 0)]
                else:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nObecna ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]{/size}{/font}" at show_hide_dissolve yalign 0.6 xalign 0.98 text_align 0.0 size 40 hover_outlines [(1, "#660066", 0, 0)]
        else:
            if minigames:
                $ totalPassedClasses = passedEnglish + passedMath + passedGender
                $ totalPerfectClasses = maxedEnglish + maxedMath + maxedGender + maxedMath_s2 + maxedEnglish_s2 + maxedGender_s2
                $ totalFailedClasses = failedEnglish + failedMath + failedGender
            if permanent_affinity:
                if minigames:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nStała ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]\nZaliczone zajęcia: [totalPassedClasses]\nZajęcia na piątkę: [totalPerfectClasses]\nNiezaliczone zajęcia: [totalFailedClasses]\nWynik rezydencji: {color=#ffed00}[mansion_score]{/color}\nPieniądze rezydencji: {color=#fe9416}$[mansion_money]{/color}{/size}{/font}" at show_hide_dissolve yalign 0.76 xalign 0.94 text_align 0.0 yoffset -100 size 33 hover_outlines [(1, "#660066", 0, 0)]
                else:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nStała ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]{/size}{/font}" at show_hide_dissolve yalign 0.6 xalign 0.98 text_align 0.0 yoffset -100 size 38 hover_outlines [(1, "#660066", 0, 0)]
            else:
                if minigames:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nObecna ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]\nZaliczone zajęcia: [totalPassedClasses]\nZajęcia na piątkę: [totalPerfectClasses]\nNiezaliczone zajęcia: [totalFailedClasses]\nWynik rezydencji: {color=#ffed00}[mansion_score]{/color}\nPieniądze rezydencji: {color=#fe9416}$[mansion_money]{/color}{/size}{/font}" at show_hide_dissolve yalign 0.76 xalign 0.94 text_align 0.0 size 33 hover_outlines [(1, "#660066", 0, 0)]
                else:
                    text "{font=candara.ttf}{size=+10}{color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wynik: [dik]\nObecna ranga: [affinityStr]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} wyborów: [cpenalty]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} wyborów: [dpenalty]\nLiczba {color=#fe9416}{size=+3}{font=collegiate.ttf}DIK{/font}{/size}{/color} akcji: [totalDikChoices]\nLiczba {color=#00a0e6}{size=+3}{font=collegiate.ttf}Simp{/font}{/size}{/color} akcji: [totalChickChoices]\nPieniądze: [mny]{/size}{/font}" at show_hide_dissolve yalign 0.6 xalign 0.98 text_align 0.0 size 38 hover_outlines [(1, "#660066", 0, 0)]
init -501:
    screen endingGirlScreen:
        modal True
        tag endingGirlScreen
        imagebutton at show_hide_dissolve idle "bios_avatar_josy" xalign 0.1 yalign 0.05 action NullAction()
        text "{size=+10}{color=#ff1c63}{font=Redressed.ttf}Josy{/font}{/color}{/size}" at show_hide_dissolve xalign 0.13 yalign 0.23 text_align 0.5
        $ josyPercentage = (int) (josyScore * 100.0)
        $ josyAlignValue = 0.55 - 0.214 * josyScore
        imagebutton at show_hide_dissolve idle "girl_arrow" xalign 0.082 yalign josyAlignValue action NullAction()
        if josyScore == 1.0:
            imagebutton at show_hide_dissolve idle "josy_temperature_100" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore >= 0.8:
            imagebutton at show_hide_dissolve idle "josy_temperature_85" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore >= 0.7:
            imagebutton at show_hide_dissolve idle "josy_temperature_75" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore >= 0.6:
            imagebutton at show_hide_dissolve idle "josy_temperature_65" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore >= 0.45:
            imagebutton at show_hide_dissolve idle "josy_temperature_50" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore >= 0.3:
            imagebutton at show_hide_dissolve idle "josy_temperature_35" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > 0.2:
            imagebutton at show_hide_dissolve idle "josy_temperature_25" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > 0.1:
            imagebutton at show_hide_dissolve idle "josy_temperature_15" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.1:
            imagebutton at show_hide_dissolve idle "josy_temperature_0" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.2:
            imagebutton at show_hide_dissolve idle "josy_temperature_m15" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.3:
            imagebutton at show_hide_dissolve idle "josy_temperature_m25" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.45:
            imagebutton at show_hide_dissolve idle "josy_temperature_m35" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.6:
            imagebutton at show_hide_dissolve idle "josy_temperature_m50" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.7:
            imagebutton at show_hide_dissolve idle "josy_temperature_m65" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -0.8:
            imagebutton at show_hide_dissolve idle "josy_temperature_m75" xalign 0.112 yalign 0.78 action NullAction()
        elif josyScore > -1:
            imagebutton at show_hide_dissolve idle "josy_temperature_m85" xalign 0.112 yalign 0.78 action NullAction()
        else:
            imagebutton at show_hide_dissolve idle "josy_temperature_m100" xalign 0.112 yalign 0.78 action NullAction()
        text "{color=#000000}[josyPercentage]%{/color}" at show_hide_dissolve xalign 0.125 yalign 0.855
        imagebutton at show_hide_dissolve idle "bios_avatar_maya" xalign 0.3 yalign 0.05 action NullAction()
        text "{size=+10}{color=#a7f442}{font=Redressed.ttf}Maya{/font}{/color}{/size}" at show_hide_dissolve xalign 0.31 yalign 0.23 text_align 0.5
        $ mayaPercentage = (int) (mayaScore * 100.0)
        $ mayaAlignValue = 0.55 - 0.214 * mayaScore
        imagebutton at show_hide_dissolve idle "girl_arrow" xalign 0.263 yalign mayaAlignValue action NullAction()
        if mayaScore == 1.0:
            imagebutton at show_hide_dissolve idle "maya_temperature_100" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore >= 0.8:
            imagebutton at show_hide_dissolve idle "maya_temperature_85" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore >= 0.7:
            imagebutton at show_hide_dissolve idle "maya_temperature_75" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore >= 0.6:
            imagebutton at show_hide_dissolve idle "maya_temperature_65" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore >= 0.45:
            imagebutton at show_hide_dissolve idle "maya_temperature_50" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore >= 0.3:
            imagebutton at show_hide_dissolve idle "maya_temperature_35" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > 0.2:
            imagebutton at show_hide_dissolve idle "maya_temperature_25" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > 0.1:
            imagebutton at show_hide_dissolve idle "maya_temperature_15" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.1:
            imagebutton at show_hide_dissolve idle "maya_temperature_0" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.2:
            imagebutton at show_hide_dissolve idle "maya_temperature_m15" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.3:
            imagebutton at show_hide_dissolve idle "maya_temperature_m25" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.45:
            imagebutton at show_hide_dissolve idle "maya_temperature_m35" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.6:
            imagebutton at show_hide_dissolve idle "maya_temperature_m50" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.7:
            imagebutton at show_hide_dissolve idle "maya_temperature_m65" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -0.8:
            imagebutton at show_hide_dissolve idle "maya_temperature_m75" xalign 0.316 yalign 0.78 action NullAction()
        elif mayaScore > -1:
            imagebutton at show_hide_dissolve idle "maya_temperature_m85" xalign 0.316 yalign 0.78 action NullAction()
        else:
            imagebutton at show_hide_dissolve idle "maya_temperature_m100" xalign 0.316 yalign 0.78 action NullAction()
        text "{color=#000000}[mayaPercentage]%{/color}" at show_hide_dissolve xalign 0.311 yalign 0.855
        imagebutton at show_hide_dissolve idle "bios_avatar_sage" xalign 0.5 yalign 0.05 action NullAction()
        text "{size=+10}{color=#BCB88A}{font=Redressed.ttf}Sage{/font}{/color}{/size}" at show_hide_dissolve xalign 0.50 yalign 0.23 text_align 0.5
        $ sagePercentage = (int) (sageScore * 100.0)
        $ sageAlignValue = 0.55 - 0.214 * sageScore
        imagebutton at show_hide_dissolve idle "girl_arrow" xalign 0.447 yalign sageAlignValue action NullAction()
        if sageScore == 1.0:
            imagebutton at show_hide_dissolve idle "sage_temperature_100" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore >= 0.8:
            imagebutton at show_hide_dissolve idle "sage_temperature_85" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore >= 0.7:
            imagebutton at show_hide_dissolve idle "sage_temperature_75" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore >= 0.6:
            imagebutton at show_hide_dissolve idle "sage_temperature_65" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore >= 0.45:
            imagebutton at show_hide_dissolve idle "sage_temperature_50" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore >= 0.3:
            imagebutton at show_hide_dissolve idle "sage_temperature_35" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > 0.2:
            imagebutton at show_hide_dissolve idle "sage_temperature_25" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > 0.1:
            imagebutton at show_hide_dissolve idle "sage_temperature_15" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.1:
            imagebutton at show_hide_dissolve idle "sage_temperature_0" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.2:
            imagebutton at show_hide_dissolve idle "sage_temperature_m15" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.3:
            imagebutton at show_hide_dissolve idle "sage_temperature_m25" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.45:
            imagebutton at show_hide_dissolve idle "sage_temperature_m35" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.6:
            imagebutton at show_hide_dissolve idle "sage_temperature_m50" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.7:
            imagebutton at show_hide_dissolve idle "sage_temperature_m65" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -0.8:
            imagebutton at show_hide_dissolve idle "sage_temperature_m75" xalign 0.525 yalign 0.78 action NullAction()
        elif sageScore > -1:
            imagebutton at show_hide_dissolve idle "sage_temperature_m85" xalign 0.525 yalign 0.78 action NullAction()
        else:
            imagebutton at show_hide_dissolve idle "sage_temperature_m100" xalign 0.525 yalign 0.78 action NullAction()
        text "{color=#000000}[sagePercentage]%{/color}" at show_hide_dissolve xalign 0.5 yalign 0.855
        imagebutton at show_hide_dissolve idle "bios_avatar_jill" xalign 0.7 yalign 0.05 action NullAction()
        text "{size=+10}{color=#ffe9b9}{font=Redressed.ttf}Jill{/font}{/color}{/size}" at show_hide_dissolve xalign 0.69 yalign 0.23 text_align 0.5
        $ jillPercentage = (int) (jillScore * 100.0)
        $ jillAlignValue = 0.55 - 0.214 * jillScore
        imagebutton at show_hide_dissolve idle "girl_arrow" xalign 0.634 yalign jillAlignValue action NullAction()
        if jillScore == 1.0:
            imagebutton at show_hide_dissolve idle "jill_temperature_100" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore >= 0.8:
            imagebutton at show_hide_dissolve idle "jill_temperature_85" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore >= 0.7:
            imagebutton at show_hide_dissolve idle "jill_temperature_75" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore >= 0.6:
            imagebutton at show_hide_dissolve idle "jill_temperature_65" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore >= 0.45:
            imagebutton at show_hide_dissolve idle "jill_temperature_50" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore >= 0.3:
            imagebutton at show_hide_dissolve idle "jill_temperature_35" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > 0.2:
            imagebutton at show_hide_dissolve idle "jill_temperature_25" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > 0.1:
            imagebutton at show_hide_dissolve idle "jill_temperature_15" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.1:
            imagebutton at show_hide_dissolve idle "jill_temperature_0" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.2:
            imagebutton at show_hide_dissolve idle "jill_temperature_m15" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.3:
            imagebutton at show_hide_dissolve idle "jill_temperature_m25" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.45:
            imagebutton at show_hide_dissolve idle "jill_temperature_m35" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.6:
            imagebutton at show_hide_dissolve idle "jill_temperature_m50" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.7:
            imagebutton at show_hide_dissolve idle "jill_temperature_m65" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -0.8:
            imagebutton at show_hide_dissolve idle "jill_temperature_m75" xalign 0.735 yalign 0.78 action NullAction()
        elif jillScore > -1:
            imagebutton at show_hide_dissolve idle "jill_temperature_m85" xalign 0.735 yalign 0.78 action NullAction()
        else:
            imagebutton at show_hide_dissolve idle "jill_temperature_m100" xalign 0.735 yalign 0.78 action NullAction()
        text "{color=#000000}[jillPercentage]%{/color}" at show_hide_dissolve xalign 0.694 yalign 0.855
        imagebutton at show_hide_dissolve idle "bios_avatar_isabella" xalign 0.9 yalign 0.05 action NullAction()
        text "{size=+10}{color=#d8f2ff}{font=Redressed.ttf}Isabella{/font}{/color}{/size}" at show_hide_dissolve xalign 0.886 yalign 0.23 text_align 0.5
        $ isabellaPercentage = (int) (isabellaScore * 100.0)
        $ isabellaAlignValue = 0.55 - 0.214 * isabellaScore
        imagebutton at show_hide_dissolve idle "girl_arrow" xalign 0.816 yalign isabellaAlignValue action NullAction()
        if isabellaScore == 1.0:
            imagebutton at show_hide_dissolve idle "isabella_temperature_100" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore >= 0.8:
            imagebutton at show_hide_dissolve idle "isabella_temperature_85" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore >= 0.7:
            imagebutton at show_hide_dissolve idle "isabella_temperature_75" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore >= 0.6:
            imagebutton at show_hide_dissolve idle "isabella_temperature_65" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore >= 0.45:
            imagebutton at show_hide_dissolve idle "isabella_temperature_50" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore >= 0.3:
            imagebutton at show_hide_dissolve idle "isabella_temperature_35" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > 0.2:
            imagebutton at show_hide_dissolve idle "isabella_temperature_25" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > 0.1:
            imagebutton at show_hide_dissolve idle "isabella_temperature_15" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.1:
            imagebutton at show_hide_dissolve idle "isabella_temperature_0" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.2:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m15" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.3:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m25" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.45:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m35" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.6:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m50" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.7:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m65" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -0.8:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m75" xalign 0.94 yalign 0.78 action NullAction()
        elif isabellaScore > -1:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m85" xalign 0.94 yalign 0.78 action NullAction()
        else:
            imagebutton at show_hide_dissolve idle "isabella_temperature_m100" xalign 0.94 yalign 0.78 action NullAction()
        text "{color=#000000}[isabellaPercentage]%{/color}" at show_hide_dissolve xalign 0.88 yalign 0.855
        imagebutton at show_hide_dissolve idle "invisible_viewport" xalign 0.5 yalign 0.5 action (Hide("endingGirlScreen"), Jump(episodeContLabel))
init -501:
    screen lewd_scene_selection_screen:
        modal False
        tag lewd_scene_selection_screen
        mousearea area (1200, 0, 720, 250) hovered SetVariable("lewd_scene_selection_hover", True) unhovered SetVariable("lewd_scene_selection_hover", False)
        if lewd_scene_selection_hover:
            hbox:
                if currentEpisode == 1 and preferredmilf == 0:
                    xanchor -8.9
                elif currentEpisode == 1 and preferredmilf == 1:
                    xalign 0.99
                elif currentEpisode == 2 and preferredmilf == 0:
                    xanchor -8.9
                elif currentEpisode == 2 and preferredmilf == 1:
                    xalign 0.99
                if lewd_pussy_available:
                    imagebutton at show_hide_dissolve idle "lewd_pussy" hover "lewd_pussy_hover" xalign 0.95 yalign 0.01 action Jump(current_lewd_pussy_label)
                if lewd_ass_available:
                    imagebutton at show_hide_dissolve idle "lewd_ass" hover "lewd_ass_hover" xalign 0.91 yalign 0.01 action Jump(current_lewd_ass_label)
                if lewd_tits_available:
                    imagebutton at show_hide_dissolve idle "lewd_tits" hover "lewd_tits_hover" xalign 0.87 yalign 0.01 action Jump(current_lewd_tits_label)
                if lewd_lips_available:
                    imagebutton at show_hide_dissolve idle "lewd_lips" hover "lewd_lips_hover" xalign 0.83 yalign 0.01 action Jump(current_lewd_lips_label)
                if lewd_hand_available:
                    imagebutton at show_hide_dissolve idle "lewd_hand" hover "lewd_hand_hover" xalign 0.79 yalign 0.01 action Jump(current_lewd_hand_label)
                if lewd_fingers_available:
                    imagebutton at show_hide_dissolve idle "lewd_fingers" hover "lewd_fingers_hover" xalign 0.75 yalign 0.01 action Jump(current_lewd_fingers_label)
                imagebutton at show_hide_dissolve idle "lewd_cum" hover "lewd_cum_hover" xalign 0.99 yalign 0.01 action Jump(current_lewd_cum_label)
init -501:
    screen magnar_shop_screen:
        modal False
        tag magnar_shop_screen
        imagebutton idle "shop_bg" xalign 0.97 yalign 0.4 action NullAction()
        imagebutton idle "shop_close" hover "shop_close_hover" xalign 0.978 yalign 0.08 action (Hide("magnar_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), Jump(afterMagnarShopLabel))
        imagebutton idle "shop_english_booster" xalign 0.953 yalign 0.23 action NullAction()
        if englishBoost == 0:
            imagebutton idle "shop_level0" xalign 0.745 yalign 0.31 action NullAction()
            imagebutton idle "shop_money1" xalign 0.86 yalign 0.31 action NullAction()
            if money > 0:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.31 action (Function(mny,-1),SetVariable("englishBoost",5), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.31 action NullAction()
        elif englishBoost == 5:
            imagebutton idle "shop_level1" xalign 0.745 yalign 0.31 action NullAction()
            imagebutton idle "shop_money2" xalign 0.86 yalign 0.31 action NullAction()
            if money > 1:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.31 action (Function(mny,-2),SetVariable("englishBoost",10), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.31 action NullAction()
        elif englishBoost == 10:
            imagebutton idle "shop_level2" xalign 0.745 yalign 0.31 action NullAction()
            imagebutton idle "shop_money3" xalign 0.86 yalign 0.31 action NullAction()
            if money > 2:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.31 action (Function(mny,-3),SetVariable("englishBoost",15), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.31 action NullAction()
        else:
            imagebutton idle "shop_level3" xalign 0.745 yalign 0.31 action NullAction()
            imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.31 action NullAction()
            imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.31 action NullAction()
        imagebutton idle "shop_math_booster" xalign 0.953 yalign 0.4 action NullAction()
        if mathBoost == 0:
            imagebutton idle "shop_level0" xalign 0.745 yalign 0.48 action NullAction()
            imagebutton idle "shop_money1" xalign 0.86 yalign 0.48 action NullAction()
            if money > 0:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.48 action (Function(mny,-1),SetVariable("mathBoost",5), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.48 action NullAction()
        elif mathBoost == 5:
            imagebutton idle "shop_level1" xalign 0.745 yalign 0.48 action NullAction()
            imagebutton idle "shop_money2" xalign 0.86 yalign 0.48 action NullAction()
            if money > 1:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.48 action (Function(mny,-2),SetVariable("mathBoost",10), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.48 action NullAction()
        elif mathBoost == 10:
            imagebutton idle "shop_level2" xalign 0.745 yalign 0.48 action NullAction()
            imagebutton idle "shop_money3" xalign 0.86 yalign 0.48 action NullAction()
            if money > 2:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.48 action (Function(mny,-3),SetVariable("mathBoost",15), Jump(talkMagnarShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.48 action NullAction()
        else:
            imagebutton idle "shop_level3" xalign 0.745 yalign 0.48 action NullAction()
            imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.48 action NullAction()
            imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.48 action NullAction()
        if genderPresented:
            imagebutton idle "shop_gender_booster" xalign 0.953 yalign 0.57 action NullAction()
            if genderBoost == 0:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.65 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.65 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.65 action (Function(mny,-1),SetVariable("genderBoost",5), Jump(talkMagnarShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
            elif genderBoost == 5:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.65 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.65 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.65 action (Function(mny,-2),SetVariable("genderBoost",10), Jump(talkMagnarShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
            elif genderBoost == 10:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.65 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.65 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.65 action (Function(mny,-3),SetVariable("genderBoost",15), Jump(talkMagnarShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.65 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.65 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
        if genderPresented:
            imagebutton idle "shop_notes" xalign 0.953 yalign 0.74 action NullAction()
            if not nerdNotes:
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.82 action NullAction()
            else:
                imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.808 action NullAction()
            if money > 2 and not nerdNotes:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.82 action (Function(mny,-3),SetVariable("nerdNotes",True), Jump(talkMagnarShopLabel))
            elif not nerdNotes:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.82 action NullAction()
        else:
            imagebutton idle "shop_notes" xalign 0.953 yalign 0.57 action NullAction()
            if not nerdNotes:
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.65 action NullAction()
            else:
                imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.638 action NullAction()
            if money > 2 and not nerdNotes:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.65 action (Function(mny,-3),SetVariable("nerdNotes",True), Jump(talkMagnarShopLabel))
            elif not nerdNotes:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
init -501:
    screen derek_shop_screen:
        modal False
        tag derek_shop_screen
        imagebutton idle "shop_bg_long" xalign 0.97 yalign 0.9 action NullAction()
        imagebutton idle "shop_close" hover "shop_close_hover" xalign 0.978 yalign 0.08 action (Hide("derek_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), Jump(afterDerekShopLabel))
        imagebutton idle "shop_english_cheat" xalign 0.953 yalign 0.2 action NullAction()
        if englishCheatBoost == 0:
            imagebutton idle "shop_level0" xalign 0.745 yalign 0.28 action NullAction()
            imagebutton idle "shop_money1" xalign 0.86 yalign 0.28 action NullAction()
            if money > 0:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.28 action (Function(mny,-1),SetVariable("englishCheatBoost",1), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.28 action NullAction()
        elif englishCheatBoost == 1:
            imagebutton idle "shop_level1" xalign 0.745 yalign 0.28 action NullAction()
            imagebutton idle "shop_money2" xalign 0.86 yalign 0.28 action NullAction()
            if money > 1:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.28 action (Function(mny,-2),SetVariable("englishCheatBoost",2), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.28 action NullAction()
        elif englishCheatBoost == 2:
            imagebutton idle "shop_level2" xalign 0.745 yalign 0.28 action NullAction()
            imagebutton idle "shop_money3" xalign 0.86 yalign 0.28 action NullAction()
            if money > 2:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.28 action (Function(mny,-3),SetVariable("englishCheatBoost",3), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.28 action NullAction()
        else:
            imagebutton idle "shop_level3" xalign 0.745 yalign 0.28 action NullAction()
            imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.28 action NullAction()
            imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.28 action NullAction()
        imagebutton idle "shop_math_cheat" xalign 0.953 yalign 0.37 action NullAction()
        if mathCheatBoost == 0:
            imagebutton idle "shop_level0" xalign 0.745 yalign 0.45 action NullAction()
            imagebutton idle "shop_money1" xalign 0.86 yalign 0.45 action NullAction()
            if money > 0:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.45 action (Function(mny,-1),SetVariable("mathCheatBoost",1), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.45 action NullAction()
        elif mathCheatBoost == 1:
            imagebutton idle "shop_level1" xalign 0.745 yalign 0.45 action NullAction()
            imagebutton idle "shop_money2" xalign 0.86 yalign 0.45 action NullAction()
            if money > 1:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.45 action (Function(mny,-2),SetVariable("mathCheatBoost",2), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.45 action NullAction()
        elif mathCheatBoost == 2:
            imagebutton idle "shop_level2" xalign 0.745 yalign 0.45 action NullAction()
            imagebutton idle "shop_money3" xalign 0.86 yalign 0.4458 action NullAction()
            if money > 2:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.45 action (Function(mny,-3),SetVariable("mathCheatBoost",3), Jump(talkDerekShopLabel))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.45 action NullAction()
        else:
            imagebutton idle "shop_level3" xalign 0.745 yalign 0.45 action NullAction()
            imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.45 action NullAction()
            imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.45 action NullAction()
        if genderPresented:
            imagebutton idle "shop_gender_cheat" xalign 0.953 yalign 0.54 action NullAction()
            if genderCheatBoost == 0:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.62 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-1),SetVariable("genderCheatBoost",1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            elif genderCheatBoost == 1:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.62 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-2),SetVariable("genderCheatBoost",2), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            elif genderCheatBoost == 2:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.62 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-3),SetVariable("genderCheatBoost",3), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.62 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
        if genderPresented:
            imagebutton idle "shop_shuffle_cheat" xalign 0.953 yalign 0.71 action NullAction()
            if gameBoost == 0:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.79 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-1),SetVariable("gameBoost",1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            elif gameBoost == 1:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.79 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-2),SetVariable("gameBoost",2), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            elif gameBoost == 2:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.79 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-3),SetVariable("gameBoost",3), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.79 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
        else:
            imagebutton idle "shop_shuffle_cheat" xalign 0.953 yalign 0.54 action NullAction()
            if gameBoost == 0:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.62 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-1),SetVariable("gameBoost",1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            elif gameBoost == 1:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.62 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-2),SetVariable("gameBoost",2), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            elif gameBoost == 2:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.62 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.62 action (Function(mny,-3),SetVariable("gameBoost",3), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.62 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.62 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.62 action NullAction()
        if genderPresented:
            imagebutton idle "shop_brawler_cheat" xalign 0.953 yalign 0.88 action NullAction()
            if bonusPointsSportsDerek == 0 and bonusPointsSports != 12:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.96 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.96 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.96 action (Function(mny,-1),SetVariable("bonusPointsSportsDerek",1),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.96 action NullAction()
            elif bonusPointsSportsDerek == 1 and bonusPointsSports != 12:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.96 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.96 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.96 action (Function(mny,-2),SetVariable("bonusPointsSportsDerek",2),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.96 action NullAction()
            elif bonusPointsSportsDerek == 2 and bonusPointsSports != 12:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.96 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.96 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.96 action (Function(mny,-3),SetVariable("bonusPointsSportsDerek",3),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.96 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.96 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.96 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.96 action NullAction()
        else:
            imagebutton idle "shop_brawler_cheat" xalign 0.953 yalign 0.71 action NullAction()
            if bonusPointsSportsDerek == 0:
                imagebutton idle "shop_level0" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money1" xalign 0.86 yalign 0.79 action NullAction()
                if money > 0:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-1),SetVariable("bonusPointsSportsDerek",1),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            elif bonusPointsSportsDerek == 1:
                imagebutton idle "shop_level1" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money2" xalign 0.86 yalign 0.79 action NullAction()
                if money > 1:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-2),SetVariable("bonusPointsSportsDerek",2),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            elif bonusPointsSportsDerek == 2:
                imagebutton idle "shop_level2" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_money3" xalign 0.86 yalign 0.79 action NullAction()
                if money > 2:
                    imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.79 action (Function(mny,-3),SetVariable("bonusPointsSportsDerek",3),SetVariable("bonusPointsSports",bonusPointsSports+1), Jump(talkDerekShopLabel))
                else:
                    imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
            else:
                imagebutton idle "shop_level3" xalign 0.745 yalign 0.79 action NullAction()
                imagebutton idle "shop_max_lvl" xalign 0.86 yalign 0.79 action NullAction()
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.79 action NullAction()
init -501:
    screen quinn_shop_screen:
        modal False
        tag quinn_shop_screen
        imagebutton idle "shop_bg" xalign 0.97 yalign 0.4 action NullAction()
        imagebutton idle "shop_close" hover "shop_close_hover" xalign 0.978 yalign 0.08 action (Hide("quinn_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), Jump(afterQuinnShopLabel))
        imagebutton idle "shop_leftovers" xalign 0.953 yalign 0.23 action NullAction()
        if not quinn_shop_freebie:
            imagebutton idle "shop_free" xalign 0.86 yalign 0.31 action NullAction()
            imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.31 action (Hide("quinn_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), SetVariable("quinn_shop_freebie",True), Jump("quinn_shop_free_label"))
        else:
            imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.31 action NullAction()
        imagebutton idle "shop_spicy" xalign 0.953 yalign 0.4 action NullAction()
        if quinn_shop_spicy_lvl == 0:
            imagebutton idle "shop_money1" xalign 0.86 yalign 0.48 action NullAction()
            if money > 0:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.48 action (Hide("quinn_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), Function(mny,-1),SetVariable("quinn_shop_spicy_lvl",1), Jump("quinn_shop_spicy_lvl1_label"))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.48 action NullAction()
        else:
            imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.48 action NullAction()
        imagebutton idle "shop_japanese" xalign 0.953 yalign 0.57 action NullAction()
        if quinn_shop_japanese_lvl == 0:
            imagebutton idle "shop_money2" xalign 0.86 yalign 0.65 action NullAction()
            if money > 1:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.65 action (Hide("quinn_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"), Function(mny,-2),SetVariable("quinn_shop_japanese_lvl",1), Jump("quinn_shop_japanese_lvl1_label"))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.65 action NullAction()
        else:
            imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.65 action NullAction()
        imagebutton idle "shop_special" xalign 0.953 yalign 0.74 action NullAction()
        if quinn_shop_special_available and quinn_shop_special_lvl == 0:
            imagebutton idle "shop_money3" xalign 0.86 yalign 0.82 action NullAction()
            if money > 2:
                imagebutton idle "shop_buy" hover "shop_buy_hover" xalign 0.977 yalign 0.82 action (Hide("quinn_shop_screen"), Hide("moneymsg"), Hide("newmoneymsg"),Function(mny,-3),SetVariable("quinn_shop_special_lvl",1), Jump("quinn_shop_special_lvl1_label"))
            else:
                imagebutton idle "shop_buy_disabled" hover "shop_buy_disabled" xalign 0.977 yalign 0.82 action NullAction()
        else:
            imagebutton idle "shop_sold_out" xalign 0.91 yalign 0.82 action NullAction()
init -501:
    screen previous_screen:
        modal False
        tag previous_screen
        imagebutton idle "skip_recap_button" hover "skip_recap_button_hover" xalign 1.0 yalign 0.0 action Jump(previousEpLabel)
init -1:
    transform transformSide:
        xpos 0
        ypos 0
        easein 2.5 xpos -1900 ypos 0
        easein 0.5 xpos -1600 ypos 0
init -1:
    transform transformSide2:
        xpos 0
        ypos 0
        easein 10 xpos -1900 ypos 0
        easein 10 xpos 0 ypos 0
        repeat
init -1:
    transform transformTop2:
        xpos 0
        ypos -3240
        easein 10 xpos 0 ypos 0
init -1:
    transform transformTop:
        xpos 0
        ypos -2000
        easein 10 xpos 0 ypos 0
init -1:
    transform transformBottom:
        xpos 0
        ypos 0
        linear 110 xpos 0 ypos -10113
init -1:
    transform animTransformEp3:
        xpos 0
        ypos -2160
        easein 40 xpos 0 ypos 0
        pause (5)
        easein 20 xpos 0 ypos -1080
        easein 20 xpos 0 ypos 0
init -1:
    style guide_style:
        color "#ffffff"
        text_align 0.5
        font "Museo500.otf"
        outlines [(1, "#4a0000", 0, 0)]
        size 50
init -501:
    screen keymap_screen:
        tag km_screen
        if (nonPatreonConfig or steamConfig) and renpy.loadable("walkthrough/season1/walkthrough_season1.rpyc"):
            if not persistent.walkthrough_tutorial:
                modal True
                add "bg_guide"
                key "K_RETURN" action Hide("nonexistent_screen")
                key "K_KP_ENTER" action Hide("nonexistent_screen")
                key "K_SPACE" action Hide("nonexistent_screen")
                key "mousedown_5" action Hide("nonexistent_screen")
                key "K_DOWN" action Hide("nonexistent_screen")
                key "K_PAGEUP" action Hide("nonexistent_screen")
                key "mousedown_4" action Hide("nonexistent_screen")
                key "K_UP" action Hide("nonexistent_screen")
                key "K_PAGEDOWN" action Hide("nonexistent_screen")
                key "mouseup_3" action Hide("nonexistent_screen")
                key "mouseup_1" action Hide("nonexistent_screen")
                text "Dziękuję za zakup\n{color=ffed00}Being a DIK - kompletny oficjalny przewodnik.{/color}\n\nWciśnij '{color=#00ff00}g{/color}' aby wyświetlić lub ukryć przewodnik.\nMożesz również nacisnąć przycisk {color=fe9416}Przewodnik{/color} w menu gry\naby otworzyć przewodnik.\n\Wciśnij '{color=#00ff00}g{/color}' aby kontynuować." style "guide_style_s2" xalign 0.2 yalign 0.3
                key "g" action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0), SetVariable("persistent.walkthrough_tutorial", True),Function(show_guide_func))
            else:
                key "g" action (SetVariable("tmpMenu2", quick_menu), SetVariable("quick_menu", 0),Function(show_guide_func))
        else:
            key "g" action NullAction()
init -1:
    style walkthrough_text:
        color "#ffffff"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 25
init -1:
    style walkthrough_text_highlighted:
        color "#fe9416"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 25
init -1:
    style walkthrough_text_s2:
        color "#ffffff"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 30
init -1:
    style walkthrough_text_s2_highlighed:
        color "#fe9416"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 30
init -1:
    style walkthrough_text_choice:
        color "#33d145"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 22
init -1:
    style walkthrough_text_choice_disabled:
        color "#d15433"
        xmaximum 500
        hover_color "#fe9416"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 22
init -1:
    style walkthrough_text_header:
        color "#fe9416"
        xmaximum 500
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 40
init -1:
    style walkthrough_text_scroll:
        color "#007db5"
        xmaximum 500
        hover_color "#007db5"
        font "candara.ttf"
        outlines [(1, "#000000", 0, 0)]
        size 22
init -1:
    style walkthrough_text_current:
        color "#000000"
        xmaximum 500
        font "cabin-regular.ttf"
        size 22
init -1:
    style tennis_tutorial_style:
        color "#ffffff"
        font "candara.ttf"
        outlines [(2, "#000000", 0, 0)]
        size 30
init -501:
    screen tennis_tutorial_screen:
        modal False
        tag tennis_tutorial_screen
        vbox:
            xalign 0.5
            yalign 0.5
            imagebutton idle "tennis_tutorial" hover "tennis_tutorial" action Jump("ep4_tennis_label2")
        text "W mini-grze tenisowej musisz znaleźć i kliknąć piłkę tenisową z napisem {color=#00ff00}UDEŻ{/color},\nunikając kliknięcia piłek tenisowych z napisem {color=#ff0000}PUŚĆ{/color}.\nWybierz odpowiedni moment uderzenia za pomocą wskaźnika siły po prawej stronie, aby uderzyć piłkę mocniej.\nJeśli zbyt długo będziesz szukać i klikać właściwą piłkę tenisową, przegapisz swój strzał." style "tennis_tutorial_style" xalign 0.5 yalign 0.85 text_align 0.5 xmaximum 1550
init -501:
    screen foundmoneymsg:
        modal False
        tag foundmoneymsg
        timer 3 action Hide('foundmoneymsg')
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        if money == 5:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 4:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 3:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 2:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        elif money == 1:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}${/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        else:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}Brak pieniędzy{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -501:
    screen newmoneymsg:
        modal False
        tag newmoneymsg
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        if (money > 10 and wallet_lvl == 3):
            $ money = 10
        elif (money > 8 and wallet_lvl == 2):
            $ money = 8
        elif (money > 6 and wallet_lvl == 1):
            $ money = 6
        elif money > 5 and wallet_lvl == 0:
            $ money = 5
        elif money < 0:
            $ money = 0
        if money > 0:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}$%i{/color}{/font}{/size}" % money at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
        else:
            text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Kieszonkowe:{/color} {color=#36ca2b}Brak pieniędzy{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
init -1:
    python:
        def savePersistentData():
            renpy.save_persistent()
            return

init -501:
    screen saveMsg:
        modal False
        tag saveMsg
        timer 3 action Hide("saveMsg")
        imagebutton at show_hide_dissolve idle "bg_toprightmsg" xalign 0.9825 yalign -0.01 action NullAction()
        text "{size=+3}{font=collegiate.ttf}{color=#ffffff}Dane kolekcjonerskie zapisane!{/color}{/font}{/size}" at show_hide_dissolve xalign 0.97 yalign 0.018 size 31 color "#ffffff"
return