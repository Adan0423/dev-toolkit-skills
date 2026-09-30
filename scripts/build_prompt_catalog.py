"""Index authored creative/web prompts; --check verifies without writing."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def build():
    categories, ids = [], set()
    paths = sorted((ROOT / 'prompts/creative').glob('*.md')) + sorted((ROOT / 'prompts/web').glob('*.md'))
    for path in paths:
        text = path.read_text(encoding='utf-8')
        matches = list(re.finditer(r'^## ([A-Z]{3}-\d{2}) · (.+)\n', text, re.M))
        if not matches:
            continue
        entries = []
        for index, match in enumerate(matches):
            identifier, title = match.groups()
            if identifier in ids:
                raise ValueError('ID repetido: ' + identifier)
            ids.add(identifier)
            section = text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)]
            blocks = re.findall(r'```text\n(.*?)\n```', section, re.S)
            if len(blocks) != 1 or 'Control de calidad:' not in blocks[0]:
                raise ValueError('Bloque incompleto: ' + identifier)
            if f'<a id="{identifier.lower()}"></a>' not in text:
                raise ValueError('Ancla ausente: ' + identifier)
            body = blocks[0]
            entries.append({'id': identifier, 'title': title, 'category': path.stem,
                            'mode': 'web' if path.parent.name == 'web' else 'codigo-svg' if identifier == 'LOG-04' else 'edicion' if path.stem in {'edicion-fotos', 'efectos-visuales'} else 'generacion',
                            'path': path.relative_to(ROOT).as_posix(), 'anchor': identifier.lower(),
                            'variables': sorted(set(re.findall(r'\{\{([a-z0-9_]+)\}\}', body)))})
        categories.append({'slug': path.stem, 'title': text.splitlines()[0].removeprefix('# '),
                           'path': path.relative_to(ROOT).as_posix(), 'prompts': entries})
    return {'version': 1, 'language': 'es', 'new_prompt_count': len(ids),
            'category_count': len(categories), 'categories': categories}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    result = build()
    if result['new_prompt_count'] != 64 or result['category_count'] != 15:
        raise ValueError('Se esperan 64 prompts y 15 categorías; revisar inventario y documentación')
    target = ROOT / 'prompts/creative/catalog.json'
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        if not target.exists() or target.read_text(encoding='utf-8') != output:
            raise ValueError('Índice desactualizado; regenerar sin --check')
    else:
        target.write_text(output, encoding='utf-8')
    print(json.dumps({'prompts': result['new_prompt_count'], 'categories': result['category_count'], 'mode': 'check' if args.check else 'build'}))


if __name__ == '__main__':
    main()
