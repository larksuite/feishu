# open_lark

OpenLark: Lark Open Platform Python SDK  / 飞书开发平台 Python SDK


## 安装

执行

```bash
pip install open_lark
```

## 优势

- 完善的文档和网站
- 类型标注，减少运行时 bug
- docstring，减少理解难度
- 实时监控 `open.feishu.cn` 文档库，保证同步更新接口
- dataclass，不用猜测数据内部结构
- 90% 单测覆盖率


## TODO

- 支持 windows(windows-latest)
- 支持 pypy

## 丰富的接口

<details>
  <summary>

    基本实现了飞书开放平台上关于机器人、发消息、日历、审批、Doc等 100 余种接口

    点击这里展开

  </summary>

</details>

## 开放平台

- [开放平台](https://open.feishu.cn/)


## 更新日志

点击查看 [更新日志](./CHANGELOG.md)


## 开发

如果想要参与开发，请参考文档 [开发指南](./DEVELOPMENT.md)

- 开发约定
  - 如果有返回 `has_more`，一般是作为第一个返回值
  - 如果参数有 `page_size` 和 `page_token`，一般 `page_size` 在前
  - `page_size` 默认值一般是 `20`
  - 批量操作统一以 `batch` 开头
