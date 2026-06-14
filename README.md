# Evaluation-Engines
/Evaluation-Engines
├── /api
│   └── sis_api.json          # The communication handshake protocol
├── /engines
│   ├── /judgement            # Automated Parity & Comparison Engine
│   │   ├── comparison.py     # Parity routines (temporal/magnitude)
│   │   └── logic_gate.py     # Fallacy & Rhetoric detection
│   └── /reputation           # Automated Confidence & Threshold Engine
│       ├── tracker.py        # Reliability Score (R) calculations
│       └── profile_store.py  # Long-term history (JSON/DB interface)
├── /forms
│   ├── audit_template.json   # Manual input forms
│   └── reconciliation.json   # ARP response templates
├── /data
│   └── entities.db           # SQLite/Relational database storage
└── README.md                 # System manifest & documentation


System Overview: Evaluation-Engines
Objective: To maintain data and behavioral integrity via dual-engine analysis.
Judgement Engine: Evaluates the Present Moment—performs real-time parity checks on logs, reports, and communications.
Reputation Tracker: Evaluates the Long-Term Trend—maintains the reliability profile for every entity node in the Sovereign Information System.
Integration: Engines communicate via the sis_api.json protocol.
