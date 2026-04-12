"""Deterministic grader for the medium task."""

from app.models import TaskData
from app.state import RuntimeState


def grade_medium(task: TaskData, runtime_state: RuntimeState) -> float:
    """Grade the vendor-selection task deterministically.

    Returns a raw score in [0.0, 1.0].  Normalization to the strict-open
    interval (0, 1) is applied by env.grade() via normalize_submission_score.
    """
    if runtime_state.selected_vendor == task.expected_vendor_id:
        return 1.0
    if runtime_state.selected_vendor in task.acceptable_vendor_ids:
        return 0.5
    return 0.0