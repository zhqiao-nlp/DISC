# DISC: A plug-and-play decoding intervention with similarity of characters for Chinese Spelling Check.

[![Paper](https://img.shields.io/badge/Paper-arXiv-red)](https://arxiv.org/abs/2412.12863v2)
[![License: Apache](https://img.shields.io/badge/License-Apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Abstract

One key characteristic of the Chinese spelling check (CSC) task is that incorrect characters are usually similar to the correct ones in either phonetics or glyph. To accommodate this, previous works usually leverage confusion sets, which suffer from two problems, i.e., difficulty in determining which character pairs to include and lack of probabilities to distinguish items in the set. In this paper, we propose a light-weight plug-and-play DISC (i.e., decoding intervention with similarity of characters) module for CSC models. DISC measures phonetic and glyph similarities between characters and incorporates this similarity information only during the inference phase. This method can be easily integrated into various existing CSC models, such as ReaLiSe, SCOPE, and ReLM, without additional training costs. Experiments on three CSC benchmarks demonstrate that our proposed method significantly improves model performance, approaching and even surpassing the current state-of-the-art models.

## Run

You can simply get phonetic and glyph similarities by running:
```bash
cd char-similarity-calculation
python merge.py
```

## Citation

If you find this work useful, please cite our paper:

```bibtex
@misc{qiao2025discplugandplaydecodingintervention,
      title={DISC: Plug-and-Play Decoding Intervention with Similarity of Characters for Chinese Spelling Check}, 
      author={Ziheng Qiao and Houquan Zhou and Yumeng Liu and Zhenghua Li and Min Zhang and Bo Zhang and Chen Li and Ji Zhang and Fei Huang},
      year={2025},
      eprint={2412.12863},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.12863}, 
}
```
