"""South Africa SA GAAP (IFRS) chart of accounts.

SA GAAP = South African Generally Accepted Accounting Practice, fully converged
with IFRS as adopted by the South African Institute of Chartered Accountants
(SAICA) and mandated by the Companies Act 71 of 2008.
VAT = Value-Added Tax (15%).
CIT = Corporate Income Tax (27% flat rate from 1 April 2022).
Dividends Tax = 20% (withheld at source).
"""

from ledgerfield.schemas.ZA.schema import ZA_GAAP, ZAGAAPAccount

__all__ = ["ZA_GAAP", "ZAGAAPAccount"]
