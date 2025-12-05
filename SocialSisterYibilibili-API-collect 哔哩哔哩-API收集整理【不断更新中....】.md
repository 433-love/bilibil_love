---
title: "SocialSisterYi/bilibili-API-collect: 哔哩哔哩-API收集整理【不断更新中....】"
source: "https://github.com/SocialSisterYi/bilibili-API-collect"
author:
  - "[[2513502304]]"
  - "[[推荐作者]]"
published:
created: 2025-12-05
description: "哔哩哔哩-API收集整理【不断更新中....】. Contribute to SocialSisterYi/bilibili-API-collect development by creating an account on GitHub."
tags:
  - "clippings"
---
**[bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect)** Public

哔哩哔哩-API收集整理【不断更新中....】

[View license](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/LICENSE)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/SocialSisterYi/bilibili-API-collect?resume=1)

[![](https://github.com/SocialSisterYi/bilibili-API-collect/raw/master/assets/img/logo.png)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/assets/img/logo.png)

[![Trendshift](https://camo.githubusercontent.com/4d25dd88c3ed54fd74192e63a11efed4fe626318b78a6c1dde73174df167fce6/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f33323138)](https://trendshift.io/repositories/3218)

### 不断更新中....

本项目旨在对 B 站 WEB、APP、TV 等客户端中，散落在世界各地的野生 API 进行收集整理，研究使用方法并对其进行说明，运用了黑箱法、控制变量法、代码逆向分析、拆包及反编译法、网络抓包法等研究办法

本文档探讨的对象是主站业务接口， [官方开放平台](https://openhome.bilibili.com/doc) 和 [直播开放平台](https://open-live.bilibili.com/document/) 均不属于本项目范畴，请移步

B站 API 采用 C/S 结构，大多数接口为 REST API 和 gRPC，少部分接口为 WebSocket；REST API 接口请求数据大多为 url query 表单或 JSON，返回数据大多为 JSON 或 Protobuf，强制使用 https 协议

📖阅读地址： [Github Pages](https://socialsisteryi.github.io/bilibili-API-collect/)

小小的 Demo： ~~av583785685~~ [视频失效原因](https://shakaianee.top/archives/56/) ([Youtube 备链](https://www.youtube.com/watch?v=nfF91Z6fqGk))

::: warning 声明

1. 本项目遵守 CC-BY-NC 4.0 协议，禁止一切商业使用，如需转载请注明作者 ID
2. **请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！**
3. 利用本项目提供的接口、文档等造成不良影响及后果与本人无关
4. 由于本项目的特殊性，可能随时停止开发或删档
5. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容
6. **上传任何信息时请注意脱敏，删去账户密码、敏感 cookies 等可能泄漏个人信息的数据（例如 `SESSDATA` 、 `bili_jct` 之类的 cookies）**

:::

## 🌱参与贡献

欢迎各位 dalao 对本项目做出贡献，也希望每个使用者都能提出宝贵的意见

目前本项目存在的问题包括但不限于：

1. 文档二级目录尚未完成
2. 部分文档较旧，修改与更新没有跟进
3. 目前文档使用 Markdown 语法编写，不易生成编程语言的 SDK，详见 [#604](https://github.com/SocialSisterYi/bilibili-API-collect/issues/604)

更多信息请浏览 [贡献指南](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/CONTRIBUTING.md)

## 🍴目录

计划整理分类 & 目录：(文档已完结请选中 checkbox)

- [接口签名与验证](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign)
	- [APP API 签名](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign/APP.md) （ `appkey` 与 `sign` ）
	- [已知的 APPKey](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign/APPKey.md)
	- [Wbi 签名](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign/wbi.md) （ `wts` 与 `w_rid` ）
	- [bili\_ticket](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign/bili_ticket.md)
	- [v\_voucher 验证](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/sign/v_voucher.md)
- [杂项](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc)
	- [获取当前时间戳](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/time_stamp.md)
	- [公共错误码](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/errcode.md)
	- [图片格式化](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/picture.md)
	- [表达式渲染](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/mathjax.md)
	- [bvid 说明](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/bvid_desc.md)
	- [设备唯一标识 BUVID](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/device_identity.md)
	- [获取 buvid3 / buvid4 / b\_nut](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/buvid3_4.md)
	- [b23.tv 短链](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/misc/b23tv.md)
- [gRPC API 接口定义](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/grpc_api)
- [登录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login)
	- [登录操作 (人机认证)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_action)
		- [短信登录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_action/SMS.md)
		- [密码登录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_action/password.md)
		- [二维码登录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_action/QR.md)
		- SNS 登录 (QQ & 微信 & 微博)
	- [登录基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_info.md)
	- [个人中心](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/member_center.md)
	- [注销登录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/exit.md)
	- [登录记录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_notice.md)
	- [Web 端 Cookie 刷新](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/cookie_refresh.md)
- [消息中心](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message)
	- [通知类消息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/msg.md)
	- [私信](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/private_msg.md)
		- [私信消息类型、内容说明](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/private_msg_content.md)
	- [设置](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/message/settings.md)
- [用户](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/info.md)
	- [状态数](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/status_number.md)
	- [关系](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/relation.md)
	- [个人空间](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/space.md)
	- ~~[检查昵称是否可注册](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/check_nickname.md)~~ (已失效)
	- [用户注册](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/register.md)
	- [用户认证类型一览](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/official_role.md)
	- [加入老粉计划](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/contract.md)
	- [所有粉丝勋章](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/medals.md)
	- [批量查询](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/batch.md)
- [大会员](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/vip)
	- [大会员基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/vip/info.md)
	- [大会员中心](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/vip/center.md)
	- [大会员签到](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/vip/clockin.md)
	- [大会员操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/vip/action.md)
- [视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video)
	- [视频分区一览 (分区代码)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/video_zone.md)
	- [视频分区一览 (分区代码) (v2)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/video_zone_v2.md)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/info.md)
	- ~~[状态数](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/status_number.md)~~ (已失效)
	- [快照](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/snapshot.md)
	- [点赞 & 投币 & 收藏 & 分享](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/action.md)
	- [TAG](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/tags.md)
	- [视频推荐](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/recommend.md)
	- [播放 & 下载地址 (视频流)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/videostream_url.md)
	- [互动视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/interact_video.md)
	- [高能进度条](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/pbp.md)
	- [信息上报 (心跳及记录历史)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/report.md)
	- [视频属性数据](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/attribute_data.md)
	- [视频在线人数](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/online.md)
	- [视频 AI 摘要](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/summary.md)
	- [稿件投诉](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/appeal.md)
	- [视频合集](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/collection.md)
	- [播放器](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video/player.md)
- [剧集 (番剧、影视)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi/info.md)
	- [播放 & 下载地址（视频流）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi/videostream_url.md)
	- [时间轴](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi/timeline.md)
	- [索引](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi/season_index.md)
	- [追番相关](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/bangumi/follow.md)
	- 状态数
	- 操作
- [视频弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku)
	- [protobuf 实时弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/danmaku_proto.md)
	- [protobuf 弹幕元数据（BAS 弹幕 / 互动弹幕）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/danmaku_view_proto.md)
	- [xml 实时弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/danmaku_xml.md)
	- [历史弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/history.md)
	- [快照](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/snapshot.md)
	- [弹幕操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/action.md)
	- 高级弹幕
	- 屏蔽管理
	- [智能防挡弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/webmask.md)
	- [弹幕个人配置修改](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/config.md)
	- [名词解释](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/buzzword.md)
	- [点赞查询](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/danmaku/thumbup.md)
- [视频笔记](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/note)
	- [笔记列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/note/list.md)
	- [笔记详细信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/note/info.md)
	- [笔记操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/note/action.md)
- [图文](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/opus)
	- [图文详细](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/opus/detail.md)
	- [空间图文](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/opus/space.md)
	- [功能模块](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/opus/features.md)
	- [富文本节点](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/opus/rich_text_nodes.md)
- [专栏](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article)
	- [专栏内容](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article/view.md)
	- 
	- [卡片信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article/card.md)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article/info.md)
	- [点赞 & 投币 & 收藏 & 分享](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article/action.md)
	- [文集基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/article/articles.md)
- [动态](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic)
	- [获取动态列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/all.md)
	- [用户空间动态](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/space.md)
	- [动态基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/basicInfo.md)
	- [动态卡片信息字段](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/card_info.md)
	- [获取动态详情](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/detail.md)
	- [动态类型对照](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/dynamic_enum.md)
	- [动态信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/content.md)
	- [发送 & 转载动态](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/publish.md)
	- [根据关键字搜索用户（at 别人时的填充列表）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/atlist.md)
	- [操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/action.md)
	- [话题](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/topic.md)
	- [动态内容](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/get_dynamic_detail.md)
	- [导航栏动态](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/nav.md)
	- [首页公告栏](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/banner.md)
- [创作中心](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter)
	- [投稿](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/upload.md)
	- [统计与数据](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/statistics&data.md)
	- 列表查询相关
	- [电磁力数据](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/railgun.md)
	- [合集管理](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/season.md)
	- [视频相关杂项](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/videos.md)
	- [图文操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/creativecenter/opus.md)
- [音频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio)
	- [歌曲基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/info.md)
	- [歌单 & 音频收藏夹详细信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/music_list.md)
	- [状态数](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/status_number.md)
	- [投币 & 收藏](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/action.md)
	- [播放 & 下载地址（音频流）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/musicstream_url.md)
	- [音频榜单](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/audio/rank.md)
- [排行榜 & 最新视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video_ranking)
	- [排行榜](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video_ranking/ranking.md)
	- [热门视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video_ranking/popular.md)
	- [最新视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video_ranking/dynamic.md)
	- [入站必刷视频](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/video_ranking/precious_videos.md)
- [搜索](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/search)
	- [搜索请求](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/search/search_request.md)
	- [搜索结果](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/search/search_response.md)
	- [默认搜索 & 热搜](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/search/hot.md)
	- [搜索建议](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/search/suggest.md)
- [小黑屋](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom)
	- 基本信息
	- [封禁公示](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom/banlist.md)
	- [风纪委员及众裁案件相关](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom/jury)
		- [风纪委员基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom/jury/base_info.md)
		- [众裁案件基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom/jury/judgement_info.md)
		- [裁决操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/blackroom/jury/action.md)
- [评论区](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/comment)
	- [评论区明细](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/comment/list.md)
	- [操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/comment/action.md)
- [表情](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/emoji)
	- [表情及表情包信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/emoji/list.md)
	- [操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/emoji/action.md)
- [实时广播（通讯协议）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/broadcast)
	- [视频内广播](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/broadcast/video_room.md)
- [充电](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric)
	- [包月充电](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric/monthly.md)
	- 自定义充电
		- [B 币方式充电](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric/Bcoin.md)
		- [微信 & 支付宝方式充电](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric/WeChat&Alipay.md)
		- [充电留言](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric/charge_msg.md)
	- [充电列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/electric/charge_list.md)
- ~~[相簿](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/album)~~ (已下线)
	- ~~[基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/album/info.md)~~
	- ~~[相簿列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/album/list.md)~~
	- 
	- ~~[活动列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/album/activity_list.md)~~
	- ~~[操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/album/action.md)~~
	- ~~投稿~~
- [历史记录 & 稍后再看](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/historytoview)
	- [历史记录](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/historytoview/history.md)
	- [稍后再看](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/historytoview/toview.md)
- [收藏夹](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/fav)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/fav/info.md)
	- [收藏夹内容](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/fav/list.md)
	- [收藏夹操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/fav/action.md)
- [课程](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/cheese)
	- [课程基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/cheese/info.md)
	- 已购课程
	- 分区推荐列表
	- 操作
	- [播放 & 下载地址（视频流）](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/cheese/videostream_url.md)
- [直播](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live)
	- [直播间基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/info.md)
	- [直播推荐](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/recommend.md)
	- [直播分区](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_area.md)
	- [直播间管理](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/manage.md)
	- 直播间操作
	- [直播视频流](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_stream.md)
	- [直播信息流](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/message_stream.md)
	- [直播红包](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/redpocket.md)
	- [直播间表情包](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/emoticons.md)
	- [直播间用户实用 API](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/user.md)
	- [直播间禁言相关](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/silent_user_manage.md)
	- [关注UP直播情况](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/follow_up_live.md)
	- [直播心跳上报](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/report.md)
	- [直播间弹幕](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/danmaku.md)
	- [直播流水](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_bill.md)
	- [礼物相关](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/gift.md)
	- [大航海/粉丝团](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/guard.md)
	- [直播回放](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_replay.md)
	- [直播数据](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_data.md)
	- [直播投票](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/live/live_vote.md)
- [活动](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/activity)
	- [活动列表](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/activity/list.md)
	- [活动主题信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/activity/info.md)
- [转正答题](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/newbie_exam)
	- [查询信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/newbie_exam/info.md)
	- [拉取题目](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/newbie_exam/fetch.md)
	- [操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/newbie_exam/action.md)
- [青少年守护](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/teenager)
	- [青少年模式](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/teenager/teenager_mode.md)
	- 亲子平台
	- 课堂模式
- [B 币钱包](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/wallet)
	- [基本信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/wallet/info.md)
	- B 币充值
	- 贝壳相关
- [哔哩哔哩漫画](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga)
	- 用户信息
	- [签到](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/ClockIn.md)
	- [积分商城](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/point_shop.md)
	- [漫画操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/Comic.md)
	- [漫画任务操作](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/Activity.md)
	- [漫画赛季](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/Season.md)
	- [漫读券/已购相关](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/User.md)
	- [下载](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/Download.md)
	- [data.index 解析](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/index_file.md)
	- [获取轻享卡信息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/manga/light_card.md)
- 哔哩哔哩游戏
- [终端网络查询](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/clientinfo)
	- [基于 IP 的地理位置查询](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/clientinfo/ip.md)
- [客服中心](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/customerservice)
	- [客服消息](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/customerservice/msg.md)
- [web 端组件](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/web_widget)
	- [分区当日投稿数](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/web_widget/zone_upload.md)
	- [404 页漫画收集](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/web_widget/404_manga.md)
	- [首页横幅头图](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/web_widget/header.md)
	- [分区横幅轮播图](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/web_widget/banner.md)
- [APP 端组件](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/APP_widget)
	- [开屏图片 + 恰饭珍贵录像](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/APP_widget/splash.md)
	- [获取最新 APP 版本](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/APP_widget/ver.md)
- [个性装扮](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/garb)
	- [APP 主题](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/garb/skin.md)
	- [主题色](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/garb/color.md)
	- [装扮/收藏集](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/garb/lottery.md)

## ✨鸣谢

你们的存在，让社区更美好

[![contributors](https://camo.githubusercontent.com/f580e0eea1f6729ab384c0d5b3a9906e6f7bfe45b6f453b62350d469303d6968/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f62696c6962696c692d6170692d636f6c6c6563742f636f6e7472696275746f72732e7376673f77696474683d38363026627574746f6e3d66616c7365)](https://github.com/SocialSisterYi/bilibili-API-collect/graphs/contributors)

## 📖相关协议基础

HTTP 协议： [传送门](https://www.cnblogs.com/an-wen/p/11180076.html)

JSON 序列格式： [传送门](https://www.sojson.com/json/json_index.html)

XML 序列格式： [传送门](https://www.w3school.com.cn/xml/xml_intro.asp)

ProtoBuf 序列格式： [传送门](https://www.jianshu.com/p/a24c88c0526a)

## 💦交流

[![](https://avatars.githubusercontent.com/u/45892418)](https://avatars.githubusercontent.com/u/45892418)

⚠注意：开源社群欢迎交流探讨， **拒绝** 咨询、 **不支持** 合作， **黑产号** 一经发现立即拉黑并举报相关 SRC

- QQ 交流群： [邀请链接](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=ympvb3LAPT-Ulu3ezhGqbkJ8zXMKImOX&authKey=z1KdkOdKO3wytN43m9K6On9nBtnDL4pAoD6VQHCipFBb9TasNDKuDHCmOE6TF3uc&noverify=0&group_code=191187164)
- Telegram 交流群： [@bilibili\_API\_collect\_community](https://t.me/bilibili_API_collect_community)

## 🧋发电

欢迎来 ~~交♂易~~ ，大家的支持就是我继续开发的动力！

~~请可爱的易姐喝杯奶茶~~

WeChat & Alipay：

[![](https://github.com/SocialSisterYi/bilibili-API-collect/raw/master/assets/img/sponsorQR.jpg)](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/assets/img/sponsorQR.jpg)

OR Aifadian： [https://afdian.com/@ShakaiAneE](https://afdian.com/@ShakaiAneE)

## 🔗相关项目推荐

### 库及文档

- [jingyuexing/bilibiliAPI](https://github.com/jingyuexing/bilibiliAPI)
- [fython/BilibiliAPIDocs](https://github.com/fython/BilibiliAPIDocs)
- [czp3009/bilibili-api](https://github.com/czp3009/bilibili-api)
- [Vespa314/bilibili-api](https://github.com/Vespa314/bilibili-api)
- [Pengfei00/bili-utils](https://github.com/Pengfei00/bili-utils): bilibili 工具箱
- [lovelyyoshino/Bilibili-Live-API](https://github.com/lovelyyoshino/Bilibili-Live-API): Bilibili 直播/番剧 API 文档
- [flaribbit/bilibili-manga-spider](https://github.com/flaribbit/bilibili-manga-spider): Bilibili 漫画爬虫
- [simon300000/bili-api](https://github.com/simon300000/bili-api): Bilibili Node.js API
- [iyear/biligo](https://github.com/iyear/biligo): Bilibili API SDK in Golang
- [bilibili-openplatform/demo](https://github.com/bilibili-openplatform/demo): 哔哩哔哩开放平台示例代码库
- [ddiu8081/blive-message-listener](https://github.com/ddiu8081/blive-message-listener): Bilibili-live danmu listener with type. Bilibili 直播间弹幕监听库，支持类型输出。
- [Nemo2011/bilibili-api](https://github.com/Nemo2011/bilibili-api): 哔哩哔哩常用API调用。支持视频、番剧、用户、频道、音频等功能。工具齐全。
- [CuteReimu/bilibili](https://github.com/CuteReimu/bilibili): 哔哩哔哩API的Go版本SDK

### 成品

- [NullPointerException/AnimePipe](https://codeberg.org/NullPointerException/AnimePipe): 功能完善的Android流媒体综合客户端，支持Bilibili, Youtube, NicoNico
- [3Shain/Comen](https://github.com/3Shain/Comen): 基于h5的B站直播弹幕姬
- [AncientLysine/BiliLocal](https://github.com/AncientLysine/BiliLocal): 本地弹幕播放器
- [zyzsdy/biliroku](https://github.com/zyzsdy/biliroku): bilibili 生放送（直播）录制
- [otakustay/danmaku-to-ass](https://github.com/otakustay/danmaku-to-ass): A站B站弹幕转字幕文件
- [bilibili-helper/bilibili-helper-o](https://github.com/bilibili-helper/bilibili-helper-o): 哔哩哔哩 (bilibili.com) 辅助工具，可以下载视频，查询弹幕发送人以及一些十分实用的直播区功能。
- [apachecn/CDNDrive](https://github.com/apachecn/CDNDrive): 基于B站相簿上传的文件分块索引存储器
- [Hsury/BiliDrive](https://github.com/Hsury/BiliDrive): 基于B站相簿上传的文件分块索引存储器
- [Tsuk1ko/bilibili-live-chat](https://github.com/Tsuk1ko/bilibili-live-chat): 无后端的仿 YouTube Live Chat 风格的简易 Bilibili 弹幕姬
- [ironmanic/crawler\_target\_users\_good](https://github.com/ironmanic/crawler_target_users_good): 搜索bilibili特定视频，为评论 点赞，关注，私信，一体化服务
- [dd-center/DDatElectron](https://github.com/dd-center/DDatElectron): DD@Home 分布式项目, 桌面客户端
- [dd-center/vtbs.moe](https://github.com/dd-center/vtbs.moe): B站VTB数据中心
- [the1812/Bilibili-Evolved](https://github.com/the1812/Bilibili-Evolved): 强大的哔哩哔哩增强脚本: 下载视频、音乐、封面、弹幕 / 简化直播间、评论区、首页 / 自定义顶栏、删除广告、夜间模式 / 触屏设备支持
- [xlzy520/bili-short-url](https://github.com/xlzy520/bili-short-url): 哔哩哔哩短链生成器
- [zjkwdy/bili\_app\_splash](https://github.com/zjkwdy/bili_app_splash): B站壁纸娘和开屏图自动下载，每天使用Actions自动同步
- [Jannchie/BiliOB](https://github.com/Jannchie/BiliOB): BiliOB观测者是一个观测B站UP主及视频数据变化，并予以分析的Web应用程序
- [biliob233/biliob233.github.io](https://github.com/biliob233/biliob233.github.io): ~~无可奉告~~
- [biliup/biliup](https://github.com/biliup/biliup): 全自动录播、投稿工具，支持录制直播弹幕，也支持Youtube、twitch直播回放列表自动搬运到B站
- [ddiu8081/bilicli](https://github.com/ddiu8081/bilicli): Bilibili-live danmu dashboard in your terminal.
- [MotooriKashin/Bilibili-Old](https://github.com/MotooriKashin/Bilibili-Old): 恢复旧版Bilibili页面，为了那些念旧的人。
- [SocialSisterYi/bcut-asr](https://github.com/SocialSisterYi/bcut-asr): 使用必剪API的语音字幕识别
- [CzJam/Bili\_Realtime\_Data](https://github.com/CzJam/Bili_Realtime_Data): Bilibili粉丝与视频实时数据统计
- [kingwingfly/fav](https://github.com/kingwingfly/fav): 自动同步bili收藏夹、合集视频到本地的CLI工具（Rust实现，并提供一个文档测试完善的Rust风格的用于构建有状态爬虫的核心库）
- [linyuye/Bilibili\_crawler](https://github.com/linyuye/Bilibili_crawler): 基于bilibili懒加载api爬取b站动态，视频等评论区
- [ouzexi/bilibili-hot-tags](https://github.com/ouzexi/bilibili-hot-tags): 一个B站热门视频标签检索统计小工具
- [SpenserCai/rust-video-downloader](https://github.com/SpenserCai/rust-video-downloader): Rust实现的高性能跨平台视频下载器（目前支持Bilibili），基本覆盖了BBDown的所有功能。

### 其他

- [kuresaru/geetest-validator](https://github.com/kuresaru/geetest-validator): GeeTest 调试器
- [bloomrpc/bloomrpc](https://github.com/bloomrpc/bloomrpc): GUI Client for GRPC Services
- [grpc/grpc](https://github.com/grpc/grpc): The C based gRPC (C++, Python, Ruby, Objective-C, PHP, C#)
- [glideapps/quicktype](https://github.com/glideapps/quicktype): quicktype generates strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries, making it a breeze to work with JSON type-safely in many programming languages. 一键生成多种语言的JSON反序列化所需类，以便于快速反序列化，有网页版
- [SessionHu/json-apidoc-gen](https://github.com/SessionHu/json-apidoc-gen): Simple CLI tool for generating BAC document template

## Sponsor this project

- [https://afdian.com/@ShakaiAneE](https://afdian.com/@ShakaiAneE)

## Languages

- [JavaScript 77.0%](https://github.com/SocialSisterYi/bilibili-API-collect/search?l=javascript)
- [Vue 23.0%](https://github.com/SocialSisterYi/bilibili-API-collect/search?l=vue)