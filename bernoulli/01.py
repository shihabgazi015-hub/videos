from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import random

class BernoulliHook(VoiceoverScene):
    def construct(self):
        # ---------------------------------------------------------
        # ENVIRONMENT & THEME SETUP
        # ---------------------------------------------------------
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        
        self.camera.background_color = BG_COLOR
        
        # Initialize Voiceover Service
        # Requires AZURE_SPEECH_KEY and AZURE_SPEECH_REGION environment variables
        self.set_speech_service(
            GTTSService(lang="en")
        )

        # ---------------------------------------------------------
        # SCENE BEATS
        # ---------------------------------------------------------
        
        # BEAT 1: The initial coin
        coin = Circle(radius=1.5, color=NEON_GREEN).set_fill(NEON_GREEN, opacity=0.1)
        with self.voiceover(text="Sometimes, math and physics conspire in ways that just feel too good to be true.") as tracker:
            self.play(Create(coin), run_time=tracker.duration)

        # BEAT 2: Spin and vectors
        arrow_up = Arrow(ORIGIN, UP*2.5, color=NEON_GREEN, stroke_width=6)
        arrow_down = Arrow(ORIGIN, DOWN*2.5, color=ICE_CYAN, stroke_width=6)
        with self.voiceover(text="Consider the act of flipping a coin. It’s the universal symbol of pure randomness.") as tracker:
            self.play(
                Rotate(coin, angle=PI, axis=UP, rate_func=smooth),
                GrowArrow(arrow_up),
                GrowArrow(arrow_down),
                run_time=tracker.duration
            )

        # BEAT 3: Split screen 1 and 0
        left_text = Text("1", font_size=144, color=NEON_GREEN).shift(LEFT * 3)
        right_text = Text("0", font_size=144, color=ICE_CYAN).shift(RIGHT * 3)
        divider = Line(UP * 4, DOWN * 4, color=WHITE, stroke_opacity=0.5)
        split_group = VGroup(left_text, right_text, divider)
        
        with self.voiceover(text="A binary fork in the road where the universe splits: success or failure, one or zero.") as tracker:
            self.play(
                ReplacementTransform(VGroup(coin, arrow_up, arrow_down), split_group),
                run_time=tracker.duration
            )

        # BEAT 4: Zoom out to geometric grid
        grid_points = VGroup(*[
            Dot(point=[x, y, 0], color=NEON_GREEN if (x+y)%2==0 else ICE_CYAN, radius=0.08)
            for x in range(-6, 7) for y in range(-4, 5)
        ])
        with self.voiceover(text="Now, zoom out from this single coin to look at something mind-bogglingly complex.") as tracker:
            self.play(
                ReplacementTransform(split_group, grid_points),
                run_time=tracker.duration
            )

        # BEAT 5: Neural network abstraction
        connections = VGroup()
        for _ in range(40):
            p1 = random.choice(grid_points)
            p2 = random.choice(grid_points)
            connections.add(Line(p1.get_center(), p2.get_center(), color=WHITE, stroke_opacity=0.2))
            
        with self.voiceover(text="Like a modern artificial intelligence weaving fluent paragraphs of prose out of raw data.") as tracker:
            self.play(
                Create(connections, lag_ratio=0.1),
                grid_points.animate.set_color(NEON_GREEN),
                run_time=tracker.duration
            )

        # BEAT 6: Binary code stream
        binary_stream = VGroup(*[
            Text(str(random.choice([0, 1])), font="Monospace", color=NEON_GREEN, font_size=24)
            .set_opacity(random.uniform(0.3, 1.0))
            for _ in range(50)
        ]).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        
        with self.voiceover(text="Or an efficient algorithm shrinking a massive video file into a tiny packet of code.") as tracker:
            self.play(
                ReplacementTransform(VGroup(grid_points, connections), binary_stream),
                binary_stream.animate.shift(LEFT * 3), 
                run_time=tracker.duration
            )

        # BEAT 7: Chaos and math symbols
        math_symbols = VGroup(
            MathTex(r"\sum", color=ICE_CYAN, font_size=96).shift(UP*2 + LEFT*3),
            MathTex(r"\int_0^1", color=NEON_GREEN, font_size=96).shift(DOWN*2 + RIGHT*2),
            MathTex(r"\sigma^2", color=WHITE, font_size=96).shift(UP*1.5 + RIGHT*3),
            MathTex(r"H(X)", color=ICE_CYAN, font_size=96).shift(DOWN*1.5 + LEFT*2)
        )
        with self.voiceover(text="At first, this might sound like complete nonsense. How could all this frenetic complexity...") as tracker:
            self.play(
                binary_stream.animate.scale(3).set_opacity(0).shift(RIGHT * 5), # Scatter binary
                FadeIn(math_symbols, shift=UP),
                run_time=tracker.duration
            )

        # BEAT 8: Collapse to coin
        single_coin = Circle(radius=1.2, color=NEON_GREEN).set_fill(NEON_GREEN, opacity=0.2)
        with self.voiceover(text="...of machine intelligence and information theory reduce down to a single, humble coin flip?") as tracker:
            self.play(
                ReplacementTransform(math_symbols, single_coin),
                run_time=tracker.duration
            )

        # BEAT 9: Lever and fulcrum
        lever = Line(LEFT * 3, RIGHT * 3, color=WHITE, stroke_width=4).shift(DOWN * 1.5)
        fulcrum = Triangle(color=ICE_CYAN).scale(0.3).next_to(lever, DOWN, buff=0)
        
        with self.voiceover(text="But I promise if you explain it the right way, it actually makes perfect sense.") as tracker:
            self.play(
                single_coin.animate.scale(0.5).next_to(lever, UP, buff=0),
                Create(lever),
                FadeIn(fulcrum, shift=UP),
                run_time=tracker.duration
            )

        # BEAT 10: Bernoulli formula
        formula = MathTex(r"X \sim \text{Bernoulli}(p)", font_size=64).shift(UP * 2)
        formula[0][8:9].set_color(NEON_GREEN) # Color the 'p'
        
        with self.voiceover(text="Underneath the surface of every complex system sits an anchor: the Bernoulli distribution.") as tracker:
            self.play(
                Write(formula),
                run_time=tracker.duration
            )

        # BEAT 11: The Variance Parabola
        axes = Axes(x_range=[0, 1, 0.5], y_range=[0, 0.3, 0.1], x_length=6, y_length=3).shift(DOWN * 0.5)
        parabola = axes.plot(lambda x: x * (1 - x), color=NEON_GREEN)
        
        with self.voiceover(text="It’s a simple equation, but why does this seemingly trivial concept hold the master key...") as tracker:
            self.play(
                FadeOut(single_coin, lever, fulcrum),
                Create(axes),
                Create(parabola),
                run_time=tracker.duration
            )

        # BEAT 12: Peak highlight
        peak_dot = Dot(axes.c2p(0.5, 0.25), color=ICE_CYAN).scale(1.5)
        glow = Dot(axes.c2p(0.5, 0.25), color=ICE_CYAN).scale(4).set_opacity(0.3)
        
        with self.voiceover(text="...to how we measure and quantify uncertainty across the entire cosmos?") as tracker:
            self.play(
                formula.animate.set_opacity(0.2),
                axes.animate.set_opacity(0.2),
                FadeIn(peak_dot),
                FadeIn(glow),
                run_time=tracker.duration
            )
        
        self.wait(1)
