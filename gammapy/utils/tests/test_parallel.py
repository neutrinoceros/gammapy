# Licensed under a 3-clause BSD style license - see LICENSE.rst
import pytest
import gammapy.utils.parallel as parallel
from gammapy.utils.testing import requires_dependency


def test_get_multiprocessing():
    parallel.MULTIPROCESSING_BACKEND = "multiprocessing"
    multiprocessing = parallel.get_multiprocessing()
    assert multiprocessing.__name__ == "multiprocessing"


@requires_dependency("ray")
def test_get_multiprocessing_ray():
    parallel.MULTIPROCESSING_BACKEND = "ray"
    multiprocessing = parallel.get_multiprocessing()
    assert multiprocessing.__name__ == "ray.util.multiprocessing"


def test_run_multiprocessing_wrong_method():
    def func(arg):
        return arg

    with pytest.raises(ValueError):
        parallel.run_multiprocessing(
            func, [True, True], method="wrong_name", pool_kwargs=dict(processes=2)
        )
