---
name: ai-for-beginners
title: AI for Beginners (Microsoft)
url: "https://github.com/microsoft/AI-For-Beginners"
category: reference
summary: "Microsoft's free 12-week, 24-lesson AI curriculum covering symbolic AI (GOFAI), neural networks and deep learning in PyTorch and TensorFlow, computer vision (CNNs, autoencoders, GANs, detection, segmentation), NLP (embeddings, RNNs, Transformers/BERT, NER, LLMs), genetic algorithms, deep RL, multi-agent systems, and AI ethics; lessons ship as executable Jupyter notebooks with quizzes and labs, in 50+ language translations"
tags: [ai, learning, curriculum, deep-learning, pytorch, tensorflow, computer-vision, nlp]
reviewed: 2026-08-09
acquired: 2026-08-09
license: MIT
security_flags: []
overlaps: [data-science-for-beginners, huggingface-llm-course, huggingface-agents-course]
source: unknown
---

## What it does

A free, self-paced introductory AI curriculum published by Microsoft (Azure Cloud Advocates; primary author Dmitry Soshnikov, PhD). Structured as 12 weeks / 24 lessons plus extras, it covers:

- **Introduction & Symbolic AI**: history of AI, knowledge representation, expert systems, ontologies, concept graphs (GOFAI).
- **Neural networks**: perceptron, multi-layer perceptron built from scratch, framework intro (PyTorch/TensorFlow/Keras), overfitting.
- **Computer vision**: OpenCV, CNNs and CNN architectures, transfer learning, autoencoders/VAEs, GANs and style transfer, object detection, semantic segmentation (U-Net).
- **NLP**: text representation (BoW/TF-IDF), word embeddings (Word2Vec/GloVe), language modeling, RNNs, generative RNNs, Transformers/BERT, named entity recognition, large language models and prompt programming.
- **Other techniques**: genetic algorithms, deep reinforcement learning, multi-agent systems.
- **Ethics**: AI ethics and responsible AI. Extras cover multi-modal networks (CLIP, VQGAN).

Explicitly out of scope (deferred to sibling curricula): classic ML, Cognitive Services applications, specific cloud ML frameworks, conversational AI/chatbots, and the deep mathematics of deep learning.

## Structure / contents

Each lesson includes pre-reading material, executable Jupyter notebooks (usually available in both PyTorch and TensorFlow variants, containing the theory), quizzes (pre/post, in a deployable quiz app under `etc/quiz-app`), and labs for some topics. Beginner-friendly standalone examples ("Hello AI World", simple neural network, image classifier, text sentiment) sit outside the main curriculum.

## Mechanical details

- Runs in VS Code or GitHub Codespaces; fork-and-clone workflow.
- Repository bundles 50+ language translations, which inflate clone size; a documented sparse-checkout (`git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'`) fetches only the course content.
- ~55.7k GitHub stars / ~11.2k forks as of August 2026.
- Part of Microsoft's "for beginners" series alongside ML-For-Beginners, data-science-for-beginners, and generative-ai-for-beginners.

## Security

MIT-licensed repository (code); curriculum content is typically Creative Commons in Microsoft's "for beginners" series — verify the `LICENSE`/content terms before republishing. Educational content only; running the notebooks pulls the standard Python DL stack (PyTorch/TensorFlow/Keras) as dependencies. No installable package or agent component.