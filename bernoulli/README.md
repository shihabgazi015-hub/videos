# How Coin ① Flips Power Modern AI: The Bernoulli Distribution

<a href="https://youtube.com" target="_blank">
  <img src="https://i9.ytimg.com/vi/_lMnfZlsALY/mqdefault_custom_2.jpg?v=6a94cf10&sqp=CPzT4dQG&rs=AOn4CLBQOHVQPkGVVkgbhyb_rBo7n9Nkmw" width="300vw" style="border-radius: 800px; box-shadow: 0 4px 8px rgba(155, 204, 237, 0.8);"/>
</a>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen?style=for-the-badge&logo=python)](https://www.python.org/)
[![Manim Engine](https://img.shields.io/badge/Rendered%20With-Manim-orange?style=for-the-badge)](https://www.manim.community/)
<br>
> An intuitive, visual guide connecting the fundamental binary trial to modern Artificial Intelligence, A/B testing, and Galton boards.

---

## 📌 Executive Overview

Underneath complex neural networks, binary classification models, and digital data pipelines sits the **Bernoulli Distribution**—the foundational atom of uncertainty. Rather than viewing statistics as abstract algebraic formulas, this repository provides physical and geometric intuition:
* **Expected Value ($E[X]$)** as the **Center of Mass / Fulcrum** of a physical balance beam.
* **Variance ($$Var(X)$$)** as the **Rotational Inertia** when spinning the beam.

---

## 🧮 Mathematical Foundations & Physical Analogies

### 1. The Bernoulli Trial
A single event with two mutually exclusive outcomes:
* **Success ($X = 1$)** with probability $p$
* **Failure ($X = 0$)** with probability $1 - p$

$$\mathbb{P}(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$$

---

### 2. Expected Value ($E[X]$) as Center of Gravity
Placing mass $(1-p)$ at position $x=0$ and mass $p$ at position $x=1$ on a weightless rod, the fulcrum position for balance is:

$$\mathbb{E}[X] = 0 \cdot (1-p) + 1 \cdot p = p$$

---

### 3. Variance ($$Var(X)$$) as Rotational Inertia
Variance measures rotational resistance around the pivot:

$$Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = p(1-p)$$

 Variance Curve: Var(X) = p(1 - p)

 * **At $p = 0.5$**: Maximum entropy ($$Var(X) = 0.25$$). Highest unpredictability.
* **At $p \to 0$ or $p \to 1$**: Mass concentrates near the fulcrum. Rotational inertia drops to 0 (high certainty).

---

## 📂 Repository File Structure & Animation Scenes

The Manim animation scripts rendering the visual scenes in the video are structured as follows:

| File Name | Description / Visual Scene |
| :--- | :--- |
| `01.py` | **Intro Scene**: Binary splits, coin flips, and AI neural net connection. |
| `2.py` | **Bernoulli Balance Beam**: Interactive fulcrum movement & Expected Value geometry. |
| `3.py` | **Variance & Inertia**: Rotational beam dynamics and moment of inertia physics. |
| `4.py` | **The Uncertainty Parabola**: Plotting $p(1-p)$ across probability spectrums. |
| `bernoulli_5.py` | **Basketball Shot Analogy & Galton Board**: Scaling single trials to Binomial distributions. |
| `6.py` | **Conclusion & Voiceover**: Real-world applications (A/B testing, AI loss functions). |
| `7.py` | **Puzzle & Outro**: Random Walk infinite convergence puzzle. |
| `Bernoulli.pdf` / `.tex` | Full mathematical LaTeX derivation document. |

---

## 🚀 Interactive Python Simulations

### 1. Bernoulli & Galton Board Simulator
Run this script to simulate $N$ Bernoulli trials converging into a Binomial Distribution:

```python
import numpy as np

def simulate_bernoulli_trials(p: float, n_trials: int = 10000):
    # Single Bernoulli Trial
    outcomes = np.random.binomial(n=1, p=p, size=n_trials)
    mean = np.mean(outcomes)
    variance = np.var(outcomes)
    
    print(f"--- Bernoulli Trial Simulation (p={p}) ---")
    print(f"Theoretical E[X]   : {p:.4f} | Simulated E[X]   : {mean:.4f}")
    print(f"Theoretical Var(X) : {p*(1-p):.4f} | Simulated Var(X) : {variance:.4f}\n")

simulate_bernoulli_trials(p=0.5)
simulate_bernoulli_trials(p=0.9)

def compute_ab_sample_size(p1: float, p2: float, alpha=0.05, beta=0.2):
    delta = abs(p2 - p1)
    p_avg = (p1 + p2) / 2
    # Approximate sample size per variation
    n = (2 * p_avg * (1 - p_avg) * (1.96 + 0.84)**2) / (delta**2)
    return int(np.ceil(n))

print(f"Required Users per Variant (p1=5%, p2=6%): {compute_ab_sample_size(0.05, 0.06)}")
```

# The Infinite Random Walk Puzzle

Welcome to the end-of-episode challenge for the video **How Coin Flips Power Modern AI (The Bernoulli Distribution)**.

## The Challenge

If we chain independent Bernoulli steps ($X_i \in \{-1, +1\}$ with $p=0.5$) tip-to-toe into a Random Walk:

$$S_N = \sum_{i=1}^N X_i$$

1. What happens to the Center of Gravity $\mathbb{E}[S_N]$ as $N \to \infty$?
2. What happens to the Rotational Inertia $Var(S_N)$ as $N \to \infty$?

## How to Participate

* Share your mathematical proof or intuition in the video comments.
* Submit a Pull Request to this repository with your written solution or simulation code.

## Watch the Video

For the complete visual journey with step-by-step animations, watch the full video on YouTube:

[Watch the Full Video Here](https://www.youtube.com/watch?v=_lMnfZlsALY)

## Credits

Created by **Shihab Gazi** • Department of Statistics, SUST
