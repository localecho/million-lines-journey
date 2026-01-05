#!/usr/bin/env python3
"""
Domain Distribution Visualization
From: I Coded a Million Lines of Code and This Is What Happened

Generates a visual breakdown of the 555-project codebase across 6 major domains.
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Codebase metrics
DOMAINS = {
    'Trading & Finance': {
        'projects': 15,
        'color': '#2ecc71',
        'icon': '$',
        'key_project': 'algo-trading-workshop'
    },
    'Music & Creative': {
        'projects': 8,
        'color': '#9b59b6',
        'icon': '~',
        'key_project': 'foot-pedal-music'
    },
    'AI Agents & Automation': {
        'projects': 12,
        'color': '#3498db',
        'icon': '>',
        'key_project': 'expert-bridge-platform'
    },
    'Data & Analytics': {
        'projects': 8,
        'color': '#e74c3c',
        'icon': '#',
        'key_project': 'ascii_constellation'
    },
    'RAG & Knowledge': {
        'projects': 4,
        'color': '#f39c12',
        'icon': '?',
        'key_project': 'RAGS-Suite'
    },
    'Specialized Tools': {
        'projects': 20,
        'color': '#1abc9c',
        'icon': '*',
        'key_project': 'bitcoin-book-cipher-hunter'
    }
}

TOTAL_METRICS = {
    'python_files': 5471,
    'lines_of_code': 172984,
    'definitions': 105553,
    'projects': 555,
    'langgraph_files': 40,
    'async_patterns': 8011
}


def create_domain_pie():
    """Create domain distribution pie chart"""
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')

    labels = list(DOMAINS.keys())
    sizes = [d['projects'] for d in DOMAINS.values()]
    colors = [d['color'] for d in DOMAINS.values()]

    # Create pie with styling
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        colors=colors,
        autopct='%1.0f%%',
        startangle=90,
        explode=[0.02] * len(sizes),
        textprops={'color': 'white', 'fontsize': 11}
    )

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax.set_title(
        'Domain Distribution\n555 Projects Across 6 Domains',
        fontsize=16,
        color='white',
        fontweight='bold',
        pad=20
    )

    plt.tight_layout()
    plt.savefig('domain_pie.png', dpi=150, facecolor='#1a1a2e', edgecolor='none')
    plt.close()
    print("Saved: domain_pie.png")


def create_metrics_bar():
    """Create key metrics horizontal bar chart"""
    fig, ax = plt.subplots(figsize=(14, 8), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')

    metrics = [
        ('Python Files', TOTAL_METRICS['python_files'], '#3498db'),
        ('Lines of Code (K)', TOTAL_METRICS['lines_of_code'] / 1000, '#e74c3c'),
        ('Definitions (K)', TOTAL_METRICS['definitions'] / 1000, '#2ecc71'),
        ('Async Patterns (K)', TOTAL_METRICS['async_patterns'] / 1000, '#9b59b6'),
        ('Projects', TOTAL_METRICS['projects'], '#f39c12'),
        ('LangGraph Files', TOTAL_METRICS['langgraph_files'], '#1abc9c'),
    ]

    y_pos = np.arange(len(metrics))
    values = [m[1] for m in metrics]
    colors = [m[2] for m in metrics]
    labels = [m[0] for m in metrics]

    bars = ax.barh(y_pos, values, color=colors, height=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=12, color='white')
    ax.set_xlabel('Count / Thousands', fontsize=12, color='white')

    # Add value labels
    for bar, val in zip(bars, values):
        width = bar.get_width()
        ax.text(
            width + max(values) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f'{val:,.0f}',
            ha='left',
            va='center',
            fontsize=11,
            color='white',
            fontweight='bold'
        )

    ax.set_title(
        'Codebase Metrics at a Glance',
        fontsize=16,
        color='white',
        fontweight='bold',
        pad=20
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(colors='white')
    ax.set_xlim(0, max(values) * 1.15)

    plt.tight_layout()
    plt.savefig('metrics_bar.png', dpi=150, facecolor='#1a1a2e', edgecolor='none')
    plt.close()
    print("Saved: metrics_bar.png")


def create_evolution_timeline():
    """Create technology evolution timeline"""
    fig, ax = plt.subplots(figsize=(16, 6), facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')

    phases = [
        {
            'name': 'Foundation',
            'years': '2019-2021',
            'x': 1,
            'tech': ['Python basics', 'Single-file scripts', 'MIDI notation']
        },
        {
            'name': 'Integration',
            'years': '2022-2023',
            'x': 2,
            'tech': ['FastAPI (861+)', 'Databases', 'Multi-file projects']
        },
        {
            'name': 'Sophistication',
            'years': '2024-2025',
            'x': 3,
            'tech': ['LangGraph (40+)', 'Multi-agent', 'Cross-domain transfer']
        }
    ]

    # Draw timeline
    ax.axhline(y=0.5, color='white', linewidth=2, alpha=0.5)

    for phase in phases:
        # Circle marker
        ax.scatter(phase['x'], 0.5, s=300, c='#3498db', zorder=5, edgecolors='white', linewidths=2)

        # Phase name above
        ax.text(phase['x'], 0.7, phase['name'], ha='center', va='bottom',
                fontsize=14, color='white', fontweight='bold')
        ax.text(phase['x'], 0.62, phase['years'], ha='center', va='bottom',
                fontsize=10, color='#888888')

        # Tech stack below
        for i, tech in enumerate(phase['tech']):
            ax.text(phase['x'], 0.35 - i*0.08, f'* {tech}', ha='center', va='top',
                   fontsize=10, color='#cccccc')

    ax.set_xlim(0.3, 3.7)
    ax.set_ylim(0, 1)
    ax.axis('off')

    ax.set_title(
        'Technology Evolution: 5+ Years of Growth',
        fontsize=16,
        color='white',
        fontweight='bold',
        pad=20
    )

    plt.tight_layout()
    plt.savefig('evolution_timeline.png', dpi=150, facecolor='#1a1a2e', edgecolor='none')
    plt.close()
    print("Saved: evolution_timeline.png")


def create_ascii_dashboard():
    """Create ASCII art dashboard for terminal display"""
    dashboard = """
+============================================================================+
|                    CODEBASE METRICS DASHBOARD                               |
|                    172,984 Lines Across 555 Projects                        |
+============================================================================+

  SCALE                           DOMAINS
  -----                           -------

  Python Files:     5,471         Trading & Finance   ########### 15
  Lines of Code:  172,984         Music & Creative    ######      8
  Definitions:    105,553         AI Agents           ########    12
  Projects:           555         Data & Analytics    ######      8
  Async Patterns:   8,011         RAG & Knowledge     ###         4
  LangGraph Files:     40         Specialized         ########### 20

+----------------------------------------------------------------------------+

  TECHNOLOGY STACK                LOC BY PHASE
  ----------------                ------------

  FastAPI        [=======] 861    Foundation (2019-21)   [==]      ~20K
  LangGraph      [=]        40    Integration (2022-23)  [=====]   ~50K
  NumPy/Pandas   [=====] 10,499   Sophistication (24-25) [========] ~100K
  Async Patterns [======] 8,011

+----------------------------------------------------------------------------+

  TOP 5 FILES BY LOC                           DOMAIN ICONS
  -------------------                          ------------

  1. executive_report_generator.py   2,699     $  Trading
  2. guggenheim_proposal.py          1,439     ~  Music
  3. advanced_grant_optimization.py  1,310     >  AI Agents
  4. cultural_impact_predictor.py    1,237     #  Data
  5. clair_continuous_improvement.py 1,193     ?  RAG
                                               *  Specialized

+============================================================================+
|              "The code you write today becomes the patterns               |
|                          you apply tomorrow."                              |
+============================================================================+
"""
    print(dashboard)
    with open('ascii_dashboard.txt', 'w') as f:
        f.write(dashboard)
    print("\nSaved: ascii_dashboard.txt")


if __name__ == '__main__':
    print("Generating visualizations...\n")

    try:
        create_domain_pie()
        create_metrics_bar()
        create_evolution_timeline()
    except ImportError:
        print("Note: matplotlib not available, skipping PNG generation")

    # ASCII always works
    create_ascii_dashboard()

    print("\nDone! Visualizations generated.")
