from manim import *

class Demo(Scene):
    def construct(self):
        text = Text('Hello, world!')
        self.play(Write(text))