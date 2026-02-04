def explain(result, keyword_hits, email_flag, salary_flag):
    reasons = []

    if keyword_hits > 0:
        reasons.append("Contains scam-related keywords")
    if email_flag:
        reasons.append("Uses free email domain")
    if salary_flag:
        reasons.append("Unrealistic salary mentioned")

    if not reasons:
        reasons.append("No major scam indicators found")

    return reasons

