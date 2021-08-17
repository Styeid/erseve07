import random

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

#Window.size = (790, 350)

#Builder.load_file("about.kv")


class MyLayoutYo(RelativeLayout):
    from animatie_knop import top_colorstonez, top_colorstonex, top_colorstoney, top_colorstonew
    from animatie_knop import ani_anystone, ani_grey, ani_green_one, ani_green_two, ani_blue_one, ani_blue_two
    from animatie_knop import ani_darkgrey, ani_darkgrey_holex, ani_darkgrey_holey, ani_darkgrey_holez
    from animatie_knop import ani_pink_one, ani_pink_two, ani_purp_one, ani_purp_two
    from twists import none_actie, front_lom, front_rom, front_left_rightx, front_left_rightz
    from twists import midle_up_downx, midle_up_downz, midle_up, midle_down
    from twists import midle_right_leftx, midle_right_leftz, midle_right, midle_left
    from twists import left_up_downx, left_up_downz, left_up, left_down
    from twists import right_up_downx, right_up_downz, right_down, right_up
    from twists import up_right_leftx, up_right_leftz, up_right, up_left
    from twists import down_right_leftx, down_right_leftz, down_right, down_left
    from twists import up_hole, down_hole, right_hole, left_hole, activate_twists, deactivate_twists

    perspectief_punt_x = NumericProperty(0)
    perspectief_punt_y = NumericProperty(0)

    NB_of_TWISTs = NumericProperty(4)
    MIN_twists = NumericProperty(2) # LET OP waarde MIN_twists op 0, onstaat er een BUG !! #
    MAX_twists = NumericProperty(34)
    AANTAL_Twistys = NumericProperty(0)

    HISTORY_twists = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                      "", "", "", "", "", "", "", "", "", ""]
    AANTAL_twists = len(HISTORY_twists)

    MisterY_twists = [u"(\u003F)"]
    DEFault_HIS_twists = [f"Last {AANTAL_twists} twists ! press DUM"]

    TWIST_TIME = NumericProperty(60) # DEFAULT 151
    TIME_LEFT = ""
    TIME_TRIG = NumericProperty(0)
    TIME_SCOOP = NumericProperty(1)

    U1 = ""
    UX1 = "111111111"
    U2 = ""
    UX2 = "222222222"
    U3 = ""
    UX3 = "333333333"
    U4 = ""
    UX4 = "444444444"
    U5 = ""
    UX5 = "555555555"
    U6 = ""
    UX6 = "666666666"
    U_TOTAAL = [""]
    U_GROEP = ""
    UX_BIT = True

    DIV_PERC = 150
    SCORE_level = 0
    ST_MAX_level = 6
    SCORE_time = 0
    ST_MAX_time = 2701
    SCORE_twist = 0
    ST_MAX_twist = 100
    SCORE_totaal = 0
    RATING = (0)
    RATING_I = (0)

    STATE_GAME_OVER = False
    STATE_GAME_STARTED = False

    sound_shuffle = None
    sound_countd_own = None
    sound_count_bang = None
    sound_onwin = None
    sound_zero_twist = None
    Last_thirty = 30

    def __init__(self, **kwargs):
        super(MyLayoutYo, self).__init__(**kwargs)
        self.init_audio()
        #self.data_display()

    def init_audio(self):
        self.sound_shuffle = SoundLoader.load("wav/BlipClockShuffle004.wav")
        self.sound_countd_own = SoundLoader.load("wav/CountD002.wav")
        self.sound_count_bang = SoundLoader.load("wav/discoWin003.wav")
        self.sound_zero_twist = SoundLoader.load("wav/GO_007a.wav")
        self.sound_onwin = SoundLoader.load("wav/ONWin_Part001w.wav")

        self.sound_shuffle.volume = 1
        self.sound_countd_own.volume = 1
        self.sound_count_bang.volume = .4
        self.sound_zero_twist.volume = 1
        self.sound_onwin.volume = 0.1

    def game_over_sound(self, dt):
        self.sound_count_bang.play()
    def game_over_soundX(self, dt):
        self.sound_zero_twist.play()
    def game_over_nonsound(self, dt):
        self.sound_count_bang.stop()


    def data_display(self, *args):
        data3 = eval(str(self.SCORE_level))
        convert_data3 = str(int(data3))
        data4 = eval(str(self.SCORE_time))
        convert_data4 = str(int(data4))
        data5 = eval(str(self.SCORE_twist))
        convert_data5 = str(int(data5))
        """print(f"UX_BIT = {self.UX_BIT} // Status = {self.U_TOTAAL} // Level = {convert_data3} // Time = {convert_data4} "
              f"// Twist = {convert_data5} // UnCut = {int(self.RATING)} // RoundUP = {self.RATING_I} /// XxX = {self.TWIST_TIME}"
              f"\n<-------------------------------------------->")"""

    def reset_all(self):
        if self.U_TOTAAL:
            self.UX_BIT = False
            self.SCORE_level = 0
            self.TWIST_TIME = 0
            self.AANTAL_Twistys = 0
            self.U_TOTAAL = [None]
            self.RATING = 0
            self.RATING_I = 0

    def deact_on_start(self):
            self.ids.home_two.disabled = False

    def on_start(self, *args):
        if not self.STATE_GAME_STARTED:
            self.TIME_SCOOP = 1
            self.CLOCK_u_total = Clock.schedule_interval(self.u_total, 1)
            self.CLOCK_aantal_x_twist = Clock.schedule_interval(self.aantal_x_twist, 1)
            self.CLOCK_gameover = Clock.schedule_interval(self.gameover, 1)
            self.CLOCK_time_stop = Clock.schedule_interval(self.time_stop, 1)
            self.ids.home_two.disabled = True
            self.ids.jufaja1.disabled = True
            #Clock.schedule_interval(self.data_display, 5)
        else:
            self.gameover()

    def cancel_onwin(self):
        self.CLOCK_u_total.cancel()
        self.CLOCK_aantal_x_twist.cancel()
        self.CLOCK_gameover.cancel()
        self.CLOCK_time_stop.cancel()
        self.CLOCK_count.cancel()

    def tijd_rest(self, *args):
        self.TWIST_TIME = self.TWIST_TIME - self.TIME_SCOOP
        m, s = divmod(self.TWIST_TIME, 60)
        self.TIME_LEFT = str(m).zfill(2) + ":" + str(s).zfill(2)
        self.ids.vizier13.text = self.TIME_LEFT

    def gameover(self, *args):
        if not self.STATE_GAME_OVER:
            if self.TWIST_TIME > -1 and self.AANTAL_Twistys > 0:
                self.tijd_rest()
                self.ids.home_two.disabled = True
                self.ids.home_twob.disabled = False
            else:
                self.STATE_GAME_STARTED = False
                self.TWIST_TIME = 0
                self.AANTAL_Twistys = 0
                self.ids.STart_BUT.opacity = 0.9
                self.deactivate_twists()
                self.TIME_LEFT = "G a m e  O v e r"
                self.ids.home_one.text = self.TIME_LEFT
                self.ids.home_two.text = ""
                self.ids.home_three.text = "Continue"
                self.ids.home_two.disabled = True
                self.ids.home_three.disabled = False
                self.ids.minx.disabled = True
                self.ids.plux.disabled = True
                self.cancel_onwin()
                self.game_over_soundX(0)
                self.game_over_nonsound(1)


    def start_button_start(self):
        self.ids.STart_BUT.opacity = 0
        self.ids.ratingY.text = str("")
        self.TWIST_TIME += 1
        self.AANTAL_Twistys += 1
        self.twist_s()
        self.ids.home_two.disabled = True
        self.ids.home_twob.disabled = True
        self.ids.jufaja1.disabled = False

    def start_button_win(self):
        self.ids.STart_BUT.opacity = 0
        self.activate_twists()
        self.ids.ratingY.text = str("")
        self.TWIST_TIME += 151
        self.AANTAL_Twistys += 10
        self.ids.home_two.text = ""
        self.ids.home_three.text = "XxX"
        self.ids.home_two.disabled = True
        self.ids.home_twob.disabled = False
        self.ids.home_three.disabled = True
        self.on_start()

        #print("<------------------------->")

    def time_stop(self, *args):
        if self.U_TOTAAL:
            self.ids.home_one.text = "J U F A J A  Grid"
            self.ids.home_onex.text = "Pro"
            self.TIME_SCOOP = 0
            self.ids.STart_BUT.opacity = 0.9
            self.deactivate_twists()
            self.ids.home_three.text = ""
            self.ids.home_twob.disabled = False
            self.rating_x()
            self.CLOCK_count.cancel()
            self.ids.minx.disabled = False
            self.ids.plux.disabled = False
        if self.UX_BIT:
            self.ids.home_two.text = "Again"
        else:
            self.ids.home_two.text = "Restart"
            self.ids.ratingY.text = str("")
            self.ids.home_three.text = ""
            self.ids.home_three.disabled = True
            self.ids.home_two.disabled = False

     ##

        self.SCORE_time = f"{str(self.TWIST_TIME)}/{str(self.ST_MAX_time)}*{str(self.DIV_PERC)}"
        display_time = eval(str(self.SCORE_time))
        self.SCORE_totaal = f"({str(self.SCORE_level)}+{str(self.SCORE_time)}+{str(self.SCORE_twist)})/3"
        self.RATING = eval(str(self.SCORE_totaal))
        ## DIsplyed score on layout(with Converting to get 000000000 numbers) ##
        multiplay_factor = "100000"
        sum_rating_displ = f"({str(self.SCORE_totaal)}*{multiplay_factor})"
        rating_displayed = eval(str(sum_rating_displ))
        convert_int_r_di = str(int((rating_displayed)))
        zero_filled_r_di = convert_int_r_di.zfill(7)
        self.ids.ratingX.text = f"Score {zero_filled_r_di}"
        return str(display_time), self.RATING

    def rating_x(self, *args):
        self.RATING_I = int(self.RATING)
        try:
            if 10 >= self.RATING_I >= -1:
                self.ids.ratingY.text = str(u"\u002D")
                self.RATING_I = "X"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 20 >= self.RATING_I >= 10:
                self.ids.ratingY.text = str("F")
                self.RATING_I = "F"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 40 >= self.RATING_I >= 20:
                self.ids.ratingY.text = str("E")
                self.RATING_I = "E"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 50 >= self.RATING_I >= 40:
                self.ids.ratingY.text = str("C")
                self.RATING_I = "C"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 60 >= self.RATING_I >= 50:
                self.ids.ratingY.text = str("C")
                self.RATING_I = "C"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 70 >= self.RATING_I >= 60:
                self.ids.ratingY.text = str("B")
                self.RATING_I = "B"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            elif 80 >= self.RATING_I >= 70:
                self.ids.ratingY.text = str("A")
                self.RATING_I = "A"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
            else:
                self.ids.ratingY.text = str("S")
                self.RATING_I = "S"
                self.game_over_nonsound(1)
                self.cancel_onwin()
                self.sound_onwin.play()
        except ValueError:
            return "sorry"

    def unik_ode(self):
     pass

    def twist_one(self, *args):
        twist = random.randint(1, 15)
        if twist == 1:
            self.front_rom()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B9F]"]))
        if twist == 4:
            self.midle_down()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B9D]"]))
        if twist == 5:
            self.midle_right()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B9C]"]))
        if twist == 6:
            self.midle_left()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B9E]"]))
        if twist == 7:
            self.left_up()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25E7\u25BD]"]))
        if twist == 8:
            self.left_down()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25E7\u25B3]"]))
        if twist == 9:
            self.right_up()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25BD\u25E8]"]))
        if twist == 10:
            self.right_down()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25B3\u25E8]"]))
        if twist == 11:
            self.up_right()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25C0\u2B12]"]))
        if twist == 12:
            self.up_left()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B12\u25B6]"]))
        if twist == 13:
            self.down_right()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u25C0\u2B13]"]))
        if twist == 14:
            self.down_left()
            self.AANTAL_Twistys = self.AANTAL_Twistys + 1
            #print(str([u"[\u2B13\u25B6]"]))
        if twist == 15:
            self.none_actie()
            #print(str("XxX"))

    def twist_s(self):
        self.TIME_SCOOP = 0
        self.ids.ratingY.text = str("")
        x_twists = 0
        while x_twists < self.NB_of_TWISTs:
            self.twist_one()
            x_twists = x_twists + 1
            self.HISTORY_twists[:1] = self.MisterY_twists
            self.UX_BIT = True
            self.sound_shuffle.play()
            #print(f"{x_twists}/{self.NB_of_TWISTs}\n"
            #      f"###########################")

    def m_max_twists(self):
        m_m_twists = self.NB_of_TWISTs
        if m_m_twists >= 1:
            self.NB_of_TWISTs = self.NB_of_TWISTs + 1
            self.ids.nu_of_twists.text = str(self.NB_of_TWISTs)
        if m_m_twists >= self.MAX_twists:
            self.NB_of_TWISTs = self.NB_of_TWISTs - 1
            self.ids.nu_of_twists.text = str(self.MAX_twists)
        self.ids.home_one.text = ""
        self.ids.home_onex.text = ""
        self.deact_on_start()
        self.reset_all()

    def min_m_twists(self):
        m_m_twists = self.NB_of_TWISTs
        if m_m_twists >= 1:
            self.NB_of_TWISTs = self.NB_of_TWISTs - 1
            self.ids.nu_of_twists.text = str(self.NB_of_TWISTs)
        if m_m_twists <= self.MIN_twists:
            self.NB_of_TWISTs = self.NB_of_TWISTs + 1
            self.ids.nu_of_twists.text = str(self.MIN_twists)
        self.ids.home_one.text = ""
        self.ids.home_onex.text = ""
        self.deact_on_start()
        self.reset_all()

    def progress_plus(self):
        plus_val = self.ids.progress_twists.value
        plus_val += 1
        self.ids.progress_twists.value = plus_val

    def progress_minus(self):
        minus_val = self.ids.progress_twists.value
        minus_val -= 1
        self.ids.progress_twists.value = minus_val

    def vizier_on(self):
        self.ids.vizier1.background_color, self.ids.vizier1.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier2.background_color, self.ids.vizier2.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier3.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier4.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier5.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier6.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier7.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier8.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier9.background_color = \
            self.ids.dum2.background_color
        self.ids.vizier10.background_color, self.ids.vizier10.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier11.background_color, self.ids.vizier11.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier12.background_color, self.ids.vizier12.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier13.background_color, self.ids.vizier13.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier14.background_color, self.ids.vizier14.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.playy_twists.background_color, self.ids.playy_twists.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier16.background_color, self.ids.vizier16.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier17.background_color, self.ids.vizier17.color =\
            self.ids.dum2.background_color, self.ids.dum2.color
        self.ids.vizier18.background_color, self.ids.vizier18.color =\
            self.ids.dum2.background_color, self.ids.dum2.color

    def vizier_off(self):
        self.ids.vizier1.background_color, self.ids.vizier1.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier2.background_color, self.ids.vizier2.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier3.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier4.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier5.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier6.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier7.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier8.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier9.background_color = \
            self.ids.dum3.background_color
        self.ids.vizier10.background_color, self.ids.vizier10.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier11.background_color, self.ids.vizier11.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier12.background_color, self.ids.vizier12.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier13.background_color, self.ids.vizier13.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier14.background_color, self.ids.vizier14.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.playy_twists.background_color, self.ids.playy_twists.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier16.background_color, self.ids.vizier16.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier17.background_color, self.ids.vizier17.color = \
            self.ids.dum3.background_color, self.ids.dum3.color
        self.ids.vizier18.background_color, self.ids.vizier18.color = \
            self.ids.dum3.background_color, self.ids.dum3.color

    def vizier_display(self, *args):
        XHISTORY_twists = f"\n\n\n\n  \t  {self.HISTORY_twists[0]}{self.HISTORY_twists[1]}{self.HISTORY_twists[2]}" \
                       f"{self.HISTORY_twists[3]}{self.HISTORY_twists[4]}\n  \t  {self.HISTORY_twists[5]}" \
                       f"{self.HISTORY_twists[6]}{self.HISTORY_twists[7]}{self.HISTORY_twists[8]}" \
                       f"{self.HISTORY_twists[9]}\n  \t  {self.HISTORY_twists[10]}{self.HISTORY_twists[11]}" \
                       f"{self.HISTORY_twists[12]}{self.HISTORY_twists[13]}{self.HISTORY_twists[14]}\n  \t  " \
                       f"{self.HISTORY_twists[15]}{self.HISTORY_twists[16]}{self.HISTORY_twists[17]}" \
                       f"{self.HISTORY_twists[18]}{self.HISTORY_twists[19]}\n  \t  {self.HISTORY_twists[20]}" \
                       f"{self.HISTORY_twists[21]}{self.HISTORY_twists[22]}{self.HISTORY_twists[23]}" \
                       f"{self.HISTORY_twists[24]}"
        self.ids.playy_twists.text = str(XHISTORY_twists)
        return XHISTORY_twists

    def view_tegel_nummersx(self):
        self.front_left_rightx()
        self.midle_up_downx()
        self.midle_right_leftx()
        self.left_up_downx()
        self.right_up_downx()
        self.up_right_leftx()
        self.down_right_leftx()

    def view_tegel_nummersz(self):
        self.front_left_rightz()
        self.midle_up_downz()
        self.midle_right_leftz()
        self.left_up_downz()
        self.right_up_downz()
        self.up_right_leftz()
        self.down_right_leftz()

    def lvel_arrow(self):
        if self.NB_of_TWISTs < 2:
            self.TWIST_TIME = 11
            self.AANTAL_Twistys = 10
            self.ids.vizier11.text = str(0)
            self.SCORE_level = 0
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.ids.vizier9.color = self.ids.dum2.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum3.color
        elif 4 >= self.NB_of_TWISTs >= 2:
            self.AANTAL_Twistys += 25
            self.TWIST_TIME = 301
            self.ids.vizier11.text = str(1)
            self.SCORE_level = 1
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum2.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum3.color
        elif 7 >= self.NB_of_TWISTs >= 4:
            self.AANTAL_Twistys += 49
            self.TWIST_TIME = 721
            self.ids.vizier11.text = str(2)
            self.SCORE_level = 2
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum2.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum3.color
        elif 10 >= self.NB_of_TWISTs >= 7:
            self.AANTAL_Twistys += 74
            self.TWIST_TIME = 901
            self.ids.vizier11.text = str(3)
            self.SCORE_level = 3
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum2.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum3.color
        elif 15 >= self.NB_of_TWISTs >= 10:
            self.AANTAL_Twistys += 99
            self.TWIST_TIME = 1201
            self.ids.vizier11.text = str(4)
            self.SCORE_level = 4
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum2.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum3.color
        elif 25 >= self.NB_of_TWISTs >= 15:
            self.AANTAL_Twistys += 124
            self.TWIST_TIME = 1501
            self.ids.vizier11.text = str(5)
            self.SCORE_level = 5
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum2.color
            self.ids.vizier3.color = self.ids.dum3.color
        else:
            self.AANTAL_Twistys += 149
            self.TWIST_TIME = 2701
            self.ids.vizier11.text = str(6)
            self.SCORE_level = 6
            self.sound_countd_own.play()
            self.CLOCK_count = Clock.schedule_once(self.game_over_sound, (self.TWIST_TIME - self.Last_thirty))
            self.SCORE_level = f"{str(self.SCORE_level)}/{str(self.ST_MAX_level)}*{str(self.DIV_PERC)}"
            display_score = eval(str(self.SCORE_level))
            self.ids.vizier9.color = self.ids.dum3.color
            self.ids.vizier8.color = self.ids.dum3.color
            self.ids.vizier7.color = self.ids.dum3.color
            self.ids.vizier6.color = self.ids.dum3.color
            self.ids.vizier5.color = self.ids.dum3.color
            self.ids.vizier4.color = self.ids.dum3.color
            self.ids.vizier3.color = self.ids.dum2.color
            return display_score

    def aantal_x_twist(self, *args):
        axt = self.AANTAL_Twistys
        self.SCORE_twist = f"{str(self.AANTAL_Twistys)}/{self.ST_MAX_twist}*{self.DIV_PERC}"
        display_twist = eval(str(self.SCORE_twist))
        self.ids.vizier17.text = f"\n[{axt}]"
        return display_twist

    def uone(self):
        self.U1 = f"{self.ids.h1_1b.value}{self.ids.z2_1b.value}{self.ids.h2_1b.value}" \
               f"{self.ids.z1_1b.value}{self.ids.c1_1b.value}{self.ids.z3_1b.value}" \
               f"{self.ids.h4_1b.value}{self.ids.z4_1b.value}{self.ids.h3_1b.value}"
        if str(self.U1) == str(self.UX1):
            self.U1 = True
        elif str(self.U1) == str(self.UX2):
            self.U1 = True
        elif str(self.U1) == str(self.UX3):
            self.U1 = True
        elif str(self.U1) == str(self.UX4):
            self.U1 = True
        elif str(self.U1) == str(self.UX5):
            self.U1 = True
        elif str(self.U1) == str(self.UX6):
            self.U1 = True
        else:
            self.U1 = False

    def utwo(self):
        self.U2 = f"{self.ids.h6_2b.value}{self.ids.z9_1b.value}{self.ids.h1_2b.value}" \
               f"{self.ids.z7_2b.value}{self.ids.c2_2b.value}{self.ids.z1_2b.value}" \
               f"{self.ids.h7_2b.value}{self.ids.z12_1b.value}{self.ids.h4_3b.value}"
        if str(self.U2) == str(self.UX1):
            self.U2 = True
        elif str(self.U2) == str(self.UX2):
            self.U2 = True
        elif str(self.U2) == str(self.UX3):
            self.U2 = True
        elif str(self.U2) == str(self.UX4):
            self.U2 = True
        elif str(self.U2) == str(self.UX5):
            self.U2 = True
        elif str(self.U2) == str(self.UX6):
            self.U2 = True
        else:
            self.U2 = False

    def uthree(self):
        self.U3 = f"{self.ids.h6_3b.value}{self.ids.z6_2b.value}{self.ids.h5_2b.value}" \
               f"{self.ids.z9_2b.value}{self.ids.c3_3b.value}{self.ids.z10_2b.value}" \
               f"{self.ids.h1_3b.value}{self.ids.z2_2b.value}{self.ids.h2_2b.value}"
        if str(self.U3) == str(self.UX1):
            self.U3 = True
        elif str(self.U3) == str(self.UX2):
            self.U3 = True
        elif str(self.U3) == str(self.UX3):
            self.U3 = True
        elif str(self.U3) == str(self.UX4):
            self.U3 = True
        elif str(self.U3) == str(self.UX5):
            self.U3 = True
        elif str(self.U3) == str(self.UX6):
            self.U3 = True
        else:
            self.U3 = False

    def ufour(self):
        self.U4 = f"{self.ids.h4_2b.value}{self.ids.z4_2b.value}{self.ids.h3_3b.value}" \
               f"{self.ids.z12_2b.value}{self.ids.c4_4b.value}{self.ids.z11_2b.value}" \
               f"{self.ids.h7_3b.value}{self.ids.z8_2b.value}{self.ids.h8_3b.value}"
        if str(self.U4) == str(self.UX1):
            self.U4 = True
        elif str(self.U4) == str(self.UX2):
            self.U4 = True
        elif str(self.U4) == str(self.UX3):
            self.U4 = True
        elif str(self.U4) == str(self.UX4):
            self.U4 = True
        elif str(self.U4) == str(self.UX5):
            self.U4 = True
        elif str(self.U4) == str(self.UX6):
            self.U4 = True
        else:
            self.U4 = False

    def ufive(self):
        self.U5 = f"{self.ids.h2_3b.value}{self.ids.z10_1b.value}{self.ids.h5_3b.value}" \
               f"{self.ids.z3_2b.value}{self.ids.c5_5b.value}{self.ids.z5_2b.value}" \
               f"{self.ids.h3_2b.value}{self.ids.z11_1b.value}{self.ids.h8_2b.value}"
        if str(self.U5) == str(self.UX1):
            self.U5 = True
        elif str(self.U5) == str(self.UX2):
            self.U5 = True
        elif str(self.U5) == str(self.UX3):
            self.U5 = True
        elif str(self.U5) == str(self.UX4):
            self.U5 = True
        elif str(self.U5) == str(self.UX5):
            self.U5 = True
        elif str(self.U5) == str(self.UX6):
            self.U5 = True
        else:
            self.U5 = False

    def usix(self):
        self.U6 = f"{self.ids.h5_1b.value}{self.ids.z6_1b.value}{self.ids.h6_1b.value}" \
               f"{self.ids.z5_1b.value}{self.ids.c6_6b.value}{self.ids.z7_1b.value}" \
               f"{self.ids.h8_1b.value}{self.ids.z8_1b.value}{self.ids.h7_1b.value}"
        if str(self.U6) == str(self.UX1):
            self.U6 = True
        elif str(self.U6) == str(self.UX2):
            self.U6 = True
        elif str(self.U6) == str(self.UX3):
            self.U6 = True
        elif str(self.U6) == str(self.UX4):
            self.U6 = True
        elif str(self.U6) == str(self.UX5):
            self.U6 = True
        elif str(self.U6) == str(self.UX6):
            self.U6 = True
        else:
            self.U6 = False

    def u_total(self, *args):
        self.uone(), self.utwo(), self.uthree(), self.ufour(), self.ufive(), self.usix()
        self.U_GROEP = f"{self.U1}\n{self.U2}\n{self.U3}\n{self.U4}\n{self.U5}\n{self.U6}"
        self.U_TOTAAL = all([self.U1, self.U2, self.U3, self.U4, self.U5, self.U6])
        self.ids.vizier12.text = f"{self.U_TOTAAL}\n\n\n"
        self.ids.vizier14.text = str(self.U_GROEP)

    def close_win(self, *kwargs):
        self.sound_onwin.stop()
        App.get_running_app().stop()


class JuFaJaApp(App):
    pass
    #def build(self):
    #    return MyLayoutYo()


#if __name__ == "__main__":
JuFaJaApp().run()


