import configparser
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np


class NegativeOneToPiIntro(VoiceoverScene, ThreeDScene):
    def construct(self):
        self.camera.background_color = "#1A1C20"  # Dark Slate Background
        self.set_speech_service(GTTSService(lang="en"))

        FIRSTCOLOR = "#38BDF8"     # Primary Math
        SECONDCOLOR = "#9BF7B0"     # Secondary Highlight
        THIRDCOLOR = "#EF4444"      # Cancellation / Warning
        FOURTHCOLOR = "#FA4C72"  # Imaginary
        FIFTHCOLOR = "#FFFFFF"    # Base Text



        config.pixel_width = 1080
        config.pixel_height = 1920
        config.frame_width = 9.0
        config.frame_height = 16.0
        config.frame_rate = 60



        gen_title = MathTex("z^w = e^{w \\ln(z)}", font_size=56, color=FIRSTCOLOR).to_edge(UP, buff=0.8)

        with self.voiceover(
            text="To understand why these infinite answers exist, we must look at how complex exponentiation is built. "
                 "For any complex numbers z and w, z to the w is defined strictly through the exponential and logarithmic functions."
        ):
            self.play(Write(gen_title), run_time=2)

        gen_log = MathTex(
            "\\ln(z) = \\ln|z| + i(\\text{Arg}(z) + 2k\\pi)",
            font_size=42,
            color=SECONDCOLOR
        ).next_to(gen_title, DOWN, buff=0.5)

        with self.voiceover(
            text="The multi-valued nature originates entirely in the complex logarithm. "
                 "Because moving in a full turn around the origin adds two pi to the argument, "
                 "the logarithm yields infinitely many outputs, one for every integer k."
        ):
            self.play(Write(gen_log), run_time=2.5)

        self.play(Indicate(gen_log, color=FOURTHCOLOR))
        self.play(FadeOut(gen_title), FadeOut(gen_log), run_time=1.5)

        # ----------------------------------------------------------------
        # The Riemann Surface Geometry (3D Spiral / Helix)
        # ----------------------------------------------------------------
        riemann_text = Text(
            "The Riemann Surface of ln(z)",
            font_size=32,
            color=FIRSTCOLOR
        ).to_edge(UP, buff=0.5)

        with self.voiceover(
            text="Instead of thinking of the logarithm as a standard single-valued function, "
                 "mathematicians visualize its domain as a multi-layered surface: a Riemann surface."
        ):
            self.play(Write(riemann_text))

        # Setup 3D camera orientation
        self.move_camera(phi=70 * DEGREES, theta=-50 * DEGREES, run_time=2)

        # Parametric Surface: Helicoid representing logarithmic sheets
        helicoid = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                0.3 * v
            ]),
            u_range=[0.3, 2.0],
            v_range=[-3 * np.pi, 3 * np.pi],
            resolution=(16, 64),
            fill_opacity=0.6,
            checkerboard_colors=[FIRSTCOLOR, FOURTHCOLOR],
            stroke_color=FIFTHCOLOR,
            stroke_width=0.5
        )

        axis_z = Line3D(start=[0, 0, -3], end=[0, 0, 3], color=SECONDCOLOR)

        with self.voiceover(
            text="Imagine a spiral staircase winding infinitely upward and downward around the origin. "
                 "Each full rotation lands you on a different sheet, corresponding to a different integer choice of k."
        ):
            self.play(Create(axis_z), Create(helicoid), run_time=4)
            self.begin_ambient_camera_rotation(rate=0.2)
            self.wait(2)

        with self.voiceover(
            text="When we evaluate negative one to the pi, we are sampling points from across all of these sheets simultaneously."
        ):
            self.play(helicoid.animate.set_color(SECONDCOLOR), run_time=2)

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=2)
        self.play(FadeOut(helicoid), FadeOut(axis_z), FadeOut(riemann_text), run_time=1.5)

        traj_title = MathTex("f(x) = (-1)^x \\quad \\text{for } x \\in [0, \\pi]", font_size=40, color=FIFTHCOLOR).to_edge(UP, buff=0.6)

        with self.voiceover(
            text="What happens if we let the exponent vary continuously from zero up to pi? "
                 "Each branch k traces out its own continuous trajectory along the complex plane."
        ):
            self.play(Write(traj_title))

        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={"stroke_color":FIRSTCOLOR, "stroke_width": 1, "stroke_opacity": 0.3}
        )

        circle = Circle(radius=1.0, color=FIRSTCOLOR, stroke_width=1.5)
        self.play(Create(plane), Create(circle))
        curves = VGroup()
        for k in [-1, 0, 1]:
            curve = ParametricFunction(
                lambda t: plane.number_to_point(np.exp(1j * np.pi * t * (1 + 2 * k))),
                t_range=[0, 1, 0.01],
                color=SECONDCOLOR if k == 0 else FOURTHCOLOR,
                stroke_width=3
            )
            curves.add(curve)

        with self.voiceover(
            text="As x increases, the primary branch k equals zero smoothly rotates around the circle, "
                 "while the higher branches wind faster and faster around the unit circle."
        ):
            self.play(Create(curves), run_time=4)

        with self.voiceover(
            text="By the time x reaches pi, these paths land at their distinct, dense positions along the boundary."
        ):
            self.play(Circumscribe(curves, color=SECONDCOLOR), run_time=2)

        self.play(FadeOut(curves), FadeOut(plane), FadeOut(circle), FadeOut(traj_title), run_time=1.5)

        final_summary = MathTex(
            r"(-1)^{\pi} = \left\{ e^{i \pi^2 (1 + 2k)} \mid k \in \mathbb{Z} \right\}",
            font_size=44,
            color=FIRSTCOLOR
        ).move_to(UP * 1.0)


        with self.voiceover(
            text="Negative one to the pi is not a single number, but an infinite spectrum of points, "
                 "densely wrapping around the complex unit circle. "
                 "It unveils the deep geometric connection between irrational numbers, complex logarithms, and Euler's formula."
        ):
            self.play(Write(final_summary), run_time=2.5)
           
            self.play(Indicate(final_summary, color=FIFTHCOLOR), run_time=2)

        self.wait(2)
        self.play(FadeOut(final_summary))
