# AWS Instance Metadata Query Tool

A lightweight Python script to query AWS EC2 instance metadata from the Instance Metadata Service (IMDS) and output results in JSON format. It supports retrieving all metadata or specific keys with optional pretty-printed output.

## Features

- Retrieve all instance metadata or a specific key (e.g., `instance-id`, `ami-id`).
- Output metadata in JSON format with optional pretty-printing.
- Robust error handling for network issues and timeouts.

## Prerequisites

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- Must run on an AWS EC2 instance with access to IMDS (`http://169.254.169.254`)

## Installation

1. Clone or download the script (`ec2-etadata.py`).
2. Install the required dependency:

   ```bash
   pip install requests
   ```

## Usage

Run the script from an AWS EC2 instance.

### Fetch All Metadata

```bash
python get_aws_metadata.py
```

### Fetch a Specific Metadata Key

```bash
python get_aws_metadata.py --key instance-id
```

### Pretty-Print JSON Output

```bash
python get_aws_metadata.py --pretty
```

### Combine Options

```bash
python get_aws_metadata.py --key instance-id --pretty
```

## Example Output

### All Metadata (Partial)

```json
{
  "ami-id": "ami-1234567890abcdef0",
  "instance-id": "i-1234567890abcdef0",
  "instance-type": "t2.micro",
  "local-ipv4": "172.31.32.123",
  ...
}
```

### Specific Key

```bash
$ python get_aws_metadata.py --key instance-id
"i-1234567890abcdef0"
```

## Common Metadata Keys

| Key               | Description                           |
|-------------------|---------------------------------------|
| `ami-id`          | AMI ID of the instance               |
| `instance-id`     | Unique instance ID                   |
| `instance-type`   | Instance type (e.g., `t2.micro`)     |
| `local-ipv4`      | Private IP address                   |
| `public-ipv4`     | Public IP address (if applicable)    |
| `security-groups` | Assigned security groups             |

## Technical Details

- Uses IMDSv2 endpoint (`http://169.254.169.254/latest/meta-data/`).
- Implements a 2-second timeout for metadata requests.
- Handles both nested metadata structures and simple values.

## Security Considerations

- Ensure the EC2 instance has appropriate IAM permissions for metadata access.
- Avoid exposing sensitive metadata (e.g., IAM credentials) in logs or outputs.

## Troubleshooting

- **No response?** Ensure the script runs on an EC2 instance with IMDS enabled.
- **Errors?** Check for network issues or IMDS restrictions (e.g., IMDSv2 required).
- **Invalid key?** Verify the metadata key exists (see AWS IMDS documentation).

## License

This project is licensed under the MIT License.
