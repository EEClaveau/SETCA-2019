"""
Tests for geom_analysis2.py
"""
import pytest
import geom_analysis2 as ga

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed=ga.calculate_distance(coord1,coord2)

    assert observed == 2.0

def test_bond_check_false():
    """A test for the bond_check function."""
    bond_distance_check=1.5
    observed=ga.bond_check(bond_distance_check)
    assert observed == False

def test_bond_check_true():
    """A test for the bond_check function."""
    bond_distance_check=1.2
    observed=ga.bond_check(bond_distance_check)
    assert observed == True

def test_bond_check_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)
