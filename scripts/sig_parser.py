#!/usr/bin/env python3
"""
sig_parser.py
=============
Parses LeetCode Python3 starter snippets into structured method signatures.
Extracts method name, parameters (name + type), return type, and detects
design (multi-method) problems.

Also provides Python-to-C++ type mapping.
"""

import re

# ═══════════════════════════════════════════
# TYPE MAPPING: Python -> C++
# ═══════════════════════════════════════════

PY_TO_CPP = {
    "int": "int",
    "float": "double",
    "bool": "bool",
    "str": "string",
    "None": "void",
    "List[int]": "vector<int>",
    "List[str]": "vector<string>",
    "List[float]": "vector<double>",
    "List[bool]": "vector<bool>",
    "List[List[int]]": "vector<vector<int>>",
    "List[List[str]]": "vector<vector<string>>",
    "List[List[char]]": "vector<vector<char>>",
    "Optional[TreeNode]": "TreeNode*",
    "Optional[ListNode]": "ListNode*",
    "TreeNode": "TreeNode*",
    "ListNode": "ListNode*",
    "'TreeNode'": "TreeNode*",
    "'Node'": "Node*",
    "'Optional[Node]'": "Node*",
    "Optional['Node']": "Node*",
    "List[Optional[TreeNode]]": "vector<TreeNode*>",
    "List[Optional[ListNode]]": "vector<ListNode*>",
}

# Default return values in C++
CPP_DEFAULTS = {
    "int": "0",
    "double": "0.0",
    "bool": "false",
    "string": '""',
    "void": "",
    "vector<int>": "{}",
    "vector<string>": "{}",
    "vector<double>": "{}",
    "vector<bool>": "{}",
    "vector<vector<int>>": "{}",
    "vector<vector<string>>": "{}",
    "TreeNode*": "nullptr",
    "ListNode*": "nullptr",
    "Node*": "nullptr",
}

# Python default return values
PY_DEFAULTS = {
    "int": "0",
    "float": "0.0",
    "bool": "False",
    "str": '""',
    "None": "None",
    "List[int]": "[]",
    "List[str]": "[]",
    "List[float]": "[]",
    "List[bool]": "[]",
    "List[List[int]]": "[]",
    "List[List[str]]": "[]",
    "Optional[TreeNode]": "None",
    "Optional[ListNode]": "None",
}


def py_type_to_cpp(py_type):
    """Convert a Python type annotation to C++ type."""
    if not py_type:
        return "void"
    py_type = py_type.strip()
    if py_type in PY_TO_CPP:
        return PY_TO_CPP[py_type]
    # Handle generic List[X]
    m = re.match(r"List\[(.+)\]", py_type)
    if m:
        inner = py_type_to_cpp(m.group(1))
        return f"vector<{inner}>"
    m = re.match(r"Optional\[(.+)\]", py_type)
    if m:
        inner = py_type_to_cpp(m.group(1))
        if "*" in inner:
            return inner
        return inner
    return py_type  # fallback


def cpp_default(cpp_type):
    """Get default return value for a C++ type."""
    if cpp_type in CPP_DEFAULTS:
        return CPP_DEFAULTS[cpp_type]
    if cpp_type.startswith("vector"):
        return "{}"
    if cpp_type.endswith("*"):
        return "nullptr"
    return "{}"


def py_default(py_type):
    """Get default return value for a Python type."""
    if not py_type:
        return "None"
    py_type = py_type.strip()
    if py_type in PY_DEFAULTS:
        return PY_DEFAULTS[py_type]
    if py_type.startswith("List"):
        return "[]"
    if py_type.startswith("Optional"):
        return "None"
    return "None"


def cpp_param_decl(name, py_type):
    """Convert a Python parameter to C++ declaration."""
    cpp_type = py_type_to_cpp(py_type)
    # Pass containers by reference
    if cpp_type.startswith("vector") or cpp_type == "string":
        return f"{cpp_type}& {name}"
    if cpp_type.endswith("*"):
        return f"{cpp_type} {name}"
    return f"{cpp_type} {name}"


def parse_snippet(snippet):
    """Parse a Python3 starter snippet into structured signature data.
    
    Returns a list of method dicts:
    [
        {
            "name": "twoSum",
            "params": [("nums", "List[int]"), ("target", "int")],
            "return_type": "List[int]",
            "is_init": False,
        },
        ...
    ]
    Also returns is_design=True if there are multiple non-init methods.
    """
    if not snippet:
        return [], False, "Solution"
    
    # Remove commented lines (TreeNode/ListNode definitions)
    clean_lines = []
    for line in snippet.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        clean_lines.append(line)
    snippet = "\n".join(clean_lines)
    
    methods = []
    class_name = "Solution"
    
    # Extract class name from uncommented code
    cm = re.search(r"class\s+(\w+)", snippet)
    if cm:
        class_name = cm.group(1)
    
    # Find all method definitions
    # Handle multi-line with careful regex
    pattern = r"def\s+(\w+)\s*\((.*?)\)\s*(?:->\s*(.+?))?\s*:"
    for match in re.finditer(pattern, snippet, re.DOTALL):
        m_name = match.group(1)
        raw_params = match.group(2)
        ret_type = match.group(3)
        
        if ret_type:
            ret_type = ret_type.strip().rstrip(":")
        
        # Parse parameters (skip 'self')
        params = []
        if raw_params:
            # Split carefully (handle nested brackets)
            depth = 0
            current = ""
            for ch in raw_params:
                if ch in "([":
                    depth += 1
                    current += ch
                elif ch in ")]":
                    depth -= 1
                    current += ch
                elif ch == "," and depth == 0:
                    current = current.strip()
                    if current and current != "self":
                        params.append(current)
                    current = ""
                else:
                    current += ch
            current = current.strip()
            if current and current != "self":
                params.append(current)
        
        # Parse each param into (name, type)
        parsed_params = []
        for p in params:
            p = p.strip()
            if ":" in p:
                parts = p.split(":", 1)
                pname = parts[0].strip()
                ptype = parts[1].strip()
                # Remove default values
                if "=" in ptype:
                    ptype = ptype.split("=")[0].strip()
                parsed_params.append((pname, ptype))
            else:
                # No type annotation
                parsed_params.append((p.strip(), "int"))
        
        methods.append({
            "name": m_name,
            "params": parsed_params,
            "return_type": ret_type or "None",
            "is_init": m_name == "__init__",
        })
    
    # Determine if design problem
    non_init = [m for m in methods if not m["is_init"]]
    is_design = len(methods) > 1 or class_name != "Solution"
    
    return methods, is_design, class_name


def generate_cpp_signature(method, class_name="Solution"):
    """Generate a C++ method signature string."""
    cpp_ret = py_type_to_cpp(method["return_type"])
    params_str = ", ".join(
        cpp_param_decl(name, ptype) for name, ptype in method["params"]
    )
    return f"    {cpp_ret} {method['name']}({params_str})"
