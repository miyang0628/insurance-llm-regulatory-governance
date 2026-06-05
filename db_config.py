"""
db_config.py
DB 연결 유틸리티

data/insurance_uw.db 를 기준으로 연결합니다.
외부 경로를 참조하지 않습니다.
"""

import sqlite3
import os

# ── DB 경로: 프로젝트 루트의 data/ 폴더 고정 ──────────
_ROOT   = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(_ROOT, "data", "insurance_uw.db")
# ──────────────────────────────────────────────────────


def get_connection() -> sqlite3.Connection:
    """DB 연결 반환. data/insurance_uw.db 없으면 안내 메시지 출력."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(
            f"DB 파일을 찾을 수 없습니다: {DB_PATH}\n"
            "논문 A의 insurance_uw.db 를 이 프로젝트의 data/ 폴더에 복사하세요."
        )
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_schema(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """테이블별 컬럼 목록 반환"""
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = [row[0] for row in cur.fetchall()]
    return {
        t: [row[1] for row in conn.execute(f"PRAGMA table_info({t})").fetchall()]
        for t in tables
    }


if __name__ == "__main__":
    conn = get_connection()
    schema = get_schema(conn)
    conn.close()
    print(f"DB: {DB_PATH}")
    print(f"테이블 수: {len(schema)}")
    for t, cols in schema.items():
        print(f"  {t}: {len(cols)}개 컬럼")
