# ichw3
Assignments of Introduction to Computing B

### 1.详述通用的高速缓存存储器结构及工作原理

#### 1-1.缓存的作用
CPU需要高速读取、写入数据,采用不同速度、成本的四层结构（最低速、最廉价←硬盘、内存、缓存、寄存器→最高速、最昂贵）.

缓存这一结构的作用是预先将内存中的部分数据存储进缓存中.当寄存器发出数据请求时,会先查看缓存中是否有相应数据,如果存在（命中,hit）则直接读取,如果不存在（失效,miss）则需先将数据载入缓存,寄存器再读取.

#### 1-2.缓存的存储结构
直接映射缓存由多个缓存块组成,一个缓存块中包括标签（tag）、索引（index）、标志位（flag bits）和数据,每个缓存块中包含连续内存地址的若干个存储单元.

![image text](https://github.com/YichenNie/ichw/blob/master/CPU%E7%BC%93%E5%AD%98_00_%E7%BC%93%E5%AD%98%E6%AE%B5%E7%BB%93%E6%9E%84.png)

#### 1-3.缓存的工作原理
系统启动时,缓存没没有任何数据.
1. 索引定位到缓存块.
2. 标签匹配缓存块的标签值（一般为最低部分）,匹配成功即命中.
3. 命中后,用块内偏移读取特定数据段,送回寄存器.
4. 未命中,则先从内存中载入相应地址的数据,然后送往寄存器.

![image text](https://github.com/YichenNie/ichw/blob/master/CPU%E7%BC%93%E5%AD%98_01_%E8%BF%90%E4%BD%9C%E6%B5%81%E7%A8%8B.png)

#### 1-4.如果没有命中,如何替换缓存块？
最理想的替换策略是替换据下次访问最晚的缓存块,然而无法真正实现.替换策略有：
1. 随机替换.
2. 最近最少使用替换(LRU).
 - 非最近使用(NMRU).替换最近未被使用的的随机一块.
3. 先进先出替换(FIFO).替换进入组内最长时间的缓存块.

#### 1-5.如何提高缓存的效率？
- 评估缓存性能的指标
 - 平均内存访问时间AMAT

  <center>
  $ AMAT = T_{hit}+MR \times MP $
  </center>

  - $T_{hit}$是定位缓存块到传回数据所需的时间,称为命中时间.  
  - MR(miss rate)是未命中的概率,称为失效率.
  - MP(miss penalty)是判定未命中,从内存中载入数据再上传至寄存器中所需的时间,称为失效代价.

 - Cache系统加速比
  <center>
  $ S=\dfrac{T_m}{T}=\dfrac{1}{(1-H)+H\times\dfrac{T_c}{T_m}} $
  </center>

  - $T_m$是访问内存所需时间
  - $T_c$是访问缓存所需时间
  - $H$是命中率

- 降低平均访问时间
 - 小缓存
 - ...
- 降低失效率
 - 大数据块
 - 大缓存
 - ...
- 降低失效代价
 - 多级缓存
 - ...

### 参考资料
1. [CPU 缓存 维基百科](https://zh.wikipedia.org/wiki/CPU缓存)
2. [Cache replacement policies Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies)
3. [计算机系统教程](https://books.google.com.hk/books?id=WREB9kclX5MC&pg=PA134&lpg=PA134&dq=%E5%9D%97%E5%86%B2%E7%AA%81&source=bl&ots=E8QBaQv3os&sig=7gFYFioVC3P8lEU14UcEff1EqUw&hl=zh-CN&sa=X&redir_esc=y&sourceid=cndr#v=onepage&q=%E5%9D%97%E5%86%B2%E7%AA%81&f=false)
