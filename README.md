# Python 알고리즘 풀이 환경

VS Code에서 Python 알고리즘 문제를 풀기 위한 가벼운 기본 구성입니다. Python 3.13,
프로젝트 로컬 가상환경(`.venv`), Ruff, pytest, Pylance, CPH를 기준으로 맞췄습니다.

## 빠른 사용법

1. 풀이 파일을 `solutions/` 아래에 만들거나 `templates/solution.py`를 복사합니다.
2. 루트의 `input.txt`에 예제 입력을 넣습니다.
3. 풀이 파일을 연 상태에서 `Ctrl+Shift+B`를 누르면 `input.txt`를 표준 입력으로 실행합니다.
4. 중단점을 찍고 `F5`를 누르면 같은 입력으로 디버깅합니다.

새 Python 파일에서 `pssolve`를 입력하고 자동 완성을 선택해도 같은 풀이 골격이 만들어집니다.

직접 입력하며 실행하려면 명령 팔레트의 `Tasks: Run Task`에서
`Python: 현재 파일 실행 (직접 입력)`을 선택합니다. 디버그 구성도 직접 입력용과
`input.txt`용 두 가지가 준비되어 있습니다. 기존 Code Runner의 `Ctrl+Alt+N`도 선택된
`.venv` 인터프리터로 직접 입력 실행되도록 연결했습니다.

## 품질 검사

VS Code는 Python 파일을 저장할 때 Ruff로 포맷하고 안전한 자동 수정을 적용합니다.
터미널에서 전체 검사를 실행하려면 다음 명령을 사용합니다.

```powershell
python -m ruff check .
python -m ruff format --check .
python -m pytest
```

또는 `Tasks: Run Task`에서 `Check: 전체`를 선택합니다.

## 폴더/파일 규칙

- `solutions/<사이트>/p문제번호_이름.py`: 풀이 파일
- `templates/solution.py`: 새 풀이용 최소 템플릿
- `tests/`: 재사용 함수나 로컬 도구 테스트
- `tools/run_with_input.py`: `input.txt`를 stdin으로 연결하는 실행/디버그 래퍼
- `input.txt`, `output.txt`: 로컬 스크래치 파일이며 Git에는 포함되지 않음

숫자로 시작하는 파일명은 Python 모듈로 가져오기 어려우므로 `1000.py`보다
`p1000_a_plus_b.py` 형식을 권장합니다.

## CPH(Competitive Programming Helper)

CPH는 Python과 이 프로젝트의 `.venv`를 사용하도록 설정되어 있습니다. 풀이 파일에서
`Ctrl+Alt+B`를 누르면 테스트 케이스 패널을 열 수 있습니다. 브라우저에서 문제와 샘플을
자동으로 가져오려면 별도로 Competitive Companion 브라우저 확장이 필요합니다.

## 환경 다시 만들기

`.venv`를 지운 뒤 Python 3.13으로 아래 명령을 실행하면 됩니다.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```
