"""Scoring utilities for ProcureFlow grader responses."""

from __future__ import annotations


def normalize_submission_score(score: float) -> float:
    """Ensure score is strictly within the range [0.1, 0.99].
    
    Clamps boundary values to ensure they satisfy validation requirements:
    score > 0.0 and score < 1.0, while using safer bounds of [0.1, 0.99].
    """
    min_score = 0.1
    max_score = 0.99
    
    if score <= 0.0:
        return min_score
    if score >= 1.0:
        return max_score
    
    # Clamp within the safe range
    if score < min_score:
        return min_score
    if score > max_score:
        return max_score
    
    return score
