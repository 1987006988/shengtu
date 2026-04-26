# A6 主线状态触发表

| `state_id` | 触发窗口 | 状态说明 | 下一状态 |
| --- | --- | --- | --- |
| `A6-CH16-FALSESAFE-BROKEN` | `CH16-S01–S03` | 伪安全路线被证伪，旧平衡无可回返。 | `A6-CH16-STARTLOCK` |
| `A6-CH16-STARTLOCK` | `CH16-S04` | 七席位进入并列承压与抢启动权状态。 | `A6-CH17-FUTURE-SIGNED` |
| `A6-CH17-FUTURE-SIGNED` | `CH17-S01–S04` | 受限未来被共同签下。 | `A6-CH18-FUTURE-LIVED` |
| `A6-CH18-FUTURE-LIVED` | `CH18-S01–S04` | 白鹿原受限未来、过渡治理与外联偏路成立。 | `V3-CLOSED` |
