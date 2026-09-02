from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BernoulliVarianceAndInertia(VoiceoverScene):
    def construct(self):
        
        # COLOR PALETTE & ENVIRONMENT SETUP
        
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        self.camera.background_color = BG_COLOR

        self.set_speech_service(GTTSService(lang="en"))

        # Pre-build the scene from the end of Part 1 (Lever balanced at p = 0.5)
        lever = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE, stroke_width=4).shift(DOWN * 1.5)
        dot_0_pos = lever.get_left()
        dot_1_pos = lever.get_right()
        
        mass_0 = Circle(radius=0.5, color=ICE_CYAN, fill_opacity=0.6).move_to(dot_0_pos)
        mass_1 = Circle(radius=0.5, color=NEON_GREEN, fill_opacity=0.6).move_to(dot_1_pos)
        fulcrum = Polygon(
            ORIGIN, LEFT * 0.25 + DOWN * 0.4, RIGHT * 0.25 + DOWN * 0.4,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.8
        ).next_to(lever.get_center(), DOWN, buff=0)

        # We keep the physical parts inside a VGroup so we can rotate them together
        physics_group = VGroup(lever, mass_0, mass_1)
        self.add(physics_group, fulcrum)

        
        #  25: Variance = Spread
        
        var_text = Text("Variance = Spread", font_size=40, color=WHITE).shift(UP * 2)
        with self.voiceover(text="In statistics, variance measures how much our possible outcomes are spread out from the expected value.") as tracker:
            self.play(FadeIn(var_text, shift=DOWN), run_time=tracker.duration)

        
        #  26: Rotational Inertia
        
        torque_arrows = VGroup(
            CurvedArrow(fulcrum.get_top() + LEFT + UP*0.5, fulcrum.get_top() + RIGHT + UP*0.5, angle=-PI/2, color=YELLOW),
            CurvedArrow(fulcrum.get_top() + RIGHT + DOWN*0.5, fulcrum.get_top() + LEFT + DOWN*0.5, angle=-PI/2, color=YELLOW)
        )
        with self.voiceover(text="Physically, this is exactly the same as rotational inertia—how much effort it takes to spin our balanced rod.") as tracker:
            self.play(Create(torque_arrows), run_time=tracker.duration)

        
        #  27: Fair coin at p=0.5
        
        with self.voiceover(text="When our coin is perfectly fair, the chance of success is fifty percent. The two masses are equal...") as tracker:
            self.play(FadeOut(torque_arrows), FadeOut(var_text), run_time=tracker.duration)

        
        #  28: Sluggish Spin (High Inertia)
        
        with self.voiceover(text="...and because they sit far from the center pivot, the system fiercely resists being rotated. High inertia means high variance.") as tracker:
            # We simulate "sluggish" rotation by using a slow rate_func
            self.play(
                Rotate(physics_group, angle=PI, about_point=fulcrum.get_top(), rate_func=there_and_back),
                run_time=tracker.duration
            )

        
        #  29: Slider to p = 0.9
        
        slider_line = Line(LEFT * 2, RIGHT * 2, color=WHITE).shift(DOWN * 3)
        slider_dot = Dot(slider_line.get_center(), color=ICE_CYAN)
        p_label = MathTex("p = 0.5").next_to(slider_dot, UP)
        
        with self.voiceover(text="But watch what happens if we use a loaded coin, say, a ninety percent chance of success.") as tracker:
            self.play(Create(slider_line), FadeIn(slider_dot), FadeIn(p_label), run_time=tracker.duration)

        
        #  30: Adjusting mass sizes and moving fulcrum
        
        target_p = 0.9
        new_fulcrum_pos = lever.point_from_proportion(target_p) + DOWN * 0.2
        target_slider_dot = slider_line.point_from_proportion(target_p)
        new_p_label = MathTex("p = 0.9").next_to(target_slider_dot, UP)

        with self.voiceover(text="The success mass becomes massive, and the fulcrum must shift to the far right to maintain equilibrium.") as tracker:
            self.play(
                mass_1.animate.scale(1.8),
                mass_0.animate.scale(0.3),
                fulcrum.animate.move_to(new_fulcrum_pos),
                slider_dot.animate.move_to(target_slider_dot),
                Transform(p_label, new_p_label),
                run_time=tracker.duration
            )

        
        #  31: Mass concentrated at pivot
        
        with self.voiceover(text="Now, almost all the physical mass is concentrated directly on top of the pivot point.") as tracker:
            self.play(Indicate(mass_1, color=NEON_GREEN, scale_factor=1.1), run_time=tracker.duration)

        
        #  32: Fast Spin (Low Inertia)
        
        with self.voiceover(text="Spinning the rod becomes incredibly easy. The variance shrinks because we are almost certain to get a success.") as tracker:
            # We simulate "fast/easy" rotation by spinning it multiple times quickly
            self.play(
                Rotate(physics_group, angle=4*PI, about_point=fulcrum.get_top(), rate_func=smooth),
                run_time=tracker.duration
            )

        
        #  33: Variance Formula
        
        variance_formula = MathTex(r"\text{Var}(X) = p(1-p)", font_size=52, color=NEON_GREEN).shift(UP * 2.5)
        
        with self.voiceover(text="The mathematics elegantly mirror this physical reality. The variance is strictly defined as p times one minus p.") as tracker:
            self.play(
                FadeOut(physics_group), FadeOut(fulcrum), FadeOut(slider_line), FadeOut(slider_dot), FadeOut(p_label),
                Write(variance_formula),
                run_time=tracker.duration
            )

        
        #  34: The Parabola
        
        axes = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 0.3, 0.1], 
            x_length=6, y_length=3,
            axis_config={"color": WHITE, "include_numbers": False}
        ).shift(DOWN * 0.5)
        
        parabola = axes.plot(lambda x: x * (1 - x), color=NEON_GREEN, stroke_width=4)
        
        with self.voiceover(text="If we plot this rotational resistance across every possible probability, a beautiful parabola emerges.") as tracker:
            self.play(Create(axes), Create(parabola), run_time=tracker.duration)

        
        #  35: Peak at 0.5
        
        peak_dot = Dot(axes.c2p(0.5, 0.25), color=ICE_CYAN).scale(1.5)
        peak_line = axes.get_vertical_line(axes.c2p(0.5, 0.25), color=ICE_CYAN, line_func=DashedLine)
        peak_label = MathTex("0.5", color=ICE_CYAN).next_to(peak_line, DOWN)
        
        with self.voiceover(text="The uncertainty hits absolute zero at the extreme ends, and reaches its maximum peak right at fifty-fifty.") as tracker:
            self.play(Create(peak_line), FadeIn(peak_dot), Write(peak_label), run_time=tracker.duration)

        
        #  36: Conclusion Zoom
        
        with self.voiceover(text="This simple geometric truth is the bedrock for everything from casino odds to modern machine learning models.") as tracker:
            self.play(
                VGroup(axes, parabola, peak_dot, peak_line, peak_label, variance_formula).animate.scale(0.8),
                run_time=tracker.duration
            )
        
        self.wait(1)
