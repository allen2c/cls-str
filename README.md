# cls-str

[![PyPI version](https://img.shields.io/pypi/v/cls-str.svg)](https://pypi.org/project/cls-str/)
[![Python Version](https://img.shields.io/pypi/pyversions/cls-str.svg)](https://pypi.org/project/cls-str/)
[![License](https://img.shields.io/pypi/l/cls-str.svg)](https://opensource.org/licenses/MIT)

Convert Python classes to strings and back. Useful for serialization, configuration files, and message passing.

## Installation

```bash
pip install cls-str
```

## Quick Start

### Basic Usage

```python
from cls_str import cls_to_str, str_to_cls

# Convert class to string
from http.server import SimpleHTTPRequestHandler

class_path = cls_to_str(SimpleHTTPRequestHandler)
print(class_path)
# Output: "http.server.SimpleHTTPRequestHandler"

# Convert string back to class
restored_class = str_to_cls(class_path)
assert restored_class is SimpleHTTPRequestHandler
```

### Nested Classes

```python
class Outer:
    class Inner:
        pass

# Works with nested classes too
path = cls_to_str(Outer.Inner)
print(path)
# Output: "your_module.Outer.Inner"

loaded_class = str_to_cls(path)
assert loaded_class is Outer.Inner
```

## License

MIT License
