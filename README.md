<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=Markdown%20Table%20Aligner&fontColor=ffffff&fontSize=34" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=Markdown%20Table%20Aligner;Clean%20up%20pipe%20tables" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/markdown-table-aligner?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/markdown-table-aligner)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/markdown-table-aligner?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/markdown-table-aligner)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Make GitHub-flavored Markdown pipe tables easier to read with aligned columns.**

</div>

## ✨ Overview

A local formatter for simple Markdown pipe tables. It preserves ordinary text and only writes files when explicitly asked.

## 🚀 Features

- 📐 Aligns header and body cells to consistent widths.
- ↔️ Preserves left, center, and right separator markers.
- 🧾 Leaves non-table Markdown lines unchanged.
- 🛡️ Prints to stdout by default; in-place editing is opt-in.

## 🧪 Demo

```text
| A | Longer |
| --- | --- |
| x | y |
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/markdown-table-aligner.git
cd markdown-table-aligner
python main.py README.md
```

## 🧰 Tech Stack

Python 3.10+ · Standard library only.

## 🗂️ Folder Structure

```text
markdown-table-aligner/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Simple pipe-table formatting
- [x] Unit tests and CI
- [ ] Escaped-pipe parsing
- [ ] Preserve Markdown alignment with custom padding

## 🤝 Contributing

Report a minimal Markdown example for any formatting issue. Add a regression test before changing parsing behavior.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>
