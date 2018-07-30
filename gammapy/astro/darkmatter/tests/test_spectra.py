# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals

from .. import PrimaryFlux
from ....utils.testing import assert_quantity_allclose

import pytest
import astropy.units as u


def test_primary_flux():
    with pytest.raises(ValueError):
        primflux = PrimaryFlux(channel="Spam", mDM=1 * u.TeV)

    primflux = PrimaryFlux(channel="W", mDM=1 * u.TeV)
    actual = primflux.table_model(500 * u.GeV)
    desired = 9.324355468682548e-05 / u.GeV
    assert_quantity_allclose(actual, desired)
