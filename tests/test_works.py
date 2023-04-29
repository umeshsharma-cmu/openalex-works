import pytest
from openalex_works.works import OpenAlexWorks


def test_ris():
    work = OpenAlexWorks("10.1038/s41586-020-2649-2")
    ris = work.get_ris()
    assert "TY  - JOUR" in ris


def test_bibtex():
    work = OpenAlexWorks("10.1038/s41586-020-2649-2")
    bibtex = work.get_bibtex()
    assert "@article{" in bibtex
