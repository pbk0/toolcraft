# Examples

This section provides practical examples of using ToolCraft in various scenarios.

## Basic Examples

### Hello World

The simplest example - printing a greeting:

```python
from toolcraft import hello_message

# Get the greeting
message = hello_message()
print(message)
```

**Output:**
```
Hello from ToolCraft!
```

### Version Information

Accessing version information:

```python
from toolcraft import __version__

print(f"ToolCraft version: {__version__}")
```

### Command Line Usage

```bash
# Basic greeting
toolcraft --hello

# Check version
toolcraft --version
```

## Automation Examples

### Simple Automation Script

```python
#!/usr/bin/env python3
"""
Simple automation script using ToolCraft.
"""

import sys
from toolcraft import hello_message, __version__

def main():
    """Main automation function."""
    print(f"Starting automation with ToolCraft {__version__}")
    
    # Your automation logic here
    greeting = hello_message()
    print(f"Status: {greeting}")
    
    # Simulate some work
    print("Performing automation tasks...")
    
    # Example: File processing, API calls, etc.
    # process_files()
    # call_apis()
    # generate_reports()
    
    print("Automation completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Batch Processing

```python
#!/usr/bin/env python3
"""
Batch processing example with ToolCraft.
"""

import os
from pathlib import Path
from toolcraft import hello_message

def process_directory(directory_path: str) -> None:
    """Process all files in a directory."""
    print(hello_message())
    print(f"Processing directory: {directory_path}")
    
    path = Path(directory_path)
    if not path.exists():
        print(f"Directory {directory_path} does not exist")
        return
    
    # Process each file
    for file_path in path.iterdir():
        if file_path.is_file():
            print(f"Processing: {file_path.name}")
            # Add your file processing logic here
            process_file(file_path)

def process_file(file_path: Path) -> None:
    """Process a single file."""
    # Example processing logic
    size = file_path.stat().st_size
    print(f"  - Size: {size} bytes")
    
    # Add your specific processing here
    # - Text processing
    # - Image manipulation
    # - Data transformation
    # etc.

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python batch_process.py <directory>")
        sys.exit(1)
    
    process_directory(sys.argv[1])
```

## Integration Examples

### CI/CD Pipeline

**GitHub Actions Example:**

```yaml
name: Automation with ToolCraft

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  automation:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install ToolCraft
      run: |
        python -m pip install --upgrade pip
        pip install toolcraft
    
    - name: Run automation
      run: |
        toolcraft --hello
        python automation_script.py
```

**Azure DevOps Example:**

```yaml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.9'
  displayName: 'Use Python 3.9'

- script: |
    python -m pip install --upgrade pip
    pip install toolcraft
  displayName: 'Install dependencies'

- script: |
    toolcraft --hello
    python automation_script.py
  displayName: 'Run automation'
```

### Docker Integration

```dockerfile
FROM python:3.9-slim

# Install ToolCraft
RUN pip install toolcraft

# Copy your automation scripts
COPY automation_script.py /app/
WORKDIR /app

# Run your automation
CMD ["python", "automation_script.py"]
```

### Web Application Integration

```python
from flask import Flask, jsonify
from toolcraft import hello_message, __version__

app = Flask(__name__)

@app.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': hello_message(),
        'version': __version__
    })

@app.route('/api/automate')
def trigger_automation():
    """Trigger automation via web API."""
    try:
        # Your automation logic here
        result = run_automation()
        return jsonify({
            'status': 'success',
            'message': hello_message(),
            'result': result
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

def run_automation():
    """Your automation logic."""
    # Implement your automation here
    return "Automation completed"

if __name__ == '__main__':
    app.run(debug=True)
```

## Advanced Examples

### Configuration-Driven Automation

```python
#!/usr/bin/env python3
"""
Configuration-driven automation example.
"""

import yaml
from pathlib import Path
from toolcraft import hello_message

def load_config(config_path: str) -> dict:
    """Load configuration from YAML file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def run_automation(config: dict) -> None:
    """Run automation based on configuration."""
    print(hello_message())
    
    for task in config.get('tasks', []):
        task_type = task.get('type')
        task_params = task.get('parameters', {})
        
        print(f"Running task: {task_type}")
        
        if task_type == 'file_process':
            process_files(task_params)
        elif task_type == 'api_call':
            make_api_call(task_params)
        elif task_type == 'report_generate':
            generate_report(task_params)
        else:
            print(f"Unknown task type: {task_type}")

def process_files(params: dict) -> None:
    """Process files based on parameters."""
    source_dir = params.get('source_directory')
    pattern = params.get('file_pattern', '*')
    
    print(f"Processing files in {source_dir} with pattern {pattern}")
    # Implementation here

def make_api_call(params: dict) -> None:
    """Make API call based on parameters."""
    url = params.get('url')
    method = params.get('method', 'GET')
    
    print(f"Making {method} request to {url}")
    # Implementation here

def generate_report(params: dict) -> None:
    """Generate report based on parameters."""
    output_file = params.get('output_file')
    template = params.get('template')
    
    print(f"Generating report: {output_file} using template {template}")
    # Implementation here

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python config_automation.py <config.yml>")
        sys.exit(1)
    
    config = load_config(sys.argv[1])
    run_automation(config)
```

**Example configuration file (config.yml):**

```yaml
tasks:
  - type: file_process
    parameters:
      source_directory: "/path/to/files"
      file_pattern: "*.txt"
      
  - type: api_call
    parameters:
      url: "https://api.example.com/data"
      method: "GET"
      
  - type: report_generate
    parameters:
      output_file: "report.html"
      template: "default"
```

## Error Handling Examples

### Robust Error Handling

```python
#!/usr/bin/env python3
"""
Example with comprehensive error handling.
"""

import logging
import sys
from pathlib import Path
from toolcraft import hello_message

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def safe_automation() -> int:
    """Run automation with proper error handling."""
    try:
        logger.info("Starting automation")
        print(hello_message())
        
        # Your automation logic here
        result = perform_critical_task()
        
        logger.info("Automation completed successfully")
        return 0
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        return 1
        
    except PermissionError as e:
        logger.error(f"Permission denied: {e}")
        return 2
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 3
        
    finally:
        logger.info("Cleanup completed")
        cleanup_resources()

def perform_critical_task():
    """Perform the main automation task."""
    # Your critical automation logic here
    pass

def cleanup_resources():
    """Clean up any resources."""
    # Cleanup logic here
    pass

if __name__ == "__main__":
    exit_code = safe_automation()
    sys.exit(exit_code)
```

These examples demonstrate various ways to use ToolCraft in real-world scenarios. Start with the basic examples and gradually work your way up to more complex automation scripts.
