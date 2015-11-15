# checkist

Minimal module for argument checking

### install

```
pip install checkist
```

### usage

let's say you have a list of valid arugments

```python
valid = ['elf', 'mage', 'knight']
```

you can check against it like this

```python
checkist.opts('elf', valid)
```

```python
checkist.opts('mage', valid)
```

```python
checkist.opts('archer', valid)
>> ValueError: Option must be one of 'elf', 'mage', 'knight', got 'archer'
```
