"""Production starter for the Normal Distribution video series.

Render examples:
    manim -pqh normal_distribution_demo.py NormalDistributionDemo
    manim -pqh --flush_cache normal_distribution_demo.py NormalDistributionDemo

Use --flush_cache only after changing narration text or making broad scene changes.
"""

from __future__ import annotations

from typing import Iterable

from manim import (
    Axes,
    Circle,
    Create,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    GRAY_B,
    LEFT,
    Line,
    MathTex,
    ORIGIN,
    ReplacementTransform,
    RIGHT,
    Scene,
    Text,
    UP,
    VGroup,
    WHITE,
    config,
    linear,
    smooth,
)
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


# ---------------------------------------------------------------------------
# Series-wide visual DNA. Keep scene-specific colors below this section rare.
# ---------------------------------------------------------------------------
BACKGROUND = "#0F172A"       # deep slate
CYAN = "#38BDF8"              # active curves and geometry
GOLD = "#FACC15"              # means, metrics, area
RED = "#EF4444"               # warnings and contrast
PURPLE = "#C084FC"            # subdued secondary geometry
MUTED_BLUE = "#3B82F6"
TEXT = "#FFFFFF"
TITLE_FONT = "Impact"
BODY_FONT = "DejaVu Sans"
MIN_RUN_TIME = 0.25
VOICE_PADDING = 0.18


def sync_time(tracker, elapsed: float = 0.0, padding: float = VOICE_PADDING) -> float:
    """Return the remaining voiceover time without allowing invalid run times."""
    return max(float(tracker.duration) - elapsed - padding, MIN_RUN_TIME)


def title(text: str, scale: float = 0.72, color: str = TEXT) -> Text:
    """Create a consistent documentary-style title."""
    return Text(text, font=TITLE_FONT, color=color).scale(scale).to_edge(UP)


def narration(scene: VoiceoverScene, text: str):
    """Keep the audio backend in one place so it can be swapped later."""
    return scene.voiceover(text=text)


class NormalDistributionDemo(VoiceoverScene):
    """A compact example of intuition -> geometry -> mathematical statement."""

    def construct(self) -> None:
        config.background_color = BACKGROUND
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # These objects intentionally live for the whole scene. Rapid method or
        # parameter changes can then transform them instead of redrawing them.
        axes = None
        curve = None
        mean_line = None

        with narration(
            self,
            "A normal distribution is not a formula that happens to make a bell. "
            "It is the geometric signature of many small, independent effects.",
        ) as tracker:
            heading = title("WHY DOES THE BELL CURVE APPEAR?")
            prompt = Text(
                "Many small effects  →  one stable shape",
                font=BODY_FONT,
                color=TEXT,
            ).scale(0.55).next_to(heading, DOWN, buff=0.45)
            self.play(FadeIn(heading, shift=DOWN), run_time=0.4)
            self.play(FadeIn(prompt, shift=UP), run_time=1)
            self.wait(2)
            self.play(FadeOut(prompt), run_time = .7)

        with narration(
            self,
            "Start with a variable centered at zero. As random contributions accumulate, "
            "the middle becomes more likely than either extreme.",
        ) as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 0.45, 0.1],
                x_length=9,
                y_length=3.8,
                axis_config={"color": GRAY_B, "stroke_width": 2},
                tips=False,
            ).shift(DOWN * 0.45)
            curve = axes.plot(
                lambda x: 0.4 * (2.71828 ** (-(x**2) / 2)),
                x_range=[-4, 4],
                color=CYAN,
                stroke_width=6,
            )
            curve_label = MathTex(r"f(x; 0, 1)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}", color=CYAN)
            curve_label.scale(0.8).to_corner(RIGHT + UP, buff=1.55)
            self.play(FadeOut(prompt), Create(axes), run_time=0.45)
            self.play(Create(curve), FadeIn(curve_label), run_time=sync_time(tracker, 0.45))

        with narration(
            self,
            "Its symmetry tells us something concrete: the mean is the balance point, "
            "and the area under the curve represents total probability.",
        ) as tracker:
            mean_line = Line(
                axes.c2p(0, 0), axes.c2p(0, 0.4), color=GOLD, stroke_width=5
            )
            mean_label = Text("mode = mean = median", font=BODY_FONT, color=GOLD).scale(0.45)
            mean_label.next_to(mean_line, UP, buff=0.12)
            area = axes.get_area(curve, x_range=[-4, 4], color=GOLD, opacity=0.35)
            self.play(Create(mean_line), FadeIn(mean_label), run_time=0.35)
            # right now, the mean, median, and mode are all at the same location, so we can animate them together
            self.play(FadeIn(area), run_time=sync_time(tracker, 0.35))

        with narration(
            self,
            "So the bell curve is a visual statement before it is an algebraic one: "
            "balance in the center, symmetry on both sides, and probability as area.",
        ) as tracker:
            summary = Text(
                "BALANCE  •  SYMMETRY  •  AREA",
                font=TITLE_FONT,
                color=WHITE,
            ).scale(0.72).to_edge(DOWN, buff=0.55)
            area1 = axes.get_area(curve, x_range=[0, 4], color=CYAN, opacity=0.35)
            area2 = axes.get_area(curve, x_range=[-4, 0], color=PURPLE, opacity=0.35)
            self.play(FadeIn(area1), run_time=0.2)
            self.wait(.1)
            self.play(FadeIn(area2), run_time=0.2)
            self.wait(.1)
            self.play(FadeOut(area1), run_time=0.2)
            self.wait(.1)
            self.play(FadeOut(area2), run_time=0.2)
            self.wait(2)
            curve = axes.plot(
                lambda x: 0.4 * (2.71828 ** (-(x**2) / 2)),
                x_range=[-4, 4],
                color=RED,
                stroke_width=6,
            )
            self.play(Create(curve), run_time=1)
            self.wait(.3)
            self.play(FadeOut(curve), run_time=1)
            self.play(FadeIn(summary, scale=1.15), run_time=sync_time(tracker))
            self.wait(0.2)


__all__ = ["NormalDistributionDemo", "BACKGROUND", "CYAN", "GOLD", "RED", "PURPLE"]
