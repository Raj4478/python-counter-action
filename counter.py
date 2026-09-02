from pathlib import Path


COUNTER_FILE = Path(__file__).with_name("counter.txt")


def read_counter() -> int:
    try:
        return int(COUNTER_FILE.read_text(encoding="utf-8").strip())
    except FileNotFoundError:
        return 0
    except ValueError as exc:
        raise ValueError(f"{COUNTER_FILE} must contain a valid integer") from exc


def main() -> None:
    next_value = read_counter() + 1
    COUNTER_FILE.write_text(f"{next_value}\n", encoding="utf-8")
    print(f"Counter updated to {next_value}")


if __name__ == "__main__":
    main()
