from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
class WhatIsJacobian(VoiceoverScene, ThreeDScene):
    def construct(self):
        # Apply Core Aesthetics & Rules
        self.camera.background_color = "#0b1624"
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Colors mapped from production notes
        CYAN = "#00E5FF"
        MAGENTA = "#FF007F"
        RED_ACCENT = "#EF4444"
        GOLD = "#FACC15"

        plane = NumberPlane(
                background_line_style={"stroke_color": CYAN, "stroke_width": 2},
                faded_line_style={"stroke_color": CYAN, "stroke_width": 1}
            )
        
        
        text_1 = "How to calculate the exact rate of change for a function of multiple functions, where every single function depends on multiple variables?"
        with self.voiceover(text=text_1) as tracker:
            # 0:00 - 0:08 
            f0 = MathTex(
            r"\vec{f}",
            color=WHITE
            ).scale(10)  

            f00 = MathTex(
            r"\vec{f}(x_1, x_2, \dots, x_n)",   
            color = WHITE
            ).scale(3)
        
            f000 = MathTex(
                r"\begin{gathered}"
                r"\vec{f}(x_1, x_2, \dots, x_n) \\"
                r"\downarrow \\"
                r"\begin{bmatrix} f_1(x_1, x_2, \dots, x_n) \\ f_2(x_1, x_2, \dots, x_n) \end{bmatrix}"
                r"\end{gathered}",
                substrings_to_isolate=["x_1", "x_2", "x_n"],
                color=WHITE
            ).scale(2)

     
            self.play(Write(f0), run_time=2)
            self.wait(1)
            self.play(ReplacementTransform(f0, f00), run_time=1)
            self.wait(1)
            self.play(ReplacementTransform(f00, f000), run_time=1) 
            self.wait(1)

            self.play(f000.animate.set_color_by_tex("x_1", YELLOW), run_time=0.3)
            self.wait(0.5)
            self.play(f000.animate.set_color_by_tex("x_2", BLUE), run_time=0.3)
            self.wait(0.5)
            self.play(f000.animate.set_color_by_tex("x_n", GREEN), run_time=0.3)
            self.wait(4)
            self.play(FadeOut(f000), run_time = 1)
        
        # 0:05 - 0:09 
        
        text_2 = "Jumping straight into the solution for this problem can be overwhelming. So let’s build this step-by-step from something we already know."
        with self.voiceover(text=text_2) as tracker:
            simple_eq = MathTex(r"f(x) = x^2", color=WHITE).scale(1.5).to_edge(UP)
            
            self.play(
                Create(simple_eq),
                run_time=tracker.duration * 0.5
            )
            
           
            curve_1d = plane.plot(lambda x: x**2, x_range=[-2, 2], color=GOLD)
            self.play(Create(curve_1d), run_time=tracker.duration * 0.5)
        
        # 0:09 - 0:16 | 1D VS MULTIVARIABLE
        
        text_3 = "In single-variable calculus, one derivative gives us the slope. Add a second variable, and we need partial derivatives—which measure the directional slope along a single grid axis while holding all other variables constant."
        with self.voiceover(text=text_3) as tracker:
            self.play(
                VGroup(plane, curve_1d).animate.scale(0.5).to_edge(LEFT),
                simple_eq.animate.to_edge(LEFT).shift(UP * 2),
                run_time=tracker.duration * 0.15
            )
            
            x_val = ValueTracker(0.2)
            dot = always_redraw(lambda: Dot(plane.c2p(x_val.get_value(), x_val.get_value()**2), color=RED_ACCENT))
         
            tangent = always_redraw(lambda: TangentLine(curve_1d, alpha=x_val.get_value()/4 + 0.5, length=3, color=GOLD))
            deriv_label = MathTex(r"\frac{df}{dx} = 2x").next_to(simple_eq, DOWN)
            
            self.play(Create(dot), Create(tangent), Write(deriv_label), run_time=tracker.duration * 0.15)
            self.play(x_val.animate.set_value(1.5), run_time=tracker.duration * 0.2)
           
            axes3d = ThreeDAxes(x_range=[-2, 2], y_range=[-2, 2], z_range=[0, 8]).scale(0.5).to_edge(RIGHT)
            surface = Surface(
                lambda u, v: axes3d.c2p(u, v, u**2 + u*v + v**2),
                u_range=[-2, 2], v_range=[-2, 2],
                resolution=(15, 15)
            ).set_style(fill_opacity=0.6, stroke_color=WHITE, stroke_width=0.5)
            p_center = axes3d.c2p(0.5, 0.5, 0.75)
            p_dx = axes3d.c2p(1.0, 0.5, 1.5)
            p_dy = axes3d.c2p(0.5, 1.0, 1.5)
            
    
            dx_vec = Arrow3D(start=p_center, end=p_dx, color=CYAN)
            dy_vec = Arrow3D(start=p_center, end=p_dy, color=MAGENTA)
            self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=tracker.duration * 0.3)
            self.play(Create(axes3d), Create(surface), run_time=tracker.duration * 0.1)
            self.play(Create(dx_vec), Create(dy_vec), run_time=tracker.duration * 0.1)
          
            dot.clear_updaters()
            tangent.clear_updaters()
        
        # 0:16 - 0:24 
        
        text_4 = "But what happens when multiple inputs produce multiple outputs simultaneously? We get a vector-valued transformation mapping one vector space directly into another."
        with self.voiceover(text=text_4) as tracker:
            self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=tracker.duration * 0.2)
            
            self.play(
                FadeOut(VGroup(plane, curve_1d, dot, tangent, deriv_label, simple_eq)),
                FadeOut(VGroup(surface, dx_vec, dy_vec, axes3d)),
                run_time=tracker.duration * 0.2
            )
            input_axes = Axes(x_range=[-3,3], y_range=[-3,3], axis_config={"color": CYAN}).scale(0.6).to_edge(LEFT)
            input_labels = input_axes.get_axis_labels(x_label="x", y_label="y")
            
            output_axes = Axes(x_range=[-3,3], y_range=[-3,3], axis_config={"color": MAGENTA}).scale(0.6).to_edge(RIGHT)
            output_labels = output_axes.get_axis_labels(x_label="f_1", y_label="f_2")
            vector_eq = MathTex(r"\vec{f}(x,y) = \begin{bmatrix} x+y \\ xy \end{bmatrix}").to_edge(UP)
            self.play(
                Create(input_axes), Write(input_labels),
                Create(output_axes), Write(output_labels),
                Write(vector_eq),
                run_time=tracker.duration * 0.3
            )
            particle_coords = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
            particles = VGroup(*[Dot(input_axes.c2p(x, y), color=CYAN, radius=0.08) for x, y in particle_coords])
            self.play(FadeIn(particles), run_time=tracker.duration * 0.1)
            
          
            particle_animations = [
                p_dot.animate.move_to(output_axes.c2p(x + y, x * y)).set_color(MAGENTA)
                for p_dot, (x, y) in zip(particles, particle_coords)
            ]
            self.play(*particle_animations, run_time=tracker.duration * 0.2)
        
        # 0:24 - 0:33 
        
        text_5 = "To track how every single output changes with respect to every single input, we organize all possible partial derivatives into a systematic matrix grid."
        with self.voiceover(text=text_5) as tracker:
            self.play(FadeOut(VGroup(input_axes, input_labels, output_axes, output_labels, particles)), run_time=tracker.duration * 0.2)
            
            jacobian_matrix = MathTex(
                r"\mathbf{J} = \begin{bmatrix}",
                r"\frac{\partial f_1}{\partial x}", r"&", r"\frac{\partial f_1}{\partial y}", r"\\",
                r"\frac{\partial f_2}{\partial x}", r"&", r"\frac{\partial f_2}{\partial y}",
                r"\end{bmatrix}"
            ).scale(1.3).move_to(ORIGIN)
            
            rect = SurroundingRectangle(jacobian_matrix, color=WHITE, buff=0.4)
            self.play(Create(rect), run_time=tracker.duration * 0.2)
            self.play(Write(jacobian_matrix), run_time=tracker.duration * 0.4)
            
            
            self.play(
                jacobian_matrix[1].animate.set_color(MAGENTA),
                jacobian_matrix[3].animate.set_color(MAGENTA),
                run_time=tracker.duration * 0.1
            )
         
            self.play(
                jacobian_matrix[3].animate.set_color(WHITE),
                jacobian_matrix[1].animate.set_color(CYAN),
                jacobian_matrix[5].animate.set_color(CYAN),
                run_time=tracker.duration * 0.1
            )
        
        # 0:33 - 0:42
        
        text_6 = "Differentiating f_1 = x+y gives us 1 and 1. Differentiating f_2 = xy gives us y and x. This structured grid is our Jacobian matrix."
        with self.voiceover(text=text_6) as tracker:
            self.play(
                vector_eq.animate.scale(0.8).to_corner(UL),
                FadeOut(rect),
                run_time=tracker.duration * 0.2
            )
            
            computed_matrix = MathTex(
                r"\mathbf{J} = \begin{bmatrix}", r"1", r"&", r"1", r"\\", r"y", r"&", r"x", r"\end{bmatrix}"
            ).scale(1.3).move_to(ORIGIN)
            
            self.play(
                ReplacementTransform(jacobian_matrix, computed_matrix),
                run_time=tracker.duration * 0.8
            )
        
        # 0:42 - 0:52
        
        text_7 = "Geometrically, the Jacobian acts as the ultimate local linear approximation. It tells us exactly how a tiny region of space stretches, rotates, or squashes under a complex transformation."
        with self.voiceover(text=text_7) as tracker:
            self.play(FadeOut(computed_matrix), FadeOut(vector_eq), run_time=tracker.duration * 0.2)
            
            grid = NumberPlane(axis_config={"color": WHITE})
            dx_dy_square = Polygon(
                grid.c2p(1, 1), grid.c2p(2, 1), grid.c2p(2, 2), grid.c2p(1, 2),
                color=CYAN, fill_opacity=0.5
            )
            
            self.play(Create(grid), FadeIn(dx_dy_square), run_time=tracker.duration * 0.2)
            
         
            matrix = np.array([[1.5, 0.5], [0.2, 1.2]])
            orig_corners = [np.array([1, 1]), np.array([2, 1]), np.array([2, 2]), np.array([1, 2])]
            transformed_corners = [grid.c2p(*(matrix @ p)) for p in orig_corners]
            
            parallelogram = Polygon(*transformed_corners, color=MAGENTA, fill_opacity=0.5)
            det_text = MathTex(r"\vert\mathbf{J}\vert").move_to(parallelogram.get_center()).set_color(GOLD)
            
            self.play(
                Transform(dx_dy_square, parallelogram),
                FadeIn(det_text),
                run_time=tracker.duration * 0.6
            )
        
        # 0:52 - 0:58
        
        text_8 = "This precise spatial tracking is what allows artificial intelligence to calculate change across millions of continuous dimensions at the exact same time."
        with self.voiceover(text=text_8) as tracker:
            ai_text = Text("HOW AI SEES SPACE", font_size=32, color=WHITE, weight=BOLD).move_to(ORIGIN)
            
            self.play(
                FadeOut(grid), FadeOut(dx_dy_square), FadeOut(det_text),
                FadeIn(ai_text, scale=1.2),
                run_time=tracker.duration * 1.0
            )
        
        # 0:58 - 1:08 
        
        text_9 = "Without the Jacobian, backpropagation in modern deep neural networks would be mathematically impossible. Want to master the visual math behind modern AI? Subscribe now so you don't miss the upcoming deep dive!"
        with self.voiceover(text=text_9) as tracker:
            self.play(FadeOut(ai_text), run_time=tracker.duration * 0.2)
            
            layers = [3, 4, 4, 2]
            nodes = VGroup()
            forward_edges = VGroup()
            backward_edges = VGroup()
            
            for i, layer_size in enumerate(layers):
                for j in range(layer_size):
                    y_pos = (j - (layer_size - 1) / 2.0) * 1.2
                    node = Circle(radius=0.15, color=WHITE, fill_opacity=1).move_to(
                        np.array([-4 + i*2.6, y_pos, 0])
                    )
                    nodes.add(node)
                    
            for i in range(len(layers)-1):
                layer1 = nodes[sum(layers[:i]):sum(layers[:i+1])]
                layer2 = nodes[sum(layers[:i+1]):sum(layers[:i+2])]
                for n1 in layer1:
                    for n2 in layer2:
                        forward_edges.add(Line(n1.get_center(), n2.get_center(), color=GRAY, stroke_opacity=0.3))
                        backward_edges.add(Line(n2.get_center(), n1.get_center(), color=MAGENTA, stroke_width=4))
            self.play(FadeIn(forward_edges), FadeIn(nodes), run_time=tracker.duration * 0.2)
            
            forward_pulse = forward_edges.copy().set_color(CYAN).set_stroke(width=3, opacity=1)
            
           
            self.play(Create(forward_pulse, lag_ratio=0.1), run_time=tracker.duration * 0.2)
            self.play(FadeOut(forward_pulse), Create(backward_edges, lag_ratio=0.1), run_time=tracker.duration * 0.2)
            
            cta_text = Text("FULL DEEP DIVE COMING SOON", font_size=36, color=GOLD, weight=BOLD).to_edge(DOWN)
            self.play(FadeIn(cta_text, shift=UP), run_time=tracker.duration * 0.2)
