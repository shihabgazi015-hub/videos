from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import numpy as np
import random

class BernoulliToBinomial(VoiceoverScene):
    def construct(self):
        # 1. Voiceover Setup
        self.set_speech_service(GTTSService(lang="en"))
        
        # 2. Color Palette Constraints
        C_BG = "#0B0E14"
        C_NEON_GREEN = "#39FF14"
        C_ICE_CYAN = "#00E5FF"
        C_YELLOW = "#FFFF00"
        C_RED = "#FF2400"
        
        config.background_color = C_BG

        # ==========================================
        #  49: The Single Trial
        # ==========================================
        bar = Line(LEFT * 1.5, RIGHT * 1.5, color=WHITE)
        fulcrum = Triangle(fill_opacity=1, color=C_YELLOW).scale(0.2).next_to(bar, DOWN)
        m1 = Circle(radius=0.4, fill_opacity=1, color=C_ICE_CYAN).move_to(bar.get_start())
        m2 = Circle(radius=0.4, fill_opacity=1, color=C_NEON_GREEN).move_to(bar.get_end())
        lever = VGroup(bar, fulcrum, m1, m2)

        with self.voiceover(text="So far, we have focused entirely on a single, isolated coin flip—one Bernoulli trial.") as tracker:
            self.play(FadeIn(lever), run_time=1)
            self.play(lever.animate.scale(0.4), run_time=1)
            circle_n1 = Circle(color=C_ICE_CYAN).surround(lever)
            label_n1 = MathTex("n = 1", color=C_ICE_CYAN).next_to(circle_n1, DOWN)
            self.play(Create(circle_n1), Write(label_n1), run_time=5)  # 2s → 7s
            self.play(FadeOut(lever), FadeOut(circle_n1), FadeOut(label_n1), run_time=1)  # 7s → 8s ✅

        # ==========================================
        #  50: Duplication
        # ==========================================
        with self.voiceover(text="But what happens when we don't just flip one coin? What happens when we repeat this game over and over?") as tracker:
            levers_with_labels = VGroup()
            for i in range(5):
                single_lever = lever.copy()
                label = MathTex(f"n = {i+1}", color=C_ICE_CYAN).scale(0.5).next_to(single_lever, DOWN)
                levers_with_labels.add(VGroup(single_lever, label))

            levers_with_labels.arrange(RIGHT, buff=0.5)
            self.play(FadeIn(levers_with_labels), run_time=1)
            self.play(levers_with_labels.animate.set_color(C_NEON_GREEN), rate_func=there_and_back, run_time=tracker.duration - 2)
            self.play(FadeOut(levers_with_labels), run_time=1)


        # ==========================================
        #  51: Branching Tree
        # ==========================================
        with self.voiceover(text="As we add trials, a branching tree of possible futures explodes exponentially...") as tracker:
            tree_group = VGroup()
            top_node = Dot(UP * 2.5, color=WHITE)
            # Level 1
            l1_l = Dot(UP * 1 + LEFT * 2, color=C_ICE_CYAN)
            l1_r = Dot(UP * 1 + RIGHT * 2, color=C_NEON_GREEN)
            # Level 2
            l2_ll = Dot(DOWN * 0.5 + LEFT * 3, color=C_ICE_CYAN)
            l2_lr = Dot(DOWN * 0.5 + LEFT * 1, color=C_NEON_GREEN)
            l2_rl = Dot(DOWN * 0.5 + RIGHT * 1, color=C_ICE_CYAN)
            l2_rr = Dot(DOWN * 0.5 + RIGHT * 3, color=C_NEON_GREEN)
            
            edges = VGroup(
                Line(top_node, l1_l), Line(top_node, l1_r),
                Line(l1_l, l2_ll), Line(l1_l, l2_lr),
                Line(l1_r, l2_rl), Line(l1_r, l2_rr)
            )
            tree_group.add(edges, top_node, l1_l, l1_r, l2_ll, l2_lr, l2_rl, l2_rr)
            
            self.play(FadeIn(tree_group), run_time=tracker.duration)

        # ==========================================
        #  52: Galton Board Morph
        # ==========================================
        with self.voiceover(text="...forming a physical pegboard of probability known as a Galton Board.") as tracker:
            pegs = VGroup()
            for row in range(7):
                for col in range(row + 1):
                    x = (col - row / 2.0) * 0.7
                    y = 2.5 - row * 0.7
                    pegs.add(Dot(point=[x, y, 0], color=LIGHT_GREY, radius=0.06))
            
            self.play(ReplacementTransform(tree_group, pegs), run_time=tracker.duration)

        # ==========================================
        #  53: Single Orb Drop
        # ==========================================
        with self.voiceover(text="Every single peg represents one Bernoulli trial—a coin toss forcing a ball to bounce left or right.") as tracker:
            orb = Dot(point=[0, 3.2, 0], color=C_YELLOW, radius=0.12)
            self.play(FadeIn(orb), run_time=0.5)
            
            bounce_path = [
                [0, 2.5, 0], [-0.35, 1.8, 0], [0, 1.1, 0],
                [0.35, 0.4, 0], [0, -0.3, 0], [-0.35, -1.0, 0], [0, -1.7, 0]
            ]
            
            for pt in bounce_path:
                self.play(orb.animate.move_to(pt), run_time=(tracker.duration - 0.5) / len(bounce_path), rate_func=linear)

        # ==========================================
        #  54: The Cascade
        # ==========================================
        with self.voiceover(text="When thousands of these individual binary decisions happen simultaneously...") as tracker:
            self.play(FadeOut(orb), run_time=0.5)
            particles = VGroup(*[
                Dot(point=[random.uniform(-0.1, 0.1), 3.5 + random.uniform(0, 2), 0], 
                    color=random.choice([C_ICE_CYAN, C_NEON_GREEN]), radius=0.04) 
                for _ in range(80)
            ])
            self.play(FadeIn(particles), run_time=0.5)
            
            offsets = np.random.normal(0, 1.5, (80,))
            self.play(
                *[
                    particles[i].animate.shift(DOWN * 6 + RIGHT * offsets[i])
                    for i in range(80)
                ],
                run_time=tracker.duration - 1
            )
            self.play(FadeOut(particles), run_time=0.5)

        # ==========================================
        #  55: The Histogram
        # ==========================================
        with self.voiceover(text="...the chaotic individual paths stack up into an amazingly predictable shape.") as tracker:
            hist_heights = [0.2, 0.8, 2.2, 3.8, 2.2, 0.8, 0.2]
            bars = VGroup()
            for i, h in enumerate(hist_heights):
                bar = Rectangle(height=0.01, width=0.6, fill_opacity=0.8, color=C_ICE_CYAN, stroke_width=0)
                bar.move_to([(i - 3) * 0.7, -3, 0], aligned_edge=DOWN)
                bars.add(bar)

            self.play(FadeIn(bars), run_time=0.5)
            animations = []
            for i, h in enumerate(hist_heights):
                bars[i].generate_target()
                bars[i].target.stretch_to_fit_height(h)
                bars[i].target.move_to([(i - 3) * 0.7, -3, 0], aligned_edge=DOWN)
                animations.append(MoveToTarget(bars[i]))
                
            self.play(AnimationGroup(*animations, lag_ratio=0.1), run_time=tracker.duration - 0.5)

        # ==========================================
        #  56: The Binomial Distribution
        # ==========================================
        with self.voiceover(text="This is the Binomial distribution—the sum of n independent Bernoulli coin flips.") as tracker:
            curve = FunctionGraph(
                lambda x: 3.8 * np.exp(-1 * x**2) - 3, 
                color=C_NEON_GREEN, x_range=[-2.5, 2.5]
            )
            formula_dist = MathTex(r"X \sim \text{Binomial}(n, p)", color=WHITE).next_to(curve, UP)
            
            self.play(Create(curve), run_time=tracker.duration / 2)
            self.play(Write(formula_dist), run_time=tracker.duration / 2)

        # ==========================================
        #  57: Expectation & Variance
        # ==========================================
        with self.voiceover(text="And because expectation and variance add up cleanly, its center and spread are completely determined by our single coin.") as tracker:
            eq1 = MathTex(r"\mathbb{E}[X] = n", r"p")
            eq2 = MathTex(r"\text{Var}(X) = n", r"p", r"(1-p)")
            
            eq1[1].set_color(C_YELLOW)
            eq2[1].set_color(C_YELLOW)
            eq2[2].set_color(C_YELLOW)
            
            equations = VGroup(eq1, eq2).arrange(DOWN).to_edge(LEFT).shift(UP * 1.5)
            
            self.play(Write(eq1), run_time=tracker.duration / 2)
            self.play(Write(eq2), run_time=tracker.duration / 2)

        # ==========================================
        #  58: Returning to Tech
        # ==========================================
        with self.voiceover(text="This bridges the gap directly back to where we started...") as tracker:
            self.play(
                FadeOut(pegs), FadeOut(bars), FadeOut(curve), FadeOut(formula_dist), FadeOut(equations),
                run_time=1
            )
            
            # Neural network grid creation
            nn_nodes = VGroup(*[Dot(point=[x, y, 0], color=WHITE, radius=0.08) for x in [-4, -1.5, 1.5, 4] for y in [-2.5, 0, 2.5]])
            nn_edges = VGroup()
            
            for n1 in nn_nodes[:3]:
                for n2 in nn_nodes[3:6]: nn_edges.add(Line(n1, n2, stroke_opacity=0.3, color=C_ICE_CYAN))
            for n1 in nn_nodes[3:6]:
                for n2 in nn_nodes[6:9]: nn_edges.add(Line(n1, n2, stroke_opacity=0.3, color=C_ICE_CYAN))
            for n1 in nn_nodes[6:9]:
                for n2 in nn_nodes[9:]: nn_edges.add(Line(n1, n2, stroke_opacity=0.3, color=C_ICE_CYAN))
                
            network = VGroup(nn_edges, nn_nodes)
            network.apply_matrix(np.array([[1, 0.4, 0], [0, 0.8, 0], [0, 0, 1]], dtype=float))  # Fake 3D isometric tilt
            
            self.play(FadeIn(network), run_time=tracker.duration - 1)

        # ==========================================
        #  59: Data Pulses
        # ==========================================
        with self.voiceover(text="...showing that every complex neural network or data pipeline is just millions of simple coin flips working together.") as tracker:
            pulses = VGroup(*[
                Dot(color=random.choice([C_NEON_GREEN, C_YELLOW]), radius=0.06).move_to(e.get_start()) 
                for e in list(nn_edges)[:15]
            ])
            self.play(FadeIn(pulses), run_time=0.5)
            self.play(*[MoveAlongPath(p, e) for p, e in zip(pulses, list(nn_edges)[:15])], run_time=tracker.duration - 1)
            self.play(FadeOut(pulses), run_time=0.5)

        # ==========================================
        #  60: The Atom of Uncertainty
        # ==========================================
        with self.voiceover(text="The humble coin flip isn't just basic math—it is the fundamental atom of uncertainty across the modern digital world.") as tracker:
            wireframe_coin = VGroup(
                Circle(radius=1.2, color=LIGHT_GREY, fill_opacity=0.1).set_stroke(width=3),
                Circle(radius=0.9, color=C_ICE_CYAN).set_stroke(width=1),
                MathTex("1 / 0", color=C_NEON_GREEN).scale(1.2)
            )
            
            self.play(ReplacementTransform(network, wireframe_coin), run_time=tracker.duration - 2)
            
            shockwave = Circle(radius=1.2, color=WHITE).set_stroke(width=6)
            self.play(
                shockwave.animate.scale(6),
                FadeOut(shockwave),
                run_time=2
            )
