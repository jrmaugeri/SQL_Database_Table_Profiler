"""
Configuration and Constants for Table Profiler Application

This module contains all configuration constants, enums, and default settings
used throughout the Table Profiler application.
"""

from enum import Enum

# Application metadata
APP_NAME = "Database Table Profiler"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Profile database tables to generate comprehensive Excel reports with metadata, statistics, and relationships"

# Database types
class DatabaseType(Enum):
    """Supported database systems"""
    MSSQL = "mssql"
    ORACLE = "oracle"
    POSTGRESQL = "postgresql"

# Profiling strategies
class ProfilingStrategy(Enum):
    """Profiling approaches"""
    RAW_DATA = "raw_data"
    DEFINED_CONSTRAINTS = "defined_constraints"

# SQL Server defaults
MSSQL_DEFAULT_HOST = "IQSSQLTEST"
MSSQL_DEFAULT_PORT = "1433"
MSSQL_DRIVER = "ODBC Driver 17 for SQL Server"

# Column data types to skip (BLOB/CLOB equivalents)
MSSQL_SKIP_TYPES = ("TEXT", "IMAGE", "VARBINARY", "BINARY", "XML")
ORACLE_SKIP_TYPES = ("CLOB", "BLOB")
POSTGRESQL_SKIP_TYPES = ("BYTEA", "TEXT", "JSON", "JSONB")

# String data types for blank detection
MSSQL_STRING_TYPES = ("VARCHAR", "NVARCHAR", "CHAR", "NCHAR")
ORACLE_STRING_TYPES = ("VARCHAR2", "NVARCHAR2", "CHAR", "NCHAR")
POSTGRESQL_STRING_TYPES = ("VARCHAR", "CHAR", "TEXT")

# Numeric data types
MSSQL_NUMERIC_TYPES = ("INT", "BIGINT", "SMALLINT", "TINYINT", "DECIMAL", "NUMERIC", "FLOAT", "REAL", "MONEY", "SMALLMONEY")
ORACLE_NUMERIC_TYPES = ("NUMBER", "FLOAT", "BINARY_FLOAT", "BINARY_DOUBLE", "INTEGER")
POSTGRESQL_NUMERIC_TYPES = ("SMALLINT", "INTEGER", "BIGINT", "DECIMAL", "NUMERIC", "REAL", "DOUBLE PRECISION")

# Date data types
MSSQL_DATE_TYPES = ("DATE", "DATETIME", "SMALLDATETIME", "DATETIME2", "DATETIMEOFFSET", "TIME")
ORACLE_DATE_TYPES = ("DATE", "TIMESTAMP", "TIMESTAMP WITH TIME ZONE", "TIMESTAMP WITH LOCAL TIME ZONE")
POSTGRESQL_DATE_TYPES = ("DATE", "TIME", "TIMESTAMP", "TIMESTAMPTZ", "TIMETZ")

# Excel constraints
EXCEL_MAX_SHEET_NAME_LENGTH = 31

# Output messages
MSG_WELCOME = f"\n{'='*60}\n{APP_NAME} v{APP_VERSION}\n{'='*60}\n"
MSG_SELECT_DB = "\nSelect Database Type:\n  1. Microsoft SQL Server\n  2. Oracle\n  3. PostgreSQL\nEnter choice (1, 2, or 3): "
MSG_SELECT_STRATEGY = "\nSelect Profiling Strategy:\n  1. Raw Data (name-based relationship inference)\n  2. Defined Constraints (explicit FK relationships)\nEnter choice (1 or 2): "
MSG_CONNECTION_MODE = "\nConnect using:\n  1. DSN (Data Source Name)\n  2. Manual Entry\nEnter choice (1 or 2): "

# Status symbols
SYMBOL_SUCCESS = "✔"
SYMBOL_SKIP = "⏭"
SYMBOL_LINK = "🔗"
SYMBOL_PROFILE = "📊"
SYMBOL_INFO = "ℹ"
SYMBOL_WARNING = "⚠"
SYMBOL_COMPLETE = "✅"
