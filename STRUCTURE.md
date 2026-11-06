SeCoNet/
│
├── network/                  # SeCoNet contact network generation (without epidemic transmission)
│   ├── components.py
│   ├── demography.py
│   ├── files.py
│   ├── main.py
│   ├── pairing.py
│   ├── plots.py
│   ├── tickets.py
│   └── updates.py
│
├── transmission/             # SIRS epidemic simulation model (built on top of network/)
│   ├── components.py
│   ├── demography.py
│   ├── files.py
│   ├── main.py
│   ├── pairing.py
│   ├── plots.py
│   ├── tickets.py
│   ├── transmission.py
│   └── updates.py
│
├── vaccination/              # Evaluation of the 7 vaccination strategies (built on top of transmission/)
│   ├── vaccinate_age/
│   ├── vaccinate_betweeness/
│   ├── vaccinate_closeness/
│   ├── vaccinate_eigen/
│   ├── vaccinate_k/
│   ├── vaccinate_percolation/
│   └── vaccinate_ring/
│
├── results/                  # Summarized simulation outputs & CSV datasets (*.csv)
├── README.md                 # Main repository documentation & execution guide
├── STRUCTURE.md              # Data dictionary and CSV column header mapping
└── requirements.txt          # Python dependency specifications
