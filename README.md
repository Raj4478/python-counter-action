# Python Counter Action

A small Python automation that increments `counter.txt` and commits the result twice each day with GitHub Actions.

## Schedule

The workflow runs at:

- 09:00 IST (`03:30 UTC`)
- 21:00 IST (`15:30 UTC`)

GitHub Actions scheduled workflows can start a few minutes later during periods of high load. You can also run the workflow manually from the repository's **Actions** tab.

## Run locally

```bash
python counter.py
```

## Test

```bash
python -m unittest -v
```
