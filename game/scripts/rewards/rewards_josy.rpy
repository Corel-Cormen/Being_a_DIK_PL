screen rewards_josy:
    tag menu
    add "rewards/general/rewards_new_bg.jpg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rewards/general/rew_josy2.jpg" xalign 0.0 yalign 0.9
    add "rewards/general/rewards_new_fg2.png"
    imagebutton idle "rewards/general/rew_x_idle.png" hover "rewards/general/rew_x_hover.png" action ShowMenu("rewards") xalign 0.99 yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Nagrody - {color=#ff1c63}Josy{/color}" style "reward_header_style" xalign 0.02 yalign 0.004
    vpgrid:
        xalign 0.85
        ypos 0.14
        ysize 0.85
        yoffset 75
        yalign 0.1
        cols 4
        spacing 50
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.5
        if persistent.ep1_card1:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy1.png") hover Transform ("images/rewards/ep1/rew_ep1_josy1_hover.png") action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                text "{size=-4}Odcinek 1 – Swobodny spacer{/size}" style "reward_locked_style"
        if persistent.ep1_card3:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy2.png") hover Transform ("images/rewards/ep1/rew_ep1_josy2_hover.png") action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                text "{size=-4}Odcinek 1 – Swobodny spacer{/size}" style "reward_locked_style"
        if persistent.ep1_card5:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy3.png") hover Transform ("images/rewards/ep1/rew_ep1_josy3_hover.png") action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                text "{size=-4}Odcinek 1 – Swobodny spacer{/size}" style "reward_locked_style"
        if persistent.ep1_card7:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy4.png") hover Transform ("images/rewards/ep1/rew_ep1_josy4_hover.png") action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                if not minigames:
                    text "{size=-4}Odcinek 1 – Skarbiec{/size}" style "reward_locked_style"
                else:
                    text "{size=-4}Sprawdzian z Matematyki{/size}" style "reward_locked_style"
        if persistent.ep1_card9:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy5.png") hover Transform ("images/rewards/ep1/rew_ep1_josy5_hover.png") action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                text "{size=-4}Odcinek 1 – Swobodny spacer{/size}" style "reward_locked_style"
        if persistent.ep1_card11:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy6.png") hover Transform ("images/rewards/ep1/rew_ep1_josy6_hover.png") action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                text "{size=-4}Odcinek 1 – Swobodny spacer{/size}" style "reward_locked_style"
        if persistent.ep1_card13:
            vbox:
                xalign 0.5
                yalign 0.0
                imagebutton focus_mask True idle Transform ("images/rewards/ep1/rew_ep1_josy7.png") hover Transform ("images/rewards/ep1/rew_ep1_josy7_hover.png") action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox:
                xalign 0.5
                yalign 0.0
                add "gallery/locked.png"
                if not minigames:
                    text "{size=-4}Odcinek 1 - Skarbiec{/size}" style "reward_locked_style"
                else:
                    text "{size=-4}Odcinek 1 - Awanturnik{/size}" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
        vbox:
            xalign 0.5
            yalign 0.0
            add "gallery/disabled_btn.png"
            text "" style "reward_locked_style"
return