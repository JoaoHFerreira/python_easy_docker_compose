# Simple Python Package Example

This project demonstrates how to create and install a basic Python package.

## Project Structure

```
fruits/
├── __init__.py      # Empty (for now)
├── fruits.py       # Defines the 'banana' variable
├── setup.py        # Provides metadata and build instructions for the package
└── tropical/
    ├── __init__.py  # Makes 'tropical' a subpackage
    └── abacaxi.py    # Defines the 'abacaxi' variable

3 directories, 5 files
```

## Steps

1. **Create the Package Directory and Modules:**
   - Make a new directory named `fruits`.
   - Inside `fruits`, create `__init__.py`, `fruits.py`, and a subdirectory `tropical` with `__init__.py` and `abacaxi.py`.

2. **Define Variables:**
   - In `fruits.py`, add:

     ```python
     banana = "banana"
     ```

   - In `tropical/abacaxi.py`, add:

     ```python
     abacaxi = "abacaxi"
     ```

3. **Create `setup.py`** in the root directory:

   ```python
   from setuptools import setup, find_packages

   setup(
       name='fruits',
       version='0.1',
       packages=find_packages(),
   )
   ```

4. **Build the package:**

   * **Wheel (recommended):**

     ```bash
     python setup.py bdist_wheel 
     ```

   * **Egg (older format):**

     ```bash
     python setup.py bdist_egg
     ```

5. **Install (editable mode - for development):**

   ```bash
   pip install -e . 
   ```

6. **Install (non-editable mode - for actual use):**

   ```bash
   pip install ./dist/<package_name>-<version>-py3-none-any.whl  # Replace with your actual wheel filename
   ```

   or 

   ```bash
   pip install ./dist/<package_name>-<version>-py3.x.egg  # Replace with your actual egg filename
   ```

## Usage

```python
import fruits
print(fruits.banana)  # Output: banana

import tropical.abacaxi as abacaxi
print(abacaxi.abacaxi)  # Output: abacaxi
```
