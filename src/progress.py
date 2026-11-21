def calculate_progress(completed: int, total: int) -> float:
    """과제 진행률을 퍼센트로 계산해 소수점 첫째 자리까지 반올림한다.

    과제 수는 정수여야 하며, 0 <= completed <= total이고 total은
    0보다 커야 한다. 조건을 벗어나면 ValueError를 발생시킨다.

    >>> calculate_progress(1, 3)
    33.3
    """
    if type(completed) is not int or type(total) is not int:
        raise ValueError("과제 수는 정수여야 합니다.")
    if total <= 0:
        raise ValueError("전체 과제 수는 0보다 커야 합니다.")
    if not 0 <= completed <= total:
        raise ValueError("완료한 과제 수는 0 이상 전체 과제 수 이하여야 합니다.")
    return round(completed / total * 100, 1)
