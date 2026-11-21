"""학생용 학습 도우미 함수 모음.

네 담당 함수를 패키지 루트에서 바로 가져올 수 있게 노출한다.
충돌 실습은 PR #23·#25에서 끝났고, 남은 두 함수는 이 파일에서 함께 노출한다.
"""

from .deadlines import days_until
from .progress import calculate_progress
from .scores import calculate_average
from .study_time import format_study_time

__all__ = [
    "calculate_average",
    "days_until",
    "format_study_time",
    "calculate_progress",
]
