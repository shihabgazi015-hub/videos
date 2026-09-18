from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import random

# Global Frame & Canvas Setup for Vertical Video (9:16)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class SquareRootTrick(VoiceoverScene):
    def construct(self):
        # ----------------------------------------------------------------
        # 0. Global Setup, Colors & Ambient Canvas
        # ----------------------------------------------------------------
        COLOR_BG = "#1A1C20"
        COLOR_CYAN = "#38BDF8"
        COLOR_GOLD = "#9BF7B0"
        COLOR_RED = "#EF4444"
        COLOR_PINK = "#FA4C72"
        COLOR_WHITE = "#FFFFFF"

        self.camera.background_color = COLOR_BG
        self.set_speech_service(GTTSService(lang="en"))

        # Ambient Drifting Particles System
        particles = VGroup(*[
            Dot(
                radius=random.uniform(0.02, 0.05),
                color=COLOR_WHITE,
                fill_opacity=random.uniform(0.1, 0.3)
            ).move_to([
                random.uniform(-4.5, 4.5),
                random.uniform(-8.0, 8.0),
                0
            ]) for _ in range(75)
        ])
        
        def update_particles(mob, dt):
            for p in mob:
                p.shift(UP * 0.15 * dt)
                if p.get_y() > 8.0:
                    p.set_y(-8.0)
                    p.set_x(random.uniform(-4.5, 4.5))
                    
        particles.add_updater(update_particles)
        self.add(particles)

        # ----------------------------------------------------------------
        # Segment 1: The High-Tension Hook [00:00:00 - 00:00:05]
        # ----------------------------------------------------------------
        target_eq = MathTex("\\sqrt{127}", font_size=140, color=COLOR_CYAN).move_to(UP * 2.5)
        
        # Procedural Calculator
        calc_body = RoundedRectangle(corner_radius=0.3, width=3.0, height=4.5, color=COLOR_WHITE, fill_color=COLOR_BG, fill_opacity=1)
        calc_screen = Rectangle(width=2.5, height=1.0, color=COLOR_WHITE).move_to(calc_body.get_top() + DOWN * 0.8)
        
        buttons = VGroup()
        for i in range(4):
            for j in range(4):
                btn = RoundedRectangle(corner_radius=0.1, width=0.5, height=0.5, color=COLOR_WHITE)
                if j == 3: 
                    btn.set_color(COLOR_GOLD)
                btn.move_to(calc_body.get_corner(UL) + RIGHT * (0.6 + j * 0.6) + DOWN * (1.8 + i * 0.7))
                buttons.add(btn)
                
        calculator = VGroup(calc_body, calc_screen, buttons).move_to(DOWN * 2)
        red_cross = Cross(calculator, stroke_color=COLOR_RED, stroke_width=18)

        with self.voiceover(
            text="Calculate the square root of one hundred twenty seven in five seconds. No calculator allowed."
        ):
            self.play(FadeIn(target_eq, shift=UP), run_time=1)
            self.play(Create(calc_body), Create(calc_screen), run_time=0.5)
            self.play(LaggedStartMap(FadeIn, buttons, lag_ratio=0.05), run_time=1)
            self.play(Create(red_cross), run_time=0.2)

        # ----------------------------------------------------------------
        # Segment 2: Suspense Buffer [00:00:05 - 00:00:06.7 + Silence]
        # ----------------------------------------------------------------
        self.play(
            calculator.animate.set_opacity(0.15),
            red_cross.animate.set_opacity(0.15),
            target_eq.animate.set_color(COLOR_GOLD),
            run_time=0.5
        )
        
        # Rhythmic pulsing during 5s manual suspense silence
        for _ in range(4):
            self.play(Indicate(target_eq, color=COLOR_CYAN, scale_factor=1.1), run_time=1.25)

        # ----------------------------------------------------------------
        # Segment 3: The Bracket Transition [00:00:06.7 - 00:00:11.2]
        # ----------------------------------------------------------------
        stuck_text = Text("Stuck?", font_size=60, color=COLOR_RED).move_to(ORIGIN)
        # bracket_text = Text("The Bracket Method", font_size=50, color=COLOR_GOLD).move_to(ORIGIN)
        
        num_line = NumberLine(
            x_range=[115, 150, 5],
            length=8,
            color=COLOR_WHITE,
            include_numbers=False
        ).move_to(DOWN * 1)

        with self.voiceover(
            text="Stuck. Here is the trick. Find the perfect squares around it."
        ):
            self.play(
                FadeOut(calculator), FadeOut(red_cross),
                target_eq.animate.scale(0.6).move_to(UP * 6).set_color(COLOR_CYAN),
                run_time=1
            )
            self.play(FadeIn(stuck_text, shift=UP))
            self.play(ReplacementTransform(stuck_text, num_line), run_time=1.5)

        # ----------------------------------------------------------------
        # Segment 4: Anchor Points & Bracketing [00:00:11.2 - 00:00:18.1]
        # ----------------------------------------------------------------
        dot_121 = Dot(num_line.n2p(121), radius=0.15, color=COLOR_GOLD)
        dot_144 = Dot(num_line.n2p(144), radius=0.15, color=COLOR_GOLD)
        dot_127 = Dot(num_line.n2p(127), radius=0.12, color=COLOR_WHITE)
        
        lbl_121 = MathTex("11^2 = 121", color=COLOR_CYAN, font_size=36).next_to(dot_121, DOWN)
        lbl_144 = MathTex("12^2 = 144", color=COLOR_CYAN, font_size=36).next_to(dot_144, DOWN)
        lbl_127 = MathTex("127", color=COLOR_WHITE, font_size=36).next_to(dot_127, UP*1.1)

        with self.voiceover(
            text="Eleven squared is one hundred twenty one. Twelve squared is one Forty four. You probably already knew those."
        ):
            self.play(FadeIn(dot_121, shift=DOWN), FadeIn(dot_144, shift=DOWN), run_time=1)
            self.play(Write(lbl_121), Write(lbl_144), run_time=1.5)
            self.play(FadeIn(dot_127), Write(lbl_127))

        # ----------------------------------------------------------------
        # Segment 5: Input Gap vs. Output Jump Rate [00:00:18.1 - 00:00:27.9]
        # ----------------------------------------------------------------
        brace_main = BraceBetweenPoints(dot_121.get_center(), dot_144.get_center(), direction=UP, color=COLOR_GOLD)
        delta_x = MathTex("\\Delta x = 23", color=COLOR_GOLD, font_size=36).next_to(brace_main, UP, buff=0.3)
        delta_y = MathTex("\\Delta y = 1", color=COLOR_CYAN, font_size=36).next_to(delta_x, UP, buff=0.3)
        rate_eq = MathTex("\\text{Rate} = \\frac{1}{23}", color=COLOR_WHITE, font_size=36).next_to(delta_y, UP, buff=0.7)

        with self.voiceover(
            text="The gap between them is twenty three. But here's the catch. As you cross that gap, the root only jumps by one from eleven to twelve."
        ):
            self.play(GrowFromCenter(brace_main), Write(delta_x), run_time=2)
            self.play(Write(delta_y), run_time=2)

        with self.voiceover(
            text="So every step in the gap adds roughly one over twenty three to the root."
        ):
            self.play(Write(rate_eq), run_time=2)

        # ----------------------------------------------------------------
        # Segment 6: Step Counter Projection [00:00:27.9 - 00:00:36.4]
        # ----------------------------------------------------------------
        brace_sub = BraceBetweenPoints(dot_121.get_center(), dot_127.get_center(), direction=UP, color=COLOR_CYAN)
        steps_lbl = Text("6 steps", color=COLOR_CYAN, font_size=24).next_to(brace_sub, UP, buff=0.1)
        step_math = MathTex("\\frac{6}{23}", color=COLOR_CYAN, font_size=36).next_to(rate_eq, DOWN, buff=0.2)

        with self.voiceover(
            text="One hundred twenty seven is six steps past one twenty one. So it's eleven plus six over twenty three."
        ):
            self.play(
                FadeOut(brace_main), FadeOut(delta_x), FadeOut(delta_y),
                GrowFromCenter(brace_sub), FadeIn(steps_lbl, shift=UP),
                run_time=2
            )
            self.play(Write(step_math), run_time=2.5)

        # ----------------------------------------------------------------
        # Segment 7: Final Mental Estimate Morph [00:00:36.4 - 00:00:41.7]
        # ----------------------------------------------------------------
        final_eq = MathTex("\\sqrt{127}", "\\approx", "11", "+", "\\frac{6}{23}", "\\approx", "11.26", font_size=56)
        final_eq.set_color_by_tex_to_color_map({"11.26": COLOR_GOLD})
        final_eq.move_to(UP * 2.5)
        
        highlight_box = SurroundingRectangle(final_eq.get_part_by_tex("11.26"), color=COLOR_GOLD, corner_radius=0.1)

        with self.voiceover(
            text="That's roughly eleven point two six."
        ):
            self.play(
                FadeOut(brace_sub), FadeOut(steps_lbl), FadeOut(step_math), FadeOut(rate_eq), FadeOut(lbl_127),
                TransformMatchingShapes(target_eq, final_eq),
                run_time=2
            )
            self.play(Create(highlight_box), run_time=1)

        # ----------------------------------------------------------------
        # Segment 8: Geometric Proof [00:00:41.7 - 00:00:51.0]
        # ----------------------------------------------------------------
        axes = Axes(
            x_range=[115, 145, 5],
            y_range=[10, 12.5, 0.5],
            x_length=7.5,
            y_length=4,
            axis_config={"color": COLOR_WHITE, "include_numbers": False}
        ).move_to(DOWN * 1.5)
        
        curve = axes.plot(lambda x: np.sqrt(x), color=COLOR_CYAN, x_range=[115, 145])
        secant = axes.plot(lambda x: 11 + (x - 121)*(1/23), color=COLOR_GOLD, x_range=[121, 144])
        
        error_badge = Text("Error < 0.009", color=COLOR_GOLD, font_size=32).next_to(axes, UP, buff=0.5)

        with self.voiceover(
            text="And the real value is eleven point two six nine four. We got within zero point zero nine. That's the power of linear approximation."
        ):
            self.play(
                FadeOut(num_line), FadeOut(dot_121), FadeOut(dot_144), FadeOut(dot_127), FadeOut(lbl_121), FadeOut(lbl_144),
                Create(axes),
                run_time=1.5
            )
            self.play(Create(curve), run_time=1.5)
            self.play(Create(secant), run_time=1.5)
            self.play(FadeIn(error_badge, shift=DOWN))

        # ----------------------------------------------------------------
        # Segment 9: Interactive Call-To-Action Screen [00:00:51.0 - 00:00:55.9]
        # ----------------------------------------------------------------
        wipe = Rectangle(width=15, height=20, fill_color=COLOR_BG, fill_opacity=1).move_to(RIGHT * 12)
        prompt = MathTex("\\sqrt{50} = ?", font_size=140, color=COLOR_CYAN).move_to(UP * 1.5)
        
        comment_box = RoundedRectangle(corner_radius=0.2, width=6, height=1.5, color=COLOR_WHITE).next_to(prompt, DOWN, buff=1.5)
        cursor = Line(UP, DOWN, color=COLOR_WHITE).scale(0.4).move_to(comment_box.get_left() + RIGHT * 0.5)

        with self.voiceover(
            text="Test this right now on the square root of fifty. Drop your estimate in the comments below."
        ):
            # Directional Wipe
            self.play(wipe.animate.move_to(ORIGIN), run_time=1)
            # Bring elements in front of wipe dynamically
            self.add(prompt, comment_box, cursor)
            self.play(Write(prompt), Create(comment_box), run_time=1)
            
            # Simulate blinking active text cursor
            for _ in range(8):
                self.play(cursor.animate.set_opacity(0), run_time=0.2)
                self.play(cursor.animate.set_opacity(1), run_time=0.2)

        self.wait(1)
