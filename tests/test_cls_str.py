import pytest

from cls_str import cls_to_str, str_to_cls


def test_cls_str_1_normal_importable_class():
    print("--- Example 1: Normal, importable Class ---")
    # Import a built-in Python class as an example
    from http.server import SimpleHTTPRequestHandler

    original_class_1 = SimpleHTTPRequestHandler

    # Class -> String
    path_1 = cls_to_str(original_class_1)
    print(f"  Serialized path: {path_1}")

    # String -> Class
    loaded_class_1 = str_to_cls(path_1)
    print(f"  Restored Class: {loaded_class_1}")

    # Validation
    assert original_class_1 is loaded_class_1
    print("  Validation successful (is): True\n")


def test_cls_str_2_nested_class():
    print("--- Example 2: Nested Class ---")

    class Outer:
        class Inner:
            pass

    original_class_2 = Outer.Inner

    # Class -> String (this will trigger logger.warning)
    path_2 = cls_to_str(original_class_2)
    print(f"  Serialized path: {path_2}")

    # String -> Class (this will succeed because we are still in __main__)
    loaded_class_2 = str_to_cls(path_2)
    print(f"  Restored Class: {loaded_class_2}")

    # Validation
    assert original_class_2 is loaded_class_2
    print("  Validation successful (is): True\n")


def test_cls_str_3_loading_failure():
    print("--- Example 3: Loading failure ---")
    bad_path = "non_existent.module.FakeClass"
    with pytest.raises(ImportError):
        str_to_cls(bad_path)
