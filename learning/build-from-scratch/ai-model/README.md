---
id: build-from-scratch.ai-model
title: "Build a Tiny AI Model"
content_type: project
locale: en
domain: ai-and-data-science
level: intermediate
status: draft
learning_objectives:
  - "Explain features, labels, and supervised learning."
  - "Create reproducible training, validation, and test splits."
  - "Compare classification metrics and their limitations."
  - "Document dataset provenance and model limitations."
prerequisites:
  - "Python functions and collections"
  - "Basic algebra"
  - "Familiarity with tables and graphs"
milestones:
  - "Inspect a public teaching dataset."
  - "Create reproducible data splits."
  - "Train a baseline and record metrics."
  - "Compare one changed feature or hyperparameter."
  - "Write a model card."
---

# Build a Tiny AI Model

**Level:** Intermediate · **Language:** Python · **Track:** `ai-model`

## Goal
Build a small supervised-learning classifier on a public teaching dataset. This track teaches the learning process; it is not a recipe for a production LLM.

## Prerequisites
Python functions and collections; basic algebra; familiarity with tables and graphs.

## Lesson 1 — Data, features, and labels
A supervised dataset contains examples. **Features** are the input information; a **label** is the target answer. A model maps features to a prediction. For a simple linear model:

`prediction = weight × feature + bias`

Training adjusts parameters to reduce a loss function on training examples. The loss measures model error according to a chosen objective; it is not a universal measure of model quality.

**Check:** In a house-price dataset, name two possible features and one label. Why might a row ID be a misleading feature?

## Lesson 2 — The training workflow
1. Inspect and clean the dataset.
2. Split it into training, validation, and test sets.
3. Choose a simple baseline.
4. Calculate predictions and loss.
5. Update parameters with an optimisation method.
6. Compare training and validation performance.
7. Evaluate once on held-out test data.

If training performance improves while validation performance worsens, the model may be overfitting. Reusing test data to tune a model causes data leakage and makes the final evaluation less trustworthy.

## Lesson 3 — Evaluation
For classification, accuracy is the fraction of correct predictions. With imbalanced classes, accuracy can hide poor performance on a minority class. Inspect a confusion matrix and, when appropriate, per-class precision and recall.

Document the dataset source, licence, intended use, limitations, and any sensitive attributes. Do not upload private or identifying data to a tutorial project.

## Build milestones
- **M1:** Load a small public dataset; print its shape, features, and label distribution.
- **M2:** Make a reproducible train/validation/test split.
- **M3:** Train a baseline and record metrics.
- **M4:** Change one feature or hyperparameter and compare validation results.
- **M5:** Write a short model card describing intended use and limitations.

## Exercises
1. Explain parameter versus hyperparameter.
2. Give an example of data leakage.
3. Why can accuracy mislead on imbalanced data?
4. Give one reason test performance may differ from real-world performance.

## Acceptance criteria
- The experiment is reproducible with a fixed random seed.
- Training and test sets remain separate.
- At least one baseline metric is reported.
- Dataset provenance and model limitations are documented.

## Further study
- [LLMs from Scratch](https://github.com/rasbt/LLMs-from-scratch)
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course/en/unit1/3)
- [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvK)

These are external resources, not UKE-authored lessons.
