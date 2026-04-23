# 《升途：封绝之地》批次化自动运行规则

## 1. 文件定位

本文档用于约束 recurring automations 如何执行 `game_narrative_batch_schedule.md`。

它是执行规则，不是正文资产文件；不得在本文档内生产主线任务、同伴对白、支线、Journal、Item 或 System 大包文本。

## 2. 自动运行硬规则

1. 每次自动运行只允许执行一个 batch。
2. 若 `game_narrative_execution_state.md` 中存在 `IN_PROGRESS` batch，则优先完成该 batch。
3. 若某 batch 预计超出 `60,000` 汉字或 `180` 分钟，应先拆分为 A/B 子批次，再执行。
4. 每个 batch 结束后必须生成对应 review 文件。
5. 每个 batch 结束后必须更新：
   - `worldbible/09_reference/decision_log.md`
   - `worldbible/00_project_overview/04_current_state.md`
   - `worldbible/09_reference/session_handoff.md`
   - `worldbible/09_reference/game_narrative_execution_state.md`
   - `worldbible/09_reference/game_narrative_rebuild_checkpoint.md`（若已建立）
6. 未通过 review 的 batch 不得进入下一批。
7. 任何时候都不得一次运行两个 batch。
8. 当前工程目标是“大型 CRPG 叙事文本总工程”，不是小说短稿。

## 3. 每次运行前检查

每次 automation 开始时必须先读取：

- `README.md`
- `AGENTS.md`
- `worldbible/00_project_overview/04_current_state.md`
- `worldbible/09_reference/session_handoff.md`
- `worldbible/09_reference/decision_log.md`
- `worldbible/09_reference/game_narrative_master_plan.md`
- `worldbible/09_reference/game_narrative_batch_schedule.md`
- `worldbible/09_reference/game_narrative_execution_state.md`
- `worldbible/09_reference/game_narrative_batch_rules.md`
- 当前 batch 的依赖 review 文件

若发现输入文件缺失，应将当前 batch 标记为 `BLOCKED`，在 notes 中说明缺失项，不得猜测补写。

## 4. Batch 选择规则

自动运行按以下顺序选择 batch：

1. 若存在 `IN_PROGRESS`，继续该 batch。
2. 若不存在 `IN_PROGRESS`，选择依赖均为 `DONE` 的最早 `PENDING` batch。
3. 若最早 `PENDING` batch 预计超体量，先把该 batch 状态改为 `SPLIT`，建立 A/B 子批次说明，再执行 A。
4. 若存在 `BLOCKED`，不得跳过执行后续依赖批次；必须先解除阻塞或等待人工处理。

## 5. Batch 输出规则

每个 batch 只能写入 schedule 指定的主输出文件与 review 文件。

允许同步更新的长期记忆文件：

- `decision_log.md`
- `04_current_state.md`
- `session_handoff.md`
- `game_narrative_execution_state.md`
- `game_narrative_rebuild_checkpoint.md`（若已建立）

不得在未列入主输出的正文资产文件中顺手扩写内容。若发现必须修改额外文件，应在 review 中提出下一批或人工确认项。

## 6. Review 必检项

每个 batch review 至少检查：

- 是否仍限定在 `白鹿原` 第一款游戏尺度。
- 是否改写了宇宙通则、九主世界总层或 `古裂残天` 长期正典。
- 白鹿之灵是否越权为万能解释器、万能支援、万能真相机或无代价复生源。
- 是否符合本 batch 输入 / 输出限制。
- 是否达到本 batch 的最低文本量目标。
- 是否存在状态差异、失败反馈、代价承担或可调用接口。
- 是否需要拆分、返工或阻塞下一批。

## 7. 失败与阻塞处理

如果 batch 未通过 review：

- 将该 batch 状态改为 `BLOCKED`。
- 在 `Last Run Summary` 写明失败原因。
- 在 `Next Action` 写明需要修复的最小动作。
- 不得进入下一 batch。

如果 batch 部分完成但未达切换门槛：

- 将该 batch 状态保持为 `IN_PROGRESS`。
- 下次 automation 优先继续该 batch。

如果 batch 超出体量：

- 将该 batch 状态改为 `SPLIT`。
- 在 notes 中写明 A/B 子批次边界。
- 只执行 A 子批次，B 子批次等待 A review 后继续。

## 8. 禁止事项

- 不得一次执行两个 batch。
- 不得跳过未通过 review 的 batch。
- 不得用任务需求反向定义宇宙底层规则。
- 不得把白鹿原写成整个 `古裂残天`。
- 不得把总蓝图或批次表当成正文资产。
- 不得把旧首批底盘误判为百万级 CRPG 文本工程完成。
- 不得在未达到 `1,500,000` 汉字前宣称大型 CRPG 叙事文本总工程完成。
