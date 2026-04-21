# Joe's Introduction
## How to Get Started
### Installation

```bash
# Clone or download the repository
cd Table_Profiler

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
python main.py
```

Then follow the interactive prompts to:
1. Select your database type (SQL Server or Oracle)
2. Configure connection details
3. Choose profiling strategy
4. Review and confirm

### SQL Server Example - Defined Constraints
```
$ python main.py

============================================================
Database Table Profiler v1.1.0
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

Enter SQL Server host(default localhost): localhost
Enter port (default 1433): 1433
Enter database name: Joes_local_db

Enter target schema name: dbo

✅ Connected to SQL Server: localhost:1433/Joes_local_db

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
```

## Output Understanding

### Excel Workbook Structure

**Sheet1: Schema Overview**
- Lists all tables and columns in the schema
- Quick reference for database structure

**[Table Name] Sheets**
- Each table gets its own sheet
- Columns organized by information type:
  - **Columns A-G**: Null statistics
  - **Columns I-M**: Relationship data
  - **Columns O-V**: Value profiling

### Understanding the Statistics

**Null Statistics (Columns A-G)**
- ColumnName: Column identifier
- DataType: SQL data type
- TotalRows: Total records in table
- NonNulls: Records with values
- Nulls: Records with NULL
- Blanks: Empty strings (for string columns)
- SpaceOnlyBlanks: Strings with only spaces

**Relationships (Columns I-M)**
- FK_Name: Foreign key constraint name
- Child_Table: Table containing the FK
- Child_Column: Column with FK
- Parent_Table: Referenced table
- Parent_Column: Referenced column

**Value Profiling (Columns O-V)**
- ColumnName: Column identifier
- DataType: SQL data type
- MinValue: Minimum value (numeric/date columns)
- MaxValue: Maximum value (numeric/date columns)
- AvgValue: Average value (numeric columns)
- MinLength: Shortest string (string columns)
- MaxLength: Longest string (string columns)
- AvgLength: Average length (string columns)

## Common Tasks

### Task 1: Profile a SQL Server Database
1. Run `python main.py`
2. Choose "1. Microsoft SQL Server"
3. Select "2. Manual Entry"
4. Enter: localhost, 1433, YourDatabase
5. Enter: dbo (or your schema)
6. Choose "2. Defined Constraints"
7. Confirm

**Result**: Excel workbook with complete schema analysis

### Task 2: Compare Raw Data vs Defined Constraints
1. Run profiler twice on same schema:
   - Once with "1. Raw Data"
   - Once with "2. Defined Constraints"
2. Compare relationship columns (I-M)
3. Raw Data shows name-inferred relationships
4. Defined Constraints shows actual DB constraints

### Task 3: Profile Oracle Database
1. Run `python main.py`
2. Choose "2. Oracle"
3. Enter credentials: user, password
4. Enter DSN: hostname:1521/service_name
5. Press Enter to use current schema or enter custom
6. Choose profiling strategy
7. Confirm

**Result**: Excel workbook with Oracle schema analysis

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| **Cannot connect to SQL Server** | Verify ODBC Driver 17: `odbcinst -j` |
| **Cannot connect to Oracle** | Test DSN format: `hostname:1521/service` |
| **Excel file won't open** | Update openpyxl: `pip install --upgrade openpyxl` |
| **Empty relationship columns** | Try "1. Raw Data" strategy if DB lacks constraints |
| **Permission denied error** | Verify user has SELECT on system tables |
| **Process is very slow** | Large databases take longer; consider smaller schemas |

## Performance Tips

- **First run**: May take longer (establishing connections)
- **Large tables**: 1000+ column tables take more time
- **Network latency**: Local databases faster than remote
- **Batch processing**: Profile one schema at a time


# 💻 Supported Databases

| Database | Status | Connection | Notes |
|----------|--------|-----------|-------|
| Microsoft SQL Server | ✅ Full | ODBC Driver 17 | Complete feature support |
| Oracle Database | ✅ Full | python-oracledb | Raw data strategy fully supported |

## 🎛️ Profiling Strategies

### 1. Raw Data Profiling
- **Infers relationships** based on column naming patterns
- Looks for columns ending in `_ID` as foreign key candidates
- Useful for databases without explicit constraints
- Works well with legacy systems

### 2. Defined Constraints Profiling
- **Extracts relationships** from database-defined foreign keys
- Uses explicit primary key/foreign key constraints
- More accurate for properly designed schemas
- Direct constraint extraction from system metadata

## 📊 Output

Generates an Excel workbook with:

- **Sheet1**: Schema overview (all tables and columns)
- **Per-table sheets**: 
  - Null/non-null statistics
  - Relationship information
  - Column value profiles (min/max/length stats)

## 🏗️ Architecture

```
Table_Profiler/
├── main.py                    # Application entry point & UI
├── config.py                  # Configuration & constants
│
├── database/                  # Database connectivity layer
│   ├── connection.py         # Connection management
│   ├── mssql_queries.py      # SQL Server queries
│   └── oracle_queries.py     # Oracle queries
│
├── profiling/                 # Profiling engine
│   ├── profiler.py           # Base profiler class
│   ├── raw_data.py           # Raw data strategy
│   └── defined_constraints.py # Constraints strategy
│
└── utils/                     # Utilities
    └── helpers.py            # Helper functions
```

## 🔧 System Requirements

- **Python**: 3.7 or higher
- **SQL Server**: ODBC Driver 17 for SQL Server
- **Oracle**: Oracle client libraries + python-oracledb
- **Disk**: ~50 MB for dependencies
- **Memory**: 100+ MB available

## 📦 Dependencies

- `pyodbc` - SQL Server connectivity
- `oracledb` - Oracle connectivity
- `pandas` - Data manipulation
- `openpyxl` - Excel generation
- `numpy` - Numerical operations

See [requirements.txt](requirements.txt) for versions.

## 💡 Use Cases

**Database Documentation**
```bash
python main.py
# → Get instant schema documentation in Excel
```

**Data Quality Assessment**
```bash
python main.py
# → Identify null values, blanks, and data patterns
```

**Schema Validation**
```bash
# Compare expected vs actual table structures
# Verify all expected relationships exist
```

**ETL/ELT Planning**
```bash
# Understand source schema before transformation
# Identify data type mismatches or issues
```

## 🐛 Troubleshooting

**Connection issues?**
- Verify database driver installation
- Check network connectivity
- Confirm credentials and permissions

**Excel file won't open?**
- Update openpyxl: `pip install --upgrade openpyxl`
- Ensure sufficient disk space
- Check file isn't locked

See [README.md](README.md#troubleshooting) for detailed troubleshooting guide.


## 📄 License

MIT License - See LICENSE file for details.

## 🎓 Learning Resources

- [Architecture & Design Patterns](README.md#architecture) - Understand the modular design
- [Extending the Application](README.md#advanced-usage) - Add custom profiling logic
- [Adding Database Support](CONTRIBUTING.md#adding-database-support) - Support new databases
- [Developer Guide](CONTRIBUTING.md) - Complete development guide

