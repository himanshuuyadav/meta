"""Deterministic grader for the easy task."""

from app.models import TaskData
from app.state import RuntimeState


def grade_easy(task: TaskData, runtime_state: RuntimeState) -> float:
    """Grade the easy policy task deterministically.

    Returns a raw score in [0.0, 1.0].  Normalization to the strict-open
    interval (0, 1) is applied by env.grade() via normalize_submission_score.
    """
    if runtime_state.decision == task.expected_decision:
        return 1.0
    return 0.0