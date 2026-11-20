# CPE two-star index

This repository contains 306 source files: 304 Python solutions and 2 C++
solutions. Most files are standalone UVa/CPE-style submissions.

## Naming conventions

| Pattern | Meaning |
|---|---|
| `2-N.py` | CPE two-star practice index |
| numeric filename | UVa-style problem identifier |
| `fast`, `good`, `plus` | alternate or improved implementation |
| `slow`, `other` | comparison implementation |
| `wrong` | incorrect or experimental version kept for study |

## Review workflow

For each problem, compare alternate versions only after understanding the
baseline solution. Test multiple cases, especially EOF/blank-line handling,
multiple test cases, and numeric boundaries. Record the algorithm and
complexity in personal notes or the original problem statement.

Example:

```bash
python3 2-1.py < input.txt
python3 10360.py < input.txt
```

The solutions intentionally remain flat and standalone for online-judge use.
