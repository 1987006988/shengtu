# 决策日志

## REBUILD-2026-04-23-01：GPT Pro 重构结果接管轮

- 日期：2026-04-23
- 状态：已确认
- 模块：00_project_overview / 01_cosmology / 04_main_world / 05_history / 07_characters / 08_story / 09_reference
- 决策主题：以 `D:\download` 中的 GPT Pro 重构 bundle 正式接管仓库主入口与当前阶段口径
- 变更类型：入口接管 / 阶段重定义 / 历史资产降级
- 背景：仓库此前长期沿用旧 `game_narrative batch / END / final acceptance / 首轮大型 CRPG 文本工程已完成` 口径，已不再符合当前真实状态；用户要求以 GPT Pro 重构结果接管当前仓库，并将项目切换到“主世界承载层与第一部施工蓝图重建阶段”。
- 决策内容：确认以 `D:\download\shengtu_rebuild_bundle.zip` 解压后的分文件 bundle 作为唯一主来源；正式落库 `project_total_verdict`、`project_core_conclusions`、`file_operations_rebuild`、`reconstruction_route_map`、`reading_order`、`execution_plan_rebuild`、`context_recovery_prompt`、`07_universe_longline_master`、`14–17`、`09_bailuyuan_prestory_timeline_rebuild`、`21/22`、`50–58`，并以 bundle 中的新 `04_current_state.md` 与新 `session_handoff.md` 接管项目入口；确认当前真实阶段改为 `主世界承载层与第一部施工蓝图重建阶段`，在 `50–58` 蓝图闭环完成前不默认进入任务层；确认旧 `33a–43a`、`17–20a`、`companion_route_state_map.md`、`game_narrative_*`、`game_batch*`、`game_phase*`、`*final_acceptance*`、`*execution_state*` 与 `story_master_execution_plan.md` 全部降级为历史资产 / narrative lab round 1，不再作为当前主入口真相。
- 影响范围：`README.md`、`AGENTS.md`、`worldbible/00_project_overview/04_current_state.md`、`worldbible/01_cosmology/07_universe_longline_master.md`、`worldbible/04_main_world/00_index.md`、`worldbible/04_main_world/11_bailuyuan_faction_landscape.md`、`worldbible/04_main_world/13_bailuyuan_functional_map.md`、`worldbible/04_main_world/14_gulie_cantian_rebuild_bible.md`、`worldbible/04_main_world/15_bailuyuan_region_bible.md`、`worldbible/04_main_world/16_book1_binding_boundary.md`、`worldbible/04_main_world/17_nine_main_world_longterm_usage_matrix.md`、`worldbible/05_history/09_bailuyuan_prestory_timeline_rebuild.md`、`worldbible/07_characters/00_index.md`、`worldbible/07_characters/11_character_concept_cards.md`、`worldbible/07_characters/21_party_story_function_bible.md`、`worldbible/07_characters/22_character_progression_master.md`、`worldbible/08_story/00_index.md`、`worldbible/08_story/50_series_master_outline.md`、`worldbible/08_story/51_book1_master_outline.md`、`worldbible/08_story/52_book1_volume_structure.md`、`worldbible/08_story/53_book1_act_structure.md`、`worldbible/08_story/54_book1_chapter_blueprint.md`、`worldbible/08_story/55_book1_scene_blueprint.md`、`worldbible/08_story/56_book1_reveal_foreshadow_table.md`、`worldbible/08_story/57_book1_character_progression_table.md`、`worldbible/08_story/58_book1_world_state_table.md`、`worldbible/09_reference/00_index.md`、`worldbible/09_reference/project_total_verdict.md`、`worldbible/09_reference/project_core_conclusions.md`、`worldbible/09_reference/file_operations_rebuild.md`、`worldbible/09_reference/reconstruction_route_map.md`、`worldbible/09_reference/reading_order.md`、`worldbible/09_reference/execution_plan_rebuild.md`、`worldbible/09_reference/context_recovery_prompt.md`、`worldbible/09_reference/session_handoff.md`
- 关联术语：GPT Pro 重构结果接管轮、主世界承载层、第一部施工蓝图、历史资产、narrative lab round 1、白鹿原地区圣经、古裂残天长期承重主世界、七席位总控
- 关联文件：`D:\download\shengtu_rebuild_bundle.zip`、`D:\download\shengtu_rebuild_master_document.md`、`D:\download\shengtu_rebuild_master_document (1).md`、`D:\download\04_current_state.md`、`D:\download\session_handoff.md`、`D:\download\context_recovery_prompt.md`
- 替代或继承关系：替代旧 `END / final acceptance / 首轮大型 CRPG 文本工程已完成` 的当前状态口径；旧 batch 工程保留为历史记录，不再继承为默认工作主线
- 备注：本次接管不是继续旧 batch，也不是继续扩写 `33a–43a`、`17–20a` 或任何 MQ / SQ / Journal / Codex / Item / System feedback 正文包；后续默认只继续 `古裂残天总层 + 白鹿原地区圣经 + 七席位总控 + 第一部 50–58 蓝图闭环`。
## GAME-2026-04-23-07：schedule 终点复核与无任务停机确认

- 日期：2026-04-23
- 状态：已确认
- 模块：00_project_overview / 09_reference
- 决策主题：本轮 recurring batch run 复核后确认当前无下一批可执行 batch
- 变更类型：执行状态复核 / 停机断点同步
- 背景：`END` 已在上一轮完成并通过 `game_batch_end_review.md`，但 recurring automation 再次唤醒时仍需按 batch rules 先读取 schedule、execution state、current state 与 handoff，确认是否存在新的 `IN_PROGRESS` 或依赖满足的最早 `PENDING` batch。
- 决策内容：确认截至 2026-04-23 17:48:51 +08:00，`worldbible/09_reference/game_narrative_execution_state.md` 中不存在 `PENDING`、`IN_PROGRESS` 或 `BLOCKED` 批次；因此本轮不执行任何新的 batch，不生成新的主输出文件或 review 文件，也不擅自创建第二轮 schedule；仅同步执行状态、当前状态、会话交接与 automation memory，把断点锁定为“等待人工新增第二轮扩容 / 生产期 batch schedule”。
- 影响范围：`09_reference/game_narrative_execution_state.md`、`00_project_overview/04_current_state.md`、`09_reference/session_handoff.md`
- 关联术语：`END`、recurring batch run、execution state、schedule 终点、第二轮扩容 / 生产期 schedule
- 关联文件：`worldbible/09_reference/game_narrative_execution_state.md`、`worldbible/09_reference/game_narrative_batch_schedule.md`、`worldbible/09_reference/game_narrative_batch_rules.md`、`worldbible/00_project_overview/04_current_state.md`、`worldbible/09_reference/session_handoff.md`
- 替代或继承关系：继承 `GAME-2026-04-23-06` 的 `END` 完成结论；不新增任何后继 batch；仅把本轮 automation 行为明确为“无任务停机”
- 备注：本次停机不构成 `BLOCKED`；原因不是依赖冲突，而是当前 schedule 已执行到终点。若后续仍需 recurring batch，必须先人工新增第二轮 schedule，再更新 execution state。
## GNB-2026-04-23-01：B15B 完成与最终验收入口切换

- 日期：2026-04-23
- 状态：已确认
- 模块：08_story / 09_reference
- 决策主题：`B15B：System 文本与最终整合准备 B` 完成并切换到 `END` 入口
- 变更类型：批次完成确认 / 执行门槛切换
- 背景：原 `B15` 已按 batch rules 拆为 `B15A / B15B`；`B15A` 已完成物件 / 文书底盘，但在进入最终验收前仍缺 system feedback 调用层与显式 final readiness 缺口清单。
- 决策内容：确认新增 `worldbible/08_story/43a_system_feedback_texts_pack.md`，用于承接 `42a / 40a / 41a / 35b / 37a / 38a / 17` 的既有结果，补齐获得、复查、预警、推进、同伴与失败回流的 system feedback 文本，并显式列出 `16` 项进入 `END` 前的 final readiness 缺口检查项；确认 `worldbible/09_reference/game_batch15b_review.md` 已通过；确认父批次 `B15` 已由 `B15A / B15B` 全段完成，下一步只允许进入 `END：最终验收轮`。
- 影响范围：`08_story/43a_system_feedback_texts_pack.md`、`09_reference/game_batch15b_review.md`、`09_reference/game_narrative_execution_state.md`、`09_reference/game_narrative_rebuild_checkpoint.md`、`00_project_overview/04_current_state.md`、`09_reference/session_handoff.md`
- 关联术语：`B15B`、`END`、system feedback、final readiness、白鹿之灵边界、受限未来
- 关联文件：`worldbible/08_story/43a_system_feedback_texts_pack.md`、`worldbible/09_reference/game_batch15b_review.md`、`worldbible/09_reference/game_batch15a_review.md`、`worldbible/08_story/42a_items_relics_and_documents_pack.md`
- 替代或继承关系：继承 `B15` 拆分执行口径；不改写 `B15A` 完成事实；把项目断点从 `B15B 待执行` 更新为 `END 待执行`
- 备注：本次确认只切换到最终验收入口，不等于最终验收已经通过；`43a` 中的缺口清单只服务验收前检查，不可直接当作最终验收结论。

## NAM-2026-04-15-01：项目命名统一与高频文件快审

- 项目中文总名正式定为：`升途`。
- 项目英文正式名正式定为：`Ascendant Path`。
- 仓库 / 目录英文名正式定为：`shengtu`。
- 第一部标题正式定为：`升途：封绝之地`。
- 本轮已执行命名统一与高频入口文件快审。
- 文档口径已统一为 `shengtu`；若物理目录仍保留旧工程名，需由人工在文件系统层执行重命名。
- 快审确认：`07_characters` 与 `08_story` 继续保持隔绝地域尺度，未发现需要改写的“大尺度主世界主线”残留。

## NAM-2026-04-17-01：命名规则补全

- `worldbible/09_reference/naming_rules.md` 已从占位稿补成正式可执行版。
- `worldbible/09_reference/naming_review_checklist.md` 已新增，用于反复执行命名审核。
- 命名规则文件已正式纳入项目级护栏 / 执行规范，不属于世界观正典正文。
- 后续新增正式命名应优先受命名规则、审核清单、术语表、正典规则与决策日志共同约束。
- 本轮只补命名规则、禁用规则、审核清单与最小必要同步，不新增大量正式专名，不推进任务层。

## BRG-2026-04-17-01：分层执行落地轮

- 已执行一轮“分层执行落地轮”。
- 已把“宇宙长期正典 / `古裂残天` 长期正典 / 第一部强绑定设定”继续压入高频执行文件。
- 已补强 `worldbible/09_reference/worldbuilding_audit_report.md`、`bridge_repair_report.md` 与 `cross_module_risk_map.md` 的分层风险归类。
- 已新增 `worldbible/09_reference/scope_execution_guide.md`，用于后续写作、修桥与自检时执行三层分层。
- 当前可判定护栏稳定度进一步提升，但仍不默认进入任务层；下一步仍应根据整体护栏稳定度决定继续补桥还是进入更细层开发。

## ARC-2026-04-17-01：第一部舞台细化轮

- 已执行“第一部舞台细化轮：隔绝地域结构落地”。
- 已完成隔绝地域结构总图、生存逻辑与结构性张力图的第一轮落地。
- 已新增 `worldbible/08_story/21_sealed_region_structure.md`、`worldbible/06_society/06_sealed_region_survival_logic.md`、`worldbible/08_story/22_sealed_region_tension_map.md`。
- 已形成 `worldbible/09_reference/sealed_region_naming_options.md` 作为正式命名预案，但当前未拍板、未写回正典。
- 本轮内容属于第一部强绑定设定层，不上浮为 `古裂残天` 长期正典或宇宙长期正典。

## ARC-2026-04-17-02：第一部舞台最后收口轮

- 已完成“第一部舞台最后收口轮”。
- 该轮曾提出将 `离序残域` 作为第一部主舞台正式设定名；此命名口径已被 `ARC-2026-04-17-03` 回撤。
- 六层结构与三带总括已定：核心维持带、生存承接带、崩坏潜伏带为高层概括，六层结构继续作为详细执行模型。
- 三类力量功能权重已定：地方承接层现实托底权重最高，守护残余结构控制权重最高，反抗残余变量改写权重最高。
- 下一阶段切换为“第一部势力与关键节点落位阶段”。

## ARC-2026-04-17-03：隔绝地域命名回撤修正

- 已执行“小范围命名回撤修正”。
- 曾提出将 `离序残域` 作为第一部主舞台正式命名方向。
- 经人工判断，现确认 `离序残域` 不适合作为当前这片隔绝地域的正式地名。
- 当前这片隔绝地域的正式命名继续待人工拍板。
- `离序残域` 仅可保留为可选工作代号 / 档案代号 / 描述性标签，不写入正典正式地名层。
- 本次只回撤命名口径，不改写六层结构、三带总括、三类力量功能权重，也不推进任务层。

## ARC-2026-04-17-04：第一部舞台最后收口轮

- 已执行“第一部舞台最后收口轮”。
- 第一部主舞台正式设定名已拍板为 `白鹿原`。
- 命名层级正式区分为：`升途` 是项目总名，`升途：封绝之地` 是第一部标题 / 叙事层称呼，`白鹿原` 是第一部主舞台在设定正文中的正式地域名；“隔绝地域 / 封绝地域”是功能性描述。
- 接引法宝之灵已正式收口为白鹿显化，其性质为主线核心装置的灵性接口，不是普通灵兽、独立神祇或 `古裂残天` 整体意志。
- 白鹿之灵功能边界已定：可识别飞升者与接引对象、维系最低限度接引秩序、作为主角团复生机制直接接口，并保留部分接引体系残忆、路径记忆与秩序碎片；不可替主角团解决结构性冲突、不可无限制无代价复生、不可取代三类力量现实作用、不可作为万能真相解释器、不可代表整个 `古裂残天` 意志。
- 三类力量功能权重继续沿用并写死：地方承接层现实托底权重最高，守护残余结构控制权重最高，反抗残余变量改写权重最高。
- 下一阶段切换为“第一部势力与关键节点落位阶段”。

## GOV-2026-04-17-01：第一部目录治理与阶段门槛轮

- 已执行“第一部目录治理与阶段门槛轮”。
- 已建立 `worldbible/00_project_overview/06_stage_gates.md`，用于明确当前推荐开发阶段顺序、各阶段输入前提、允许产物、禁止越界项与切换门槛。
- 已建立 `worldbible/00_project_overview/07_directory_responsibilities.md`，用于明确 `01_cosmology` 至 `09_reference` 当前阶段的目录职责与允许深度。
- 已建立 `worldbible/00_project_overview/08_pre_task_layer_requirements.md`，用于明确进入任务层前必须满足的前置条件。
- 当前仍不默认进入任务层。
- 下一步继续保持为“白鹿原势力与关键节点落位阶段”。

## STO-2026-04-17-02：第一部故事总控计划建立

- 已建立 `worldbible/09_reference/story_master_execution_plan.md`。
- 已把《升途：封绝之地》从阶段 0 到阶段 7 的输入、产出、自检重点、切换门槛与总验收标准压成正式执行计划。
- 本次确认后，第一部推进方式从“停在舞台承载准备”切换为“按计划连续推进到完整故事结果”。

## STO-2026-04-17-03：阶段一完成

- 已新增 `worldbible/04_main_world/12_gulie_cantian_macro_structure.md` 与 `worldbible/05_history/08_first_arc_pre_story_timeline.md`。
- 已将 `古裂残天` 总层、白鹿原第一部定位与从大战到开场的前史逻辑链压稳。
- 已确认主角团卷入白鹿原的宏观逻辑为“接引异常 + 法宝残接口 + 白鹿原需要新变量”。
- 已新增阶段回顾 `worldbible/09_reference/story_phase1_review.md`。

## STO-2026-04-17-04：阶段二完成

- 已新增 `worldbible/04_main_world/11_bailuyuan_faction_landscape.md`、`worldbible/08_story/23_bailuyuan_key_nodes.md`、`worldbible/04_main_world/13_bailuyuan_functional_map.md`、`worldbible/08_story/24_white_deer_manifestation_rules.md`。
- 白鹿原已从“设定舞台”推进为“可承载故事的舞台”。
- 已明确白鹿之灵只能作为法宝灵性接口使用，不得越权为万能解释器或万能支援。
- 已新增阶段回顾 `worldbible/09_reference/story_phase2_review.md`。

## STO-2026-04-17-05：阶段三完成

- 已新增 `worldbible/07_characters/15_party_entry_interfaces.md` 与 `worldbible/07_characters/16_party_bailuyuan_alignment.md`。
- 七席位已与白鹿原舞台、三类力量、白鹿之灵和接引残忆形成稳定接口。
- 已明确前段观察口、中段穿透口与后段增权口的角色分工。
- 已新增阶段回顾 `worldbible/09_reference/story_phase3_review.md`。

## STO-2026-04-17-06：阶段四完成

- 已新增 `worldbible/08_story/25_volume1_core_conflict.md`、`worldbible/08_story/26_volume1_revelation_ladder.md`、`worldbible/08_story/27_volume1_plot_spine.md`。
- 第一卷主问题正式收口为“白鹿原要如何继续存在，以及谁承担代价”。
- 第一卷终局正式收口为“争得受限未来路径”，而非彻底重连或彻底封死。
- 已新增阶段回顾 `worldbible/09_reference/story_phase4_review.md`。

## STO-2026-04-17-07：阶段五完成

- 已新增 `worldbible/08_story/28_volume1_chapter_outline.md` 与 `worldbible/08_story/29_volume1_scene_cards.md`。
- 第一卷已具备 16 章章纲与 24 张场景卡，可直接支持正文开写。
- 本轮明确这些场景卡属于小说场景层，不等于任务表。
- 已新增阶段回顾 `worldbible/09_reference/story_phase5_review.md`。

## STO-2026-04-17-08：阶段六完成

- 已新增 `worldbible/08_story/30_book1_story_draft.md`。
- 已完成第一部完整故事初稿，形成从坠落、求存、穿透到决断的完整正文闭环。
- 已新增阶段回顾 `worldbible/09_reference/story_phase6_review.md`。

## STO-2026-04-17-09：阶段七完成与项目状态切换

- 已新增 `worldbible/08_story/31_book1_story_revised.md` 与 `worldbible/09_reference/story_final_acceptance_report.md`。
- 已完成第一部故事修订稿，并通过总验收。
- 当前项目状态正式切换为：`第一部故事完成稿`。
- 当前状态正式更新为：已完成从白鹿原承载面到第一部故事修订稿的全流程构建。
- 下一步正式切换为：进入正文优化 / 审稿阶段。

## 1. 使用说明

- 本文件用于记录重大设定决定、确认过程、影响范围与回溯信息。
- 凡是跨模块、改动核心术语、改变底层结构或会引发设定冲突风险的内容，都必须记录。
- 旧口径如已被新口径覆盖，应显式说明继承或覆盖关系，不做无痕删除。

## 2. 统一记录模板

### [DECISION-ID]

- 日期：
- 状态：待确认 / 已确认 / 已废弃 / 已被更新口径覆盖
- 模块：
- 决策主题：
- 变更类型：
- 背景：
- 决策内容：
- 影响范围：
- 关联术语：
- 关联文件：
- 替代或继承关系：
- 备注：

## 3. 日志记录

### [COS-2026-04-12-01]

- 日期：2026-04-12
- 状态：已确认
- 模块：01_cosmology
- 决策主题：宇宙结构第一版定稿
- 变更类型：模块定稿确认
- 背景：需要为后续力量体系、世界设定、飞升制度与跨界剧情提供统一地基。
- 决策内容：确认三层宇宙结构为小世界 / 主世界 / 更高层界域；确认小世界与主世界构成明确位格高低关系；确认主世界为复数存在；确认飞升是先触规后感知接引并完成的位格跃迁；确认稳定飞升依赖主世界建立的接引体系与上升通道；确认高位世界对低位世界的干涉受位格差异、世界承载上限、规则冲突与通道成本共同限制。
- 影响范围：01_cosmology、02_power_system、03_worlds_and_paths、04_main_world、05_history、06_society、08_story
- 关联术语：规则、飞升、小世界、主世界、更高层界域、位格、接引、上升通道、跨界干涉、秩序
- 关联文件：`worldbible/01_cosmology/01_universe_structure.md`、`worldbible/01_cosmology/02_ascension.md`、`worldbible/01_cosmology/03_world_tiers.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：宇宙结构模块第一版正式定稿
- 备注：本次只确认宇宙结构层结论，不展开力量体系细节、具体势力结构、角色信息与具体剧情。

### [POW-2026-04-12-01]

- 日期：2026-04-12
- 状态：已确认
- 模块：02_power_system
- 决策主题：力量体系第一版正式稿
- 变更类型：模块定稿确认
- 背景：需要为后续世界设定、职业源流、飞升制度与高阶修行结构提供统一力量通则。
- 决策内容：正式确认气为诸天万界一切超凡现象的共同根源；规则为真实存在、数量有限的深层秩序；法为众生修行过程中总结出的诸般方法与路径，不是独立本体；修行者与规则的关系通常经历感知、映照、借用、掌控四个层次；锚点定义为修行者真实接触规则之后建立的主规则凭依，并遵守主锚点唯一原则。
- 影响范围：02_power_system、03_worlds_and_paths、04_main_world、06_society、07_characters、08_story
- 关联术语：气、规则、法、感知、映照、借用、掌控、锚点、主锚点、一锚多载体、器物型锚点、肉身型锚点、象征 / 秩序型锚点、结构型锚点
- 关联文件：`worldbible/02_power_system/01_foundations.md`、`worldbible/02_power_system/02_anchor_system.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：02_power_system 第一版正式稿
- 备注：本次只确认背景世界通则，不展开具体势力、人物、剧情、玩法与主角专属设定。

### [POW-2026-04-12-02]

- 日期：2026-04-12
- 状态：已确认
- 模块：02_power_system
- 决策主题：气 / 规则 / 法的表达补强与边界澄清
- 变更类型：表达完善与边界澄清
- 背景：在不改写核心结论的前提下，需要增强正式文档的完整度、长期可维护性与误解防护能力。
- 决策内容：补强了气的环境性、流动性、偏性、可塑性与不绝性表达；补强了规则的真实性、有限性、差异性、非同名性与边界说明；补强了法的桥梁性、多样性、方法性与文明性表达；明确这些变更属于表达完善，不构成核心定义重写。
- 影响范围：02_power_system、03_worlds_and_paths、04_main_world、06_society、08_story
- 关联术语：气、规则、法、锚点
- 关联文件：`worldbible/02_power_system/01_foundations.md`、`worldbible/02_power_system/02_anchor_system.md`、`worldbible/02_power_system/qi_rule_fa_research_notes.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `POW-2026-04-12-01`，不重写核心结论
- 备注：本次补强只涉及表述、边界、误解澄清与非采纳方向，不新增剧情、玩法、势力、人物或具体法宝实例。

### [WAP-2026-04-12-01]

- 日期：2026-04-12
- 状态：已确认
- 模块：03_worlds_and_paths
- 决策主题：小世界道路模板库第一阶段启动
- 变更类型：模块启动与框架确认
- 背景：需要为后续具体小世界设定、飞升者归类与道路源流扩写提供统一模板库与分类语言。
- 决策内容：正式确认 `03_worlds_and_paths` 第一阶段完成；小世界模板固定为八个主模板；单个小世界通常采用“一个主模板 + 一个副模板”的结构；当前阶段只建立模板层、分类框架与使用规则，不进入具体世界、具体小说映射、具体势力、具体人物与具体剧情。
- 影响范围：03_worlds_and_paths、04_main_world、05_history、06_society、07_characters、08_story
- 关联术语：世界模板、主模板、副模板、道路源流、飞升者归类及八个主模板名称
- 关联文件：`worldbible/03_worlds_and_paths/01_world_templates.md`、`worldbible/03_worlds_and_paths/02_path_classification.md`、`worldbible/03_worlds_and_paths/03_template_usage_rules.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：03_worlds_and_paths 第一阶段
- 备注：当前只确认模板层结构，不进入具体小世界正文。

### [MW-2026-04-12-01]

- 日期：2026-04-12
- 状态：已确认
- 模块：04_main_world
- 决策主题：主世界第一轮框架稿与研究补强启动
- 变更类型：模块启动与初稿确认
- 背景：需要先为主世界 / 主大陆建立基础框架，再为后续社会、历史、制度与剧情模块提供统一前提。
- 决策内容：确认 `04_main_world` 第一轮完成主世界基础框架、主大陆与小世界差异草案、修炼比较稿与研究笔记；重点围绕规则完整度、空间厚度、秩序基础设施、修炼起点与节奏、道路总谱与地方偏科、历史层次与文明寿命六个差异维度展开；当前属于“内部框架初稿 + 研究补强稿”，不是最终定稿。
- 影响范围：04_main_world、05_history、06_society、07_characters、08_story
- 关联术语：主大陆、空间厚度、秩序基础设施、道路总谱、地方偏科、飞升者价值
- 关联文件：`worldbible/04_main_world/01_main_world_foundations.md`、`worldbible/04_main_world/02_mainland_vs_small_worlds.md`、`worldbible/04_main_world/03_research_notes.md`、`worldbible/04_main_world/04_cultivation_comparison.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：04_main_world 第一轮
- 备注：本次不进入具体地名、势力、区域名、剧情与玩法。

### [MW-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：04_main_world
- 决策主题：主世界体量与空间厚度规则收口
- 变更类型：结构收口与执行口径补充
- 背景：需要将 `04_main_world` 从“概念正确”推进到“可执行设定”。
- 决策内容：确认主大陆核心文明区整体体量约等于 30–50 个成熟小世界；当前故事所聚焦的整个主世界体系整体体量约等于 100–300 个成熟小世界；单个成熟小世界在主大陆中的对应位置更接近域级单位；确认主世界存在稳定附属空间层，表现为洞天、碎界、遗迹等长期附着结构，并显著支撑高阶资源与高阶修行；确认下界飞升者的价值还体现于路径更纯、体系依赖更低、在不完整规则环境中更接近规则本身的触达方式。
- 影响范围：04_main_world、05_history、06_society、07_characters、08_story
- 关联术语：主大陆、空间厚度、秩序基础设施、道路总谱、飞升者价值
- 关联文件：`worldbible/04_main_world/01_main_world_foundations.md`、`worldbible/04_main_world/02_mainland_vs_small_worlds.md`、`worldbible/04_main_world/04_cultivation_comparison.md`
- 替代或继承关系：继承 `MW-2026-04-12-01`，属于第一轮收口补强
- 备注：本次不新增势力、地名、剧情与玩法，只补执行尺度、空间规则与结构性对比。

### [COS-2026-04-13-02]

- 日期：2026-04-13
- 状态：已确认
- 模块：01_cosmology
- 决策主题：九主世界与三千小世界宏观格局草案启动
- 变更类型：上层宇宙结构补完与宏观分布确认
- 背景：在 `01_cosmology`、`02_power_system`、`03_worlds_and_paths` 与 `04_main_world` 形成基础结构后，需要补足更上层的宇宙宏观格局，以承接后续故事主世界细化。
- 决策内容：确认宇宙第一层共有 `3000` 个小世界，并与“3000 大道 / 3000 规则”的宇宙观形成象征对应；确认宇宙第二层共有 `9` 个主世界；宏观分配采用 `6` 个常规主世界、`2` 个强势主世界、`1` 个古老残缺主世界，以及约 `120` 个失落、争夺、断联或归属不清的灰色小世界；同步启动九主世界第一轮世界卡草案与对应研究笔记。
- 影响范围：01_cosmology、04_main_world、05_history、06_society、08_story
- 关联术语：九主世界、世界群、灰色小世界、失落小世界、争夺小世界、主世界统治形式、仙凡关系模型、主世界档位
- 关联文件：`worldbible/01_cosmology/04_macro_cosmic_layout.md`、`worldbible/01_cosmology/05_nine_main_worlds_draft.md`、`worldbible/01_cosmology/06_research_notes_main_worlds.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `COS-2026-04-12-01`，在既有三层宇宙结构之上补完第二层宏观分布
- 备注：本次属于宏观格局第一轮草案，不等于九主世界最终定稿。

### [COS-2026-04-13-03]

- 日期：2026-04-13
- 状态：已确认
- 模块：01_cosmology / 04_main_world
- 决策主题：九主世界统一结构初稿与故事主世界重点深描启动
- 变更类型：结构补完与重点世界深化
- 背景：在九主世界宏观格局已建立后，需要把九个主世界补成统一结构的可比较世界卡，并把故事主世界单独推进到重点深描层。
- 决策内容：九个主世界已完成统一结构初稿，全部具备统一字段；天阙序庭与皇极法朝的仙凡关系边界已再次压实；故事主世界正式采用古老残缺修复型主世界方向，并进入第一版重点深描阶段；其他主世界保持“可比较、可区分”的骨架设定，不进入具体剧情与具体地名层。
- 影响范围：01_cosmology、04_main_world、05_history、06_society、08_story
- 关联术语：主世界统治形式、仙凡关系模型、古老残缺修复型主世界、旧势力、新势力、隐势力、地方势力
- 关联文件：`worldbible/01_cosmology/05_nine_main_worlds_draft.md`、`worldbible/01_cosmology/06_research_notes_main_worlds.md`、`worldbible/04_main_world/05_story_main_world_draft.md`、`worldbible/04_main_world/06_main_world_comparison.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `COS-2026-04-13-02`，从宏观分布草案推进到统一世界卡和重点主世界深描
- 备注：本次未写入具体剧情事件、具体人物、具体地名、具体法宝与玩法内容。

### [COS-2026-04-13-04]

- 日期：2026-04-13
- 状态：已确认
- 模块：04_main_world / 01_cosmology
- 决策主题：古裂残天收口补强与九主世界差异对照表生成
- 变更类型：结构收口与差异审阅支撑
- 背景：在九主世界统一世界卡和故事主世界重点深描初稿完成后，需要把古裂残天的核心格局进一步收口，并为九主世界提供一份可快速审阅的差异对照结构。
- 决策内容：古裂残天的旧时代统治格局正式拍板为“双极顶层势力统治”；双极旧秩序最终爆发高烈度大战，并以一方残胜告终；残胜者保有名义中心与部分旧秩序合法性，但无力恢复对全域的恒压统治；古裂残天的空间形态正式锁定为“受损主大陆 + 裂散群陆 + 外海体系 + 大量附属空间层”；九主世界差异对照表已新增，用于压实主世界边界与换皮风险识别。
- 影响范围：01_cosmology、04_main_world、06_society、08_story
- 关联术语：残胜、名义中心、双极旧秩序、结构性裂伤、古老残缺修复型主世界
- 关联文件：`worldbible/01_cosmology/05_nine_main_worlds_draft.md`、`worldbible/04_main_world/05_story_main_world_draft.md`、`worldbible/04_main_world/07_nine_main_worlds_difference_matrix.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `COS-2026-04-13-03`，进一步压实故事主世界核心格局
- 备注：本次仅做收口补强，不新增具体人物、地名、法宝、剧情事件与玩法内容。

### [MW-2026-04-13-02]

- 日期：2026-04-13
- 状态：已确认
- 模块：04_main_world
- 决策主题：古裂残天统治结构与社会结构草案启动
- 变更类型：重点世界细层结构补完
- 背景：在古裂残天的大框架、残胜格局与空间形态已锁定后，需要进一步明确其统治层、地方层、暗线层与社会分层逻辑，以支撑后续区域、制度与势力展开。
- 决策内容：古裂残天正式收口为“大势力主导型格局”，不是多强权并立；残胜后的中心大势力仍是全世界最强主导者，但因结构性裂伤、统治半径收缩、执行链条不完整与外围治理成本过高，无法恢复旧时代对全域的恒压统治；反抗势力来源正式明确为旧敌残余、不认同当前统治风格者，以及借裂伤成长的暗线力量；同步启动古裂残天统治结构草案、社会结构草案与权力层级草案。
- 影响范围：04_main_world、06_society、08_story
- 关联术语：主导势力、残胜格局、统治边界、暗线势力、反抗势力、地方势力、名义中心
- 关联文件：`worldbible/04_main_world/05_story_main_world_draft.md`、`worldbible/04_main_world/08_story_main_world_governance_draft.md`、`worldbible/04_main_world/09_story_main_world_society_draft.md`、`worldbible/04_main_world/10_story_main_world_power_layers.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `COS-2026-04-13-04`，进入故事主世界更细层结构设定
- 备注：本次只补背景结构，不新增具体人物、具体地名、法宝细节、剧情事件与玩法内容。

### [MW-2026-04-13-03]

- 日期：2026-04-13
- 状态：已确认
- 模块：04_main_world
- 决策主题：古裂残天统治结构与社会结构正式收口
- 变更类型：分歧收口与正式口径确认
- 背景：在古裂残天统治结构与社会结构草案形成后，需要清除仍待拍板的旧分歧版本，并把当前阶段正式口径写回相关文件。
- 决策内容：古裂残天名义中心正式收口为“中心仍强，但区域执行力分层衰减”；古裂残天正式采用四级社会模型，即核心区、地方区、群陆外海区、空间入口带；地方势力与中心关系正式收口为“依附坐大为主，区域自立为辅”；反抗势力正式收口为“分散残余逐步汇流，并最终形成长期渗透网络”；空间入口带正式收口为“半军事化管理下的高风险秩序市场”。
- 影响范围：04_main_world、01_cosmology、06_society、08_story
- 关联术语：名义中心、执行力衰减、四级社会模型、依附坐大、渗透网络、高风险秩序市场、反抗势力、地方势力
- 关联文件：`worldbible/04_main_world/05_story_main_world_draft.md`、`worldbible/04_main_world/08_story_main_world_governance_draft.md`、`worldbible/04_main_world/09_story_main_world_society_draft.md`、`worldbible/04_main_world/10_story_main_world_power_layers.md`、`worldbible/01_cosmology/05_nine_main_worlds_draft.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `MW-2026-04-13-02`，并覆盖其中仍未拍板的旧分歧版本
- 备注：本次只做正式收口，不新增具体人物、地名、法宝、剧情事件与玩法内容。

### [OVR-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：00_project_overview / 全仓库
- 决策主题：仓库范围正式校准
- 变更类型：范围边界与协作护栏确认
- 背景：随着九主世界与故事主世界内容不断增加，需要明确各目录分别服务于宇宙通则层、主世界层、故事主世界层与游戏聚焦层，防止整个仓库逐步写窄为 `古裂残天` 专属仓库。
- 决策内容：正式确认本仓库是宇宙级设定仓库；古裂残天只是当前重点展开对象，不是整个仓库的唯一对象；明确 `01_cosmology`、`02_power_system`、`03_worlds_and_paths` 属于宇宙通则层，`04_main_world` 属于主世界层并兼容故事主世界层，`05_history` 与 `06_society` 应先写主世界总层再落到故事主世界层，`07_characters` 与 `08_story` 属于游戏聚焦层；明确游戏聚焦层内容不得反向定义宇宙通则文件。
- 影响范围：全仓库
- 关联术语：宇宙通则层、主世界层、故事主世界层、游戏聚焦层、范围地图
- 关联文件：`README.md`、`AGENTS.md`、`worldbible/00_project_overview/00_index.md`、`worldbible/00_project_overview/05_scope_map.md`、各模块 `00_index.md`、`worldbible/00_project_overview/04_current_state.md`
- 替代或继承关系：新增项目级范围护栏，不改写既有世界观正典内容
- 备注：本次只做范围校准、索引更新与协作规范补强，不新增具体世界观设定。

### [HIS-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：05_history
- 决策主题：历史模块第一轮框架搭建
- 变更类型：模块启动与历史书写方法确认
- 背景：在宇宙结构、力量体系、小世界模板、九主世界草案与古裂残天阶段性展开已建立后，需要为整个仓库补上可持续扩写的历史骨架。
- 决策内容：`05_history` 已正式开启；历史模块采用“时代框架 + 总时间轴 + 分层历史”写法；当前阶段先写宇宙总史与九主世界格局史，再写古裂残天重点史；当前阶段不展开 `3000` 小世界个体历史，而只保留世界群与历史层级框架；同时保留历史断层、多版本记载与非唯一真相的书写边界。
- 影响范围：05_history、01_cosmology、04_main_world、06_society、08_story
- 关联术语：时代划分、宇宙总史、世界群格局史、历史断层、多版本记载、修复期、当前时代
- 关联文件：`worldbible/05_history/00_index.md`、`worldbible/05_history/01_eras_and_calendar.md`、`worldbible/05_history/02_cosmic_history.md`、`worldbible/05_history/03_nine_main_worlds_history.md`、`worldbible/05_history/04_gulie_cantian_history.md`、`worldbible/05_history/05_historical_faultlines.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：新增历史模块方法框架，不改写既有宇宙结构、力量体系与主世界口径
- 备注：本次优先搭建历史结构，不进入具体年份、大量碎事件、角色前史、游戏前史与玩法内容。

### [HIS-2026-04-13-02]

- 日期：2026-04-13
- 状态：已确认
- 模块：05_history
- 决策主题：九主世界七时代历史映射表建立
- 变更类型：历史轨迹补完与横向比较框架确认
- 背景：在历史模块第一轮框架已建立后，需要让九个主世界在统一时代框架下都拥有清晰、可比较、可扩写的历史位置，而不是停留在静态世界卡差异。
- 决策内容：九主世界七时代历史映射表已建立；九主世界当前差异进一步落实为“历史路径差异”，而不是静态设定差异；古裂残天已被放入九主世界整体历史框架中，而非孤立展开；当前阶段仍不进入细年表、具体战役过程与 `3000` 小世界个体历史。
- 影响范围：05_history、01_cosmology、04_main_world、06_society、08_story
- 关联术语：历史映射、七时代轨迹、延续型文明、转型型文明、九主世界
- 关联文件：`worldbible/05_history/03_nine_main_worlds_history.md`、`worldbible/05_history/06_nine_main_worlds_era_matrix.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `HIS-2026-04-13-01`，从历史框架推进到九主世界统一轨迹层
- 备注：本次不新增具体人物、地名、法宝、战役过程、剧情与玩法内容。

### [SOC-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：06_society
- 决策主题：社会模块第一轮框架搭建
- 变更类型：模块启动与社会书写方法确认
- 背景：在宇宙结构、力量体系、主世界差异与历史模块框架已建立后，需要为社会层补上“主世界总层 + 故事主世界落地层”的正式骨架。
- 决策内容：`06_society` 已正式开启；社会模块采用“主世界社会总层 + 古裂残天落地层”写法；先写主世界社会模型总论与仙凡关系模型，再写古裂残天社会落地；古裂残天社会正式被写成区域差异混合型，而非单一仙凡模型，并继续承接其四级社会模型；当前阶段不进入剧情、角色、玩法、任务与具体地区风物细节。
- 影响范围：06_society、04_main_world、05_history、07_characters、08_story
- 关联术语：主世界社会模型、仙凡关系模型、区域差异混合型社会、四级社会模型、地方共同体、风险治理区、高风险秩序市场
- 关联文件：`worldbible/06_society/00_index.md`、`worldbible/06_society/01_main_world_social_models.md`、`worldbible/06_society/02_immortal_mortal_relation_models.md`、`worldbible/06_society/03_gulie_cantian_society_draft.md`、`worldbible/06_society/04_gulie_cantian_four_tier_society.md`、`worldbible/06_society/05_social_faultlines.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：新增社会模块方法框架，不改写既有主世界与历史正典
- 备注：本次优先搭建社会结构骨架，不写剧情、角色、玩法、任务与具体地名人物。

### [CHR-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：07_characters
- 决策主题：角色模块第一轮框架搭建
- 变更类型：模块启动与角色书写方法确认
- 背景：在宇宙结构、主世界格局、历史层与社会层已建立后，需要为游戏聚焦层补上角色来源模型、主角团框架与角色类别骨架，避免直接滑入零散人物小传写法。
- 决策内容：`07_characters` 已正式开启；角色模块采用“来源模型 + 主角团框架 + 角色类别”写法；当前阶段先写角色为什么会从这个宇宙与古裂残天现实格局中长出来，再写具体是谁；当前阶段不直接写完整角色传记；主角团不得全部来自同一种模板或同一种势力来源，角色模块也不得反向定义宇宙通则文件。
- 影响范围：07_characters、08_story、06_society、05_history
- 关联术语：角色来源模型、主角团框架、阵营角色、历史承载型角色、反抗网络人物、地方关键人物
- 关联文件：`worldbible/07_characters/00_index.md`、`worldbible/07_characters/01_character_source_models.md`、`worldbible/07_characters/02_protagonist_party_framework.md`、`worldbible/07_characters/03_major_role_categories.md`、`worldbible/07_characters/04_character_generation_rules.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：新增角色模块方法框架，不改写既有宇宙结构、主世界与社会层正典
- 备注：本次只搭角色接口层，不写姓名、对白、剧情桥段、任务线、恋爱线与结局线。

### [CHR-2026-04-13-02]

- 日期：2026-04-13
- 状态：已确认
- 模块：07_characters
- 决策主题：主角团七席位角色原型骨架
- 变更类型：主角团结构收口与席位分布确认
- 背景：在角色来源模型、主角团框架与角色类别已建立后，需要进一步把主角团压成可比较、可扩写、但尚未落到具体人物传记的七席位原型结构。
- 决策内容：主角团正式采用 `1 主角位 + 6 关键同伴位`；整体来源比例采用 `3` 个飞升者接口与 `3` 个本土 / 灰线接口；中心体系位、地方接口位、边缘流动位、灰线历史位明确纳入主角团骨架；主角位默认来自高含金量飞升者来源；反抗网络来源人物进入核心同伴层；历史承载型角色与灰线位合并，不单独拆出纯解释型角色；当前阶段仍不直接写完整角色传记。
- 影响范围：07_characters、08_story、06_society、05_history
- 关联术语：角色席位、主角团框架、中心体系位、地方接口位、边缘流动位、灰线历史位、角色来源模型
- 关联文件：`worldbible/07_characters/05_party_seat_blueprint.md`、`worldbible/07_characters/06_party_role_distribution.md`、`worldbible/07_characters/07_companion_contrast_rules.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `CHR-2026-04-13-01`，从角色框架层推进到主角团席位原型层
- 备注：本次只确认席位原型与分布逻辑，不写正式姓名、完整生平、对白、任务线、恋爱线与结局线。

### [CHR-2026-04-13-03]

- 日期：2026-04-13
- 状态：已确认
- 模块：07_characters
- 决策主题：七席位具体角色原型第一轮设计
- 变更类型：角色原型层推进与接口锁定
- 背景：在主角团七席位骨架已建立后，需要进一步把每个席位推进到可落地的角色原型层，同时仍然停在“非传记化、非剧情化”的设计阶段。
- 决策内容：三个飞升位模板覆盖正式锁定为正统宗门修仙模板、剑道 / 本命器模板、香火 / 神道 / 佛国模板；中心体系位立场区间正式锁定为“中心秩序的现实执行者”，不是中心意识形态的绝对代言人；灰线历史位正式锁定为“以历史余波承载者为主，兼具反抗网络接口”；七席位角色原型设计已正式开启，并通过角色原型卡、结构张力图与进入顺序结构推进；当前阶段仍不写正式姓名与完整人物传记。
- 影响范围：07_characters、08_story、06_society、05_history
- 关联术语：角色原型卡、结构张力图、功能代号、进入顺序、中心体系位、灰线历史位
- 关联文件：`worldbible/07_characters/08_party_archetype_cards.md`、`worldbible/07_characters/09_party_tension_map.md`、`worldbible/07_characters/10_party_entry_order.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `CHR-2026-04-13-02`，从席位骨架推进到具体角色原型层
- 备注：本次只确认原型层接口、张力与进入顺序结构，不写剧情桥段、对白、任务线、恋爱线与结局线。

### [CHR-2026-04-13-04]

- 日期：2026-04-13
- 状态：已确认
- 模块：07_characters
- 决策主题：七个具体角色概念卡第一轮草案
- 变更类型：角色概念层推进与内部动力结构开启
- 背景：在七席位角色原型与结构张力已建立后，需要进一步推进到“具体角色概念卡”层，但仍然停在非传记化、非剧情化阶段。
- 决策内容：七席位已推进到具体角色概念阶段；当前阶段仍不进入正式姓名与完整传记；角色概念卡需同时成立世界接口、社会接口与历史接口；主角团内部动力结构设计已正式开启，并通过内部动力结构文件与可见度曲线文件承接；七位角色的显性程度采用“前段建立基础接口、中段扩大差异、后段抬高灰线与异质接口”的结构。
- 影响范围：07_characters、08_story、06_society、05_history
- 关联术语：角色概念卡、内部动力结构、可见度曲线、进入顺序
- 关联文件：`worldbible/07_characters/11_character_concept_cards.md`、`worldbible/07_characters/12_party_internal_dynamics.md`、`worldbible/07_characters/13_character_visibility_curve.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `CHR-2026-04-13-03`，从角色原型层推进到角色概念层
- 备注：本次只确认概念层人物轮廓与内部动力结构，不写正式姓名、剧情桥段、对白、任务线、恋爱线与结局线。

### [STO-2026-04-13-01]

- 日期：2026-04-13
- 状态：已确认
- 模块：08_story
- 决策主题：故事模块第一轮结构骨架与主线节拍启动
- 变更类型：模块启动与故事结构方法确认
- 背景：在宇宙结构、主世界格局、历史层、社会层与角色层已建立后，需要为游戏聚焦层补上 premise、核心命题、幕结构、揭示顺序与主线节拍骨架，避免直接滑入任务设计或对白草稿。
- 决策内容：`08_story` 已正式开启；当前阶段先写故事骨架，不写具体任务与对白；故事正式采用“四幕 + 渐进揭示”结构，不压成三幕；核心命题主轴锁定为“选择修复秩序的代价”，反秩序的代价作为镜像与反证保留；故事模块明确承接古裂残天的历史裂伤、现实社会结构、反抗网络以及 `07_characters` 中已建立的七席位角色骨架；同步建立四幕主线节拍、幕内转折结构与揭示节奏图。
- 影响范围：08_story、07_characters、06_society、05_history、04_main_world
- 关联术语：故事命题、幕结构、主线节拍、幕内转折、认知翻转、冲突层、揭示顺序、揭示节奏图、空间推进
- 关联文件：`worldbible/08_story/00_index.md`、`worldbible/08_story/01_story_premise_and_core_question.md`、`worldbible/08_story/02_story_structure_draft.md`、`worldbible/08_story/03_party_entry_and_reveal_order.md`、`worldbible/08_story/04_conflict_layers.md`、`worldbible/08_story/05_space_progression_draft.md`、`worldbible/08_story/06_mainline_beats.md`、`worldbible/08_story/07_act_turning_points.md`、`worldbible/08_story/08_reveal_pacing_map.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：新增故事模块方法框架，不改写既有宇宙结构、主世界、历史、社会与角色层正典
- 备注：本次只搭故事结构骨架，不写任务说明书、对白、支线列表、恋爱线与结局树。

### [STO-2026-04-14-01]

- 日期：2026-04-14
- 状态：已确认
- 模块：08_story
- 决策主题：四幕剧情分段设计阶段启动
- 变更类型：故事结构深化与分段方法确认
- 背景：在 premise、核心命题、四幕结构、冲突层、空间推进、角色揭示顺序、主线节拍与幕内转折已建立后，需要进一步把四幕拆成可比较、可扩写的剧情分段骨架。
- 决策内容：`08_story` 已进入四幕剧情分段设计阶段；当前阶段仍不写任务与对白；四幕被进一步拆解为若干功能分明的剧情段，用于回答每一段负责什么世界问题、抬高哪层冲突、推动哪些角色、形成何种认知翻转；第四幕权重进一步明确偏向“秩序选择”而非“历史真相展示”。
- 影响范围：08_story、07_characters、06_society、05_history、04_main_world
- 关联术语：剧情分段骨架、推进图、压力曲线、主线节拍、幕内转折、认知翻转
- 关联文件：`worldbible/08_story/09_act_segment_skeleton.md`、`worldbible/08_story/10_story_progression_map.md`、`worldbible/08_story/11_reveal_and_pressure_curve.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `STO-2026-04-13-01`，从幕结构骨架推进到四幕分段骨架
- 备注：本次只写剧情分段骨架，不写任务清单、对白草稿、结局树、详细分支脚本与完整章节梗概。

### [STO-2026-04-14-02]

- 日期：2026-04-14
- 状态：已确认
- 模块：08_story
- 决策主题：具体剧情节点设计阶段启动
- 变更类型：故事结构深化与节点推进方法确认
- 背景：在四幕结构、剧情分段骨架、推进图与揭示 / 压力曲线已建立后，需要进一步把每个剧情段拆成关键剧情节点，同时仍然停留在非任务化、非对白化阶段。
- 决策内容：`08_story` 已进入具体剧情节点设计阶段；当前阶段仍不写任务与对白；四幕各剧情段继续拆成关键节点，用于回答每个节点负责推进什么、抬高什么、揭示什么、把玩家推向哪里；故事推进继续遵守“先现实、后翻面、再命题”的揭示顺序；新增节点骨架、节点推进链与角色节点权重图三份文件，第四幕继续保持“秩序选择”权重大于“历史真相展示”。
- 影响范围：08_story、07_characters、06_society、05_history、04_main_world
- 关联术语：剧情节点骨架、节点推进链、节点权重图、剧情分段骨架、压力曲线
- 关联文件：`worldbible/08_story/12_story_node_skeleton.md`、`worldbible/08_story/13_act_node_progression.md`、`worldbible/08_story/14_character_node_weight_map.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `STO-2026-04-14-01`，从剧情分段骨架推进到节点骨架层
- 备注：本次只写关键剧情节点结构，不写任务清单、对白草稿、详细关卡流程、分支脚本与结局树。

### [STO-2026-04-14-03]

- 日期：2026-04-14
- 状态：已确认
- 模块：08_story
- 决策主题：章节束 / 主线任务簇骨架阶段启动
- 变更类型：故事结构深化与章节束归并确认
- 背景：在四幕结构、剧情分段骨架、34 个关键剧情节点与节点推进链已建立后，需要进一步把节点收束成更高一级的章节束 / 主线任务簇结构，以便后续进入任务层设计前保留稳定中层骨架。
- 决策内容：`08_story` 已进入章节束 / 主线任务簇骨架阶段；当前阶段仍不写详细任务与对白；34 个节点已进一步归并为章节束骨架，用于回答每个章节束负责哪一段故事推进、承接哪些节点、主导哪层冲突、抬高哪些角色、把玩家从什么认知推进到什么认知；第四幕重心继续明确为“秩序选择与代价”，并进一步落实为“代价承担者比较”高于“历史真相回收”。
- 影响范围：08_story、07_characters、06_society、05_history、04_main_world
- 关联术语：章节束、主线任务簇、章节推进链、剧情节点骨架、节点推进链
- 关联文件：`worldbible/08_story/15_chapter_cluster_skeleton.md`、`worldbible/08_story/16_cluster_progression_map.md`、`worldbible/08_story/17_cluster_character_pressure_map.md`、`worldbible/09_reference/glossary.md`
- 替代或继承关系：继承 `STO-2026-04-14-02`，从剧情节点骨架推进到章节束骨架层
- 备注：本次只写章节束结构，不写详细任务链、对白草稿、关卡脚本、分支树与结局树。

### [STO-2026-04-14-04]

- 日期：2026-04-14
- 状态：已确认
- 模块：08_story
- 决策主题：故事尺度纠偏与主线舞台收束
- 变更类型：主线尺度收口与故事结构重写
- 背景：此前 `08_story` 的若干结构文件逐步放大为“主角团接入并影响整个古裂残天大结构”的写法，已超出主角团当前能力尺度，也偏离了接引法宝与隔绝地域本应居中的主线设计。
- 决策内容：`08_story` 已完成一次故事尺度纠偏；当前主线舞台正式收束为“古裂残天内部被大战推离的隔绝地域”；主角团当前主线只对这片地域命运起决定性作用，而不直接决定整个主世界命运；接引法宝重新成为主线核心装置，同时承担接引体系核心、主角团复生根源与地域未彻底崩塌的重要支点；四幕、分段、节点与章节束已统一按这一尺度重写。
- 影响范围：08_story、07_characters、06_society、05_history、04_main_world
- 关联术语：隔绝地域、接引法宝、故事尺度纠偏、残秩序带、复生机制
- 关联文件：`worldbible/08_story/01_story_premise_and_core_question.md`、`worldbible/08_story/02_story_structure_draft.md`、`worldbible/08_story/04_conflict_layers.md`、`worldbible/08_story/05_space_progression_draft.md`、`worldbible/08_story/06_mainline_beats.md`、`worldbible/08_story/07_act_turning_points.md`、`worldbible/08_story/09_act_segment_skeleton.md`、`worldbible/08_story/10_story_progression_map.md`、`worldbible/08_story/11_reveal_and_pressure_curve.md`、`worldbible/08_story/12_story_node_skeleton.md`、`worldbible/08_story/13_act_node_progression.md`、`worldbible/08_story/14_character_node_weight_map.md`、`worldbible/08_story/15_chapter_cluster_skeleton.md`、`worldbible/08_story/16_cluster_progression_map.md`、`worldbible/08_story/17_cluster_character_pressure_map.md`
- 替代或继承关系：继承 `STO-2026-04-14-01`、`STO-2026-04-14-02`、`STO-2026-04-14-03` 的结构成果，并覆盖其中“主角团逐步影响整个古裂残天大结构”的旧尺度口径
- 备注：本次只做故事尺度收束，不进入详细任务、对白、分支树、结局树与关卡脚本。

### [AUD-2026-04-15-01]

- 日期：2026-04-15
- 状态：已确认
- 模块：01–09 / 全仓库
- 决策主题：世界观总审与仓库可扩写性判定
- 变更类型：全局审计与风险分级
- 背景：在 `01–08` 已形成完整骨架后，需要确认当前仓库是否足以支撑“庞大宇宙第一版”，并识别最高优先级的结构风险，而不是继续默认下沉到任务层。
- 决策内容：已完成一次 `01–09` 世界观总审；确认当前仓库已足够支撑“庞大宇宙第一版”的继续开发；确认 `08_story` 的隔绝地域尺度纠偏总体有效；确认当前最高优先级问题不是缺设定，而是少数关键正典文件存在乱码损坏，以及“第一部强绑定设定 / 古裂残天长期正典 / 宇宙长期正典”仍需继续显式分层。
- 影响范围：全仓库
- 关联术语：世界观总审、跨模块风险图、第一部强绑定设定、宇宙长期正典、隔绝地域、接引法宝
- 关联文件：`worldbible/09_reference/worldbuilding_audit_report.md`、`worldbible/09_reference/cross_module_risk_map.md`、`worldbible/09_reference/first_arc_vs_universe_scope.md`、`worldbible/00_project_overview/04_current_state.md`、`worldbible/09_reference/session_handoff.md`
- 替代或继承关系：继承此前各模块定稿与纠偏成果，对当前仓库做一次总体验证，不改写既有底层正典
- 备注：本次以审计、分级与协作护栏为主，不新增大型设定，不推进任务层、对白层与玩法层。

### [BRG-2026-04-15-01]

- 日期：2026-04-15
- 状态：已确认
- 模块：00_project_overview / 01_cosmology / 07_characters / 08_story / 09_reference
- 决策主题：修桥轮执行
- 变更类型：关键文件修复、项目护栏补写与跨模块接口收束
- 背景：世界观总审已确认当前仓库足以支撑“庞大宇宙第一版”，但最高优先级问题仍是关键文件损坏、项目级护栏占位、以及 `07_characters` 与 `08_story` 之间少数尺度接口未完全收束。
- 决策内容：已执行一轮“修桥轮”；`worldbible/01_cosmology/02_ascension.md`、`worldbible/01_cosmology/04_macro_cosmic_layout.md`、`worldbible/07_characters/08_party_archetype_cards.md`、`worldbible/07_characters/11_character_concept_cards.md` 已恢复可读并回扣当前口径；`worldbible/00_project_overview/01_project_brief.md`、`worldbible/00_project_overview/02_design_principles.md`、`worldbible/00_project_overview/03_scope_and_constraints.md` 已从占位补成正式护栏版；`07_characters` 与 `08_story` 的隔绝地域尺度接口已再次收束；story 层章节束最终统一口径为“34 个节点归并为 11 个章节束”。
- 影响范围：00_project_overview、01_cosmology、07_characters、08_story、09_reference
- 关联术语：修桥轮、隔绝地域、接引法宝、章节束、第一部强绑定设定、宇宙长期正典
- 关联文件：`worldbible/00_project_overview/01_project_brief.md`、`worldbible/00_project_overview/02_design_principles.md`、`worldbible/00_project_overview/03_scope_and_constraints.md`、`worldbible/01_cosmology/02_ascension.md`、`worldbible/01_cosmology/04_macro_cosmic_layout.md`、`worldbible/07_characters/05_party_seat_blueprint.md`、`worldbible/07_characters/08_party_archetype_cards.md`、`worldbible/07_characters/11_character_concept_cards.md`、`worldbible/08_story/15_chapter_cluster_skeleton.md`、`worldbible/09_reference/bridge_repair_report.md`、`worldbible/00_project_overview/04_current_state.md`、`worldbible/09_reference/session_handoff.md`
- 替代或继承关系：继承 `AUD-2026-04-15-01` 的优先级排序，优先处理关键文件、护栏与接口问题，不新增大型设定
- 备注：本次不进入任务层、对白层、玩法层；下一步应根据修桥结果再决定继续补桥还是下沉更细层开发。

## GAME-2026-04-17-01：阶段 0 游戏叙事总控计划建立

- 已新增 `worldbible/09_reference/game_narrative_master_plan.md` 与 `game_narrative_master_plan_review.md`。
- 已确认《升途：封绝之地》从小说短稿 / 故事完成稿切换为白鹿原大型 CRPG 叙事文本总工程。
- 已确认 `30` 与 `31` 继续保留为小说化参考底稿，不再作为游戏叙事工程终点。

## GAME-2026-04-17-02：阶段 1 游戏级主线架构完成

- 已重做 `25`、`26`、`27`、`28`、`29`。
- 主线结构已从 16 章小说章纲升级为 Act 1 / Act 2 / Act 3 / Epilogue。
- 已建立 48 个主线任务节点与 128 张主线场景卡。
- 已新增 `worldbible/09_reference/game_phase1_review.md`。

## GAME-2026-04-17-03：阶段 2 势力与区域状态机完成

- 已新增 `worldbible/04_main_world/14_bailuyuan_faction_state_machine.md` 与 `15_bailuyuan_region_state_machine.md`。
- 已把地方承接层、守护残余、流动层、小势力、灰线与白鹿接口写成可调用状态机。
- 已新增 `worldbible/09_reference/game_phase2_review.md`。

## GAME-2026-04-17-04：阶段 3 主线任务文本工程第一阶段完成

- 已新增 `32_main_quest_architecture.md`、`33_main_quest_text_pack_part1.md`、`34_main_quest_text_pack_part2.md`、`35_main_quest_text_pack_part3.md`。
- 已形成主线任务树、状态映射、场景叙述、关键对话、Journal 与失败反馈底稿。
- 已新增 `worldbible/09_reference/game_phase3_review.md`。

## GAME-2026-04-17-05：阶段 4 同伴文本工程第一阶段完成

- 已新增 `17_companion_arc_matrix.md`、`18_companion_dialogue_pack_part1.md`、`19_companion_dialogue_pack_part2.md`、`20_companion_banter_camp_pack.md`。
- 七席位已具备长期弧线、节点反应、营地对话、banter 与终局反馈底盘。
- 已新增 `worldbible/09_reference/game_phase4_review.md`。

## GAME-2026-04-17-06：阶段 5 支线、区域与灰线文本工程第一阶段完成

- 已新增 `36_sidequest_matrix.md`、`37_sidequest_text_pack_part1.md`、`38_sidequest_text_pack_part2.md`、`39_settlement_and_region_texts.md`。
- 已覆盖主聚落、交换带、入口残带、裂伤外缘、隐匿潜伏层与法宝相关区。
- 已新增 `worldbible/09_reference/game_phase5_review.md`。

## GAME-2026-04-17-07：阶段 6 Codex / Journal / 物品 / 系统反馈文本底盘完成

- 已新增 `40_codex_entries.md`、`41_journal_and_update_texts.md`、`42_items_relics_and_documents.md`、`43_system_feedback_texts.md`。
- 已形成可供 UI、任务与系统继续调用的基础文本底盘。
- 已新增 `worldbible/09_reference/game_phase6_review.md`。

## GAME-2026-04-17-08：阶段 7 总整合与最终验收完成

- 已新增 `worldbible/09_reference/game_narrative_final_acceptance.md`。
- 当前项目状态正式切换为：`第一款游戏叙事文本总工程`。
- 当前状态正式更新为：`已完成白鹿原大型 CRPG 叙事文本支撑库第一阶段构建`。
- 下一步正式切换为：`进入游戏叙事生产 / 任务实现 / 内容扩容阶段`。

## GAME-2026-04-17-09：游戏叙事总工程重新核定与口径修正

- 已重新核定 `game_narrative_master_plan.md` 所要求的七阶段执行情况。
- 结论：当前仅完成七阶段锚点文件、结构底盘与首批文本资产包；未完成大型 CRPG 所要求的百万级文本资产总量。
- 当前新增 / 重做的游戏叙事工程文件约为 `33,727` 个字符级别，远低于最低目标 `1,500,000` 汉字。
- 已将 `game_narrative_final_acceptance.md` 修正为“重新核定报告”，不再宣称完整完成大型 CRPG 叙事文本总工程。
- 当前状态修正为：`已完成白鹿原大型 CRPG 叙事文本工程框架与首批文本底盘，尚未完成百万级文本资产生产`。
- 下一步修正为：`继续执行游戏叙事生产 / 任务文本扩容 / 同伴与支线文本扩容`。

## GAME-2026-04-17-10：主线任务文本第一轮拆包扩容

- 已新增主线拆包 `33a_main_quest_act1_mq01_mq06_text.md`、`33b_main_quest_act1_mq07_mq12_text.md`、`34a_main_quest_act2_mq13_mq18_text.md`、`34b_main_quest_act2_mq19_mq24_text.md`、`35a_main_quest_act3_mq25_mq34_text.md`、`35b_main_quest_act3_mq35_epilogue_text.md`。
- 已更新 `33`、`34`、`35` 三个主线文本包锚点文件，加入拆包索引。
- 当前主线任务文本包合计约 `31,934` 字符。
- 本轮结论：主线文本工程完成第一轮拆包扩容，但仍远低于计划要求的 `300,000–800,000` 汉字目标，不得宣称主线文本工程完成。

## GAME-2026-04-18-01：同伴文本第一轮拆包扩容

- 已新增同伴拆包 `18a_companion_dialogue_entry_act1_pack.md`、`18b_companion_dialogue_act2_reaction_pack.md`、`19a_companion_dialogue_act3_loyalty_pack.md`、`20a_companion_banter_route_reaction_pack.md`。
- 已更新 `18`、`19`、`20` 三个同伴文本锚点文件，加入拆包索引。
- 当前同伴文本包合计约 `21,345` 字符。
- 本轮结论：同伴文本工程完成第一轮拆包扩容，但仍远低于计划要求的 `300,000–1,000,000` 汉字目标，不得宣称同伴文本工程完成。

## GAME-2026-04-20-01：游戏叙事总蓝图落库

- 已将外部输入《升途：封绝之地》大型 CRPG 叙事文本总工程计划正式落库为 `worldbible/09_reference/game_narrative_master_plan.md`。
- 已新增 `worldbible/09_reference/game_narrative_master_plan_review.md`，用于审查总蓝图规模、白鹿原范围、护栏保留、拆批必要性与后续批次计划输入价值。
- 已确认 `game_narrative_master_plan.md` 是《升途：封绝之地》大型 CRPG 叙事文本总工程的项目级总蓝图母本，不是一次性执行 prompt。
- 已确认本轮只完成总蓝图落库、review 与最小必要同步，不进入主线任务文本、同伴文本、支线文本或系统反馈文本生产。
- 当前状态更新为：`已建立大型 CRPG 叙事文本总工程母本`。
- 下一步更新为：`进入批次化重构`。

## GAME-2026-04-20-02：批次化重构启动轮

- 已新增 `worldbible/09_reference/game_narrative_batch_schedule.md`，将《升途：封绝之地》大型 CRPG 叙事文本总工程拆成 B00–B15 共 16 个 Plus 5 小时额度友好的最小可执行批次。
- 已新增 `worldbible/09_reference/game_narrative_execution_state.md`，用于 recurring automations 判断下一个 batch；初始状态下 B00–B15 均为 `PENDING`，旧首批底盘只作为输入参考，不直接标记为新批次 DONE。
- 已新增 `worldbible/09_reference/game_narrative_batch_rules.md`，明确每次自动运行只允许执行一个 batch、未通过 review 不得进入下一批、超体量必须先拆分。
- 已新增 `worldbible/09_reference/game_narrative_batch_schedule_review.md`，确认批次表已经能用于 recurring execution。
- 本轮只做批次化重构，不扩写主线任务正文、同伴文本、支线文本、Journal、Item 或 System 大包。
- 当前状态更新为：`已完成批次工程重构，准备进入 recurring execution`。
- 下一步更新为：`创建 recurring automations 并执行 Batch 00`。

## GAME-2026-04-20-03：Batch 00 资产盘点与断点建立完成

- 已执行 recurring batch run 的 B00：`现有资产盘点与执行断点建立`。
- 已新增 `worldbible/09_reference/game_narrative_asset_inventory.md`，盘点当前可用总蓝图、小说化参考底稿、旧 GAME 阶段日志与当前文件系统差异。
- 已新增 `worldbible/09_reference/game_narrative_rebuild_checkpoint.md`，建立后续 recurring run 的断点、资产使用等级、B01 入口与停止点。
- 已新增 `worldbible/09_reference/game_batch00_review.md`，确认 B00 范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮确认：`game_narrative_final_acceptance.md` 当前不存在；旧 GAME 阶段日志中提到的大多数 `25–43` 游戏文本资产文件当前也不存在，不能作为后续 batch 的现存输入。
- 本轮未拆分 batch，未执行 B01，未补写 `25–29`，未生产主线任务、同伴、支线、Codex、Journal、Item 或 System 正文。
- 当前状态更新为：`B00 已完成，B01 输入缺失风险待处理`。
- 下一步更新为：`定位 B01；若 25–29 仍缺失且 schedule 未修订，应按规则标记 B01 BLOCKED`。

## GAME-2026-04-20-04：B00R batch schedule repair 完成

- 已执行人工修正批次 `B00R：batch schedule repair`。
- 已按 `game_narrative_master_plan.md` 修正 `game_narrative_batch_schedule.md`：阶段 1 的 `25–29` 是重做 / 扩充输出链，不是 B01 的硬输入。
- B01 已改为 `重建游戏级主线架构 A`，输入改为上游故事骨架、白鹿原结构、白鹿之灵规则与角色接口文件，主输出为 `25_volume1_core_conflict.md` 与 `26_volume1_revelation_ladder.md`，review 为 `game_phase1a_review.md`。
- B02 已改为创建 / 重建 `27_volume1_plot_spine.md` 与 `28_volume1_chapter_outline.md`，review 为 `game_phase1b_review.md`。
- B03/B04 已改为创建 / 扩容 `29` 的场景卡子包与总索引，review 分别为 `game_phase1c_review.md` 与 `game_phase1d_review.md`。
- 已更新 `game_narrative_execution_state.md`，B01 仍为 `PENDING`，不应因旧 schedule 错误被长期标记为 `BLOCKED`。
- 已新增 `worldbible/09_reference/game_batch00r_review.md`，确认 B00R 通过，且本轮没有进入 B01 正文生产。
- 当前状态更新为：`已修正阶段 1 批次依赖关系`。
- 下一步更新为：`允许执行 B01：重建游戏级主线架构 A`。

## GAME-2026-04-21-01：B01 游戏级主线架构 A 完成

- 已执行 recurring batch run 的 B01：`重建游戏级主线架构 A`。
- 已新增 `worldbible/08_story/25_volume1_core_conflict.md`，建立第一款游戏主问题、五层核心冲突、四幕冲突推进、玩家状态维度、七席位功能与白鹿之灵使用边界。
- 已新增 `worldbible/08_story/26_volume1_revelation_ladder.md`，建立 `R0–R8` 揭示阶梯、Act 揭示节奏、揭示承载方式与状态差异下的揭示变体。
- 已新增 `worldbible/09_reference/game_phase1a_review.md`，确认 B01 范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未执行 B02，未创建 `27/28/29`，未生产主线任务正文、同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B01 已完成并通过 review`。
- 下一步更新为：`执行 B02：重建游戏级主线架构 B`。

## GAME-2026-04-21-02：B02 游戏级主线架构 B 完成

- 已执行 recurring batch run 的 B02：`重建游戏级主线架构 B`。
- 已新增 `worldbible/08_story/27_volume1_plot_spine.md`，建立 `48` 个主线任务节点候选，并压实每个节点的揭示层级、状态输入 / 输出、白鹿之灵接口、失败 / 代价反馈与后续去向。
- 已新增 `worldbible/08_story/28_volume1_chapter_outline.md`，建立 `17` 章章节纲要，并为 B03/B04 场景卡拆解明确章节目标、结构节点、状态变化与场景卡要求。
- 已新增 `worldbible/09_reference/game_phase1b_review.md`，确认 B02 范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未执行 B03，未创建 `29a/29b/29`，未生产主线任务正文、同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B02 已完成并通过 review`。
- 下一步更新为：`执行 B03：重建游戏级场景卡 A`。

## GAME-2026-04-21-03：B03 游戏级场景卡 A 完成

- 已执行 recurring batch run 的 B03：`重建游戏级场景卡 A`。
- 已新增 `worldbible/08_story/29a_volume1_scene_cards_act1_act2.md`，建立 `MQ01–MQ24` 范围内的 `40` 张场景卡，覆盖第 `01–07` 章、Act 1 / Act 2 的存在理由、冲突推进、增权对象、前置状态、成功 / 失败变体、状态输出与后续挂钩。
- 已在 `29a` 内补齐章节级状态联动矩阵、任务簇提取清单、营地 / 同伴最小落点、失败回流要求、可视化清单、误判空间与不可删卡清单，确保本批输出是可继续生产的工程底盘，而不是章节摘要。
- 已新增 `worldbible/09_reference/game_phase1c_review.md`，确认 B03 范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未执行 B04，未创建 `29b` 或 `29` 总索引，未进入主线任务正文、同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B03 已完成并通过 review`。
- 下一步更新为：`执行 B04：重建游戏级场景卡 B 与总索引`。

## GAME-2026-04-21-04：B04 游戏级场景卡 B 与总索引完成

- 已执行 recurring batch run 的 B04：`重建游戏级场景卡 B 与总索引`。
- 已新增 `worldbible/08_story/29b_volume1_scene_cards_act3_epilogue.md`，建立第 `08–17` 章、`MQ25–MQ48` 范围内的 `40` 张场景卡，覆盖灰线显形、异质承认、法宝翻面、绑定回返、认知崩解、代价聚焦、立场压缩、路径比较与受限未来。
- 已新增 `worldbible/08_story/29_volume1_scene_cards.md`，把 `29a` 与 `29b` 统一编成全卷场景卡总索引，明确 `17` 章、`48` 个 MQ 节点、`80` 张场景卡与六项状态曲线的调用入口。
- 已新增 `worldbible/09_reference/game_phase1d_review.md`，确认 B04 的范围、口径、因果、状态机兼容性、白鹿之灵边界、总索引完整性与文本厚度通过 review。
- 本轮未拆分 batch，未执行 B05，未创建主线任务 ID、主线正文、同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B04 已完成并通过 review`。
- 下一步更新为：`执行 B05：主线任务架构与 ID 体系`。

## GAME-2026-04-21-05：B05 主线任务架构与 ID 体系完成

- 已执行 recurring batch run 的 B05：`主线任务架构与 ID 体系`。
- 已新增 `worldbible/08_story/32_main_quest_architecture.md`，把全卷主线压成 `14` 组任务簇、`4` 幕 + `1` 个尾声层级、`MQ01–MQ48` 任务树、六项状态写回分布与 B06 直接展开边界。
- 已新增 `worldbible/08_story/main_quest_id_and_state_registry.md`，为 `MQ01–MQ48` 建立来源卡、进入条件、玩家目标、关键选择、成功写回、失败回流、Journal 锚与白鹿之灵边界。
- 已新增 `worldbible/09_reference/game_batch05_review.md`，确认 B05 的范围、输入口径修补、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 已修正 `worldbible/09_reference/game_narrative_batch_schedule.md` 中 B05 的实际输入口径，使其回扣 `29a/29b` 与 `game_phase1d_review.md`，不再被不存在的旧 review 文件名误导。
- 本轮未拆分 batch，未执行 B06，未创建 `33a` / `33b` 主线正文，也未进入同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B05 已完成并通过 review`。
- 下一步更新为：`执行 B06：主线任务文本 Act 1`。

## GAME-2026-04-22-01：B06 主线任务文本 Act 1 完成

- 已执行 recurring batch run 的 B06：`主线任务文本 Act 1`。
- 已新增 `worldbible/08_story/33a_main_quest_act1_mq01_mq06_text.md`，把 `MQ01–MQ06` 落成主线任务正文、关键对白、失败反馈、Journal 文本与补充对白库，完成高位坠落、残秩序试压、回返代价、聚落拒识、现实承压与缓冲圈边测的任务化落地。
- 已新增 `worldbible/08_story/33b_main_quest_act1_mq07_mq12_text.md`，把 `MQ07–MQ12` 落成主线任务正文、关键对白、失败反馈、Journal 文本与补充对白库，完成法宝托底证实、入口封锁、封绝定性、外界隔断确认、地方运转与凡俗承重的任务化落地。
- 已新增 `worldbible/09_reference/game_batch06_review.md`，确认 B06 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未执行 B07，未创建 `34a` / `34b` 主线正文，也未进入同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B06 已完成并通过 review`。
- 下一步更新为：`执行 B07：主线任务文本 Act 2`。

## GAME-2026-04-22-02：B07 输入冲突阻塞

- 已执行 recurring batch run 的 B07 定位与输入校验。
- 已确认 `game_narrative_batch_schedule.md` 仍将 `14_bailuyuan_faction_state_machine.md`、`15_bailuyuan_region_state_machine.md` 列为 B07 显式输入，但这两个文件当前不存在。
- 已确认 `game_narrative_rebuild_checkpoint.md` 与 `04_current_state.md` 又把 B07 正确输入口径写成 `29_volume1_scene_cards.md`、`29a_volume1_scene_cards_act1_act2.md`、`33a`、`33b` 与 `game_batch06_review.md` 体系，形成与 schedule 冲突的双口径状态。
- 已新增 `worldbible/09_reference/game_batch07_review.md`，按 batch rules 将 B07 标记为 `BLOCKED`，本轮未创建 `34a_main_quest_act2_mq13_mq18_text.md`、`34b_main_quest_act2_mq19_mq24_text.md`。
- 本轮未拆分 batch，未进入 `MQ13–MQ24` 正文，也未进入 `B08`、同伴文本、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B07 已阻塞，待修复输入清单冲突`。
- 下一步更新为：`先统一 B07 输入清单或补齐缺失文件，再重新执行 B07`。

## GAME-2026-04-22-03：B07 主线任务文本 Act 2 完成

- 已执行 recurring batch run 的 B07：`主线任务文本 Act 2`。
- 已最小修正 `worldbible/09_reference/game_narrative_batch_schedule.md` 中 B07 的错误显式输入，将不存在的 `14_bailuyuan_faction_state_machine.md`、`15_bailuyuan_region_state_machine.md` 修正为当前已存在的 `29_volume1_scene_cards.md` 与 `29a_volume1_scene_cards_act1_act2.md` 输入链。
- 已新增 `worldbible/08_story/34a_main_quest_act2_mq13_mq18_text.md`，把 `MQ13–MQ18` 落成主线任务正文、关键对白、失败反馈、Journal 文本与中段同伴插话接口，完成风险定价、处置权、通路、资格、流通失稳与飞升路径对照的任务化落地。
- 已新增 `worldbible/08_story/34b_main_quest_act2_mq19_mq24_text.md`，把 `MQ19–MQ24` 落成主线任务正文、关键对白、失败反馈、Journal 文本与第二幕收束接口，完成异质接口、地方依附、灰线风闻、托底对账、深因追问与第三幕入口锁定的任务化落地。
- 已更新 `worldbible/09_reference/game_batch07_review.md`，确认 B07 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未进入 `MQ25+`，也未进入同伴文本、支线文本、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B07 已完成并通过 review`。
- 下一步更新为：`执行 B08：主线任务文本 Act 3 / Epilogue`。

## GAME-2026-04-22-04：B08 拆分与 B08A 完成

- 已执行 recurring batch run 的 B08 定位、修补与首个子批次生产。
- 已确认原 `worldbible/09_reference/game_narrative_batch_schedule.md` 中 B08 仍沿用不存在的 `14_bailuyuan_faction_state_machine.md`、`15_bailuyuan_region_state_machine.md` 作为显式输入，且 `MQ25–MQ48` 终局段按既有批次密度保守预计超出单批 `180` 分钟上限。
- 已按 batch rules 将原 `B08` 拆为父批次 `SPLIT` + `B08A/B08B`，并修正其输入链：`B08A` 以 `29_volume1_scene_cards.md`、`29b_volume1_scene_cards_act3_epilogue.md`、`34a`、`34b` 与 `game_batch07_review.md` 为正文承接；`B08B` 以后续 `35a` 与 `game_batch08a_review.md` 为直接前置。
- 已新增 `worldbible/08_story/35a_main_quest_act3_mq25_mq34_text.md`，把 `MQ25–MQ34` 落成第三幕前中段主线正文、关键对白、失败反馈、Journal 文本与补充插话接口，完成灰线显形、异质承认、法宝承认链、接引残忆、推离成因、残余布局、复生来源与绑定代价的任务化落地。
- 已新增 `worldbible/09_reference/game_batch08a_review.md`，确认 `B08A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、拆分合法性与文本厚度通过 review。
- 本轮已拆分 batch，但只执行 `B08A`；未进入 `MQ35–MQ48`，未创建 `35b_main_quest_act3_mq35_epilogue_text.md`，也未进入同伴文本、支线文本、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B08 已拆分；B08A 已完成并通过 review`。
- 下一步更新为：`执行 B08B：主线任务文本 Act 3 B / Epilogue`。

## GAME-2026-04-22-05：B08B 主线任务文本 Act 3 B / Epilogue 完成

- 已执行 recurring batch run 的 `B08B：主线任务文本 Act 3 B / Epilogue`。
- 已新增 `worldbible/08_story/35b_main_quest_act3_mq35_epilogue_text.md`，把 `MQ35–MQ48` 落成第三幕后段、第四幕与尾声主线正文、关键对白、失败反馈、Journal 文本与补充插话接口，完成命运卷入、反派框架失效、修复代价预示、第三幕收束、法宝回收、承压面聚拢、代价镜像、团队分歧、四类路线比较、承担者比较与白鹿原受限未来落地。
- 已新增 `worldbible/09_reference/game_batch08b_review.md`，确认 `B08B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、尾声余压与文本厚度通过 review。
- 本轮未继续拆分 batch，未进入 `B09`，也未进入支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B08 已通过 B08A/B08B 全段完成并通过 review`。
- 下一步更新为：`执行 B09：同伴弧线矩阵与路线状态`。

## GAME-2026-04-22-06：B09 同伴弧线矩阵与路线状态完成

- 已执行 recurring batch run 的 `B09：同伴弧线矩阵与路线状态`。
- 已新增 `worldbible/07_characters/17_companion_arc_matrix.md`，把七席位压成卷内主命题、分幕推进、任务簇主责、四路线争论链、终局条件支持与尾声差异矩阵。
- 已新增 `worldbible/07_characters/companion_route_state_map.md`，把七席位压成 `AS1–AS5` 相位、`RS+2` 至 `RS-2` 路线状态、`CA01–CA06` 判断轴、`PT01–PT04` 队内组合态与 `TV1–TV4` 尾声版本。
- 已新增 `worldbible/09_reference/game_batch09_review.md`，确认 B09 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未拆分 batch，未进入 `B10` 同伴前中段正文，也未进入支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B09 已完成并通过 review`。
- 下一步更新为：`执行 B10：同伴文本前中段`。

## GAME-2026-04-22-07：B10 拆分与 B10A 完成

- 已执行 recurring batch run 的 `B10` 定位、拆分与首个子批次生产。
- 已确认原 `B10` 同时覆盖初识、入队、Act 1、Act 2、节点反应与营地前中段文本，按现有 `17` / `33a` / `33b` / `34a` 输入密度与双输出 review 负担，保守执行风险已逼近单批上限。
- 已按 batch rules 将原 `B10` 拆为父批次 `SPLIT` + `B10A/B10B`，并修正后续输入链：`B10A` 承接 `17`、`companion_route_state_map`、`32`、`33a`、`33b` 与 `game_batch09_review.md`；`B10B` 承接 `18a_companion_dialogue_entry_act1_pack.md` 与 `game_batch10a_review.md`。
- 已新增 `worldbible/07_characters/18a_companion_dialogue_entry_act1_pack.md`，把七席位的初识、同行确认、`MQ01–MQ12` 插话、营地前段、多组节点级反应库与低信任变体压实到 `AS1`，并显式禁止提前进入 `MQ13+`、`AS2` 明牌、路线投票与终局口径。
- 已新增 `worldbible/09_reference/game_batch10a_review.md`，确认 `B10A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、拆分合法性与文本厚度通过 review。
- 本轮已拆分 batch，但只执行 `B10A`；未创建 `18b_companion_dialogue_act2_reaction_pack.md`，未进入 `B10B`、`B11`、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B10 已拆分；B10A 已完成并通过 review`。
- 下一步更新为：`执行 B10B：同伴文本前中段 B`。

## GAME-2026-04-22-08：B10B 同伴文本前中段 B 完成

- 已执行 recurring batch run 的 `B10B：同伴文本前中段 B`。
- 已新增 `worldbible/07_characters/18b_companion_dialogue_act2_reaction_pack.md`，把七席位的 `MQ13–MQ24` 插话、第二幕节点反应、营地中段、多组复盘句库、双人错位对谈模板与差异变体压实到 `AS2`，并显式禁止提前进入 `MQ25+`、`AS3+`、忠诚线、路线明牌与 banter 后段。
- 已新增 `worldbible/09_reference/game_batch10b_review.md`，确认 `B10B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮未新增拆分动作；原 `B10` 仍沿既有 `B10A/B10B` 拆分链完成，并在本轮结束后视作父批次全段完成。
- 本轮未进入 `B11`、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B10 已通过 B10A/B10B 全段完成并通过 review`。
- 下一步更新为：`执行 B11：同伴文本后段与 Banter`。

## GAME-2026-04-22-09：B11 拆分与 B11A 完成

- 已执行 recurring batch run 的 `B11` 定位、拆分与首个子批次生产。
- 已确认原 `B11` 同时覆盖 `MQ25–MQ48` 的同伴后段正文、第四幕路线前置与 banter 后段，按当前 `17`、`companion_route_state_map`、`18b`、`35a`、`35b` 的输入密度与双输出 / 双 review 负担，保守执行风险已超出单批安全范围。
- 已按 batch rules 将原 `B11` 拆为父批次 `SPLIT` + `B11A/B11B`：
  - `B11A` 只处理 `MQ25–MQ38`、七席位从 `AS2` 到 `AS3` 的第三幕翻面文本。
  - `B11B` 再承接 `19a` 与 `game_batch11a_review.md`，处理 `MQ39+`、`AS4` 与 banter 后段。
- 已新增 `worldbible/07_characters/19a_companion_dialogue_act3_loyalty_pack.md`，把七席位的 `MQ25–MQ38` 插话、第三幕节点反应、营地后段前半、复盘触发组、低信任 / 高承担变体、双人错位对谈模板与即时复盘句库压实到 `AS3`。
- 已新增 `worldbible/09_reference/game_batch11a_review.md`，确认 `B11A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、拆分合法性与文本厚度通过 review。
- 本轮只完成 `B11A`，未进入 `B11B`、`B12`、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B11 已拆分；B11A 已完成并通过 review`。
- 下一步更新为：`执行 B11B：同伴文本后段 B / Banter`。

## GAME-2026-04-23-01：B11B 同伴文本后段 B / Banter 完成

- 已执行 recurring batch run 的 `B11B：同伴文本后段 B / Banter`。
- 已新增 `worldbible/07_characters/20a_companion_banter_route_reaction_pack.md`，把七席位的 `MQ39–MQ48` 路线条件回收、营地后段后半、banter、组合态调用模板与尾声余压压实到 `AS4 / AS5`。
- 已新增 `worldbible/09_reference/game_batch11b_review.md`，确认 `B11B` 的范围、口径、因果、状态机兼容性、白鹿之灵边界、尾声余压与文本厚度通过 review。
- 本轮未新增拆分动作；原 `B11` 仍沿既有 `B11A/B11B` 拆分链完成，并在本轮结束后视作父批次全段完成。
- 本轮未进入 `B12`、支线、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B11 已通过 B11A/B11B 全段完成并通过 review`。
- 下一步更新为：`执行 B12：支线矩阵与聚落区域文本底盘`。

## GAME-2026-04-23-02：B12 支线矩阵与聚落区域文本底盘完成

- 已执行 recurring batch run 的 `B12：支线矩阵与聚落区域文本底盘`。
- 已最小修正 `worldbible/09_reference/game_narrative_batch_schedule.md` 中 B12 的失效显式输入，将不存在的 `14_bailuyuan_faction_state_machine.md`、`15_bailuyuan_region_state_machine.md` 修正为当前已实际存在、且已被 `04_current_state.md`、`game_narrative_rebuild_checkpoint.md` 与 `game_batch11b_review.md` 明确要求读取的 `35b_main_quest_act3_mq35_epilogue_text.md`、`20a_companion_banter_route_reaction_pack.md` 链路。
- 已同步最小修正 B13 的同类失效输入，使其改由 `36_sidequest_matrix.md`、`39_settlement_and_region_texts.md`、`35b_main_quest_act3_mq35_epilogue_text.md`、`20a_companion_banter_route_reaction_pack.md` 与 `game_batch12_review.md` 承接，而不再依赖缺失的旧 `14/15` 状态机文件。
- 已新增 `worldbible/08_story/36_sidequest_matrix.md`，把支线工程压成 `12` 条主支线簇，逐条写明主线窗口、区域落点、关键选择、状态写回、灰线接口、同伴接口、结算模板、失败回流与 `B13` 展开要求。
- 已新增 `worldbible/08_story/39_settlement_and_region_texts.md`，把 `白鹿原` 压成主聚落承接面、交换带、入口残带、裂伤外缘、隐匿潜伏层与法宝相关区 `6` 个区域文本包，并补齐互动槽、状态回显、失败回流、区域转场与尾声回声规则。
- 已新增 `worldbible/09_reference/game_batch12_review.md`，确认 B12 的范围、口径、因果、状态机兼容性、白鹿之灵边界、schedule 修补合法性与文本厚度通过 review。
- 本轮未拆分 batch，未进入 `B13`、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B12 已完成并通过 review`。
- 下一步更新为：`执行 B13：支线与灰线文本包`。

## GAME-2026-04-23-03：B13 支线与灰线文本包完成

- 已执行 recurring batch run 的 `B13：支线与灰线文本包`。
- 已新增 `worldbible/08_story/37a_sidequest_text_pack_core_regions.md`，把 `SQ01–SQ06` 压成核心聚落 / 通路组六条可执行支线，逐条补齐开场叙述、关键流程、对话文本、状态写回、失败回流、支线 Journal、区域回流、同伴接口与尾声钩子。
- 已新增 `worldbible/08_story/38a_sidequest_text_pack_grayline_and_outskirts.md`，把 `SQ07–SQ12` 压成灰线 / 外缘 / 法宝组六条可执行支线，逐条补齐危区 / 回引 / 反证 / 借道 / 余压 / 受限未来缺口正文、失败回流、支线 Journal、区域回流、同伴接口与低强度白鹿边界。
- 已新增 `worldbible/09_reference/game_batch13_review.md`，确认 B13 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本密度通过 review，并记录“总量低于理想区间下沿，但未退化为摘要或目录式缩写”的风险说明。
- 本轮未拆分 batch，未进入 `B14`、Codex、Journal、Item 或 System 文本。
- 当前状态更新为：`B13 已完成并通过 review`。
- 下一步更新为：`执行 B14：Codex / Journal 文本包`。


## GAME-2026-04-23-04：B14 Codex 与 Journal 文本包完成

- 已执行 recurring batch run 的 `B14：Codex 与 Journal 文本包`。
- 已新增 `worldbible/08_story/40a_codex_entries_bailuyuan_pack.md`，把 `白鹿原` 的区域、分带、结构、行动面、历史残忆、法宝、白鹿之灵与受限未来压成可分阶段解锁的 Codex 条目包，并补齐解锁提示与调用边界。
- 已新增 `worldbible/08_story/41a_journal_and_update_texts_pack.md`，把 `CL01–CL14`、`SQ01–SQ12`、六大区域状态更新、Codex 解锁提示、阶段短提示、失败回流与尾声不整齐更新压成可调用 Journal / 更新文本包。
- 已新增 `worldbible/09_reference/game_batch14_review.md`，确认 B14 的范围、口径、因果、状态机兼容性、白鹿之灵边界与调用层完整性通过 review，并记录“总量低于理想区间下沿，但未退化为摘要或目录式缩写”的风险说明。
- 本轮未拆分 batch，未进入 `B15`、Item 或 System 文本。
- 当前状态更新为：`B14 已完成并通过 review`。
- 下一步更新为：`执行 B15：Item / System 文本与最终整合准备`。

## GAME-2026-04-23-05：B15 拆分与 B15A 物件 / 文献底盘完成

- 已执行 recurring batch run 的 `B15` 定位、拆分与首个子批次生产。
- 已确认原 `B15` 同时覆盖 `42a`、`43a` 与进入最终验收前的缺口准备，按现有输入密度、两层输出差异与 review 负担，保守执行风险已顶到单批 `180` 分钟上限。
- 已按 batch rules 将原 `B15` 拆为父批次 `SPLIT` + `B15A / B15B`：
  - `B15A` 只处理物件 / 文献底盘 `42a_items_relics_and_documents_pack.md`。
  - `B15B` 再承接 `42a` 与 `game_batch15a_review.md`，处理 `43a_system_feedback_texts_pack.md` 与 final readiness 缺口清单。
- 已新增 `worldbible/08_story/42a_items_relics_and_documents_pack.md`，把法宝 / 任务物件 / 灰线物件 / 文书底盘压成可直接被主线、支线、区域、Codex、Journal 与后续 system 调用的资产，并补齐现场调用块、失败回流矩阵、归档语气、尾声保留语气与二次查看短段落。
- 已新增 `worldbible/09_reference/game_batch15a_review.md`，确认 `B15A` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与拆分合法性通过 review，并记录“体量贴近拆分后下沿但未退化为目录”的提醒。
- 本轮只完成 `B15A`，未进入 `B15B`、最终验收轮或任何额外系统反馈文件。
- 当前状态更新为：`B15 已拆分；B15A 已完成并通过 review`。
- 下一步更新为：`执行 B15B：System 文本与最终整合准备 B`。

## GAME-2026-04-23-06：END 最终验收轮完成

- 已执行 recurring batch run 的 `END：最终验收轮`。
- 已新增 `worldbible/09_reference/game_narrative_final_acceptance.md`，基于 `game_batch15b_review.md`、`43a_system_feedback_texts_pack.md`、`42a_items_relics_and_documents_pack.md`、`40a_codex_entries_bailuyuan_pack.md`、`41a_journal_and_update_texts_pack.md`、`35b_main_quest_act3_mq35_epilogue_text.md`、`37a_sidequest_text_pack_core_regions.md`、`38a_sidequest_text_pack_grayline_and_outskirts.md`、`17_companion_arc_matrix.md`、`game_narrative_rebuild_checkpoint.md` 与 `canon_rules.md` 完成最终验收。
- 本轮已明确复核并解除进入 `END` 前的两个疑点：`session_handoff.md` 当前摘要与 `B15B` 状态一致；`43a_system_feedback_texts_pack.md` 当前字符级长度为 `16,081`，与 `game_batch15b_review.md` 一致，daily audit 中的 `12,329` 为过时口径。
- 已新增 `worldbible/09_reference/game_batch_end_review.md`，确认 `END` 的范围、口径、因果、状态机兼容性、白鹿之灵边界与文本厚度通过 review。
- 本轮重新统计当前 batch schedule 主输出总量约为 `572,037` 个字符级单位；结论是：首轮白鹿原大型 CRPG 叙事资产通过最终验收，但仍未达到 `game_narrative_master_plan.md` 要求的最低目标 `1,500,000` 汉字，因此不得宣称整个大型 CRPG 叙事文本总工程已经整体完成。
- 当前状态更新为：`B00–B15 与 END 已完成并通过 review；当前 batch schedule 已执行到终点`。
- 下一步更新为：`如需继续 recurring batch，必须先人工新增第二轮扩容 / 生产期 batch schedule；当前不存在自动可执行的下一批`。
