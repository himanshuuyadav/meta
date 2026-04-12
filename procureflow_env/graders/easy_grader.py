"""Deterministic grader for the easy task."""

from app.models import TaskData
from app.state import RuntimeState


def grade_easy(task: TaskData, runtime_state: RuntimeState) -> float:
    """Grade the easy policy task deterministically.

    Returns a score strictly within (0, 1).
    """
    if runtime_state.decision == task.expected_decision:
        return 0.99
    return 0.1