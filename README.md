## Updated on 2026.02.14

## Categories

- [Manipulation](#manipulation)
- [World Model](#world-model)
- [VLM](#vlm)
- [VLA](#vla)
- [Humanoid](#humanoid)

## Manipulation

|Publish Date|Title|Chinese Summary|Authors|PDF|Code|
|---|---|---|---|---|---|
|**2026-02-12**|**FAIL: Flow Matching Adversarial Imitation Learning for Image Generation**||Weidi Xie Team|[2602.12155](http://arxiv.org/abs/2602.12155)|null|
|**2026-02-12**|**GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning**||Zheng Zhu Team|[2602.12099](http://arxiv.org/abs/2602.12099)|**[link](https://gigabrain05m.github.io/)**|
|**2026-02-12**|**Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable Embodied Learning**||Changshui Zhang Team|[2602.12065](http://arxiv.org/abs/2602.12065)|null|
|**2026-02-12**|**HoloBrain-0 Technical Report**||Zhizhong Su Team|[2602.12062](http://arxiv.org/abs/2602.12062)|null|
|**2026-02-12**|**When would Vision-Proprioception Policies Fail in Robotic Manipulation?**||Di Hu Team|[2602.12032](http://arxiv.org/abs/2602.12032)|null|
|**2026-02-12**|**Accelerating Robotic Reinforcement Learning with Agent Guidance**||Yaodong Yang Team|[2602.11978](http://arxiv.org/abs/2602.11978)|null|
|**2026-02-12**|**Robot-DIFT: Distilling Diffusion Features for Geometrically Consistent Visuomotor Control**||Georgia Chalvatzaki Team|[2602.11934](http://arxiv.org/abs/2602.11934)|null|
|**2026-02-12**|**JEPA-VLA: Video Predictive Embedding is Needed for VLA Models**||Mingsheng Long Team|[2602.11832](http://arxiv.org/abs/2602.11832)|null|
|**2026-02-12**|**Clutt3R-Seg: Sparse-view 3D Instance Segmentation for Language-grounded Grasping in Cluttered Scenes**||Ayoung Kim Team|[2602.11660](http://arxiv.org/abs/2602.11660)|null|
|**2026-02-12**|**ViTaS: Visual Tactile Soft Fusion Contrastive Learning for Visuomotor Learning**||Huazhe Xu Team|[2602.11643](http://arxiv.org/abs/2602.11643)|null|
|**2026-02-12**|**EasyMimic: A Low-Cost Framework for Robot Imitation Learning from Human Videos**||Qin Jin Team|[2602.11464](http://arxiv.org/abs/2602.11464)|null|
|**2026-02-12**|**Scaling World Model for Hierarchical Manipulation Policies**||Xinghang Li Team|[2602.10983](http://arxiv.org/abs/2602.10983)|null|
|**2026-02-11**|**Human Preference Modeling Using Visual Motion Prediction Improves Robot Skill Learning from Egocentric Human Video**||Christopher G. Atkeson Team|[2602.11393](http://arxiv.org/abs/2602.11393)|null|
|**2026-02-11**|**MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation**||Ranjay Krishna Team|[2602.11337](http://arxiv.org/abs/2602.11337)|null|
|**2026-02-11**|**YOR: Your Own Mobile Manipulator for Generalizable Robotics**||Zichen Jeff Cui Team|[2602.11150](http://arxiv.org/abs/2602.11150)|null|
|**2026-02-11**|**ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning**||Mu Xu Team|[2602.11236](http://arxiv.org/abs/2602.11236)|**[link](https://amap-cvlab.github.io/ABot-Manipulation/)**|
|**2026-02-11**|**OSIL: Learning Offline Safe Imitation Policies with Safety Inferred from Non-preferred Trajectories**||Balaraman Ravindran Team|[2602.11018](http://arxiv.org/abs/2602.11018)|null|
|**2026-02-11**|**Towards Learning a Generalizable 3D Scene Representation from 2D Observations**||Stefan Wermter Team|[2602.10943](http://arxiv.org/abs/2602.10943)|null|
|**2026-02-11**|**Semi-Supervised Cross-Domain Imitation Learning**||Ping-Chun Hsieh Team|[2602.10793](http://arxiv.org/abs/2602.10793)|null|
|**2026-02-11**|**Say, Dream, and Act: Learning Video World Models for Instruction-Driven Robot Manipulation**||Yanwei Fu Team|[2602.10717](http://arxiv.org/abs/2602.10717)|null|

<p align=right>(<a href=#updated-on-20260214>back to top</a>)</p>

## World Model

|Publish Date|Title|Chinese Summary|Authors|PDF|Code|
|---|---|---|---|---|---|
|**2026-02-12**|**The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics**|为了评估神经模型是否内化了物理定律而非仅仅利用统计捷径，尤其是在域外泛化（OOD）测试下，传统基于适应性的评估方法可能混淆模型的潜在表示。本文提出PhyIP非侵入式评估协议，通过线性表示假设，测试冻结表示中物理量是否可线性解码。结果表明，当自监督学习（SSL）实现低误差时，潜在结构变得可线性访问，PhyIP在OOD测试中成功恢复了内部能量和牛顿平方反比定律，而适应性评估则可能破坏这些结构，这强调了低容量探针在评估物理世界模型方面的准确性。|Barbara Hammer Team|[2602.12218](http://arxiv.org/abs/2602.12218)|null|
|**2026-02-12**|**LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion**|现有机器人基础模型主要依赖行为克隆，未能充分利用异构具身数据中蕴含的可迁移动力学知识，且统一世界模型（UWM）的现有实现难以扩展。为此，本研究提出了LDA-1B机器人基础模型，通过联合学习动力学、策略和视觉预测，实现通用具身数据摄入，并根据数据质量分配不同角色。研究构建了包含超3万小时轨迹的EI-30k数据集，并通过结构化DINO潜在空间中的预测和多模态扩散Transformer实现大规模动力学学习。实验证明，LDA-1B在多种复杂任务上显著优于现有方法，且能高效利用低质量数据进行微调，进一步提升性能。|He Wang Team|[2602.12215](http://arxiv.org/abs/2602.12215)|**[link](https://pku-epic.github.io/LDA)**|
|**2026-02-12**|**DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation**|当前联合音视频生成模型将人本任务视为独立目标，且在多人物场景下对多角色身份和音色进行精确解耦控制仍是挑战。本文提出了DreamID-Omni，一个统一的可控人本音视频生成框架。该框架设计了对称条件扩散Transformer来整合异构条件信号，并引入双层解耦策略（信号层面的同步RoPE和语义层面的结构化字幕）以解决身份-音色绑定失败和说话人混淆问题。此外，采用多任务渐进训练方案来协调不同目标并防止过拟合。大量实验表明，DreamID-Omni在视频、音频和音视频一致性方面均达到最先进性能，甚至超越商业模型。|Xiangwang Hou Team|[2602.12160](http://arxiv.org/abs/2602.12160)|**[link](https://guoxu1233.github.io/DreamID-Omni/)**|
|**2026-02-12**|**It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks**|时间序列基础模型（TSFMs）正在革新预测领域，但现有基准存在数据构成受限、数据完整性差、任务制定脱离实际以及分析视角僵化等问题。为解决这些不足，本文引入了TIME，一个新一代以任务为中心的基准，包含50个新数据集和98个预测任务，专为严格零样本TSFM评估设计。研究利用大型语言模型和人类专业知识，建立严谨的人机协作构建流程，确保数据完整性并使任务制定更符合现实操作需求。此外，提出了一种超越传统数据集级评估的模式级评估视角，通过结构化时间序列特征提供对模型能力的普适性洞察。该基准评估了12个代表性TSFMs并建立了多粒度排行榜。|Chenghao Liu Team|[2602.12147](http://arxiv.org/abs/2602.12147)|null|
|**2026-02-12**|**Commencing-Student Enrolment Forecasting Under Data Sparsity with Time Series Foundation Models**|许多大学面临财务压力，需要准确预测入学人数，但高等教育入学预测通常数据稀疏，传统方法在短样本和结构性变化下表现不佳。本文研究了时间序列基础模型（TSFMs）在零样本数据稀疏机构预测中的应用。研究评估了多种TSFM家族，并引入了一个紧凑、防数据泄露的协变量集，包括可迁移的机构运营条件指数（IOCI）和经过特征工程处理的Google Trends需求代理。通过严格的回溯测试，结果表明协变量条件下的TSFMs在无需机构特定训练的情况下，其表现与经典基准相当，展现了在数据稀疏场景下的潜力。|Surangika Ranathunga Team|[2602.12120](http://arxiv.org/abs/2602.12120)|null|
|**2026-02-12**|**The Pensieve Paradigm: Stateful Language Models Mastering Their Own Context**|现有大型语言模型（LLMs）缺乏主动管理自身状态（即记忆）的能力，受限于固定上下文窗口，被动地接受手动设计的上下文。本文提出StateLM，一种新型基础模型，通过内置的内部推理循环来管理自身状态。StateLM配备了上下文剪枝、文档索引和笔记记录等记忆工具，并被训练主动管理这些工具，从而动态构建其上下文。实验表明，StateLM在长文档问答任务上始终优于标准LLMs，在聊天记忆任务上实现了10%到20%的绝对准确率提升，并在深度研究任务BrowseComp-Plus上取得高达52%的准确率，远超标准LLMs。这使得LLMs从被动预测器转变为状态感知智能体。|Yan Wang Team|[2602.12108](http://arxiv.org/abs/2602.12108)|null|
|**2026-02-12**|**GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning**|现有视觉-语言-动作（VLA）模型直接预测多步动作时，受限于场景理解和未来预测能力。针对此问题，本文提出GigaBrain-0.5M*，一个通过世界模型强化学习训练的VLA模型，旨在利用视频世界模型强大的时空推理和未来预测能力。该模型基于在超过1万小时机器人操作数据上预训练的GigaBrain-0.5，并通过RAMP（Reinforcement leArning via world Model-conditioned Policy）进一步整合世界模型强化学习，以实现鲁棒的跨任务适应。实验结果表明，RAMP在多项挑战性任务上（如洗衣折叠、箱子打包、浓缩咖啡制作）实现了约30%的性能提升，且GigaBrain-0.5M*展示了可靠的长时序执行能力。|Zheng Zhu Team|[2602.12099](http://arxiv.org/abs/2602.12099)|**[link](https://gigabrain05m.github.io/)**|
|**2026-02-12**|**Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable Embodied Learning**|在真实世界中训练机器人策略成本高昂且难以扩展，而现有生成式仿真方法难以生成逻辑连贯的长时序任务，且因开环执行而难以应对动态物理不确定性。为解决这些挑战，本文提出了Affordance-Graphed Task Worlds (AGT-World) 框架。该框架能够基于真实世界观察自主构建交互式模拟环境和相应的机器人任务策略，并通过将任务空间形式化为结构化图来实现复杂目标的精确分层分解。此外，引入具有混合反馈的自进化机制，结合视觉-语言模型推理和几何验证来自主完善策略。实验证明，该方法在成功率和泛化性方面显著优于现有方法，实现了提案、执行和纠正的自改进循环。|Changshui Zhang Team|[2602.12065](http://arxiv.org/abs/2602.12065)|null|
|**2026-02-12**|**VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model**|为提升视觉-语言-动作（VLA）模型在在线交互中的性能和可靠性，本文研究了利用学习到的模拟器（即动作条件视频生成模型）生成额外执行数据。然而，现有世界模型缺乏足够的物理保真度，难以准确模拟接触丰富的物体操作中的细微物理细节。为此，本研究提出了一种简单的迭代改进算法：首先利用真实世界执行数据提升世界模型的保真度，然后世界模型再生成补充合成数据以改进VLA模型。在真实机器人实验中，该方法将一个最先进VLA模型在多个下游任务上的成功率提高了39.2%，其中通过合成执行数据训练带来了11.6%的提升。|Chelsea Finn Team|[2602.12063](http://arxiv.org/abs/2602.12063)|null|
|**2026-02-12**|**HoloBrain-0 Technical Report**|当前基础模型研究与真实世界机器人部署之间存在差距。为此，本文推出了HoloBrain-0，一个全面的视觉-语言-动作（VLA）框架，其核心是一个新型VLA架构，明确整合了机器人具身先验（如多视角相机参数和运动学描述URDF），以增强3D空间推理并支持多样化的具身形式。该设计通过可扩展的“预训练-后训练”范式进行验证，并在多项仿真基准和长时序真实世界操作任务上取得了最先进的结果。值得注意的是，其0.2B参数的高效变体能与更大的基线模型媲美，实现低延迟设备部署。为加速研究，HoloBrain生态系统已全面开源，包括预训练VLA基础模型、后训练检查点和全栈VLA基础设施RoboOrchard。|Zhizhong Su Team|[2602.12062](http://arxiv.org/abs/2602.12062)|null|
|**2026-02-12**|**FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards from Domain Client**|联邦基础模型（FedFMs）在利用客户端数据增强服务器端模型时面临高训练成本、通信开销和隐私风险。为此，本文提出了FedGRPO框架，将问题重新定义为强化学习风格的评估，通过轻量级置信图进行能力导向的专家选择，并利用“组相对”概念，将问题和解决方案打包为策略，通过聚合标量奖励信号来训练。实验证明，FedGRPO通过交换奖励而非数据或模型更新，有效降低了隐私风险和通信开销，并在多个任务上展现出优于传统FedFMs基线的下游精度和通信效率。|Yuxing Han Team|[2602.12014](http://arxiv.org/abs/2602.12014)|null|
|**2026-02-12**|**Accelerating Robotic Reinforcement Learning with Agent Guidance**|强化学习在机器人技能学习中面临样本效率低下和人工监督难以扩展的问题，传统的人在环（HIL）方法受限于1:1监督比例、操作员疲劳和人为误差。本文提出了Agent-guided Policy Search (AGPS) 框架，通过多模态智能体取代人类监督，将智能体视为语义世界模型，利用可执行工具提供精确的校正路径点和空间约束来指导探索。实验结果表明，AGPS在样本效率方面优于HIL方法，实现了监督流程自动化，为机器人学习提供了可扩展且无需人工干预的路径。|Yaodong Yang Team|[2602.11978](http://arxiv.org/abs/2602.11978)|null|
|**2026-02-12**|**Where Bits Matter in World Model Planning: A Paired Mixed-Bit Study for Efficient Spatial Reasoning**|高效空间推理要求世界模型在低精度预算下保持可靠性，本文研究低位规划行为受总位宽还是位分配的影响。通过在DINO-WM上进行“墙体规划”任务的配对目标混合位评估，发现存在一致的三阶段模式：8位和6位设置接近FP16，3位设置崩溃，4位设置则对位分配敏感。在4位过渡区域，保留编码器精度能改善规划性能，且不对称量化也显示出编码器侧的优势。这些发现表明应采用模块感知、预算感知的量化策略以实现高效空间推理。|Vaishak Menon Team|[2602.11882](http://arxiv.org/abs/2602.11882)|null|
|**2026-02-12**|**PuYun-LDM: A Latent Diffusion Model for High-Resolution Ensemble Weather Forecasts**|潜在扩散模型（LDMs）在高分辨率集成天气预报中存在扩散性受限问题，且现有方法因缺乏通用气象模型和变量间谱异质性导致正则化不均。针对此，本文提出了PuYun-LDM，其中包含3D掩码自编码器（3D-MAE）用于编码天气状态演变特征作为扩散模型的额外条件，并引入变量感知掩码频率建模（VA-MFM）策略以自适应选择阈值。结果显示，PuYun-LDM增强了潜在扩散性，在短期预报中超越了ENS，并在长期预报中与其可比，同时能在一个GPU上快速生成15天全球预报。|Bin Wang Team|[2602.11807](http://arxiv.org/abs/2602.11807)|null|
|**2026-02-12**|**HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model**|类人机器人在复杂任务中潜力巨大，但现有方法多关注刚性耦合物体，忽略了欠驱动物体的独立动力学和非完整约束带来的控制挑战。本文提出了HAIC框架，通过仅利用本体感受历史估计高阶物体状态的动力学预测器，并将预测投影到几何先验上形成动态占用图，从而推断盲点中的碰撞和接触。结合不对称微调，HAIC在类人机器人上实现了高成功率的敏捷任务（如滑板、推拉购物车）和多物体长周期任务，通过主动补偿惯性扰动，展示了对多样物体动力学的鲁棒交互能力。|Renjing Xu Team|[2602.11758](http://arxiv.org/abs/2602.11758)|**[link](https://haic-humanoid.github.io/)**|
|**2026-02-12**|**ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation**|具身导航领域长期存在任务特定架构碎片化的问题。本文提出了ABot-N0，一个统一的视觉-语言-动作（VLA）基础模型，旨在实现对五项核心导航任务的“大统一”。该模型采用分层“大脑-动作”架构，结合基于LLM的认知大脑进行语义推理和基于流匹配的动作专家进行精确轨迹生成。通过构建大规模ABot-N0数据引擎，ABot-N0在7个基准测试中取得了新的SOTA性能，显著优于专用模型，其代理导航系统还能在动态环境中执行鲁棒、长周期的任务。|Mu Xu Team|[2602.11598](http://arxiv.org/abs/2602.11598)|**[link](https://amap-cvlab.github.io/ABot-Navigation/ABot-N0/)**|
|**2026-02-12**|**Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signal**|脑基础模型（BFMs）通过可扩展和可迁移学习推动神经科学发展，但目前缺乏统一的方法理解和标准化评估框架。为填补空白，本文通过自监督学习（SSL）分类法组织BFMs，并从数据集角度总结了下游任务和公共数据集。在此基础上，本文提出了Brain4FMs，一个开放的评估平台，集成了15个代表性BFMs和18个公共数据集。该平台支持标准化比较和分析预训练数据、SSL策略和架构对泛化及下游性能的影响，从而指导开发更准确、更可迁移的BFMs。|Yang Yang Team|[2602.11558](http://arxiv.org/abs/2602.11558)|null|
|**2026-02-12**|**TS-Memory: Plug-and-Play Memory for Time Series Foundation Models**|时间序列基础模型（TSFMs）在零样本预测方面表现出色，但在领域分布偏移下的适应性仍是挑战，现有参数化适应易导致灾难性遗忘，非参数化检索则面临高推理延迟。本文提出了参数化记忆蒸馏方法TS-Memory，一个轻量级记忆适配器。它分两阶段训练：首先构建离线kNN教师模型合成置信度感知的分位数目标，然后通过置信度门控监督将检索诱导的分布校正蒸馏到适配器中。TS-Memory在推理时能以恒定时间开销融合预测，实验表明其在点预测和概率预测上均优于现有适应方法，且效率与冻结骨干网络相当。|Yuxuan Liang Team|[2602.11550](http://arxiv.org/abs/2602.11550)|null|
|**2026-02-12**|**Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use**|在预算受限的工具增强型智能体中，大型语言模型在调用外部工具解决多步任务时，面临巨大的状态-动作空间、高方差结果和高昂探索成本等挑战，导致直接规划难以实施。为解决此问题，本文提出了INTENT，一个推理时规划框架。该框架利用意图感知的层次化世界模型，预测未来工具使用和风险校准成本，并在线指导决策。实验证明，INTENT在成本增强型StableToolBench上严格遵守预算限制，同时显著提高了任务成功率，并在工具价格和预算变化等动态市场条件下保持了鲁棒性。|Qi Qi Team|[2602.11541](http://arxiv.org/abs/2602.11541)|null|
|**2026-02-12**|**Vascular anatomy-aware self-supervised pre-training for X-ray angiogram analysis**|X射线血管造影的深度学习分析受限于带注释数据的稀缺性，且大规模自监督学习在该领域应用不足。针对此，本文提出了血管解剖感知掩码图像建模（VasoMIM）框架，其包含解剖引导掩码策略和解剖一致性损失，旨在明确整合领域特定的解剖知识。VasoMIM通过策略性掩盖含血管的图像块并保持血管结构一致性，从而学习鲁棒的血管语义。结合VasoMIM，本文还构建了迄今最大的X射线血管造影预训练数据集XA-170K。实验表明，VasoMIM在多个下游任务上展现出卓越的可迁移性和最先进的性能，有望成为X射线血管造影分析的基础模型。|Zeng-Guang Hou Team|[2602.11536](http://arxiv.org/abs/2602.11536)|null|

<p align=right>(<a href=#updated-on-20260214>back to top</a>)</p>

## VLM

|Publish Date|Title|Chinese Summary|Authors|PDF|Code|
|---|---|---|---|---|---|
|**2026-02-12**|**Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment**||Marco Pavone Team|[2602.12281](http://arxiv.org/abs/2602.12281)|null|
|**2026-02-12**|**ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images**||Manuela Veloso Team|[2602.12203](http://arxiv.org/abs/2602.12203)|null|
|**2026-02-12**|**3DGSNav: Enhancing Vision-Language Model Reasoning for Object Navigation via Active 3D Gaussian Splatting**||Xinyi Yu Team|[2602.12159](http://arxiv.org/abs/2602.12159)|null|
|**2026-02-12**|**Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable Embodied Learning**||Changshui Zhang Team|[2602.12065](http://arxiv.org/abs/2602.12065)|null|
|**2026-02-12**|**Can Local Vision-Language Models improve Activity Recognition over Vision Transformers? -- Case Study on Newborn Resuscitation**||Øyvind Meinich-Bache Team|[2602.12002](http://arxiv.org/abs/2602.12002)|null|
|**2026-02-12**|**Benchmarking Vision-Language Models for French PDF-to-Markdown Conversion**||Nicolas Mery Team|[2602.11960](http://arxiv.org/abs/2602.11960)|null|
|**2026-02-12**|**Are Two LLMs Better Than One? A Student-Teacher Dual-Head LLMs Architecture for Pharmaceutical Content Optimization**||Anubhav Girdhar Team|[2602.11957](http://arxiv.org/abs/2602.11957)|null|
|**2026-02-12**|**LAMP: Implicit Language Map for Robot Navigation**||Sunwook Choi Team|[2602.11862](http://arxiv.org/abs/2602.11862)|**[link](https://lab-of-ai-and-robotics.github.io/LAMP/)**|
|**2026-02-12**|**JEPA-VLA: Video Predictive Embedding is Needed for VLA Models**||Mingsheng Long Team|[2602.11832](http://arxiv.org/abs/2602.11832)|null|
|**2026-02-12**|**Revis: Sparse Latent Steering to Mitigate Object Hallucination in Large Vision-Language Models**||Zhou Yang Team|[2602.11824](http://arxiv.org/abs/2602.11824)|null|
|**2026-02-12**|**Adaptive Debiasing Tsallis Entropy for Test-Time Adaptation**||Jianfeng Lu Team|[2602.11743](http://arxiv.org/abs/2602.11743)|null|
|**2026-02-12**|**Adapting Vision-Language Models for E-commerce Understanding at Scale**||Shahram Khadivi Team|[2602.11733](http://arxiv.org/abs/2602.11733)|null|
|**2026-02-12**|**STVG-R1: Incentivizing Instance-Level Reasoning and Grounding in Videos via Reinforcement Learning**||Qing Li Team|[2602.11730](http://arxiv.org/abs/2602.11730)|null|
|**2026-02-12**|**ScalSelect: Scalable Training-Free Multimodal Data Selection for Efficient Visual Instruction Tuning**||Kai Chen Team|[2602.11636](http://arxiv.org/abs/2602.11636)|**[link](https://github.com/ChangtiWu/ScalSelect}{ScalSelect})**|
|**2026-02-12**|**SkillRater: Untangling Capabilities in Multimodal Data**||Akshat Shrivastava Team|[2602.11615](http://arxiv.org/abs/2602.11615)|null|
|**2026-02-12**|**Chatting with Images for Introspective Visual Thinking**||Tieniu Tan Team|[2602.11073](http://arxiv.org/abs/2602.11073)|null|
|**2026-02-11**|**Hierarchical Concept Embedding & Pursuit for Interpretable Image Classification**||René Vidal Team|[2602.11448](http://arxiv.org/abs/2602.11448)|null|
|**2026-02-11**|**Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling**||Wenhan Luo Team|[2602.11146](http://arxiv.org/abs/2602.11146)|**[link](https://github.com/HKUST-C4G/diffusion-rm)**|
|**2026-02-11**|**Active Zero: Self-Evolving Vision-Language Models through Active Environment Exploration**||Tat-Seng Chua Team|[2602.11241](http://arxiv.org/abs/2602.11241)|null|
|**2026-02-11**|**Safe mobility support system using crowd mapping and avoidance route planning using VLM**||Koichi Ozaki Team|[2602.10910](http://arxiv.org/abs/2602.10910)|null|

<p align=right>(<a href=#updated-on-20260214>back to top</a>)</p>

## VLA

|Publish Date|Title|Chinese Summary|Authors|PDF|Code|
|---|---|---|---|---|---|
|**2026-02-12**|**Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment**||Marco Pavone Team|[2602.12281](http://arxiv.org/abs/2602.12281)|null|
|**2026-02-12**|**GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning**||Zheng Zhu Team|[2602.12099](http://arxiv.org/abs/2602.12099)|**[link](https://gigabrain05m.github.io/)**|
|**2026-02-12**|**VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model**||Chelsea Finn Team|[2602.12063](http://arxiv.org/abs/2602.12063)|null|
|**2026-02-12**|**HoloBrain-0 Technical Report**||Zhizhong Su Team|[2602.12062](http://arxiv.org/abs/2602.12062)|null|
|**2026-02-12**|**When would Vision-Proprioception Policies Fail in Robotic Manipulation?**||Di Hu Team|[2602.12032](http://arxiv.org/abs/2602.12032)|null|
|**2026-02-12**|**JEPA-VLA: Video Predictive Embedding is Needed for VLA Models**||Mingsheng Long Team|[2602.11832](http://arxiv.org/abs/2602.11832)|null|
|**2026-02-12**|**ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation**||Mu Xu Team|[2602.11598](http://arxiv.org/abs/2602.11598)|**[link](https://amap-cvlab.github.io/ABot-Navigation/ABot-N0/)**|
|**2026-02-12**|**Scaling World Model for Hierarchical Manipulation Policies**||Xinghang Li Team|[2602.10983](http://arxiv.org/abs/2602.10983)|null|
|**2026-02-11**|**H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model**||Yingxue Zhang Team|[2602.11291](http://arxiv.org/abs/2602.11291)|null|
|**2026-02-11**|**RISE: Self-Improving Robot Policy with Compositional World Model**||Hongyang Li Team|[2602.11075](http://arxiv.org/abs/2602.11075)|**[link](https://opendrivelab.com/kai0-rl/)**|
|**2026-02-11**|**RADAR: Benchmarking Vision-Language-Action Generalization via Real-World Dynamics, Spatial-Physical Intelligence, and Autonomous Evaluation**||Guangrun Wang Team|[2602.10980](http://arxiv.org/abs/2602.10980)|null|
|**2026-02-11**|**From Representational Complementarity to Dual Systems: Synergizing VLM and Vision-Only Backbones for End-to-End Driving**||Yan Wang Team|[2602.10719](http://arxiv.org/abs/2602.10719)|null|
|**2026-02-11**|**Say, Dream, and Act: Learning Video World Models for Instruction-Driven Robot Manipulation**||Yanwei Fu Team|[2602.10717](http://arxiv.org/abs/2602.10717)|null|
|**2026-02-11**|**AugVLA-3D: Depth-Driven Feature Augmentation for Vision-Language-Action Models**||F. Richard Yu Team|[2602.10698](http://arxiv.org/abs/2602.10698)|null|
|**2026-02-11**|**Improving Medical Visual Reinforcement Fine-Tuning via Perception and Reasoning Augmentation**||Qicheng Lao Team|[2602.10619](http://arxiv.org/abs/2602.10619)|null|
|**2026-02-11**|**LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer**||Anirudha Majumdar Team|[2602.10556](http://arxiv.org/abs/2602.10556)|**[link](https://lap-vla.github.io)**|
|**2026-02-11**|**Found-RL: foundation model-enhanced reinforcement learning for autonomous driving**||Sikai Chen Team|[2602.10458](http://arxiv.org/abs/2602.10458)|null|
|**2026-02-10**|**Hardware Co-Design Scaling Laws via Roofline Modelling for On-Device LLMs**||Cheng Deng Team|[2602.10377](http://arxiv.org/abs/2602.10377)|null|
|**2026-02-10**|**ST4VLA: Spatially Guided Training for Vision-Language-Action Models**||Jiangmiao Pang Team|[2602.10109](http://arxiv.org/abs/2602.10109)|null|
|**2026-02-10**|**EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration**||Li Chen Team|[2602.10106](http://arxiv.org/abs/2602.10106)|**[link](https://opendrivelab.com/EgoHumanoid)**|

<p align=right>(<a href=#updated-on-20260214>back to top</a>)</p>

## Humanoid

|Publish Date|Title|Chinese Summary|Authors|PDF|Code|
|---|---|---|---|---|---|
|**2026-02-12**|**General Humanoid Whole-Body Control via Pretraining and Fast Adaptation**||Zongqing Lu Team|[2602.11929](http://arxiv.org/abs/2602.11929)|null|
|**2026-02-12**|**HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model**||Renjing Xu Team|[2602.11758](http://arxiv.org/abs/2602.11758)|**[link](https://haic-humanoid.github.io/)**|
|**2026-02-12**|**Future Mining: Learning for Safety and Security**||Sanjay Madria Team|[2602.11472](http://arxiv.org/abs/2602.11472)|null|
|**2026-02-12**|**Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations**||Yang Gao Team|[2602.06643](http://arxiv.org/abs/2602.06643)|**[link](https://humanoid-manipulation-interface.github.io)**|
|**2026-02-11**|**ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control**||Chuang Gan Team|[2602.11321](http://arxiv.org/abs/2602.11321)|**[link](https://owenowl.github.io/extremcontrol)**|
|**2026-02-11**|**APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots**||Ding Zhao Team|[2602.11143](http://arxiv.org/abs/2602.11143)|**[link](https://apex-humanoid.github.io/)**|
|**2026-02-11**|**Towards Learning a Generalizable 3D Scene Representation from 2D Observations**||Stefan Wermter Team|[2602.10943](http://arxiv.org/abs/2602.10943)|null|
|**2026-02-11**|**MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation**||Alois Knoll Team|[2602.08594](http://arxiv.org/abs/2602.08594)|null|
|**2026-02-10**|**EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration**||Li Chen Team|[2602.10106](http://arxiv.org/abs/2602.10106)|**[link](https://opendrivelab.com/EgoHumanoid)**|
|**2026-02-10**|**Humanoid Factors: Design Principles for AI Humanoids in Human Worlds**||Lixiao Huang Team|[2602.10069](http://arxiv.org/abs/2602.10069)|null|
|**2026-02-10**|**TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior**||Rongyun Cao Team|[2602.09628](http://arxiv.org/abs/2602.09628)|null|
|**2026-02-09**|**Characteristics, Management, and Utilization of Muscles in Musculoskeletal Humanoids: Empirical Study on Kengoro and Musashi**||Masayuki Inaba Team|[2602.08518](http://arxiv.org/abs/2602.08518)|null|
|**2026-02-09**|**Learning Human-Like Badminton Skills for Humanoid Robots**||Peng Lu Team|[2602.08370](http://arxiv.org/abs/2602.08370)|null|
|**2026-02-07**|**VividFace: Real-Time and Realistic Facial Expression Shadowing for Humanoid Robots**||Yang Zhang Team|[2602.07506](http://arxiv.org/abs/2602.07506)|null|
|**2026-02-07**|**TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control**||Xuelong Li Team|[2602.07439](http://arxiv.org/abs/2602.07439)|**[link](https://text-op.github.io/)**|
|**2026-02-07**|**Bridging Speech, Emotion, and Motion: a VLM-based Multimodal Edge-deployable Framework for Humanoid Robots**||Miao Li Team|[2602.07434](http://arxiv.org/abs/2602.07434)|null|
|**2026-02-06**|**Cerebellar-Inspired Residual Control for Fault Recovery: From Inference-Time Adaptation to Structural Consolidation**||Amit Ranjan Trivedi Team|[2602.07227](http://arxiv.org/abs/2602.07227)|null|
|**2026-02-06**|**DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization**||Majid Khadiv Team|[2602.06827](http://arxiv.org/abs/2602.06827)|null|
|**2026-02-06**|**ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking**||Yao Su Team|[2602.06445](http://arxiv.org/abs/2602.06445)|null|
|**2026-02-06**|**Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels**||Zongwu Xie Team|[2602.06382](http://arxiv.org/abs/2602.06382)|null|

<p align=right>(<a href=#updated-on-20260214>back to top</a>)</p>
