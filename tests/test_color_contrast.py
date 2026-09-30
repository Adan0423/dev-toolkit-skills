import copy
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/design/color-palette-studio'
spec = importlib.util.spec_from_file_location('contrast', SKILL / 'scripts/contrast_audit.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class ContrastTests(unittest.TestCase):
    def test_reference_extremes(self):
        self.assertEqual(c.contrast_ratio('#fff', '#000'), 21)
        self.assertEqual(c.contrast_ratio('#abc', '#abc'), 1)

    def test_normalization_and_symmetry(self):
        self.assertEqual(c.normalize_hex('#abc'), '#AABBCC')
        self.assertEqual(c.contrast_ratio('#123', '#abc'), c.contrast_ratio('#abc', '#123'))

    def test_no_rounding_to_pass(self):
        self.assertFalse(c.meets_requirement(4.4999, 'text'))
        self.assertFalse(c.pair_result('#777777', '#FFFFFF')['passes'])
        self.assertTrue(c.meets_requirement(3, 'ui'))

    def test_original_teal_fails_white_text(self):
        self.assertFalse(c.pair_result('#FFFFFF', '#00ADB5')['passes'])

    def test_unsupported_formats(self):
        for value in ('#fff8', '#12345678', 'white', 'oklch(50% 0.1 20)', None):
            with self.assertRaises(ValueError):
                c.normalize_hex(value)
        with self.assertRaises(ValueError):
            c.pair_result('#fff', '#000', [])

    def test_example_and_derived_css(self):
        palette = c.load_palette(SKILL / 'assets/palette-example.json')
        result = c.audit_palette(palette)
        self.assertTrue(result['passes_all_declared_pairs'])
        self.assertEqual(result['checked_pairs'], 32)
        self.assertEqual(result['unchecked_themes'], [])
        self.assertEqual(c.emit_css(palette), (SKILL / 'assets/tokens-example.css').read_text(encoding='utf-8'))

    def test_invalid_pairs(self):
        original = c.load_palette(SKILL / 'assets/palette-example.json')
        for mutation in ('empty', 'token', 'duplicate'):
            palette = copy.deepcopy(original)
            if mutation == 'empty':
                palette['checks'] = []
            elif mutation == 'token':
                palette['checks'][0]['foreground'] = 'missing'
            else:
                palette['checks'].append(copy.deepcopy(palette['checks'][0]))
            with self.assertRaises(ValueError):
                c.audit_palette(palette)

    def test_unchecked_theme_is_reported(self):
        palette = c.load_palette(SKILL / 'assets/palette-example.json')
        palette['checks'] = [item for item in palette['checks'] if item['theme'] == 'light']
        self.assertEqual(c.audit_palette(palette)['unchecked_themes'], ['dark'])

    def test_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'invalid.json'
            path.write_text('{"themes": {}, "themes": {}}', encoding='utf-8')
            with self.assertRaises(ValueError):
                c.load_palette(path)


if __name__ == '__main__':
    unittest.main()
