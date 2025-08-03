## 3. Fraud Detection Agent

**Prompt Template:**
```
You are a fraud detection assistant.
Evaluate the following transaction log for anomalies:

{transaction_details}

Rules to consider:
- Unusual transaction time (e.g. night hours)
- IP or geo mismatch
- Amount spikes or irregular patterns
- Multiple failed attempts
- Account/device changes

Return: 
- A risk level (Low, Medium, High)
- Explanation of detected signals
```
**Placeholders:** `{transaction_details}`

**Example Input:**
```json
{
  "user_id": "U12345",
  "transactions": [
    {
      "timestamp": "2025-07-28T03:15:00Z",
      "ip": "45.23.1.5",
      "amount": 2500,
      "device": "iPhone13"
    },
    {
      "timestamp": "2025-07-28T03:16:30Z",
      "ip": "91.204.3.9",
      "amount": 2700,
      "device": "Android"
    }
  ]
}
```
**Example Output:**
```json
{
  "risk": "High",
  "signals": [
    "Unusual transaction time (03:15 AM)",
    "Multiple high-value transactions in <2 mins",
    "Different IPs and devices suggest location/device spoofing"
  ]
}
```
**Test Criteria:**
- True positive rate (compared to labeled data)
- False positive minimization
- Explanation clarity
- Latency (response time)

---