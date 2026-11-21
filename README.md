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

## 팀 합의 사항

- 오류는 모두 `ValueError`로 통일하고, `"ValueError"` 문자열을 반환하는 방식은 쓰지 않습니다.
- 숫자를 받는 함수는 `True`/`False`(bool)를 **허용하지 않고** `ValueError`를 냅니다. (Python에서 bool은 int로 취급되기 때문)
- 반환 형식과 반올림 자릿수는 함수마다 Issue에서 정하고, 각 함수 docstring의 예시로 확인합니다. 현재 평균은 소수 둘째 자리, 진행률은 소수 첫째 자리입니다.
- `src/__init__.py`는 첫 PR에서 수정하지 않고, 충돌 실습 뒤 PR #23·#25에서 함수 노출을 추가했습니다.

## 사용 방법

```python
from src.scores import calculate_average
from src.deadlines import days_until
from src.study_time import format_study_time
from src.progress import calculate_progress

print(calculate_average([88, 91, 95]))          # 91.33
print(days_until("2026-11-25", "2026-11-20"))   # 5
print(format_study_time(95))                    # 1시간 35분
print(calculate_progress(1, 3))                 # 33.3
```

잘못된 입력은 모두 `ValueError`로 처리합니다.

```python
calculate_average([])                  # ValueError: 빈 목록
days_until("2026-02-30", "2026-11-20") # ValueError: 존재하지 않는 날짜
format_study_time(90.5)                # ValueError: 정수가 아님
calculate_progress(4, 3)               # ValueError: 완료 수가 전체보다 큼
```

## 브랜치 전략

GitHub Flow를 사용합니다. 자세한 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 봐 주세요.

- `main`은 항상 동작하는 상태로 두고, 작업마다 Issue와 `feature/이름-작업` 브랜치를 따로 만듭니다.
- 모든 변경은 PR로 올려 다른 팀원 1명 이상의 리뷰와 승인을 받은 뒤 병합합니다.
- 작은 단위로 자주 병합해 충돌 범위를 줄이고, 병합된 브랜치는 정리합니다.

## 문서

- [협업 규칙](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md)
- [트러블슈팅 기록](docs/troubleshooting-log.md)
- [제출물 인덱스](SUBMISSION.md)
