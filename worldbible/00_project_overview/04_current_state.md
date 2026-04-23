# 04 当前状态

## 1. 文档用途

本文档用于维护项目级“当前状态页”，只保留当前有效状态，帮助后续协作者快速恢复上下文。

## 2. 项目一句话定位

本项目正式名为 `升途`，英文正式名为 `Ascendant Path`，仓库 / 目录英文名为 `shengtu`；目标是构建一个具有大型桌面角色扮演世界观深度的原创中式玄幻宇宙，并在第一款游戏 `升途：封绝之地` 中以 `白鹿原` 为强叙事 CRPG 舞台。

## 3. 当前模块

- 当前模块：`END：最终验收轮（已完成）`
- 当前状态：`B00–B15 与 END 已完成并通过 review；已确认首轮白鹿原大型 CRPG 叙事资产通过最终验收，但当前主输出总量约 572,037 字符级单位，尚未达到 1,500,000 汉字最低目标`
- 下一步：`如需继续 recurring batch，必须先人工新增第二轮扩容 / 生产期 batch schedule；当前不存在可自动继续的下一批`

## 4. 当前结论

- 《升途：封绝之地》已从单纯小说化故事稿，推进到大型 CRPG 叙事文本总工程方向。
- 已正式落库 `worldbible/09_reference/game_narrative_master_plan.md`，作为后续批次化执行的项目级总蓝图母本。
- 已建立 `worldbible/09_reference/game_narrative_batch_schedule.md`、`game_narrative_execution_state.md` 与 `game_narrative_batch_rules.md`，用于 recurring automations 判断下一个 batch、限制单次运行范围并强制 review。
- 已完成 B00、B00R、B01、B02、B03、B04、B05、B06、B07、`B08A`、`B08B`、`B09`、`B10A`、`B10B`、`B11A`、`B11B`、`B12` 与 `B13`。
- 已将原 `B08` 拆为 `B08A/B08B`，并修正其错误显式输入：废弃不存在的 `14/15`，改由当前已落地的 `29/29b` 场景卡与前批正文链承接。
- 已将原 `B10` 拆为 `B10A/B10B`，避免在单次 recurring run 中同时完成 Act 1 与 Act 2 同伴正文。
- 已新增 `worldbible/08_story/25_volume1_core_conflict.md`、`26_volume1_revelation_ladder.md`、`27_volume1_plot_spine.md`、`28_volume1_chapter_outline.md`。
- 已新增 `worldbible/08_story/29a_volume1_scene_cards_act1_act2.md`，建立 `MQ01–MQ24` 的 `40` 张场景卡。
- 已新增 `worldbible/08_story/29b_volume1_scene_cards_act3_epilogue.md`，建立第 `08–17` 章、`MQ25–MQ48` 的 `40` 张场景卡。
- 已新增 `worldbible/08_story/29_volume1_scene_cards.md`，把 `29a` 与 `29b` 统一编成全卷总索引，明确 `17` 章、`48` 个 MQ 节点、`80` 张场景卡与六项状态曲线的调用入口。
- 已新增 `worldbible/08_story/32_main_quest_architecture.md`，把全卷主线压成 `14` 组任务簇、`4` 幕 + `1` 个尾声层级与 `MQ01–MQ48` 的任务树。
- 已新增 `worldbible/08_story/main_quest_id_and_state_registry.md`，为 `MQ01–MQ48` 建立来源卡、进入条件、关键选择、状态写回、失败回流、Journal 锚与白鹿之灵边界。
- 已新增 `worldbible/08_story/33a_main_quest_act1_mq01_mq06_text.md`，把 `MQ01–MQ06` 扩写成主线任务正文、关键对白、失败反馈、Journal 文本与补充对白库。
- 已新增 `worldbible/08_story/33b_main_quest_act1_mq07_mq12_text.md`，把 `MQ07–MQ12` 扩写成主线任务正文、关键对白、失败反馈、Journal 文本与补充对白库。
- 已新增 `worldbible/08_story/34a_main_quest_act2_mq13_mq18_text.md`，把 `MQ13–MQ18` 扩写成主线任务正文、关键对白、失败反馈、Journal 文本与中段同伴插话接口。
- 已新增 `worldbible/08_story/34b_main_quest_act2_mq19_mq24_text.md`，把 `MQ19–MQ24` 扩写成主线任务正文、关键对白、失败反馈、Journal 文本与第二幕收束接口。
- 已新增 `worldbible/08_story/35a_main_quest_act3_mq25_mq34_text.md`，把 `MQ25–MQ34` 扩写成第三幕前中段主线任务正文、失败回流、Journal 文本与补充插话接口。
- 已新增 `worldbible/08_story/35b_main_quest_act3_mq35_epilogue_text.md`，把 `MQ35–MQ48` 扩写成第三幕后段、第四幕与尾声主线任务正文、失败回流、Journal 文本与补充插话接口，并把终局落回白鹿原受限未来。
- 已新增 `worldbible/07_characters/17_companion_arc_matrix.md`，把七席位压成卷内主命题、分幕推进、任务簇主责、终局条件支持与尾声差异矩阵。
- 已新增 `worldbible/07_characters/companion_route_state_map.md`，把七席位压成 `AS1–AS5` 相位、`RS+2` 至 `RS-2` 路线状态、`CA01–CA06` 判断轴、`PT01–PT04` 组合态与 `TV1–TV4` 尾声版本。
- 已新增 `worldbible/07_characters/18a_companion_dialogue_entry_act1_pack.md`，把七席位的初识、同行确认、`MQ01–MQ12` 插话、营地前段、多组节点级反应库与低信任变体压实到 `AS1`。
- 已新增 `worldbible/07_characters/18b_companion_dialogue_act2_reaction_pack.md`，把七席位的 `MQ13–MQ24` 插话、第二幕节点反应、营地中段、多组复盘句库与差异变体压实到 `AS2`。
- 已将原 `B11` 按 batch rules 拆为父批次 `SPLIT` + `B11A/B11B`，避免在单次 recurring run 中同时完成第三幕翻面文本与第四幕明牌 / banter 后段。
- 已新增 `worldbible/07_characters/19a_companion_dialogue_act3_loyalty_pack.md`，把七席位的 `MQ25–MQ38` 插话、第三幕节点反应、营地后段前半、复盘触发组、差异变体与错位对谈模板压实到 `AS3`。
- 已新增 `worldbible/07_characters/20a_companion_banter_route_reaction_pack.md`，把七席位的 `MQ39–MQ48` 路线条件回收、营地后段后半、banter、组合态调用模板与尾声余压压实到 `AS4 / AS5`。
- 已新增 `worldbible/08_story/36_sidequest_matrix.md`，把支线工程压成 `12` 条支线簇，逐条绑定主线窗口、区域落点、状态写回、灰线接口、同伴接口与 `B13` 展开要求。
- 已新增 `worldbible/08_story/39_settlement_and_region_texts.md`，把 `白鹿原` 的主聚落承接面、交换带、入口残带、裂伤外缘、隐匿潜伏层与法宝相关区压成 `6` 个区域文本包，并补齐互动槽、状态回显、失败回流与尾声回声规则。
- 已新增 `worldbible/08_story/37a_sidequest_text_pack_core_regions.md`，把 `SQ01–SQ06` 压成核心聚落 / 通路组六条可执行支线，补齐开场叙述、关键流程、对话文本、状态写回、失败回流、Journal 锚、区域回流与尾声钩子。
- 已新增 `worldbible/08_story/38a_sidequest_text_pack_grayline_and_outskirts.md`，把 `SQ07–SQ12` 压成灰线 / 外缘 / 法宝组六条可执行支线，补齐危区 / 回引 / 反证 / 借道 / 余压 / 尾声缺口正文、失败回流、Journal 锚、区域回流与低强度白鹿边界。
- 已新增 `worldbible/09_reference/game_phase1a_review.md`、`game_phase1b_review.md`、`game_phase1c_review.md`、`game_phase1d_review.md`、`game_batch05_review.md`、`game_batch06_review.md`、`game_batch07_review.md`、`game_batch08a_review.md`、`game_batch08b_review.md`、`game_batch09_review.md`，确认 B01–B09 均已通过 review。
- 已新增 `worldbible/09_reference/game_batch10a_review.md`，确认 `B10A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、拆分合法性与文本厚度通过 review。
- 已新增 `worldbible/09_reference/game_batch10b_review.md`，确认 `B10B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review，并使 `B10` 全段完成。
- 已新增 `worldbible/09_reference/game_batch11a_review.md`，确认 `B11A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、拆分合法性与文本厚度通过 review。
- 已新增 `worldbible/09_reference/game_batch11b_review.md`，确认 `B11B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、尾声余压与文本厚度通过 review，并使 `B11` 全段完成。
- 已新增 `worldbible/09_reference/game_batch12_review.md`，确认 `B12` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、schedule 修补合法性与文本厚度通过 review。
- 已新增 `worldbible/09_reference/game_batch13_review.md`，确认 `B13` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本密度通过 review，并记录“低于理想区间下沿但未退化为摘要”的风险说明。
- 已新增 `worldbible/08_story/40a_codex_entries_bailuyuan_pack.md`，把 `白鹿原` 的区域、分带、结构、行动面、历史残忆、法宝、白鹿之灵与受限未来压成可分阶段解锁的 Codex 条目包。
- 已新增 `worldbible/08_story/41a_journal_and_update_texts_pack.md`，把 `CL01–CL14`、`SQ01–SQ12`、六大区域状态更新、Codex 解锁提示、阶段短提示、失败回流与尾声不整齐更新压成可调用 Journal / 更新文本包。
- 已新增 `worldbible/09_reference/game_batch14_review.md`，确认 `B14` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与调用层完整性通过 review，并记录“体量低于理想区间下沿但未退化为摘要”的风险说明。
- 已将原 `B15` 按 batch rules 拆为父批次 `SPLIT` + `B15A/B15B`，避免在单次 recurring run 中同时完成物件 / 文献底盘、system feedback 与 final readiness 缺口层。
- 已新增 `worldbible/08_story/42a_items_relics_and_documents_pack.md`，把法宝 / 任务物件 / 灰线物件 / 文书底盘压成可直接被主线、支线、区域、Codex、Journal 与后续 system 调用的资产，并补齐现场调用块、失败回流矩阵、归档语气与尾声保留语气。
- 已新增 `worldbible/09_reference/game_batch15a_review.md`，确认 `B15A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与拆分合法性通过 review，并记录“体量贴近拆分后下沿但未退化为目录”的提醒。
- 已新增 `worldbible/08_story/43a_system_feedback_texts_pack.md`，把物件 / 文书底盘继续压成 system feedback 调用层，补齐获得 / 复查 / 预警 / 推进 / 同伴 / 失败回流文本，并显式列出进入最终验收前的 final readiness 缺口清单。
- 已新增 `worldbible/09_reference/game_batch15b_review.md`，确认 `B15B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review，并确认 `B15` 已由 `B15A / B15B` 全段完成。
- 已新增 `worldbible/09_reference/game_narrative_final_acceptance.md`，完成 `END：最终验收轮`，按 `43a` 的 `16` 项 final readiness 检查项对主线、支线、同伴、Codex、Journal、Item 与 System 调用面做最终验收。
- 已新增 `worldbible/09_reference/game_batch_end_review.md`，确认 `END` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review，并明确“本轮 batch schedule 完成”不等于“整个大型 CRPG 叙事文本总工程已完成”。
- 已最小修正 `worldbible/09_reference/game_narrative_batch_schedule.md` 中 B12 / B13 的失效 `14/15` 显式输入链，改由 `36/39 + 35b/20a` 的现有资产承接。
- `30_book1_story_draft.md` 与 `31_book1_story_revised.md` 继续保留为小说化参考底稿。
- 当前总目标仍是“大型 CRPG 叙事文本总工程”；但现阶段已完成的是首轮批次化重建与最终验收，不是全量内容生产完成。后续若继续推进，应在新 schedule 下做第二轮扩容 / 生产期，而不是回头重做已通过 END 的既有批次。

## 5. 已锁定原则 / 禁止随意改动项

- `白鹿原` 是第一款游戏主舞台，不等于整个 `古裂残天`。
- 不得改写宇宙通则、九主世界总层或 `古裂残天` 长期正典。
- 白鹿之灵是接引法宝之灵的白鹿显化，只能作为接口、残忆、触发器、示警与边界反馈。
- 白鹿之灵不得成为普通灵兽、独立神祇、世界意志、万能解释器、万能支援或万能真相机。
- 复生机制必须有代价、边界与状态反馈。
- 后续 B14 不得回头重做 `B13` 的支线与灰线正文，也不得把 `37a/38a` 压回目录式提纲、支线摘要或无失败回流的空壳框架。
- 第三幕与第四幕已锁定的白鹿之灵边界、失败回流、路线代价、承担者比较、七席位条件支持、尾声余压与白鹿原受限未来口径，不得在后续批次中被抹平或重写。
- 后续 B15 不得回头重做 `40a/41a`，也不得把 Codex / Journal 调用层再压回一次性提纲、占位卡或纯 UI 占位句。
- 后续若新增第二轮 batch，不得回头重做 `42a` 或 `43a`，也不得把物件 / 文献层与 system 层压回条目目录、占位卡或只剩标题的索引页。

## 6. 下一步动作

- 当前 batch schedule 已执行至终点，下一次 recurring run 不存在自动可执行的下一批。
- 若需继续自动执行，必须先人工新增第二轮扩容 / 生产期 batch schedule，并同步更新 `game_narrative_batch_schedule.md` 与 `game_narrative_execution_state.md`。
- 在新的 schedule 建立前，不得回头重做 `B15A`、`B15B`、`B14`、`B13`、`B12`、`B09`、`B10A/B10B`、`B11A/B11B` 或 `B08A/B08B`。

## 7. 下次恢复上下文时应优先阅读的文件

- `AGENTS.md`
- `worldbible/09_reference/canon_rules.md`
- `worldbible/09_reference/glossary.md`
- `worldbible/09_reference/decision_log.md`
- `worldbible/00_project_overview/05_scope_map.md`
- `worldbible/00_project_overview/06_stage_gates.md`
- `worldbible/00_project_overview/08_pre_task_layer_requirements.md`
- `worldbible/00_project_overview/04_current_state.md`
- `worldbible/09_reference/session_handoff.md`
- `worldbible/09_reference/game_narrative_batch_schedule.md`
- `worldbible/09_reference/game_narrative_execution_state.md`
- `worldbible/09_reference/game_narrative_batch_rules.md`
- `worldbible/09_reference/game_narrative_rebuild_checkpoint.md`
- `worldbible/08_story/32_main_quest_architecture.md`
- `worldbible/08_story/main_quest_id_and_state_registry.md`
- `worldbible/08_story/34a_main_quest_act2_mq13_mq18_text.md`
- `worldbible/08_story/34b_main_quest_act2_mq19_mq24_text.md`
- `worldbible/08_story/35a_main_quest_act3_mq25_mq34_text.md`
- `worldbible/08_story/35b_main_quest_act3_mq35_epilogue_text.md`
- `worldbible/07_characters/17_companion_arc_matrix.md`
- `worldbible/07_characters/companion_route_state_map.md`
- `worldbible/07_characters/18a_companion_dialogue_entry_act1_pack.md`
- `worldbible/07_characters/18b_companion_dialogue_act2_reaction_pack.md`
- `worldbible/07_characters/19a_companion_dialogue_act3_loyalty_pack.md`
- `worldbible/07_characters/20a_companion_banter_route_reaction_pack.md`
- `worldbible/08_story/36_sidequest_matrix.md`
- `worldbible/08_story/37a_sidequest_text_pack_core_regions.md`
- `worldbible/08_story/38a_sidequest_text_pack_grayline_and_outskirts.md`
- `worldbible/08_story/39_settlement_and_region_texts.md`
- `worldbible/08_story/42a_items_relics_and_documents_pack.md`
- `worldbible/09_reference/game_batch15a_review.md`
- `worldbible/09_reference/game_batch13_review.md`
- `worldbible/09_reference/game_batch12_review.md`
- `worldbible/09_reference/game_batch11b_review.md`
- `worldbible/09_reference/game_batch11a_review.md`
- `worldbible/09_reference/game_batch10b_review.md`
- `worldbible/09_reference/game_batch10a_review.md`
- `worldbible/09_reference/game_batch09_review.md`
- `worldbible/09_reference/game_batch08a_review.md`
- `worldbible/09_reference/game_batch08b_review.md`
- `worldbible/08_story/29b_volume1_scene_cards_act3_epilogue.md`
- `worldbible/08_story/29_volume1_scene_cards.md`
- `worldbible/09_reference/game_phase1d_review.md`
