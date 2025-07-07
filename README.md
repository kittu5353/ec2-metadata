AWS Instance Metadata Query Tool
Overview
This Python script retrieves metadata from the AWS Instance Metadata Service (IMDS) for EC2 instances and outputs it in JSON format. It can fetch all available metadata or a specific metadata key, with optional pretty-printed JSON output.
Features

Query all instance metadata or a specific key (e.g., instance-id, ami-id).
JSON-formatted output with optional pretty-printing.
Handles network errors and timeouts gracefully.

Requirements

Python 3.6 or higher
requests library (pip install requests)
Must run on an AWS EC2 instance with access to IMDS (http://169.254.169.254)

Installation

Clone or download the script (get_aws_metadata.py).
Install the required library:pip install requests



Usage
Run the script from an EC2 instance.
Fetch All Metadata
python get_aws_metadata.py

Fetch a Specific Metadata Key
python get_aws_metadata.py --key instance-id

Pretty-Print JSON Output
python get_aws_metadata.py --pretty

Combine Options
python get_aws_metadata.py --key instance-id --pretty

Example Output
All Metadata (Partial)
{
  "ami-id": "ami-1234567890abcdef0",
  "instance-id": "i-1234567890abcdef0",
  "instance-type": "t2.micro",
  ...
}

Specific Key
$ python get_aws_metadata.py --key instance-id
"i-1234567890abcdef0"

Common Metadata Keys

ami-id: AMI ID of the instance
instance-id: Unique instance ID
instance-type: Instance type (e.g., t2.micro)
local-ipv4: Private IP address
public-ipv4: Public IP address (if applicable)
security-groups: Assigned security groups

Notes

Uses IMDSv2 endpoint (http://169.254.169.254/latest/meta-data/).
Includes a 2-second timeout for metadata requests to prevent hanging.
Some metadata keys return nested structures, while others return simple values.

Security Considerations

Ensure the EC2 instance has appropriate IAM permissions for accessing sensitive metadata.
Use caution when querying sensitive keys to avoid exposing confidential information.

Troubleshooting

If metadata retrieval fails, verify the script is running on an EC2 instance with IMDS access.
Check for network issues or IMDS configuration restrictions.
