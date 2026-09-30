from pathlib import Path

def write(slug, title, prefix, entries, edit=False, web=False):
    path = Path('prompts') / ('web' if web else 'creative') / (slug + '.md')
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ['# ' + title, '', '[Biblioteca](../README.md) · [Guía de uso](../creative/guia-de-uso.md)', '',
             'Completa las variables y copia el bloque del ID elegido. Adjunta las referencias indicadas.', '']
    for n, (name, body, check) in enumerate(entries, 1):
        identifier = f'{prefix}-{n:02d}'
        if web:
            output = 'Entrega archivos implementados si tienes acceso; si no, código y pasos aplicables. Resume pruebas reales y pendientes. No publiques o despliegues sin autorización para ese entorno.'
        elif edit:
            output = 'Edita la imagen base y entrega una copia en {{formato}} para {{destino}}, conservando el original. Si falta referencia o capacidad, indica el dato o paso necesario; no afirma haber editado sin salida real.'
        else:
            output = 'Genera la imagen en {{formato}} para {{destino}}. Las referencias adjuntas guían únicamente su función indicada. Configura tamaño y cantidad en los controles disponibles. Si una capacidad no existe, explica el paso pendiente; no simula archivos editables o transparencia.'
        lines.extend([f'<a id="{identifier.lower()}"></a>', f'## {identifier} · {name}', '', '```text', body, '', output, '', 'Control de calidad: ' + check, '```', ''])
    path.write_text('\n'.join(lines), encoding='utf-8')
