# A2 主线状态触发表

## 1. 文件定位

本表只服务 `A2 / CH04–CH06`。  
它只锁 `A2` 状态增量，不顺手越入 `CH07+`。

## 2. 状态总表

| `state_id` | 触发窗口 | 状态说明 | 下一状态 |
| --- | --- | --- | --- |
| `A2-CH04-ROAD-BARGAIN` | `CH04-S01` | 断引栈道前哨谈判完成，道路政治成立。 | `A2-CH04-NODE-STABILIZED` |
| `A2-CH04-NODE-STABILIZED` | `CH04-S02` | 旧接引节点被临时补稳，主角反冲加重。 | `A2-CH04-SELLROAD-LOCK` |
| `A2-CH04-SELLROAD-LOCK` | `CH04-S03–S04` | “有人卖路 / 空名册可能被人动过”成立为内部问题。 | `A2-CH05-LEVY-OPEN` |
| `A2-CH05-LEVY-OPEN` | `CH05-S01` | 守衡司与地方的人命账 / 制度账公开对撞。 | `A2-CH05-WINDCELL-LOCK` |
| `A2-CH05-WINDCELL-LOCK` | `CH05-S02–S04` | 风窖台现场与夜间决断窗口成立。 | `A2-CH06-CHOICE-SIGNED` |
| `A2-CH06-CHOICE-SIGNED` | `CH06-S01–S03` | 主角完成第一次地区级代价排序。 | `A2-CH06-GRAYSEAL-FOUND` |
| `A2-CH06-GRAYSEAL-FOUND` | `CH06-S04` | 灰缄封记出现，白鹿原内部裂口获得实物证据。 | `V1-A2-CLOSED` |
| `V1-A2-CLOSED` | `95 PASS` | `A2` 主线任务层通过，可评估 `SQ-SCOPE-02`。 | `SQ-A2-01-PILOT` |

## 3. 调用规则

1. `94` 只服务 `CH04–CH06`，不提前创建 `CH07` 的碑林、灰市或历史状态。
2. 任一状态都必须能回锚 `83–85` 的具体场景与 `91` 的具体任务节点。
3. `V1-A2-CLOSED` 只表示 `A2` 主线闭环完成，不表示 `V1` 或 `Book1` 已进入后续生产口径。

## 4. 一句话口径

> `94` 只把 `A2` 从“路权成立”推进到“灰缄封记入主轴”，不顺手越入后段历史线。
