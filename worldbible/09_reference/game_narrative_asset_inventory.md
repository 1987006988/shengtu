# 《升途：封绝之地》游戏叙事资产盘点

## 1. 文件定位

本文档是 `B00：现有资产盘点与执行断点建立` 的主输出之一，用于给后续 recurring batch run 提供一份文件级资产底表。

本文档不生产主线任务正文、同伴对白、支线文本、Codex、Journal、物品文本或系统反馈正文。它只回答四个问题：

1. 当前仓库中哪些文件可以作为大型 CRPG 叙事文本工程的稳定输入。
2. 哪些文件只是小说化参考、总蓝图、review 或旧日志，不得被误判为可直接交付的游戏文本资产。
3. 哪些旧阶段日志声称存在的游戏文本资产在当前文件系统中缺失。
4. B01 及后续批次在执行前需要注意哪些输入缺口、范围边界与状态口径。

本盘点属于项目执行层与协作记忆层，不新增世界观正典，不新增正式势力、地名、人物名、任务名或系统名。

## 2. 本轮 batch 判定

本轮读取 `game_narrative_batch_schedule.md`、`game_narrative_execution_state.md` 与 `game_narrative_batch_rules.md` 后，确认当前没有 `IN_PROGRESS` batch，最早可执行的 `PENDING` batch 为 B00。

B00 的目标是“现有资产盘点与执行断点建立”。本轮没有进入 B01，没有重建 `25_volume1_core_conflict.md` 或 `26_volume1_revelation_ladder.md`，也没有顺手修补后续批次输入文件。原因是自动运行规则明确要求每次只执行一个 batch，未通过当前 batch review 前不得开始下一批。

本轮未触发 A/B 拆分。B00 的输出范围为两份主文件与一份 review 文件，未预计超过 `60,000` 汉字或 `180` 分钟。

## 3. 已读取输入文件

### 3.1 B00 指定输入

| 文件 | 当前状态 | 读取结论 | 后续定位 |
| --- | --- | --- | --- |
| `worldbible/09_reference/game_narrative_master_plan.md` | 存在 | 已读。它是大型 CRPG 叙事文本总工程的项目级总蓝图母本。 | 后续批次的规模、资产层、拆包规则、验收标准来自此文件。 |
| `worldbible/09_reference/game_narrative_master_plan_review.md` | 存在 | 已读。它确认总蓝图可作为拆批母本，并指出必须先做资产盘点。 | B00 的直接依据之一。 |
| `worldbible/09_reference/decision_log.md` | 存在 | 已读。它包含旧故事阶段、旧 GAME 阶段和最新批次化重构记录。 | 可作为历史口径参考，但不能替代文件系统事实。 |
| `worldbible/00_project_overview/04_current_state.md` | 存在 | 已读。当前状态仍停留在“准备进入 recurring execution”。 | 本轮完成后需同步为 B00 已完成。 |
| `worldbible/09_reference/session_handoff.md` | 存在 | 已读。交接页指向“执行 B00”。 | 本轮完成后需改写为 B01 前置状态。 |
| `worldbible/09_reference/game_narrative_final_acceptance.md` | 不存在 | 已按“如存在”规则检查。当前文件系统中不存在。 | 不得把旧最终验收口径当成现存交付物。 |
| `worldbible/09_reference/story_master_execution_plan.md` | 存在 | 已读。它是小说化故事工程的旧总控计划。 | 可作为故事稿来源链参考，不是游戏文本批次计划。 |

### 3.2 自动运行规则要求的启动输入

| 文件 | 当前状态 | 读取结论 |
| --- | --- | --- |
| `README.md` | 存在 | 已读。确认本仓库是宇宙级世界观仓库，第一款游戏只聚焦白鹿原。 |
| `AGENTS.md` | 存在 | 已读。确认不得越权新增正典、不得把白鹿原写成整个古裂残天、重大变更需记入决策日志。 |
| `worldbible/09_reference/game_narrative_batch_schedule.md` | 存在 | 已读。确认 B00 输出、review 文件、目标和下一批为 B01。 |
| `worldbible/09_reference/game_narrative_execution_state.md` | 存在 | 已读。确认 B00–B15 均为 `PENDING`，当前应执行 B00。 |
| `worldbible/09_reference/game_narrative_batch_rules.md` | 存在 | 已读。确认每次只能执行一个 batch，且每批结束必须 review 与同步状态。 |
| `worldbible/09_reference/game_batch00_review.md` | 不存在 | 已检查。当前没有上一次 B00 review。 |

## 4. 输入文件体量快照

以下统计来自本轮文件系统检查，仅用于识别现存资产体量，不作为文学质量或正典等级判断。

| 文件 | 是否存在 | 字符数 | 行数 | 盘点意义 |
| --- | --- | ---: | ---: | --- |
| `game_narrative_master_plan.md` | 是 | 6,690 | 293 | 总蓝图母本存在，但它不是正文资产。 |
| `game_narrative_master_plan_review.md` | 是 | 3,046 | 135 | 总蓝图 review 存在，可作为批次化依据。 |
| `decision_log.md` | 是 | 31,206 | 635 | 历史记录充足，但部分旧 GAME 记录与当前文件系统不一致。 |
| `04_current_state.md` | 是 | 2,240 | 58 | 当前状态页需要在 B00 后同步。 |
| `session_handoff.md` | 是 | 2,077 | 43 | 交接摘要需要在 B00 后同步。 |
| `story_master_execution_plan.md` | 是 | 5,016 | 167 | 旧故事工程总控存在，可解释 30/31 的来源。 |
| `game_narrative_final_acceptance.md` | 否 | 0 | 0 | 当前不存在，不能作为可用验收依据。 |

## 5. 现存上游故事资产

当前文件系统中仍然存在小说化故事资产与旧故事验收文件。它们可以为后续 B01–B02 提供上游叙事参考，但不能替代游戏级 Act 架构、任务节点、状态机、场景卡或可用任务文本。

| 文件 | 是否存在 | 字符数 | 行数 | 可复用价值 | 限制 |
| --- | --- | ---: | ---: | --- | --- |
| `worldbible/08_story/30_book1_story_draft.md` | 是 | 4,373 | 184 | 可作为第一部故事初稿参考，帮助识别主线情绪、行动链和白鹿原终局方向。 | 它是小说化正文，不是任务树、任务文本、可交互状态反馈或分支脚本。 |
| `worldbible/08_story/31_book1_story_revised.md` | 是 | 4,118 | 202 | 可作为修订后的小说化参考底稿，帮助判断故事闭环与代价表达。 | 不能被当作大型 CRPG 叙事文本工程完成证明。 |
| `worldbible/09_reference/story_final_acceptance_report.md` | 是 | 1,356 | 119 | 可证明旧“完整故事稿”阶段曾完成过小说化验收。 | 只验收故事稿，不验收主线任务、同伴文本、支线、Codex、Journal、Item 或 System。 |

### 5.1 对 30/31 的使用规则

后续批次可以读取 30/31 的叙事骨干，但必须执行降级使用：

- 可以复用：白鹿原不是整个古裂残天、主角团卷入白鹿原的宏观逻辑、白鹿之灵作为接引法宝灵性接口、受限未来路径、代价承担、接引异常与残秩序压力。
- 需要重写：章节推进方式、场景密度、角色出场功能、冲突节点、任务前置、失败反馈、玩家选择差异、Journal 更新、区域状态、势力状态。
- 不得复用为终稿：小说段落不能直接粘成任务文本；若后续需要改写为任务文本，必须补足 `ID / 前置 / 目标 / 冲突 / 选择 / 输出状态 / 关联对象 / Journal 更新`。

## 6. 旧 GAME 阶段记录与当前文件系统差异

`decision_log.md` 中保留了 `GAME-2026-04-17-01` 至 `GAME-2026-04-18-01` 等旧 GAME 阶段记录，记录中曾提到若干主线、状态机、同伴、支线、Codex、Journal、Item 与 System 文件。但本轮文件系统检查显示，当前仓库里多数对应文件并不存在。

此差异是 B00 最重要的断点信息。后续 batch 不得因为 `decision_log.md` 曾记录“已新增”就假设这些资产当前可读取、可复用或可审查。批次执行必须以当前文件系统为准。

### 6.1 游戏级主线架构文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/08_story/25_volume1_core_conflict.md` | 不存在 | B01 输出目标之一。后续不能把旧日志视作输入正文。 |
| `worldbible/08_story/26_volume1_revelation_ladder.md` | 不存在 | B01 输出目标之一。后续必须重建揭示阶梯。 |
| `worldbible/08_story/27_volume1_plot_spine.md` | 不存在 | B02 输出目标之一，但 B01/B02 当前输入表也引用它，存在输入缺失风险。 |
| `worldbible/08_story/28_volume1_chapter_outline.md` | 不存在 | B02 参考输入之一缺失。需要在后续执行策略中处理。 |
| `worldbible/08_story/29_volume1_scene_cards.md` | 不存在 | B02 输出目标之一。当前没有 120–240 张游戏级场景卡。 |

### 6.2 势力与区域状态机文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/04_main_world/14_bailuyuan_faction_state_machine.md` | 不存在 | B03 输出目标。当前没有可供任务系统调用的势力状态机。 |
| `worldbible/04_main_world/15_bailuyuan_region_state_machine.md` | 不存在 | B04 输出目标。当前没有可供任务、支线、系统反馈调用的区域状态机。 |

### 6.3 主线任务工程文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/08_story/32_main_quest_architecture.md` | 不存在 | B05 输出目标。当前没有稳定主线任务树与 ID 体系。 |
| `worldbible/08_story/33_main_quest_text_pack_part1.md` | 不存在 | 旧锚点不存在。新批次表将改用 `33a/33b` 拆包输出。 |
| `worldbible/08_story/34_main_quest_text_pack_part2.md` | 不存在 | 旧锚点不存在。新批次表将改用 `34a/34b` 拆包输出。 |
| `worldbible/08_story/35_main_quest_text_pack_part3.md` | 不存在 | 旧锚点不存在。新批次表将改用 `35a/35b` 拆包输出。 |
| `worldbible/08_story/33a_main_quest_act1_mq01_mq06_text.md` | 不存在 | 新 B06 输出目标。 |
| `worldbible/08_story/33b_main_quest_act1_mq07_mq12_text.md` | 不存在 | 新 B06 输出目标。 |
| `worldbible/08_story/34a_main_quest_act2_mq13_mq18_text.md` | 不存在 | 新 B07 输出目标。 |
| `worldbible/08_story/34b_main_quest_act2_mq19_mq24_text.md` | 不存在 | 新 B07 输出目标。 |
| `worldbible/08_story/35a_main_quest_act3_mq25_mq34_text.md` | 不存在 | 新 B08 输出目标。 |
| `worldbible/08_story/35b_main_quest_act3_mq35_epilogue_text.md` | 不存在 | 新 B08 输出目标。 |

### 6.4 同伴文本工程文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/07_characters/17_companion_arc_matrix.md` | 不存在 | B09 输出目标。当前没有新批次可用的同伴弧线矩阵。 |
| `worldbible/07_characters/18_companion_dialogue_pack_part1.md` | 不存在 | 旧锚点不存在。 |
| `worldbible/07_characters/19_companion_dialogue_pack_part2.md` | 不存在 | 旧锚点不存在。 |
| `worldbible/07_characters/20_companion_banter_camp_pack.md` | 不存在 | 旧锚点不存在。 |
| `worldbible/07_characters/18a_companion_dialogue_entry_act1_pack.md` | 不存在 | 新 B10 输出目标。 |
| `worldbible/07_characters/18b_companion_dialogue_act2_reaction_pack.md` | 不存在 | 新 B10 输出目标。 |
| `worldbible/07_characters/19a_companion_dialogue_act3_loyalty_pack.md` | 不存在 | 新 B11 输出目标。 |
| `worldbible/07_characters/20a_companion_banter_route_reaction_pack.md` | 不存在 | 新 B11 输出目标。 |

### 6.5 支线、区域、Codex、Journal、Item 与 System 文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/08_story/36_sidequest_matrix.md` | 不存在 | B12 输出目标。当前没有新批次可用支线矩阵。 |
| `worldbible/08_story/37_sidequest_text_pack_part1.md` | 不存在 | 旧锚点不存在。 |
| `worldbible/08_story/38_sidequest_text_pack_part2.md` | 不存在 | 旧锚点不存在。 |
| `worldbible/08_story/39_settlement_and_region_texts.md` | 不存在 | B12 输出目标之一。 |
| `worldbible/08_story/40_codex_entries.md` | 不存在 | 旧 Codex 锚点不存在。新批次表将改用 `40a`。 |
| `worldbible/08_story/41_journal_and_update_texts.md` | 不存在 | 旧 Journal 锚点不存在。新批次表将改用 `41a`。 |
| `worldbible/08_story/42_items_relics_and_documents.md` | 不存在 | 旧 Item 锚点不存在。新批次表将改用 `42a`。 |
| `worldbible/08_story/43_system_feedback_texts.md` | 不存在 | 旧 System 锚点不存在。新批次表将改用 `43a`。 |
| `worldbible/08_story/37a_sidequest_text_pack_core_regions.md` | 不存在 | 新 B13 输出目标。 |
| `worldbible/08_story/38a_sidequest_text_pack_grayline_and_outskirts.md` | 不存在 | 新 B13 输出目标。 |
| `worldbible/08_story/40a_codex_entries_bailuyuan_pack.md` | 不存在 | 新 B14 输出目标。 |
| `worldbible/08_story/41a_journal_and_update_texts_pack.md` | 不存在 | 新 B14 输出目标。 |
| `worldbible/08_story/42a_items_relics_and_documents_pack.md` | 不存在 | 新 B15 输出目标。 |
| `worldbible/08_story/43a_system_feedback_texts_pack.md` | 不存在 | 新 B15 输出目标。 |

### 6.6 旧 GAME review 文件

| 文件 | 当前状态 | 处理结论 |
| --- | --- | --- |
| `worldbible/09_reference/game_phase1_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B01 review 替代。 |
| `worldbible/09_reference/game_phase2_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B03/B04 review 替代。 |
| `worldbible/09_reference/game_phase3_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B05–B08 review 替代。 |
| `worldbible/09_reference/game_phase4_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B09–B11 review 替代。 |
| `worldbible/09_reference/game_phase5_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B12/B13 review 替代。 |
| `worldbible/09_reference/game_phase6_review.md` | 不存在 | 旧阶段 review 不存在，不能作为新 B14/B15 review 替代。 |
| `worldbible/09_reference/game_batch00_review.md` | 不存在 | 本轮应新建。 |

## 7. 可复用锚点

### 7.1 总蓝图锚点

`game_narrative_master_plan.md` 是后续所有批次最重要的计划锚点。它明确了几个必须保留的工程结论：

- 当前目标是大型 CRPG 叙事文本总工程，不是再写一卷小说。
- 总量最低目标为 `1,500,000` 汉字，目标区间为 `3,000,000–6,000,000` 汉字。
- 文本资产必须分布于主线、支线、同伴、区域、Codex、Journal、物品、系统反馈、状态差异、失败反馈等多层。
- `30_book1_story_draft.md` 与 `31_book1_story_revised.md` 只作为小说化参考底稿。
- 后续新增拆包子文件允许承载正文资产，但主文件要负责总览、索引、规则、映射和跨包引用。
- 每个任务单元必须具备 `ID / 前置 / 目标 / 关键冲突 / 关键选择 / 输出状态 / 关联区域 / 关联势力 / 关联同伴 / Journal 更新`。
- 每张场景卡必须具备 `存在理由 / 推动冲突 / 增权对象 / 前置状态 / 变体结果 / 输出状态`。
- 状态机文件要使用“状态触发条件 + 可见反馈 + 对其他系统影响”的写法。

这些结论可以直接服务 B01–B15，但它们仍是计划与规范，不是正文资产。

### 7.2 范围锚点

来自 `README.md`、`AGENTS.md`、`04_current_state.md`、`session_handoff.md` 与 `decision_log.md` 的范围锚点如下：

- 项目总名：`升途`。
- 英文正式名：`Ascendant Path`。
- 第一款游戏 / 第一部标题：`升途：封绝之地`。
- 第一款游戏主舞台：`白鹿原`。
- `白鹿原` 是 `古裂残天` 内部隔绝地域，不等于整个 `古裂残天`。
- 当前重点展开对象是 `古裂残天` 内部的白鹿原阶段，但仓库不是古裂残天单世界仓库。
- 游戏聚焦层不得反向改写宇宙通则、九主世界总层或古裂残天长期正典。

这些锚点对 B01–B15 全部有效。

### 7.3 白鹿之灵边界锚点

当前已锁定的白鹿之灵边界可以继续作为后续批次检查项：

- 白鹿之灵是接引法宝之灵的白鹿显化。
- 它是主线核心装置的灵性接口，不是普通灵兽、独立神祇、世界意志或古裂残天整体意志。
- 它可以作为接口、残忆、触发器、示警、边界反馈与复生机制的代价提示。
- 它不得成为万能解释器、万能支援、万能真相机、无代价复生源。
- 它不能替主角团解决结构性冲突，不能取代地方承接层、守护残余、反抗残余等现实力量的作用。

后续凡是涉及任务推进、失败反馈、复生、残忆、揭示、Codex 或系统提示，都应回查此边界。

### 7.4 旧故事工程锚点

`story_master_execution_plan.md`、`30_book1_story_draft.md`、`31_book1_story_revised.md` 与 `story_final_acceptance_report.md` 的可复用价值主要在于：

- 它们证明白鹿原故事曾完成从承载面到小说化修订稿的闭环。
- 它们能提供故事主问题、开场卷入、白鹿之灵边界、代价承担、受限未来路径等叙事参考。
- 它们能帮助后续 B01 判断哪些故事问题需要转译为 Act 结构，而不是从零发明主线。

但它们不能替代游戏级资产，因为它们缺少：

- 任务 ID。
- 可检查前置状态。
- 玩家选择输出状态。
- 失败路径。
- Journal 更新位。
- 区域状态机映射。
- 势力状态机映射。
- 同伴路线状态接口。
- 可复用系统反馈文本。

## 8. 需要重写的资产层

### 8.1 游戏级主线架构层

B01 与 B02 必须重写或重建游戏级主线架构层。当前没有可直接读取的 `25–29` 文件，因此后续不能宣称“已有 Act 结构、48 个主线任务节点、128 张场景卡”。这些内容只存在于旧决策日志的阶段记录中，不存在于当前文件系统。

后续应按新批次表重建：

- B01：`25_volume1_core_conflict.md` 与 `26_volume1_revelation_ladder.md`。
- B02：`27_volume1_plot_spine.md` 与 `29_volume1_scene_cards.md`。

需要注意：B01 输入表目前也列出了 `25–29`，但这些文件缺失。若下次自动运行严格按输入缺失规则处理，B01 会出现阻塞风险。此问题不在 B00 输出权限内修 schedule，但必须在 checkpoint 和 review 中显式提醒。

### 8.2 状态机层

当前没有 `14_bailuyuan_faction_state_machine.md` 与 `15_bailuyuan_region_state_machine.md`。这意味着后续主线、支线、同伴、区域与系统反馈不能假设已有稳定状态机。

B03/B04 必须承担状态机重建，不得只写静态说明。状态机最低要求包括：

- 初始状态。
- 状态触发条件。
- 可见反馈。
- 对主线 / 支线 / 同伴 / 区域 / Journal / System 的影响。
- 玩家选择能改写的部分。
- 剧情强推但仍有可见代价的部分。

### 8.3 主线任务文本层

当前没有 `32` 与 `33–35` 系列主线任务文件。后续不得将小说正文拆段后直接冒充主线任务文本。

B05–B08 需要依序建立：

- 主线任务树。
- 主线任务 ID registry。
- Act 1 文本。
- Act 2 文本。
- Act 3 与 Epilogue 文本。

每个任务单元都必须能被任务设计和叙事设计引用，而不是只有剧情简介。

### 8.4 同伴文本层

当前没有 `17–20` 系列同伴文本文件。旧角色框架可以提供七席位来源与功能位置，但不能替代同伴路线状态、节点反应、入队文本、营地文本、banter 或终局反馈。

B09–B11 需要完成：

- 七席位弧线矩阵。
- 同伴路线状态图。
- 初识 / 入队 / Act 1 文本。
- Act 2 节点反应。
- Act 3 / 忠诚 / 路线反馈。
- banter 与终局反馈。

### 8.5 支线、区域与灰线文本层

当前没有 `36–39` 系列支线和区域文本文件。白鹿原已有舞台与功能地图，但尚未变成可执行的支线矩阵与区域文本底盘。

B12/B13 需要特别防止两类偷工：

- 只列支线目录，不写状态差异、失败结果和区域影响。
- 只写区域世界说明，不写可交互触发点、地方反馈和灰线接口。

### 8.6 Codex、Journal、Item 与 System 层

当前没有 `40–43` 系列文件。总蓝图要求这些层不是附录，而是游戏文本资产的一部分。

B14/B15 需要建立：

- Codex 词条。
- Journal 更新文本。
- 物品、遗物、文献文本。
- 系统反馈文本。
- 白鹿之灵异常与复生代价反馈。
- 任务、支线、区域和状态机之间的文本调用接口。

## 9. 缺口清单

### 9.1 文件缺口

当前最紧急的文件缺口不是“内容不够厚”，而是很多后续 batch 输入/输出文件尚不存在。尤其是 B01 所列输入 `25–29` 全部缺失，会影响下次自动运行的规则判断。

缺口分级如下：

| 等级 | 缺口 | 影响 |
| --- | --- | --- |
| 一级 | B01 输入表引用的 `25–29` 文件不存在。 | 下次执行 B01 时可能因输入缺失而按规则 BLOCKED。 |
| 一级 | `game_narrative_final_acceptance.md` 不存在。 | 不能沿用旧“最终验收完成”口径。 |
| 二级 | `14/15` 状态机不存在。 | B03/B04 前不能假设任务可调用状态机。 |
| 二级 | `32` 与主线任务文本拆包不存在。 | B05–B08 必须从架构层建立，不得直接扩写正文。 |
| 二级 | 同伴、支线、Codex、Journal、Item、System 文件不存在。 | B09–B15 都属于待建资产层。 |
| 三级 | 旧 GAME review 文件不存在。 | 旧阶段记录不能替代新 batch review。 |

### 9.2 口径缺口

旧决策日志中存在“游戏叙事阶段 1–7 已完成”“最终验收完成”等历史记录，但后续又有 `GAME-2026-04-17-09` 与 `GAME-2026-04-20-01/02` 重新核定：旧资产远低于百万级目标，不能宣称大型 CRPG 叙事文本总工程完成。

本轮 B00 的执行口径应固定为：

- 旧 GAME 阶段记录只可作为历史背景。
- 当前新批次化 recurring execution 从 B00 重新开始。
- B00 完成后只能进入 B01，不能跳到 B03 或后续文本包。
- 后续每批都必须产生自己的 review。

### 9.3 文本厚度缺口

当前现存可读的故事正文资产主要是 30/31，合计字符量约八千余级别。即使加上故事验收报告与总控计划，也远低于大型 CRPG 文本工程最低 `1,500,000` 汉字目标。

因此后续不得使用以下结论：

- “已有小说稿，所以主线文本完成。”
- “已有故事最终验收，所以游戏叙事工程完成。”
- “旧日志曾记录游戏阶段完成，所以新批次可以跳过。”
- “有总蓝图和 schedule，所以资产已经生产完毕。”

## 10. B01 输入风险提示

按当前 `game_narrative_batch_schedule.md`，B01 输入文件包括：

- `25_volume1_core_conflict.md`
- `26_volume1_revelation_ladder.md`
- `27_volume1_plot_spine.md`
- `28_volume1_chapter_outline.md`
- `29_volume1_scene_cards.md`
- `game_narrative_asset_inventory.md`
- `game_narrative_rebuild_checkpoint.md`
- `canon_rules.md`
- `glossary.md`

其中，本轮已生成 `game_narrative_asset_inventory.md` 与 `game_narrative_rebuild_checkpoint.md`，而 `canon_rules.md` 与 `glossary.md` 当前在仓库中存在。但 `25–29` 当前不存在。由于自动运行规则写明“若发现输入文件缺失，应将当前 batch 标记为 BLOCKED，不得猜测补写”，所以下次若直接执行 B01，存在规则冲突。

B00 不修改 B01 schedule，因为 schedule 修改不是本批主输出，也不是拆分需要。但 B00 必须把这个风险暴露给下次运行：

- 若严格执行输入缺失规则，下次 B01 应先标记 `BLOCKED`，说明 `25–29` 缺失。
- 若人工决定 B01 的目的就是重建缺失的 `25/26`，则应先修订 schedule 或明确允许 B01 将缺失的旧锚点视为“无旧稿可读”，再执行 B01。
- 不得由自动运行在没有规则授权的情况下默默跳过缺失输入并创作 B01 正文。

## 11. 后续批次使用本盘点的方式

### 11.1 B01 使用方式

B01 应优先读取本盘点第 7–10 节，确认：

- 旧 GAME 记录不能当作当前文件事实。
- 30/31 只是小说化参考，不是游戏主线架构。
- B01 的核心任务是重建 `25` 与 `26`，但当前 schedule 对缺失输入的处理需要先解决。
- B01 必须继续限定在白鹿原第一款游戏尺度。

### 11.2 B02 使用方式

B02 应检查 B01 review 是否通过，并确认 `25/26` 已存在后再建立 `27/29`。如果 B02 仍缺少 `28`，需要按规则处理，不得猜测旧章纲内容。

### 11.3 B03–B04 使用方式

B03/B04 不得假设已有状态机。它们需要从白鹿原势力景观、关键节点、功能地图、主线架构和 B02 review 中生成可调用状态机。

### 11.4 B05–B15 使用方式

B05–B15 应把“当前大多数游戏文本资产不存在”作为默认前提。每批只在前批 review 通过后推进，不得因为总蓝图完整就跳批生产。

## 12. 本批不处理事项

B00 不处理以下事项：

- 不补写 `25–29`。
- 不修订 `game_narrative_batch_schedule.md`。
- 不修订 `canon_rules.md` 或 `glossary.md`。
- 不创建主线任务、同伴、支线、Codex、Journal、Item 或 System 正文。
- 不恢复旧 GAME 阶段文件。
- 不判断旧 GAME 文件为何缺失。
- 不把 `30/31` 扩写成任务文本。

这些事项只能由后续 batch 或人工确认后单独处理。

## 13. B00 盘点结论

B00 的盘点结论为：当前仓库已具备大型 CRPG 叙事文本工程的总蓝图、批次表、执行规则、执行状态表、小说化参考底稿与旧故事验收链；但当前文件系统中缺少大多数游戏级正文资产、状态机资产和旧 GAME 阶段 review 文件。

因此，后续 recurring execution 必须从新批次状态表出发，逐批生产、逐批 review、逐批同步。不得把旧日志记录当作当前资产，不得把小说化故事稿当作大型 CRPG 文本工程完成证明，不得把白鹿原扩大为整个古裂残天。

本轮之后，B00 可以视为已完成资产盘点与断点建立；下一批理论上为 B01，但 B01 输入缺失风险必须在下次运行开始时优先处理。
