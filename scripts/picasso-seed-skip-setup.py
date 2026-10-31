#!/usr/bin/env python3
"""Mark Setup as done in a copy of the Data seed for the selected iOS userland.

  picasso-seed-skip-setup.py BASE.dbr OUTPUT.dbr [--no-auto-dim]

Runs the upstream scripts/seed-data-skip-setup.py with this board's userland build and version
(picasso_target) instead of the iPadOS 17.7.11 / 21H461 pair it carries. com.apple.migration's
LastSystemVersion must name the system that boots: a mismatch makes the data migrator run on every
boot before SpringBoard can show anything. Everything else is the upstream tool unchanged.
"""
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import picasso_target as target


def main():
    spec = importlib.util.spec_from_file_location('seed_data_skip_setup', HERE / 'seed-data-skip-setup.py')
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    tool.BUILD, tool.VERSION = target.BUILD, target.VERSION
    print(f'picasso: Setup marked done for {target.PRODUCT} {target.VERSION} ({target.BUILD})')
    tool.main()


if __name__ == '__main__':
    main()
