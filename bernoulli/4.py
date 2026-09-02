from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BernoulliAnalogyAndMistakes(VoiceoverScene):
    def construct(self):
        
        # COLOR PALETTE & ENVIRONMENT SETUP
        
        BG_COLOR = "#0B0E14"
        NEON_GREEN = "#39FF14"
        ICE_CYAN = "#00E5FF"
        ORANGE = "#FF8C00"
        RED_ALERT = "#FF2400"
        
        self.camera.background_color = BG_COLOR
        self.set_speech_service(GTTSService(lang="en"))

        
        #  37: The Recap Split Screen
        
        lever_recap = Line(LEFT*1.5, RIGHT*1.5, color=WHITE).shift(LEFT*3)
        fulcrum_recap = Triangle(color=YELLOW).scale(0.2).next_to(lever_recap, DOWN, buff=0)
        parabola_axes = Axes(x_range=[0, 1, 0.5], y_range=[0, 0.3, 0.1], x_length=3, y_length=2).shift(RIGHT*3)
        parabola_curve = parabola_axes.plot(lambda x: x*(1-x), color=NEON_GREEN)
        
        recap_group = VGroup(lever_recap, fulcrum_recap, parabola_axes, parabola_curve)
        recap_title = Text("Recap", font_size=48, color=ICE_CYAN).to_edge(UP)

        with self.voiceover(text="So, let's do a quick recap. We’ve built our balance beam, and we've felt the rotational resistance.") as tracker:
            self.play(
                FadeIn(recap_title), 
                Create(recap_group), 
                run_time=max(0.1, tracker.duration)
            )

        
        #  38: Transition to Real World
        
        real_world_text = Text("The Real World", font_size=60, color=ORANGE)
        
        with self.voiceover(text="But to really cement this intuition, we need to bring it down to earth with a real-world analogy.") as tracker:
            self.play(
                FadeOut(recap_group), 
                FadeOut(recap_title), 
                run_time=max(0.1, tracker.duration * 0.4)
            )
            self.play(
                Write(real_world_text), 
                run_time=max(0.1, tracker.duration * 0.6)
            )

        
        #  39: Basketball Analogy
        
        basketball = Circle(radius=0.8, color=ORANGE, fill_opacity=0.8)
        lines = VGroup(
            Line(UP*0.8, DOWN*0.8, color=BG_COLOR),
            Arc(radius=0.8, angle=PI/2, color=BG_COLOR).shift(LEFT*0.4),
            Arc(radius=0.8, angle=PI/2, color=BG_COLOR).shift(RIGHT*0.4).rotate(PI)
        )
        ball_group = VGroup(basketball, lines).shift(DOWN*0.5)

        make_box = Text("Make (1)", font_size=36, color=NEON_GREEN).shift(LEFT*3 + UP*2)
        miss_box = Text("Miss (0)", font_size=36, color=ICE_CYAN).shift(RIGHT*3 + UP*2)

        with self.voiceover(text="Imagine you are shooting a basketball free throw. You either make the shot, a one, or miss it, a zero.") as tracker:
            self.play(
                FadeOut(real_world_text), 
                run_time=max(0.1, tracker.duration * 0.3)
            )
            self.play(
                FadeIn(ball_group, shift=UP*2),
                FadeIn(make_box, shift=RIGHT), 
                FadeIn(miss_box, shift=LEFT),
                run_time=max(0.1, tracker.duration * 0.7)
            )

        
        #  40: Beginner Stats p = 0.2
        
        p_stat = MathTex(r"p = 0.2", font_size=64, color=WHITE).next_to(ball_group, UP, buff=0.8)

        with self.voiceover(text="If you are a total beginner, maybe your chance of making it is only twenty percent. So, p equals 0.2.") as tracker:
            self.play(
                ball_group.animate.scale(0.5).shift(DOWN*1.5),
                FadeOut(make_box), 
                FadeOut(miss_box),
                Write(p_stat),
                run_time=max(0.1, tracker.duration)
            )

        
        #  41: Expected Value Calculation
        
        ev_calc = MathTex(r"\mathbb{E}[X] = 0.2", font_size=52, color=NEON_GREEN).next_to(p_stat, RIGHT, buff=1)

        with self.voiceover(text="Your expected value for a single shot is just 0.2 points. But what about the variance?") as tracker:
            self.play(
                VGroup(ball_group, p_stat).animate.shift(LEFT*2),
                Write(ev_calc),
                run_time=max(0.1, tracker.duration)
            )

        
        #  42: Variance Calculation
        
        var_calc = MathTex(r"\text{Var}(X) = 0.2 \times 0.8 = 0.16", font_size=52, color=ICE_CYAN).next_to(ev_calc, DOWN, buff=0.5)

        with self.voiceover(text="Let's plug it in: 0.2 times its complement, 0.8, gives a variance of 0.16. Pretty small.") as tracker:
            self.play(
                Write(var_calc), 
                run_time=max(0.1, tracker.duration)
            )

        
        #  43: Predictable = Low Variance
        
        predictable_text = Text("Predictable       Low Variance", font_size=36, color=ICE_CYAN).next_to(var_calc, DOWN, buff=1)

        with self.voiceover(text="Because you are consistently missing, your outcome is actually highly predictable. Low variance.") as tracker:
            self.play(
                VGroup(p_stat, ev_calc, var_calc).animate.set_opacity(0.4),
                FadeIn(predictable_text, shift=UP),
                run_time=max(0.1, tracker.duration)
            )

        
        #  44: The Common Mistake Trap
        
        safe_bet = Text("50/50 is a Safe Bet", font_size=64, color=WHITE)
        

        with self.voiceover(text="Now, here is a common trap. A lot of people think a fifty-fifty shot is the 'safest' bet.") as tracker:
            self.play(
                FadeOut(ball_group), 
                FadeOut(p_stat), 
                FadeOut(ev_calc), 
                FadeOut(var_calc), 
                FadeOut(predictable_text),
                run_time=max(0.1, tracker.duration * 0.4)
            )
            self.play(
                Write(safe_bet), 
                run_time=max(0.1, tracker.duration * 0.4)
            )
            self.wait(1)

        
        #  45: Climbing to the Peak
        
        axes = Axes(x_range=[0, 1, 0.25], y_range=[0, 0.3, 0.1], x_length=7, y_length=4)
        curve = axes.plot(lambda x: x * (1 - x), color=WHITE)
        red_dot = Dot(axes.c2p(0.2, 0.16), color=RED_ALERT).scale(1.5)

        with self.voiceover(text="But mathematically, it is the exact opposite.") as tracker:
            self.play(
                FadeOut(safe_bet),
                
                Create(axes),
                Create(curve),
                FadeIn(red_dot),
                run_time=max(0.1, tracker.duration)
            )

        
        #  46: Peak of the Parabola
        
        peak_pos = axes.c2p(0.5, 0.25)
        
        with self.voiceover(text="At p equals 0.5, your variance hits 0.25—the absolute peak of our curve.") as tracker:
            self.play(
                red_dot.animate.move_to(peak_pos),
                run_time=max(0.1, tracker.duration)
            )

        
        #  47: Maximum Chaos
        
        chaos_text = Text("Maximum Chaos", font_size=48, color=RED_ALERT).next_to(red_dot, UP, buff=0.5)
        shockwave = Circle(radius=0.1, color=RED_ALERT).move_to(peak_pos)

        with self.voiceover(text="It is the zone of maximum chaos. You are completely unpredictable.") as tracker:
            self.play(
                Write(chaos_text), 
                run_time=max(0.1, tracker.duration * 0.4)
            )
            self.play(
                shockwave.animate.scale(30).set_opacity(0), 
                run_time=max(0.1, tracker.duration * 0.6)
            )

        
        #  48: Predictability is Safety
        
        safe_dots = VGroup(
            Dot(axes.c2p(0, 0), color=ICE_CYAN).scale(2),
            Dot(axes.c2p(1, 0), color=ICE_CYAN).scale(2)
        )
        safe_text = Text("Predictable = Safe", font_size=36, color=ICE_CYAN).next_to(axes, DOWN, buff=0.5)

        with self.voiceover(text="To a statistician, predictability is safety, whether you are always winning, or always losing.") as tracker:
            self.play(
                red_dot.animate.set_color(WHITE),
                chaos_text.animate.set_opacity(0.3),
                FadeIn(safe_dots),
                FadeIn(safe_text, shift=UP),
                run_time=max(0.1, tracker.duration)
            )
            
        self.wait(1)
