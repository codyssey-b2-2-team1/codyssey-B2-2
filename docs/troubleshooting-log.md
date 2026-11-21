# Troubleshooting Log

> 주말 실습 후 시나리오마다 아래 양식을 채웁니다. (amend / reset --soft / revert / stash·pop 4종, 전원 최소 1개 참여)

## 시나리오: stash

### 참여자·역할
- 임재홍(`sarguments`)(실행·기록)

### 상황·재현 절차
- 개인 브랜치 `feature/jaehong-stash-log`에서 임시 브랜치 `stash-test`를 만들어 실습했다.
- 추적 파일 수정만 보관하는 경우(`git stash`)와 추적하지 않는 새 파일까지 보관하는 경우(`git stash -u`)를 나눠 확인했다.
- 같은 줄을 양쪽에서 다르게 수정한 뒤 복원해 충돌을 재현했다.

### 수행 명령
```bash
git switch -c stash-test

# 1) 새 파일 포함 여부
echo 'scratch2' > stash-test2.tmp
printf '\n-u 확인\n' >> docs/team-practice.md
git stash -u
git status --short
git stash pop

# 2) 복원 충돌 재현
sed -i '' 's/^- 강서연: 점수 평균 계산 함수 담당$/- 강서연: 점수 평균·중앙값 계산 함수 담당/' docs/team-practice.md
git stash
sed -i '' 's/^- 강서연: 점수 평균 계산 함수 담당$/- 강서연: 점수 평균 전용 함수 담당/' docs/team-practice.md
git commit -am "test: stash 복원 충돌 재현"
git stash pop
```

### 결과
- `-u` 없이 보관하면 추적하지 않는 새 파일은 보관되지 않아 워킹트리에 남는다.
- `git stash -u` 직후 `git status --short`는 비어 있었고, 추적 파일 수정과 새 파일 `stash-test2.tmp`가 함께 보관됐다. `git stash pop` 후 두 변경이 모두 돌아왔다.
- `git stash pop` 충돌 시 실제 마커:
```text
<<<<<<< Updated upstream
- 강서연: 점수 평균 전용 함수 담당
=======
- 강서연: 점수 평균·중앙값 계산 함수 담당
>>>>>>> Stashed changes
- 임재홍: 과제 진행률 계산 함수 담당
```
- 함께 출력된 메시지: `CONFLICT (content): Merge conflict in docs/team-practice.md`, `The stash entry is kept in case you need it again.`

### 주의점 (원격 히스토리·협업 영향)
- 충돌한 `pop`은 stash를 지우지 않는다. 정리하지 않으면 stash가 계속 쌓이므로 `git stash drop` 또는 `git stash clear`로 지운다.
- `-u` 없이 보관하면 새 파일이 워킹트리에 남아 브랜치를 바꿔도 따라간다. 새 파일까지 정리하려면 `-u`를 쓴다.
- 실습은 push하지 않은 임시 브랜치에서만 했고, 공유 브랜치 이력은 바꾸지 않았다. 실습 커밋은 브랜치 삭제로 사라졌다.

### 이 방법을 선택한 이유
- 작업 도중 긴급히 브랜치를 전환할 때 커밋하지 않은 변경을 보존할 수 있고, 커밋을 만들지 않아 이력이 남지 않는다.
- `reset --soft`는 이력 재작성, `revert`는 취소 커밋 생성이라 "미커밋 변경 보관" 목적에는 stash가 맞다.

### 증빙 링크
- 이슈: https://github.com/codyssey-b2-2-team1/codyssey-B2-2/issues/27
