# A5 主线状态触发表

| `state_id` | 触发窗口 | 状态说明 | 下一状态 |
| --- | --- | --- | --- |
| `A5-CH13-INNERGATE-OPEN` | `CH13-S01–S02` | 内环门槛与代价回声成立。 | `A5-CH13-ANCHOR-CANDIDATE` |
| `A5-CH13-ANCHOR-CANDIDATE` | `CH13-S03–S04` | 比较盘边界与替代锚点候选成立。 | `A5-CH14-OLDORDER-BROKEN` |
| `A5-CH14-OLDORDER-BROKEN` | `CH14-S01–S02` | 旧令失去自动正确性。 | `A5-CH14-COST-MEASURED` |
| `A5-CH14-COST-MEASURED` | `CH14-S03–S04` | 主角回返代价被测定成立。 | `A5-CH15-OPTIONS-ONDESK` |
| `A5-CH15-OPTIONS-ONDESK` | `CH15-S01–S04` | 三方案具备比较重量，拖延失效。 | `V3-A5-CLOSED` |
