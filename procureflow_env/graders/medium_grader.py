"""Deterministic grader for the medium task."""

from app.models import TaskData
from app.state import RuntimeState


def grade_medium(task: TaskData, runtime_state: RuntimeState) -> float:
    """Grade the vendor-selection task deterministically.

    Returns a score strictly within (0, 1).
    """
    if runtime_state.selected_vendor == task.expected_vendor_id:
        return 0.99
    if runtime_state.selected_vendor in task.acceptable_vendor_ids:
        return 0.5
    return 0.1