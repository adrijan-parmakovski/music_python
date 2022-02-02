import numpy as np
import plotly.graph_objects as go

A4 = 440 # A4 is tuned to 440Hz

def get_sine_wave(
    frequency: float,
    duration: float,
    sample_rate: int = 44100,
    amplitude: int = 4096):

    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=wave, name=f"{frequency} Hz"))
    fig.show()

def plot_chord(
    frequencies: list = [261.63,  329.63,  392.00],
    duration: float = 0.03,
    sample_rate: int = 44100,
    amplitude: int = 4096):

    t = np.linspace(0, duration, int(sample_rate * duration)) # Time axis
    c_wave = amplitude * np.sin(2 * np.pi * 261.63 * t)
    e_wave = amplitude * np.sin(2 * np.pi * 329.63 * t)
    g_wave = amplitude * np.sin(2 * np.pi * 392.00 * t)
    bb_wave = amplitude * np.sin(2 * np.pi * 466.16 * t)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=c_wave, name=f"C"))
    fig.add_trace(go.Scatter(x=t, y=e_wave, name=f"E"))
    fig.add_trace(go.Scatter(x=t, y=g_wave, name=f"G"))
    fig.add_trace(go.Scatter(x=t, y=bb_wave, name=f"Bb"))
    fig.show()



if __name__ == '__main__':
    
    plot_chord()
