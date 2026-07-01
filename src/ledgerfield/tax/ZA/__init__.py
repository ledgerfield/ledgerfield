"""South Africa tax calculators.

CIT = 27% flat rate (effective 1 April 2022).
VAT = 15% standard rate.
Dividends Tax = 20%.
SDL = 1% Skills Development Levy.
UIF = 1% employer + 1% employee (capped at ZAR 17,712/year contribution base).
"""

from ledgerfield.tax.ZA.cit import bereken_cit_south_africa, CITResultZA

__all__ = ["bereken_cit_south_africa", "CITResultZA"]
