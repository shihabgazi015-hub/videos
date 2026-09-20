from manim import *
import numpy as np

class NegativeOneToPiIntro0(ThreeDScene):
    def construct(self):
        # 0. Global Canvas Setup & Sync Helper
        COLOR_BG = "#1A1C20"
        COLOR_CYAN = "#38BDF8"
        COLOR_GOLD = "#9BF7B0"
        COLOR_RED = "#EF4444"
        COLOR_PINK = "#FA4C72"
        COLOR_WHITE = "#FFFFFF"

        self.camera.background_color = COLOR_BG

        def sync_to(target_time):
            """Pads the scene with wait time to match exact SRT timestamps."""
            current_time = self.renderer.time
            if target_time > current_time:
                self.wait(target_time - current_time)

        # Segment 1: The Imaginary Unit & 3D Transition [00:00:00 - 00:17:12]
        axes = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-2, 5, 1],
            x_length=6, y_length=6, z_length=5
        )
        axes_labels = axes.get_axis_labels(x_label="Real", y_label="Imaginary")
        
        # 1D line representation initially
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        
        unit_vector = Arrow(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), buff=0, color=COLOR_WHITE)
        real_label = MathTex("1", color=COLOR_WHITE).next_to(unit_vector.get_end(), DOWN)
        
        self.play(Create(axes), Create(unit_vector), Write(real_label), run_time=3)
        sync_to(5.48) # "If I asked you to picture... step off the familiar real number line"

        # 90 degree turn into the complex plane
        arc = Arc(radius=1, start_angle=0, angle=PI/2, color=COLOR_PINK)
        imag_vector = Arrow(axes.c2p(0, 0, 0), axes.c2p(0, 1, 0), buff=0, color=COLOR_PINK)
        imag_label = MathTex("i", color=COLOR_PINK).next_to(imag_vector.get_end(), LEFT)
        
        self.play(
            Rotate(unit_vector, angle=PI/2, about_point=axes.c2p(0, 0, 0)),
            Create(arc),
            Transform(real_label, imag_label),
            run_time=2.5
        )
        self.play(Transform(unit_vector, imag_vector))
        
        # Tilt into 3D Space
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=3)
        sync_to(13.75) # "...completely different dimension."

        def_eq = MathTex("i", "=", "\\sqrt{-1}", font_size=60).to_corner(UL, buff = 1)
        def_eq[0].set_color(COLOR_PINK)
        self.add_fixed_in_frame_mobjects(def_eq)
        self.play(Write(def_eq), run_time=2)
        sync_to(17.12) # "By definition, it's the square root of negative one."

        # Segment 2: Raised to its own power [00:17:12 - 00:36:11]
        power_eq = MathTex("i^{i}", font_size=120).next_to(def_eq, DOWN, buff=0.5)
        power_eq.set_color(COLOR_PINK)
        self.add_fixed_in_frame_mobjects(power_eq)
        self.play(Write(power_eq))
        sync_to(23.32) # "raise it to its own power?"

        # Plunge into complex space and land on real axis
        plunge_path = ParametricFunction(
            lambda t: axes.c2p(0.208 * np.cos(t), 0.208 * np.sin(t), 7 * np.exp(-t)),
            t_range=[0, 9*PI],
            color=COLOR_CYAN
        )
        #plunge path label
        plunge_path_label = MathTex("cos\\theta + isin\\theta", font_size=32).next_to(plunge_path.point_from_proportion(0.5), RIGHT).move_to(UR*1.5)
        self.add_fixed_in_frame_mobjects(plunge_path_label)
        self.play(Write(plunge_path_label), run_time=0.5)
        self.play(Create(plunge_path), run_time=4)
        sync_to(29.76) # "...plunge even deeper into the complex plane..."
        self.play(FadeOut(plunge_path_label), run_time=0.5)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1)
        landing_dot = Dot(axes.c2p(0.208, 0, 0), color=COLOR_GOLD, radius=0.15)
        self.play(Create(landing_dot), run_time=0.5)
        sync_to(32.15) # "...lands right back on the real number line."

        result_eq = MathTex("i^{i}", "\\approx", "0.208", font_size=80).move_to(power_eq)
        result_eq[0].set_color(COLOR_PINK)
        result_eq[2].set_color(COLOR_GOLD)
        self.play(ReplacementTransform(power_eq, result_eq))
        sync_to(36.11) # "It's approximately 0.208."

        # Segment 3: The Flawed Proof [00:36:11 - 01:24:76]
        self.play(
            FadeOut(axes), FadeOut(unit_vector), FadeOut(arc), FadeOut(real_label), 
            FadeOut(plunge_path), FadeOut(landing_dot), FadeOut(def_eq), FadeOut(result_eq),
            run_time=2
        )
        # Reset camera for 2D math layout
        sync_to(48.96) # "elegant and completely flawed proof..."

        flawed_1 = MathTex("e^{", "i", "\\frac{\\pi}{2}", "}", "=", "i", font_size=120)
        flawed_1.set_color_by_tex("i", COLOR_PINK)
        
        self.play(Write(flawed_1))
        sync_to(59.03) # "Euler's formula tells us..."

        flawed_2 = MathTex("(", "e^{", "i", "\\frac{\\pi}{2}", "}", ")^{", "i", "}", font_size=120)
        flawed_2.set_color_by_tex("i", COLOR_PINK)
        
        self.play(TransformMatchingShapes(flawed_1, flawed_2))
        sync_to(66.70) # "So we substitute that into our expression..."

        flawed_3 = MathTex("e^{", "i", "\\cdot", "i", "\\frac{\\pi}{2}", "}", font_size=120)
        flawed_3.set_color_by_tex("i", COLOR_PINK)
        
        self.play(TransformMatchingShapes(flawed_2, flawed_3))
        sync_to(70.98) # "multiply the exponents..."

        flawed_4 = MathTex("e^{", "-", "\\frac{\\pi}{2}", "}", font_size=120)
        flawed_4.set_color_by_tex("-", COLOR_RED)
        
        self.play(TransformMatchingShapes(flawed_3, flawed_4))
        sync_to(76.65) # "result simplifies neatly to e to the negative pi over two."

        flawed_5 = MathTex("e^{", "-", "\\frac{\\pi}{2}", "}", "\\approx", "0.208", font_size=120)
        flawed_5.set_color_by_tex("0.208", COLOR_GOLD)
        
        self.play(TransformMatchingShapes(flawed_4, flawed_5))
        sync_to(84.76) # "Plug that into a calculator and you get 0.208. It's very clear right?"

        # Segment 4: The Hidden Trap & Paradox [01:24:76 - 02:15:75]
        self.play(flawed_5.animate.scale(0.5).to_corner(UR).set_opacity(0.3))
        
        rule = MathTex("(a^b)^c = a^{bc}", font_size=120, color=COLOR_WHITE)
        self.play(Write(rule))
        sync_to(105.12) # "works beautifully for real numbers. But the moment we leave..."

        trap_cross = Cross(rule, stroke_color=COLOR_RED, stroke_width=12)
        self.play(Create(trap_cross))
        sync_to(108.71) # "that rule completely shatters. To see why, consider number one."

        self.play(FadeOut(rule), FadeOut(trap_cross))
        
        paradox_1 = MathTex("1", "=", "e^{", "2\\pi", "i", "}", font_size=120)
        paradox_1.set_color_by_tex("i", COLOR_PINK)
        self.play(Write(paradox_1))
        sync_to(114.37) # "We can write one as e to the 2 pi i."

        paradox_2 = MathTex("1^{1/2}", "=", "(", "e^{", "2\\pi", "i", "}", ")^{1/2}", font_size=120)
        paradox_2.set_color_by_tex("i", COLOR_PINK)
        self.play(TransformMatchingShapes(paradox_1, paradox_2))
        sync_to(118.28) # "Now let's raise both sides to the power of one half."

        paradox_3 = MathTex("1", "=", "e^{", "\\pi", "i", "}", font_size=120)
        paradox_3.set_color_by_tex("i", COLOR_PINK)
        self.play(TransformMatchingShapes(paradox_2, paradox_3))
        sync_to(128.43) # "blindly multiply... e to the pi i"

        paradox_4 = MathTex("1", "=", "-1", font_size=120)
        paradox_4[2].set_color(COLOR_RED)
        self.play(TransformMatchingShapes(paradox_3, paradox_4))
        sync_to(133.71) # "We just proved that 1 equals negative 1."

        self.play(Wiggle(paradox_4, scale_value=1.5, rotation_angle=0.05 * PI))
        sync_to(135.75) # "We broke math."

        # Segment 5: The Complex Logarithm [02:15:75 - 03:34:47]
        self.play(FadeOut(paradox_4), FadeOut(flawed_5))
        
        rigorous_def = MathTex("a^b", "=", "e^{", "b", "\\ln a", "}", font_size=120)
        rigorous_def.set_color_by_tex("a", COLOR_CYAN)
        rigorous_def.set_color_by_tex("b", COLOR_GOLD)
        
        self.play(Write(rigorous_def))
        sync_to(161.13) # "The rigorous bullet proof way to define A to the power of B..."

        log_sub = MathTex("i^i", "=", "e^{", "i", "\\ln i", "}", font_size=120)
        log_sub.set_color_by_tex("i", COLOR_PINK)

        self.play(TransformMatchingShapes(rigorous_def, log_sub))
        sync_to(167.43) # "So to calculate i to the i, we need to evaluate e to the i ln i."

        self.play(log_sub.animate.to_corner(UL).scale(0.7))
        
        # Return to 3D for multivalued logarithm visualization
        self.add_fixed_in_frame_mobjects(log_sub)
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=2)
        
        self.play(FadeIn(axes), FadeIn(unit_vector))
        sync_to(185.06) # "Getting to i means starting at one and rotating 90 degrees..."

        arc_pi_2 = Arc(radius=1, start_angle=0, angle=PI/2, color=COLOR_PINK)
        self.play(Create(arc_pi_2))
        sync_to(191.56) # "So one answer is i times pi over 2."

        log_ans_1 = MathTex("\\ln(i)", "=", "i", "\\frac{\\pi}{2}").to_corner(UR)
        log_ans_1.set_color_by_tex("i", COLOR_PINK)
        self.add_fixed_in_frame_mobjects(log_ans_1)
        self.play(Write(log_ans_1))
        sync_to(195.08) # "But remember this is a geometric rotation."

        # Multivalued Helix Animation
        helix = ParametricFunction(
            lambda t: axes.c2p(np.cos(t), np.sin(t), t / (2*PI)),
            t_range=[PI/2, PI/2 + 4*PI],
            color=COLOR_CYAN
        )
        self.play(Create(helix), run_time=4)
        sync_to(205.52) # "spin around... pi over 2 plus a full turn... plus another..."
        
        log_ans_multi = MathTex("\\ln(i)", "=", "i", "\\left(", "\\frac{\\pi}{2}", "+", "2\\pi k", "\\right)").to_corner(UR)
        self.add_fixed_in_frame_mobjects(log_ans_multi)
        log_ans_multi.set_color_by_tex("i", COLOR_PINK)
        self.add_fixed_in_frame_mobjects(log_ans_multi)
        
        self.play(ReplacementTransform(log_ans_1, log_ans_multi))
        sync_to(227.15) # "where k is any integer."

        # Segment 6: The Resolution & Principal Branch [03:34:47 - 04:57:12]
        self.play(FadeOut(axes), FadeOut(unit_vector), FadeOut(arc_pi_2), FadeOut(helix))
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1)
        
        final_sub_1 = MathTex("i^i", "=", "e^{", "i", "\\cdot", "i", "\\left(", "\\frac{\\pi}{2}", "+", "2\\pi k", "\\right)", "}", font_size=120)
        final_sub_1.set_color_by_tex("i", COLOR_PINK)
        
        self.play(TransformMatchingShapes(log_sub, final_sub_1), FadeOut(log_ans_multi))
        sync_to(240.96) # "Now let us substitute this complete truth... here is where the magic happens."

        final_sub_2 = MathTex("i^i", "=", "e^{", "-", "\\left(", "\\frac{\\pi}{2}", "+", "2\\pi k", "\\right)", "}", font_size=120)
        final_sub_2.set_color_by_tex("-", COLOR_RED)
        
        self.play(TransformMatchingShapes(final_sub_1, final_sub_2))
        sync_to(248.31) # "Those two i's multiply to negative one... perfectly annihilate each other."

        missing_i_highlight = SurroundingRectangle(final_sub_2[3:], color=COLOR_GOLD)
        self.play(Create(missing_i_highlight))
        sync_to(259.75) # "Notice what is missing... no i left. It is an entirely real number"

        self.play(FadeOut(missing_i_highlight))
        
        branch_text = Text("Principal Branch (k = 0)", font_size=36, color=COLOR_CYAN).next_to(final_sub_2, DOWN, buff=1)
        self.add_fixed_in_frame_mobjects(branch_text)
        self.play(Write(branch_text))
        sync_to(278.45) # "If we take what mathematicians call the principal branch, where k is exactly zero..."

        final_ans = MathTex("i^i", "=", "e^{", "-", "\\frac{\\pi}{2}", "}", "\\approx", "0.208", font_size=120).move_to(UP*1.5)
        final_ans.set_color_by_tex("0.208", COLOR_GOLD)
        
        self.play(
            ReplacementTransform(final_sub_2, final_ans),
            FadeOut(branch_text)
        )
        sync_to(287.72) # "we get e to the negative pi over two. That is where our 0.208 comes from."

        final_box = SurroundingRectangle(final_ans, color=COLOR_CYAN, corner_radius=0.2, buff = 1.1)
        self.play(Create(final_box))
        
        sync_to(297.12) # "...stumbled into the right answer using an entirely wrong method."
        self.wait(2)
