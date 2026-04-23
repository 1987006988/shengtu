# 《升途：封绝之地》批次化重构执行总表

## 1. 文件定位

本文档把 `game_narrative_master_plan.md` 重构为 Plus 5 小时额度友好的小批次工程。

本文档不是正文生成文件，不承载主线任务、同伴对白、支线、Journal、Item 或 System 大包正文。它用于 recurring automations 连续执行时选择下一个 batch，并限制每次运行的输入、输出、体量、时长与验收门槛。

## 2. 总原则

- 每次自动运行只执行一个 batch。
- 每个 batch 目标新增文本量为 `20,000–60,000` 汉字。
- 推荐执行时长为 `60–120` 分钟，保守上限为 `180` 分钟。
- 每个 batch 输入文件不超过 `10` 个。
- 每个 batch 主输出文件不超过 `2` 个。
- 每个 batch 必须有 `1` 个 review 文件。
- 若预计超出 `60,000` 汉字或 `180` 分钟，先拆成 A/B 子批次，再执行。
- 未通过 review 的 batch 不得进入下一批。
- 全部批次仍限定在 `白鹿原` 第一款游戏尺度，不上浮为整个 `古裂残天` 大全。

## 2.1 B00R 修正说明

2026-04-20 执行人工修正批次 `B00R：batch schedule repair`。

修正原因：B00 盘点确认 `25_volume1_core_conflict.md` 至 `29_volume1_scene_cards.md` 当前不存在；旧 schedule 曾把阶段 1 应重做并扩充的输出文件误写为 B01/B02 的硬输入，导致 B01 可能被错误地长期 `BLOCKED`。

修正口径：以 `game_narrative_master_plan.md` 为准，阶段 1 本来就是重做并扩充 `25–29`。因此：

- B01 改为创建 / 重建 `25` 与 `26`，输入来自上游故事骨架、白鹿原结构、白鹿之灵规则与角色接口。
- B02 改为创建 / 重建 `27` 与 `28`。
- B03/B04 改为创建 / 扩容 `29` 场景卡子包与总索引。
- 旧日志中提到的 `25–29` 不得被当作当前现存输入。

## 3. 批次总表

| Batch ID | 批次名称 | 目标 | 输入文件（不超过 10 个） | 主输出文件（不超过 2 个） | Review 文件 | 预计新增文本量 | 推荐执行时长 | 切换门槛 | 下一批 | 超体量 A/B 拆分规则 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B00 | 现有资产盘点与执行断点建立 | 盘点旧首批底盘、确认哪些只作输入参考、建立 recurring 执行断点 | `game_narrative_master_plan.md`; `game_narrative_master_plan_review.md`; `decision_log.md`; `04_current_state.md`; `session_handoff.md`; `game_narrative_final_acceptance.md`（如存在）; `story_master_execution_plan.md`（如存在） | `game_narrative_asset_inventory.md`; `game_narrative_rebuild_checkpoint.md` | `game_batch00_review.md` | 20,000–35,000 | 60–90 分钟 | 盘点表列出可复用锚点、需重写资产层、缺口与下一批输入 | B01 | A：只盘点文件与字数；B：建立断点与缺口清单 |
| B01 | 重建游戏级主线架构 A | 创建 / 重建 `25_volume1_core_conflict.md` 与 `26_volume1_revelation_ladder.md`，把上游故事骨架转为游戏级主问题、Act 主冲突、揭示阶梯与状态入口 | `08_story/01_story_premise_and_core_question.md`; `08_story/02_story_structure_draft.md`; `08_story/09_act_segment_skeleton.md`; `08_story/12_story_node_skeleton.md`; `08_story/15_chapter_cluster_skeleton.md`; `08_story/21_sealed_region_structure.md`; `08_story/22_sealed_region_tension_map.md`; `08_story/23_bailuyuan_key_nodes.md`; `08_story/24_white_deer_manifestation_rules.md`; `07_characters/15_party_entry_interfaces.md`; `07_characters/16_party_bailuyuan_alignment.md` | `25_volume1_core_conflict.md`; `26_volume1_revelation_ladder.md` | `game_phase1a_review.md` | 25,000–45,000 | 90–120 分钟 | Act 主问题、核心冲突、揭示层级、白鹿原边界与白鹿之灵边界通过 review；不得依赖 `25–29` 预先存在 | B02 | B00R 修正：旧 schedule 把阶段 1 输出误写为阶段 1 输入；本批改为从上游故事骨架重建 `25/26` |
| B02 | 重建游戏级主线架构 B | 创建 / 重建 `27_volume1_plot_spine.md` 与 `28_volume1_chapter_outline.md`，建立 40–80 个主线任务节点候选与 Act / 章节束承接关系 | `25_volume1_core_conflict.md`; `26_volume1_revelation_ladder.md`; `08_story/09_act_segment_skeleton.md`; `08_story/12_story_node_skeleton.md`; `08_story/15_chapter_cluster_skeleton.md`; `08_story/21_sealed_region_structure.md`; `08_story/22_sealed_region_tension_map.md`; `08_story/23_bailuyuan_key_nodes.md`; `game_narrative_rebuild_checkpoint.md`; `game_phase1a_review.md` | `27_volume1_plot_spine.md`; `28_volume1_chapter_outline.md` | `game_phase1b_review.md` | 30,000–50,000 | 90–150 分钟 | `27/28` 含任务节点候选、Act 结构、前置状态、输出状态与章节束映射；不得依赖 `27/28/29` 预先存在 | B03 | B00R 修正：B02 只产出 `27/28`，不再把 `29` 场景卡提前写成输入或同批主输出 |
| B03 | 重建游戏级场景卡 A | 创建 `29a_volume1_scene_cards_act1_act2.md`，扩容 Act 1 / Act 2 场景卡子包，要求每张卡具备存在理由、推动冲突、增权对象、前置状态、变体结果与输出状态 | `25_volume1_core_conflict.md`; `26_volume1_revelation_ladder.md`; `27_volume1_plot_spine.md`; `28_volume1_chapter_outline.md`; `08_story/21_sealed_region_structure.md`; `08_story/22_sealed_region_tension_map.md`; `08_story/23_bailuyuan_key_nodes.md`; `08_story/24_white_deer_manifestation_rules.md`; `07_characters/15_party_entry_interfaces.md`; `game_phase1b_review.md` | `29a_volume1_scene_cards_act1_act2.md` | `game_phase1c_review.md` | 30,000–50,000 | 90–150 分钟 | Act 1 / Act 2 场景卡不是小说摘要，必须可支持任务设计、状态差异和同伴插话接口 | B04 | A：Act 1 / Act 2 场景卡子包 |
| B04 | 重建游戏级场景卡 B 与总索引 | 创建 `29b_volume1_scene_cards_act3_epilogue.md` 并建立 / 更新 `29_volume1_scene_cards.md` 总索引，完成 Act 3 / Epilogue 场景卡子包与全阶段场景卡导航 | `25_volume1_core_conflict.md`; `26_volume1_revelation_ladder.md`; `27_volume1_plot_spine.md`; `28_volume1_chapter_outline.md`; `29a_volume1_scene_cards_act1_act2.md`; `08_story/21_sealed_region_structure.md`; `08_story/22_sealed_region_tension_map.md`; `08_story/23_bailuyuan_key_nodes.md`; `08_story/24_white_deer_manifestation_rules.md`; `game_phase1c_review.md` | `29_volume1_scene_cards.md`; `29b_volume1_scene_cards_act3_epilogue.md` | `game_phase1d_review.md` | 30,000–50,000 | 90–150 分钟 | `29` 总索引与场景卡子包完成；120–240 张场景卡的结构底盘具备前置状态、输出状态与变体结果 | B05 | B：Act 3 / Epilogue 场景卡子包；总索引汇总 `29a/29b` |
| B05 | 主线任务架构与 ID 体系 | 建立主线任务树、任务 ID、输入条件、关键选择、输出状态和状态机映射 | `25_volume1_core_conflict.md`; `26_volume1_revelation_ladder.md`; `27_volume1_plot_spine.md`; `29_volume1_scene_cards.md`; `29a_volume1_scene_cards_act1_act2.md`; `29b_volume1_scene_cards_act3_epilogue.md`; `game_narrative_rebuild_checkpoint.md`; `game_phase1d_review.md`; `canon_rules.md`; `glossary.md` | `32_main_quest_architecture.md`; `main_quest_id_and_state_registry.md` | `game_batch05_review.md` | 30,000–50,000 | 90–150 分钟 | 每个任务单元具备 ID、前置、目标、冲突、选择、输出状态与 Journal 更新位 | B06 | A：任务树与 ID；B：状态映射与 Journal 更新位；B05 以 `29a/29b` 已落地的状态接口为准，不依赖不存在的旧 review 文件名 |
| B06 | 主线任务文本 Act 1 | 扩写 Act 1 主线任务可用文本，覆盖场景叙述、关键对话、失败反馈与 Journal | `32_main_quest_architecture.md`; `main_quest_id_and_state_registry.md`; `29_volume1_scene_cards.md`; `14_bailuyuan_faction_state_machine.md`; `15_bailuyuan_region_state_machine.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch05_review.md`; `canon_rules.md`; `glossary.md` | `33a_main_quest_act1_mq01_mq06_text.md`; `33b_main_quest_act1_mq07_mq12_text.md` | `game_batch06_review.md` | 40,000–60,000 | 120–180 分钟 | Act 1 文本具备状态差异，不是单线假分支；白鹿之灵不越权 | B07 | A：MQ01–MQ06；B：MQ07–MQ12 |
| B07 | 主线任务文本 Act 2 | 扩写 Act 2 主线任务可用文本，强化中段揭示、势力压力与区域变化 | `32_main_quest_architecture.md`; `main_quest_id_and_state_registry.md`; `29_volume1_scene_cards.md`; `29a_volume1_scene_cards_act1_act2.md`; `33a_main_quest_act1_mq01_mq06_text.md`; `33b_main_quest_act1_mq07_mq12_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch06_review.md`; `canon_rules.md`; `glossary.md` | `34a_main_quest_act2_mq13_mq18_text.md`; `34b_main_quest_act2_mq19_mq24_text.md` | `game_batch07_review.md` | 40,000–60,000 | 120–180 分钟 | Act 2 文本能体现揭示阶梯、状态机影响与同伴插话接口 | B08 | A：MQ13–MQ18；B：MQ19–MQ24 |
| B08 | 主线任务文本 Act 3 / Epilogue（父批次） | 原批次覆盖 `MQ25–MQ48`，经校验显式输入含不存在的 `14/15`，且终局段保守预计超出 `180` 分钟；已按规则拆为 `B08A` / `B08B`，父批次不直接执行 | 见 `B08A` / `B08B` | `35a_main_quest_act3_mq25_mq34_text.md`; `35b_main_quest_act3_mq35_epilogue_text.md` | `game_batch08a_review.md`; `game_batch08b_review.md` | 40,000–60,000 | 120–240 分钟 | 父批次仅保留总边界：终局不是彻底重连或彻底封死；选择有代价、状态有反馈 | B08A | 已拆分：A=`MQ25–MQ34`；B=`MQ35–MQ48`；原 `14/15` 输入作废，改由 `29/29b` 的现存场景卡与前批正文承接 |
| B08A | 主线任务文本 Act 3 A | 扩写 `MQ25–MQ34`，覆盖灰线显形、异质承认、法宝翻面与绑定回返，停止在第三幕内，不进入 `MQ35+` | `32_main_quest_architecture.md`; `main_quest_id_and_state_registry.md`; `29_volume1_scene_cards.md`; `29b_volume1_scene_cards_act3_epilogue.md`; `34a_main_quest_act2_mq13_mq18_text.md`; `34b_main_quest_act2_mq19_mq24_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch07_review.md`; `canon_rules.md`; `glossary.md` | `35a_main_quest_act3_mq25_mq34_text.md` | `game_batch08a_review.md` | 25,000–35,000 | 90–150 分钟 | `MQ25–MQ34` 必须具备状态差异、失败回流、Journal 与白鹿之灵边界；不得提前进入 `MQ35+` | B08B | A：`MQ25–MQ27` 灰线显形；B：`MQ28–MQ34` 法宝翻面与绑定回返 |
| B08B | 主线任务文本 Act 3 B / Epilogue | 扩写 `MQ35–MQ48`，覆盖第三幕收束、代价聚焦、立场压缩、路径比较与受限未来，完成 B08 后段 | `32_main_quest_architecture.md`; `main_quest_id_and_state_registry.md`; `29_volume1_scene_cards.md`; `29b_volume1_scene_cards_act3_epilogue.md`; `35a_main_quest_act3_mq25_mq34_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch08a_review.md`; `canon_rules.md`; `glossary.md` | `35b_main_quest_act3_mq35_epilogue_text.md` | `game_batch08b_review.md` | 20,000–30,000 | 90–150 分钟 | `MQ35–MQ48` 必须把终局落回白鹿原受限未来，不得写成零代价尾声或上浮到整个 `古裂残天` | B09 | A：`MQ35–MQ38` 绑定回返收束；B：`MQ39–MQ48` 终局与尾声 |
| B09 | 同伴弧线矩阵与路线状态 | 重构七席位同伴弧光、Act 节点、路线敏感点、与主线交叉关系 | `15_party_entry_interfaces.md`; `16_party_bailuyuan_alignment.md`; `32_main_quest_architecture.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch08b_review.md`; `canon_rules.md`; `glossary.md` | `17_companion_arc_matrix.md`; `companion_route_state_map.md` | `game_batch09_review.md` | 30,000–50,000 | 90–150 分钟 | 每位同伴具备主命题、路线敏感点、节点反应接口，不只是设定卡 | B10 | A：七席位弧线；B：路线状态与主线交叉 |
| B10 | 同伴文本前中段（父批次） | 原批次覆盖初识、入队、Act 1 / Act 2 任务插话、节点反应与营地前中段文本；按 `17` / `33a` / `33b` / `34a` 的现有输入密度与双输出 review 负担，保守执行风险已逼近单批上限，现按规则拆为 `B10A` / `B10B`，父批次不直接执行 | 见 `B10A` / `B10B` | `18a_companion_dialogue_entry_act1_pack.md`; `18b_companion_dialogue_act2_reaction_pack.md` | `game_batch10a_review.md`; `game_batch10b_review.md` | 40,000–60,000 | 120–210 分钟 | 父批次仅保留总边界：前中段同伴文本必须随主线、区域与信任状态变化，不停留在营地闲聊，也不得提前写成第四幕路线明牌 | B10A | 已拆分：A=`初识/入队/Act 1`；B=`Act 2 任务插话/节点反应/营地中段` |
| B10A | 同伴文本前中段 A | 扩写七席位的初识、入队、`MQ01–MQ12` 插话、节点反应与营地前段文本，只推进到 `AS1`，不得进入 `MQ13+` 或 `AS2` 明牌 | `17_companion_arc_matrix.md`; `companion_route_state_map.md`; `32_main_quest_architecture.md`; `33a_main_quest_act1_mq01_mq06_text.md`; `33b_main_quest_act1_mq07_mq12_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch09_review.md`; `canon_rules.md`; `glossary.md` | `18a_companion_dialogue_entry_act1_pack.md` | `game_batch10a_review.md` | 20,000–35,000 | 90–150 分钟 | 初识 / 入队 / Act 1 文本必须把七席位推进到 `AS1`，埋下 `CA01–CA06` 底线，但不得提前写成 `AS3+` 或路线投票 | B10B | A：坠落区 / 聚落边线前段；B：封绝定性 / 主聚落承重前段 |
| B10B | 同伴文本前中段 B | 扩写 `MQ13–MQ24` 的 Act 2 任务插话、节点反应与营地中段文本，在 `B10A` 基础上把七席位推进到 `AS2`，不得提前写成第四幕路线明牌 | `17_companion_arc_matrix.md`; `companion_route_state_map.md`; `32_main_quest_architecture.md`; `34a_main_quest_act2_mq13_mq18_text.md`; `18a_companion_dialogue_entry_act1_pack.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch10a_review.md`; `canon_rules.md`; `glossary.md` | `18b_companion_dialogue_act2_reaction_pack.md` | `game_batch10b_review.md` | 20,000–30,000 | 90–150 分钟 | Act 2 文本必须把七席位推进到 `AS2`，强化现实优先级、资格争议与通路代价，不得提前进入 `MQ25+` 或 `AS4` 明牌 | B11 | A：`MQ13–MQ18` 风险 / 通路 / 资格反应；B：`MQ19–MQ24` 深因追问 / 营地中段 |
| B11 | 同伴文本后段与 Banter（父批次） | 原批次同时覆盖 Act 3 忠诚 / 路线压力、终局前后差异反馈、banter 与营地后段文本；按 `17` / `companion_route_state_map` / `35a` / `35b` 的现有输入密度与双输出 review 负担，保守执行风险已逼近并极易越过单批上限，现按规则拆为 `B11A` / `B11B`，父批次不直接执行 | 见 `B11A` / `B11B` | `19a_companion_dialogue_act3_loyalty_pack.md`; `20a_companion_banter_route_reaction_pack.md` | `game_batch11a_review.md`; `game_batch11b_review.md` | 40,000–70,000 | 120–240 分钟 | 父批次仅保留总边界：后段同伴文本必须承接 `AS2` 并推进到 `AS3/AS4/AS5` 的条件链，但不得把白鹿原上浮为整个 `古裂残天`，也不得把白鹿之灵写成路线裁判 | B11A | 已拆分：A=`Act 3 / 忠诚压力 / 路线前置`；B=`banter / 终局前后反馈 / 尾声余压` |
| B11A | 同伴文本后段 A | 扩写 `MQ25–MQ38` 的 Act 3 任务插话、节点反应、营地后段前半与忠诚压力文本，在 `B10B` 基础上把七席位从 `AS2` 推进到 `AS3`，允许埋入 `AS4` 条件句，但不得提前进入 `MQ39+` 或终局站队收束 | `17_companion_arc_matrix.md`; `companion_route_state_map.md`; `34b_main_quest_act2_mq19_mq24_text.md`; `35a_main_quest_act3_mq25_mq34_text.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch10b_review.md`; `canon_rules.md`; `glossary.md` | `19a_companion_dialogue_act3_loyalty_pack.md` | `game_batch11a_review.md` | 20,000–35,000 | 90–150 分钟 | Act 3 同伴文本必须把七席位推进到 `AS3`，把忠诚压力写成共同承压与条件支持，而不是二元站队或提前明牌终局路线 | B11B | A：`MQ25–MQ30` 灰线 / 异质 / 法宝翻面；B：`MQ31–MQ38` 绑定代价 / 命运卷入 / 第三幕收束 |
| B11B | 同伴文本后段 B / Banter | 扩写 `MQ39–MQ48` 的终局前后差异反馈、路线状态回收、banter、营地后段后半与尾声余压，在 `B11A` 基础上把七席位从 `AS3` 推进到 `AS4/AS5`，完成 B11 后段 | `17_companion_arc_matrix.md`; `companion_route_state_map.md`; `19a_companion_dialogue_act3_loyalty_pack.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch11a_review.md`; `canon_rules.md`; `glossary.md` | `20a_companion_banter_route_reaction_pack.md` | `game_batch11b_review.md` | 20,000–35,000 | 90–150 分钟 | banter 与终局反馈必须回收路线状态和尾声余压，保留差异接受、保留刺点与未清零代价，不得写成整齐鼓掌 | B12 | A：`MQ39–MQ42` 路线条件明牌；B：`MQ43–MQ48` 终局反馈 / 尾声余压 |
| B12 | 支线矩阵与聚落区域文本底盘 | 建立支线矩阵、聚落 / 区域文本规则、灰线接口与主线联动点 | `35b_main_quest_act3_mq35_epilogue_text.md`; `20a_companion_banter_route_reaction_pack.md`; `32_main_quest_architecture.md`; `17_companion_arc_matrix.md`; `13_bailuyuan_functional_map.md`; `21_sealed_region_structure.md`; `22_sealed_region_tension_map.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch11b_review.md`; `canon_rules.md` | `36_sidequest_matrix.md`; `39_settlement_and_region_texts.md` | `game_batch12_review.md` | 35,000–60,000 | 120–180 分钟 | 支线不是空目录，区域文本具备可交互触发点、失败回流与状态影响；不依赖缺失的旧 `14/15` 状态机文件 | B13 | A：支线矩阵；B：聚落与区域文本底盘 |
| B13 | 支线与灰线文本包 | 扩写支线对话、支线 Journal、多结局反馈、灰线节点与地方共同体事件 | `36_sidequest_matrix.md`; `39_settlement_and_region_texts.md`; `32_main_quest_architecture.md`; `17_companion_arc_matrix.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `20a_companion_banter_route_reaction_pack.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch12_review.md`; `canon_rules.md`; `glossary.md` | `37a_sidequest_text_pack_core_regions.md`; `38a_sidequest_text_pack_grayline_and_outskirts.md` | `game_batch13_review.md` | 40,000–60,000 | 120–180 分钟 | 支线有状态差异、失败结果、区域或同伴反馈，不写成世界说明附录；继续沿现有主线 / 同伴链而非缺失旧 `14/15` 输入 | B14 | A：主聚落 / 交换带 / 入口残带；B：裂伤外缘 / 隐匿潜伏层 / 法宝相关区 |
| B14 | Codex 与 Journal 文本包 | 扩写区域、势力、历史残忆、白鹿之灵词条与主支线 Journal 更新文本 | `32_main_quest_architecture.md`; `36_sidequest_matrix.md`; `37a_sidequest_text_pack_core_regions.md`; `38a_sidequest_text_pack_grayline_and_outskirts.md`; `39_settlement_and_region_texts.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch13_review.md`; `canon_rules.md`; `glossary.md` | `40a_codex_entries_bailuyuan_pack.md`; `41a_journal_and_update_texts_pack.md` | `game_batch14_review.md` | 35,000–60,000 | 120–180 分钟 | Codex / Journal 与主支线一致，不泄露超阶段真相，不替代正文推进 | B15 | A：Codex；B：Journal |
| B15 | Item / System 文本与最终整合准备（父批次） | 原批次同时覆盖 `42a`、`43a` 与 final readiness，按单批安全窗口已拆为 `B15A / B15B`，父批次不直接执行 | 见 `B15A / B15B` | `42a_items_relics_and_documents_pack.md`; `43a_system_feedback_texts_pack.md` | `game_batch15a_review.md`; `game_batch15b_review.md` | 35,000–60,000 | 120–180 分钟 | 父批次仅保留总边界：Item / System 层必须可调用，最终验收缺口清单留在 `B15B` 落地 | B15A | 已拆分：A=`Items / Documents`；B=`System feedback / final readiness` |
| B15A | Item / Document 文本 A | 扩写 `42a_items_relics_and_documents_pack.md`，建立法宝 / 任务 / 区域物品与文献底盘，供主线、支线、Codex、Journal 与后续 system 调用 | `40a_codex_entries_bailuyuan_pack.md`; `41a_journal_and_update_texts_pack.md`; `32_main_quest_architecture.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `37a_sidequest_text_pack_core_regions.md`; `38a_sidequest_text_pack_grayline_and_outskirts.md`; `17_companion_arc_matrix.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch14_review.md`; `canon_rules.md` | `42a_items_relics_and_documents_pack.md` | `game_batch15a_review.md` | 20,000–35,000 | 90–150 分钟 | 物品 / 文献必须具备来源、使用边界、尾声余压与调用接口；不得提前进入 system feedback 或 final readiness 清单 | B15B | A：法宝 / 任务物件；B：文书 / 抄件 / 缺口记录 |
| B15B | System 文本与最终整合准备 B | 扩写 `43a_system_feedback_texts_pack.md`，补齐 UI / 系统反馈文本，并生成进入最终验收前的缺口清单与调用边界 | `42a_items_relics_and_documents_pack.md`; `40a_codex_entries_bailuyuan_pack.md`; `41a_journal_and_update_texts_pack.md`; `35b_main_quest_act3_mq35_epilogue_text.md`; `37a_sidequest_text_pack_core_regions.md`; `38a_sidequest_text_pack_grayline_and_outskirts.md`; `17_companion_arc_matrix.md`; `game_narrative_rebuild_checkpoint.md`; `game_batch15a_review.md`; `canon_rules.md` | `43a_system_feedback_texts_pack.md` | `game_batch15b_review.md` | 15,000–30,000 | 90–150 分钟 | System feedback 必须承接 `42a / 40a / 41a` 调用面，并显式生成最终验收缺口清单；不得顺手进入最终验收轮 | END | A：系统即时反馈；B：最终整合缺口清单 |

## 4. 预建议拆分批次

以下批次天然接近体量上限，recurring automation 执行时建议优先按 A/B 子批次处理：

- B02：主线任务节点与场景卡扩展。
- B06：Act 1 主线任务文本。
- B07：Act 2 主线任务文本。
- B08：Act 3 / Epilogue 主线任务文本。
- B10：同伴前中段文本。
- B11：同伴后段与 banter。
- B12：支线矩阵与聚落区域文本底盘。
- B13：支线与灰线文本包。
- B14：Codex 与 Journal 文本包。
- B15：Item / System 文本与最终整合准备。

## 5. 第一次 recurring execution 建议

第一次自动执行应从 B00 开始。

B00 不生产主线、支线、同伴或系统正文，只做资产盘点、旧底盘可复用性判断、执行断点与缺口清单。它能避免后续 automation 把旧首批底盘误判为“大型 CRPG 总工程已完成”。

## 6. 完成定义

当 B00–B15 全部通过 review 后，才允许进入 `game_narrative_final_acceptance.md` 或等价最终验收轮。

在最终验收前，不得宣称大型 CRPG 叙事文本总工程完成；若累计文本量未达 `1,500,000` 汉字，不得宣称达到最低总量目标。
