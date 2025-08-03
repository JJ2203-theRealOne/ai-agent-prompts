## 1. Data Analysis Agent

**Prompt Template:**
```
Analyze the following dataset:
{data_summary}
Return insights on trends, anomalies, and correlations.
```
**Placeholders:** `{data_summary}`

**Example Input:**
```
data_summary = "Monthly sales for 12 months, with regional breakdowns."
```
**Example Output:**
```
Sales peaked in December (30% higher). Region B shows consistent growth; Region A stagnates.
```
**Test Criteria:**
- Insight relevance (human-reviewed)
- Anomaly detection accuracy
- Trend correctness

---