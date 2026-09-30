"""Read normalized, non-overlapping ad rows; emit grouped metrics, never mutate accounts."""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

BASE = ("platform", "account", "currency", "attribution", "conversion_event", "period")
METRICS = ("spend", "impressions", "clicks", "conversions")


def number(raw, field, row):
    try:
        value = Decimal(raw.strip())
    except (AttributeError, InvalidOperation):
        raise ValueError(f"Fila {row}: {field} no es un número") from None
    if not value.is_finite() or value < 0:
        raise ValueError(f"Fila {row}: {field} debe ser finito y no negativo")
    if field in ("impressions", "clicks") and value != value.to_integral_value():
        raise ValueError(f"Fila {row}: {field} debe ser entero")
    # JSON output must stay finite in consumers that use IEEE 754 numbers.
    if not math.isfinite(float(value)):
        raise ValueError(f"Fila {row}: {field} fuera del rango representable")
    return value


def safe_float(value):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("Total o ratio fuera del rango JSON representable")
    return result


def ratio(numerator, denominator, multiplier=1):
    return safe_float(numerator * multiplier / denominator) if denominator else None


def analyze(path, group_by=("campaign",)):
    if len(set(group_by)) != len(group_by) or set(group_by) & (set(BASE) | set(METRICS) | {"conversion_value"}):
        raise ValueError("Dimensiones duplicadas o métricas usadas como dimensiones")
    dimensions = (*BASE, *group_by)
    groups = {}
    row_count = 0
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        required = {*dimensions, *METRICS, "campaign"}
        if len(set(fields)) != len(fields):
            raise ValueError("Encabezados duplicados")
        if not required.issubset(fields):
            raise ValueError("Columnas ausentes: " + ", ".join(sorted(required - set(fields))))
        for index, row in enumerate(reader, 2):
            if None in row:
                raise ValueError(f"Fila {index}: columnas adicionales sin encabezado")
            for field in (*dimensions, "campaign"):
                if not row.get(field) or not row[field].strip():
                    raise ValueError(f"Fila {index}: {field} vacío")
            key = tuple(row[field].strip() for field in dimensions)
            totals = groups.setdefault(key, {**{field: Decimal(0) for field in METRICS},
                                              "conversion_value": Decimal(0), "value_complete": True, "rows": 0})
            for field in METRICS:
                totals[field] += number(row.get(field), field, index)
            value = row.get("conversion_value")
            if value is None or not value.strip():
                totals["value_complete"] = False
            else:
                totals["conversion_value"] += number(value, "conversion_value", index)
            totals["rows"] += 1
            row_count += 1
    if not row_count:
        raise ValueError("CSV sin filas de datos")
    result = []
    for key, totals in sorted(groups.items()):
        spend, impressions, clicks, conversions = (totals[field] for field in METRICS)
        result.append({
            "dimensions": dict(zip(dimensions, key)), "rows": totals["rows"],
            "totals": {**{field: safe_float(totals[field]) for field in METRICS},
                       "conversion_value": safe_float(totals["conversion_value"]) if totals["value_complete"] else None},
            "metrics": {"ctr_percent": ratio(clicks, impressions, 100),
                        "cpc": ratio(spend, clicks), "cpm": ratio(spend, impressions, 1000),
                        "cpa": ratio(spend, conversions),
                        "roas": ratio(totals["conversion_value"], spend) if totals["value_complete"] else None},
            "warnings": [] if totals["value_complete"] else ["Valor de conversión incompleto: ROAS desconocido"],
        })
    return {"input_rows": row_count, "group_count": len(result), "groups": result,
            "limitations": ["Filas deben ser no solapadas y de igual granularidad",
                            "Métricas atribuidas no prueban incrementalidad ni beneficio"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--group-by", default="campaign")
    args = parser.parse_args()
    try:
        dimensions = tuple(part.strip() for part in args.group_by.split(",") if part.strip())
        print(json.dumps(analyze(args.csv_file, dimensions), ensure_ascii=False, indent=2, allow_nan=False))
    except (ValueError, OSError, csv.Error, OverflowError, ArithmeticError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
