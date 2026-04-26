# 升途（Ascendant Path）世界观仓库

## 项目命名

- 项目中文总名：`升途`
- 英文正式名：`Ascendant Path`
- 仓库 / 目录英文名：`shengtu`
- 第一部标题：`升途：封绝之地`

说明：若本地物理路径仍保留旧工程名，应以本文档与 `worldbible/09_reference/project_rename_note.md` 中的 `shengtu` 口径为准；物理目录重命名需由人工在文件系统层执行。

## 仓库目标

本仓库是一套中式玄幻 CRPG 的宇宙级世界观设定仓库，用于维护 `升途` / `Ascendant Path` 的长期设定。

它的目标是：

- 维护一套可长期扩写、可逐步拍板、可追踪变更来源的原创中式玄幻宇宙设定。
- 让宇宙通则、主世界层、故事主世界层与游戏聚焦层有清晰分层，避免后续协作时互相越权。
- 让后续所有扩写都尽量基于仓库沉淀，而不是依赖会话记忆。

必须明确：

- 这是宇宙级设定仓库。
- 不是“古裂残天单世界设定仓库”。
- 古裂残天是当前重点展开对象，不是整个仓库的唯一对象。
- 第一部 `升途：封绝之地` 的当前舞台是古裂残天内部隔绝地域，不等于整个主世界。
- 游戏内容只是宇宙设定中的一个聚焦层，不应反向吞没整个仓库。

## 目录说明

- `worldbible/00_project_overview/`：项目总纲、设计原则、范围边界、当前状态与范围地图。
- `worldbible/01_cosmology/`：宇宙通则层，负责三层宇宙、小世界 / 主世界关系、飞升、接引、宏观格局与九主世界上层框架。
- `worldbible/02_power_system/`：宇宙通则层，负责气、规则、法、锚点等全宇宙适用的底层力量逻辑。
- `worldbible/03_worlds_and_paths/`：宇宙通则层 + 小世界道路源流层，负责八个主模板、小世界道路分化与模板化结构。
- `worldbible/04_main_world/`：主世界层设定，先写主世界共性与九主世界比较，再重点展开故事主世界 `古裂残天`。
- `worldbible/05_history/`：历史层，先写宇宙宏观格局史与九主世界关系演变，再落到故事主世界历史。
- `worldbible/06_society/`：社会层，先写主世界常见社会模型与统治形式总论，再落到故事主世界社会细化。
- `worldbible/07_characters/`：游戏聚焦层为主，负责主角团、重要角色、角色来源与模板映射。
- `worldbible/08_story/`：游戏聚焦层，负责主线、分支、阵营冲突与叙事推进。
- `worldbible/09_reference/`：长期记忆与协作规范层，负责术语表、正典规则、决策日志、交接摘要与审阅记录。
- `worldbible/10_templates/`：模板工具层，负责模块、角色、势力、地区等写作模板，不承载正典本身。

## 推荐工作流

推荐始终一次只推进一个明确问题，并按层级判断内容归属：

1. 先判断当前内容属于哪一层：宇宙通则层 / 九主世界与主世界层 / 故事主世界层 / 游戏聚焦层。
2. 先检查对应模块 `00_index.md` 与 `worldbible/00_project_overview/05_scope_map.md`，确认范围边界。
3. 只把已经拍板的内容写入正式文件，未确认内容显式标记为待定。
4. 若本轮结论影响跨模块口径，同步更新 `worldbible/09_reference/glossary.md` 与 `worldbible/09_reference/decision_log.md`。
5. 结束时同步更新 `worldbible/00_project_overview/04_current_state.md` 与 `worldbible/09_reference/session_handoff.md`。

当前不默认进入任务层。写入具体任务、对白、分支、结局或玩法前，必须先确认状态页、执行状态页与护栏文件允许下沉。

当前下一步不再是讨论能否打开 `A1`，而是基于 `81_act1_task_layer_integration_review.md` 的结论，评估 `A2 / CH04–CH06` 是否具备同等级正文与任务层闭环；在此之前，不允许把当前状态写成“全面任务层已开放”。

## 如何避免设定冲突

- 以仓库文件为唯一长期事实来源，不依赖聊天记忆。
- 以 `worldbible/09_reference/glossary.md` 统一术语口径。
- 以 `worldbible/09_reference/canon_rules.md` 判断哪些内容属于正典。
- 以 `worldbible/09_reference/decision_log.md` 记录重大拍板与口径更新。
- 扩写前先判断层级，不要让游戏聚焦层反向改写宇宙通则层。
- 不要让 `04_main_world` 退化成只服务 `古裂残天` 的单世界目录。
- 不要让 `03_worlds_and_paths` 退化成单纯为游戏职业找来源的目录。


## 当前默认入口

当前仓库默认已切换到：`Act I 任务层开放`。

后续默认先读：

1. `worldbible/09_reference/project_total_verdict.md`
2. `worldbible/00_project_overview/04_current_state.md`
3. `worldbible/09_reference/session_handoff.md`
4. `worldbible/09_reference/execution_plan_rebuild.md`
5. `worldbible/09_reference/rebuild_execution_state.md`
6. `worldbible/09_reference/rebuild_run_review.md`
7. `worldbible/09_reference/reading_order.md`

旧 `game_narrative_*`、`game_batch*`、`game_phase*`、`final_acceptance` 以及 `33a–43a`、`17–20a` 文本包现统一视为历史资产 / narrative lab round 1，不再作为当前主入口真相。



当前仓库已完成宇宙结构、力量体系、小世界模板、九主世界草案与故事主世界 `古裂残天` 的阶段性展开。

当前重点对象仍是 `古裂残天`，但后续 `04_main_world`、`05_history`、`06_society` 的推进都应先处理主世界总层，再处理故事主世界层，避免范围写窄。
