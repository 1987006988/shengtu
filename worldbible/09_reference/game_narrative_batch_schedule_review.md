# 《升途：封绝之地》批次化重构启动轮 Review

## 1. 文件定位

本文档审查 `game_narrative_batch_schedule.md`、`game_narrative_execution_state.md` 与 `game_narrative_batch_rules.md` 是否足以支撑后续 recurring automations 连续执行。

本 review 不生产主线、支线、同伴、Journal、Item 或 System 大包正文。

## 2. 总体结论

- 判定：通过。
- 已将总蓝图拆成 B00–B15 共 `16` 个最小可执行批次。
- 每个批次均限定输入文件不超过 `10` 个，主输出文件不超过 `2` 个，review 文件 `1` 个。
- 每个批次均写明预计文本量、推荐执行时长、切换门槛、下一批与超体量 A/B 拆分规则。
- 批次表已经能作为 recurring automations 的执行母表。

## 3. 检查项

### 3.1 是否已经把总蓝图真正重构成小批次工程

判定：通过。

依据：

- 总蓝图七阶段被拆解为 B00–B15。
- 阶段 1 被拆为 B01–B02。
- 状态机被拆为 B03–B04。
- 主线任务工程被拆为 B05–B08。
- 同伴工程被拆为 B09–B11。
- 支线与区域工程被拆为 B12–B13。
- Codex / Journal / Item / System 被拆为 B14–B15。

### 3.2 是否每批都足够小，适合 Plus 环境

判定：基本通过。

依据：

- 每批目标文本量为 `20,000–60,000` 汉字。
- 推荐执行时长为 `60–120` 分钟，多数保守上限为 `180` 分钟。
- 对接近上限的批次已预设 A/B 拆分。

需要注意：

- B06、B07、B08、B10、B11、B13、B14、B15 是最可能超体量的批次，应优先按 A/B 子批次运行。

### 3.3 是否没有偷工减料把多个大阶段塞回单批

判定：通过。

依据：

- 没有把主线全阶段塞进一个 batch。
- 没有把同伴全阶段塞进一个 batch。
- 没有把支线、区域、Codex、Journal、Item、System 合并成一个尾批。
- B00 专门用于盘点与断点建立，避免直接跳入正文生产。

### 3.4 是否仍保持白鹿原尺度与现有护栏

判定：通过。

已保留护栏：

- `白鹿原` 是第一款游戏主舞台，不等于整个 `古裂残天`。
- 不改写宇宙通则。
- 不改写九主世界总层。
- 不改写 `古裂残天` 长期正典。
- 白鹿之灵只能作为接口、残忆、触发器、示警与边界反馈。
- 现有小说稿只作为上游参考，不再作为项目终点。

### 3.5 是否已经能直接用于 recurring automations

判定：通过。

依据：

- 已建立 `game_narrative_execution_state.md`，可用于判断下一个 batch。
- 已建立 `game_narrative_batch_rules.md`，约束自动运行每次只执行一个 batch。
- 已指定第一次 recurring execution 应执行 B00。
- 已明确若存在 `IN_PROGRESS`，优先继续；若超体量，先拆分；若 review 未通过，不得进入下一批。

## 4. 发现的问题

### 4.1 旧首批底盘不可直接视为新批次完成

说明：仓库中已有旧主线、同伴、支线等首批底盘与旧 review，但本轮建立的是新的 recurring 执行体系。旧资产可作为 B00 盘点输入，不应让 B01–B15 初始状态直接标记为 DONE。

处理：`game_narrative_execution_state.md` 已将全部批次设为 `PENDING`，并在 notes 中说明旧资产只作输入参考。

### 4.2 多个正文批次仍接近 Plus 上限

说明：主线、同伴、支线、Codex / Journal / Item / System 天然大体量，单批可能触碰 `60,000` 汉字或 `180` 分钟上限。

处理：schedule 已给出 A/B 拆分规则，rules 要求超体量先拆分再执行。

### 4.3 B00 是必要缓冲批

说明：如果直接跑 B01，automation 容易误用旧资产或漏掉缺口盘点。

处理：状态表已指定最适合先跑 B00。

## 5. Review 自检

- 是否没有越界生成大体量正文：是。本轮只生成批次表、状态表、规则与 review。
- 是否已完成批次化重构：是。总蓝图已拆成 16 个可执行 batch。
- 是否已为 recurring execution 做好准备：是。已有 schedule、execution state、rules 与 schedule review。
