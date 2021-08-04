def activate_twists(self):
    self.ids.FL.disabled = False
    self.ids.MU.disabled = False
    self.ids.FR.disabled = False
    self.ids.ML.disabled = False
    self.ids.MR.disabled = False
    self.ids.MD.disabled = False
    self.ids.LU.disabled = False
    self.ids.UL.disabled = False
    self.ids.UR.disabled = False
    self.ids.RU.disabled = False
    self.ids.LD.disabled = False
    self.ids.DL.disabled = False
    self.ids.DR.disabled = False
    self.ids.RD.disabled = False


def deactivate_twists(self):
    self.ids.FL.disabled = True
    self.ids.MU.disabled = True
    self.ids.FR.disabled = True
    self.ids.ML.disabled = True
    self.ids.MR.disabled = True
    self.ids.MD.disabled = True
    self.ids.LU.disabled = True
    self.ids.UL.disabled = True
    self.ids.UR.disabled = True
    self.ids.RU.disabled = True
    self.ids.LD.disabled = True
    self.ids.DL.disabled = True
    self.ids.DR.disabled = True
    self.ids.RD.disabled = True


# none_actie = Twist zonder resultaaT (XxX). Wordt gebruikt in methode (def twist_one(self):).
def none_actie(self):
    pass


def front_rom(self):
    ##  A/X  ##
    default_xone_a = self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, \
                     self.ids.h1_1b.value, \
                     self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, \
                     self.ids.h1_2b.value, \
                     self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, \
                     self.ids.h1_3b.value
    ##  B/Y  ##
    positi_secon_a = self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, \
                     self.ids.h2_1b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, \
                     self.ids.h2_2b.value, \
                     self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, \
                     self.ids.h2_3b.value
    ##  C/Z  ##
    positi_thirt_a = self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, \
                     self.ids.h3_1b.value, \
                     self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, \
                     self.ids.h3_2b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, \
                     self.ids.h3_3b.value
    ##  D/A  ##
    positi_fourt_a = self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, \
                     self.ids.h4_1b.value, \
                     self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, \
                     self.ids.h4_2b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, \
                     self.ids.h4_3b.value
    ##  I/X  ##
    default_xone_b = self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, \
                     self.ids.z1_1b.value, \
                     self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, \
                     self.ids.z1_2b.value
    ##  J/Y  ##
    positi_secon_b = self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, \
                     self.ids.z2_1b.value, \
                     self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, \
                     self.ids.z2_2b.value
    ##  K/Z  ##
    positi_thirt_b = self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, \
                     self.ids.z3_1b.value, \
                     self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, \
                     self.ids.z3_2b.value
    ##  L/A  ##
    positi_fourt_b = self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, \
                     self.ids.z4_1b.value, \
                     self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, \
                     self.ids.z4_2b.value, \
        ##  =H---X(data)  wordt/krijgt  H---Y(data)  ##
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value = default_xone_a
    ##  =H---A(data)  wordt/krijgt  H---X(data)  ##
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value = positi_fourt_a
    ##  =H---Y(data)  wordt/krijgt  H---Z(data)  ##
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value = positi_secon_a
    ##  =H---Z(data)  wordt/krijgt  H---A(data)  ##
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = positi_thirt_a
    ##  =H---X(data)  wordt/krijgt  H---Y(data)  ##
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value, \
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value = default_xone_b
    ##  =H---A(data)  wordt/krijgt  H---X(data)  ##
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value = positi_fourt_b
    ##  =H---Y(data)  wordt/krijgt  H---Z(data)  ##
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value = positi_secon_b
    ##  =H---Z(data)  wordt/krijgt  H---A(data)  ##
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value = positi_thirt_b
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2BA7]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xone_b, positi_secon_b, positi_thirt_b, positi_fourt_b


def front_lom(self):
    ##  A/X  ##
    default_xone_a = self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, \
                     self.ids.h1_1b.value, \
                     self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, \
                     self.ids.h1_2b.value, \
                     self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, \
                     self.ids.h1_3b.value
    ##  B/Y  ##
    positi_secon_a = self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, \
                     self.ids.h2_1b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, \
                     self.ids.h2_2b.value, \
                     self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, \
                     self.ids.h2_3b.value
    ##  C/Z  ##
    positi_thirt_a = self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, \
                     self.ids.h3_1b.value, \
                     self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, \
                     self.ids.h3_2b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, \
                     self.ids.h3_3b.value
    ##  D/A  ##
    positi_fourt_a = self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, \
                     self.ids.h4_1b.value, \
                     self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, \
                     self.ids.h4_2b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, \
                     self.ids.h4_3b.value
    ##  =H---Z(data)  wordt/krijgt  H---Y(data)  ##
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value = positi_thirt_a
    ##  =H---Y(data)  wordt/krijgt  H---X(data)  ##
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value = positi_secon_a
    ##  =H---A(data)  wordt/krijgt  H---Z(data)  ##
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value = positi_fourt_a
    ##  =H---X(data)  wordt/krijgt  H---A(data)  ##
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = default_xone_a
    ##  I/X  ##
    default_xone_b = self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
                     self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value
    ##  J/Y  ##
    positi_secon_b = self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value, \
                     self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value
    ##  K/Z  ##
    positi_thirt_b = self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value, \
                     self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
        ##  L/A  ##
    positi_fourt_b = self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
                     self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
        ##  =H---Z(data)  wordt/krijgt  H---Y(data)  ##
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value, \
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value = positi_thirt_b
    ##  =H---Y(data)  wordt/krijgt  H---X(data)  ##
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value = positi_secon_b
    ##  =H---A(data)  wordt/krijgt  H---Z(data)  ##
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value = positi_fourt_b
    ##  =H---X(data)  wordt/krijgt  H---A(data)  ##
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value = default_xone_b
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2BA6]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xone_b, positi_secon_b, positi_thirt_b, positi_fourt_b


def front_left_rightx(self):
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z1_2b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.z2_2b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z4_2b.background_normal, = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def front_left_rightz(self):
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z1_2b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.z2_2b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z4_2b.background_normal, = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def midle_up_downx(self):
    self.ids.c1_1b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.c3_3b.background_normal, \
    self.ids.z6_2b.background_normal, \
    self.ids.z2_2b.background_normal, \
    self.ids.c6_6b.background_normal, \
    self.ids.z6_1b.background_normal, \
    self.ids.z8_1b.background_normal, \
    self.ids.c4_4b.background_normal, \
    self.ids.z8_2b.background_normal, \
    self.ids.z4_2b.background_normal = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def midle_up_downz(self):
    self.ids.c1_1b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.c3_3b.background_normal, \
    self.ids.z6_2b.background_normal, \
    self.ids.z2_2b.background_normal, \
    self.ids.c6_6b.background_normal, \
    self.ids.z6_1b.background_normal, \
    self.ids.z8_1b.background_normal, \
    self.ids.c4_4b.background_normal, \
    self.ids.z8_2b.background_normal, \
    self.ids.z4_2b.background_normal = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def midle_up(self):
    default_xtwo_c = self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
                     self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
                     self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value
    positi_secon_c = self.ids.c3_3b.text, self.ids.c3_3b.color, self.ids.c3_3b.background_color, self.ids.c3_3b.value, \
                     self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, \
                     self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value
    positi_thirt_c = self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
                     self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value, \
                     self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value
    positi_fourt_c = self.ids.c4_4b.text, self.ids.c4_4b.color, self.ids.c4_4b.background_color, self.ids.c4_4b.value, \
                     self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
                     self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value
    self.ids.c3_3b.text, self.ids.c3_3b.color, self.ids.c3_3b.background_color, self.ids.c3_3b.value, \
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
    self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, = default_xtwo_c
    self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value = positi_fourt_c
    self.ids.c4_4b.text, self.ids.c4_4b.color, self.ids.c4_4b.background_color, self.ids.c4_4b.value, \
    self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, = positi_thirt_c
    self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
    self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value, \
    self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value = positi_secon_c
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B9D]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xtwo_c, positi_secon_c, positi_thirt_c, positi_fourt_c


def midle_down(self):
    default_xtwo_d = self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
                     self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
                     self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value
    positi_secon_d = self.ids.c3_3b.text, self.ids.c3_3b.color, self.ids.c3_3b.background_color, self.ids.c3_3b.value, \
                     self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
                     self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value
    positi_thirt_d = self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
                     self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value, \
                     self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value
    positi_fourt_d = self.ids.c4_4b.text, self.ids.c4_4b.color, self.ids.c4_4b.background_color, self.ids.c4_4b.value, \
                     self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
                     self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value
    self.ids.c3_3b.text, self.ids.c3_3b.color, self.ids.c3_3b.background_color, self.ids.c3_3b.value, \
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
    self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, = positi_thirt_d
    self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value, \
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value, = positi_secon_d
    self.ids.c4_4b.text, self.ids.c4_4b.color, self.ids.c4_4b.background_color, self.ids.c4_4b.value, \
    self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, = default_xtwo_d
    self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
    self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value, \
    self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value = positi_fourt_d
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B9F]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xtwo_d, positi_secon_d, positi_thirt_d, positi_fourt_d


def midle_right_leftx(self):
    self.ids.c1_1b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.c5_5b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z5_2b.background_normal, \
    self.ids.c6_6b.background_normal, \
    self.ids.z5_1b.background_normal, \
    self.ids.z7_1b.background_normal, \
    self.ids.c2_2b.background_normal, \
    self.ids.z7_2b.background_normal, \
    self.ids.z1_2b.background_normal = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def midle_right_leftz(self):
    self.ids.c1_1b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.c5_5b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z5_2b.background_normal, \
    self.ids.c6_6b.background_normal, \
    self.ids.z5_1b.background_normal, \
    self.ids.z7_1b.background_normal, \
    self.ids.c2_2b.background_normal, \
    self.ids.z7_2b.background_normal, \
    self.ids.z1_2b.background_normal = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def midle_right(self):
    default_xtre_e = self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
                     self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
                     self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value
    positi_secon_e = self.ids.c5_5b.text, self.ids.c5_5b.color, self.ids.c5_5b.background_color, self.ids.c5_5b.value, \
                     self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
                     self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value
    positi_thirt_e = self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
                     self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
                     self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value
    positi_fourt_e = self.ids.c2_2b.text, self.ids.c2_2b.color, self.ids.c2_2b.background_color, self.ids.c2_2b.value, \
                     self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
                     self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value
    self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value = positi_fourt_e
    self.ids.c5_5b.text, self.ids.c5_5b.color, self.ids.c5_5b.background_color, self.ids.c5_5b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
    self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value = default_xtre_e
    self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
    self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
    self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value = positi_secon_e
    self.ids.c2_2b.text, self.ids.c2_2b.color, self.ids.c2_2b.background_color, self.ids.c2_2b.value, \
    self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value = positi_thirt_e
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B9E]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xtre_e, positi_secon_e, positi_thirt_e, positi_fourt_e


def midle_left(self):
    default_xtre_f = self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
                     self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
                     self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value
    positi_secon_f = self.ids.c5_5b.text, self.ids.c5_5b.color, self.ids.c5_5b.background_color, self.ids.c5_5b.value, \
                     self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
                     self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value
    positi_thirt_f = self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
                     self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
                     self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value
    positi_fourt_f = self.ids.c2_2b.text, self.ids.c2_2b.color, self.ids.c2_2b.background_color, self.ids.c2_2b.value, \
                     self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
                     self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value
    self.ids.c1_1b.text, self.ids.c1_1b.color, self.ids.c1_1b.background_color, self.ids.c1_1b.value, \
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value = positi_secon_f
    self.ids.c5_5b.text, self.ids.c5_5b.color, self.ids.c5_5b.background_color, self.ids.c5_5b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
    self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value = positi_thirt_f
    self.ids.c6_6b.text, self.ids.c6_6b.color, self.ids.c6_6b.background_color, self.ids.c6_6b.value, \
    self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
    self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value = positi_fourt_f
    self.ids.c2_2b.text, self.ids.c2_2b.color, self.ids.c2_2b.background_color, self.ids.c2_2b.value, \
    self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value = default_xtre_f
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B9C]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xtre_f, positi_secon_f, positi_thirt_f, positi_fourt_f


def left_up_downx(self):
    self.ids.h6_1b.background_normal, \
    self.ids.h6_2b.background_normal, \
    self.ids.h6_3b.background_normal, \
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.h7_1b.background_normal, \
    self.ids.h7_2b.background_normal, \
    self.ids.h7_3b.background_normal, \
    self.ids.z7_1b.background_normal, \
    self.ids.z7_2b.background_normal, \
    self.ids.z9_1b.background_normal, \
    self.ids.z9_2b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z1_2b.background_normal, \
    self.ids.z12_1b.background_normal, \
    self.ids.z12_2b.background_normal, = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def left_up_downz(self):
    self.ids.h6_1b.background_normal, \
    self.ids.h6_2b.background_normal, \
    self.ids.h6_3b.background_normal, \
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.h7_1b.background_normal, \
    self.ids.h7_2b.background_normal, \
    self.ids.h7_3b.background_normal, \
    self.ids.z7_1b.background_normal, \
    self.ids.z7_2b.background_normal, \
    self.ids.z9_1b.background_normal, \
    self.ids.z9_2b.background_normal, \
    self.ids.z1_1b.background_normal, \
    self.ids.z1_2b.background_normal, \
    self.ids.z12_1b.background_normal, \
    self.ids.z12_2b.background_normal, = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def left_up(self):
    default_xfou_g = self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value, \
                     self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
                     self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value
    positi_secon_g = self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value, \
                     self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
                     self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value
    positi_thirt_g = self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value, \
                     self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value
    positi_fourt_g = self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
                     self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value, \
                     self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value = positi_thirt_g
    self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value, \
    self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
    self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value = positi_secon_g
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = positi_fourt_g
    self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value, \
    self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
    self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value = default_xfou_g
    default_xfou_h = self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
                     self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value
    positi_secon_h = self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
                     self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value
    positi_thirt_h = self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value, \
                     self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value
    positi_fourt_h = self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
                     self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value
    self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value, \
    self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value = positi_thirt_h
    self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value, \
    self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value = positi_secon_h
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value = positi_fourt_h
    self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value, \
    self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value = default_xfou_h
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25E7\u25B3]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xfou_h, positi_secon_h, positi_thirt_h, positi_fourt_h


def left_down(self):
    default_xfou_i = self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value, \
                     self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
                     self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value
    positi_secon_i = self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value, \
                     self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
                     self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value
    positi_thirt_i = self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value, \
                     self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value
    positi_fourt_i = self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
                     self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
                     self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value = default_xfou_i
    self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value, \
    self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
    self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value = positi_fourt_i
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = positi_secon_i
    self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value, \
    self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
    self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value = positi_thirt_i
    default_xfou_j = self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, \
                     self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value
    positi_secon_j = self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
                     self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value
    positi_thirt_j = self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value, \
                     self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value
    positi_fourt_j = self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
                     self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value
    self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value, \
    self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, = default_xfou_j
    self.ids.z7_1b.text, self.ids.z7_1b.color, self.ids.z7_1b.background_color, self.ids.z7_1b.value, \
    self.ids.z7_2b.text, self.ids.z7_2b.color, self.ids.z7_2b.background_color, self.ids.z7_2b.value, = positi_fourt_j
    self.ids.z1_1b.text, self.ids.z1_1b.color, self.ids.z1_1b.background_color, self.ids.z1_1b.value, \
    self.ids.z1_2b.text, self.ids.z1_2b.color, self.ids.z1_2b.background_color, self.ids.z1_2b.value, = positi_secon_j
    self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value, \
    self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, = positi_thirt_j
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25E7\u25BD]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xfou_j, positi_secon_j, positi_thirt_j, positi_fourt_j


def right_up_downx(self):
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h5_1b.background_normal, \
    self.ids.h5_2b.background_normal, \
    self.ids.h5_3b.background_normal, \
    self.ids.h8_1b.background_normal, \
    self.ids.h8_2b.background_normal, \
    self.ids.h8_3b.background_normal, \
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z10_1b.background_normal, \
    self.ids.z10_2b.background_normal, \
    self.ids.z5_1b.background_normal, \
    self.ids.z5_2b.background_normal, \
    self.ids.z11_1b.background_normal, \
    self.ids.z11_2b.background_normal, = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def right_up_downz(self):
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h5_1b.background_normal, \
    self.ids.h5_2b.background_normal, \
    self.ids.h5_3b.background_normal, \
    self.ids.h8_1b.background_normal, \
    self.ids.h8_2b.background_normal, \
    self.ids.h8_3b.background_normal, \
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.z3_1b.background_normal, \
    self.ids.z3_2b.background_normal, \
    self.ids.z10_1b.background_normal, \
    self.ids.z10_2b.background_normal, \
    self.ids.z5_1b.background_normal, \
    self.ids.z5_2b.background_normal, \
    self.ids.z11_1b.background_normal, \
    self.ids.z11_2b.background_normal, = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def right_up(self):
    default_xfiv_k = self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
                     self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value
    positi_secon_k = self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
                     self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
                     self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value
    positi_thirt_k = self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
                     self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value, \
                     self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value
    positi_fourt_k = self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
                     self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value
    self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
    self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
    self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value, = default_xfiv_k
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, = positi_fourt_k
    self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value, \
    self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value, \
    self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, = positi_secon_k
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value, \
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, = positi_thirt_k
    default_xfiv_l = self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
                     self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value
    positi_secon_l = self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
                     self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value
    positi_thirt_l = self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value, \
                     self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value
    positi_fourt_l = self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
                     self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value
    self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value, \
    self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value = default_xfiv_l
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value = positi_fourt_l
    self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
    self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value = positi_secon_l
    self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value, \
    self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value = positi_thirt_l
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25B3\u25E8]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xfiv_l, positi_secon_l, positi_thirt_l, positi_fourt_l


def right_down(self):
    default_xfiv_m = self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
                     self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value
    positi_secon_m = self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
                     self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
                     self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value
    positi_thirt_m = self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
                     self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value, \
                     self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value
    positi_fourt_m = self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
                     self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value
    self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value, \
    self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
    self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, = positi_thirt_m
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, = positi_secon_m
    self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value, \
    self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value, \
    self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, = positi_fourt_m
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value, = default_xfiv_m
    default_xfiv_n = self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value, \
                     self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value
    positi_secon_n = self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
                     self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value
    positi_thirt_n = self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value, \
                     self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value
    positi_fourt_n = self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
                     self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value
    self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value, \
    self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value = positi_thirt_n
    self.ids.z3_1b.text, self.ids.z3_1b.color, self.ids.z3_1b.background_color, self.ids.z3_1b.value, \
    self.ids.z3_2b.text, self.ids.z3_2b.color, self.ids.z3_2b.background_color, self.ids.z3_2b.value = positi_secon_n
    self.ids.z5_1b.text, self.ids.z5_1b.color, self.ids.z5_1b.background_color, self.ids.z5_1b.value, \
    self.ids.z5_2b.text, self.ids.z5_2b.color, self.ids.z5_2b.background_color, self.ids.z5_2b.value = positi_fourt_n
    self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value, \
    self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value = default_xfiv_n
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25BD\u25E8]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xfiv_n, positi_secon_n, positi_thirt_n, positi_fourt_n


def up_right_leftx(self):
    self.ids.h6_1b.background_normal, \
    self.ids.h6_2b.background_normal, \
    self.ids.h6_3b.background_normal, \
    self.ids.h5_1b.background_normal, \
    self.ids.h5_2b.background_normal, \
    self.ids.h5_3b.background_normal, \
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.z9_1b.background_normal, \
    self.ids.z9_2b.background_normal, \
    self.ids.z6_1b.background_normal, \
    self.ids.z6_2b.background_normal, \
    self.ids.z10_1b.background_normal, \
    self.ids.z10_2b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.z2_2b.background_normal, = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def up_right_leftz(self):
    self.ids.h6_1b.background_normal, \
    self.ids.h6_2b.background_normal, \
    self.ids.h6_3b.background_normal, \
    self.ids.h5_1b.background_normal, \
    self.ids.h5_2b.background_normal, \
    self.ids.h5_3b.background_normal, \
    self.ids.h2_1b.background_normal, \
    self.ids.h2_2b.background_normal, \
    self.ids.h2_3b.background_normal, \
    self.ids.h1_1b.background_normal, \
    self.ids.h1_2b.background_normal, \
    self.ids.h1_3b.background_normal, \
    self.ids.z9_1b.background_normal, \
    self.ids.z9_2b.background_normal, \
    self.ids.z6_1b.background_normal, \
    self.ids.z6_2b.background_normal, \
    self.ids.z10_1b.background_normal, \
    self.ids.z10_2b.background_normal, \
    self.ids.z2_1b.background_normal, \
    self.ids.z2_2b.background_normal, = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def up_right(self):
    default_xsix_o = self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value, \
                     self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
                     self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value
    positi_secon_o = self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value, \
                     self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
                     self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value
    positi_thirt_o = self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
                     self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value
    positi_fourt_o = self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
                     self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value, \
                     self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value
    self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
    self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
    self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value, = positi_thirt_o
    self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value, \
    self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
    self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value, = positi_secon_o
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, = positi_fourt_o
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value, = default_xsix_o
    default_xsix_p = self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
                     self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value
    positi_secon_p = self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, \
                     self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value
    positi_thirt_p = self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
                     self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value
    positi_fourt_p = self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
                     self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value
    self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
    self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value, = positi_secon_p
    self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, \
    self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value, = positi_thirt_p
    self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
    self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value, = positi_fourt_p
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value, = default_xsix_p
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B12\u25B6]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xsix_p, positi_secon_p, positi_thirt_p, positi_fourt_p


def up_left(self):
    default_xsix_q = self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value, \
                     self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
                     self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value
    positi_secon_q = self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
                     self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value, \
                     self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value
    positi_thirt_q = self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
                     self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value, \
                     self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value
    positi_fourt_q = self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value, \
                     self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
                     self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value
    self.ids.h5_3b.text, self.ids.h5_3b.color, self.ids.h5_3b.background_color, self.ids.h5_3b.value, \
    self.ids.h5_1b.text, self.ids.h5_1b.color, self.ids.h5_1b.background_color, self.ids.h5_1b.value, \
    self.ids.h5_2b.text, self.ids.h5_2b.color, self.ids.h5_2b.background_color, self.ids.h5_2b.value = default_xsix_q
    self.ids.h6_3b.text, self.ids.h6_3b.color, self.ids.h6_3b.background_color, self.ids.h6_3b.value, \
    self.ids.h6_2b.text, self.ids.h6_2b.color, self.ids.h6_2b.background_color, self.ids.h6_2b.value, \
    self.ids.h6_1b.text, self.ids.h6_1b.color, self.ids.h6_1b.background_color, self.ids.h6_1b.value = positi_fourt_q
    self.ids.h2_1b.text, self.ids.h2_1b.color, self.ids.h2_1b.background_color, self.ids.h2_1b.value, \
    self.ids.h2_2b.text, self.ids.h2_2b.color, self.ids.h2_2b.background_color, self.ids.h2_2b.value, \
    self.ids.h2_3b.text, self.ids.h2_3b.color, self.ids.h2_3b.background_color, self.ids.h2_3b.value = positi_secon_q
    self.ids.h1_2b.text, self.ids.h1_2b.color, self.ids.h1_2b.background_color, self.ids.h1_2b.value, \
    self.ids.h1_1b.text, self.ids.h1_1b.color, self.ids.h1_1b.background_color, self.ids.h1_1b.value, \
    self.ids.h1_3b.text, self.ids.h1_3b.color, self.ids.h1_3b.background_color, self.ids.h1_3b.value = positi_thirt_q
    default_xsix_r = self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
                     self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value
    positi_secon_r = self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, \
                     self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value
    positi_thirt_r = self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
                     self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value
    positi_fourt_r = self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
                     self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value
    self.ids.z9_2b.text, self.ids.z9_2b.color, self.ids.z9_2b.background_color, self.ids.z9_2b.value, \
    self.ids.z9_1b.text, self.ids.z9_1b.color, self.ids.z9_1b.background_color, self.ids.z9_1b.value = positi_fourt_r
    self.ids.z6_2b.text, self.ids.z6_2b.color, self.ids.z6_2b.background_color, self.ids.z6_2b.value, \
    self.ids.z6_1b.text, self.ids.z6_1b.color, self.ids.z6_1b.background_color, self.ids.z6_1b.value = default_xsix_r
    self.ids.z10_2b.text, self.ids.z10_2b.color, self.ids.z10_2b.background_color, self.ids.z10_2b.value, \
    self.ids.z10_1b.text, self.ids.z10_1b.color, self.ids.z10_1b.background_color, self.ids.z10_1b.value = positi_secon_r
    self.ids.z2_2b.text, self.ids.z2_2b.color, self.ids.z2_2b.background_color, self.ids.z2_2b.value, \
    self.ids.z2_1b.text, self.ids.z2_1b.color, self.ids.z2_1b.background_color, self.ids.z2_1b.value = positi_thirt_r
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25C0\u2B12]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xsix_r, positi_secon_r, positi_thirt_r, positi_fourt_r


def down_right_leftx(self):
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.h8_1b.background_normal, \
    self.ids.h8_2b.background_normal, \
    self.ids.h8_3b.background_normal, \
    self.ids.h7_1b.background_normal, \
    self.ids.h7_2b.background_normal, \
    self.ids.h7_3b.background_normal, \
    self.ids.z12_1b.background_normal, \
    self.ids.z12_2b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z4_2b.background_normal, \
    self.ids.z11_1b.background_normal, \
    self.ids.z11_2b.background_normal, \
    self.ids.z8_1b.background_normal, \
    self.ids.z8_2b.background_normal, = \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal, \
        self.ids.dum5.background_normal


def down_right_leftz(self):
    self.ids.h3_1b.background_normal, \
    self.ids.h3_2b.background_normal, \
    self.ids.h3_3b.background_normal, \
    self.ids.h4_1b.background_normal, \
    self.ids.h4_2b.background_normal, \
    self.ids.h4_3b.background_normal, \
    self.ids.h8_1b.background_normal, \
    self.ids.h8_2b.background_normal, \
    self.ids.h8_3b.background_normal, \
    self.ids.h7_1b.background_normal, \
    self.ids.h7_2b.background_normal, \
    self.ids.h7_3b.background_normal, \
    self.ids.z12_1b.background_normal, \
    self.ids.z12_2b.background_normal, \
    self.ids.z4_1b.background_normal, \
    self.ids.z4_2b.background_normal, \
    self.ids.z11_1b.background_normal, \
    self.ids.z11_2b.background_normal, \
    self.ids.z8_1b.background_normal, \
    self.ids.z8_2b.background_normal, = \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal, \
        self.ids.dum1.background_normal


def down_right(self):
    default_xsev_s = self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value, \
                     self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value
    positi_secon_s = self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value, \
                     self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value
    positi_thirt_s = self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
                     self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value, \
                     self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value
    positi_fourt_s = self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
                     self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
                     self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value = default_xsev_s
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = positi_fourt_s
    self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
    self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value, \
    self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value = positi_secon_s
    self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
    self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
    self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value = positi_thirt_s
    default_xsev_t = self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
                     self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value
    positi_secon_t = self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
                     self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value
    positi_thirt_t = self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
                     self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value
    positi_fourt_t = self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
                     self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value = default_xsev_t
    self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
    self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value = positi_fourt_t
    self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
    self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value = positi_secon_t
    self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
    self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value = positi_thirt_t
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u2B13\u25B6]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xsev_t, positi_secon_t, positi_thirt_t, positi_fourt_t


def down_left(self):
    default_xsev_u = self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
                     self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
                     self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value
    positi_secon_u = self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
                     self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value, \
                     self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value
    positi_thirt_u = self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
                     self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value, \
                     self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value
    positi_fourt_u = self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
                     self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
                     self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value
    self.ids.h3_2b.text, self.ids.h3_2b.color, self.ids.h3_2b.background_color, self.ids.h3_2b.value, \
    self.ids.h3_1b.text, self.ids.h3_1b.color, self.ids.h3_1b.background_color, self.ids.h3_1b.value, \
    self.ids.h3_3b.text, self.ids.h3_3b.color, self.ids.h3_3b.background_color, self.ids.h3_3b.value = positi_thirt_u
    self.ids.h4_1b.text, self.ids.h4_1b.color, self.ids.h4_1b.background_color, self.ids.h4_1b.value, \
    self.ids.h4_2b.text, self.ids.h4_2b.color, self.ids.h4_2b.background_color, self.ids.h4_2b.value, \
    self.ids.h4_3b.text, self.ids.h4_3b.color, self.ids.h4_3b.background_color, self.ids.h4_3b.value = positi_secon_u
    self.ids.h8_1b.text, self.ids.h8_1b.color, self.ids.h8_1b.background_color, self.ids.h8_1b.value, \
    self.ids.h8_3b.text, self.ids.h8_3b.color, self.ids.h8_3b.background_color, self.ids.h8_3b.value, \
    self.ids.h8_2b.text, self.ids.h8_2b.color, self.ids.h8_2b.background_color, self.ids.h8_2b.value = positi_fourt_u
    self.ids.h7_2b.text, self.ids.h7_2b.color, self.ids.h7_2b.background_color, self.ids.h7_2b.value, \
    self.ids.h7_3b.text, self.ids.h7_3b.color, self.ids.h7_3b.background_color, self.ids.h7_3b.value, \
    self.ids.h7_1b.text, self.ids.h7_1b.color, self.ids.h7_1b.background_color, self.ids.h7_1b.value = default_xsev_u
    default_xsev_v = self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
                     self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value
    positi_secon_v = self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
                     self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value
    positi_thirt_v = self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
                     self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value
    positi_fourt_v = self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
                     self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value
    self.ids.z4_2b.text, self.ids.z4_2b.color, self.ids.z4_2b.background_color, self.ids.z4_2b.value, \
    self.ids.z4_1b.text, self.ids.z4_1b.color, self.ids.z4_1b.background_color, self.ids.z4_1b.value = positi_thirt_v
    self.ids.z12_2b.text, self.ids.z12_2b.color, self.ids.z12_2b.background_color, self.ids.z12_2b.value, \
    self.ids.z12_1b.text, self.ids.z12_1b.color, self.ids.z12_1b.background_color, self.ids.z12_1b.value = positi_secon_v
    self.ids.z11_2b.text, self.ids.z11_2b.color, self.ids.z11_2b.background_color, self.ids.z11_2b.value, \
    self.ids.z11_1b.text, self.ids.z11_1b.color, self.ids.z11_1b.background_color, self.ids.z11_1b.value = positi_fourt_v
    self.ids.z8_2b.text, self.ids.z8_2b.color, self.ids.z8_2b.background_color, self.ids.z8_2b.value, \
    self.ids.z8_1b.text, self.ids.z8_1b.color, self.ids.z8_1b.background_color, self.ids.z8_1b.value = default_xsev_v
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"[\u25C0\u2B13]"]
    self.AANTAL_Twistys = self.AANTAL_Twistys - 1
    return default_xsev_v, positi_secon_v, positi_thirt_v, positi_fourt_v


def up_hole(self):
    self.midle_up()
    self.right_up()
    self.left_up()
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"<\u23EB>"]
    self.AANTAL_Twistys = self.AANTAL_Twistys + 3


def down_hole(self):
    self.midle_down()
    self.right_down()
    self.left_down()
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"<\u23EC>"]
    self.AANTAL_Twistys = self.AANTAL_Twistys + 3


def left_hole(self):
    self.midle_left()
    self.up_left()
    self.down_left()
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"<\u23EA>"]
    self.AANTAL_Twistys = self.AANTAL_Twistys + 3


def right_hole(self):
    self.midle_right()
    self.up_right()
    self.down_right()
    self.HISTORY_twists.pop()
    self.HISTORY_twists[:0] = [u"<\u23E9>"]
    self.AANTAL_Twistys = self.AANTAL_Twistys + 3