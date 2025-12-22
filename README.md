# awesome-reinforced-learning
A repository of articles, papers, and books on Reinforce Learning (RL)


## Bibliography

<!-- BEGIN_AUTO_BIBLIOGRAPHY -->
<!-- This section is auto-generated from refs/references.bib. -->

- **`tapenade2025survey`** — **Comprehensive Survey of Reinforcement Learning** (2025). *MDPI*.
  - _Why it matters_: A recent survey covering traditional RL to modern deep RL, valuable for mapping trends and research directions.
- **`behrouz2024titans`** — **Titans: Learning to Memorize at Test Time** (2024). [DOI](https://doi.org/10.48550/arXiv.2501.00663) · [Link](https://arxiv.org/abs/2501.00663)
- **`ha2018recurrentworldmodels`** — **Recurrent World Models Facilitate Policy Evolution** (2018). *Advances in Neural Information Processing Systems 31 (NeurIPS 2018)*. [Link](https://arxiv.org/abs/1809.01999)
  - _Why it matters_: Shows training/optimizing policies inside a learned recurrent world model and transferring back to the real env; key for “imagination-based” control.
- **`ha2018worldmodels`** — **World Models** (2018). [DOI](https://doi.org/10.5281/zenodo.1207631) · [Link](https://zenodo.org/record/1207631)
  - _Why it matters_: Seminal modern world-model paper: learn latent dynamics (VAE + RNN) and train policies using model features or entirely “in imagination,” influencing a large wave of model-based RL.
- **`hessel2018rainbow`** — **Rainbow: Combining Improvements in Deep Reinforcement Learning** (2018). *AAAI*.
  - _Why it matters_: Unified “Rainbow” agent that integrates multiple DQN enhancements (Double, Prioritized Replay, Distributional, etc.), setting a strong benchmark in deep RL.
- **`sutton2018reinforcement`** — **Reinforcement Learning: An Introduction** (2018). *MIT Press*.
  - _Why it matters_: The foundational textbook in RL, covering theory and core algorithms such as dynamic programming, TD learning, and policy gradient methods — essential for anyone studying RL.
- **`worldmodels2018interactive`** — **World Models (Interactive Project Page)** (2018). [Link](https://worldmodels.github.io/)
  - _Why it matters_: Canonical companion site with explanations and demos; great link target for an Awesome list entry.
- **`haarnoja2017softq`** — **Reinforcement Learning with Deep Energy-Based Policies** (2017). *arXiv preprint*.
  - _Why it matters_: Soft Q-learning / maximum entropy RL, advancing exploration and robustness in continuous control.
- **`schulman2017ppo`** — **Proximal Policy Optimization Algorithms** (2017). *arXiv preprint arXiv:1707.06347*. [Link](https://arxiv.org/abs/1707.06347)
- **`schulman2017ppo`** — **Proximal Policy Optimization Algorithms** (2017). *arXiv preprint*.
  - _Why it matters_: PPO presents a simpler and efficient policy gradient method widely used in modern deep RL applications due to its robustness and performance.
- **`silver2017alphagozero`** — **Mastering the game of Go without human knowledge** (2017). *Nature*.
  - _Why it matters_: AlphaGo Zero learns tabula-rasa with self-play and reinforcement learning, illustrating the power of purely algorithmic learning.
- **`mnih2016asynchronous`** — **Asynchronous Methods for Deep Reinforcement Learning** (2016). *ICML*.
  - _Why it matters_: Introduces A3C, a scalable parallel policy gradient method that helped the field move beyond purely value-based deep RL.
- **`silver2016alphago`** — **Mastering the game of Go with deep neural networks and tree search** (2016). *Nature*.
  - _Why it matters_: AlphaGo demonstration of combining deep RL with Monte Carlo Tree Search to reach superhuman performance, cementing RL’s prominence in game AI.
- **`vanhasselt2016double`** — **Deep Reinforcement Learning with Double Q-Learning** (2016). *AAAI*.
  - _Why it matters_: Introduces Double DQN to reduce overestimation bias in Q-learning, improving stability and performance in deep RL.
- **`lillicrap2015ddpg`** — **Continuous control with deep reinforcement learning** (2015). *arXiv preprint*.
  - _Why it matters_: Deep Deterministic Policy Gradient (DDPG) extends deep RL to high-dimensional continuous action spaces using an actor-critic approach.
- **`mnih2015dqn`** — **Human-level control through deep reinforcement learning** (2015). *Nature*. [DOI](https://doi.org/10.1038/nature14236)
- **`mnih2015dqn`** — **Human level control through deep reinforcement learning** (2015). *Nature*.
  - _Why it matters_: The Deep Q-Network (DQN) paper that ignited modern deep reinforcement learning by training an end-to-end neural agent on Atari games from pixels.
- **`schmidhuber2015deeplearningoverview`** — **Deep Learning in Neural Networks: An Overview** (2015). *Neural Networks*. [DOI](https://doi.org/10.1016/j.neunet.2014.09.003)
  - _Why it matters_: Broad, highly cited overview that also connects deep learning, sequence models, and RL threads (useful “bridge reference” in an Awesome RL repo).
- **`schmidhuber2015learning`** — **On Learning to Think: Algorithmic Information Theory for Novel Combinations of Reinforcement Learning Controllers and Recurrent Neural World Models** (2015). [DOI](https://doi.org/10.48550/arXiv.1511.09249) · [Link](https://arxiv.org/abs/1511.09249)
- **`schulman2015trust`** — **Trust Region Policy Optimization** (2015). *ICML*.
  - _Why it matters_: TRPO improves policy gradient learning by enforcing trust regions for more stable updates, a precursor to PPO.
- **`wierstra2014nes`** — **Natural Evolution Strategies** (2014). *Journal of Machine Learning Research*.
  - _Why it matters_: Key neuroevolution / black-box optimization method often used as an RL alternative; important in the ES-vs-RL lineage and policy search.
- **`koutnik2013evolving`** — **Evolving Large-Scale Neural Networks for Vision-Based Reinforcement Learning** (2013). *Proceedings of the 15th Annual Conference on Genetic and Evolutionary Computation (GECCO '13)*. [DOI](https://doi.org/10.1145/2463372.2463509)
  - _Why it matters_: High-impact neuroevolution + RL from raw pixels; helps ground the “evolutionary RL / policy search” branch tied to IDSIA work.
- **`cuccu2011intrinsicneuroevolution`** — **Intrinsically Motivated Neuroevolution for Vision-Based Reinforcement Learning** (2011). *2011 IEEE International Conference on Development and Learning (ICDL)*. [DOI](https://doi.org/10.1109/DEVLRN.2011.6037324)
  - _Why it matters_: Combines intrinsic motivation + neuroevolution for RL from pixels; relevant precursor to modern curiosity+representation learning pipelines.
- **`schmidhuber2010intrinsicmotivation`** — **Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990--2010)** (2010). *IEEE Transactions on Autonomous Mental Development*. [DOI](https://doi.org/10.1109/TAMD.2010.2056368)
  - _Why it matters_: Theory backbone for curiosity-driven exploration: intrinsic reward via compression progress / learning progress; widely cited in intrinsic-motivation RL.
- **`sehnke2010pgpe`** — **Parameter-Exploring Policy Gradients** (2010). *Neural Networks*. [DOI](https://doi.org/10.1016/j.neunet.2009.12.004)
  - _Why it matters_: Influential policy-search method (parameter-space exploration) for RL/POMDP control with lower-variance gradient estimates.
- **`schmidhuber2006developmentalrobotics`** — **Developmental Robotics, Optimal Artificial Curiosity, Creativity, Music, and the Fine Arts** (2006). *Connection Science*. [DOI](https://doi.org/10.1080/09540090600768658)
  - _Why it matters_: Accessible synthesis of optimal curiosity and intrinsic motivation ideas that later reappear across exploration-heavy RL methods.
- **`hochreiter1997lstm`** — **Long Short-Term Memory** (1997). *Neural Computation*. [DOI](https://doi.org/10.1162/neco.1997.9.8.1735)
  - _Why it matters_: Core sequence-memory architecture; enables practical RL in partially observable environments and underpins many world-model approaches.
- **`wiering1997hqlearning`** — **HQ-Learning** (1997). *Adaptive Behavior*. [DOI](https://doi.org/10.1177/105971239700600202)
  - _Why it matters_: Hierarchical / decomposition-flavored RL ideas for POMDP-like settings; helps connect memory + hierarchy themes in Schmidhuber’s RL work.
- **`tesauro1995tdgammon`** — **Temporal difference learning and TD-Gammon** (1995). *Communications of the ACM*.
  - _Why it matters_: A pioneering neural network + RL system that achieved expert-level backgammon play using TD(λ), showing the power of combining learning with neural networks.
- **`schmidhuber1992historycompression`** — **Learning Complex, Extended Sequences Using the Principle of History Compression** (1992). *Neural Computation*. [DOI](https://doi.org/10.1162/neco.1992.4.2.234)
  - _Why it matters_: Memory and representation learning for long temporal dependencies; highly relevant to POMDP RL and predictive world modeling.
- **`watkins1992qlearning`** — **Q-Learning** (1992). *Cambridge University Engineering Department*.
  - _Why it matters_: Introduces Q-learning, a foundational off-policy RL algorithm for discrete action spaces; basis for many later extensions (e.g., DQN).
- **`williams1992reinforce`** — **Simple statistical gradient-following algorithms for connectionist reinforcement learning** (1992). *Machine Learning*.
  - _Why it matters_: Defines the REINFORCE policy gradient algorithm, a foundational on-policy method directly optimizing expected returns.
- **`schmidhuber1991curiosityboredom`** — **A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers** (1991). *From Animals to Animats: Proceedings of the First International Conference on Simulation of Adaptive Behavior*. [DOI](https://doi.org/10.7551/mitpress/3115.003.0030)
  - _Why it matters_: Foundational intrinsic reward idea (novelty / learning progress) for exploration—still central in curiosity-driven RL.
- **`schmidhuber1991curiousmodelbuilding`** — **Curious Model-Building Control Systems** (1991). *Proceedings of the International Joint Conference on Neural Networks (IJCNN)*.
  - _Why it matters_: A core intrinsic-motivation formulation: agents act to improve their world model (curiosity), shaping modern exploration methods in RL.
- **`DBLP:conf/nips/Schmidhuber90`** — **Reinforcement Learning in Markovian and Non-Markovian Environments** (1990). *Advances in Neural Information Processing Systems 3 (NIPS 1990)*. [Link](http://papers.nips.cc/paper/393-reinforcement-learning-in-markovian-and-non-markovian-environments)
  - _Why it matters_: Early treatment of RL under partial observability/non-Markov settings—an enduring theme for world models + memory-based agents.
- **`schmidhuber1990makingworlddifferentiable`** — **Making the World Differentiable: On Using Self-Supervised Fully Recurrent Neural Networks for Dynamic Reinforcement Learning and Planning in Non-Stationary Environments** (1990). *Institut f\"ur Informatik, Technische Universit\"at M\"unchen*.
  - _Why it matters_: Classic technical report on training recurrent predictive models of the environment and using them for RL/planning under non-stationarity.
- **`schmidhuber1990onlinealgorithm`** — **An On-Line Algorithm for Dynamic Reinforcement Learning and Planning in Reactive Environments** (1990). *Proceedings of the International Joint Conference on Neural Networks (IJCNN)*. [DOI](https://doi.org/10.1109/IJCNN.1990.137723)
  - _Why it matters_: Early differentiable model-based RL: recurrent world model + planning/control ideas that anticipate later “world model” lines of work.
- **`sutton1988tdlearning`** — **Learning to predict by the methods of temporal differences** (1988). *Machine Learning*.
  - _Why it matters_: Introduces temporal-difference (TD) learning, a cornerstone of RL that precedes and underlies many later methods such as Q-learning.
<!-- END_AUTO_BIBLIOGRAPHY -->
