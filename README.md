# iil-demo-fixture

Demo-Org-Fixture für die iil-Plattform — liefert idempotente Stammdaten
(Demo-Organisation, Standard-User) für alle Staging-Umgebungen.

**ADR-212** (Demo-Org-Fixture) definiert dieses Package als zentrale
Quelle für Staging-Stammdaten. Fachliche Sample-Daten bleiben **repo-lokal**.

## Installation

```bash
pip install iil-demo-fixture
```

## Quickstart

```python
from iil_demo_fixture import apply_demo_fixture

# In einer Django-Datenmigration oder Management-Command:
apply_demo_fixture(env="staging")  # idempotent
```

Die Funktion erstellt (oder aktualisiert):
- `Organization(slug="staging-demo", name="Demo GmbH", …)`
- 3 Standard-User: Admin, Member, Guest (mit Authentik-OIDC-`sub`)
- Standard-Adresse und Kontaktdaten

## Stammdaten-Separation

**Was dieses Package liefert:** Organisations-Identität und Standard-User —
die Mindest-Stammdaten, die jedes Klausel-1-Repo zum Start braucht.

**Was hier NICHT enthalten ist:** Fachliche Sample-Daten (risk-hub GBU,
coach-hub Kurse, …). Diese bleiben in repo-lokalen Daten-Migrationen
(`0NNN_demo_sample_data.py`). Vom Tester erzeugte Daten werden durch
täglichen idempotenten Reset entfernt.

## Entwicklung

```bash
git clone https://github.com/achimdehnert/iil-demo-fixture
cd iil-demo-fixture
pip install -e ".[dev]"
pytest tests/ -v
```

## Status

`0.1.0` — Scaffold. Die Fixture-Implementierung erfolgt in einem Folge-Issue,
sobald das erste Klausel-1-Repo (risk-hub) die Integration aufnimmt und das
Organization-Model-Interface definiert ist.

## Referenzen

- [ADR-212](https://github.com/achimdehnert/platform/blob/main/docs/adr/ADR-212-traefik-ingress-staging-iil-pet.md)
- [platform#248](https://github.com/achimdehnert/platform/issues/248)
