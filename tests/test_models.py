"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected"
    [
       ([[0, 0],[0, 0],[0, 0]],[0,0]) 
       ([[1, 2],[3, 4],[5, 6]],[3,4]) 
    ]
) 
def test_daily_mean_zeros(test, expexted):
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expexted)

@@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [4, 6, 9]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [4, -1, 9]),
    ])
def test_daily_max(test, expected):
    """Test that max function works for an array of positive integers."""
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [1, 1, 2]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [-4, -6, 2]),
    ])
def test_daily_min(test, expected):
    """Test that min function works for an array of positive and negative integers."""
    from inflammation.models import daily_min

    npt.assert_array_equal(daily_min(test), expected)
    
def test_daily_min_string():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min(['abd', 'ads'], ['aff','gfy'])