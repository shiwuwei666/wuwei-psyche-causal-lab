# Wuwei Psyche Causal Lab · Overview (English)

This repository is a **lab edition** of a psychological causal engine
built around the chain:

> Motive → Belief → Affect → Behavior

The goal is to turn human psychological structure into a **computable intermediate layer**, with:

- A structured `PsycheVector` extracted from text
- A simplified causal graph (M → B → A → C → Risk)
- A small **counterfactual demo** to ask:
  > "What if this belief were a bit softer?"

## 1. Modules

- `engine/vectorizer`: text → PsycheVector
- `engine/causal/simple_causal_engine.py`: simplified causal graph & counterfactual demo
- `engine/causal/advanced_placeholder.py`: placeholder for the non-open-sourced advanced engine
- `engine/persona`: simple persona buckets
- `engine/strategy`: low-risk suggestion generator
- `engine/safety`: safety filters & risk limits
- `engine/runtime`: EngineCore orchestrator

The **advanced causal engine (M3.4 / M3.5 / M3.6)** is *not* part of this repo.
It remains proprietary and is under ongoing research & patent planning.

## 2. Intended Users

- Researchers in psychology / behavioral science
- Conversational AI / affective computing / UX engineers
- People exploring human-like intelligence architectures
- Curious minds who want to see "how motives and beliefs can be modeled"

## 3. Safety & Scope

Please read:

- `DISCLAIMER.md`
- `ETHICS.md`
- `SECURITY.md`

This lab edition is only suitable for:

- Research & teaching
- Prototyping and UX experiments
- Visualizing and discussing psychological causal structures

It is **not** intended for:

- Medical diagnosis or treatment
- Closed-loop emotional control over minors
- Addictive product optimization
- Any unlawful or high-risk applications

## 4. Relation to the full architecture

The full system behind this repo includes:

- Ψ / Φ / Ξ three-domain mind dynamics engine
- A richer M-B-A-C psychological state model
- An external rules base (world rules)
- Advanced causal simulation and counterfactual reasoning modules

This repository exposes only:

- A subset of the intermediate representation (PsycheVector)
- A demonstrative causal graph
- A toy-level counterfactual demo
- Clear safety & ethics boundaries

The aim is to provide a **usable, inspectable starting point** for research and engineering,
while keeping the core commercial / patented algorithms private.