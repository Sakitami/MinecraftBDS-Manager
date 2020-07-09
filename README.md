> Minecraft BDS Manager 是一个可以便利地在本地计算机远程管理minecraft bedrock server 的程序。

---

目前，本程序仍在开发（或者说是根本没有怎么动）

/* 我知道我的代码是辣鸡 */
/* 跪求大佬优化 */

**该程序的特点**
- 可以远程管理服务器
- 可以远程上传/加载插件（基于 Element Zero）
- 拥有插件仓库，可以实现一键加载，不需要下载插件到本地
- 解决插件前置问题（相当于....解决依赖问题..???)
- 可一键开服(Linux + Wine + BDS + ElementZero)
- 可控选项更多
- 方便的控制白名单、OP
- 基于Python+Qt，全平台通用

---

前端截图：

![控制面板](https://i.loli.net/2020/05/10/AePYNXcxK2UQbJO.png)
![一键开服](https://i.loli.net/2020/05/10/v7eHV5diFbfALqy.png)
![服务器日志](https://i.loli.net/2020/05/10/M5kSuirdzDOhgXc.png)
![白名单管理](https://i.loli.net/2020/05/10/wFNUbYREWQ25gGa.png)
![白名单管理-新](https://i.loli.net/2020/07/05/9bhg7PyYdLmEcJl.png)
![插件管理](https://i.loli.net/2020/05/10/gfen4Vi78hdPbX1.png)
![插件管理-新](https://i.loli.net/2020/07/05/Bbgc6QZxrpkT7Fw.png)
![插件仓库](https://i.loli.net/2020/05/10/gBfc6qLskXoAEme.png)

---

### 开发日志
[20.05.09]
- UI设计完成

[20.05.10]

[20.05.11]
- 初步实现了SSH连接到服务器
- 可检查一次服务端的存活状态(screen方法)
- 实现了服务端一键搭建的部分功能(上传本地服务端)

[20.05.12]
- 暂停开发

[20.07.03]
- 开始继续开发
- 初步完成了一件搭建服务端功能
- ~~服务器设置功能开发中~~
- 初步实现了服务器控制功能（部分）
- 仍在开发中！

[20.07.04]
- 部分完成了白名单功能
- 完善了插件管理部分UI界面

[20.07.09]
- 完成了日志监控功能
- 添加了设置标签页
- 一键搭建服务端功能正在重构中
