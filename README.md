# Evaluation-Engines
/Evaluation-Engines
├── /api
│   └── sis_api.json            # Communication handshake protocol (Inter-Engine)
├── /engines
│   ├── /judgement              # Automated Parity & Comparison Engine
│   │   ├── comparison.py       # Parity routines (temporal/magnitude)
│   │   ├── logic_gate.py       # Fallacy & Rhetoric detection
│   │   └── snf_filter.py       # Statistical Noise Filter (3σ logic)
│   └── /reputation             # Automated Confidence & Threshold Engine
│       ├── tracker.py          # Reliability Score (R) calculations
│       └── profile_store.py    # Entity memory/history bank
├── /forms
│   ├── audit_template.json     # Manual audit input forms
│   ├── reconciliation.json     # ARP response & follow-up templates
│   └── forensic_audit.json     # Forensic Narrative Audit (High-fidelity record)
├── /tests
│   ├── /unit
│   │   ├── test_snf_filter.py  # Verify 3σ noise thresholding
│   │   └── test_comparison.py  # Verify parity/magnitude routines
│   ├── /integration
│   │   └── test_reconciliation.py # Verify Judgement -> Reputation handshake
│   └── /adversarial
│       ├── test_gaslighting.py # Test narrative drift detection
│       └── test_data_injection.py # Test magnitude manipulation detection
├── /data
│   └── entities.db             # SQLite/Relational database storage
├── README.md                   # System manifest & integration workflows
└── main.py                     # System entry point/initialization


System Overview: Evaluation-Engines
Objective: To maintain data and behavioral integrity via dual-engine analysis.
Judgement Engine: Evaluates the Present Moment—performs real-time parity checks on logs, reports, and communications.
Reputation Tracker: Evaluates the Long-Term Trend—maintains the reliability profile for every entity node in the Sovereign Information System.
Integration: Engines communicate via the sis_api.json protocol.
