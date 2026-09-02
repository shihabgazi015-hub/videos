from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class BernoulliIntroAndBalance(VoiceoverScene):
    def construct(self):
        
        # COLOR PALETTE & ENVIRONMENT
        
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"

        self.camera.background_color = BG_COLOR

        # Initialize free TTS service
        self.set_speech_service(GTTSService(lang="en"))

        
        #  13: Abstract Formulas & Cross-out
        
        bad_formula = MathTex(
            r"\mathbb{P}(X=x) = p^x (1-p)^{1-x}", font_size=44, color=WHITE
        ).shift(UP * 0.5)

        cross_line = Line(
            start=bad_formula.get_corner(UL) + LEFT * 0.2 + UP * 0.2,
            end=bad_formula.get_corner(DR) + RIGHT * 0.2 + DOWN * 0.2,
            color=RED,
            stroke_width=6,
        )

        with self.voiceover(
            text="Traditional pedagogical methods love to throw abstract symbols and dry formulas at you,"
        ) as tracker:
            self.play(Write(bad_formula), run_time=tracker.duration * 0.6)
            self.play(Create(cross_line), run_time=tracker.duration * 0.4)

        
        #  14: Fragile Rote Memorization
        
        rote_text = Text(
            "Fragile Rote Memorization", font_size=36, color=RED_B
        ).next_to(bad_formula, DOWN, buff=0.5)

        with self.voiceover(
            text="leaving you with a fragile, rote understanding of probability distributions."
        ) as tracker:
            self.play(FadeIn(rote_text, shift=UP), run_time=tracker.duration)

        
        #  15: Spatial & Geometric Discovery
        
        good_text = Text(
            "Active Geometric Discovery", font_size=40, color=NEON_GREEN
        )
        box = SurroundingRectangle(
            good_text, color=NEON_GREEN, buff=0.25, corner_radius=0.1
        )
        discovery_group = VGroup(good_text, box)

        with self.voiceover(
            text="But you and I are going to take a very different path—a path of active spatial and geometric discovery."
        ) as tracker:
            self.play(
                ReplacementTransform(
                    VGroup(bad_formula, cross_line, rote_text), discovery_group
                ),
                run_time=tracker.duration,
            )

        
        #  16: Setup Lever & Outcome Nodes
        
        lever = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE, stroke_width=4).shift(
            DOWN * 1.0
        )
        dot_0 = Dot(lever.get_left(), color=ICE_CYAN, radius=0.12)
        dot_1 = Dot(lever.get_right(), color=NEON_GREEN, radius=0.12)

        lbl_0 = MathTex(r"\text{Failure } (0)", font_size=32, color=ICE_CYAN).next_to(
            dot_0, DOWN, buff=0.3
        )
        lbl_1 = MathTex(
            r"\text{Success } (1)", font_size=32, color=NEON_GREEN
        ).next_to(dot_1, DOWN, buff=0.3)

        with self.voiceover(
            text="Let’s construct a simple game. Suppose we have a single trial with two outcomes: 0 and 1."
        ) as tracker:
            self.play(
                FadeOut(discovery_group),
                Create(lever),
                FadeIn(dot_0),
                FadeIn(dot_1),
                Write(lbl_0),
                Write(lbl_1),
                run_time=tracker.duration,
            )

        
        #  17: Probabilities p and 1-p
        
        p_lbl_0 = MathTex(r"1 - p", font_size=38, color=ICE_CYAN).next_to(
            dot_0, UP, buff=0.3
        )
        p_lbl_1 = MathTex(r"p", font_size=38, color=NEON_GREEN).next_to(
            dot_1, UP, buff=0.3
        )

        with self.voiceover(
            text="Let's call the chance of success p, which means the chance of failure is its complement, 1 minus p."
        ) as tracker:
            self.play(
                Write(p_lbl_0), Write(p_lbl_1), run_time=tracker.duration
            )

        
        #  18: Physical Mass Spheres
        
        mass_0 = Circle(
            radius=0.3, color=ICE_CYAN, fill_opacity=0.6
        ).move_to(dot_0.get_center())
        mass_1 = Circle(
            radius=0.3, color=NEON_GREEN, fill_opacity=0.6
        ).move_to(dot_1.get_center())

        with self.voiceover(
            text="Instead of treating these as abstract numbers, let's treat them as actual physical matter on a weightless rod."
        ) as tracker:
            self.play(
                ReplacementTransform(dot_0, mass_0),
                ReplacementTransform(dot_1, mass_1),
                run_time=tracker.duration,
            )

        
        #  19: Fulcrum at Center (p = 0.5)
        
        fulcrum = Polygon(
            ORIGIN,
            LEFT * 0.25 + DOWN * 0.4,
            RIGHT * 0.25 + DOWN * 0.4,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.8,
        ).next_to(lever.get_center(), DOWN, buff=0)

        with self.voiceover(
            text="Now, ask yourself: where would you slide a fulcrum so that the system sits in perfect equilibrium?"
        ) as tracker:
            self.play(FadeIn(fulcrum, shift=UP), run_time=tracker.duration)

        
        #  20: Biasing Success Mass (p -> 0.75)
        
        with self.voiceover(
            text="If our coin is fair, it balances right in the middle. But if we bias it toward success..."
        ) as tracker:
            self.play(
                mass_1.animate.scale(1.4).set_fill(opacity=0.9),
                mass_0.animate.scale(0.6).set_fill(opacity=0.3),
                run_time=tracker.duration,
            )

        
        #  21: Fulcrum Glides to Center of Mass (0.75 position)
        
        target_fulcrum_pos = lever.point_from_proportion(0.75) + DOWN * 0.2

        with self.voiceover(
            text="...the fulcrum must glide smoothly to the right, landing precisely under that coordinate."
        ) as tracker:
            self.play(
                fulcrum.animate.move_to(target_fulcrum_pos),
                run_time=tracker.duration,
            )

        
        #  22: Center of Gravity = Expected Value
        
        cog_title = Text(
            "Center of Gravity = Expected Value", font_size=32, color=YELLOW
        ).to_edge(UP, buff=0.8)

        arrow_to_fulcrum = Arrow(
            start=cog_title.get_bottom(),
            end=fulcrum.get_top() + UP * 0.1,
            color=YELLOW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )

        with self.voiceover(
            text="Physics tells us this balance point is the center of gravity. In statistics, we call it the expected value."
        ) as tracker:
            self.play(
                Write(cog_title),
                GrowArrow(arrow_to_fulcrum),
                run_time=tracker.duration,
            )

        
        #  23: Expectation Formula Derivation
        
        ev_formula = MathTex(
            r"\mathbb{E}[X] = 0(1-p) + 1(p) = p",
            font_size=42,
            color=NEON_GREEN,
        ).next_to(cog_title, DOWN, buff=0.4)

        with self.voiceover(
            text="The standard formula isn't an arbitrary rule. It is the inevitable geometric consequence of finding balance."
        ) as tracker:
            self.play(Write(ev_formula), run_time=tracker.duration)

        
        #  24: Teasing Rotational Motion / Variance
        
        scene_group = VGroup(
            lever,
            mass_0,
            mass_1,
            fulcrum,
            lbl_0,
            lbl_1,
            p_lbl_0,
            p_lbl_1,
            cog_title,
            arrow_to_fulcrum,
            ev_formula,
        )

        with self.voiceover(
            text="But what happens when we try to spin this system? That’s where variance comes alive."
        ) as tracker:
            self.play(
                Rotate(
                    lever,
                    angle=0.08,
                    about_point=fulcrum.get_top(),
                    rate_func=wiggle,
                ),
                scene_group.animate.set_opacity(0.3),
                run_time=tracker.duration,
            )

        self.wait(0.5)
