#!/usr/bin/env python3
import hashlib
import argparse

def generate_md5_hash(password: str) -> str:
    """
    Generate the MD5 hash for the provided password.

    Args:
        password (str): The plain text password.

    Returns:
        str: The MD5 hash of the password.
    """
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Convert password to MD5 hash")
    parser.add_argument("--password", required=True, help="Password to be hashed")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Hash the password
    hashed_password = generate_md5_hash(args.password)
    
    # Print hashed password
    print("MD5 Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
