"""
One-Click Migration Script for Neon Database
Tests your Neon connection, creates relational tables,
and uploads all student CSV records directly to Neon cloud PostgreSQL.
"""
import os
import sys
from dotenv import load_dotenv

# Ensure root directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.neon_manager import NeonDatabaseManager

load_dotenv()


def main():
    print("=" * 65)
    print("   NEON POSTGRESQL DATABASE - ONE-CLICK SETUP & MIGRATION")
    print("=" * 65)

    conn_url = os.getenv("NEON_DATABASE_URL", "").strip()

    if not conn_url or "YOUR_PASSWORD_HERE" in conn_url:
        print("\n[!] NEON_DATABASE_URL not found in .env file.")
        print("Please enter your Neon connection string:")
        print("Example: postgresql://neondb_owner:pass@ep-xyz.us-east-2.aws.neon.tech/neondb?sslmode=require\n")
        conn_url = input("Paste your Neon Connection String: ").strip()

        if not conn_url:
            print("[-] No connection string provided. Aborting.")
            return

        # Save to .env
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(f"NEON_DATABASE_URL={conn_url}\n")
        print(f"[+] Saved connection string to {env_path}")

    # Initialize Neon Manager
    neon = NeonDatabaseManager(conn_url)

    # 1. Test Connection
    print("\n[Step 1/3] Testing connection to Neon Cloud...")
    test_res = neon.test_connection()
    if test_res["status"] != "Success":
        print(f"[-] Connection Error: {test_res['message']}")
        return
    print(f"[+] {test_res['message']}")
    print(f"    - Database Name: {test_res['database']}")
    print(f"    - Database User: {test_res['user']}")
    print(f"    - Postgres Version: {test_res['version'][:50]}...")

    # 2. Create Tables
    print("\n[Step 2/3] Creating PostgreSQL schema (students, semester_marks, supplementary_exams, academic_summaries)...")
    tbl_res = neon.create_tables()
    if tbl_res["status"] != "Success":
        print(f"[-] Error: {tbl_res['message']}")
        return
    print(f"[+] {tbl_res['message']}")

    # 3. Migrate CSV records
    print("\n[Step 3/3] Uploading academic datasets to Neon...")
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    s1 = os.path.join(data_dir, "semester_1.csv")
    s2 = os.path.join(data_dir, "semester_2.csv")
    s3 = os.path.join(data_dir, "semester_3.csv")
    mk = os.path.join(data_dir, "makeup_exam.csv")
    bk = os.path.join(data_dir, "backup_exam.csv")

    sync_res = neon.sync_from_csv(s1, s2, s3, mk, bk)
    if sync_res["status"] != "Success":
        print(f"[-] Error: {sync_res['message']}")
        return
    print(f"[+] {sync_res['message']}")

    # 4. Verify Data from Cloud
    print("\n[Verification] Fetching live data from Neon:")
    df = neon.fetch_all_students_df()
    print(f"[+] Total students in Neon: {len(df)}")
    print(df[["Roll No", "Name", "Department", "Cumulative %", "Grade", "Status"]].head())

    print("\n" + "=" * 65)
    print("SUCCESS: Your project is now connected and synced with Neon!")
    print("You can view your tables live in the Neon Console: https://console.neon.tech")
    print("=" * 65)


if __name__ == "__main__":
    main()
