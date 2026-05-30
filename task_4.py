import re
from datetime import datetime

from core.enums import (
    HIDDEN_EMAIL,
    HIDDEN_PHONE,
    INITIAL_TEST_TXT_DOC_PATH,
    TEST_TXT_DOC_PATH,
)

DATE_FORMATS = [
    "%d/%m/%Y %H:%M",
    "%d.%m.%Y %H:%M",
    "%Y-%m-%d %H:%M",
]


def normalize_date(date_value: str) -> str:
    for date_format in DATE_FORMATS:
        try:
            parsed_date = datetime.strptime(date_value, date_format)
            return parsed_date.strftime("%d.%m.%Y %H:%M")
        except ValueError:
            continue

    return date_value


def replace_date(match: re.Match) -> str:
    raw_date = match.group(1)
    normalized_date = normalize_date(raw_date)

    return f"[{normalized_date}]"


def anonymize_text(text: str) -> str:
    text = re.sub(
        r"\[([^\]]+)\]",
        replace_date,
        text,
    )

    text = re.sub(
        r"[\w.\-+]+@[\w.\-]+\.\w+",
        HIDDEN_EMAIL,
        text,
    )

    text = re.sub(
        r"\+7\s*\(\d{3}\)\s*\d{3}-\d{2}-\d{2}|\+7\d{10}|8\d{10}",
        HIDDEN_PHONE,
        text,
    )

    return text


def main() -> None:
    text = INITIAL_TEST_TXT_DOC_PATH.read_text(encoding="utf-8")
    anonymized_text = anonymize_text(text)
    TEST_TXT_DOC_PATH.write_text(anonymized_text, encoding="utf-8")


if __name__ == "__main__":
    main()
