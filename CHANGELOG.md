# Changelog

All notable changes to the Database Table Profiler project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Oracle value profiling (min/max/avg/length statistics)
- Automated test suite (unit and integration tests)
- PostgreSQL database support
- MySQL/MariaDB database support
- Progress indicators for long-running operations
- Configuration file support (.ini/.yaml)
- Batch schema processing
- Database view profiling
- Data lineage tracking

## [1.0.0] - 2026-01-20

### Added
- Initial release of modular application architecture
- **Database Support**:
  - Microsoft SQL Server via ODBC Driver 17
  - Oracle Database via python-oracledb
- **Profiling Strategies**:
  - Raw Data: Name-based relationship inference (columns ending in _ID)
  - Defined Constraints: Explicit foreign key relationships
- **Features**:
  - Complete schema metadata extraction
  - Null/non-null/blank/space-only statistics per column
  - Foreign key relationship discovery
  - Column value profiling (numeric: min/max/avg; string: length stats)
  - Excel workbook generation with multiple sheets
  - Interactive command-line interface
  - User-friendly error messages with emojis
- **Documentation**:
  - Comprehensive README with examples
  - Setup and installation guide
  - Architecture and design patterns documentation
  - Troubleshooting section
  - Contributing guidelines
- **Code Quality**:
  - Modular architecture with clear separation of concerns
  - Strategy pattern for pluggable profiling approaches
  - Comprehensive docstrings and type hints
  - Configuration management via config.py
  - Helper utilities for common operations
- **Project Files**:
  - requirements.txt for dependency management
  - setup.py for package installation
  - .gitignore for version control
  - CONTRIBUTING.md for developer guidelines

### Technical Details
- Python 3.7+ compatibility
- Type hints throughout codebase
- Abstract base classes for extensibility
- Database abstraction layer for easy multi-DB support
- Query templating system for maintainability

## Migration Notes

### From Original Files
The application consolidates functionality from four separate scripts:

1. `table_profiler_ms_raw_data.py` → `profiling/raw_data.py` (MSSQL)
2. `table_profiler_ms_raw_definedconstraints.py` → `profiling/defined_constraints.py` (MSSQL)
3. `table_profiler_oracle_raw_data.py` → `profiling/raw_data.py` (Oracle)
4. `table_profiler_oracle_defined_constraints.py` → `profiling/defined_constraints.py` (Oracle)

**Key Improvements:**
- Unified interface for both database types
- Single entry point instead of four separate scripts
- Shared utilities and helpers reduce code duplication
- Consistent error handling and logging
- Easier maintenance and feature additions

### Breaking Changes
- None (first release of modular version)

### Deprecated
- Original four separate Python scripts (functionality preserved in unified application)

---

## Version Format
- Major: Breaking changes or significant feature additions
- Minor: New features, non-breaking improvements
- Patch: Bug fixes, documentation updates

## Reporting Issues
Please report bugs and feature requests on the GitHub issue tracker with:
- Clear description
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Environment details (Python version, database type, OS)
