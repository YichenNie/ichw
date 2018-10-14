# ichw4
Assignments of Introduction to Computing B


**需要Chrome浏览器插件[GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)才能正确显示公式.**

###1. 解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？
**作业**：计算机操作者交给操作系统的执行单位。
**进程**：计算机中已运行程序的实体。早期的计算机同一时间只能运行一个程序，然而有时有些程序需要做速度慢的操作，此时处理器就相当于进入空闲状态。为使计处理器保持运作，可以使不同程序轮流使用处理器一段时间，这看上去就像多个程序共享运算能力。进程的概念因此产生。
**线程**：操作系统能够进行运算调度的最小单位。进程只能使同一时间内做同一件事，且进程中遇到阻塞（如等待输入）时，即便有不需要输入的数据也无法进行处理。将进程变为多个线程即可解决该问题。同时线程使进程可以在中多核处理器分散计算，加快速度。

####参考资料
1. https://baike.baidu.com/item/作业
2. https://zh.wikipedia.org/zh-cn/行程
3. https://zh.wikipedia.org/wiki/线程
4. http://www.cnblogs.com/Berryxiong/p/6429723.html

###2. 调研虚拟存储器的概念，描述其工作原理和作用

虚拟存储器（虚拟内存）是内存管理的一种技术。它使得应用程序认为它拥有连续可用的内存（一个连续完整的地址空间），而实际上，它通常是被分隔成多个物理内存碎片，还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。   
虚拟存储器它为每个进程提供了一个大的，一致的和私有的地址空间。
####参考
https://blog.csdn.net/lisi1129/article/details/56479975
https://zh.wikipedia.org/wiki/虚拟内存