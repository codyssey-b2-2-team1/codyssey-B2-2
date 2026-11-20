"""마감일 관련 함수 모음."""

import re
import sys
from datetime import date, datetime


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
    ValueError: 잘못된 날짜 입력입니다.
    >>> days_until("2026/11/25", "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다.
    >>> days_until("2026-1-5", "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다.
    >>> days_until("2026-11-25", "2026-13-01")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다.
    >>> days_until(None, "2026-11-20")
    Traceback (most recent call last):
        ...
    ValueError: 잘못된 날짜 입력입니다.
    """
    if not isinstance(due_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", due_date):
        raise ValueError("잘못된 날짜 입력입니다.")
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("잘못된 날짜 입력입니다.")

    if not isinstance(base_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", base_date):
        raise ValueError("잘못된 날짜 입력입니다.")
    try:
        base = datetime.strptime(base_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("잘못된 날짜 입력입니다.")

    return (due - base).days
