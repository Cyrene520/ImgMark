# 图片批量水印工具

一个用 Python 编写的图片批量水印添加脚本，支持自定义文字、透明度、旋转角度和间距。

---

##  功能特点

- 批量处理 `.jpg`、`.jpeg`、`.png` 格式图片
- 自定义水印文字内容
- 可调节透明度（0-255）
- 可调节旋转角度（0-360）
- 可调节水印间距
- 平铺式水印覆盖整张图片
- 支持自定义字体文件

---

效果预览<img width="2400" height="1080" alt="Screenshot_1029632950239240" src="https://github.com/user-attachments/assets/8195406f-c76f-4e10-815e-9c8098175fd2" />


##  如何使用？

 依赖安装

```bash
pip install Pillow
```
然后直接运行脚本
```bash
python 水印.py
```

---

##  参数调节
```
input_folder_path = "C"
输入文件夹（填写完整的文件所在路径）

output_folder_path = "Cyrene"
输出文件夹（同上）

watermark_text = "需要添加的文本"
水印文字

font_file_path = "DINCOND-BOLD.otf"                
字体文件路径（同样填写完成途径）

text_size = 50                                         
字号大小

spacing = 50
间距

alpha = 20
透明度（填写0～255的整数数字）

angle = 45
旋转角度（0～360）
```
## 下载
[水印.py](https://github.com/user-attachments/files/30675976/default.py)

