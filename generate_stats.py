#!/usr/bin/env python3
"""
Script para generar estadísticas del Glosario de Programación
"""

import re
import json
from datetime import datetime
from pathlib import Path

def count_terms_in_section(content, section_emoji):
    """Cuenta los términos en una sección específica"""
    pattern = f"## {section_emoji}.*?(?=## |$)"
    section_match = re.search(pattern, content, re.DOTALL)
    
    if section_match:
        section_content = section_match.group(0)
        terms = re.findall(r"### (?!.*📚)", section_content)
        return len(terms)
    return 0

def count_code_examples(content):
    """Cuenta los ejemplos de código por lenguaje"""
    languages = {
        'javascript': len(re.findall(r'```javascript', content, re.IGNORECASE)),
        'python': len(re.findall(r'```python', content, re.IGNORECASE)),
        'html': len(re.findall(r'```html', content, re.IGNORECASE)),
        'css': len(re.findall(r'```css', content, re.IGNORECASE)),
        'bash': len(re.findall(r'```bash', content, re.IGNORECASE)),
        'json': len(re.findall(r'```json', content, re.IGNORECASE)),
    }
    return languages

def analyze_content_quality(content):
    """Analiza la calidad del contenido"""
    # Contar definiciones
    definitions = len(re.findall(r'\*\*Definición:\*\*', content))
    
    # Contar ejemplos prácticos
    examples = len(re.findall(r'\*\*Ejemplo:\*\*', content))
    
    # Contar ejemplos de código
    code_examples = len(re.findall(r'```\w+', content))
    
    # Calcular ratio de calidad
    quality_ratio = {
        'definitions_per_term': 0,
        'examples_per_term': 0,
        'code_per_term': 0
    }
    
    total_terms = len(re.findall(r'### (?!.*📚)', content))
    
    if total_terms > 0:
        quality_ratio['definitions_per_term'] = round(definitions / total_terms, 2)
        quality_ratio['examples_per_term'] = round(examples / total_terms, 2)
        quality_ratio['code_per_term'] = round(code_examples / total_terms, 2)
    
    return quality_ratio

def generate_stats():
    """Genera las estadísticas completas del glosario"""
    
    # Buscar archivo README.md
    readme_paths = [
        Path('README.md'),
        Path('../README.md'),
        Path('../../README.md')
    ]
    
    readme_path = None
    for path in readme_paths:
        if path.exists():
            readme_path = path
            break
    
    if not readme_path:
        print("❌ No se encontró el archivo README.md")
        return
    
    # Leer contenido
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Estadísticas básicas
    total_terms = len(re.findall(r'### (?!.*📚)', content))
    total_words = len(content.split())
    total_chars = len(content)
    
    # Términos por categoría
    categories = {
        'Conceptos Fundamentales': count_terms_in_section(content, '🏛️'),
        'POO': count_terms_in_section(content, '📦'),
        'Web y Redes': count_terms_in_section(content, '🌐'),
        'Hardware y Sistemas': count_terms_in_section(content, '🖥️'),
        'Tipos de Datos': count_terms_in_section(content, '🧮'),
        'Sintaxis de Código': count_terms_in_section(content, '✍️'),
        'Seguridad y Errores': count_terms_in_section(content, '🐛')
    }
    
    # Ejemplos de código
    code_examples = count_code_examples(content)
    total_code_examples = sum(code_examples.values())
    
    # Análisis de calidad
    quality = analyze_content_quality(content)
    
    # Estadísticas compiladas
    stats = {
        'general': {
            'total_terms': total_terms,
            'total_words': total_words,
            'total_characters': total_chars,
            'average_words_per_term': round(total_words / total_terms, 2) if total_terms > 0 else 0,
            'last_updated': datetime.now().isoformat()
        },
        'categories': categories,
        'code_examples': {
            'by_language': code_examples,
            'total': total_code_examples,
            'average_per_term': round(total_code_examples / total_terms, 2) if total_terms > 0 else 0
        },
        'quality_metrics': quality,
        'coverage': {
            'terms_with_definitions': len(re.findall(r'\*\*Definición:\*\*', content)),
            'terms_with_examples': len(re.findall(r'\*\*Ejemplo:\*\*', content)),
            'terms_with_code': len(re.findall(r'```\w+.*?```', content, re.DOTALL))
        }
    }
    
    return stats

def display_stats(stats):
    """Muestra las estadísticas de forma legible"""
    
    print("📊 ESTADÍSTICAS DEL GLOSARIO DE PROGRAMACIÓN")
    print("=" * 50)
    
    # Estadísticas generales
    general = stats['general']
    print(f"\n📈 GENERALES:")
    print(f"   📖 Total de términos: {general['total_terms']}")
    print(f"   📝 Total de palabras: {general['total_words']:,}")
    print(f"   📄 Total de caracteres: {general['total_characters']:,}")
    print(f"   📊 Promedio palabras por término: {general['average_words_per_term']}")
    
    # Términos por categoría
    categories = stats['categories']
    print(f"\n🏷️ POR CATEGORÍA:")
    for category, count in categories.items():
        percentage = round((count / general['total_terms']) * 100, 1) if general['total_terms'] > 0 else 0
        print(f"   {category}: {count} términos ({percentage}%)")
    
    # Ejemplos de código
    code = stats['code_examples']
    print(f"\n💻 EJEMPLOS DE CÓDIGO:")
    print(f"   Total: {code['total']} ejemplos")
    print(f"   Promedio por término: {code['average_per_term']}")
    for lang, count in code['by_language'].items():
        if count > 0:
            print(f"   {lang.capitalize()}: {count}")
    
    # Métricas de calidad
    quality = stats['quality_metrics']
    print(f"\n⭐ CALIDAD DEL CONTENIDO:")
    print(f"   Definiciones por término: {quality['definitions_per_term']}")
    print(f"   Ejemplos por término: {quality['examples_per_term']}")
    print(f"   Código por término: {quality['code_per_term']}")
    
    # Cobertura
    coverage = stats['coverage']
    print(f"\n📋 COBERTURA:")
    print(f"   Términos con definición: {coverage['terms_with_definitions']}")
    print(f"   Términos con ejemplo: {coverage['terms_with_examples']}")
    print(f"   Términos con código: {coverage['terms_with_code']}")
    
    print(f"\n🕒 Última actualización: {general['last_updated']}")

def main():
    """Función principal"""
    try:
        stats = generate_stats()
        if stats:
            display_stats(stats)
            
            # Guardar en archivo JSON
            with open('glosario-stats.json', 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Estadísticas guardadas en: glosario-stats.json")
        
    except Exception as e:
        print(f"❌ Error al generar estadísticas: {e}")

if __name__ == "__main__":
    main()
