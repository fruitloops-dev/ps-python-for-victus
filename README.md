# Python 알고리즘 수업 연습 환경

대학교 알고리즘 수업에서 Python 파일을 바로 작성하고 실행하기 위한 간단한 VS Code
환경입니다. Python 3.13, 프로젝트 가상환경(`.venv`), Pylance와 Ruff를 사용합니다.

## 실행

1. 실행할 `.py` 파일을 엽니다.
2. 편집기 오른쪽 위의 `▶ Run Python File` 버튼을 누릅니다.
3. 아래쪽 `TERMINAL`에서 출력 결과를 확인합니다.

코드에 `input()`이 있으면 같은 터미널에 값을 입력하고 `Enter`를 누르면 됩니다. 현재
파일을 실행하는 다른 방법은 `Ctrl+Shift+B`입니다.

처음 확인할 때는 루트의 `main.py`를 열고 `▶` 버튼을 누르면 다음 결과가 출력됩니다.

```text
before: [5, 2, 4, 1, 3]
after: [1, 2, 3, 4, 5]
```

## 새 연습 파일

수업 주차나 주제에 맞게 자유롭게 파일을 만들면 됩니다.

```text
week01/selection_sort.py
week02/binary_search.py
week03/graph.py
```

실행할 파일이 현재 편집기 탭에 열려 있는지만 확인하고 `▶` 버튼을 누르면 됩니다.

## 디버깅과 코드 정리

- 중단점을 찍고 `F5`: 현재 파일 디버깅
- `Ctrl+S`: Ruff로 자동 포맷 및 import 정리
- `Ctrl+Shift+P` → `Tasks: Run Task` → `Check: 전체`: 전체 코드 검사

인터프리터가 자동으로 선택되지 않으면 `Ctrl+Shift+P` → `Python: Select Interpreter`에서
`.venv\Scripts\python.exe`를 한 번 선택합니다.
