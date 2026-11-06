# Simulation Results Directory

This directory contains the numerical output datasets generated across all 15,200+ simulation sets evaluated in the study.

## Dataset File Structure

Files are saved in `.csv` format and structured by experimental parameters:

- `results.csv`: Core baseline simulations ($N = 3000, \beta = 0.13, \langle\delta\rangle = 100$).
- `15year.csv`: Appendix A results ($\langle\eta\rangle = 1.5$ years).
- `beta.csv`: Appendix B results ($\beta = 0.30$).
- `duration{300,500,700}.csv`: Appendix C results ($\langle\delta\rangle = 300, 500, 700$ days).
- `coverage{20,40,80}.csv`: Appendix D results ($c = 20\%, 40\%, 80\%$).
- `5k.csv`: Appendix E results ($N = 5000$).

## Data Metrics (CSV Columns)

Each CSV file reports aggregated statistics across 10 independent stochastic runs ($N = 10$):

| Column Header | Description | Metric Type |
| :--- | :--- | :--- |
| `m` | Initial node attachment parameter $m$ | Input Parameter |
| `mean_<k>` / `std_<k>` | Mean and SD of network average degree ($\langle k \rangle$) | Topological Metric |
| `mean_gamma` / `std_gamma` | Mean and SD of scale-free power-law exponent ($\gamma$) | Topological Metric |
| `mean_path` / `std_path` | Mean and SD of average shortest path length ($L$) | Topological Metric |
| `mean_cc` / `std_cc` | Mean and SD of network clustering coefficient ($C$) | Topological Metric |
| `mean_no_general_day` / `std_no_general_day` | Peak prevalence day (Overall cohort, No vaccination) | Outcome Metric |
| `mean_age_general_day` / `std_age_general_day` | Peak prevalence day (Overall cohort, Age-based) | Outcome Metric |
| `mean_ring_general_day` / `std_ring_general_day` | Peak prevalence day (Overall cohort, Ring) | Outcome Metric |
| `mean_k_general_day` / `std_k_general_day` | Peak prevalence day (Overall cohort, Degree centrality) | Outcome Metric |
| `mean_between_general_day` / `std_between_general_day` | Peak prevalence day (Overall cohort, Betweenness centrality) | Outcome Metric |
| `mean_close_general_day` / `std_close_general_day` | Peak prevalence day (Overall cohort, Closeness centrality) | Outcome Metric |
| `mean_percolation_general_day` / `std_percolation_general_day` | Peak prevalence day (Overall cohort, Percolation centrality) | Outcome Metric |
| `mean_eigen_general_day` / `std_eigen_general_day` | Peak prevalence day (Overall cohort, Eigenvector centrality) | Outcome Metric |
| `mean_no_general_cumulative` / `std_no_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, No vaccination) | Outcome Metric |
| `mean_age_general_cumulative` / `std_age_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Age-based) | Outcome Metric |
| `mean_ring_general_cumulative` / `std_ring_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Ring) | Outcome Metric |
| `mean_k_general_cumulative` / `std_k_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Degree) | Outcome Metric |
| `mean_between_general_cumulative` / `std_between_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Betweenness) | Outcome Metric |
| `mean_close_general_cumulative` / `std_close_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Closeness) | Outcome Metric |
| `mean_percolation_general_cumulative` / `std_percolation_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Percolation) | Outcome Metric |
| `mean_eigen_general_cumulative` / `std_eigen_general_cumulative` | Cumulative incidence at $T=1000$ (Overall, Eigenvector) | Outcome Metric |
| `mean_no_general_incidence` / `std_no_general_incidence` | Daily peak incidence (Overall cohort, No vaccination) | Outcome Metric |
| `mean_age_general_incidence` / `std_age_general_incidence` | Daily peak incidence (Overall cohort, Age-based) | Outcome Metric |
| `mean_ring_general_incidence` / `std_ring_general_incidence` | Daily peak incidence (Overall cohort, Ring) | Outcome Metric |
| `mean_k_general_incidence` / `std_k_general_incidence` | Daily peak incidence (Overall cohort, Degree) | Outcome Metric |
| `mean_between_general_incidence` / `std_between_general_incidence` | Daily peak incidence (Overall cohort, Betweenness) | Outcome Metric |
| `mean_close_general_incidence` / `std_close_general_incidence` | Daily peak incidence (Overall cohort, Closeness) | Outcome Metric |
| `mean_percolation_general_incidence` / `std_percolation_general_incidence` | Daily peak incidence (Overall cohort, Percolation) | Outcome Metric |
| `mean_eigen_general_incidence` / `std_eigen_general_incidence` | Daily peak incidence (Overall cohort, Eigenvector) | Outcome Metric |
| `mean_*_female_day` / `std_*_female_day` | Peak prevalence day for female cohort across strategies | Outcome Metric |
| `mean_*_female_cumulative` / `std_*_female_cumulative` | Cumulative incidence for female cohort across strategies | Outcome Metric |
| `mean_*_female_incidence` / `std_*_female_incidence` | Daily peak incidence for female cohort across strategies | Outcome Metric |
| `mean_*_male_day` / `std_*_male_day` | Peak prevalence day for male cohort across strategies | Outcome Metric |
| `mean_*_male_cumulative` / `std_*_male_cumulative` | Cumulative incidence for male cohort across strategies | Outcome Metric |
| `mean_*_male_incidence` / `std_*_male_incidence` | Daily peak incidence for male cohort across strategies | Outcome Metric |
