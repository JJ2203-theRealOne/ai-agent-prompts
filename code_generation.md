## 2. Code Generation Agent

**Prompt Template:**
```
Write a {language} function that {task_description}.
```
**Placeholders:** `{language}`, `{task_description}`

**Example Input:**
```
language = "Python"
task_description = "parses CSV and returns JSON"
```
**Example Output:**
```python
def csv_to_json(file_path):
    import csv, json
    with open(file_path) as f:
        return json.dumps(list(csv.DictReader(f)))
```
**Test Criteria:**
- Code correctness (unit test)
- Output validity
- Runtime performance

---