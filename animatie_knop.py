from kivy.animation import Animation

def top_colorstonew(self, widget, *args):
    animate = Animation(size_hint=(0.05, 1), duration=(0.3), background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(0.05, 1), duration=(0.3), background_color=(77 / 255, 0 / 255, 170 / 255, 0.1))
    animate.start(widget)


def top_colorstonex(self, widget, *args):
    animate = Animation(size_hint=(0.1, 0.09), duration=(0.3), background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(0.1, 0.09), duration=(0.3), background_color=(1/255, 200/255, 255/255, 0.5))
    animate.start(widget)


def top_colorstoney(self, widget, *args):
    animate = Animation(size_hint=(0.05, 1), duration=(0.3), background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(0.05, 1), duration=(0.3), background_color=(77 / 255, 0 / 255, 170 / 255, 0))
    animate.start(widget)


def top_colorstonez(self, widget, *args):
    animate = Animation(size_hint=(0.1, 1), duration=(0.3), background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(0.1, 1), duration=(0.3), background_color=(77 / 255, 0 / 255, 170 / 255, 0.1))
    animate.start(widget)


def ani_anystone(self, widget, *args):
    animate = Animation(size_hint=(0, 0), duration=(0.5), background_color=(0 / 255, 0 / 255, 0 / 255, 1))
    animate += Animation(size_hint=(1, 1), duration=(1), background_color=(90 / 255, 90 / 255, 90 / 255, 1))
    animate.start(widget)


def ani_grey(self, widget, *args):
    animate = Animation(size_hint=(1, 1), duration=0.3, background_color=(206 / 255, 0 / 255, 0 / 255, 1))
    animate += Animation(size_hint=(1, 1), duration=0.7, background_color=(0 / 255, 10 / 255, 90 / 255, 0))
    animate.start(widget)


def ani_darkgrey(self, widget, *args):
    animate = Animation(size_hint=(1, 1), duration=0.3, background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(1, 1), duration=0.7, background_color=(0 / 255, 10 / 255, 70 / 255, 0))
    animate.start(widget)


def ani_darkgrey_holex(self, widget, *args):
    animate = Animation(size_hint=(1.5, 1), duration=0.3, background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(1.5, 1), duration=0.7, background_color=(0 / 255, 10 / 255, 70 / 255, 0))
    animate.start(widget)


def ani_darkgrey_holey(self, widget, *args):
    animate = Animation(size_hint=(1, 2), duration=0.3, background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(1, 2), duration=0.7, background_color=(0 / 255, 10 / 255, 70 / 255, 0))
    animate.start(widget)


def ani_darkgrey_holez(self, widget, *args):
    animate = Animation(size_hint=(1, 2), duration=0.3, background_color=(255 / 255, 95 / 255, 1 / 255, 1))
    animate += Animation(size_hint=(1, 2), duration=0.7, background_color=(0 / 255, 10 / 255, 70 / 255, 0))
    animate.start(widget)


def ani_green_one(self, widget, *args):
    animate = Animation(background_color=(164 / 255, 255 / 255, 160 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_green_two(self, widget, *args):
    animate = Animation(background_color=(64 / 255, 226 / 255, 160 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_pink_one(self, widget, *args):
    animate = Animation(background_color=(255 / 255, 102 / 255, 102 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_pink_two(self, widget, *args):
    animate = Animation(background_color=(255 / 255, 147 / 255, 147 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_blue_one(self, widget, *args):
    animate = Animation(background_color=(190 / 255, 240 / 255, 255 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_blue_two(self, widget, *args):
    animate = Animation(background_color=(124 / 255, 178 / 255, 232 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_purp_one(self, widget, *args):
    animate = Animation(background_color=(220 / 255, 105 / 255, 248 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)


def ani_purp_two(self, widget, *args):
    animate = Animation(background_color=(240 / 255, 170 / 255, 248 / 255, 1), duration=0.3)
    animate += Animation(background_color=(0 / 255, 33 / 255, 138 / 255, 0), duration=0.7)
    animate.start(widget)