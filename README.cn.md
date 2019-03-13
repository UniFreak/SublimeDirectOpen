Sublime Text 的 `Direct Open` 包能根据配置, 通过快捷键快速打开常用的文件以编辑

## 安装

有两种方式可以安装, 第一种是通过 `Package Control`:

1. 确保装有 Package Control, 参见 <https://packagecontrol.io/installation>
2. 搜索 `Direct Open` 并安装

另一种方式是直接通过克隆源码安装:

1. 进入 sublime text 的包目录
2. 运行 `git clone https://github.com/UniFreak/SublimeDirectOpen.git`

## 配置 & 使用

已经提供了一个默认的 `Host` 文件配置, 你可以在 `files` 配置项下面, 依照 `Host` 的配置添加额外的文件名 (`title` 配置项) 及其路径 (`location` 配置项). 如下:

```json
{
    "files":
    [
        {
            "title" : "Host",
            "location" : "/etc/hosts"
        },
    ]
}
```

配置完成后, 可以通过快捷键 `ctrl+shift+o` (Windows) 或 `super+shift+o` (Mac) 调出文件列表, 选中即可打开文件, 如图

![example](./shot.png)


## 感谢

感谢 [SublimeHostsEdit][hostsEdit] 包及其作者为此包提供灵感

## TODO


[hostsEdit]: https://github.com/martinssipenko/SublimeHostsEdit
