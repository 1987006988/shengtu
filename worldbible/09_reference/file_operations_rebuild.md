# 文件操作清单（重构版）

## 1. 操作原则

本清单不是“把旧文件全部推倒重来”，而是按以下原则处理：

- **保留**：上层世界观中已成立、可继续承重的正式文件。
- **重写**：口径已失真或承重不足，但仍处于正确目录层级的文件。
- **新增**：旧仓库缺失、但后续施工必需的正式母本文件。
- **合并**：多个内容相近、接口重复、容易造成口径分裂的文件，收束到单一母本。
- **降级**：保留内容价值，但取消其“当前真实状态 / 主入口 / 当前主线”资格。
- **废弃为主入口**：文件可保留为历史记录，但后续不得再作为默认入口读取。
- **历史归档**：批次 review / acceptance / phase 文档全部转入历史区或被阅读顺序降到最后。

## 2. 保留为正式正典主干（可轻修但不推翻）

### 2.1 项目级
- `README.md`
- `AGENTS.md`
- `worldbible/00_project_overview/01_project_brief.md`
- `worldbible/00_project_overview/02_design_principles.md`
- `worldbible/00_project_overview/03_scope_and_constraints.md`
- `worldbible/00_project_overview/05_scope_map.md`
- `worldbible/00_project_overview/06_stage_gates.md`
- `worldbible/00_project_overview/07_directory_responsibilities.md`
- `worldbible/00_project_overview/08_pre_task_layer_requirements.md`

### 2.2 宇宙与规则层
- `worldbible/01_cosmology/01_universe_structure.md`
- `worldbible/01_cosmology/02_ascension.md`
- `worldbible/01_cosmology/03_world_tiers.md`
- `worldbible/01_cosmology/04_macro_cosmic_layout.md`
- `worldbible/01_cosmology/05_nine_main_worlds_draft.md`
- `worldbible/02_power_system/01_foundations.md`
- `worldbible/02_power_system/02_anchor_system.md`
- `worldbible/03_worlds_and_paths/01_world_templates.md`
- `worldbible/03_worlds_and_paths/02_path_classification.md`
- `worldbible/03_worlds_and_paths/03_template_usage_rules.md`

### 2.3 主世界 / 历史 / 社会层
- `worldbible/04_main_world/01_main_world_foundations.md`
- `worldbible/04_main_world/05_story_main_world_draft.md`
- `worldbible/04_main_world/06_main_world_comparison.md`
- `worldbible/04_main_world/07_nine_main_worlds_difference_matrix.md`
- `worldbible/04_main_world/12_gulie_cantian_macro_structure.md`
- `worldbible/05_history/01_eras_and_calendar.md`
- `worldbible/05_history/02_cosmic_history.md`
- `worldbible/05_history/03_nine_main_worlds_history.md`
- `worldbible/05_history/04_gulie_cantian_history.md`
- `worldbible/05_history/05_historical_faultlines.md`
- `worldbible/05_history/06_nine_main_worlds_era_matrix.md`
- `worldbible/05_history/08_first_arc_pre_story_timeline.md`
- `worldbible/06_society/01_main_world_social_models.md`
- `worldbible/06_society/02_immortal_mortal_relation_models.md`
- `worldbible/06_society/03_gulie_cantian_society_draft.md`
- `worldbible/06_society/04_gulie_cantian_four_tier_society.md`
- `worldbible/06_society/05_social_faultlines.md`
- `worldbible/06_society/06_sealed_region_survival_logic.md`

### 2.4 参考层中仍有价值的规则文件
- `worldbible/09_reference/canon_rules.md`
- `worldbible/09_reference/first_arc_vs_universe_scope.md`
- `worldbible/09_reference/decision_log.md`
- 现有命名 / glossary / canon 相关文件（若存在）

## 3. 必须重写

### 3.1 项目状态与入口
- `worldbible/00_project_overview/04_current_state.md`
- `worldbible/09_reference/session_handoff.md`

### 3.2 白鹿原承载层
- `worldbible/04_main_world/11_bailuyuan_faction_landscape.md`
- `worldbible/04_main_world/13_bailuyuan_functional_map.md`

### 3.3 角色总控入口
- `worldbible/07_characters/11_character_concept_cards.md`  
  说明：保留原“概念卡”历史价值，但必须被新的角色总控文件覆盖其主入口资格。

### 3.4 故事模块入口
- `worldbible/08_story/00_index.md`  
  说明：重写为“蓝图层入口”，明确当前不默认进入任务包 / 文本包层。

## 4. 新增正式母本（本套文件）

### 4.1 参考与治理
- `worldbible/09_reference/project_total_verdict.md`
- `worldbible/09_reference/project_core_conclusions.md`
- `worldbible/09_reference/file_operations_rebuild.md`
- `worldbible/09_reference/reconstruction_route_map.md`
- `worldbible/09_reference/reading_order.md`
- `worldbible/09_reference/execution_plan_rebuild.md`
- `worldbible/09_reference/context_recovery_prompt.md`

### 4.2 宇宙与主世界承载层
- `worldbible/01_cosmology/07_universe_longline_master.md`
- `worldbible/04_main_world/14_gulie_cantian_rebuild_bible.md`
- `worldbible/04_main_world/15_bailuyuan_region_bible.md`
- `worldbible/04_main_world/16_book1_binding_boundary.md`
- `worldbible/04_main_world/17_nine_main_world_longterm_usage_matrix.md`
- `worldbible/05_history/09_bailuyuan_prestory_timeline_rebuild.md`

### 4.3 角色母本
- `worldbible/07_characters/21_party_story_function_bible.md`
- `worldbible/07_characters/22_character_progression_master.md`

### 4.4 故事施工母本
- `worldbible/08_story/50_series_master_outline.md`
- `worldbible/08_story/51_book1_master_outline.md`
- `worldbible/08_story/52_book1_volume_structure.md`
- `worldbible/08_story/53_book1_act_structure.md`
- `worldbible/08_story/54_book1_chapter_blueprint.md`
- `worldbible/08_story/55_book1_scene_blueprint.md`
- `worldbible/08_story/56_book1_reveal_foreshadow_table.md`
- `worldbible/08_story/57_book1_character_progression_table.md`
- `worldbible/08_story/58_book1_world_state_table.md`

## 5. 建议合并为新母本，不再分散读取

### 5.1 白鹿原文件合并
将以下旧文件的有效内容并入 `15_bailuyuan_region_bible.md`：
- `11_bailuyuan_faction_landscape.md`
- `13_bailuyuan_functional_map.md`
- `06_sealed_region_survival_logic.md` 中对白鹿原的关键承载逻辑
- `08_story/21_sealed_region_structure.md`
- `08_story/22_sealed_region_tension_map.md`
- `08_story/23_bailuyuan_key_nodes.md`
- `08_story/24_white_deer_manifestation_rules.md`

### 5.2 角色入口合并
将以下文件的“有效结构层内容”并入 `21_party_story_function_bible.md`：
- `02_protagonist_party_framework.md`
- `05_party_seat_blueprint.md`
- `10_party_entry_order.md`
- `11_character_concept_cards.md`
- `15_party_entry_interfaces.md`
- `16_party_bailuyuan_alignment.md`

### 5.3 第一部蓝图合并
将以下旧文件的“有效上游骨架内容”并入 50–58 系列文件：
- `01_story_premise_and_core_question.md`
- `02_story_structure_draft.md`
- `03_party_entry_and_reveal_order.md`
- `04_conflict_layers.md`
- `05_space_progression_draft.md`
- `06_mainline_beats.md`
- `07_act_turning_points.md`
- `08_reveal_pacing_map.md`
- `09_act_segment_skeleton.md`
- `10_story_progression_map.md`
- `11_reveal_and_pressure_curve.md`
- `12_story_node_skeleton.md`
- `13_act_node_progression.md`
- `14_character_node_weight_map.md`
- `15_chapter_cluster_skeleton.md`
- `16_cluster_progression_map.md`
- `17_cluster_character_pressure_map.md`
- `25_volume1_core_conflict.md`
- `26_volume1_revelation_ladder.md`
- `27_volume1_plot_spine.md`
- `28_volume1_chapter_outline.md`
- `29_volume1_scene_cards.md` 及其拆包文件

## 6. 必须降级为历史资产 / 参考仓

### 6.1 第一轮任务文本与系统文本资产
以下文件不删除，但取消“当前主线”资格，统一标注为：
> `历史资产 / narrative lab round 1 / 非当前默认正史入口`

- `worldbible/08_story/30_book1_story_draft.md`
- `worldbible/08_story/31_book1_story_revised.md`
- `worldbible/08_story/32_main_quest_architecture.md`
- `worldbible/08_story/33a_main_quest_act1_mq01_mq06_text.md`
- `worldbible/08_story/33b_main_quest_act1_mq07_mq12_text.md`
- `worldbible/08_story/34a_main_quest_act2_mq13_mq18_text.md`
- `worldbible/08_story/34b_main_quest_act2_mq19_mq24_text.md`
- `worldbible/08_story/35a_main_quest_act3_mq25_mq34_text.md`
- `worldbible/08_story/35b_main_quest_act3_mq35_epilogue_text.md`
- `worldbible/08_story/36_sidequest_matrix.md`
- `worldbible/08_story/37a_sidequest_text_pack_core_regions.md`
- `worldbible/08_story/38a_sidequest_text_pack_grayline_and_outskirts.md`
- `worldbible/08_story/39_settlement_and_region_texts.md`
- `worldbible/08_story/40a_codex_entries_bailuyuan_pack.md`
- `worldbible/08_story/41a_journal_and_update_texts_pack.md`
- `worldbible/08_story/42a_items_relics_and_documents_pack.md`
- `worldbible/08_story/43a_system_feedback_texts_pack.md`

### 6.2 角色 late-stage 文本包
- `worldbible/07_characters/17_companion_arc_matrix.md`
- `worldbible/07_characters/18a_companion_dialogue_entry_act1_pack.md`
- `worldbible/07_characters/18b_companion_dialogue_act2_reaction_pack.md`
- `worldbible/07_characters/19a_companion_dialogue_act3_loyalty_pack.md`
- `worldbible/07_characters/20a_companion_banter_route_reaction_pack.md`
- `worldbible/07_characters/companion_route_state_map.md`

### 6.3 过度工程化的批次文档
- `worldbible/09_reference/game_narrative_master_plan.md`
- `worldbible/09_reference/game_narrative_batch_schedule.md`
- `worldbible/09_reference/game_narrative_execution_state.md`
- `worldbible/09_reference/game_narrative_final_acceptance.md`
- `worldbible/09_reference/story_master_execution_plan.md`
- 全部 `game_batch*_review.md`
- 全部 `game_phase*_review.md`
- `game_batch_end_review.md`

## 7. 废弃为主入口

以下文件可以保留，但以后**不得再作为主入口文件**：

- 旧 `worldbible/00_project_overview/04_current_state.md`
- 旧 `worldbible/09_reference/session_handoff.md`
- `worldbible/09_reference/game_narrative_execution_state.md`
- `worldbible/09_reference/game_narrative_final_acceptance.md`
- `worldbible/09_reference/game_narrative_master_plan.md`

## 8. 以后不能再这样做

- 不能再以“已有大量文本包”为理由跳过白鹿原地区圣经重建。
- 不能再让 `09_reference` 继续膨胀成 batch 审批仓。
- 不能再把 `08_story` 默认入口放在任务包 / 文本包层。
- 不能再用 acceptance / final / end 等命名制造阶段完成错觉。

## 9. 一句话执行口径

> **保住世界观成立部分；撤销错误阶段口径；冻结旧批次工程为历史资产；用新的主世界—地区—角色—章节—场景蓝图重新接管项目。**
