# Week 2 - Day 2: Probability & Distributions

## Overview

Focused on the mathematical foundations of probability used in Machine Learning, including probability rules, conditional probability, Bayes' theorem, and the three most common probability distributions used in ML.

---

## Files

- `day2_probability.ipynb` — detailed notes, mathematical explanations, worked examples, visualizations, and Python implementations.
- `Hands_On_Lab.ipynb` — official hands-on exercises with simulations and result verification.

---

## Topics Covered

### Probability Fundamentals

- Sample Space
- Events
- Random Experiments
- Random Variables
- Probability notation
- Discrete vs Continuous Random Variables

### Core Probability Rules

- Complement Rule
- Addition Rule
- Multiplication Rule
- Independent Events
- Probability calculations with worked examples
- Python verification using NumPy

### Conditional Probability

- Definition of conditional probability
- Formula intuition
- Student-major worked example
- Manual calculation
- Python simulation to verify the result

### Bayes' Theorem

- Prior
- Likelihood
- Posterior
- Medical test example
- Demonstrated why a **99% accurate test** can still correspond to only about a **16.67% probability** of actually having a rare disease.

### Probability Distributions

#### Normal Distribution

- Bell-shaped distribution
- Mean and standard deviation
- 68–95–99.7 rule
- PDF intuition
- Sampling with `scipy.stats.norm`
- Histogram visualization
- ML applications:
  - Feature distributions
  - Measurement errors
  - Anomaly detection

#### Binomial Distribution

- Discrete probability distribution
- Bernoulli trials
- Conditions of a Binomial experiment
- Formula intuition
- Coin-flip simulations
- `scipy.stats.binom`
- ML applications:
  - Classification probabilities
  - A/B testing
  - Success/failure modeling

#### Uniform Distribution

- Discrete vs Continuous Uniform
- Equal probability for all outcomes
- PDF intuition
- `scipy.stats.uniform`
- Uniform random sampling
- ML applications:
  - Random initialization
  - Random sampling
  - Simulation

### Distribution Comparison

- Normal vs Binomial vs Uniform
- Key properties
- Real Machine Learning use cases
- When each distribution is appropriate

---

## Hands-On Lab

Implemented and verified three probability simulations:

- Simulated **10,000 coin flips** and confirmed the proportion of heads converged to approximately **0.5**.
- Generated samples from a **Normal Distribution** and verified the expected bell-shaped histogram.
- Simulated a **Conditional Probability** scenario (pass rate given study hours) and compared:
  - Expected probability: **0.80**
  - Simulation result: **0.795**

All simulation results closely matched their theoretical expectations.

---

## Libraries Used

- NumPy
- SciPy (`scipy.stats`)
- Matplotlib

---

## Skills Practiced

- Applying probability rules mathematically and programmatically
- Computing conditional probabilities
- Applying Bayes' theorem
- Working with Normal, Binomial, and Uniform distributions
- Generating random samples
- Running Monte Carlo-style probability simulations
- Visualizing probability distributions
- Comparing theoretical and simulated probabilities
- Connecting probability concepts to real Machine Learning applications