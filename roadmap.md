# The First-Principles AIML Engineer Roadmap (Master Map)

**Philosophy:** For every topic — *what problem existed before this? what was tried and how did it fail? what did this fix, and what does it break in return?* No trivia, no "who invented it." Definitions are things you *derive* after understanding, never memorize first.

**Target levels per topic (borrowed because it's the right frame):**

- **Know** — can explain correctly, spot it in a system design.
- **Use** — can implement/apply it correctly in a project.
- **Master** — can derive it from scratch, debug it when it breaks, explain trade-offs against alternatives, defend it in an interview whiteboard.

**Ordering logic:** ground-truth systems knowledge first (so abstractions later have something real to attach to), then math (taught by deriving from problems you already understand, not as cold theory), then ML built by "what problem forces this," then specialized layers (CV/NLP/LLMs/GenAI), then the engineering/production/security layer that separates a "model builder" from a hireable engineer, then research skill for FAANG/Anthropic/OpenAI-research-adjacent roles.

**Status legend:** ✅ covered · ⏳ outlined, not yet started · 🖊 needs a from-scratch derivation session, no single resource nails it the derive-it-yourself way

---

## PHASE 0 — How a Computer Actually Runs Your Code ✅ *covered*

Compiled vs interpreted, memory (stack/heap), processes/threads, Python's GIL, why NumPy is fast. **Target: Master.**

---

## PHASE 1 — Programming as a Craft, Not Syntax

Not "learn Python syntax" — learn *why* each language feature exists as a solution to a real pain.

- **Why functions exist**: to name a piece of logic and stop re-writing it → leads naturally to *why recursion works* (a function trusting a smaller version of itself).
- **Why OOP exists**: as codebases grow, data and the logic that changes it get scattered and inconsistent → classes bundle them together. Inheritance/polymorphism exist to avoid duplicating near-identical logic across similar objects. Understand where OOP *helps* and where it over-engineers (a common real interview question).
- **Iterators/generators**: why loading a huge file fully into memory breaks, and how generators solve it by producing one item at a time (lazy evaluation).
- **Decorators**: why you'd want to "wrap" a function's behavior without rewriting it (logging, timing, auth checks) — this is functions-as-values taken to its logical end.
- **Exceptions**: why silent failures are worse than loud ones, and why exception handling exists as a *separate* control flow from normal logic.
- **Type hints / static analysis**: why large Python codebases (like ML pipelines with many contributors) need some of the safety statically-typed languages give for free.
- **Testing**: why "it worked when I ran it" isn't engineering — unit tests exist to catch what changes silently break.
- **Git**: not "commands to memorize" — understand it as a *graph of snapshots*. Branching = a parallel timeline; merging = reconciling two timelines; a merge conflict = the tool honestly telling you it can't guess your intent. This mental model removes 90% of Git confusion forever.

**Target: Master** (Python + Git), **Use** (testing/type systems as full discipline — deepens with experience).

**Resources:**

- *CS50P (Harvard's CS50 Python, free, YouTube)* — teaches Python by building understanding, not memorizing syntax.
- *"Missing Semester" (MIT, free, YouTube)* — the single best resource for Git-as-a-graph, shell, and tooling literacy nobody else teaches properly.

---

## PHASE 2 — Data Structures & Algorithms, By Problem Not By List

The FAANG-interview layer — but taught right, this *is* first-principles computer science, not interview-grinding.

**The one question to hold**: *why would a real system need this shape of data, and what breaks if you used the wrong one?*

- Arrays vs linked lists: contiguous memory (fast random access, slow insertion) vs pointer-chained (slow access, fast insertion) — a direct consequence of Phase 0's memory model.
- Stacks/queues: why "undo" features and "task scheduling" naturally map to these shapes.
- Hash tables: why looking things up by key needs to be O(1) at scale, and how hashing achieves that (and what a collision is and why it matters).
- Trees: why hierarchical/sorted data (file systems, databases indexes) needs a structure better than a flat list; BSTs, then why they can degrade to a linked list (unbalanced) forcing AVL/Red-Black trees.
- Heaps: why "always give me the current minimum/maximum, fast" is a distinct enough need to deserve its own structure (priority queues, scheduling, Dijkstra's algorithm).
- Graphs: why most real-world relationships (social networks, road maps, dependency chains) aren't trees, and BFS/DFS as the two fundamentally different ways to explore them.
- Dynamic programming: not "a trick" — it's *recognizing you're solving the same subproblem repeatedly* and caching the answer. Once you see it this way, DP stops being scary.
- **Big-O**: not notation to memorize — the honest question "if my input doubles, does my runtime stay the same, double, or explode?" This is the single most FAANG-relevant lens for every design decision you'll make in ML pipelines too (does this preprocessing step scale to 10M rows?).

**Target: Master** (this is a hard requirement for FAANG/Anthropic/OpenAI SWE-adjacent interviews).

**Resources:**

- *NeetCode (YouTube)* — explains the *pattern* behind problems (why this is a sliding-window problem), not just solutions — exactly the "understand don't memorize" approach.
- *"Grokking Algorithms" by Aditya Bhargava* — a visual, intuition-first book, genuinely fun, zero unnecessary jargon.

---

## PHASE 3 — Operating Systems & Databases (the invisible infrastructure under every system you'll ever build)

**OS**, deepened from Phase 0: scheduling (how does the CPU decide who runs next when everything wants to run "now"?), virtual memory (why every process *believes* it owns all the RAM — and how that illusion is maintained), deadlocks (why two processes can freeze each other forever, and the conditions required for it), synchronization primitives (locks, semaphores — solving the race-condition problem Phase 0 introduced).

**DBMS** — the question: *how do you store data so it survives crashes, stays consistent under concurrent access, and can be found fast?*

- Relational model: why data got normalized into tables (avoiding duplication/inconsistency) — then why normalization itself sometimes needs to be undone (denormalization for read speed).
- SQL: joins/aggregation aren't syntax to memorize — they're answering "how do I recombine data I deliberately split apart for consistency?"
- **ACID** & transactions: why "partially completed" database writes (e.g., money leaves one account but never arrives in another) are catastrophic, and what each ACID guarantee specifically prevents.
- Indexes: why a database can search a billion rows in milliseconds — and why indexes aren't free (they slow down writes) — a genuine trade-off, not a "just add an index" cheat code.
- NoSQL: born from one honest limitation — rigid schemas and single-machine relational databases don't scale horizontally across many servers easily. Document/key-value/column/graph DBs each optimize for a different access pattern. Know *when* each is the right call, not "NoSQL is modern, SQL is old" (a common wrong belief).

**Target: Master** (OS scheduling/memory/DBMS fundamentals — constant in system design interviews), **Use** (writing complex SQL, running an actual Postgres instance).

**Resources:**

- *"Operating Systems: Three Easy Pieces" (free online, OSTEP)* — the best free OS book, deeply intuition-driven.
- *"Designing Data-Intensive Applications" by Martin Kleppmann* (again — it's this good) for the database/consistency/scaling reasoning.
- *freeCodeCamp SQL course (YouTube)* for hands-on practice.

---

## PHASE 4 — Networking, From First Packet to Your College Portal ⏳ *outlined, not yet started*

OSI/TCP-IP layering (why each layer solves one problem so the layer above doesn't have to), NAT (a patch for IPv4 address scarcity), DNS, TCP vs UDP (reliability vs speed trade-off), HTTP statelessness → why it forced cookies/JWT to exist, firewalls, forward proxy (hides the client) vs reverse proxy (hides the server), then assembling the full request path of a real system end to end (laptop → NAT → firewall → DNS → reverse proxy/load balancer → backend server → database).

**Target: Master.** **Resources:** "High Performance Browser Networking" by Ilya Grigorik (free online), Hussein Nasser (YouTube), PowerCert Animated Videos (YouTube).

---

## PHASE 5 — APIs, Backend Architecture & Auth ⏳ *outlined, not yet started*

Why APIs exist as a contract between systems → RPC (call a remote function, but tightly coupled) → SOAP (rigid, verbose, but strictly contracted) → REST (reused HTTP itself as the contract, why it "won") → where REST strains (over/under-fetching → GraphQL; too slow for internal microservices → gRPC). FastAPI/Flask/Django are *frameworks for building* REST/GraphQL/gRPC APIs, not competitors to REST itself — FastAPI's real edge is native async + auto-validation/docs. Auth evolution: Basic Auth (insecure, sent every request) → Sessions/cookies (server remembers you, doesn't scale across servers) → JWT (stateless, scalable, hard to revoke) → OAuth (delegated access without sharing passwords).

**Target: Master.** **Resources:** Hussein Nasser (YouTube), freeCodeCamp full backend courses (YouTube).

---

## PHASE 6 — Full-Stack, DevOps, Cloud & Distributed Systems

- **Frontend/backend split, CSR vs SSR** (why Next.js exists — fixing React's slow first paint).
- **Caching** (Redis/CDNs) — why re-computing the same expensive thing repeatedly is the actual root cause of most "slow app" complaints.
- **Docker**: solves "works on my machine" by packaging environment + code together.
- **Kubernetes**: solves "one container isn't resilient/scalable enough" by orchestrating many.
- **CI/CD**: solves "manual deployment is slow and error-prone."
- **Cloud fundamentals** (compute/storage/networking/IAM/serverless) — know *why* serverless trades control for zero-ops-overhead, when that trade is worth it.
- **Distributed systems**: horizontal vs vertical scaling, replication, partitioning/sharding, the **CAP theorem** (you cannot have perfect Consistency + Availability during a network Partition — every real distributed system is a deliberate choice of which to sacrifice), eventual consistency, message queues (Kafka) for decoupling systems that shouldn't block each other.

**Target: Use** for Docker/K8s/cloud/CI-CD (enough to deploy and reason about real systems); **Master** for CAP theorem and distributed trade-off reasoning (a favorite system-design interview topic at every top company).

**Resources:**

- *TechWorld with Nana (YouTube)* — Docker/K8s/CI-CD taught by "why," not command lists.
- *"Designing Data-Intensive Applications"* (a third time — it single-handedly covers Phase 3 + Phase 6's distributed-systems reasoning better than anything else that exists).
- *ByteByteGo (YouTube)* — excellent visual system-design breakdowns (CAP theorem, load balancing, caching strategies).

---

## PHASE 7 — Math, Derived From Problems You Already Understand

**Not taught as cold theory — taught by deriving each concept from a concrete need.** For phases marked 🖊, no single external resource nails the "derive it yourself, visualize it" version you want — I'll write those directly, in-thread, step by step with you, when we reach them.

- **Linear Algebra**: vectors as "a list of numbers describing something" (a data point, a direction) → matrix multiplication as "applying a transformation" (rotate/stretch/project data) → *why* this is exactly what a neural network layer does → eigenvectors/eigenvalues as "directions a transformation doesn't rotate, only stretches" → *why* this directly explains PCA (find the directions of maximum spread) and gives intuition for embeddings. 🖊
- **Calculus**: derivative as "how sensitive is the output to a tiny nudge in the input" → gradient as the multivariable version → *why* gradient descent is just "walk downhill, one small step at a time, in the direction that decreases error fastest" — this single idea *is* how every neural network learns. 🖊
- **Probability**: why ML is fundamentally betting under uncertainty, not certainty → Bayes' theorem derived from a simple diagnostic-test example (not memorized formula) → distributions as "shapes of uncertainty" you'll recognize later in loss functions (Gaussian → MSE loss, Bernoulli → cross-entropy loss — these aren't arbitrary, they fall directly out of "assume this distribution, maximize the likelihood"). 🖊
- **Statistics**: bias vs variance derived from an archery-target example, not a formula; hypothesis testing/p-values derived from "how surprised should I be by this result if nothing were actually going on."

**Target: Master** (this is what separates people who can debug *why* a model fails from people who can only call `.fit()`).

**Resources:**

- *3Blue1Brown — "Essence of Linear Algebra" & "Essence of Calculus" (YouTube)* — unmatched visual intuition, watch before we derive together.
- *StatQuest with Josh Starmer (YouTube)* — best plain-language stats/probability-for-ML resource that exists.
- *"Mathematics for Machine Learning" (free PDF, Deisenroth/Faisal/Ong, Cambridge)* — rigorous but readable once intuition is built first from the above.

---

## PHASE 8 — Data Engineering & Exploratory Data Analysis

Before any model: data collection → validation → cleaning (missing values, duplicates, outliers) → transformation (encoding, scaling) → EDA (univariate/bivariate/multivariate analysis, correlation, distribution shape, leakage detection). **The reasoning to internalize**: a model is only as honest as the data pipeline feeding it — most real "ML failures" in industry are data problems wearing a model costume.

**Target: Master.**

**Resources:**

- *Krish Naik (YouTube)* — strong practical Pandas/EDA/feature-engineering walkthroughs grounded in real datasets.
- *Kaggle "Learn" micro-courses (free)* — short, hands-on, surprisingly good for EDA/feature engineering practice.

---

## PHASE 9 — Classical Machine Learning, By Problem Not By Algorithm List

1. Predicting a number → **Linear Regression** (derive the cost function, derive gradient descent updates yourself — don't just import sklearn). Fails on non-linear relationships.
2. Yes/no decision → **Logistic Regression**. Fails on complex non-linear boundaries.
3. Non-linear, human-readable decisions → **Decision Trees** (entropy/information gain/Gini — derived from "which question splits my data most usefully"). Fail by overfitting/memorizing noise.
4. Fixing overfitting via combining many weak trees → **Random Forests** (bagging = averaging independent guesses) vs **Gradient Boosting/XGBoost** (each new tree fixes the previous one's mistakes) — genuinely different philosophies, know why each exists.
5. **k-NN, Naive Bayes, SVM**: each solving classification via a different geometric/probabilistic intuition (nearest neighbors, independence assumption, maximum-margin boundary) — know *when* each assumption holds or breaks.
6. **Unsupervised**: K-means (why iteratively re-centering clusters converges), hierarchical clustering, DBSCAN (density-based — solves K-means's "must know K in advance and assumes round clusters" weakness). PCA/t-SNE/UMAP for dimensionality reduction — *why* high-dimensional data is hard to reason about (curse of dimensionality) and what each technique trades off (PCA = linear/fast/interpretable; t-SNE/UMAP = non-linear/better visualization/less interpretable globally).
7. **Evaluation**: why accuracy lies on imbalanced data → precision/recall/F1 derived from a real confusion matrix, not memorized formulas; ROC-AUC as "how well does this model rank positives above negatives regardless of threshold."
8. **ML theory**: bias-variance trade-off, overfitting/underfitting, cross-validation (why a single train/test split can mislead you), regularization (L1/L2 — deriving *why* penalizing large weights fights overfitting), data leakage (the single most common real-world bug that makes a model look great and then fail completely in production).

**Target: Master** for regression/logistic/trees/NNs/evaluation/bias-variance; **Use + understand deeply** for boosting variants, SVM, clustering.

**Resources:**

- *StatQuest (YouTube)* — again, unmatched for this entire phase.
- *Andrew Ng's Machine Learning Specialization (Coursera, audit free)* — the industry-standard intuition-first course.

---

## PHASE 10 — Deep Learning Core

Single neuron/perceptron → fails on non-linearly-separable data (XOR problem) → stacking layers + non-linear activation functions (Sigmoid/Tanh/ReLU — *why* ReLU mostly won: cheap to compute, fights vanishing gradients) → **backpropagation** derived as repeated chain rule (don't memorize the algorithm — derive it by hand on a 2-layer network once, it demystifies deep learning permanently) → optimizers (SGD → Momentum → RMSProp → Adam, each fixing a specific failure of the previous: Momentum fixes oscillation, Adam adapts per-parameter learning rates) → weight initialization (why starting all weights at zero breaks learning) → **regularization for deep nets**: dropout (randomly disabling neurons — why this fights co-dependency/overfitting), batch normalization (why normalizing activations mid-network stabilizes training), early stopping.

Then **PyTorch**: tensors, autograd (understand it as "the computational graph that makes backprop automatic" — not magic), `nn.Module`, training loops, GPU/CUDA (*why* matrix multiplication parallelizes beautifully on GPU architecture — ties back to Phase 0's compute model).

**Target: Master.**

**Resources:**

- *Andrej Karpathy — "Neural Networks: Zero to Hero" (YouTube)* — builds backprop and a GPT from raw Python, line by line. The single best deep learning resource that exists for exactly your learning style.
- *3Blue1Brown's neural network series* for visual grounding before Karpathy's code-first approach.

---

## PHASE 11 — Computer Vision

Why images need a different architecture than plain neural nets: a fully-connected net on a 224×224 image has *millions* of redundant parameters and no concept of "an edge here looks like an edge there." **Convolution** fixes this — a small filter shared across the whole image, detecting the same pattern anywhere (edges → shapes → object parts → objects, layer by layer — this hierarchy is the actual reason CNNs work, not a coincidence). Pooling for spatial compression, receptive fields for "how much of the image can one neuron 'see.'" Architecture evolution (LeNet → AlexNet → VGG → ResNet) each solving the previous one's specific limitation (ResNet's residual connections specifically fixing *vanishing gradients in very deep networks* — a direct callback to Phase 10's backprop). Then object detection (bounding boxes, IoU, YOLO's single-pass philosophy vs two-stage detectors), segmentation (pixel-level classification), and modern Vision Transformers/CLIP (treating image patches like words — a direct bridge to Phase 12).

**Target: Master core CNN reasoning; Use for detection/segmentation architectures; Know modern ViT/CLIP.**

**Resources:**

- *CS231n (Stanford, free lecture videos + notes online)* — the canonical, derivation-heavy computer vision course.

---

## PHASE 12 — NLP, Attention & Transformers

Text preprocessing/tokenization/TF-IDF as the "dumb but honest" baseline → why counting words loses all meaning/order → word embeddings (Word2Vec — *why* representing a word by "what words tend to appear near it" captures real semantic meaning, provably, e.g. king − man + woman ≈ queen) → RNN/LSTM (processing sequences step by step, carrying memory forward) → their real failure: sequential processing can't parallelize, and memory decays over long sequences → **self-attention**, derived as "let every word directly look at every other word and decide how much to pay attention to it" (Query/Key/Value is just a searchable-database metaphor made differentiable) → multi-head attention (why one "view" of relationships isn't enough) → positional encoding (since attention has no built-in sense of order, unlike RNNs) → the full Transformer (encoder/decoder, residual connections, layer norm) — and *why* this architecture is what made massive-scale parallel training (and therefore LLMs) possible at all.

**Target: Master** — this is the single highest-leverage topic for any 2026 AI role, research or applied.

**Resources:**

- *Andrej Karpathy's "Let's build GPT from scratch" (YouTube)* — builds a working transformer line by line.
- *"The Illustrated Transformer" by Jay Alammar (free blog)* — the best visual walkthrough of attention that exists.

---

## PHASE 13 — LLMs & LLM Engineering

**LLM theory**: next-token prediction as the entire "party trick" underlying seemingly-intelligent behavior; pretraining (learning language/world patterns from raw text) vs fine-tuning (specializing); instruction tuning and RLHF/DPO (*why* a raw pretrained model is a text-completer, not an assistant, and what alignment training actually changes); tokenization (BPE — why sub-word tokens, not whole words, solve the "unknown word" problem); context windows, temperature/top-k/top-p (derived as "how do you turn a probability distribution over next words into an actual choice, and how much randomness do you allow").

**LLM Engineering** (the applied, hireable layer): prompting as software engineering (structured outputs, few-shot examples, system prompts); **RAG** (why LLMs hallucinate/have stale knowledge, and how retrieval — chunking, embeddings, vector databases, reranking — grounds generation in real, current data); **agents** (tool calling, planning, memory/state, multi-step workflows — and honestly, *why* agent reliability is still one of the hardest unsolved production problems, worth understanding the failure modes deeply); **fine-tuning at scale**: full fine-tuning vs LoRA/QLoRA/PEFT (why updating all parameters of a billion-parameter model is often wasteful, and how low-rank updates capture most of the benefit for a fraction of the cost) and quantization (trading numeric precision for memory/speed).

**Target: Master** theory + RAG + prompting; **Use** for fine-tuning/agents (deepens fast with hands-on projects — build a real RAG app, not a tutorial clone).

**Resources:**

- *Karpathy's "Let's build the GPT Tokenizer" and "Intro to LLMs" (YouTube)*.
- *DeepLearning.AI's short courses on RAG/LangChain/agents (free)* — practical, current, hands-on.

---

## PHASE 14 — Generative AI Beyond LLMs

Autoencoders (compress → reconstruct, learning a compact representation) → Variational Autoencoders (making that compressed space *smooth and sample-able*, so you can generate new data, not just reconstruct) → GANs (two networks in an adversarial game — a generator trying to fool a discriminator — *why* this produces sharp realistic outputs but is notoriously unstable to train) → Diffusion models (the current state of the art for images: learn to reverse a gradual noising process — genuinely different philosophy from GANs, more stable to train, why it won). Multimodal models (text↔image↔audio, shared embedding spaces like CLIP).

**Target: Know deeply; Use for diffusion/multimodal if it's a specific interest.**

**Resources:**

- *3Blue1Brown/Computerphile explainer videos on GANs and diffusion* for visual intuition before any paper.

---

## PHASE 15 — Recommender Systems, Time Series, Reinforcement Learning *(specialize based on interest)*

- **Recommenders**: content-based (similarity of item features) vs collaborative filtering (similarity of user behavior) vs matrix factorization (learning latent taste dimensions) — this is a genuinely different paradigm from supervised learning, worth knowing even outside a recsys-specific role.
- **Time series**: why i.i.d. assumptions in classical ML break for sequential/temporal data (autocorrelation), classical (ARIMA) vs modern (LSTM/Temporal CNN/Transformer-based forecasting).
- **RL**: agent/environment/reward/policy framed as "learning by trial and consequence, not by labeled examples" — a fundamentally different learning paradigm from everything in Phase 9-13. Bellman equation derived from "the value of a decision = immediate reward + discounted value of what follows" — genuinely elegant once derived, not memorized. Q-learning → DQN (why neural nets were needed once state spaces got too large for a lookup table) → policy gradients/PPO (directly learning the decision-making function instead of scoring every option).

**Target: Know** all three; **Master** only the one matching your eventual specialization (RL is increasingly relevant for agent/LLM post-training work at labs like Anthropic/OpenAI, worth extra attention if that's your direction).

**Resources:**

- *David Silver's RL Course (DeepMind, free, YouTube)* — the canonical, derivation-first RL course.

---

## PHASE 16 — MLOps, Deployment & Production Engineering

The gap between "model scores well in a notebook" and "model survives contact with the real world": experiment tracking/model versioning (MLflow, DVC — *why* "just remember which model.pkl was good" fails at team scale), model serving (real-time vs batch inference, and the latency/cost/accuracy triangle you're always trading off), **data drift vs concept drift** (the world changing under your model's feet — the actual #1 cause of "our AI got worse over time" incidents), monitoring/alerting, A/B testing before full rollout, model optimization for deployment (ONNX, quantization — same idea as LoRA/quantization from Phase 13, now applied to any model), caching/load balancing at the serving layer (a direct callback to Phase 4-6).

**Target: Use** deeply — this phase is exactly where "I can build a model" becomes "I can ship and maintain a product," the difference FAANG/frontier-lab interviews specifically probe for.

**Resources:**

- *"Designing Machine Learning Systems" by Chip Huyen* — the best production-ML book, written in exactly this why-did-it-break/what-fixed-it style.
- *Made With ML (free online course, madewithml.com)* — excellent practical MLOps walkthrough.

---

## PHASE 17 — AI Security, Responsible AI & Explainability

**Security**: prompt injection (why an LLM can't reliably distinguish "instructions" from "data" it's shown — a structural problem, not a bug to patch away), jailbreaking, data/model poisoning (corrupting training data or the model itself), adversarial examples (tiny, human-imperceptible input changes that fool a model — revealing that models learn different features than humans assume), membership inference/model extraction attacks (can an attacker learn what data trained the model, or steal the model itself via queries?).

**Responsible AI**: fairness/bias (where does biased training data become biased real-world outcomes, concretely), explainability (SHAP/LIME/Grad-CAM — *why* "the model said so" isn't good enough for high-stakes decisions, and what these tools actually approximate — correlation of feature importance, **not** causal proof, a distinction worth holding onto), hallucination and human oversight for LLM systems specifically.

**Target: Know deeply** — increasingly a direct interview topic at safety-focused labs (Anthropic especially) and a genuine differentiator, since most AIML students skip this entirely.

**Resources:**

- *Anthropic's own research blog (anthropic.com/research)* — genuinely the best primary source for current thinking on AI safety/alignment/interpretability, directly relevant if a lab like this is a goal.
- *"Interpretable Machine Learning" by Christoph Molnar (free online book)* for SHAP/LIME/explainability depth.

---

## PHASE 18 — Research Skills (for 4th-year/grad-school/research-track roles)

How to actually read a paper (abstract → figures → method → results, in that order, not linearly); understanding math in papers without getting stuck (identify what's genuinely novel vs. standard notation); reproducing a paper's core result from scratch (the single best way to *prove* you understood it); designing experiments with real baselines and ablations (changing one thing at a time to isolate what actually mattered); honestly analyzing failure cases instead of only reporting wins.

**Landmark ideas worth understanding deeply** (not memorizing): AlexNet (why deep CNNs suddenly became trainable), ResNet (residual connections solving vanishing gradients), "Attention Is All You Need" (the transformer paper), BERT vs GPT-style architectures (encoder-only vs decoder-only — different pretraining objectives, different use cases), ViT, GANs/VAEs/diffusion, DQN/PPO, LoRA, CLIP.

**Target: Use** if research-track is a real goal; otherwise **Know** the landmark ideas — they come up constantly in interviews as "explain how X works" questions.

**Resources:**

- *Yannic Kilcher (YouTube)* — paper walkthroughs that explain *why* a paper's idea works, not just what it says.
- *"How to Read a Paper" by S. Keshav (short free PDF)* — the actual method, not vague advice.

---

### How to actually use this

This is the full master map — treat it as the destination, not a weekly checklist. Go phase by phase, in order, and inside each phase, resist the urge to skip to code before the "why" clicks. Phases marked 🖊 (math derivations) are meant to be worked through interactively with Claude, step by step, visually — no formula should be handed over without seeing where it came from.