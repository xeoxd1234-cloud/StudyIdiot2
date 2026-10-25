# AI Lab Python Codes

This folder contains separate Python files extracted and organized from the uploaded **Short lab codes** PDF.

## Naming convention

Files are numbered in the order of the source material and use lowercase `snake_case` names that describe the algorithm or problem.

## Programs

1. `01_route_planning_bfs.py` — Breadth-First Search
2. `02_route_planning_dfs.py` — Depth-First Search
3. `03_route_planning_depth_limited_search.py` — Depth-Limited Search
4. `04_route_planning_iterative_deepening.py` — Iterative Deepening Search
5. `05_eight_puzzle_astar.py` — 8-Puzzle A* solver
6. `06_water_jug_bfs.py` — Water Jug BFS
7. `07_tsp_hill_climbing_simulated_annealing.py` — TSP Hill Climbing and Simulated Annealing
8. `08_tic_tac_toe_minimax_alpha_beta.py` — Minimax with Alpha-Beta Pruning
9. `09_fol_plant_disease_expert_system.py` — Plant disease rule inference
10. `10_fol_unification_student_eligibility.py` — Unification example
11. `11_naive_bayes_spam_classifier.py` — Naive Bayes spam classifier
12. `12_hidden_markov_model_viterbi_activity.py` — HMM activity recognition
13. `13_fol_scholarship_rahul.py` — Rahul scholarship eligibility
14. `14_fol_tommy_mammal_animal.py` — Tommy mammal/animal inference
15. `15_fol_scholarship_priya.py` — Priya scholarship eligibility
16. `16_fol_tomato_plant_disease.py` — Tomato plant disease inference
17. `17_fol_library_book_borrowing.py` — Library book borrowing inference
18. `18_fol_promotion_amit.py` — Amit promotion eligibility
19. `19_fol_online_order_neha.py` — Neha online order inference

## Requirements

Most scripts use only the Python standard library. The following scripts require third-party packages:

- `11_naive_bayes_spam_classifier.py`: `scikit-learn`
- `12_hidden_markov_model_viterbi_activity.py`: `numpy`

Install both with:

```bash
python -m pip install scikit-learn numpy
```

## Run a program

From this directory, run any individual script, for example:

```bash
python 01_route_planning_bfs.py
```

The scripts are standalone and use `if __name__ == "__main__":` entry points where appropriate.

## Notes

- The PDF contains two repeated Amit promotion examples (items 15 and 16); they are represented once as `18_fol_promotion_amit.py` to avoid an unnecessary duplicate.
- The source describes the Rahul scholarship inference as resolution, but the code shown is forward rule application; this file preserves the source's facts and rules rather than implementing a full resolution theorem prover.
- The original 8-puzzle code is formatted across broken PDF lines. It has been reconstructed into runnable Python.
