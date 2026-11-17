# Computational Biology: Progression Towards Modeling of Cancer Cells and Subcellular Organelles using Molecular Dynamics Simulations

**Undergraduate Senior Thesis** · John Quinn · University of Wisconsin–Milwaukee, Biomedical Engineering
Mentor: Dr. Mahsa Dabagh

<p align="center">
  <img src="simulations/2020-12-15%20Work/fluidcopy/outards.png" width="49%" alt="Coarse-grained cell model: outer membrane surface in a periodic simulation box">
  <img src="simulations/2020-12-15%20Work/fluidcopy/innards.png" width="49%" alt="Same cell model with the outer surface hidden, showing the internal bonded network">
</p>
<p align="center"><em>Coarse-grained cell model from the December 2020 fluid-like membrane runs:
outer membrane (left) and the bonded internal network beneath it (right).
Files: <code>simulations/2020-12-15 Work/fluidcopy</code>.</em></p>

This repository collects the simulation inputs, Python geometry builders and
documents behind my undergraduate research (2020) on modeling cancer cells,
red blood cells and lipid membranes with the molecular dynamics package
[LAMMPS](https://www.lammps.org/). The work started in UWM's Summer Undergraduate
Research Fellowship (SURF) and grew into my senior thesis, then into my MS thesis.

- 📄 **Thesis:** [thesis/Senior Thesis Document.pdf](thesis/Senior%20Thesis%20Document.pdf)
- 🖼️ **Poster:** [CEAS Student Research Poster Competition, 2020](thesis/CEAS%20Poster%20-%20SURF%20Symposium%20Spring%202020.pdf)
- 🔗 **SURF symposium (2020):** [abstract](https://dc.uwm.edu/uwsurca/2020/virtual/170/) · [poster repo](https://github.com/jqstudy2019/2020-SURF-Research-Symposium)

## What's here

| Folder | Contents |
|---|---|
| [`thesis/`](thesis) | Final thesis PDF and the CEAS research poster |
| [`docs/`](docs) | Presentations (LAMMPS research introduction, blood-flow MD slides), notes on the LJ-type pair potential, plots and figures |
| [`geometry-builders/`](geometry-builders) | Python scripts that generate LAMMPS data files: membranes, spheres, bonded cell models, water/plasma boxes, ten-point and fluid-like membranes. Each project keeps its scripts and small example outputs. |
| [`simulations/`](simulations) | LAMMPS input scripts, one folder per work session (`YYYY-MM-DD Work`), from May to December 2020: bonding and coefficient tests, water–plasma, timestep and potential tests, packing, velocity and wall-hit studies, ELBA water models, and the fluid-like membrane runs |
| [`templates/`](templates) | Reusable membrane input template |
| [`third-party/`](third-party) | Code by other researchers that this work builds on, kept with credit (see below) |

Folder names follow the original work sessions. Version labels (`V1`–`V9`)
record each iteration, `working` / `failed` mark which attempts ran, and an
`_alt2` suffix marks a different file that had the same name in another backup.

## Running an example

Requirements:
- **LAMMPS**: the runs used the 2 Jun 2020 release. Most inputs need the
  `MOLECULE`, `MC` (for `fix bond/create`), `RIGID` and `ASPHERE` packages; the
  water models also need `KSPACE`, and a few runs use `OPENMP`, `MANYBODY`,
  `COLLOID` or `BODY`.
- **Membrane runs** need the `fluidmembrane` pair style and `harmonic1` bond
  style from `third-party/fluidmembrane` compiled into LAMMPS.
- **Python 3 with NumPy** for the geometry builders.

Example: the bonded-membrane test from July 2020.

```bash
cd "simulations/2020-07-27 Work/Bonding Test/V4"
python "../../../../geometry-builders/Bonding_Test/V4/Bonding_Test_V4.py" Bonding_Test_V4.1.data
#   (or copy the ready-made file from geometry-builders/Bonding_Test/V4)
lmp -in in.Bonding_Test_IN_V1
```

Each builder takes the output file name as its first argument (it prompts for
one if none is given), and each input script's `read_data` line names the file
it expects.

Large outputs (trajectory dumps, rendered videos, and data files over 500 KB)
are not included; the builders regenerate the data files.

## Credits

- **fluidmembrane pair style** (`third-party/fluidmembrane`): Fu, S.-P., Peng, Z.,
  Yuan, H., Kfoury, R. & Young, Y.-N., "Lennard-Jones type pair-potential method
  for coarse-grained lipid bilayer membrane simulations in LAMMPS," *Computer
  Physics Communications* 210, 193–203 (2017),
  [doi:10.1016/j.cpc.2016.09.018](https://doi.org/10.1016/j.cpc.2016.09.018). `simulations/Modified Fu Files`
  holds my modified inputs built on it.
- **ELBA force field** (`third-party/elba-lammps-examples`): Orsi, M. & Essex,
  J. W., "The ELBA force field for coarse-grain modeling of lipid membranes,"
  *PLoS ONE* 6(12), e28637 (2011),
  [doi:10.1371/journal.pone.0028637](https://doi.org/10.1371/journal.pone.0028637). The example runs are from the ELBA-LAMMPS
  distribution.
- **LAMMPS–Palabos coupling / validation method:** Tan, J., Sinno, T. R. & Diamond, S. L.,
  "A parallel fluid–solid coupling model using LAMMPS and Palabos based on the
  immersed boundary method," *Journal of Computational Science* 25, 89–100 (2018),
  [doi:10.1016/j.jocs.2018.02.006](https://doi.org/10.1016/j.jocs.2018.02.006),
  [arXiv:1704.04551](https://arxiv.org/abs/1704.04551). The folders named after
  Scott Diamond (`Scott_Test`, `scott_diamond_test`, `scot diamond files`,
  `Scott_testing`, …) are my tests built on this method.
- **LAMMPS:** Thompson, A. P. et al., "LAMMPS – a flexible simulation tool for
  particle-based materials modeling at the atomic, meso, and continuum scales,"
  *Computer Physics Communications* 271, 108171 (2022),
  [doi:10.1016/j.cpc.2021.108171](https://doi.org/10.1016/j.cpc.2021.108171);
  <https://www.lammps.org/>.
- Thanks to Dr. Mahsa Dabagh for mentoring this research.

## License

My own code and input scripts are released under the GNU GPL v3 (see
[LICENSE](LICENSE)). Files in `third-party/` remain under their authors'
original terms. The thesis, poster and presentations are © John Quinn and
are shared for reading, not reuse.

## Related work

This project led to my MS thesis, *Modeling of Circulating Cancer Cells
Subjected to Arterial Flow Conditions* (UW–Milwaukee, 2025).
