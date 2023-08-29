from manim import *
from manim_fonts import *
from manim.mobject.text.text_mobject import remove_invisible_chars

class ChannelsIntro(Scene):
    def construct(self):
        logo_source = "Go.svg"

        logo = SVGMobject(logo_source).scale(1)
        title =  Text ("Channels",
            font="",
            font_size=64,
            weight=BOLD,
        ).next_to(logo, RIGHT)
        group = VGroup(logo, title)

        self.play(Create(logo), run_time=1)
        self.wait(0.5)
        self.play(Write(title), group.animate.move_to(ORIGIN))
        self.wait(2)
        self.play(Uncreate(group))

class GoChannels(Scene):
    def construct(self):
        code = """
        package main

        func main() {
            ch := make(chan int)
        }
        """
        gopher_source = "gopher.svg"

        code = Code(
            code=code,
            insert_line_no=False,
            language="golang",
            style="monokai",
            background_stroke_width=0,
        )
        gopher1 = SVGMobject(gopher_source).move_to(DOWN+LEFT*3).flip()
        gopher2 = SVGMobject(gopher_source).move_to(DOWN+RIGHT*3)

        self.play(Write(code.code))
        self.play(code.code.animate.to_edge(UL))
        self.play(Indicate(code.code[3][4:]))
        self.play(FadeIn(gopher1), FadeIn(gopher2))
        self.wait(1)

class Episode(Scene):
    def construct(self):
        ChannelsIntro.construct(self)
        GoChannels.construct(self)