import configparser
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np


class NegativeOneToPiIntro(VoiceoverScene, ThreeDScene):
    def construct(self):
      
        # 0. Global Setup & Color Palette
      
        self.camera.background_color = "#1A1C20"  # Dark Slate Background
        self.set_speech_service(GTTSService(lang="en"))

        COLOR_CYAN = "#38BDF8"     # Primary Math
        COLOR_GOLD = "#9BF7B0"     # Secondary Highlight
        COLOR_RED = "#EF4444"      # Cancellation / Warning
        COLOR_MAGENTA = "#FA4C72"  # Imaginary
        COLOR_WHITE = "#FFFFFF"    # Base Text

        question = MathTex("(-1)^{\\pi} = ?", font_size=72, color=COLOR_GOLD)
        
        with self.voiceover(
            text="What is negative one raised to the power of pi? Take a second. "
                 "I want to picture it in your mind."
        ):
            self.play(Write(question), run_time=3)
            
        with self.voiceover(
            text="If you are imagining a single number, you are about to be wrong, "
                 "not because you made an error, but because the question itself hides something extraordinary."
        ):
            self.play(question.animate.set_color(COLOR_CYAN), run_time=2)
            
        with self.voiceover(
            text="This is because the answer is not a single specific number. "
                 "Rather, there are countless such numbers. And the strange thing is that all occupy the exact same spot."
        ):
            inf_sign = MathTex("(-1)^{\\pi} \\longleftarrow \\infty \\text{ answers}", font_size=60, color=COLOR_MAGENTA)
            self.play(ReplacementTransform(question, inf_sign), run_time=3)
            self.wait(4)
            self.play(FadeOut(inf_sign))

      
        # Scene 2: The Function f(x) = (-1)^x
      
        func_def = MathTex("f(x) = (-1)^x", font_size=56, color=COLOR_WHITE).to_edge(UP, buff=1)
        
        with self.voiceover(
            text="Let us clarify the matter using a seemingly simple function, f of x equals negative one raised to the x. "
                 "At first glance, there is nothing alarming about it."
        ):
            self.play(Write(func_def), run_time=2)

        even_case = MathTex("f(2) = (-1)^2 = 1", font_size=48, color=COLOR_CYAN).next_to(func_def, DOWN, buff=0.8)
        odd_case = MathTex("f(3) = (-1)^3 = -1", font_size=48, color=COLOR_MAGENTA).next_to(even_case, DOWN, buff=0.4)

        with self.voiceover(
            text="Plug in any even whole number and you get one, plug in an odd whole number and you get negative one. "
                 "Simple enough."
        ):
            self.play(Write(even_case), run_time=2)
            self.play(Write(odd_case), run_time=2)

        half_case = MathTex("f(1/2) = (-1)^{1/2} = \\sqrt{-1} = i", font_size=48, color=COLOR_GOLD).next_to(odd_case, DOWN, buff=0.4)

        with self.voiceover(
            text="But try plugging in one half. Negative one to the one half power is the square root of negative one which is i."
        ):
            self.play(Write(half_case), run_time=3)

        with self.voiceover(
            text="So somewhere between whole numbers, this ordinary looking function has already slipped into imaginary territory."
        ):
            self.play(Indicate(half_case, color=COLOR_WHITE))
            self.play(FadeOut(even_case), FadeOut(odd_case), FadeOut(half_case), run_time=1.5)

      
        # Scene 3: Approximating 5^pi (The Real Way)
      
        real_q = MathTex("f(\\pi) = (-1)^{\\pi} = ?", font_size=56, color=COLOR_GOLD).next_to(func_def, DOWN, buff=0.8)
        
        with self.voiceover(
            text="Which raises the real question of this video. What happens when we plug in pi?"
        ):
            self.play(Write(real_q), run_time=2)

        five_pi = MathTex("5^{\\pi}", font_size=56, color=COLOR_CYAN).move_to(UP * 1.5)
        
        with self.voiceover(
            text="Here is how mathematicians usually handle a power with an irrational exponent. "
                 "Let's take a positive base. Let's say five raised to the pi."
        ):
            self.play(ReplacementTransform(real_q, five_pi), FadeOut(func_def), run_time=2)

        approx_1 = MathTex("5^{3} = 125", font_size=42).next_to(five_pi, DOWN, buff=0.5)
        approx_2 = MathTex("5^{3.1} = 5^{31/10} \\approx 146.8", font_size=42).next_to(approx_1, DOWN, buff=0.3)
        approx_3 = MathTex("5^{3.14} = 5^{314/100} \\approx 156.0", font_size=42).next_to(approx_2, DOWN, buff=0.3)
        approx_group = VGroup(approx_1, approx_2, approx_3)

        with self.voiceover(
            text="We approximate pi with closer and closer fractions: three, three point one, three point one four, "
                 "and raise five to each one."
        ):
            self.play(Write(approx_1), run_time=1)
            self.play(Write(approx_2), run_time=1.5)
            self.play(Write(approx_3), run_time=1.5)

        with self.voiceover(
            text="Every step is well defined because taking a root of a positive number gives exactly one positive number."
        ):
            self.play(Indicate(approx_group, color=COLOR_CYAN))

        limit_val = MathTex("\\lim_{x \\to \\pi} 5^x \\approx 156.99", font_size=48, color=COLOR_GOLD).next_to(approx_group, DOWN, buff=0.5)

        with self.voiceover(
            text="Those approximations settle down, converging toward a single value. "
                 "And that limit is what we call five to the pi."
        ):
            self.play(Write(limit_val), run_time=5)
            self.play(FadeOut(five_pi), FadeOut(approx_group), FadeOut(limit_val), run_time=1.5)

      
        # Scene 4: The Method Collapses for (-1)^pi
      
        neg_pi = MathTex("(-1)^{\\pi}", font_size=56, color=COLOR_MAGENTA).move_to(UP * 1.5)

        with self.voiceover(
            text="So why not do the same thing for negative one to the pi? Try it yourself."
        ):
            self.play(Write(neg_pi), run_time=2)

        neg_approx_1 = MathTex("(-1)^{3.1} = \\sqrt[10]{(-1)^{31}} \\Rightarrow 10 \\text{ roots}", font_size=42, color=COLOR_WHITE)
        comment = MathTex("Comment Below \\Downarrow" , font_size=42 , color=COLOR_WHITE).next_to(neg_pi, LEFT, buff=2.3)
        self.play(Write(comment), run_time=2)
        self.wait(2)
        self.play(FadeOut(comment), run_time=1.5)
      
        with self.voiceover(
            text="Unfortunately, the method collapses almost immediately. "
                 "Negative one to the three point one power means taking a tenth root of negative one, "
                 "and the tenth root of a negative number isn't one answer, it's ten."
        ):
            self.play(Write(neg_approx_1), run_time=4)

       

        neg_approx_2 = MathTex("(-1)^{3.14} = \\sqrt[100]{(-1)^{314}} \\Rightarrow 100 \\text{ candidate answers}", font_size=42, color=COLOR_CYAN).next_to(neg_approx_1, DOWN, buff=0.4)

        with self.voiceover(
            text="Push the approximation further to three point one four, and now you need a one hundredth root, "
                 "which answers a one hundred candidate answer. All different."
        ):
            self.play(Write(neg_approx_2), run_time=4)

        with self.voiceover(
            text="None of them converging toward anything. The more precisely we approximate pi, the more answers multiply. Not settle."
        ):
            self.play(Indicate(neg_approx_2, color=COLOR_MAGENTA), run_time=2)

        with self.voiceover(
            text="This is not a technical problem. It is a sign that raising a negative number to an irrational power "
                 "needs an entirely different definition, one built not on approximation, "
                 "but on the structure of the complex plane itself."
        ):
            self.play(FadeOut(neg_pi), FadeOut(neg_approx_1), FadeOut(neg_approx_2), run_time=2)

      
        # Scene 5: Euler's Formula
      
        euler_eq = MathTex("e^{i\\pi} = -1", font_size=60, color=COLOR_GOLD).move_to(UP * 1.5)

        with self.voiceover(
            text="To find that definition, we must return to an old friend. Euler's formula e to the i pi equals negative one."
        ):
            self.play(Write(euler_eq), run_time=3)

        with self.voiceover(
            text="You have probably seen this before. It is often called the most beautiful equation in mathematics."
        ):
            self.play(Circumscribe(euler_eq, color=COLOR_CYAN), run_time=2)

        euler_extended = MathTex("-1 = e^{i\\pi} = e^{3i\\pi} = e^{5i\\pi} = \\dots", font_size=48, color=COLOR_WHITE).next_to(euler_eq, DOWN, buff=0.8)

        with self.voiceover(
            text="But there is a subtlety hiding something in this equation. Negative one is not just e to the i pi. "
                 "It is also e to the I times three pi and e to the i times five pi."
        ):
            self.play(Write(euler_extended), run_time=4)

        with self.voiceover(
            text="In fact, add any multiple of two pi to that angle and you land on exactly the same point. "
                 "Because the complex plane does not just have one path to negative one. It has infinitely many."
        ):
            self.play(Indicate(euler_extended, color=COLOR_MAGENTA), run_time=3)

        with self.voiceover(
            text="Each one wrapping a different number of times around the origin before arriving. "
                 "This is where exponentiation gets strange."
        ):
            self.play(FadeOut(euler_eq), FadeOut(euler_extended), run_time=2)

      
        # Scene 6: Complex Logarithm & Definition of a^b 
      
        gen_title = MathTex("a^b = e^{b \\ln(a)}", font_size=56, color=COLOR_CYAN).move_to(UP * 1.5)

        with self.voiceover(
            text="To raise a number to an irrational power like pi, we can't just multiply it by itself pi times. "
                 "Pi is not something you can count. Instead, mathematicians define it using the exponential and the logarithm: "
                 "a to the b equals e to the b times the log of a."
        ):
            self.play(Write(gen_title), run_time=2)

        log_def = MathTex(
            "\\ln(-1) = i\\pi + 2k\\pi i = i\\pi(1 + 2k), \\quad k \\in \\mathbb{Z}",
            font_size=42,
            color=COLOR_MAGENTA
        ).next_to(gen_title, DOWN, buff=0.5)

        with self.voiceover(
            text="But here is the catch. Because negative one has infinitely many valid angles—pi, "
                 "three pi, five pi, and so on—its logarithm is not one number either. "
                 "The logarithm of negative one is i times pi plus any integer multiple of two pi i. "
                 "One input, infinitely many valid logarithms."
        ):
            self.play(Write(log_def), run_time=3)
            self.play(Indicate(log_def, color=COLOR_GOLD))

        with self.voiceover(
            text="It is in this sense that the complex logarithm, and by extension the complex exponential operation, "
                 "is multi-valued."
        ):
            self.play(log_def.animate.set_color(COLOR_CYAN), run_time=1.5)

      
        # Scene 7: Deriving (-1)^\pi & Purely Imaginary Exponent Magnitude
      
        eval_pi = MathTex(
            "(-1)^{\\pi} = e^{\\pi \\ln(-1)} = e^{i \\pi^2 (1 + 2k)}",
            font_size=48,
            color=COLOR_CYAN
        ).move_to(UP * 1.8)

        with self.voiceover(
            text="So let's actually compute negative one to the power of pi. "
                 "By substituting our logarithm in, negative one to the pi equals e to the i pi squared times "
                 "one plus two k, for any integer k."
        ):
            self.play(
                ReplacementTransform(gen_title, eval_pi),
                FadeOut(log_def),
                run_time=2.5
            )

        unit_mag = MathTex(
            "|(-1)^{\\pi}| = \\left| e^{i \\pi^2 (1 + 2k)} \\right| = 1",
            font_size=44,
            color=COLOR_GOLD
        ).next_to(eval_pi, DOWN, buff=0.5)

        with self.voiceover(
            text="Notice what is sitting in that exponent: it's purely imaginary. "
                 "And whenever e is raised to a purely imaginary number, the result always lands exactly on the unit circle, "
                 "which means every single one of these infinite answers, every possible value of negative one to the pi "
                 "has a magnitude of exactly one."
        ):
            self.play(Write(unit_mag), run_time=3)

        with self.voiceover(
            text="They are all different points, but they all live in the same circle."
        ):
            self.play(Indicate(unit_mag, color=COLOR_WHITE))

        self.play(FadeOut(eval_pi), FadeOut(unit_mag), run_time=1.5)

      
        # Scene 8: 3D Visualization of Dense Points on the Complex Circle
      
        complex_plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_color": COLOR_CYAN, "stroke_width": 1, "stroke_opacity": 0.3}
        ).scale(1.4)

        unit_circle = Circle(radius=1.4, color=COLOR_CYAN, stroke_width=2)

        with self.voiceover(
            text="Now here is where it gets genuinely beautiful. Each answer sits at an angle of pi squared times one plus two k."
        ):
            self.play(Create(complex_plane), Create(unit_circle), run_time=2)
            self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=3)

        # Plotting values of k to demonstrate density around the unit circle
        dense_dots = VGroup()
        k_range = list(range(-30, 30))
        for k in k_range:
            angle = (np.pi ** 2) * (1 + 2 * k)
            coords = complex_plane.number_to_point(np.exp(1j * angle))
            dot = Dot3D(point=coords, radius=0.05, color=COLOR_GOLD)
            dense_dots.add(dot)

        with self.voiceover(
            text="As k increases—one, two, three, one thousand—you might expect the points to eventually repeat, "
                 "to fall into the same pattern. They never do because pi is irrational. "
                 "None of these angles ever land in exactly the same spot twice."
        ):
            self.play(LaggedStartMap(FadeIn, dense_dots, lag_ratio=0.03), run_time=4)

        with self.voiceover(
            text="Instead, as k grows, the points scatter farther and farther around the circle. "
                 "And remarkably, they fill it completely. Every arc, no matter how small, eventually contains one of these points."
        ):
            self.begin_ambient_camera_rotation(rate=0.18)
            self.play(dense_dots.animate.set_color(COLOR_MAGENTA), run_time=3)

        with self.voiceover(
            text="Negative one to the pi does not just have infinitely many answers. "
                 "Those answers are dense across the entire circle—a direct fingerprint of pi's irrationality "
                 "hiding inside a single exponent."
        ):
            self.play(Circumscribe(unit_circle, color=COLOR_GOLD), run_time=2)

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=2)
        self.play(FadeOut(dense_dots), FadeOut(complex_plane), FadeOut(unit_circle), run_time=1.5)

      
        # Scene 9: Principal Value (k = 0) Convention & Conclusion
      
        principal_header = Text("Principal Value (k = 0)", font_size=36, color=COLOR_GOLD).to_edge(UP, buff=0.8)

        principal_eq = MathTex(
            "(-1)^{\\pi} \\approx e^{i \\pi^2} \\approx 0.903 - 0.430i",
            font_size=46,
            color=COLOR_CYAN
        ).next_to(principal_header, DOWN, buff=0.6)

        with self.voiceover(
            text="So if there are infinitely many valid answers, which one do we consider the standard? "
                 "Mathematicians handle this with a convention. We pick the one logarithm whose angle is closest to zero."
        ):
            self.play(Write(principal_header))

        with self.voiceover(
            text="Using k equals to zero, and negative one to the pi comes out to approximately zero point nine zero three "
                 "minus zero point four three i."
        ):
            self.play(Write(principal_eq), run_time=3)

        with self.voiceover(
            text="That's the default answer, not because it's more correct than the others, "
                 "because it's the one that keeps complex exponentiation consistent with the real number rules we already know."
        ):
            self.play(Indicate(principal_eq, color=COLOR_WHITE))

        with self.voiceover(
            text="This is the strange and wonderful trade off of complex numbers. "
                 "We gain the ability to raise anything to any power, but we lose the guarantee of a single answer."
        ):
            self.play(
                principal_eq.animate.scale(1.15).set_color(COLOR_GOLD),
                run_time=2.5
            )
            self.wait(1)

        self.play(FadeOut(principal_header), FadeOut(principal_eq), run_time=2)
