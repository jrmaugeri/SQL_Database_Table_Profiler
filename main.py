#!/usr/bin/env python3
"""
Database Table Profiler - Main Application Entry Point

A robust, modular Python application for profiling database tables and generating
comprehensive Excel reports with metadata, statistics, and relationship analysis.

Supports:
- Microsoft SQL Server and Oracle databases
- Raw data profiling (name-based relationship inference)
- Defined constraints profiling (explicit FK relationships)

Usage:
    python main.py
"""

import sys
from config import (
    APP_NAME, APP_VERSION, DatabaseType, ProfilingStrategy,
    MSG_WELCOME, MSG_SELECT_DB, MSG_SELECT_STRATEGY
)
from database.connection import (
    MSSQLConnection, OracleConnection, PostgreSQLConnection, get_schema_name
)
from profiling.raw_data import RawDataProfiler
from profiling.defined_constraints import DefinedConstraintsProfiler
from utils.helpers import print_banner


def get_user_database_choice() -> DatabaseType:
    """
    Prompt user to select database type.
    
    Returns:
        DatabaseType: Selected database type
    """
    while True:
        try:
            choice = input(MSG_SELECT_DB).strip()
            if choice == '1':
                return DatabaseType.MSSQL
            elif choice == '2':
                return DatabaseType.ORACLE
            elif choice == '3':
                return DatabaseType.POSTGRESQL
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")


def get_user_strategy_choice() -> ProfilingStrategy:
    """
    Prompt user to select profiling strategy.
    
    Returns:
        ProfilingStrategy: Selected profiling strategy
    """
    while True:
        try:
            choice = input(MSG_SELECT_STRATEGY).strip()
            if choice == '1':
                return ProfilingStrategy.RAW_DATA
            elif choice == '2':
                return ProfilingStrategy.DEFINED_CONSTRAINTS
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")


def establish_mssql_connection():
    """
    Establish Microsoft SQL Server connection.
    
    Returns:
        Tuple of (connection, database_identifier) or (None, None) on failure
    """
    print("\n--- Microsoft SQL Server Connection ---")
    conn, server, port, database = MSSQLConnection.get_connection_interactive()
    
    if conn is None:
        return None, None
    
    print(f"✅ Connected to SQL Server: {server}:{port}/{database}")
    return conn, database


def establish_oracle_connection():
    """
    Establish Oracle database connection.
    
    Returns:
        Connection object or None on failure
    """
    print("\n--- Oracle Database Connection ---")
    conn, user, password, dsn = OracleConnection.get_connection_interactive()
    
    if conn is None:
        return None
    
    print(f"✅ Connected to Oracle: {dsn} (user: {user})")
    return conn


def establish_postgresql_connection():
    """
    Establish PostgreSQL database connection.
    
    Returns:
        Tuple of (connection, database_identifier) or (None, None) on failure
    """
    print("\n--- PostgreSQL Database Connection ---")
    conn, host, port, database, user, password = PostgreSQLConnection.get_connection_interactive()
    
    if conn is None:
        return None, None
    
    print(f"✅ Connected to PostgreSQL: {host}:{port}/{database} (user: {user})")
    return conn, database


def get_schema_name_from_user(conn, db_type: DatabaseType) -> str:
    """
    Get schema name from user (or automatically detect for some databases).
    
    Args:
        conn: Database connection
        db_type: Type of database
    
    Returns:
        Schema name or None
    """
    try:
        if db_type == DatabaseType.MSSQL:
            schema = input("Enter target schema name: ").strip()
            if not schema:
                print("Schema name cannot be empty.")
                return None
            return schema
        elif db_type == DatabaseType.ORACLE or db_type == DatabaseType.POSTGRESQL:
            # Try to auto-detect current schema
            cursor = conn.cursor()
            schema = get_schema_name(cursor, db_type)
            cursor.close()
            
            if schema:
                print(f"ℹ Current schema: {schema}")
                confirm = input("Use this schema? (y/n): ").strip().lower()
                if confirm in ('y', 'yes'):
                    return schema
                else:
                    schema = input("Enter target schema name: ").strip()
                    if not schema:
                        print("Schema name cannot be empty.")
                        return None
                    return schema
            return None
    except Exception as e:
        print(f"Error getting schema name: {e}")
        return None


def execute_profiling(
    conn,
    db_type: DatabaseType,
    strategy: ProfilingStrategy,
    schema_name: str,
    database_name: str = None
) -> bool:
    """
    Execute the profiling workflow.
    
    Args:
        conn: Database connection
        db_type: Type of database
        strategy: Profiling strategy to use
        schema_name: Schema to profile
        database_name: Database name (for output file naming)
    
    Returns:
        True if successful, False otherwise
    """
    try:
        cursor = conn.cursor()
        
        # Select profiler based on strategy
        if strategy == ProfilingStrategy.RAW_DATA:
            profiler = RawDataProfiler(db_type, cursor, schema_name, database_name)
        else:  # DEFINED_CONSTRAINTS
            profiler = DefinedConstraintsProfiler(db_type, cursor, schema_name, database_name)
        
        # Execute profiling
        profiler.profile()
        
        return True
    except Exception as e:
        print(f"Profiling failed: {e}")
        return False
    finally:
        try:
            cursor.close()
        except:
            pass


def main() -> int:
    """
    Main application entry point.
    
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    # Display welcome banner
    print_banner(f"{APP_NAME} v{APP_VERSION}")
    
    try:
        # Step 1: Get database type from user
        db_type = get_user_database_choice()
        
        # Step 2: Establish database connection
        if db_type == DatabaseType.MSSQL:
            conn, db_id = establish_mssql_connection()
            if conn is None:
                print("Failed to connect to SQL Server.")
                return 1
            schema_name = get_schema_name_from_user(conn, db_type)
        elif db_type == DatabaseType.ORACLE:
            conn = establish_oracle_connection()
            if conn is None:
                print("Failed to connect to Oracle.")
                return 1
            db_id = None  # Oracle doesn't have explicit database selection
            schema_name = get_schema_name_from_user(conn, db_type)
        else:  # POSTGRESQL
            conn, db_id = establish_postgresql_connection()
            if conn is None:
                print("Failed to connect to PostgreSQL.")
                return 1
            schema_name = get_schema_name_from_user(conn, db_type)
        
        if not schema_name:
            print("Invalid schema name.")
            return 1
        
        # Step 3: Get profiling strategy from user
        strategy = get_user_strategy_choice()
        
        # Step 4: Execute profiling
        print(f"\n{'='*60}")
        print(f"Configuration:")
        print(f"  Database: {db_type.value.upper()}")
        print(f"  Schema: {schema_name}")
        print(f"  Strategy: {strategy.value.replace('_', ' ').title()}")
        print(f"{'='*60}")
        
        confirm = input("\nProceed with profiling? (y/n): ").strip().lower()
        if confirm not in ('y', 'yes'):
            print("Operation cancelled.")
            return 0
        
        success = execute_profiling(conn, db_type, strategy, schema_name, db_id)
        
        if success:
            print(f"\n✅ Profiling completed successfully!")
            return 0
        else:
            return 1
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return 1
    finally:
        try:
            if 'conn' in locals() and conn:
                conn.close()
                print("✓ Database connection closed.")
        except:
            pass


if __name__ == "__main__":
    sys.exit(main())
