# Contributing to Database Table Profiler

Thank you for your interest in contributing! This document provides guidelines and information for developers.

## Code of Conduct

- Be respectful and professional
- Provide constructive feedback
- Help others learn and improve
- Report issues responsibly

## Getting Started

### Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pylint pytest black
   ```

4. Set up your IDE (VSCode recommended)

### Architecture Overview

The application follows a modular, layered architecture:

- **UI Layer** (`main.py`): User interaction and orchestration
- **Configuration Layer** (`config.py`): Constants and enums
- **Database Layer** (`database/`): Connection management and queries
- **Business Logic Layer** (`profiling/`): Profiling strategies
- **Utility Layer** (`utils/`): Shared functions

### Key Design Principles

1. **Single Responsibility**: Each module has one clear purpose
2. **Separation of Concerns**: Database, business logic, and UI are separate
3. **Extensibility**: New database types or strategies can be added easily
4. **Configuration Management**: All magic strings and constants in one place
5. **Error Handling**: Graceful degradation and informative error messages

## Making Changes

### Before You Start

1. Create an issue to discuss your idea
2. Wait for feedback from maintainers
3. For large changes, submit a design proposal first

### Development Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/description-of-feature
   ```

2. Make your changes following the style guide
3. Test thoroughly (manual testing for now)
4. Run linters:
   ```bash
   pylint database/ profiling/ utils/ main.py config.py
   black --check database/ profiling/ utils/ main.py config.py
   ```

5. Update documentation if needed
6. Commit with clear messages:
   ```bash
   git commit -m "Add feature: Clear description of change"
   ```

7. Push to your fork and create a pull request

### Code Style

- Follow PEP 8 for Python code
- Use type hints for function parameters and returns
- Maximum line length: 100 characters
- Use docstrings for all public functions and classes
- Use meaningful variable names

Example:
```python
def get_table_names(self) -> List[str]:
    """
    Get all table names from the current schema.
    
    Returns:
        List of table names sorted alphabetically
    
    Raises:
        RuntimeError: If database connection is not established
    """
    try:
        if self.db_type == DatabaseType.MSSQL:
            query = MSSQLQueries.get_schema_tables()
            self.cursor.execute(query, (self.schema_name,))
        else:
            query = OracleQueries.get_schema_tables()
            self.cursor.execute(query)
        
        return [row[0] for row in self.cursor.fetchall()]
    except Exception as e:
        self.log_warning(f"Failed to get table names: {e}")
        return []
```

### Testing

While we don't have automated tests yet, please:

1. Test your changes thoroughly manually
2. Create test cases if implementing new features
3. Test edge cases (empty tables, special characters, etc.)
4. Verify on both SQL Server and Oracle if applicable

### Documentation

Update documentation for:
- New features or changes to existing behavior
- New database types or profiling strategies
- API changes or new public functions
- Configuration options

## Adding Database Support

### Steps to Add a New Database Type

1. **Update `config.py`**:
   ```python
   class DatabaseType(Enum):
       MSSQL = "mssql"
       ORACLE = "oracle"
       NEW_DB = "new_db"  # Add new database type
   ```

2. **Create connection class in `database/connection.py`**:
   ```python
   class NewDBConnection(DatabaseConnection):
       @staticmethod
       def get_connection_interactive():
           # Implementation
           pass
   ```

3. **Create query templates in `database/new_db_queries.py`**:
   ```python
   class NewDBQueries:
       @staticmethod
       def get_schema_tables() -> str:
           # Query template
           pass
   ```

4. **Update profilers** to handle new database type in conditionals

5. **Update `main.py`** with new connection option

6. **Test thoroughly** with sample database

7. **Update documentation** with new database support

## Adding Profiling Strategies

### Steps to Add a New Strategy

1. **Update `config.py`**:
   ```python
   class ProfilingStrategy(Enum):
       RAW_DATA = "raw_data"
       DEFINED_CONSTRAINTS = "defined_constraints"
       NEW_STRATEGY = "new_strategy"  # Add new strategy
   ```

2. **Create new profiler in `profiling/`**:
   ```python
   from profiling.profiler import BaseProfiler
   
   class NewStrategyProfiler(BaseProfiler):
       def get_table_names(self) -> List[str]:
           # Implementation
           pass
       
       def profile(self) -> None:
           # Implementation
           pass
   ```

3. **Update `main.py`** to include new strategy in user prompts

4. **Update `README.md`** with strategy description

## Pull Request Process

1. **Update version** in `config.py` and `setup.py` if needed
2. **Write clear PR description** explaining:
   - What problem does this solve?
   - How does it work?
   - What testing was done?
   - Any breaking changes?

3. **Link related issues** using "Fixes #123"
4. **Request review** from maintainers
5. **Address feedback** and update PR as needed

## Reporting Bugs

When reporting bugs, include:

1. **Clear description** of the issue
2. **Steps to reproduce**
3. **Expected vs. actual behavior**
4. **Database type and version**
5. **Python version**
6. **Full error message or traceback**
7. **Sample schema** if applicable (sanitized for privacy)

## Performance Considerations

When making changes, consider:

1. **Query efficiency**: Minimize database round-trips
2. **Memory usage**: Handle large result sets efficiently
3. **User experience**: Provide progress feedback for long operations
4. **Error recovery**: Graceful handling of partial failures

## Future Improvements

High-priority items for contribution:

- [ ] Oracle value profiling (min/max/avg/length)
- [ ] Unit and integration tests
- [ ] Progress indicators for long operations
- [ ] PostgreSQL support
- [ ] MySQL/MariaDB support
- [ ] Batch schema processing
- [ ] Configuration file support
- [ ] Enhanced error messages with troubleshooting tips
- [ ] Support for database views and synonyms
- [ ] Data lineage tracking

## Questions?

Feel free to:
1. Open a discussion issue
2. Comment on existing issues
3. Contact the maintainers

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to make Database Table Profiler better!
