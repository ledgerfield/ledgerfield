"""NEN4400 compliance checklist for Dutch payroll/labour chain liability."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum


class ComplianceStatus(Enum):
    OK = "ok"
    WARNING = "warning"
    MISSING = "missing"
    NOT_APPLICABLE = "n/a"


@dataclass
class ComplianceItem:
    code: str
    description: str
    requirement: str
    status: ComplianceStatus = ComplianceStatus.MISSING
    notes: str = ""
    mandatory: bool = True


# All 16 items ported from NEN4400_CHECKLIST in rgs_source.py
NEN4400_ITEMS: list[ComplianceItem] = [
    ComplianceItem(
        code="NEN4400-01",
        description="KvK inschrijving",
        requirement="Actueel uittreksel Kamer van Koophandel",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-02",
        description="Belastingdienst registratie",
        requirement="BTW-nummer, loonheffingennummer, VPB",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-03",
        description="Identificatie bestuurders",
        requirement="Paspoort/ID + uittreksel KvK alle bestuurders",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-04",
        description="Loonheffing aangiften",
        requirement="Tijdig ingediend en betaald (geen achterstanden)",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-05",
        description="BTW aangiften",
        requirement="Tijdig ingediend en betaald",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-06",
        description="VPB aangiften",
        requirement="Tijdig ingediend en betaald",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-07",
        description="Jaarrekening",
        requirement="Gedeponeerd bij KvK (binnen 13 maanden)",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-08",
        description="G-rekening",
        requirement="Geopend bij een bank die G-rekeningen aanbiedt",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-09",
        description="Personeelsadministratie",
        requirement="Loonadministratie compleet, ID-plicht, VOG indien vereist",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-10",
        description="Verklaring betalingsgedrag",
        requirement="Geen betalingsachterstanden Belastingdienst",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-11",
        description="Verzekeringen",
        requirement="Bedrijfsaansprakelijkheid, beroepsaansprakelijkheid",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-12",
        description="Arbeidsovereenkomsten",
        requirement="Alle werknemers hebben getekend contract",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-13",
        description="WAB/Waadi registratie",
        requirement="Inschrijving NBBU/ABU indien uitzendbureau",
        mandatory=False,
    ),
    ComplianceItem(
        code="NEN4400-14",
        description="Grootboekadministratie",
        requirement="Sluitende administratie volgens RGS",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-15",
        description="Facturen",
        requirement="Voldoen aan BTW-factuureisen (15 elementen)",
        mandatory=True,
    ),
    ComplianceItem(
        code="NEN4400-16",
        description="Audit trail",
        requirement="Alle wijzigingen traceerbaar",
        mandatory=True,
    ),
]


class NEN4400Checker:
    def __init__(self, items: list[ComplianceItem] | None = None) -> None:
        if items is None:
            # Deep-copy defaults so mutations don't affect the module-level list
            self._items: dict[str, ComplianceItem] = {
                item.code: ComplianceItem(
                    code=item.code,
                    description=item.description,
                    requirement=item.requirement,
                    status=item.status,
                    notes=item.notes,
                    mandatory=item.mandatory,
                )
                for item in NEN4400_ITEMS
            }
        else:
            self._items = {item.code: item for item in items}

    def check(self, item_code: str, status: ComplianceStatus, notes: str = "") -> None:
        """Update the status (and optional notes) for a compliance item."""
        if item_code not in self._items:
            raise KeyError(f"Unknown NEN4400 item code: {item_code!r}")
        item = self._items[item_code]
        self._items[item_code] = ComplianceItem(
            code=item.code,
            description=item.description,
            requirement=item.requirement,
            status=status,
            notes=notes,
            mandatory=item.mandatory,
        )

    def score(self) -> tuple[int, int]:
        """Return (passed_mandatory, total_mandatory).

        'passed' means status is OK.
        """
        mandatory = [i for i in self._items.values() if i.mandatory]
        passed = sum(1 for i in mandatory if i.status == ComplianceStatus.OK)
        return passed, len(mandatory)

    def is_compliant(self) -> bool:
        """True when all mandatory items have status OK."""
        passed, total = self.score()
        return passed == total

    def report(self) -> list[dict]:
        """Return all items as a list of dicts, sorted by code."""
        return [
            {
                "code": item.code,
                "description": item.description,
                "requirement": item.requirement,
                "status": item.status.value,
                "notes": item.notes,
                "mandatory": item.mandatory,
            }
            for item in sorted(self._items.values(), key=lambda i: i.code)
        ]
