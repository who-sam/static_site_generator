# first course 

> [home](../backend career path)

- F-strings, provide a concise and readable way to include variable values within strings. The `f` before the string denotes an f-string, and any expression inside curly brackets `{}` is evaluated and interpolated into the string at runtime. This feature is useful for creating dynamic strings with embedded variable values.
- Most Python developers solve this problem by defining _all_ the functions in their program first, then they call an "entry point" function _last_. That way _all_ of the functions have been read by the Python interpreter before the first one is called.
	- Conventionally this "entry point" function is usually called `main` to keep things simple and consistent.

```python
def main():
    health = 10
    armor = 5
    addArmor(health, armor)
def addArmor(h, a):
    newHealth = h + a
    printHealth(newHealth)
def printHealth(newHealth):
    print(f"The player now has {newHealth} health")
# call entrypoint last
main()
```
- Parameters are the names used for inputs when _defining_ a function. Arguments are the values of the inputs supplied when a function is _called_.
- Python is one of the few languages that got a built in exponents it's in the format of 
- it also got built in flooring in the following formula `55 // 4` 
- the flooring means the result is rounded down to the nearest integer.
- The built-in [float()](https://docs.python.org/3/library/functions.html#float) function can create a numeric floating point value of negative/positive infinity.
- `negativeInfinity = float("-inf")`
- `positiveInfinity = float("inf")`
- [Tuples](https://docs.python.org/3/library/stdtypes.html#typesseq-tuple) are collections of data that are ordered and unchangeable. You can think of a tuple as a `List` with a fixed size. Tuples are created with round brackets.
- You can easily assign the values of a tuple to variables using unpacking.
- `dogName, dogAge = dog` 
- When you return multiple values from a function, you're actually returning a tuple.
- In Python, you can check if an item exists in a list using the `in` keyword. This operation is called a membership test and returns `True` if the specified item is found in the list, and `False` otherwise. This is a simple and efficient way to verify the presence of an element within a list.
```python
heroes = ["Spiderman", "Ironman", "Thor"]
print("Thor" in heroes)    # True
print("Batman" in heroes)  # False
```
- `[]` -> **lists** 
- indexed (ordered)
- changeable 
- can hold one type
- `()` -> **tuples**
- indexed (ordered)
- unchangeable
- can hold more than one type 
- `(2,)` \# note the comma! It's required for a single-element tuple
- `{}` -> **dictionaries and sets** 
- to make and empty dict. `{}` , to make an empty set `set()`
- both of them allow no duplicates
- `set()` removes duplicates automatically 

---

### Copying a List

To get a _new copy_ of a list, use the `copy()` method. If you just do `newList = oldList`, your new variable will just be a [reference](https://en.wikipedia.org/wiki/Reference_\(computer_science\)) to the original list... which is not what we want.
```python
nums = [4, 3, 2, 1]
numsCopy = nums.copy()
# numsCopy is [4, 3, 2, 1]
```

---
