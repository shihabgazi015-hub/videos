from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BernoulliConclusion(VoiceoverScene):
    def construct(self):
        # ---------------------------------------------------------
        # COLOR PALETTE & ENVIRONMENT SETUP
        # ---------------------------------------------------------
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        BLUE_ACCENT = "#2196F3"
        RED_ALERT = "#FF2400"
        YELLOW = "#FFFF00"
        
        self.camera.background_color = BG_COLOR
        self.set_speech_service(GTTSService(lang="en"))

        # ---------------------------------------------------------
        # BEAT 61: A/B Testing Phones
        # ---------------------------------------------------------
        phone_a = RoundedRectangle(corner_radius=0.2, height=3.5, width=2, color=WHITE).shift(LEFT * 2.5)
        phone_b = RoundedRectangle(corner_radius=0.2, height=3.5, width=2, color=WHITE).shift(RIGHT * 2.5)
        
        btn_a = Rectangle(height=0.6, width=1.4, color=BLUE_ACCENT).set_fill(BLUE_ACCENT, opacity=0.8).move_to(phone_a)
        btn_b = Rectangle(height=0.6, width=1.4, color=NEON_GREEN).set_fill(NEON_GREEN, opacity=0.8).move_to(phone_b)
        
        lbl_a = Text("Version A", font_size=24).next_to(phone_a, UP)
        lbl_b = Text("Version B", font_size=24).next_to(phone_b, UP)

        with self.voiceover(text="So, where do you actually see this in your daily life? Take something like A/B testing on your favorite app.") as tracker:
            self.play(
                FadeIn(phone_a, shift=DOWN), FadeIn(phone_b, shift=DOWN),
                FadeIn(btn_a), FadeIn(btn_b),
                Write(lbl_a), Write(lbl_b),
                run_time=tracker.duration
            )

        # ---------------------------------------------------------
        # BEAT 62: Pure Bernoulli (1s and 0s)
        # ---------------------------------------------------------
        N = None
        stream_a = VGroup(*[Text(str(n), font_size=24, color=ICE_CYAN).move_to(phone_a.get_center() + UP*(i*0.5)) for i, n in enumerate([0, 1, 0, 0, 0, ])])
        stream_b = VGroup(*[Text(str(n), font_size=24, color=NEON_GREEN).move_to(phone_b.get_center() + UP*(i*0.5)) for i, n in enumerate([1, 1, 0, 1, 1, ])])

        with self.voiceover(text="Every time a user clicks a button, it’s a one. If they ignore it, it’s a zero. Pure Bernoulli.") as tracker:
            self.play(
                ApplyWave(btn_a), ApplyWave(btn_b),
                FadeIn(stream_a, shift=UP), FadeIn(stream_b, shift=UP),
                run_time=tracker.duration
            )

        # ---------------------------------------------------------
        # BEAT 63: Expected Value Comparison
        # ---------------------------------------------------------
        with self.voiceover(text="Tech giants stack millions of these simple coin flips to determine which version has a higher expected value.") as tracker:
            self.play(
                FadeOut(phone_a), FadeOut(phone_b), FadeOut(btn_a), FadeOut(btn_b), 
                FadeOut(stream_a), FadeOut(stream_b), FadeOut(lbl_a), FadeOut(lbl_b),
                run_time=tracker.duration
            )

        # ---------------------------------------------------------
        # BEAT 64: Real World Badges
        # ---------------------------------------------------------
        badge_med = Text("Medical Trials", font_size=36, color=ICE_CYAN).shift(UP * 1.5 + LEFT * 2)
        badge_wea = Text("Weather Models", font_size=36, color=NEON_GREEN).shift(UP * 1.5 + RIGHT * 2)
        badge_ele = Text("Election Forecasts", font_size=36, color=YELLOW).shift(DOWN * 1)
        
        lines = VGroup(
            Line(badge_med.get_bottom(), badge_ele.get_top(), color=WHITE, stroke_opacity=0.3),
            Line(badge_wea.get_bottom(), badge_ele.get_top(), color=WHITE, stroke_opacity=0.3),
            Line(badge_med.get_right(), badge_wea.get_left(), color=WHITE, stroke_opacity=0.3)
        )

        with self.voiceover(text="The exact same math applies to medical trials, weather forecasts, and predicting election outcomes.") as tracker:
            self.play(Write(badge_med), Write(badge_wea), Write(badge_ele), Create(lines), run_time=tracker.duration)

        # ---------------------------------------------------------
        # BEAT 65: Textbook & Memorization
        # ---------------------------------------------------------
        textbook = Rectangle(height=3, width=2.5, color=WHITE).set_fill(WHITE, opacity=0.1)
        book_title = Text("STATISTICS", font_size=28, weight=BOLD).move_to(textbook)
        book_group = VGroup(textbook, book_title)
        
       

        with self.voiceover(text="The secret to mastering statistics isn't cramming complex formulas into your head right before a test.") as tracker:
            self.play(FadeOut(badge_med, badge_wea, badge_ele, lines))
            self.play(FadeIn(book_group, shift=DOWN*2), run_time=tracker.duration * 0.6)
        # ---------------------------------------------------------
        # BEAT 66: Building Intuition (The Lever Returns)
        # ---------------------------------------------------------
        lever = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE, stroke_width=4)
        fulcrum = Triangle(color=YELLOW).scale(0.3).next_to(lever, DOWN, buff=0)
        mass_0 = Dot(lever.get_left(), color=ICE_CYAN, radius=0.2)
        mass_1 = Dot(lever.get_right(), color=NEON_GREEN, radius=0.4)
        beam_group = VGroup(lever, fulcrum, mass_0, mass_1).shift(DOWN*0.5)

        with self.voiceover(text="It’s about building a rock-solid, visual intuition for how systems naturally behave.") as tracker:
            self.play(ReplacementTransform(VGroup(book_group,  ), beam_group), run_time=tracker.duration)

        # ---------------------------------------------------------
        # BEAT 67: Equations Write Themselves
        # ---------------------------------------------------------
        ev_formula = MathTex(r"\mathbb{E}[X] = p", font_size=64, color=NEON_GREEN).next_to(fulcrum, UP, buff=1)

        with self.voiceover(text="Once you see the geometric balance behind the numbers, the equations just write themselves.") as tracker:
            self.play(Write(ev_formula), run_time=tracker.duration)

        # ---------------------------------------------------------
        # BEAT 68: Clarity & Safety
        # ---------------------------------------------------------
        grid = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": TEAL, "stroke_width": 1, "stroke_opacity": 0.2}
        )
        
        with self.voiceover(text="And the fear of the unknown is completely replaced by the clarity of understanding.") as tracker:
            self.play(FadeIn(grid), beam_group.animate.set_opacity(0.8), run_time=tracker.duration)

        # ---------------------------------------------------------
        # BEAT 69: Intuition > Memorization
        # ---------------------------------------------------------
        philosophy_text = Text("Intuition > Memorization", font_size=52, color=WHITE)

        with self.voiceover(text="If you want to keep building your statistical intuition without the academic jargon...") as tracker:
            self.play(FadeOut(beam_group), FadeOut(ev_formula), FadeOut(grid))
            self.play(Write(philosophy_text), run_time=tracker.duration - 1)

        # ---------------------------------------------------------
        # BEAT 70: Call to Action (Subscribe)
        # ---------------------------------------------------------
        sub_box = RoundedRectangle(corner_radius=0.2, height=1.2, width=4.5, color=RED_ALERT).set_fill(RED_ALERT, opacity=1)
        sub_text = Text("SUBSCRIBE", font_size=40, weight=BOLD).move_to(sub_box)
        sub_btn = VGroup(sub_box, sub_text)
        
       

        with self.voiceover(text="...then you are in exactly the right place. Hit that subscribe button.") as tracker:
            self.play(ReplacementTransform(philosophy_text, sub_btn), run_time=tracker.duration * 0.5)
            self.play(sub_box.animate.set_fill(GRAY, opacity=1).set_color(GRAY), run_time=tracker.duration * 0.2)

        # ---------------------------------------------------------
        # BEAT 71: Comment Engagement
        # ---------------------------------------------------------
        comment_bubble = RoundedRectangle(corner_radius=0.5, height=1.5, width=9, color=WHITE).set_fill(WHITE, opacity=0.1).shift(UP*2)
        comment_text = Text("Can we do the Poisson distribution next?", font_size=24, color=NEON_GREEN).move_to(comment_bubble)

        with self.voiceover(text="Leave a comment below on what math concept you want us to visualize next.") as tracker:
            self.play(FadeOut(sub_btn))
            self.play(Create(comment_bubble), Write(comment_text), run_time=tracker.duration - 1)

        # ---------------------------------------------------------
        # BEAT 72: Final Outro Coin
        # ---------------------------------------------------------
        final_coin = Circle(radius=1.5, color=NEON_GREEN).set_fill(NEON_GREEN, opacity=0.1)

        with self.voiceover(text="Keep exploring, and I will see you in the next one.") as tracker:
            self.play(FadeOut(comment_bubble), FadeOut(comment_text))
            self.play(Create(final_coin), run_time=tracker.duration * 0.5)
            self.play(FadeOut(final_coin, scale=0.1), run_time=tracker.duration * 0.5)
            
        self.wait(1)