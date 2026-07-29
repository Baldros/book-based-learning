# Transformers: The Definitive Guide

> Study notes, implementations, and experiments inspired by
> *Transformers: The Definitive Guide* by Nicole Koenigstein (O'Reilly Media, 2026).

[![Book](https://img.shields.io/badge/O'Reilly-Book-D16C32?logo=oreilly)](https://www.oreilly.com/library/view/transformers-the-definitive/9781098167004/)
[![Official code](https://img.shields.io/badge/GitHub-Official_Code-181717?logo=github)](https://github.com/Nicolepcx/transformers-the-definitive-guide)
[![Level](https://img.shields.io/badge/Level-Intermediate–Advanced-4C1)](#prerequisites)
[![Status](https://img.shields.io/badge/Status-In_Progress-yellow)](#study-progress)

## About this repository

This directory documents a hands-on study of the book. It contains personal notes,
reimplementations, visual explanations, and experiments designed to connect the
book's theory with working code.

The central idea is that transformers are not merely language models. The same
architecture can operate on text tokens, time-series patches, image patches,
video frames, and spectrogram slices. Once these shared patterns are understood,
transformers become reusable building blocks for larger systems—including
reasoning models, reinforcement-learning systems, and AI agents.

This is an independent learning project. It is **not** the publisher's source-code
repository and is not affiliated with or endorsed by the author or O'Reilly Media.

## Official code repository

The book's official companion code is an essential resource:

### [Nicolepcx/transformers-the-definitive-guide](https://github.com/Nicolepcx/transformers-the-definitive-guide)

The official repository organizes notebooks by chapter (`CH01`, `CH02`, and so
on), includes shared utilities and resources, and is intended to support
GPU-backed notebook environments. Use it to:

- access the author's reference implementations;
- compare these study implementations with the original examples;
- obtain chapter-specific notebooks, utilities, and supporting resources;
- follow corrections and future code updates; and
- report problems with the official examples through its
  [GitHub issues](https://github.com/Nicolepcx/transformers-the-definitive-guide/issues).

> **Important:** Treat the official repository as the source of truth for the
> book's supplemental code. The material here records an independent study path
> and may intentionally differ for explanation or experimentation.

## Book at a glance

| Item | Details |
| --- | --- |
| Title | *Transformers: The Definitive Guide* |
| Author | Nicole Koenigstein |
| Publisher | O'Reilly Media |
| Publication | March 2026 |
| Audience | Intermediate to advanced |
| Length | 372 pages |
| Language | English |
| ISBN | `978-1-098-16701-1` (print); `978-1-098-16700-4` (online edition) |
| Official book page | [O'Reilly](https://www.oreilly.com/library/view/transformers-the-definitive/9781098167004/) |
| Book website | [transformers-the-definitive-guide.com](https://transformers-the-definitive-guide.com/) |
| Official code | [GitHub](https://github.com/Nicolepcx/transformers-the-definitive-guide) |
| Errata and updates | [O'Reilly book resources](https://www.oreilly.com/library/view/transformers-the-definitive/9781098167004/) |

## What the book covers

The book develops a systems-oriented view of transformers from first principles
to production:

- tokenization, embeddings, positional representations, attention, encoders,
  decoders, and long-context enhancements;
- transformer applications beyond text, including time series, computer vision,
  image and video generation, and audio;
- reinforcement learning, decision transformers, and world models;
- reasoning, planning, coding models, and test-time compute;
- agent workflows, multi-agent systems, memory, and human-in-the-loop control;
- training and inference optimization, adaptive compute, and agent learning; and
- deployment concerns such as runtime behavior, KV caches, quantization,
  evaluation, security, hardware efficiency, and cost.

The recurring engineering question is not only *whether a model works*, but
whether the complete system remains reliable beyond a notebook demonstration.

## Chapter roadmap

| Chapter | Subject | Main themes |
| ---: | --- | --- |
| 1 | From First Principles to State-of-the-Art Transformers | Tokenization, embeddings, attention, encoder/decoder design, long context |
| 2 | Transformers for Time Series | Stationarity, autocorrelation, forecasting, anomaly detection, foundation models |
| 3 | Transformers for Vision Tasks | Image tokenization, classification, segmentation, vision transformers |
| 4 | Transformers for Image Generation | Diffusion transformers and scalable latent image generation |
| 5 | Transformers for Video Generation | Latent video models, temporal structure, and controlled generation |
| 6 | From Sound to Token and Back | Waveforms, spectrograms, speech, multimodal audio, and music |
| 7 | Reinforcement Learning Transformers | Decision transformers, online RL, and transformer world models |
| 8 | Planning, Reasoning, and Coding | Reinforcement learning for reasoning, coding models, and test-time compute |
| 9 | AI Agents for Complex Tasks | Workflows, multi-agent systems, memory, communication, and human oversight |
| 10 | Optimizing LLMs and AI Agents | Agent RL, adaptive compute, rewards, and training-system optimization |
| 11 | Deploying Transformer Models | Runtime engineering, evaluation, security, quantization, hardware, and cost |
| 12 | From Models to Intelligent Systems | Combining specialist models and scaling agentic systems |

The chapters are largely self-contained, but reading them in sequence gives the
strongest progression from model fundamentals to intelligent systems.

## Who this study is for

This material is most useful to:

- ML engineers designing systems for text, vision, video, audio, or time series;
- practitioners moving transformer models from notebooks into production;
- data scientists who want to understand architectural trade-offs rather than
  only call hosted APIs; and
- systems thinkers exploring reasoning, reinforcement learning, and AI agents.

## Prerequisites

The book is not an introduction to deep learning or to large language models.
Readers should already be comfortable with:

- Python and Jupyter notebooks;
- neural networks and backpropagation;
- basic linear algebra, probability, and optimization;
- standard machine-learning training and evaluation workflows; and
- the basic purpose and use of large language models.

The focus is architecture and engineering—not prompt engineering, API recipes,
exhaustive proofs, or benchmark comparisons detached from implementation.

## Study progress

| Chapter | Local material | Status |
| ---: | --- | :---: |
| 1 | [Chapter1.ipynb](./Chapter%201%20-%20From%20First%20Principles%20to%20State-of-the-Art%20Transformers/Chapter1.ipynb) | 🚧 In progress |
| 2 | `Chapter 2/` | ⏳ Planned |
| 3–12 | — | ⏳ Planned |

Chapter 1 currently explores:

- CUDA and alternative acceleration backends;
- character-, word-, and subword-level tokenization;
- token and positional embeddings;
- scaled dot-product and multi-head attention;
- bidirectional and causal attention;
- encoder and decoder architectures; and
- long-context techniques such as RoPE, positional interpolation, and YaRN.

## Repository structure

```text
Transformers - The Definitive Guide/
├── README.md
├── Chapter 1 - From First Principles to State-of-the-Art Transformers/
│   └── Chapter1.ipynb
└── Chapter 2/
```

The Chapter 1 notebook also imports `utils.utilities` from the root of the parent
`book-based-learning` repository.

## Running the local notebook

From the root of `book-based-learning`, create and activate a virtual environment,
then install the notebook's current direct dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyter matplotlib torch transformers
python -m jupyter lab
```

Open:

```text
Transformers - The Definitive Guide/
└── Chapter 1 - From First Principles to State-of-the-Art Transformers/
    └── Chapter1.ipynb
```

Notes:

- Launch Jupyter from the repository root so the shared `utils` module can be
  resolved correctly.
- Hugging Face examples download pretrained model files and therefore require an
  internet connection and sufficient disk space.
- Some examples inspect NVIDIA GPU support with `nvidia-smi`; a compatible GPU is
  useful for larger workloads but not required for every introductory cell.
- Install the PyTorch build appropriate for your CPU/GPU platform by following
  the [official PyTorch installation selector](https://pytorch.org/get-started/locally/).
- The book's official notebooks may have their own per-chapter requirements and
  stronger GPU needs. Follow the instructions in the official GitHub repository
  when running those notebooks.

## Recommended references

- [Official companion repository](https://github.com/Nicolepcx/transformers-the-definitive-guide)
- [Official book page and table of contents](https://www.oreilly.com/library/view/transformers-the-definitive/9781098167004/)
- [Book website and supplementary resources](https://transformers-the-definitive-guide.com/)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/)
- [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html)
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- [Linear Algebra Done Right](https://linear.axler.net/) by Sheldon Axler

## Guiding principle

> “Any sufficiently advanced technology is indistinguishable from magic.”
> — Arthur C. Clarke

The goal of this study is to turn the apparent magic of attention into something
understandable, testable, and reliable enough to engineer.

## Copyright and use

The book and its published content are copyright Nicole Koenigstein and O'Reilly
Media. The official companion repository has its own
[Apache 2.0 license](https://github.com/Nicolepcx/transformers-the-definitive-guide/blob/master/LICENSE);
consult that license and the book's usage terms before redistributing official
examples.

This repository contains independent study material. It does not include or
replace the book. Purchase or access the book through
[O'Reilly](https://www.oreilly.com/library/view/transformers-the-definitive/9781098167004/)
to follow the complete text.

For technical support concerning O'Reilly's examples, contact
[`support@oreilly.com`](mailto:support@oreilly.com). For permissions beyond the
book's stated code-example terms, contact
[`permissions@oreilly.com`](mailto:permissions@oreilly.com).
