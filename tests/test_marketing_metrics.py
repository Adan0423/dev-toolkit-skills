"""Regression checks for financial reporting invariants; no network or ad mutations."""
import csv
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
MODULE = Path(__file__).resolve().parents[1] / "skills/marketing/marketing-measurement-optimizer/scripts/analyze_ads_csv.py"
spec = importlib.util.spec_from_file_location("ads_metrics", MODULE)
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)


class MetricsTest(unittest.TestCase):
    def report(self, overrides):
        base = dict(platform="meta", account="a", currency="PEN", attribution="click7",
                    conversion_event="purchase", period="week1", campaign="c",
                    spend="100", impressions="1000", clicks="100", conversions="5", conversion_value="400")
        with tempfile.TemporaryDirectory(prefix="marketing-metrics-") as directory:
            path = Path(directory) / "report.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(base))
                writer.writeheader()
                writer.writerows([{**base, **change} for change in overrides])
            return metrics.analyze(path)

    def test_weighted_ratios(self):
        group = self.report([{}, dict(spend="50", impressions="9000", clicks="90", conversions="1", conversion_value="100")])["groups"][0]
        self.assertEqual(group["metrics"]["ctr_percent"], 1.9)
        self.assertEqual(group["metrics"]["cpa"], 25)
        self.assertAlmostEqual(group["metrics"]["cpc"], 150/190)
        self.assertAlmostEqual(group["metrics"]["roas"], 500/150)

    def test_zero_denominators_are_unknown(self):
        group = self.report([dict(spend="0", impressions="0", clicks="0", conversions="0", conversion_value="0")])["groups"][0]
        self.assertTrue(all(value is None for value in group["metrics"].values()))

    def test_missing_revenue_is_not_zero(self):
        group = self.report([{}, dict(conversion_value="")])["groups"][0]
        self.assertIsNone(group["metrics"]["roas"])
        self.assertIsNone(group["totals"]["conversion_value"])

    def test_incompatible_context_stays_separate(self):
        for field, value in [("currency","USD"),("platform","google"),("attribution","view1"),
                             ("account","b"),("conversion_event","lead"),("period","week2")]:
            with self.subTest(field=field):
                self.assertEqual(self.report([{}, {field:value}])["group_count"], 2)

    def test_invalid_data_rejected(self):
        for field,value in [("spend","NaN"),("spend","Infinity"),("spend","-1"),
                            ("conversions",""),("impressions","1.5"),("currency",""),("spend","1e999")]:
            with self.subTest(field=field):
                with self.assertRaises(ValueError): self.report([{field:value}])

    def test_fractional_conversions(self):
        group = self.report([dict(conversions="2.5")])["groups"][0]
        self.assertEqual(group["metrics"]["cpa"], 40)

    def test_absent_value_column(self):
        with tempfile.TemporaryDirectory(prefix="marketing-metrics-") as directory:
            path=Path(directory)/"input.csv"
            path.write_text("platform,account,currency,attribution,conversion_event,period,campaign,spend,impressions,clicks,conversions\nmeta,a,PEN,click7,purchase,week1,c,100,1000,100,5\n",encoding="utf-8")
            self.assertIsNone(metrics.analyze(path)["groups"][0]["metrics"]["roas"])


if __name__ == "__main__":
    unittest.main()
