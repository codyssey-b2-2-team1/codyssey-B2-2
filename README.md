# 학생용 학습 도우미 함수 모음

코디세이 B2-2 팀미션 「친구 3~5명과 함께 프로그램 만드는 법 연습하기」 팀 저장소입니다.
학생이 공부할 때 자주 쓰는 계산을 작은 Python 함수로 만들면서 GitHub 협업 과정(Issue → 브랜치 → PR → 리뷰 → 병합)을 연습합니다.

## 개발 환경

- Python 3.10 이상
- 외부 라이브러리 없음 (표준 라이브러리만 사용)

## 담당 기능

| 담당 | 파일 | 함수 | 하는 일 |
| --- | --- | --- | --- |
| A: 강서연 | `src/scores.py` | `calculate_average(scores)` | 점수 목록의 평균 |
| B: 김수민 | `src/deadlines.py` | `days_until(due_date, base_date)` | 마감일까지 남은 날짜 |
| C: 윤정민 | `src/study_time.py` | `format_study_time(minutes)` | 분 → "N시간 M분" |
| D: 임재홍 | `src/progress.py` | `calculate_progress(completed, total)` | 과제 진행률(%) |

## 팀 합의 사항 (구현 전 확정)

- `calculate_progress`는 **퍼센트**를 소수점 첫째 자리까지 반올림해 반환합니다.
- 숫자를 받는 함수는 `True`/`False`(bool)를 **허용하지 않고** `ValueError`를 냅니다. (Python에서 bool은 int로 취급되기 때문)
- 오류는 모두 `ValueError`로 통일합니다.
- `src/__init__.py`는 첫 PR에서 수정하지 않습니다. 주말 충돌 실습 때 함께 수정합니다.

## 사용 방법

(각 담당자가 기능 PR에서 사용 예시를 채웁니다.)

과제 진행률 계산:

```python
from src.progress import calculate_progress

print(calculate_progress(1, 3))  # 33.3
```

## 브랜치 전략

GitHub Flow를 사용합니다. 자세한 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 봐 주세요.

(GitHub Flow를 선택한 이유 3줄 — 담당자가 PR로 작성)

## 문서

- [협업 규칙](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출물 인덱스](SUBMISSION.md)
