# pokemonbattle_autotests_2026
Тренировочный проект

## Test launch rules

- Run tests via `pytest` only (do not use `Run Python File` for test modules).
- In IDE use `Testing` panel or `Run Test` / `Run All Tests`.

## Console commands

- Run all tests:
  - `./venv/bin/pytest -s tests -v`
- One specific test:
  - `./venv/bin/pytest -s tests/api/test_me_smoke.py::test_get_me_smoke -v`
