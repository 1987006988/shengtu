# 阅读顺序与工作顺序（重构后）

## 1. 默认阅读顺序

### 第一组：项目真相入口（必读）
1. `README.md`
2. `AGENTS.md`
3. `worldbible/09_reference/project_total_verdict.md`
4. `worldbible/00_project_overview/04_current_state.md`
5. `worldbible/09_reference/session_handoff.md`
6. `worldbible/09_reference/reconstruction_route_map.md`
7. `worldbible/09_reference/file_operations_rebuild.md`

### 第二组：项目护栏（必读）
8. `worldbible/00_project_overview/01_project_brief.md`
9. `worldbible/00_project_overview/02_design_principles.md`
10. `worldbible/00_project_overview/03_scope_and_constraints.md`
11. `worldbible/00_project_overview/05_scope_map.md`
12. `worldbible/00_project_overview/06_stage_gates.md`
13. `worldbible/00_project_overview/07_directory_responsibilities.md`
14. `worldbible/00_project_overview/08_pre_task_layer_requirements.md`
15. `worldbible/09_reference/canon_rules.md`
16. `worldbible/09_reference/first_arc_vs_universe_scope.md`

### 第三组：宇宙与主世界根部（必读）
17. `worldbible/01_cosmology/01_universe_structure.md`
18. `worldbible/01_cosmology/02_ascension.md`
19. `worldbible/01_cosmology/03_world_tiers.md`
20. `worldbible/01_cosmology/04_macro_cosmic_layout.md`
21. `worldbible/01_cosmology/05_nine_main_worlds_draft.md`
22. `worldbible/01_cosmology/07_universe_longline_master.md`
23. `worldbible/04_main_world/01_main_world_foundations.md`
24. `worldbible/04_main_world/12_gulie_cantian_macro_structure.md`
25. `worldbible/04_main_world/14_gulie_cantian_rebuild_bible.md`
26. `worldbible/04_main_world/17_nine_main_world_longterm_usage_matrix.md`

### 第四组：白鹿原与前史（必读）
27. `worldbible/05_history/04_gulie_cantian_history.md`
28. `worldbible/05_history/08_first_arc_pre_story_timeline.md`
29. `worldbible/05_history/09_bailuyuan_prestory_timeline_rebuild.md`
30. `worldbible/06_society/06_sealed_region_survival_logic.md`
31. `worldbible/04_main_world/15_bailuyuan_region_bible.md`
32. `worldbible/04_main_world/16_book1_binding_boundary.md`

### 第五组：角色总控（必读）
33. `worldbible/07_characters/21_party_story_function_bible.md`
34. `worldbible/07_characters/22_character_progression_master.md`

### 第六组：第一部施工母本（必读）
35. `worldbible/08_story/50_series_master_outline.md`
36. `worldbible/08_story/51_book1_master_outline.md`
37. `worldbible/08_story/52_book1_volume_structure.md`
38. `worldbible/08_story/53_book1_act_structure.md`
39. `worldbible/08_story/54_book1_chapter_blueprint.md`
40. `worldbible/08_story/55_book1_scene_blueprint.md`
41. `worldbible/08_story/56_book1_reveal_foreshadow_table.md`
42. `worldbible/08_story/57_book1_character_progression_table.md`
43. `worldbible/08_story/58_book1_world_state_table.md`

## 2. 历史资产阅读顺序（只在需要时查）

只有在以上 43 步读完后，才允许回头查以下内容：

- `08_story/01–29` 中可回收的上游骨架文件；
- `07_characters/02 / 05 / 10 / 11 / 15 / 16` 中的旧角色接口文件；
- `08_story/30–43a` 与 `07_characters/17–20a` 的历史文本资产；
- `09_reference/game_narrative_*`、`game_batch*`、`game_phase*` 历史工程文件。

## 3. 默认工作顺序

工作时必须按下面顺序推进：

1. 先确认当前口径是否仍与 `current_state` 一致；
2. 再确认本轮工作属于哪一层：
   - 主世界层
   - 地区层
   - 角色层
   - 蓝图层
3. 只在上游层稳定后，才继续下游层；
4. 下游内容不得反向改写上游文件；
5. 若旧历史资产与新母本冲突，以新母本为准。

## 4. 绝对不要这样工作

- 不要一上来就打开 `33a–43a` 想继续补文；
- 不要从 `session_handoff` 之外的旧 batch 状态页判断“现在做到哪了”；
- 不要混着看 `task pack`、`world bible`、`review`、`acceptance` 试图拼出真相；
- 不要让旧 acceptance 命名影响你对当前阶段的判断。

## 5. 一句话提醒

> 先读新入口，再读上游承载层，最后才读第一部蓝图；历史资产只能回收，不能接管主线。
