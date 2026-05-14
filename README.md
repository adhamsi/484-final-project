# Exploring the Tree of Thoughts Framework Through Hyperparameter Adjustment, Efficiency Analysis, and a Novel Task

## Yusuf Abdelnur (ya1653@princeton.edu), Ayaat Al-Yasseri (aa1461@princeton.edu), Adham Ibrahim (ai0492@princeton.edu)

This repository contains the code used for a COS 484, Natural Language Processing, Final Report.

_Abstract_:

This study seeks to build upon and evaluate the Tree of Thoughts (ToT) framework, a method to improve the reasoning capabilities of models through prompt engineering. This work evaluates ToT in three ways. First, we conduct hyperparameter testing to try and improve model performance and cost efficiency, using the Game of 24 task. Secondly, we compare the performance between ToT and the Chain of Thought (CoT) framework and between gpt-4o-mini and gpt-5.4-mini, and discuss a precise metric to evaluate the relative performance of different model settings. Finally, we test ToT’s ability on a new task, 9x9 Sudoku.

This study finds that by adjusting hyperparameters of both the LLM model and ToT framework the efficiency and accuracy of the model can be tuned, and we analyze the performance and cost differences under these modifications. The efficiency analysis confirms that even with the improvements to cost through hyperparameter optimization, there is a significant gap in the effiency between CoT and ToT as measured by the ratio of accuracy to cost per task. Finally, we extended the original ToT framework by introducing Sudoku as a new reasoning benchmark. We find that ToT improves the performance on the Sudoku task in comparison to CoT, both in general board-solving accuracy and individual-cell accuracy.

The results can be found in `/logs/game24` and `/logs/sudoku`.
