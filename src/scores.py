"""점수 목록의 평균을 계산하는 학습 도우미 함수."""


def calculate_average(scores: list[int | float]) -> float:
    """0~100점 목록의 평균을 소수 둘째 자리까지 반올림해 반환한다.

    scores는 비어 있지 않은 list여야 한다. 각 점수는 bool을 제외한
    int 또는 float이며, 0 이상 100 이하여야 한다.
    잘못된 자료형, 빈 목록, 범위 밖 점수는 모두 ValueError로 처리한다.
    점수 자체는 반올림하지 않고 최종 평균만 반올림한다.

    사용 예시:
        일반 평균과 소수점 반올림:
        >>> calculate_average([80, 90, 100])
        90.0
        >>> calculate_average([88, 91, 95])
        91.33

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

    return round(sum(scores) / len(scores), 2)
