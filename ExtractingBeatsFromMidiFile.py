from pretty_midi import pretty_midi
import numpy as np
import matplotlib.pyplot as plt

file = pretty_midi.PrettyMIDI('MIDIs/green-hill-zone.mid')

beats = file.get_beats()
time = np.arange(beats.size)

tempo_change_times, tempi = file.get_tempo_changes()

plt.plot([1, 2, 3], [4, 5, 6])
plt.plot(tempo_change_times, tempi)
