from handler import lambda_handler
import json




data = [
    {
  "email": "user@example.com",
  "type": "income",
  "amount": 4100,
  "category": "salary",
  "description": "Monthly paycheck",
  "recurrence": "monthly",
  "start_date": "2025-11-01",
  "end_date": None
},
    {
  "email": "user@example.com",
  "type": "expense",
  "amount": 1000,
  "category": "rent",
  "description": "Monthly paycheck",
  "recurrence": "monthly",
  "start_date": "2025-11-01",
  "end_date": "2026-02-28"
}
]

for entry in data:
    event = {
        'httpMethod':'POST',
        'path':'/financial',
        'body':json.dumps(entry)
    }

    lambda_handler(event,{})
