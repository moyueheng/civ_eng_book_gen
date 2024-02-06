# 轻型门式钢架 
# 一、设计资料 
单跨双坡轻型门式刚架，刚架跨度18m，长度60m，柱距7.5m，柱高6m，共有9.0榀刚架，屋面坡度0.1，刚架为等截面梁柱，采用Q235钢材，焊条采用E43型，螺栓采用高强度摩擦螺栓。地震设防烈度为7度，地震加速度设计值为0.1g，风振系数和风压高度变化系数均取1.0，檩条间距1.5m，恒荷载分项系数取1.3，活荷载分项系数取1.5，最不利截面内力设计值按荷载基本组合设计。# 二、柱网及屋面布置 
## 1、柱网平面布置
## 2、支撑体系布置
![18m跨度7.5m柱距平面支撑.png](./image/18m跨度7.5m柱距平面支撑.png)![18m跨度7.5m柱距柱间支撑.png](./image/18m跨度7.5m柱距柱间支撑.png)# 三、结构内力分析
## 1、荷载计算
永久荷载：吊顶0.5kN/m²
屋面活荷载：计算刚架时0.5kN/m²，计算檩条时0.5kN/m²
风荷载和雪荷载：0.4kN/m²，0.5kN/m²


**各荷载标准值计算**
| 类型 | 参数 | 值 |
| :--: | :--: | :--: |
| 屋面 | 活荷载标准值 | 0.5×7.5=3.75kN/m |
| 钢架 | 吊顶 | 0.5×7.5=3.75kN/m |
| 迎风面 | 柱上q1 | 0.4×7.5×0.8=2.4kN/m |
|  | 横梁上q2 | 0.4×7.5×-0.6=-1.8kN/m |
| 背风面 | 柱上q3 |0.4×7.5×-0.5=-1.5kN/m  |
|  | 横梁上q4 | 0.4×7.5×-0.5=-1.5kN/m |

## 2、恒活荷载、风荷载计算简图
![恒荷载下的计算简图.png](./image/恒荷载下的计算简图.png)
![风荷载下的计算简图.png](./image/风荷载下的计算简图.png)
# 四、内力分析## 1、内力计算为了简化计算，假设恒荷载沿水平方向分布在梁上，风荷载沿竖直方向分布在柱子上及沿着坡屋顶分布，当遇到左风时，左侧为风压力，右侧为风吸力，且屋面坡度小于30°，左侧风载体形系数为0.6，右侧为-0.5。计算内力时候避免复杂运算，可采取单位力法计算出内力系数(即q=1时，钢架的内力值)，后根据荷载大小进行扩大倍数，最后求出实际内力值。内力系数分布如下图所示。
![恒荷载下的计算简图.png](./image/恒活荷载内力系数1.png)
![风荷载下的计算简图.png](./image/恒活荷载内力系数2.png)
![恒荷载下的计算简图.png](./image/恒活荷载内力系数3.png)
![风荷载下的计算简图.png](./image/风荷载内力系数1.png)
![恒荷载下的计算简图.png](./image/风荷载内力系数2.png)
![风荷载下的计算简图.png](./image/风荷载内力系数3.png)
恒荷载取3.75kN/m，活荷载取风荷载和雪荷载最大值，即3.75kN/m，按照以下三种组合方式，选取最不利截面设计值：
组合①：1.35×恒荷载+1.5×0.7×活荷载
组合②：1.3×恒荷载+1.5×活荷载
组合③：1.3×恒荷载+1.5×0.9×(活荷载+风荷载)
| 截面   | 内力   |    恒荷载 |    活荷载 |    风荷载 |     组合① |     组合② |     组合③ |   最不利组合 |
|:-----|:-----|-------:|-------:|-------:|--------:|--------:|--------:|--------:|
| 柱A   | M    |  59.29 |  59.29 | -67.2  |  142.29 |  166    |  208.34 |  208.34 |
|      | N    | -39.38 | -39.38 |  -8.64 |  -94.5  | -110.25 | -138.36 |  138.36 |
|      | Q    | -24.82 | -24.82 |  20.4  |  -59.58 |  -69.51 |  -87.24 |   87.24 |
| 柱B   | M    | -99.67 | -99.67 |  14.21 | -239.22 | -279.09 | -350.26 |  350.26 |
|      | N    | -39.38 | -39.38 |   8.64 |  -94.5  | -110.25 | -138.36 |  138.36 |
|      | Q    | -24.75 | -24.75 |  20.4  |  -59.4  |  -69.3  |  -86.97 |   86.97 |
| 柱B   | M    | -99.67 | -99.67 |  24.84 | -239.22 | -279.09 | -199.55 |  279.09 |
|      | N    | -32.06 | -32.06 |   2.21 |  -76.95 |  -89.78 |  -64.19 |   89.78 |
|      | Q    |  33.75 |  33.75 |  -7.16 |   81    |   94.5  |   67.57 |   94.5  |
| 梁C   | M    |  58.05 |  58.05 | -24.84 |  139.32 |  162.54 |  116.22 |  162.54 |
|      | N    | -24.34 | -24.34 |  -2.21 |  -58.41 |  -68.15 |  -48.72 |   68.15 |
|      | Q    |  -4.88 |  -4.88 |  -7.16 |  -11.7  |  -13.65 |   -9.76 |   13.65 |
# 五、钢架设计
## 1、截面设计
梁柱均选用HM588×300×12×20，截面特性为A=192.5mm²，b=300mm，t=20mm，Ix=118000mm⁴，Wx=4020cm³，ix=24.8cm，Iy=9020mm⁴，Wy=601cm³，iy=6.85cm。
## 2、构件验算
构件宽厚比的验算：
翼缘部分：
$$
\frac{b}{t}=\frac{300}{20}=15.00<15\sqrt{\frac{335}{f_y}}=15
$$
腹板部分：
$$
\frac{h_w}{t_w}=\frac{568}{12}=47.3<250\sqrt{\frac{335}{f_y}}=250
$$


钢架梁的验算:
内力设计值$V_{max}=94.5kN$
①抗剪强度验算(考虑仅有支座加劲肋)：
$$
\lambda_s=\frac{{hw}/{tw}}{41\sqrt{5.34}}\sqrt{\frac{fy}{235}}=\frac{568/12}{41\sqrt{5.34}}=0.6<0.8
$$
则极限承载力：
$$
V_u=h_w\times t_w\times f_v=568\times12\times125=852.0kN>94.5kN
$$
满足要求。
②弯、剪、压共同作用下的验算：
取梁端截面：
$$
N=89.78kN，V=94.5kN，M=279.09kN·m，\text{又因}V<0.5V_u，\text{取}V=0.5V_u=426.0kN
M_f=\left(A_{f1}\times\frac{h_1^2}{h_2}+A_{f2}\times h_2\right)\times\left(f-\frac{N}{A}\right)=\left(6.0\times\frac{0.28^2}{0.28}+6.0\times 0.28\right)\times\left(315-\frac{89.78}{1.93}\right)=1058.38kN·m＞279.09kN·m
M_f＞M，\text{取}M=M_f=1058.38kN·m,\text{故：}
\left(\frac{V}{0.5\times V_u}-1\right)^2+\frac{M-M_f}{M_{eu}-M_f}=\left(\frac{426000.0}{0.5\times852000}-1\right)^2+\frac{1058.38-1058.38}{279.09-1058.38}=0.0<1
$$
满足要求。
③整体稳定性验算:
1)梁平面内稳定验算
$$
\text{计算长度取横梁长度}l_x=18000mm。
\lambda_x=\frac{l_x}{i_x}=\frac{1800.0}{24.8}=72.58<[\lambda]=150,\text{b类截面，查表得}φ_x=0.855
N^' = \frac{\pi^2 \times E \times A}{1.1 \times \lambda^2} = \frac{3.14^2 \times 206 \times 10^6 \times 192.5}{1.1 \times 72.58^2}=67541.56kN,\text{取}\beta_{mx}=1.0
$$
则弯剪压共同作用下最大应力：
$$
\frac{N}{\varphi_x \times A} + \frac{\beta_{mx} \times M_x}{W_{e1} \times \left(1-\varphi_x \times \frac{N}{N'}\right)} = \frac{89.78}{0.855 \times 192.5} + \frac{1.0 \times 279090.0}{4020 \times \left(1-0.855 \times \frac{89.78}{67541.56}\right)} = 70.05N/mm^2 < f = 315N/mm^2
$$
满足要求。
2)梁平面外稳定验算
考虑蒙皮效应，两个檩条间距不小于1200mm，计算长度按两个檩距考虑，即：
$$
l_y=2400mm，\text{对于等截面构件}\gamma=0，μ_s=μ_w=1。
\lambda_y=\frac{l_y}{i_y}=\frac{120.0}{6.85}=17.5，\text{是b类截面，查表得}φ_y=0.965。
$$
$$
\varphi_{by}=\frac{4320}{{\lambda_y}^2}\times\frac{A\times h_w}{W_x\times{10}^3}\times\sqrt{\left(\frac{\lambda_y\times t}{4.4\times h_w}\right)^2}=\frac{4320}{{17.52}^2}\times\frac{19250.0\times568}{4020\times{10}^3}\times\sqrt{\left(\frac{17.52\times20}{4.4\times568}\right)^2}=5.4＞0.6
$$
$$
\text{则取}{\varphi_b}^'=1.07-0.282/\varphi_{by}=1.02
$$
$$
\beta_t=1.0-\frac{N}{N\prime}+0.75\times\left(\frac{N}{N\prime}\right)^2=1.0-\frac{89.78}{67541.56}+0.75\times\left(\frac{89.78}{67541.56}\right)^2=0.999
$$
$$
\frac{N}{\varphi_y\times A}+\frac{\beta_t\times M}{Wx\times\varphi_b^'}=\frac{89.78}{0.965\times192.5}+\frac{0.999\times279090.0}{4020\times1.02}=68.46N/mm^2<f=315N/mm^2
$$
钢架柱的验算:
内力设计值$V_{max}=87.24kN$
①抗剪强度验算(考虑仅有支座加劲肋)：
$$
\lambda_s=\frac{{hw}/{tw}}{41\sqrt{5.34}}\sqrt{\frac{fy}{235}}=\frac{568/12}{41\sqrt{5.34}}=0.6<0.8
$$
则极限承载力：
$$
V_u=h_w\times t_w\times f_v=568\times12\times125=852.0kN>87.24kN
$$
满足要求。
②弯、剪、压共同作用下的验算：
取柱端截面：
$$
N=138.36kN，V=87.24kN，M=350.26kN·m，\text{又因}V<0.5V_u，\text{取}V=0.5V_u=426.0kN
$$
$$
M_f=\left(A_{f1}\times\frac{h_1^2}{h_2}+A_{f2}\times h_2\right)\times\left(f-\frac{N}{A}\right)=\left(6.0\times\frac{0.28^2}{0.28}+6.0\times 0.28\right)\times\left(335-\frac{138.36}{1.93}\right)=1125.58kN·m＞350.26kN·m
$$
$$
M_f＞M，\text{取}M=M_f=1125.58kN·m，\text{故：}
\left(\frac{V}{0.5\times V_u}-1\right)^2+\frac{M-M_f}{M_{eu}-M_f}=\left(\frac{426000.0}{0.5\times852000}-1\right)^2+\frac{1125.58-1125.58}{279.09-1125.58}=0.0<1
$$
满足要求。
③整体稳定性验算:
1)柱平面内稳定验算
$$
\text{钢架柱高}H=6000mm，\text{梁长}L=19386.6mm。
$$
柱的线刚度：
$$
k_1=\frac{I_a}{h}=\frac{118000\times10^4}{6000}=196666.67mm³
$$
梁的线刚度:
$$
k_2=\frac{I_b}{h}=\frac{118000\times10^4}{19386.6}=60866.78mm³
\text{则}k_1/k_2=196666.67/60866.78=3.23，I_y/I_x=0.08，\text{查表得}μ_r=3.414
$$
计算长度：
$$
l_x=\mu_r\times h=3.414\times6000=20484.0mm
$$
验算长细比：
$$
\lambda_x=\frac{l_x}{i_x}=\frac{20484.0}{248.0}=82.60<\left[\lambda\right]=150,b\text{类截面}，\text{查表得}\varphi_x=0.835
$$
$$
N^' = \frac{\pi^2 \times E \times A}{1.1 \times \lambda^2} = \frac{3.14^2 \times 206 \times 10^6 \times 192.5}{1.1 \times 82.6^2}=52148.87kN，\text{取}\beta_{mx}=1.0
$$
则弯、剪、压共同作用下截面最大应力：
$$
\frac{N}{\varphi_x \times A} + \frac{\beta_{mx} \times M_x}{W_{e1} \times \left(1-\varphi_x \times \frac{N}{N'}\right)} = \frac{138.36}{0.835 \times 192.5} + \frac{1.0 \times 350260.0}{4020 \times \left(1-0.835 \times \frac{138.36}{52148.87}\right)} = 88.18N/mm^2 < f = 315N/mm^2
$$
满足要求。
2)柱面外稳定验算
考虑蒙皮效应，两个檩条间距不小于1200mm，计算长度按两个檩距考虑，$\text{即}l_y=2400mm，\text{对于等截面构件}\gamma=0，μ_s=μ_w=1$。
$$
\lambda_y=\frac{l_y}{i_y}=\frac{120.0}{6.85}=17.5
$$
$$
\text{是b类截面，查表得}φ_y=0.965。
$$
$$
\varphi_{by}=\frac{4320}{{\lambda_y}^2}\times\frac{A\times h_w}{W_x\times{10}^3}\times\sqrt{\left(\frac{\lambda_y\times t}{4.4\times h_w}\right)^2}=\frac{4320}{{17.52}^2}\times\frac{19250.0\times568}{4020\times{10}^3}\times\sqrt{\left(\frac{17.52\times20}{4.4\times568}\right)^2}=5.4＞0.6
$$
则取${\varphi_b}^'=1.07-0.282/\varphi_{by}=1.02$
$$
\beta_t=1.0-\frac{N}{N\prime}+0.75\times\left(\frac{N}{N\prime}\right)^2=1.0-\frac{138.36}{52148.87}+0.75\times\left(\frac{138.36}{52148.87}\right)^2=0.997
$$
则弯、剪、压共同作用下截面最大应力：
$$
\frac{N}{\varphi_y\times A}+\frac{\beta_t\times M}{Wx\times\varphi_b^'}=\frac{138.36}{0.965\times192.5}+\frac{0.997\times279090.0}{4020\times1.02}=68.63N/mm^2<f=315N/mm^2
$$
4)钢架在风荷载作用下侧移验算
截面惯性矩：
$$
I_c=I_b=118000mm^4
$$
位移修正系数：
$$
\xi_t=\frac{I_cL}{hI_B}=\frac{18000}{6000}=3.00
$$
风压设计值：
$$
W=\left(W_1+W_4\right)\times h=\left(2.4+1.5\right)\times 6=23.400kN
$$
钢架柱顶等效水平力：
$$
W_k=0.67×W=0.67×23.400=15.678kN
$$
左风荷载下顶点位移：
$$
\mu=\frac{H\times h^3}{12\times E\times I_c}\times\left(2+\xi_1\right)=\frac{23.4\times10^3\times6000^3}{12\times206\times10^3\times118000\times10^4}\times\left(2+3.0\right)=8.66mm<\left[\mu\right]=h/150=60mm
$$


# 3、节点验算
拼接板尺寸如图：
![拼接板尺寸详图.png](./image/拼接板尺寸详图.png)

## (1)梁柱节点验算
①螺栓强度验算
梁柱节点采用10.9级M27高强度摩擦型螺栓连接，摩擦面抗滑移系数µ=0.45，每个高强度螺栓的预拉力为290N,连接处传递内力设计值：
$$
N=89.78kN,V=94.5kN,M=279.09kN·m
$$
每个螺栓拉力设计值：
$$
N_1=\frac{M\times y_1}{4\times\sum y_i^2}-\frac{N}{n}=\frac{279.09\times0.3}{4\times\sum 0.3^2+0.4^2}-\frac{89.78}{10}=75kN<0.8×290=232.0kN
$$
$$
N_2=\frac{M\times y_2}{4\times\sum y_i^2}-\frac{N}{n}=\frac{279.09\times0.4}{4\times\sum 0.3^2+0.4^2}-\frac{89.78}{10}=103kN<0.8×290=232.0kN
$$
螺栓群抗剪承载力：
$$
N_v^b=0.9\times N_f\times \mu\times P=0.9\times 1\times 0.45\times 290\times 8=940kN>V=94.5kN
$$
最外排一个螺栓承载力：
$$
\frac{N_v}{N_v^b}+\frac{N_t}{N_t^b}=\frac{94.5}{939.6}+\frac{89.78}{232.0}=0.49<1
$$
满足要求。
②端板厚度验算
短板厚度取为t=30mm，按二辩支撑类端板计算：
$$
t \geq \sqrt{\frac{6 \times e_f \times e_w \times N_t}{e_w \times b + 2 \times e_f \times (e_f + e_w) \times f}} = \sqrt{\frac{6 \times 60 \times 80 \times 89.78 \times 1000}{80 \times 300 + 2 \times 60 \times (60 + 80) \times 315}} = 22.05mm>25mm
$$
满足要求。
③梁柱节点域的剪应力验算
$$
\tau=\frac{M}{d_b\times d_c\times t_c}=\frac{279.09\times 10^6}{568\times 568\times 20}=43.25N/mm^2<f=315N/mm^2
$$
满足要求。
④螺栓处腹板强度验算
$$
N_t=89.78kN<0.4\times290=116.0kN
$$
抗剪强度验算：
$$
\frac{0.4P}{e_w\times t_w}=\frac{0.4\times290000}{80\times12}=120.83N/mm^2 < f=315N/mm^2
$$
满足要求。



## (2)跨中梁节点验算
①螺栓强度验算
跨中梁节点采用10.9级M22高强度摩擦型螺栓连接，摩擦面抗滑移系数µ=0.45，每个高强度螺栓的预拉力为190N,连接处传递内力设计值：
$$
N=68.15kN,V=13.65kN,M=162.54kN·m
$$
每个螺栓拉力设计值：
$$
N_1=\frac{M\times y_1}{4\times\sum y_i^2}-\frac{N}{n}=\frac{162.54\times0.3}{4\times\sum 0.3^2+0.4^2}-\frac{68.15}{10}=42kN<0.8×190=152.0kN
$$
$$
N_2=\frac{M\times y_2}{4\times\sum y_i^2}-\frac{N}{n}=\frac{162.54\times0.4}{4\times\sum 0.3^2+0.4^2}-\frac{68.15}{10}=58kN<0.8×190=152.0kN
$$
螺栓群抗剪承载力：
$$
N_v^b=0.9\times N_f\times \mu\times P=0.9\times 1\times 0.45\times 190\times 8=616kN>V=13.65kN
$$
最外排一个螺栓承载力：
$$
\frac{N_v}{N_v^b}+\frac{N_t}{N_t^b}=\frac{13.65}{615.6}+\frac{68.15}{152.0}=0.47<1
$$
满足要求。
②端板厚度验算
短板厚度取为t=20mm，按二辩支撑类端板计算：
$$
t \geq \sqrt{\frac{6 \times e_f \times e_w \times N_t}{e_w \times b + 2 \times e_f \times (e_f + e_w) \times f}} = \sqrt{\frac{6 \times 60 \times 80 \times 68.15 \times 1000}{80 \times 300 + 2 \times 60 \times (60 + 80) \times 335}} = 18.63mm>15mm
$$
满足要求。
③螺栓处腹板强度验算
$$
N_t=68.15kN<0.4\times190=116.0kN
$$
抗剪强度验算：
$$
\frac{0.4P}{e_w\times t_w}=\frac{0.4\times290000}{80\times12}=79.17N/mm^2 < f=315N/mm^2
$$
满足要求。


## (2)柱脚节点验算
钢柱与基础铰接连接
①柱脚内力设计值
$$
N_{max}=89.78kN,N_{min}=68.15kN
V_{max}=94.5kN,V_{min}=13.65kN
$$
②构造要求
由于柱底剪力比较小，且$$V_{max}=94.5kN>0.4N_{max}=35.912kN\$ ，故设置柱间支撑的开间必须设置剪力键，按构造要求设置锚栓即可，采用4M24螺栓。
③柱脚底板面积
$$
b=b_0+2t+2c=300+2\times20+2\times\left(20~50\right)=380~440mm,\text{取}b=400mm
h=h_0+2t+2c=588+2\times20+2\times\left(20~50\right)=668~728mm,\text{取}h=700mm
$$
底板混凝土强度验算：
采用C30混凝土，$f_c=14.3N/mm^2$ ,则最大压应力：
$$
\sigma=\frac{N}{bh}=\frac{68.15\times{10}^3}{400\times700}=0.24N/mm^2<f_c=14.3N/mm^2
$$
③柱脚底板厚度
支撑板部分弯矩：
$$
M_1=\frac12\times\sigma\times a_1^2=\frac12\times0.24\times150^2=2700.0N\bullet m
$$
悬挑部分弯矩：
$$
M_2=\frac12\times\sigma\times a_2^2=\frac12\times0.24\times50^2=300.0N\bullet m
$$
则底板厚度为：
$$
t=\sqrt{\frac{6M_{max}}{f}}=\sqrt{\frac{6\times2700.0}{315}}=7.17mm,\text{取}t=10mm
$$
# 六、檩条设计
 檩条选用实腹式檩条，截面形式选用冷弯薄壁C型钢C250X70X20X3.0，钢材钢号：Q235钢。拉条设置：设置一道拉条，拉条作用：约束檩条上翼缘。由于设置了一道拉条，保证了檩条在竖向荷载的作用下的整体稳定性，故不用验算檩条的整体稳定性。檩条计算简图如图
![檩条计算简图.png](./image/檩条计算简图.png)
檩条所受的竖向荷载，屋面板和檩条自重：3.75kN/m2，可变荷载：3.75kN/m2，则线荷载设计值q=((3.75+3.75)×1.5=11.25kN/m。
按简支梁计算，两个方向弯矩分别是：
跨中最大弯矩：
$$
M_x=\frac{1}{8}q_yl^2=\frac{1}{8}ql^2\cos{{\alpha}}=\frac{1}{8}\times11.25\times7500.0^2\times \cos{5.71}^\circ=66.46 \mathrm{kN·m}
M_y=0.0156q_xl^2=0.0156ql^2\sin{{\alpha}}=0.0156\times11.25\times7.5^2\times \sin{5.71}^\circ=5.35 \mathrm{kN·m}
$$
支座负弯矩：
$$
M_y=-0.0313q_xl^2=-0.0313ql^2\sin{{\alpha}}=-0.0313\times11.25\times7.5^2\times \sin{5.71}^\circ=10.74 \mathrm{kN·m}
$$
檩条的受弯强度验算：
冷弯薄壁C型钢C250X70X20X3.0的截面特性为:I_x=1013.01cm^4，W_x=81040.0mm³，W_y=12820.0mm³。验算强度时，最不利截面取Mx最大值及其同一截面的My进行计算。
截面最大正应力：
$$
\frac{M_x}{W_x}+\frac{M_y}{W_y}=\frac{66459377.80}{81040.0}+\frac{-5353626.60}{12820.0}=402.48 \mathrm{N/m}\mathrm{m}^2 < f=315 \mathrm{N/m}\mathrm{m}^2
$$
檩条的挠度验算：
由于设有拉条，只验算垂直于屋面坡度的挠度即可。考虑荷载的组合系数，采用恒载+活载+0.9积灰荷载的荷载标准值组合，则:
$$
q_y^\prime=(0.5+3.75+0.9\times0.5)\times1.5\times\cos{5.71}^\circ=5.92 \mathrm{N/m}
\frac{w}{l}=\frac{5q_y^\prime l^3}{384EI_x}=\frac{5\times5.92\times7500.0^3}{384\times206000.00\times10130100.00}=0.015592<\frac{1}{150}
$$


