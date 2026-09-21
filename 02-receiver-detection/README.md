# 02 — How a receiver finds that signal

Goal: build a detector that takes a noisy sample stream and says "the known
preamble arrived at sample N". This is the software model of what the DW3000
does in hardware; every timestamp downstream comes from this operation.

## Concepts

### Noise and SNR
- Additive white Gaussian noise (AWGN): model receiver thermal noise as
  independent Gaussian samples with variance sigma^2.
- SNR (dB) = 10 log10(P_signal / P_noise). Work in dB; get comfortable
  converting.
- A single 2 ns pulse at the receiver is often *below* the noise floor.
  You can't detect it by looking at one sample. Hence: correlation.

### Correlation
- Cross-correlation of received signal r with known template s:
  c[k] = sum_n r[n] * s[n - k]. Peak at k = arrival offset.
- Matched filter: convolve with the time-reversed template. Same thing.
  It is the optimal linear detector in AWGN (maximizes SNR at the peak).
- Processing gain: correlating over N template samples buys ~10 log10(N) dB.
  This is how sub-noise-floor pulses become detectable.

### Preambles
- The transmitter sends a *known* sequence before the data so the receiver
  can lock on. 802.15.4 UWB uses Ipatov ternary codes (values -1, 0, +1).
- Why Ipatov: perfect periodic autocorrelation (a single sharp peak, flat
  elsewhere). Random sequences have sidelobes that look like false arrivals.
- The preamble is many repetitions of one code symbol (e.g. 64, 128, 1024
  symbols). Receiver accumulates across repetitions: more repetitions = more
  processing gain = works at lower SNR, but longer airtime.
- SFD (start of frame delimiter): a short pattern after the preamble that says
  "preamble over, here's where the data starts". Gives a precise reference point.

### Timing estimation
- Naive: take the correlation peak index. Resolution = 1 sample.
- Sub-sample: parabolic interpolation around the peak, or upsample.
- Leading edge vs peak: in a real channel the *strongest* correlation peak is
  often a reflection. What you want is the *first* significant rise above the
  noise floor. DW3000 does this in hardware (leading-edge detection, reports
  first-path index in 1/64 sample units). Lesson 6 goes deep on this.
- Threshold selection: relative to estimated noise floor, not absolute.

## Project

1. Build the channel: take a template (start with a random +/-1 sequence,
   then switch to a real Ipatov code), place it at a random offset inside a
   longer buffer of zeros, add AWGN at a chosen SNR.
2. Write the detector: cross-correlate, find peak, report arrival index.
   Verify against ground truth. Plot received signal, correlation output,
   and the true arrival on one figure.
3. Sweep SNR from +20 dB down to -20 dB. Plot detection error vs SNR.
   Find where it falls apart.
4. Repeat the code symbol N times (preamble). Accumulate the correlation
   across repetitions. Show the SNR floor drop by ~10 log10(N) dB.
5. Add sub-sample interpolation. Measure timing error in fractions of a sample
   at high SNR.
6. Compare random sequence vs Ipatov code: plot the autocorrelation of each.
   Point at the sidelobes and say why they matter.

## Break it

- Put a *stronger* delayed copy of the signal 5 samples after the first.
  Does your peak detector report the first arrival or the strong one?
  (This is the multipath problem; lesson 6.)
- Slightly mismatch the template (wrong pulse width, slight frequency offset).
  How fast does the correlation peak degrade?
- Reduce preamble repetitions to 1 at low SNR. Watch it fail.
- Add a DC offset or a slow drift to the noise. Does your threshold logic survive?

## Checkpoints

You're done when you can:

- Explain why correlation finds a signal that's below the noise floor.
- State the processing gain of an N-length correlation and where it comes from.
- Say why Ipatov codes and not random bits.
- Explain the difference between "strongest path" and "first path" and why
  a ranging system wants the latter.
- Explain what the SFD is for.
- Look at a correlation plot and estimate the SNR.

## Hardware hook

Every DW3000 RX timestamp is the output of this pipeline. Registers you'll
meet later: preamble code selection (`RX_PCODE`), preamble length (`TXPSR`),
SFD type, and the diagnostic registers that expose first-path index and
first-path power (`IP_DIAG_*`). Keep the mental model: hardware correlator ->
accumulator -> leading-edge detector -> timestamp.

## Anki seeds

- matched filter = correlate with time-reversed template; optimal in AWGN
- processing gain formula
- why Ipatov codes
- preamble length tradeoff: sensitivity vs airtime
- first path vs strongest path
