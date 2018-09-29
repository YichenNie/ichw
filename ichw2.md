<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>
# ichw2
Assignments of Introduction to Computing B
## 用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么.
## 你在向中学生做科普，请向他们解释二进制补码的原理.
## 某基于 IEEE 754浮点数格式的 16 bit 浮点数表示, 有 8 个小数位, 请给出 ±0, ±1.0, 最大非规范化数, 最小非规范化数, 最小规范化浮点数, 最大规范化浮点数, ±∞, NaN 的二进制表示.
|数|二进制数|十进制表示|
|:----:|:------:|:----:|
|+0|0000 0000 0000 0000|0|
|-0|1000 0000 0000 0000|0|
|+1.0|0011 1111 0000 0000|1|
|-1.0|1011 1111 0000 0000|-1|
|最大非规范化数|0000 0000 1111 1111|$ (1-2^{-8})\times 2^{-62} $|
|最小非规范化数|0000 0000 0000 0001|$ 2^{-8}\times 2^{-62} $|
|最小规范化浮点数|0000 0001 0000 0000|$ 1\times 2^{-62} $|
|最大规范化浮点数|0111 1110 1111 1111|$ (2-2^{-8})\times 2^{63} $|
|±∞|\*111 1111 0000 0000|$ \pm \infty $|
|NaN|\*111 1111 小数部分非零|NaN|

**需要Chrome浏览器插件[GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)才能正确显示公式**
