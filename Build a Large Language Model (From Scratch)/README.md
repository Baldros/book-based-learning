# Build a Large Language Model (From Scratch)

> Study notes and implementations inspired by
> *Build a Large Language Model (From Scratch)* by Sebastian Raschka (Manning, 2024).

[![Book](https://img.shields.io/badge/Manning-Book-8A2BE2)](https://www.manning.com/books/build-a-large-language-model-from-scratch)
[![Official code](https://img.shields.io/badge/GitHub-Official_Code-181717?logo=github)](https://github.com/rasbt/LLMs-from-scratch)
[![Framework](https://img.shields.io/badge/PyTorch-From_Scratch-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![Status](https://img.shields.io/badge/Status-In_Progress-yellow)](#study-progress)

## About this repository

This directory documents a hands-on study of how GPT-style large language models
work internally. It contains personal notes, mathematical explanations, and
PyTorch implementations that follow the book's bottom-up path:

```text
raw text → tokens → embeddings → attention → GPT model
         → pretraining → classification fine-tuning → instruction fine-tuning
```

The goal is not to reproduce a frontier-scale model. It is to build a smaller,
functional version from first principles so that every major component can be
inspected, tested, modified, and understood.

This is an independent learning project. It is **not** the author's official
source-code repository and is not affiliated with or endorsed by Sebastian
Raschka or Manning Publications.

## Official code repository

The book's official companion repository is the most important external resource
for this study:

### [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)

It contains the latest reference implementations for developing, pretraining, and
fine-tuning a GPT-like LLM. The repository includes:

- complete notebooks and compact Python implementations for Chapters 2–7;
- exercise solutions and supplementary notebooks for every implementation stage;
- appendices covering PyTorch, training improvements, and LoRA;
- environment setup instructions and a detailed troubleshooting guide;
- bonus implementations of tokenizers, attention variants, KV caching, and
  architecture comparisons;
- pretrained-weight loading and evaluation utilities; and
- ongoing corrections and updates beyond the printed book.

Useful direct links:

- [Official repository](https://github.com/rasbt/LLMs-from-scratch)
- [Setup recommendations](https://github.com/rasbt/LLMs-from-scratch/tree/main/setup)
- [Troubleshooting guide](https://github.com/rasbt/LLMs-from-scratch/blob/main/troubleshooting.md)
- [Issues](https://github.com/rasbt/LLMs-from-scratch/issues)
- [Discussions](https://github.com/rasbt/LLMs-from-scratch/discussions)

> **Important:** Use the official GitHub repository as the source of truth for
> the book's code and latest corrections. The notebooks here represent an
> independent study path and may add explanations or experiments.

## Book at a glance

| Item | Details |
| --- | --- |
| Title | *Build a Large Language Model (From Scratch)* |
| Author | Sebastian Raschka, PhD |
| Publisher | Manning Publications |
| Publication | September 2024 |
| Length | 368 pages |
| ISBN | `978-1-63343-716-6` |
| Main framework | Python and PyTorch |
| Book page | [Manning](https://www.manning.com/books/build-a-large-language-model-from-scratch) |
| Author's companion hub | [sebastianraschka.com/llms-from-scratch](https://sebastianraschka.com/llms-from-scratch/) |
| Official code | [GitHub](https://github.com/rasbt/LLMs-from-scratch) |
| Discussion forum | [Manning liveBook](https://livebook.manning.com/book/build-a-large-language-model-from-scratch/discussion) |

## Why build an LLM from scratch?

Calling an API can show what an LLM does; implementing one reveals why it works.
Building the model component by component develops the practical intuition needed
to:

- debug tensor shapes, masks, data pipelines, and training behavior;
- understand what is learned during pretraining and fine-tuning;
- estimate parameter counts, memory needs, and computational costs;
- compare architectural choices without treating the model as a black box;
- load and adapt pretrained weights confidently; and
- experiment with new ideas on top of a known, testable baseline.

The models in the book are intentionally educational and smaller than commercial
foundation models, but they use the same core concepts.

## What you will build

By following the complete path, you will implement:

- a text-processing and byte pair encoding pipeline;
- sliding-window input/target datasets and data loaders;
- token and positional embedding layers;
- self-attention with learned query, key, and value projections;
- causal masks, dropout, and multi-head attention;
- layer normalization, GELU feed-forward networks, and shortcut connections;
- reusable transformer blocks and a GPT-style model;
- autoregressive text generation with temperature and top-k sampling;
- a pretraining loop with training and validation losses;
- checkpoint saving, loading, and GPT-2 weight import;
- a classification fine-tuning pipeline; and
- a supervised instruction fine-tuning and evaluation pipeline.

## Chapter roadmap

The book is designed to be read sequentially because each chapter depends on the
implementation created in the preceding chapters.

| Chapter | Subject | Main outcomes |
| ---: | --- | --- |
| 1 | Understanding large language models | LLM concepts, transformers, GPT architecture, and the development lifecycle |
| 2 | Working with text data | Tokenization, BPE, sliding-window sampling, token embeddings, and positional embeddings |
| 3 | Coding attention mechanisms | Self-attention, trainable projections, causal masking, dropout, and multi-head attention |
| 4 | Implementing a GPT model from scratch | Layer normalization, GELU, feed-forward layers, residual paths, transformer blocks, and generation |
| 5 | Pretraining on unlabeled data | Loss calculation, training, decoding strategies, checkpoints, and GPT-2 weights |
| 6 | Fine-tuning for classification | Dataset preparation, classification heads, supervised training, and spam detection |
| 7 | Fine-tuning to follow instructions | Instruction datasets, batching, supervised fine-tuning, response extraction, and evaluation |

## Appendices

| Appendix | Subject |
| :---: | --- |
| A | PyTorch fundamentals, tensors, autograd, neural networks, data loaders, training loops, and GPU training |
| B | References and further reading |
| C | Exercise solutions |
| D | Learning-rate warmup, cosine decay, gradient clipping, and an improved training loop |
| E | Parameter-efficient fine-tuning with LoRA |

## Who this study is for

This material is useful to:

- students and developers who want to understand LLMs below the API layer;
- ML engineers who need confidence debugging or adapting transformer models;
- researchers looking for a compact, inspectable GPT implementation;
- practitioners moving from general Python into deep learning; and
- experienced developers who want to rebuild the complete LLM pipeline as a
  coherent project.

## Prerequisites

The essential prerequisite is a solid foundation in Python. Helpful—but not
strictly required—background includes:

- basic machine-learning and deep-learning concepts;
- vectors, matrices, matrix multiplication, and elementary probability;
- familiarity with tensors and neural networks; and
- basic command-line and Jupyter notebook usage.

Prior PyTorch expertise is not required. Appendix A introduces the parts of
PyTorch needed throughout the book.

## Study progress

| Chapter | Local material | Status |
| ---: | --- | :---: |
| 1 | Conceptual introduction; no local notebook | 📖 Reference chapter |
| 2 | [Working with text data](./Chapter%202/Chapter%202%20-%20Working%20with%20text%20data.ipynb) | ✅ Notes implemented |
| 3 | [Coding attention mechanisms](./Chapter%203/Chapter%203%20-%20Coding%20attention%20mechanisms.ipynb) | 🚧 In progress |
| 4–7 | — | ⏳ Planned |
| A–E | — | ⏳ Planned |

### Current Chapter 2 coverage

The local Chapter 2 notebook includes:

- text acquisition and preprocessing;
- regular-expression tokenization;
- token-to-ID and ID-to-token conversion;
- unknown and end-of-text context tokens;
- byte pair encoding with `tiktoken`;
- sliding-window dataset sampling;
- PyTorch `Dataset` and `DataLoader` construction;
- token embeddings; and
- positional embeddings.

The accompanying sample text is stored at
[`Chapter 2/data/the-verdict.txt`](./Chapter%202/data/the-verdict.txt).

### Current Chapter 3 coverage

The local Chapter 3 notebook includes:

- the limitations of earlier long-sequence modeling approaches;
- dot products and attention-score intuition;
- self-attention without trainable weights;
- learned query, key, and value projections;
- scaled dot-product attention;
- compact PyTorch self-attention modules;
- causal attention masks; and
- the path toward multi-head attention.

## Repository structure

```text
Build a Large Language Model (From Scratch)/
├── README.md
├── Chapter 2/
│   ├── Chapter 2 - Working with text data.ipynb
│   └── data/
│       └── the-verdict.txt
└── Chapter 3/
    └── Chapter 3 - Coding attention mechanisms.ipynb
```

The notebooks import `utils.utilities` from the root of the parent
`book-based-learning` repository.

## Running the local notebooks

From the root of `book-based-learning`, create a virtual environment and install
the current direct dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyter matplotlib requests tiktoken torch
python -m jupyter lab
```

Then open either notebook under `Build a Large Language Model (From Scratch)`.

Notes:

- Launch Jupyter from the repository root so the shared `utils` module resolves.
- The local Chapter 2 notebook may download text or other supporting resources,
  so some cells require an internet connection.
- The included text file allows the main tokenization and data-loader exercises
  to be repeated locally.
- Select the PyTorch installation appropriate for your platform using the
  [official PyTorch installer](https://pytorch.org/get-started/locally/).
- Keep model and dataset sizes modest when using CPU-only hardware.

## Hardware expectations

The main educational implementations are designed to run on a conventional
laptop. A GPU is optional for the early chapters and small experiments, although
it can substantially accelerate pretraining and fine-tuning.

The book demonstrates architecture and training mechanics; it does not claim that
a laptop can reproduce the scale, dataset, or compute budget of frontier LLMs.

## Suggested study workflow

1. Read the chapter once for the conceptual map.
2. Reimplement or run the local notebook cell by cell.
3. Change dimensions, inputs, or hyperparameters and predict the outcome.
4. Complete the chapter exercises before reading the solutions.
5. Compare the result with the
   [official chapter implementation](https://github.com/rasbt/LLMs-from-scratch).
6. Record mistakes, tensor shapes, and design decisions as part of the notes.

This approach follows the author's recommended read → watch → code → exercise
cycle while keeping the implementation work central.

## Official learning resources

- [Book companion hub](https://sebastianraschka.com/llms-from-scratch/) — chapter
  map, study guide, course links, concept guides, and next steps
- [Official GitHub repository](https://github.com/rasbt/LLMs-from-scratch) —
  current code, exercise solutions, setup, and bonus materials
- [Manning book page](https://www.manning.com/books/build-a-large-language-model-from-scratch) —
  book access, errata, source bundle, and publisher resources
- [Free YouTube course](https://www.youtube.com/playlist?list=PLTKMiZHVd_2IIEsoJrWACkIxLRdfMlw11) —
  chapter-aligned implementation videos
- [Free “Test Yourself” companion](https://www.manning.com/books/test-yourself-on-sebastian-raschkas-build-a-large-language-model-from-scratch) —
  300+ practice problems and answers
- [liveBook discussion forum](https://livebook.manning.com/book/build-a-large-language-model-from-scratch/discussion) —
  questions and section-specific discussion
- [Author's AI research blog](https://magazine.sebastianraschka.com/) — current
  LLM research, architecture, and implementation articles
- [Author's free courses](https://sebastianraschka.com/teaching/) — supporting
  machine-learning, deep-learning, and PyTorch material

## Particularly useful official bonus material

After completing the relevant core chapter, the official repository offers
supplementary material on:

- implementing BPE from scratch and comparing tokenizer implementations;
- embedding layers versus linear layers;
- efficient multi-head attention implementations;
- PyTorch buffers and causal masks;
- KV caching for faster autoregressive generation;
- LoRA and other parameter-efficient adaptation methods;
- modern architecture variants and model-family comparisons; and
- evaluation, instruction fine-tuning, and training refinements.

These supplements are valuable extensions, but the seven-chapter sequence remains
the clearest path through the fundamentals.

## Where to go next

After completing the book:

1. Extend the baseline GPT implementation with modern components such as RoPE,
   RMSNorm, SwiGLU, grouped-query attention, and KV caching.
2. Compare the implementation against current open-weight architectures.
3. Work through the author's
   [Build a Reasoning Model (From Scratch)](https://sebastianraschka.com/reasoning-from-scratch/)
   material for inference-time scaling, reinforcement learning, and distillation.
4. Build a small end-to-end project with explicit evaluation, reproducible
   checkpoints, and documented limitations.

## About the author

[Sebastian Raschka](https://sebastianraschka.com/) is a machine-learning and AI
researcher, engineer, educator, open-source contributor, and author. His work
spans academic deep-learning research, industry LLM engineering, and practical
technical education.

## Copyright and use

The book and its published content are copyright Sebastian Raschka and Manning
Publications. The official companion repository's software is distributed under
the [Apache License 2.0](https://github.com/rasbt/LLMs-from-scratch/blob/main/LICENSE.txt);
the license explicitly excludes book-specific content and related images from its
definition of licensed source. Consult the license and publisher terms before
redistributing material.

This repository contains independent study material. It does not include or
replace the book. Purchase or access the complete book through
[Manning](https://www.manning.com/books/build-a-large-language-model-from-scratch).
