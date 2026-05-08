import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'COS 484 Final Project Results - Sheet1.csv'
df = pd.read_csv(file_path)

def create_dual_axis_plot_poster(data, title, xlabel, filename):
    """Generates a high-visibility plot for posters with large fonts and thick lines."""
    # Ensure data is clean for plotting
    data = data.dropna(subset=[data.columns[0], 'Accuracy', 'Accuracy per dollar'])
    
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Poster-optimized formatting constants
    TITLE_SIZE = 26
    LABEL_SIZE = 22
    TICK_SIZE = 18
    LINE_WIDTH = 5
    MARKER_SIZE = 14
    LEGEND_SIZE = 18

    # Left Axis: Accuracy
    color_acc = 'tab:blue'
    ax1.set_xlabel(xlabel, fontsize=LABEL_SIZE, fontweight='bold')
    ax1.set_ylabel('Accuracy', color=color_acc, fontsize=LABEL_SIZE, fontweight='bold')
    line1 = ax1.plot(data.iloc[:, 0].astype(float), data['Accuracy'], 
                     marker='o', markersize=MARKER_SIZE, color=color_acc, 
                     linewidth=LINE_WIDTH, label='Accuracy')
    ax1.tick_params(axis='y', labelcolor=color_acc, labelsize=TICK_SIZE)
    ax1.tick_params(axis='x', labelsize=TICK_SIZE)
    ax1.grid(True, linestyle='--', alpha=0.7)

    # Right Axis: Accuracy per dollar
    ax2 = ax1.twinx()
    color_cost = 'tab:red'
    ax2.set_ylabel('Accuracy per dollar ($)', color=color_cost, fontsize=LABEL_SIZE, fontweight='bold')
    line2 = ax2.plot(data.iloc[:, 0].astype(float), data['Accuracy per dollar'], 
                     marker='s', markersize=MARKER_SIZE, linestyle='--', color=color_cost, 
                     linewidth=LINE_WIDTH, label='Accuracy per dollar')
    ax2.tick_params(axis='y', labelcolor=color_cost, labelsize=TICK_SIZE)

    # Title and Legend
    plt.title(title, fontsize=TITLE_SIZE, pad=25, fontweight='bold')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', frameon=True, fontsize=LEGEND_SIZE, shadow=True)

    plt.tight_layout()
    # dpi=300 ensures high resolution for physical printing
    plt.savefig(filename, dpi=300)
    plt.close()

# 1. Temperature Experiment
temp_df = df.iloc[0:4].copy()
create_dual_axis_plot_poster(temp_df, 'Accuracy vs Cost-Efficiency: Temperature', 
                             'Temperature', 'temperature_experiment.png')

# 2. Sampling Experiment
sampling_df = df.iloc[6:10].copy()
create_dual_axis_plot_poster(sampling_df, 'Accuracy vs Cost-Efficiency: ToT Sampling', 
                             'ToT Sampling Value (b)', 'sampling_experiment.png')

# 3. CoT Sampling Experiment
cot_sampling_df = df.iloc[12:18].copy()
create_dual_axis_plot_poster(cot_sampling_df, 'Accuracy vs Cost-Efficiency: CoT Sampling', 
                             'CoT Sampling Value (k)', 'cot_sampling_experiment.png')