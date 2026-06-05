"""
regulatory_tags.py
실제 DB 컬럼명 기준으로 작성된 컬럼 → 규제 조항 매핑
"""

REGULATORY_TAG_MAP = {

    # ── 개인정보보호법 제15조: 일반 개인정보 ──
    "insured_name":    {"law": "개인정보보호법", "article": "제15조", "severity": "중", "category": "개인정보"},
    "birth_date":      {"law": "개인정보보호법", "article": "제15조", "severity": "중", "category": "개인정보"},
    "gender":          {"law": "개인정보보호법", "article": "제15조", "severity": "하", "category": "개인정보"},

    # ── 개인정보보호법 제23조: 민감정보 ──
    "diagnosis_code":       {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "prior_diagnosis_code": {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "primary_diagnosis":    {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "icd_code":             {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "death_cause":          {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "death_cause_type":     {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "disability_type":      {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "disability_subtype":   {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "disability_body_part": {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "cdr_score":            {"law": "개인정보보호법", "article": "제23조", "severity": "상", "category": "민감정보"},
    "health_exam_completed":{"law": "개인정보보호법", "article": "제23조", "severity": "중", "category": "민감정보"},

    # ── 보험업법 제176조: 보험정보 ──
    "monthly_premium":        {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "annual_premium":         {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "total_paid_premium":     {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "sum_insured":            {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "paid_amount":            {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "claim_denial_reason":    {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "denial_detail":          {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "premium_surcharge_rate": {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "condition_type":         {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "decision_type":          {"law": "보험업법", "article": "제176조", "severity": "중", "category": "보험정보"},
    "surrender_value":        {"law": "보험업법", "article": "제176조", "severity": "하", "category": "보험정보"},

    # ── 망분리규제: 외부망 전송 시 문제되는 식별·심사 정보 ──
    "disability_payment_rate":    {"law": "망분리규제", "article": "금융위 가이드라인", "severity": "중", "category": "심사정보"},
    "risk_surcharge_rate":        {"law": "망분리규제", "article": "금융위 가이드라인", "severity": "중", "category": "심사정보"},
    "extra_surcharge_rate":       {"law": "망분리규제", "article": "금융위 가이드라인", "severity": "중", "category": "심사정보"},
    "investigation_consent":      {"law": "망분리규제", "article": "금융위 가이드라인", "severity": "중", "category": "심사정보"},
    "insured_written_consent":    {"law": "망분리규제", "article": "금융위 가이드라인", "severity": "중", "category": "심사정보"},
}

SEVERITY_COLOR = {"상": "#E24B4A", "중": "#EF9F27", "하": "#1D9E75"}

REGULATION_SUMMARY = {
    "개인정보보호법": {"article_range": "제15·23조",    "key_risk": "개인정보·민감정보 외부 전송"},
    "보험업법":       {"article_range": "제176조",      "key_risk": "보험정보 제3자 제공"},
    "AI 기본법":      {"article_range": "제10·11조",    "key_risk": "고영향 AI 안전성·투명성 의무"},
    "망분리규제":     {"article_range": "금융위 가이드","key_risk": "클라우드 LLM API 외부망 호출"},
}