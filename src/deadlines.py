"""마감일 관련 함수 모음."""

import re
from datetime import datetime


def _parse_date(value):
    """``YYYY-MM-DD`` 형식의 문자열을 ``date``로 변환한다.

    잘못된 입력이면 입력값을 포함한 메시지로 ``ValueError``를 발생시킨다.
    """
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError(f"잘못된 날짜 입력입니다: {value!r}")
    return datetime.strptime(value, "%Y-%m-%d").date()

    # try:
    #     return datetime.strptime(value, "%Y-%m-%d").date()
    # except ValueError:
    #     raise ValueError(f"잘못된 날짜 입력입니다: {value!r}") from None


def days_until(due_date, base_date):
    """마감일까지 남은 날짜 수를 반환한다.

    두 인자는 ``YYYY-MM-DD`` 형식의 문자열이어야 한다.
    마감일 당일은 0, 마감일이 지났으면 음수를 반환한다.

    잘못된 입력(문자열이 아닌 값, 형식 오류, 존재하지 않는 날짜)은
    ``ValueError``를 발생시킨다.

    >>> days_until("2026-11-25", "2026-11-20")
    5
    >>> days_until("2026-11-20", "2026-11-20")
    0
    >>> days_until("2026-11-19", "2026-11-20")
    -1
    >>> days_until("2026-12-31", "2026-11-20")
    41
    >>> days_until("2026-02-30", "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다: '2026-02-30'
    >>> days_until("2026/11/25", "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다: '2026/11/25'
    >>> days_until("2026-1-5", "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다: '2026-1-5'
    >>> days_until("2026-11-25", "2026-13-01")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다: '2026-13-01'
    >>> days_until(None, "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다: None
    """
    due = _parse_date(due_date)
    base = _parse_date(base_date)
    return (due - base).days
