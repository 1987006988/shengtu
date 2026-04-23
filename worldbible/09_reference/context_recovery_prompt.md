# 上下文恢复文本（给 ChatGPT / Codex）

你现在接手的是《升途 / Ascendant Path》项目的重构后阶段。

## 一、项目真实状态

这不是一个“已完成第一轮大型 CRPG 文本工程、只待扩容”的项目。  
它是一个：

- 宇宙与主世界上层框架可用；
- 古裂残天方向正确；
- 白鹿原尺度正确；
- 但白鹿原承载层仍不足；
- 角色和故事层曾过早下沉到任务 / 文本包；
- 旧 `current_state` / `session_handoff` / `final acceptance` 口径已被废弃；

的**施工母本重建项目**。

## 二、当前唯一正确阶段

当前阶段是：

> **主世界承载层与第一部施工蓝图重建阶段**

这意味着：

- 不默认进入任务层；
- 不默认继续旧 batch；
- 不把旧文本包当成当前主线真相；
- 先把古裂残天、白鹿原、七席位与第一部蓝图做实。

## 三、当前必须视为历史资产的旧文件

以下文件类型一律视为历史资产，不得作为当前主入口：

- `08_story/30–43a`
- `07_characters/17–20a`
- `09_reference/game_narrative_*`
- `09_reference/game_batch*`
- `09_reference/game_phase*`
- 旧 `final acceptance`、旧 `END`、旧 `execution_state`

它们可以被回收其中有价值的局部桥段、术语、句群或结构，  
但不能决定当前阶段口径。

## 四、当前主控文件

以后默认先读：

1. `worldbible/09_reference/project_total_verdict.md`
2. `worldbible/00_project_overview/04_current_state.md`
3. `worldbible/09_reference/session_handoff.md`
4. `worldbible/09_reference/reading_order.md`
5. `worldbible/09_reference/reconstruction_route_map.md`
6. `worldbible/09_reference/execution_plan_rebuild.md`
7. `worldbible/04_main_world/14_gulie_cantian_rebuild_bible.md`
8. `worldbible/04_main_world/15_bailuyuan_region_bible.md`
9. `worldbible/07_characters/21_party_story_function_bible.md`
10. `worldbible/08_story/50–58`

## 五、第一部的正确控制口径

第一部 / 第一款游戏《升途：封绝之地》只做：

- 白鹿原这一伤区的承载；
- 七席位第一阶段闭环；
- 主角与白鹿原的绑定；
- 白鹿原有限重开的受限未来；
- 古裂残天更广阔伤区的下一步入口。

第一部绝不做：

- 解决整个古裂残天；
- 解释整个九主世界；
- 解释飞升与高层宇宙全部真相；
- 把主角写成古裂残天级救世主。

## 六、后续工作默认怎么做

你后续默认只做这四件事：

1. 补上游承载层；
2. 锁死白鹿原边界；
3. 细化第一部蓝图；
4. 为将来的任务化试点留挂点。

不要再问“下一批 batch 是什么”，  
要先问“这一层是否已经足够承重，足以让下游不再靠猜”。

## 七、对你自己的约束

- 不制造完成错觉；
- 不把旧 acceptance 当作真相；
- 不让下游反写上游；
- 不用大批量文本掩盖结构空洞；
- 不跳过白鹿原地区圣经；
- 不跳过分章 / 分场蓝图闭环。

## 八、一句话提醒

> 这个项目现在最需要的不是更多文本，而是更真实、更能承重的正式母本。
