<h1 align="center">XL Hero Siege</h1>

<p align="center">
<a href="./CHANGELOG.md">更新日志</a> |
<a href="https://shimo.im/docs/kXjjhdkx6j636xjx">地图教程/文档集合(石墨文档)</a>
</p>

<p align="center">这是一张经典的魔兽RPG图, 此版本根据XHS吧主的原版3.30的基础上进行二次开发</p>
<p align="center">目前地图在功能上已基本与原版3.33同步, 同时保留旧版本一些特性以增强可玩性</p>

## 二次开发

### 工具需求

- [YDWE](http://www.ydwe.net/download.html)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python3](https://www.python.org/downloads/)
- [w3x2lni](https://github.com/LengSword/xl-hero-siege/releases/download/XL-v1.0.1/w3x2lni.7z)

### 具体步骤

1. 克隆此项目到你的本地(或下载项目的压缩包)
2. 安装YDWE(已安装可跳过)
3. 下载 `w3x2lni` 工具, 在 `tools` 目录下放置 `w3x2lni` 工具
4. 安装VSCode(已安装可跳过)
5. 使用VSCode打开此项目
6. 安装VSCode扩展 `jass.jass`
7. 已配置好各项`运行任务`
   1. 调试运行地图
      - 运行 `运行(Slk)` 或 `运行(Obj)` 任务
   2. 打包成品地图 `XL_Hero_Siege_{当前版本号}.w3x`
      - 运行 `部署` 任务
8. 编辑触发请修改 `war3map.j` 文件, 改物编数据则修改 `table` 目录下的文件

## 项目基本结构

```
XL Hero Siege
 ├── map
 │   ├── war3map.doo
 │   ├── war3map.j          // 触发脚本文件
 │   ├── war3map.mmp
 │   ├── war3map.shd
 │   ├── war3map.w3c
 │   ├── war3map.w3e
 │   ├── war3map.w3r
 │   ├── war3map.wpm
 │   ├── war3map.wts
 │   ├── war3mapskin.txt
 │   └── war3mapUnits.doo
 ├── releases               // 地图部署发布目录
 ├── resource               // 资源目录
 ├── table                  // 数据相关文件(物编/导入/地图信息等)
 └── tools                  // 工具目录
 │   └── w3x2lni            // w3x2lni 工具目录
```

## 捐赠支持

开发维护不易, 如果你喜欢我对这地图的更新, 可以给我赏几个钱.😀

赞赏:

![赞赏码](images/wechat_pay.jpg)

### 捐赠感谢名单

-  **郑**  - ￥33
