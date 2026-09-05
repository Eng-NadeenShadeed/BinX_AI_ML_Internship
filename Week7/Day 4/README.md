# Week 7 · Day 4 — Attention & Transformers

## Overview
I studied the Transformer architecture from first principles — attention
mechanism, self-attention with Q/K/V matrices, multi-head attention, and
positional encoding — then applied a pretrained DistilBERT model to medical
text classification. I trained a BiLSTM baseline on the same dataset for a
fair architectural comparison, confirming that pretrained language models
outperform sequence models trained from scratch when task-specific data is limited.
A key finding before training was the discovery and correction of data leakage
between the original train and test splits.

## Files
```
Day 4/
├── day4_attention_transformers.ipynb ← Theory notebook
├── Hands_On_Lab.ipynb ← Medical abstracts classification
├── README.md
```


## Topics Covered — Learning Notebook
- RNN/LSTM limitations: sequential processing, memory bottleneck, no parallelism
- Attention mechanism: scores, softmax, weighted sum
- Self-attention: Q, K, V matrices — full worked example with code
- Multi-head attention: parallel heads, different relationship types
- Transformer parallelism vs RNN sequential dependency chain
- Sinusoidal positional encoding — visualization across 50 positions
- Transformer families: BERT (encoder), GPT (decoder), T5 (encoder-decoder)
- Transfer learning for text — same principle as CNN transfer learning (Day 2)

## Dataset — Medical Abstracts
5-class disease classification from medical paper abstracts

| Class | Disease Category | Train | Test |
|-------|-----------------|-------|------|
| 1 | Neoplasms | ~2,023 | ~660 |
| 2 | Digestive system diseases | ~956 | ~299 |
| 3 | Nervous system diseases | ~1,232 | ~385 |
| 4 | Cardiovascular diseases | ~1,953 | ~610 |
| 5 | General pathological conditions | ~3,075 | ~961 |

> Counts reflect clean splits after removing data leakage (988 overlapping abstracts)

## Hands-On Lab — Key Steps

### Data Quality Findings
| Issue | Count | Action |
|-------|-------|--------|
| Duplicate abstracts | 2,105 | Identified and analyzed |
| Conflicting labels | 1,956 | Resolved by majority vote |
| Train/test leakage | 988 | Removed — rebuilt clean splits |

### Results

| Model | Test Accuracy | Macro F1 | Pretrained |
|-------|--------------|----------|------------|
| BiLSTM (from scratch) | 71.49% | 0.604 | No |
| **DistilBERT (fine-tuned)** | **83.61%** | **0.831** | Yes — Wikipedia + BookCorpus |

### Per-Class F1 Comparison

| Class | BiLSTM | DistilBERT | Gap |
|-------|--------|------------|-----|
| Neoplasms | 0.867 | 0.906 | +0.039 |
| Digestive diseases | **0.104** | **0.814** | **+0.710** |
| Nervous system | 0.539 | 0.779 | +0.240 |
| Cardiovascular | 0.834 | 0.902 | +0.068 |
| General pathological | 0.674 | 0.752 | +0.078 |

### Key Findings
- Data leakage discovered and fixed before any model training
- DistilBERT outperformed BiLSTM by +12.12% accuracy and +0.227 macro F1
- Biggest gap: Digestive diseases (BiLSTM: 0.104 vs DistilBERT: 0.814)
- Pretrained weights matter most when task-specific training data is small
- Gradio demo built for interactive medical abstract classification
- Architecture decision confirmed: Dense Network for cardiac tabular data —
  Transformers require sequential or text structure that tabular data lacks

## Connection to Project
Class 4 (Cardiovascular diseases) covers the same medical domain as the
cardiac monitoring project — demonstrating how a Transformer approaches
cardiovascular risk from a text perspective vs the tabular approach in Sprint 2.

## Next
**Day 5 — Sprint 2 Close-Out:**
Core model training on 70K cardiovascular dataset, experiment logging,
Sprint Review, and Retrospective.
