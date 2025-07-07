import requests
import json
import argparse

# Base URL for AWS instance metadata service
METADATA_BASE_URL = "http://169.254.169.254/latest/meta-data/"

def get_metadata(path=""):
    """
    Retrieve metadata from AWS instance metadata service.
    Args:
        path (str): Specific metadata path to query
    Returns:
        dict or str: Metadata content
    """
    try:
        url = METADATA_BASE_URL + path
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        
        # If the response is a list of keys, recurse through them
        if path == "" or path.endswith("/"):
            keys = response.text.splitlines()
            result = {}
            for key in keys:
                # Skip empty keys
                if not key:
                    continue
                # Recursively get metadata for each key
                result[key] = get_metadata(f"{path}{key}")
            return result
        else:
            # Handle cases where the response is a text value
            return response.text
    except requests.RequestException as e:
        return f"Error retrieving metadata for {path}: {str(e)}"

def format_metadata(data, pretty=False):
    """
    Format metadata as JSON.
    Args:
        data: Metadata to format
        pretty (bool): If True, pretty-print the JSON
    Returns:
        str: JSON formatted string
    """
    indent = 2 if pretty else None
    return json.dumps(data, indent=indent)

def main():
    parser = argparse.ArgumentParser(description="Query AWS instance metadata")
    parser.add_argument("--key", help="Specific metadata key to retrieve (e.g., instance-id)")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    args = parser.parse_args()

    if args.key:
        # Fetch specific key
        result = get_metadata(args.key)
    else:
        # Fetch all metadata
        result = get_metadata()

    print(format_metadata(result, args.pretty))

if __name__ == "__main__":
    main()
