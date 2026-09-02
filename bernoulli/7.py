from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import random

class BernoulliPuzzleAndOutro(VoiceoverScene):
    def construct(self):
        
        # COLOR PALETTE & SETUP
        
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        YELLOW = "#FFFF00"
        
        self.camera.background_color = BG_COLOR
        self.set_speech_service(GTTSService(lang="en"))

        
        #  73: Chaining the Levers
        
        start_point = LEFT * 5
        current_point = start_point
        levers = VGroup()
        
        # Create a jagged random walk path
        for i in range(8):
            direction = UP if i % 2 == 0 else DOWN
            next_point = current_point + RIGHT * 1.2 + direction * 0.8
            lever = Line(current_point, next_point, color=ICE_CYAN, stroke_width=4)
            fulcrum = Dot(current_point, color=YELLOW, radius=0.1)
            levers.add(lever, fulcrum)
            current_point = next_point
            
        levers.add(Dot(current_point, color=YELLOW, radius=0.1)) # final dot

        with self.voiceover(text="Wait a minute, before you go, I want to leave you pondering a puzzle: If we take these individual, isolated Bernoulli levers and chain them together tip-to-tail in a sequence, we create a random walk—the foundation of the Binomial distribution.") as tracker:
            self.play(Create(levers, lag_ratio=1), run_time=tracker.duration)

        
        #  74: To Infinity
        
        infinity_math = MathTex(r"n \to \infty", font_size=72, color=NEON_GREEN).shift(UP * 2)
        question_math = MathTex(r"\mathbb{E}[X] = ? \quad \text{Var}(X) = ?", font_size=56, color=WHITE).next_to(infinity_math, DOWN, buff=0.5)
        
        with self.voiceover(text="What do you think happens to the center of gravity and the rotational inertia as that sequence grows to infinity?") as tracker:
            self.play(levers.animate.set_stroke(opacity=0.3).set_fill(opacity=0.3))
            self.play(Write(infinity_math), Write(question_math), run_time=tracker.duration - 1)

        
        #  75: Community CTA
        
        comment_box = RoundedRectangle(corner_radius=0.3, width=6, height=2, color=WHITE).set_fill(WHITE, opacity=0.1)
        comment_text = Text("Leave your answer below!", font_size=32, color=YELLOW).move_to(comment_box)
        comment_group = VGroup(comment_box, comment_text)

        with self.voiceover(text="Take a stab at it yourself in the comments below, and be social about it—it always helps to recruit other smart minds to the task.") as tracker:
            self.play(FadeOut(levers), FadeOut(infinity_math), FadeOut(question_math))
            self.play(FadeIn(comment_group, shift=UP), run_time=tracker.duration)

        
        #  76: GitHub & Code
        
        terminal_window = RoundedRectangle(corner_radius=0.2, width=8, height=4, color=GRAY).set_fill("#1E1E1E", opacity=1)
        code_text_1 = Text("git clone https://github.com/...", font_size=24, color=NEON_GREEN, font="monospace").shift(UP*0.5 + LEFT*1)
        code_text_2 = Text("manim -pqh script.py", font_size=24, color=WHITE, font="monospace").next_to(code_text_1, DOWN, aligned_edge=LEFT)
        code_group = VGroup(terminal_window, code_text_1, code_text_2)

        with self.voiceover(text="If you are itching to look under the hood of the animations you saw today, I have uploaded the complete, open-source Python code repositories for this video. In the public GitHub repository linked in the description below, you will find the documented python scripts.") as tracker:
            self.play(ReplacementTransform(comment_group, code_group), run_time=tracker.duration * 0.4)
            self.play(Write(code_text_1), Write(code_text_2), run_time=tracker.duration * 0.6)

        
        #  77: The Final Stretch
        
        stretch_text = Text("Stand up. Stretch. Let it settle.", font_size=42, weight=BOLD, color=ICE_CYAN)

        with self.voiceover(text="Because the intricacy of these connections is worth absorbing, I want you to take a brief moment to just stand up, stretch out, and let this physical intuition settle deep into your mind.") as tracker:
            self.play(FadeOut(code_group))
            self.play(FadeIn(stretch_text), run_time=tracker.duration * 0.4)
            self.play(FadeOut(stretch_text, run_time=tracker.duration * 0.6))
            
        self.wait(2)
