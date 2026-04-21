# Database Table Profiler

A robust, modular Python application for profiling database tables and generating comprehensive Excel reports with metadata, statistics, and relationship analysis.

## Overview

Database Table Profiler analyzes database schemas to create detailed Excel workbooks containing:

- **Schema Metadata**: Complete listing of all tables and columns
- **Null/Non-Null Statistics**: Count of null, non-null, blank, and space-only values per column
- **Relationship Analysis**: Database foreign key relationships (two strategies)
- **Column Profiling**: Min/max/average values and string length statistics

Supported Databases:
- **Microsoft SQL Server** (via ODBC Driver 17)
- **Oracle Database** (via python-oracledb)
- **PostgreSQL** (via psycopg)

## Features

### Dual Profiling Strategies

#### 1. Raw Data Profiling
- Infers relationships based on column naming patterns
- Looks for columns ending in `_ID` as foreign key candidates
- Useful for databases without explicit constraints or legacy systems
- Name-based matching across tables

#### 2. Defined Constraints Profiling  
- Extracts relationships from database-defined foreign keys
- Uses explicit primary key/foreign key constraints
- More accurate for databases with proper schema design
- Direct constraint extraction from system tables

### Multi-Database Support

#### Microsoft SQL Server
- Connection via DSN or manual entry
- Supports parameterized queries
- Handles all SQL Server data types
- INFORMATION_SCHEMA queries for portability

#### Oracle Database
- EZConnect format or TNS names
- USER_* views for current schema
- Proper quote handling for identifiers
- Support for Oracle-specific data types

#### PostgreSQL
- Connection via host, port, database, user, password
- INFORMATION_SCHEMA queries for schema information
- Support for PostgreSQL-specific data types
- Handles JSON/JSONB and other advanced types

## Installation

### Prerequisites

- Python 3.7+
- Microsoft SQL Server ODBC Driver 17 (for MSSQL connectivity)
- Oracle client libraries (for Oracle connectivity)
- PostgreSQL client libraries (for PostgreSQL connectivity)

### Setup

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify database driver installation:
   ```bash
   # For SQL Server
   odbcinst -j  # Check installed drivers
   
   # For Oracle  
   python -c "import oracledb; print(oracledb.__version__)"
   
   # For PostgreSQL
   python -c "import psycopg; print(psycopg.__version__)"
   ```

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Workflow

The application guides you through a series of prompts:

1. **Select Database Type**
   ```
   1. Microsoft SQL Server
   2. Oracle
   3. PostgreSQL
   ```

2. **Configure Connection**
   - For SQL Server: Choose DSN or manual entry
     - Manual: Server, Port, Database
     - DSN: Data source name
   - For Oracle: Enter username, password, DSN (EZCONNECT format)
   - For PostgreSQL: Enter host, port, database, username, password

3. **Specify Schema**
   - Enter the schema/database name to profile
   - For Oracle, current schema is auto-detected

4. **Select Profiling Strategy**
   ```
   1. Raw Data (name-based relationship inference)
   2. Defined Constraints (explicit FK relationships)
   ```

5. **Confirm and Execute**
   - Review configuration
   - Confirm to proceed with profiling

### Output

Results are saved in an Excel workbook with the following structure:

- **Sheet1**: Schema metadata (all tables and columns)
- **[Table Name]**: For each table:
  - Columns A-G: Null/non-null statistics
  - Columns I-M: Relationship data (ForeignKey/Parent-Child info)
  - Columns O-V: Column profiling (min/max/avg/lengths)

### Example Session

```
============================================================
Database Table Profiler v1.0.0
============================================================

Select Database Type:
  1. Microsoft SQL Server
  2. Oracle
Enter choice (1 or 2): 1

--- Microsoft SQL Server Connection ---

Connect using:
  1. DSN
  2. Manual Entry
Enter choice (1 or 2): 2

Enter SQL Server host(default IQSSQLTEST): localhost
Enter port (default 1433): 1433
Enter database name: MyDatabase

Enter target schema name: dbo

✅ Connected to SQL Server: localhost:1433/MyDatabase

Select Profiling Strategy:
  1. Raw Data (name-based relationship inference)
  2. Defined Constraints (explicit FK relationships)
Enter choice (1 or 2): 2

============================================================
Configuration:
  Database: MSSQL
  Schema: dbo
  Strategy: Defined Constraints
============================================================

Proceed with profiling? (y/n): y

============================================================
Starting Defined Constraints Profiling
============================================================

Output folder: C:\Users\...\MyDatabase
Excel file: C:\Users\...\MyDatabase\MyDatabase.xlsx

✔ Schema information written to Sheet1

Profiling null/non-null statistics...
✔ Stats written for table: Customers
✔ Stats written for table: Orders
...

Extracting defined foreign key relationships...
🔗 Relationships written for table: Orders

✅ Defined constraints profiling complete: C:\Users\...\MyDatabase\MyDatabase.xlsx
```

## Project Structure

```
Table_Profiler/
├── main.py                          # Application entry point
├── config.py                        # Configuration and constants
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── database/                        # Database connectivity layer
│   ├── __init__.py
│   ├── connection.py               # Connection management
│   ├── mssql_queries.py            # MS SQL query templates
│   ├── oracle_queries.py           # Oracle query templates
│   └── postgresql_queries.py       # PostgreSQL query templates
│
├── profiling/                       # Profiling engine
│   ├── __init__.py
│   ├── profiler.py                 # Base profiler class
│   ├── raw_data.py                 # Raw data strategy
│   └── defined_constraints.py      # Defined constraints strategy
│
└── utils/                           # Utilities
    ├── __init__.py
    └── helpers.py                  # Helper functions
```

### Module Responsibilities

- **main.py**: User interface, orchestration, application flow
- **config.py**: Constants, enums, configuration defaults
- **database/**: All database connectivity and query management
  - **connection.py**: Connection establishment and lifecycle
  - **mssql_queries.py**: SQL Server query templates
  - **oracle_queries.py**: Oracle query templates
- **profiling/**: Profiling logic and strategies
  - **profiler.py**: Base class with common profiling logic
  - **raw_data.py**: Name-based relationship inference
  - **defined_constraints.py**: Constraint-based relationship extraction
- **utils/**: Shared utility functions

## Architecture

### Design Patterns

- **Strategy Pattern**: Two profiling strategies (raw data vs. defined constraints)
- **Template Method**: Base profiler with strategy-specific implementations
- **Factory Pattern**: Database-specific query creation
- **Dependency Injection**: Clean separation of concerns

### Key Design Decisions

1. **Modular Structure**: Each component has a single responsibility
2. **Database Abstraction**: Query logic separated by database type
3. **Strategy Pattern**: Pluggable profiling approaches
4. **Configuration as Code**: All constants in one place
5. **Rich Logging**: Emoji-enhanced status messages for user clarity

## Advanced Usage

### Programmatic Usage

```python
from config import DatabaseType, ProfilingStrategy
from database.connection import MSSQLConnection
from profiling.defined_constraints import DefinedConstraintsProfiler

# Establish connection
conn, server, port, db = MSSQLConnection.get_connection_manual(
    server="localhost",
    port="1433",
    database="MyDB"
)

# Create profiler
cursor = conn.cursor()
profiler = DefinedConstraintsProfiler(
    db_type=DatabaseType.MSSQL,
    cursor=cursor,
    schema_name="dbo"
)

# Execute profiling
profiler.profile()

# Cleanup
cursor.close()
conn.close()
```

### Extending the Application

To add custom profiling logic:

1. Extend `BaseProfiler` in `profiling/profiler.py`
2. Implement required abstract methods
3. Update `main.py` to include new strategy option

Example:
```python
class CustomProfiler(BaseProfiler):
    def get_table_names(self) -> List[str]:
        # Custom implementation
        pass
    
    def profile(self) -> None:
        # Custom profiling workflow
        pass
```

## Troubleshooting

### Connection Failures

**SQL Server Connection Error**
```
Connection failed: ('HY000', '[HY000] [Microsoft][ODBC Driver 17 for SQL Server]...')
```
- Verify SQL Server is running
- Check ODBC Driver 17 installation: `odbcinst -j`
- Ensure network connectivity to server
- Verify credentials and database permissions

**Oracle Connection Error**
```
Connection failed - Code 12514: TNS:listener could not resolve SERVICE_NAME given in connect descriptor
```
- Verify DSN format (host:port/service_name)
- Check Oracle listener is running
- Test with SQL*Plus: `sqlplus user/pass@dsn`
- Verify credentials

### Permission Errors

- Ensure user has SELECT privilege on INFORMATION_SCHEMA (SQL Server) or USER_* views (Oracle)
- For foreign key detection, need access to constraint metadata views
- May need DBA assistance for restricted system tables

### Excel File Issues

**"Excel cannot open the file because the file format or file extension is not valid"**
- Ensure openpyxl version is compatible: `pip install --upgrade openpyxl`
- Check disk space availability
- Verify file isn't locked by another process

### Performance

**Profiling is slow**
- Large tables with many columns take longer
- Network latency affects execution
- Consider profiling one schema at a time
- Check database server load

## Development

### Adding a New Database Type

1. Add enum to `DatabaseType` in `config.py`
2. Create connection class in `database/connection.py`
3. Create query module `database/{db_type}_queries.py`
4. Extend profiler classes as needed
5. Update `main.py` with user prompts

### Running Tests

Currently no automated tests. To validate:

1. Create test database with sample schema
2. Run profiler on test schema
3. Verify Excel output structure and data accuracy

## Known Limitations

- Very large databases (1000+ tables) may require extended execution time
- Sheet names limited to 31 characters (Excel constraint)
- Blob/Clob columns are skipped
- Date range analysis limited to Oracle date types without timezone handling

## Contributing

Improvements welcome! Consider:

- Batch processing for large schemas
- Progress indicators for long-running operations
- Unit and integration tests
- Additional database support (MySQL, etc.)

## License

See LICENSE file for details.

## Support

For issues, questions, or suggestions:
1. Review this README and troubleshooting section
2. Check database connectivity separately
3. Verify all required drivers are installed
4. Review console output for detailed error messages

## Version History

### v1.0.0 (Current)
- Initial modular release
- Full MS SQL Server support
- Oracle and PostgreSQL support with raw data and defined constraints
- Two profiling strategies
- Interactive user interface
- Comprehensive documentation

---

**Last Updated**: January 2026  
**Maintained by**: DataForge Development Team
