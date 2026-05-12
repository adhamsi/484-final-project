import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'COS 484 Final Project Results - Sheet1.csv'
df = pd.read_csv(file_path)

def create_dual_axis_plot_poster(data, title, xlabel, filename):
    """Generates a high-visibility plot for posters with large fonts and thick lines."""
    # Ensure data is clean for plotting
    data = data.dropna(subset=[data.columns[0], 'Accuracy', 'Efficiency'])
    
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
    ax2.set_ylabel('Efficiency (-ln(1-p)/c)', color=color_cost, fontsize=LABEL_SIZE, fontweight='bold')
    line2 = ax2.plot(data.iloc[:, 0].astype(float), data['Efficiency'], 
                     marker='s', markersize=MARKER_SIZE, linestyle='--', color=color_cost, 
                     linewidth=LINE_WIDTH, label='Efficiency (-ln(1-p)/c)')
    ax2.tick_params(axis='y', labelcolor=color_cost, labelsize=TICK_SIZE)

    # Title and Legend
    plt.title(title, fontsize=TITLE_SIZE, pad=25, fontweight='bold')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    # ax1.legend(lines, labels, loc='upper left', frameon=True, fontsize=LEGEND_SIZE, shadow=True)

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
                             'Number of nodes kept (b)', 'sampling_experiment.png')

# 2. Evaluations Experiment
sampling_df = df.iloc[12:15].copy()
create_dual_axis_plot_poster(sampling_df, 'Accuracy vs Cost-Efficiency: ToT Evaluations', 
                             'Number of evaluations (v)', 'evaluations_experiment.png')

# 3. CoT 4o-mini
cot_sampling_df = df.iloc[17:21].copy()
create_dual_axis_plot_poster(cot_sampling_df, 'CoT gpt-4o-mini', 
                             'Number of retries (k)', 'cot_4omini_experiment.png')

# 4. CoT 5.4-mini
cot_sampling_df = df.iloc[23:27].copy()
create_dual_axis_plot_poster(cot_sampling_df, 'CoT gpt-5.4-mini', 
                             'Number of retries (k)', 'cot_54mini_experiment.png')