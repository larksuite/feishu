# open_lark

OpenLark: Lark Open Platform Python SDK  / 飞书开发平台 Python SDK


## 安装

执行

```bash
pip install open_lark
```

更详细的安装文档请点击 [这里](https://cyllibmm.fn.bytedance.net/install.html)


## 文档

请点击：https://cyllibmm.fn.bytedance.net/

## 优势

- 完善的文档和网站
- 类型标注，减少运行时 bug
- docstring，减少理解难度
- 实时监控 `open.feishu.cn` 文档库，保证同步更新接口
- dataclass，不用猜测数据内部结构
- 90% 单测覆盖率


## 丰富的接口

<details>
  <summary>

    基本实现了飞书开放平台上关于机器人、发消息、日历、审批、Doc等 100 余种接口

    点击这里展开

  </summary>

- 机器人
  - 获取机器人信息 `get_bot_info`
- 聊天
  - 批量发送消息 `batch_send_message`
  - 发送文字消息 `lark.send().to_xx(xx).send_text()`
  - 发送图片消息 `lark.send().to_xx(xx).send_image()`
  - 发送 at 消息
  - 发送图文消息 `lark.send().to_xx(xx).send_post()`
  - 发送卡片消息
  - 链式调用 `lark.send().to_xx(xx).send_post()`
  - 消息加急 `urgent_message`
- 群组
  - 创建一个群聊 `create_chat`
  - 获取机器人所有的群聊列表 `get_chat_list_of_bot`
  - 获取群聊信息 `get_chat_info`
  - 解散一个群聊 `disband_chat`
  - 邀请用户加入群聊 `invite_user_to_chat`
  - 将用户从群聊移除 `remove_user_from_chat`
  - 邀请机器人加入群聊 `invite_bot_to_chat`
  - 将机器人从群里移除 `remove_bot_from_chat`
- 通讯录
  - 获取通讯录授权范围 `get_contact_scope`
  - 获取子部门 ID 列表 `get_department_children`
- 审批
  - 查看审批定义 `get_approval_definition`
  - 获取单个审批实例详情 `get_approval_instance`
  - 批量获取审批实例ID `get_approval_instance_code_list`
  - 创建审批实例 `create_approval`
  - 订阅审批事件 `subscribe_approval`
  - 取消订阅审批事件 `unsubscribe_approval`
  - 上传审批文件 `upload_approval_file`
- 日历
  - 根据 ID 获取日历 `get_calendar_by_id`
  - 获取日历列表 `get_calendar_list`
  - 创建日历 `create_calendar`
  - 删除日历 `delete_calendar_by_id`
  - 更新日历 `update_calendar_by_id`
  - 获取日程 `get_calendar_event`
  - 创建日程 `create_calendar_event`
  - 获取日程列表 `get_calendar_event_list`
  - 删除日程 `delete_calendar_event`
  - 更新日程 `update_calendar_event`
  - 邀请/移除日程参与者
  - 获取访问控制列表
  - 创建访问控制
  - 删除访问控制
  - 查询日历的忙闲状态
- 小程序
  - code 换 session `mina_code_2_session`
- OAuth
  - 生成 OAuth 授权链接 `gen_oauth_url`
  - Web 扫码后拿到的 code 换取用户信息 `oauth_code_2_session`
  - OAuth 登录后获取用户信息 `oauth_get_user`
  - 使用 app_id 获取用户信息 `get_user`
  - 重新推送 app_ticket `resend_app_ticket`
- id 转换
  - email 转 open_id和employee_id `email_to_id`
  - open_id 转 user_id `open_id_to_user_id`
  - user_id 转 open_id `user_id_to_open_id`
  - employee_id 转 user_id `employee_id_to_user_id`
  - user_id 转 employee_id `user_id_to_employee_id`
  - chat_id 转 open_chat_id `chat_id_to_open_chat_id`
  - open_chat_id 转 chat_id `open_chat_id_to_chat_id`
  - message_id 转 open_message_id `message_id_to_open_message_id`
  - open_message_id 转 message_id `open_message_id_to_message_id`
  - department_id 转 open_department_id `department_id_to_open_department_id`
  - open_department_id 转 department_id `open_department_id_to_department_id`
  - 获取机器人和用户的 chat_id `get_chat_id_between_user_bot`
  - 获取用户和用户的之前的 chat_id `get_chat_id_between_users`
- 图片
  - 上传图片（支持文件本地路径、超链接、bytes 数据、BytesIO 接口） `upload_image`
  - 下载图片 `get_image`
- 回调处理
  - 审批通过 `handle_approval`
  - 请假审批 `handle_leave_approval`
  - 加班审批 `handle_work_approval`
  - 换班审批 `handle_shift_approval`
  - 补卡审批 `handle_remedy_approval`
  - 出差审批 `handle_trip_approval`
  - 开通应用 `handle_app_open`
  - 通讯录用户相关变更事件，包括 user_add, user_update 和 user_leave 事件类型 `handle_contact_user`
  - 通讯录部门相关变更事件，包括 dept_add, dept_update 和 dept_delete `handle_contact_department`
  - 通讯录部门变更权限范围 `handle_contact_scope`
  - 收到消息（必须单聊或者是艾特机器人） `handle_message`
  - 机器人被移出群聊/机器人被邀请进入群聊
  - 下发 app_ticket `handle_app_ticket`
- 服务台
  - 加入服务台 `join_duty_room`

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
