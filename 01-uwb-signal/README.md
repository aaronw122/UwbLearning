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

1. Generate a single pulse at a chosen sample rate (start ~ 10-20 GS/s so a 2 ns
   pulse has plenty of samples). Gaussian is fine to start.
2. FFT it. Plot magnitude spectrum in dB. Mark the -10 dB bandwidth.
3. Vary pulse width: 0.5 ns, 2 ns, 10 ns, 100 ns. Plot time + spectrum side by side.
   Watch bandwidth shrink as width grows.
4. Modulate onto a carrier (multiply by cos(2*pi*f_c*t)). Show the spectrum
   shifts to f_c but its width doesn't change.
5. Generate a pulse *train* at a pulse repetition interval. Look at the spectrum:
   it becomes lines spaced at the PRF. Understand why.
6. Add two pulses separated by dt. Sweep dt downward. At what separation can
   you no longer see two distinct pulses? Relate this to pulse width.

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
