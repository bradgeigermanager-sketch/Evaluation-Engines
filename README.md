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
