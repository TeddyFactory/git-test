import subprocess
import os
from datetime import date, timedelta

# 새로운 Git 저장소 초기화
subprocess.run(["git", "init"])
# git remote add origin git@github-floatfactory:TeddyFactory/git-test.git
# 시작 날짜와 종료 날짜 설정
start_date = date(2023, 6, 1)
end_date = date(2023, 8, 31)

# 초급 Python 코드 조각 목록
python_snippets = [
    "print('Hello, world!')",
    "x = 5",
    "y = 10",
    "print(x + y)",
    "for i in range(5): print(i)",
    "if x > y: print('x is greater')",
    "else: print('y is greater')",
    "def greet(): print('Hello')",
    "greet()",
    "import math",
    "print(math.sqrt(16))",
    "numbers = [1, 2, 3]",
    "print(sum(numbers))"
]

# 현재 날짜를 시작 날짜로 설정
current_date = start_date

# 파일 인덱스와 스니펫 인덱스 초기화
file_index = 1
snippet_index = 0

# 주어진 기간 동안 월, 수, 금에 커밋
while current_date <= end_date:
    if current_date.weekday() in [0, 2, 4]:  # 월요일은 0, 수요일은 2, 금요일은 4
        # 파일 생성 및 Python 코드 추가
        with open(f"python_code_{file_index}.py", "w") as f:
            f.write(python_snippets[snippet_index])

        # Git에 추가 및 커밋
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Adding python_code_{file_index}.py"])

        # 커밋 날짜 변경
        formatted_date = f"{current_date}T{10+file_index%12}:00:00"

        # GIT_COMMITTER_DATE 설정
        os.environ["GIT_COMMITTER_DATE"] = formatted_date

        # 날짜를 변경하여 커밋 다시 생성
        subprocess.run(["git", "commit", "--amend", "--no-edit", "--date", formatted_date])

        # rebase를 사용하여 커밋 시간을 재조정
        subprocess.run(["git", "rebase", "--ignore-date", "HEAD~1"])

        # 파일 인덱스와 스니펫 인덱스 업데이트
        file_index += 1
        snippet_index = (snippet_index + 1) % len(python_snippets)

    # 다음 날짜로 이동
    current_date += timedelta(days=1)
# Git에 푸시
subprocess.run(["git", "push", "-u", "origin", "main", "-f"])