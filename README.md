# UWB Learning

nand2tetris-style course on ultra-wideband localization. Bottom abstraction:
"a waveform travels through space; how does hardware turn its arrival time into a number?"
Then open every black box between electromagnetic signal and (x, y, z).

Hardware: Qorvo DWM3001CDK (nRF52833 + DW3110). Four boards = four anchors.

## Rule

simulate it -> visualize it -> break it -> understand why -> test it on real hardware

## Cadence

- During Recurse batch: foundations, simulation, firmware (lessons 1-10).
- Outside batch: keep implementing on the real system (11-12, AR integration).
- Every day: anki cards + reflection in `journal/`.

## Lessons

| # | folder | topic | status |
|---|--------|-------|--------|
| 0 | `00-toolchain/` | flash, debug, serial on the DWM3001CDK (pre-batch) | |
| 1 | `01-uwb-signal/` | what a uwb signal actually is | |
| 2 | `02-receiver-detection/` | how a receiver finds that signal | |
| 3 | `03-the-chip/` | meet the actual uwb chip | |
| 4 | `04-first-firmware/` | first firmware: read DEV_ID over SPI | |
| 5 | `05-uwb-packets/` | uwb packets; transmit your first frame | |
| 6 | `06-propagation-multipath/` | propagation, CIR, LOS/NLOS | |
| 7 | `07-timing-hardware/` | where the timestamp physically comes from | |
| 8 | `08-ranging/` | ToF, SS-TWR, DS-TWR in firmware | |
| 9 | `09-ranging-errors/` | clock drift, antenna delay, multipath bias, body blocking | |
| 10 | `10-localization/` | trilateration, TDoA, DL-TDoA | |
| 11 | `11-real-systems/` | sync, scheduling, quality, tracking, fusion | |
| 12 | `12-final-project/` | own firmware -> raw timing/CIR -> 3D position | |

Lessons 1-2 are elaborated. 3-12 are shells; fill each in when you reach it,
since what you learn earlier will change what the later ones should be.

## Layout

Each lesson folder: `README.md` (goals, project, checkpoints, break-it experiments),
plus whatever code/notebooks/notes you write. When sim code gets reused across
lessons, pull it into a shared `sim/` package rather than copy-pasting.

`journal/` holds daily reflections (`YYYY-MM-DD.md`).

## External

GT CS8803 Mobile Computing & IoT (Dhekne): https://faculty.cc.gatech.edu/~dhekne/cs8803/course.html
Its UWB papers and assignment shapes are referenced from lessons 8-11. It starts
at the ranging API; lessons 3-7 here go below that.
