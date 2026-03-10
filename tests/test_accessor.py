from fluxopt_plot import PlotAccessor


def test_plot_accessor_instantiates() -> None:
    accessor = PlotAccessor(result=None)
    assert accessor._result is None
