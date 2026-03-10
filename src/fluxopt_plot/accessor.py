"""PlotAccessor — main entry point for plotting fluxopt results."""

from __future__ import annotations

from typing import Any


class PlotAccessor:
    """Accessor providing plot methods for a fluxopt Result.

    Args:
        result: A solved fluxopt Result object.
    """

    def __init__(self, result: Any) -> None:
        self._result = result
