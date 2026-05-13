# hitokoto-fortune

将 [一言](https://hitokoto.cn/)（hitokoto-osc/sentences-bundle）的语录数据转换为 `fortune-mod` 格式的数据库文件，并构建为 Debian 软件包。

## 安装

### Debian/Ubuntu

```bash
sudo dpkg -i fortune-hitokoto_<version>_all.deb
fortune hitokoto
```

### Termux (Android)

```bash
dpkg -i fortune-hitokoto_<version>_aarch64.deb
fortune hitokoto
```

按分类查看：

```bash
fortune hitokoto-a   # 动画
fortune hitokoto-b   # 漫画
fortune hitokoto-c   # 游戏
fortune hitokoto-d   # 文学
fortune hitokoto-e   # 原创
fortune hitokoto-f   # 网络
fortune hitokoto-g   # 其他
fortune hitokoto-h   # 影视
fortune hitokoto-i   # 诗词
fortune hitokoto-j   # 网易云
fortune hitokoto-k   # 哲学
fortune hitokoto-l   # 搞笑
```

## 构建

需要 `fortune-mod` 和 `python3`：

```bash
# 克隆数据源
git clone https://github.com/hitokoto-osc/sentences-bundle.git sentences-bundle

# 转换为 fortune 格式
python3 scripts/convert.py sentences-bundle/sentences fortunes

# 生成 .dat 索引文件
for f in fortunes/hitokoto*; do
  [[ "$f" != *.dat ]] && strfile "$f" "${f}.dat"
done
```

## 分类

| 键 | 分类 |
|----|------|
| a  | 动画 |
| b  | 漫画 |
| c  | 游戏 |
| d  | 文学 |
| e  | 原创 |
| f  | 网络 |
| g  | 其他 |
| h  | 影视 |
| i  | 诗词 |
| j  | 网易云 |
| k  | 哲学 |
| l  | 搞笑 |

## 自动构建

项目通过 GitHub Actions 自动构建，每周定时从上游数据源更新并发布新的 deb 包到 [Releases](https://github.com/bcw222/hitokoto-fortune/releases)，同时提供标准 Debian 包和 Termux 包。

## 许可证

本项目使用 [AGPL-3.0](LICENSE) 许可证，因为输出的数据文件衍生自 [hitokoto-osc/sentences-bundle](https://github.com/hitokoto-osc/sentences-bundle)（同样为 AGPL-3.0）。