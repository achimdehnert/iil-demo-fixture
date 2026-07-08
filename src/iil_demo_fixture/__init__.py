"""iil-demo-fixture — Demo-Org-Fixture für iil-Plattform-Staging.

Liefert idempotente Stammdaten (Demo-Organisation, Standard-User) für alle
Klausel-1-Repos (ADR-212). Fachliche Sample-Daten (GBU, Kurse, …) bleiben
repo-lokal in separaten Daten-Migrationen.

Usage:
    from iil_demo_fixture import apply_demo_fixture
    apply_demo_fixture(env="staging")  # idempotent
"""

from __future__ import annotations

__version__ = "0.1.0"
__all__ = ["apply_demo_fixture"]


def apply_demo_fixture(env: str = "staging") -> None:
    """Apply Demo-Org-Fixture to the current Django database.

    Creates (or updates) a standard Demo-Organisation with:
    - Organization(slug="demo"|"staging-demo", name="Demo GmbH")
    - 3 standard users: Admin, Member, Guest (with Authentik OIDC sub)
    - Standard address + contact data

    Idempotent — safe to call multiple times (uses get_or_create).

    Args:
        env: Target environment ("staging" | "local"). Controls slug prefix.

    TODO (Folge-Issue):
        Implement actual fixture data once first Klausel-1-Repo (risk-hub)
        integrates this package. Define canonical Organization model interface.
    """
    # TODO: implement once Organization model interface is defined
    # Track: achimdehnert/platform#248 Folge-Issue
    raise NotImplementedError(
        "apply_demo_fixture() is not yet implemented. Track: achimdehnert/platform#248 Folge-Issue."
    )
