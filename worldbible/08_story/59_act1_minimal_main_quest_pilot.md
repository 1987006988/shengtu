# Act I 最小主线试点文件

## 1. 文件定位

本文件只服务 `Act I / CH01–CH02` 的最小主线任务化试点。  
它不是全面 `MQ` 包，也不是支线任务入口。

## 2. 上游继承边界

本文件只允许继承以下已落库文件：

- `worldbible/04_main_world/15_bailuyuan_region_bible.md`
- `worldbible/04_main_world/16_book1_binding_boundary.md`
- `worldbible/07_characters/21_party_story_function_bible.md`
- `worldbible/07_characters/22_character_progression_master.md`
- `worldbible/08_story/54_book1_chapter_blueprint.md`
- `worldbible/08_story/55_book1_scene_blueprint.md`
- `worldbible/08_story/56_book1_reveal_foreshadow_table.md`
- `worldbible/08_story/57_book1_character_progression_table.md`
- `worldbible/08_story/58_book1_world_state_table.md`

本文件当前明确不得承载：

- `CH03+` 的任务节点
- 白鹿之灵的完整解释权
- 古战前史或主世界全貌
- 远端主世界的完整制度说明
- 终局未来、救世主预演或无代价回返解释

## 3. 最小主线任务链

| quest_id | chapter_window | 任务目标 | 完成条件 | allowed_reveals | forbidden_reveals |
| --- | --- | --- | --- | --- | --- |
| `MQ-ACT1-01A《裂风带活下来》` | `CH01-S01–S03` | 让玩家先活下来，并理解外缘会主动追人 | 完成坠落求生、跟随桑沉岫撤离、见证第一次异常回返 | 白鹿原外缘仍有人活着；主角存在异常回返；桑沉岫承担第一层身体代价 | 不得解释回返原因、白鹿高位性质或主角终局身份 |
| `MQ-ACT1-01B《被押送的人》` | `CH01-S04` | 把主角从幸存者压成待审风险人 | 完成巡守队押送、触发回引印被识别、进入鹿门集 | 白鹿原对主角的第一反应是风险管理而不是欢迎 | 不得让任何人把主角当救世主或既定核心 |
| `MQ-ACT1-02A《鹿门的价钱》` | `CH02-S01–S03` | 让玩家看见承接位、基础补给、工分和承接排序怎样决定今天谁先活 | 完成照护棚协助、账本分账、劳作换取临时停留 | 鹿门集靠延后名单与配额苟活；柳照禾是地方现实锚点 | 不得把共保会写成纯温情组织或把配额压力写空 |
| `MQ-ACT1-02B《移交前夜》` | `CH02-S04` | 把主角推进守衡司结构审查线 | 完成议棚对峙、确认本地陪同移交、锁定进入 `CH03` 的结构审查前状态 | 主角是结构异常变量；柳照禾争取到最小地方看护权 | 不得提前讲守衡司全貌、白鹿之灵解释权或后段未来比较 |

## 4. 状态机锁定

| state_id | 触发条件 | 作用 |
| --- | --- | --- |
| `PILOT-CH01-START` | 主角坠入白鹿原外缘 | 锁定开场不是新手村，而是风险外缘 |
| `PILOT-CH01-RETURN-SEEN` | 第一次异常回返被目击 | 锁定主角被视为结构风险变量 |
| `PILOT-CH01-ESCORTED` | 巡守队完成押送进入鹿门集 | 锁定 `CH02` 开场的登记与分账压力 |
| `PILOT-CH02-REGISTERED` | 照护棚与账本室段落完成 | 锁定鹿门集的人命账、配额账与停留条件 |
| `PILOT-CH02-HANDOFF-EVE` | 议棚对峙后进入移交前夜 | 锁定进入 `CH03` 前的结构审查前状态 |

## 5. 当前硬规则

1. 每个任务目标都必须先服务“活下来、被收下、被登记、被分账、被移交”的现实动作。
2. 任意说明只要不改变玩家当前行动判断，就不应进入本文件。
3. 本文件的终点不是“理解世界”，而是“被白鹿原纳入风险登记并被迫进入结构审查线”。
4. 本文件只验证四个连续前段主线节点能否成立，不开启大规模任务写作。
