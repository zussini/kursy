# Course materials: 2026 additions

This selected set extends [Piotr Kuterba's AI courses](https://github.com/zussini/kursy) with new materials prepared in 2026 for the 2026/2027 academic year. The teaching material is primarily in Polish. Student notebooks are exercise templates, not submitted student work.

## Reinforcement learning

[`reinforcement_learning_2026`](reinforcement_learning_2026) includes bandit experiments and a recycling-robot exercise, followed by dynamic programming, Monte Carlo and TD prediction, SARSA and Q-learning, multistep returns, eligibility traces, Double Q-learning and Dyna-Q. An interactive atlas compares where these algorithms obtain their update targets.

Start with `RL_01_Student/START.txt` for the opening exercises, or `RL_Tabelaryczne_Student/START.html` for the tabular sequence. The two notebooks in `RL_Atlas_i_laboratorium` are complementary worked comparisons. Keep each notebook beside its accompanying Python modules. The selected notebook exercises use Python's standard library; the interactive HTML files open in a browser.

This selection contains the code and interactive materials. The opening lesson also refers to slides and worksheets that are not included here. No completed worksheets or student submissions are included.

## Attention and a mini-Transformer

[`deep_learning_2026`](deep_learning_2026) contains three sequential notebooks: attention heads and independent readouts; a Transformer block with LayerNorm, residual connections and masks; and training a small causal Transformer on synthetic sequences. Keep `mini_transformer_numpy.py` beside the notebooks.

The notebooks use NumPy and Matplotlib on CPU, without downloading a dataset or model weights. Install these packages in a Python environment and open the notebooks in Jupyter or a compatible editor. The notebooks contain further references to companion course material beyond this selection.

## Sources and attribution

These additions belong to the course series maintained in [zussini/kursy](https://github.com/zussini/kursy). The Gridworld exercise links to the [earlier dynamic-programming notebook](https://github.com/zussini/kursy/blob/170b201b2fe8fd1300d2ceb3afffab7cb823c020/reinforcement_learning/notebooks/Ch04_Dynamic_Programming_full.ipynb). The atlas also identifies the [June 2026 course baseline](https://github.com/zussini/kursy/tree/a8dc975f01fc67470003dd9bf8bb9b97f00153fc/reinforcement_learning).

The bandit demonstration credits Sutton and Barto's *Reinforcement Learning: An Introduction*, section 2.3. The atlas retains its references to Sutton and Barto and David Silver. The Transformer-block notebook records the origin of its NumPy implementation, hand calculations and padding test. Existing attribution and public source links are preserved. References to private companion packages remain as text with their private links removed.

When incorporated into the course repository, its existing licensing applies: executable code under [MIT](https://github.com/zussini/kursy/blob/main/LICENSE), and educational text and explanations under [CC BY-NC-SA 4.0](https://github.com/zussini/kursy/blob/main/LICENSE-CONTENT), subject to the attribution and rights of referenced third-party material.
