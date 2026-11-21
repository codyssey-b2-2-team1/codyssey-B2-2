"""공부 시간(분)을 "N시간 M분" 형식의 문자열로 바꾸는 함수."""


def format_study_time(minutes):
    """공부한 시간(분)을 "N시간 M분" 형식의 문자열로 바꾼다.

    Args:
        minutes: 0 이상의 정수(분).

    Returns:
        "N시간 M분" 형식의 문자열. 0분이면 "0시간 0분".

    Raises:
        ValueError: 음수이거나 정수가 아닌 값(실수, 문자열, None, True/False 등)일 때.

    사용 예시:
        >>> format_study_time(95)
        '1시간 35분'
        >>> format_study_time(0)
        '0시간 0분'
        >>> format_study_time(59)
        '0시간 59분'
        >>> format_study_time(120)
        '2시간 0분'
        >>> format_study_time(1500)
        '25시간 0분'
        >>> format_study_time(-1)
        Traceback (most recent call last):
        ...
        ValueError: minutes는 0 이상이어야 합니다: -1
        >>> format_study_time(90.5)
        Traceback (most recent call last):
        ...
        ValueError: minutes는 정수여야 합니다: 90.5
    """
    # bool은 int의 하위 타입이라 True가 1로 계산되므로 따로 막는다.
    if isinstance(minutes, bool) or not isinstance(minutes, int):
        raise ValueError(f"minutes는 정수여야 합니다: {minutes!r}")
    if minutes < 0:
        raise ValueError(f"minutes는 0 이상이어야 합니다: {minutes}")

    hours, remaining = divmod(minutes, 60)
    return f"{hours}시간 {remaining}분"


if __name__ == "__main__":
    # 직접 실행하면 docstring의 사용 예시(doctest)를 테스트한다.
    import doctest

    doctest.testmod(verbose=True)
