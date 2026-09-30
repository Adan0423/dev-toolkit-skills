"""Execute example SQLite DDL; verify integrity, not remote authorization or server RLS."""
from pathlib import Path
import sqlite3
import unittest

SQL = Path(__file__).resolve().parents[1] / "skills/architecture/database-engineering-suite/assets/sqlite-relational-example.sql"


class RelationalExampleTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.executescript(SQL.read_text(encoding="utf-8"))
        self.db.executescript("""
        INSERT INTO tenants VALUES (1,'A'),(2,'B');
        INSERT INTO customers VALUES (1,11,'Customer A'),(2,22,'Customer B');
        INSERT INTO products VALUES (1,101,'same-sku'),(2,202,'same-sku');
        INSERT INTO orders(tenant_id,id,customer_id,currency) VALUES (1,31,11,'PEN'),(2,32,22,'USD');
        INSERT INTO order_items VALUES (1,31,1,101,2,500),(2,32,1,202,1,300);
        """)

    def tearDown(self):
        self.db.close()

    def test_valid_relations_and_no_fk_violations(self):
        self.assertEqual(self.db.execute("PRAGMA foreign_keys").fetchone()[0], 1)
        self.assertEqual(self.db.execute("PRAGMA foreign_key_check").fetchall(), [])
        self.assertEqual(self.db.execute("SELECT sum(quantity * unit_price_minor) FROM order_items WHERE tenant_id=1 AND order_id=31").fetchone()[0], 1000)

    def test_customer_from_another_tenant_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO orders(tenant_id,id,customer_id,currency) VALUES (1,99,22,'PEN')")

    def test_product_from_another_tenant_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO order_items VALUES (1,31,2,202,1,100)")

    def test_order_from_another_tenant_rejected(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO order_items VALUES (1,32,2,101,1,100)")

    def test_duplicate_sku_rejected_within_tenant(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO products VALUES (1,303,'same-sku')")

    def test_invalid_quantity_and_money_rejected(self):
        for quantity, price in [(0,1),(-1,1),(1,-1),(1.5,1),(1,1.5),(None,1)]:
            with self.subTest(quantity=quantity, price=price):
                with self.assertRaises(sqlite3.IntegrityError):
                    self.db.execute("INSERT INTO order_items VALUES (1,31,2,101,?,?)",(quantity,price))

    def test_null_customer_invalid_status_and_currency_rejected(self):
        for customer,status,currency in [(None,'draft','PEN'),(11,'other','PEN'),(11,'draft','pen'),(11,'draft','P3N')]:
            with self.subTest(customer=customer,status=status,currency=currency):
                with self.assertRaises(sqlite3.IntegrityError):
                    self.db.execute("INSERT INTO orders(tenant_id,id,customer_id,status,currency) VALUES (1,99,?,?,?)",(customer,status,currency))

    def test_referenced_parent_delete_rejected(self):
        for statement in ["DELETE FROM customers WHERE tenant_id=1 AND id=11",
                          "DELETE FROM products WHERE tenant_id=1 AND id=101",
                          "DELETE FROM orders WHERE tenant_id=1 AND id=31"]:
            with self.subTest(statement=statement):
                with self.assertRaises(sqlite3.IntegrityError): self.db.execute(statement)

    def test_tenant_reassignment_rejected_by_relationship(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("UPDATE orders SET tenant_id=2 WHERE tenant_id=1 AND id=31")


if __name__ == "__main__":
    unittest.main()
