from pathlib import Path

Path("C:\\Program Files\\Microsoft")
# can do as raw string like this
Path(r"C:\Program Files\Mircrosoft")

Path()

Path("ecommerce/__init.py")
Path() / Path("ecommoerce") / "__init__.py"
Path.home()

path = Path.home()

path.exists()
path.is_file()
path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)

# path = path.with_name("file.txt")
# print(path.absolute())
# path = path.with_suffix(".txt")

# for p in path.iterdir():
#     print(p)

p = [p for p in path.iterdir() if p.is_dir()]
# print(p)

py_files = [p for p in path.glob("*.py")]
print(py_files)