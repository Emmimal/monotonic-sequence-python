# monotonic-sequence-python
7 efficient ways to check if a list/array is monotonic in Python (non-strict &amp; strict). Includes edge cases, performance comparison, floating-point handling, interview tips for LeetCode 896, and real-world examples. O(n) solutions + NumPy/pairwise variants.

# Monotonic Sequence Check in Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**7 efficient methods** to check if a list/array is **monotonic** (non-decreasing or non-increasing) in Python — including edge cases, floating-point safety, performance analysis, and interview tips for **LeetCode 896 (Monotonic Array)**.

Perfect for:
- Data validation pipelines
- Time-series analysis
- Machine learning loss monitoring
- Technical interview preparation

→ Original in-depth article: https://emitechlogic.com/monotonic-sequence-in-python/

## Features

- All methods are **O(n)** time (except naive sorted version)
- Handles **strict** vs **non-strict** monotonicity
- Floating-point tolerance with `math.isclose`
- Early exit optimizations
- NumPy vectorized version for large arrays
- `itertools.pairwise` (Python 3.10+) — clean & zero-copy

## Quick Start

```bash
git clone https://github.com/Emmimal/monotonic-sequence-python.git
cd python-monotonic-check
pip install -r requirements.txt          # only if using NumPy
python -m pytest tests/                   # run tests
