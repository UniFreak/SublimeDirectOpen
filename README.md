# Sublime 3: Direct Open plugin

Config the file paths that you frequently have to edit, then you can hit `ctrl+shift+o` to directly open them and edit


## Installation

- Use package control: search `DirectOpen` and install
- Clone the source code into your sublime text's package folder

## Configuration

In the config file, there are three block for each platform: `windows`, `osx` and `linux`, you just need to add your files config into your corresponding platform config block.

There is only one field you need to contern now, the `files` field. You give it a `title` and a `location`, then it's available in the selection panel when you hit `ctrl+shift+o`.

There is already a configed entry for `Hosts` file. You can refer to that for how to config new entries.

## Thanks

Many thanks to the [SublimeHostsEdit][hostsEdit]'s author, it inspired me to create this plugins. Actually this plugins is simply a extended version of `SublimeHostsEdit`, and I refered to it a lot when begining my path of learning python and sublime plugin development.

## Todo



[hostsEdit]: https://github.com/martinssipenko/SublimeHostsEdit
