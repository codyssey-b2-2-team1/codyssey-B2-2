"""점수 목록의 평균을 계산하는 학습 도우미 함수."""

from decimal import Decimal, ROUND_HALF_UP


def calculate_average(scores: list[int | float]) -> float:
    """0~100점 목록의 평균을 소수 둘째 자리까지 반올림해 반환한다.

    scores는 비어 있지 않은 list여야 한다. 각 점수는 bool을 제외한
    int 또는 float이며, 0 이상 100 이하여야 한다.
    잘못된 자료형, 빈 목록, 범위 밖 점수는 모두 ValueError로 처리한다.
    각 점수를 Decimal(str(score))로 변환해 십진수 기준으로 평균을 구한다.
    점수 자체는 반올림하지 않고, 최종 평균의 소수 셋째 자리에서
    5 이상이면 올리는 ROUND_HALF_UP 방식으로 반올림한다.
    결과는 기존 사용 방식에 맞춰 float로 반환한다.

    사용 예시:
        일반 평균과 소수점 반올림:
        >>> calculate_average([80, 90, 100])
        90.0
        >>> calculate_average([88, 91, 95])
        91.33

        십진수 기준 반올림과 중간값 처리:
        >>> calculate_average([2.675])
        2.68
        >>> calculate_average([2.665])
        2.67
        >>> calculate_average([2.67, 2.68])
        2.68

        0점과 100점 경계값:
        >>> calculate_average([0, 100])
        50.0

        빈 목록:
        >>> calculate_average([])
        Traceback (most recent call last):
            ...
        ValueError: 점수는 비어 있지 않은 리스트로 입력해야 합니다.

        점수 범위 밖 입력:
        >>> calculate_average([-1, 80])
        Traceback (most recent call last):
            ...
        ValueError: 각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다.
        >>> calculate_average([80, 101])
        Traceback (most recent call last):
            ...
        ValueError: 각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다.

        문자열과 True/False 거부:
        >>> calculate_average(["80", 90])
        Traceback (most recent call last):
            ...
        ValueError: 각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다.
        >>> calculate_average([True, 90])
        Traceback (most recent call last):
            ...
        ValueError: 각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다.
        >>> calculate_average([False, 90])
        Traceback (most recent call last):
            ...
        ValueError: 각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다.
    """
    if not isinstance(scores, list) or not scores:
        raise ValueError("점수는 비어 있지 않은 리스트로 입력해야 합니다.")

    for score in scores:
        if (
            isinstance(score, bool)
            or not isinstance(score, (int, float))
            or not 0 <= score <= 100
        ):
            raise ValueError(
                "각 점수는 0~100 사이의 숫자여야 하며, True/False는 사용할 수 없습니다."
            )

    total = sum((Decimal(str(score)) for score in scores), Decimal("0"))
    average = total / Decimal(len(scores))
    rounded_average = average.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return float(rounded_average)
