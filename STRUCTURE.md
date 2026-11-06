SeCoNet/
│
├── seconet/                  # Core Python module
│   ├── __init__.py
│   ├── network_growth.py     # SeCoNet preferential attachment & link removal dynamics
│   ├── transmission.py       # SIRS epidemic model & parameter settings
│   └── vaccination.py        # Implementation of targeting heuristics (Degree, BC, PC, etc.)
│
├── results/                  # Summarized simulation outputs & CSV datasets
│   ├── STRUCTURE.md          # Data dictionary and directory guide
│   └── *.csv                 # Raw & aggregated scenario outputs (Mean ± SD)
│
├── requirements.txt          # Python dependency specifications
└── README.md                 # Main repository documentation
