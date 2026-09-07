from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MatrixRank(VoiceoverScene):
    def construct(self):
        philosophy_text = Text("", font_size=52, color=WHITE)


        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        BLUE_ACCENT = "#2196F3"
        RED_ALERT = "#FF2400"
        YELLOW = "#FFFF00"
        self.set_speech_service(GTTSService(lang="en"))


        sub_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=4.5, color=RED_ALERT).set_fill(RED_ALERT, opacity=1)
        sub_text = Text("SUBSCRIBE", font_size=40, weight=BOLD).move_to(sub_box)
        sub_btn = VGroup(sub_box, sub_text)
        
       

        with self.voiceover(text="...then you are in exactly the right place. Hit that subscribe button.") as tracker:
            self.play(ReplacementTransform(philosophy_text, sub_btn), run_time=tracker.duration * 0.5)
            self.play(sub_box.animate.set_fill(GRAY, opacity=1).set_color(GRAY), run_time=tracker.duration * 0.2)