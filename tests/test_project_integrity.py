
from pathlib import Path

# 프로젝트의 필수 파일이 존재하는지 검사
ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "app.py",
    "pages",
    "images",
]

def test_required_files_exist():
    """필수 파일과 폴더가 존재하는지 확인한다."""
    missing = [
        name
        for name in REQUIRED_FILES
        if not (ROOT / name).exists()
    ]

    assert not missing, f"필수 파일 또는 폴더 누락: {missing}"
