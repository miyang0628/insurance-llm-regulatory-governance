# Insurance LLM Regulatory Governance

생명보험사 LLM 기반 언더라이팅 AI 도입의 규제 리스크와 거버넌스 프레임워크

## 논문 정보
- **제목**: 생명보험사 LLM 기반 언더라이팅 AI 도입의 규제 리스크와 거버넌스 프레임워크
- **목표 저널**: 경영정보학연구 (KCI우수등재)
- **방법론**: 법령 분석 + 규제 위반 시뮬레이션 실험 (3종)

## 폴더 구조
```
├── data/                          # 실험용 DB (자체 보관, 외부 경로 참조 없음)
│   └── insurance_uw.db
├── db_config.py                   # DB 연결 유틸 (data/ 내부 경로 고정)
├── regulatory_tags.py             # 컬럼 → 규제 조항 매핑 딕셔너리
├── regulation_analysis/           # 4개 규제 분석 문서
├── experiments/                   # 규제 위반 시뮬레이션 실험 3종
│   ├── exp1_sensitive_exposure/   # 민감정보 노출 측정
│   ├── exp2_network_separation/   # 망분리 시나리오
│   └── exp3_semantic_layer_effect/# Semantic Layer 규제 충족 효과
├── notebooks/                     # 주피터노트북 (00~06)
├── results/                       # 실험 결과 (raw/figures/tables)
├── framework/                     # 거버넌스 프레임워크 산출물
└── paper_assets/                  # 논문 그림·표 목록
```

## 환경 설정
```bash
conda activate uw-benchmark
pip install -r requirements.txt
```

## DB 준비
논문 A(`insurance-underwriting-nl2sql-benchmark`)의 DB를 복사합니다.
```bash
cp ../insurance-underwriting-nl2sql-benchmark/data/insurance_uw.db data/
```
또는 `setup_project_paper_b.py` 실행 전 같은 위치에 `insurance_uw.db` 를 두면 자동 복사됩니다.

## 실험 실행
```bash
python experiments/exp1_sensitive_exposure/exp1_run.py
python experiments/exp2_network_separation/exp2_run.py
python experiments/exp3_semantic_layer_effect/exp3_run.py
```

## 분석 대상 법령
- AI 기본법 (법률 제20676호, 2026.1.22 시행)
- 개인정보보호법 제23조 (민감정보 처리 제한)
- 보험업법 제176조 (정보보호 의무)
- 금융위원회 망분리 규제 가이드라인
