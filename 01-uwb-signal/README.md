# 01 — What a UWB signal actually is

Goal: understand, by building it, why a ~2 ns pulse lets you measure time to
picoseconds, and therefore distance to centimeters.

## Concepts

### Short pulses
- A UWB "symbol" is a train of very short pulses, not a continuous carrier.
- 802.15.4 pulse shape: roughly a root-raised-cosine / Gaussian-ish pulse, ~2 ns wide.
- Pulses are modulated onto a carrier (channel 5: 6489.6 MHz, channel 9: 7987.2 MHz).
  For simulation, work at baseband first; the carrier only shifts the spectrum.

### Time vs frequency domain
- Fourier duality: narrow in time <=> wide in frequency.
- Nominal 802.15.4 UWB channel bandwidth: 499.2 MHz. Chip rate: 499.2 MHz.
- Compare: WiFi 20/40/80 MHz, BLE 1-2 MHz. UWB is "ultra" wide because of this.
- Regulatory reason UWB is allowed at all: very low power spectral density (-41.3 dBm/MHz).

### Why bandwidth gives timing resolution
- Rough rule: timing resolution ~ 1 / bandwidth. 1/499.2 MHz ~= 2 ns ~= 60 cm.
  That is the *pulse width*, not the ranging precision.
- Ranging precision is much better than pulse width because you locate the
  *leading edge* or correlation peak, and sharpness of that edge scales with bandwidth.
- DW3000 timestamp unit: 1/(128 * 499.2 MHz) ~= 15.65 ps ~= 4.7 mm.
- Speed of light: c ~= 0.2998 m/ns. Memorize: 1 ns = 30 cm. 1 m = 3.33 ns.

### Wavelength vs bandwidth (don't confuse them)
- Wavelength at 6.5 GHz ~= 4.6 cm. This sets antenna size and phase behavior.
- Bandwidth sets time resolution. Narrowband 6.5 GHz would have the same
  wavelength and terrible timing resolution.

## Project

Write from scratch in Python (numpy + matplotlib):

Order is oscillation-first: see how a bump is assembled from oscillations before taking one apart with the FFT.

1. One cosine at the carrier (8 GHz for channel 9). Fine time step (0.005 ns).
2. Two cosines, 8.0 + 8.5 GHz. See the beat envelope. Overlay the analytic envelope 2*cos(2*pi*0.25*t). Change the second to 8.1, then 8.02: envelope slows as the frequencies get closer.
3. Many cosines: sum N cosines spread evenly across 8 +/- 0.25 GHz, each with a
   Gaussian weight. Start with 3, then 10, then 50. A single bump forms at t0.
   Then narrow the spread to +/- 0.05 GHz and watch the bump widen. This is the
   whole lesson: range of frequencies <-> width of bump.
4. Gaussian envelope times carrier: y * cos(2*pi*8*t). A real UWB pulse. Compare
   to step 3's result.
5. FFT of step 4. Blob at 8 GHz, ~500 MHz wide. Mark the -10 dB bandwidth.
6. FFT of the bare envelope y. Same blob at 0. The envelope owns the bandwidth;
   the carrier only relocates it.
7. Sweep sigma: 0.2, 0.85, 4, 40 ns. Time + spectrum side by side. Bandwidth
   shrinks as width grows. Measure FWHM x bandwidth at each; roughly constant.
8. Pulse train at a repetition interval. Spectrum becomes lines spaced at the PRF.
9. Two pulses separated by dt. Sweep dt downward. At what separation can you no
   longer see two distinct pulses? Relate this to pulse width.

## Break it

- Undersample the pulse (drop sample rate below 2x bandwidth). What happens to the spectrum?
- Make the pulse 100 ns wide. How far apart do two reflections have to be to resolve them now?
- Window the pulse abruptly (rectangular) vs smoothly (Gaussian). Compare the spectral sidelobes.

## Checkpoints

You're done when you can, without notes:

- Explain why a 2 ns pulse has ~500 MHz bandwidth and a 2 us pulse doesn't.
- State what the timing resolution vs ranging precision distinction is.
- Convert between ns and meters instantly.
- Explain why UWB coexists with WiFi/BLE in the same building.
- Point at a spectrum plot and say what the pulse width was.

## Hardware hook

Nothing on the boards yet. But note for lesson 5: DW3000 has a configurable
`TX_PSDU`/pulse shape and a `PRF` (16/64 MHz mean). You'll set those.

## Anki seeds

(Write your own; these are the concepts worth carding.)
- 1 ns <-> 30 cm
- channel 5 / channel 9 center frequencies and nominal bandwidth
- time-bandwidth duality
- timestamp resolution of DW3000 and why it's finer than pulse width
- wavelength vs bandwidth: what each one determines
