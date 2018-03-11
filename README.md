# daydif
Tool for computing the number of days between two calendar dates.

### Installation
```bash
pip install git+https://github.com/kerrycobb/daydif
```

# Usage
### Command Line

Number of days between input date and todays date
```bash
daydiff yyyy-mm-dd
```

Number of days between two dates
```bash
daydiff yyyy-mm-dd yyyy-mm-dd
```

### Python Module
```python
import daydif as dd

# Number of days between input date and todays date
dd.daydif('yyyy-mm-dd')

# Number of days between two dates
dd.daydif('yyyy-mm-dd', enddate='yyyy-mm-dd')

```
