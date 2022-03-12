# Exploring Data Aalysis in MIDI format using the following link:
# https://www.kaggle.com/wfaria/midi-music-data-extraction-using-music21/notebook
import numpy as np
import pandas as pd
import wget
import os
from pretty_midi import pretty_midi
from music21 import converter, corpus, instrument, midi, note, chord, pitch

midi_path = "MIDIs"

sonic_folder = "sonic"

# os.removedirs(midi_path)
# os.makedirs(midi_path)


def concat_path(path, child):
    return path+"/"+child


def download_midi(midi_url, path):
    wget.download(midi_url, out=path)


sonic_path = concat_path(midi_path, sonic_folder)
url = "https://files.khinsider.com/midifiles/genesis/sonic-the-hedgehog/green-hill-zone.mid"
# download_midi(url, sonic_path)


def open_midi(midi_path, remove_drums):
    mf = midi.MidiFile()  # Read Midi file
    mf.open(midi_path)
    mf.read()
    mf.close()
    if (remove_drums):
        for i in range(len(mf.tracks)):
            mf.tracks[i].events = [
                ev for ev in mf.tracks[i].events if ev.channel != 10]
    return midi.translate.midiFileToStream(mf)


base_midi = open_midi(concat_path(midi_path, "green-hill-zone.mid"), True)
print(base_midi)

# Listing instrument used in the music


def list_instruments(midi):
    partStream = midi.parts.stream()
    print("List of Instruments found on MIDI file")
    for p in partStream:
        aux = p
        print(p.partName)


list_instruments(base_midi)
