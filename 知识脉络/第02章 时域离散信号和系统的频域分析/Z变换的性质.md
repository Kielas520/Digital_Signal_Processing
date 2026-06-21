# Z 变换的性质

## 【通俗理解】

Z 变换的性质就是一组"快捷键"——利用它们可以避免从定义出发重新算，直接从已知变换对推出新的变换对。

---

## 核心性质速查表

### 1. 线性

$$
ax_1(n) + bx_2(n) \xleftrightarrow{Z} aX_1(z) + bX_2(z)
$$

收敛域至少是两个收敛域的交集。

### 2. 移位（延迟）性质

$$
x(n - m) \xleftrightarrow{Z} z^{-m} X(z)
$$

时域延迟 $m$ 步 = 频域乘以 $z^{-m}$。收敛域不变（可能 $z=0$ 或 $z=\infty$ 处有变化）。

> 这是 Z 变换最常用的性质，也是解差分方程的基础。

### 3. 乘以指数序列（Z 域尺度变换）

$$
a^n x(n) \xleftrightarrow{Z} X(a^{-1}z)
$$

收敛域变为 $\lvert a\rvert R_1 < \lvert z\rvert < \lvert a\rvert R_2$。

### 4. 翻转

$$
x(-n) \xleftrightarrow{Z} X(z^{-1})
$$

收敛域取倒数：$\frac{1}{R_2} < \lvert z\rvert < \frac{1}{R_1}$。

### 5. 共轭

$$
x^*(n) \xleftrightarrow{Z} X^*(z^*)
$$

### 6. Z 域微分

$$
nx(n) \xleftrightarrow{Z} -z\frac{dX(z)}{dz}
$$

### 7. 卷积定理

$$
x(n) * h(n) \xleftrightarrow{Z} X(z) \cdot H(z)
$$

**时域卷积 = Z 域相乘。** 收敛域至少为两个收敛域的交集。

> 这个性质直接导出了系统函数：$H(z) = Y(z) / X(z)$。

### 8. 初值定理

若 $x(n)$ 为因果序列（$n<0$ 时 $x(n)=0$），则：

$$
x(0) = \lim_{z \to \infty} X(z)
$$

### 9. 帕塞瓦尔定理（能量守恒）

$$
\sum_{n=-\infty}^{+\infty} \lvert x(n)\rvert^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} \lvert X(e^{j\omega})\rvert^2 d\omega
$$

时域能量 = 频域能量。

---

## 【考试最常用的性质】

1. **移位性质**（解差分方程必用）
2. **卷积定理**（推导系统函数必用）
3. **Z 域微分**（求 $na^n u(n)$ 的变换时用）

---

## 【考卷标答模板】

**题型：利用性质求 Z 变换**

> 例：已知 $a^n u(n) \xleftrightarrow{Z} \frac{1}{1-az^{-1}}$，求 $na^n u(n)$ 的 Z 变换。
>
> 解：由 Z 域微分性质 $nx(n) \xleftrightarrow{Z} -z\frac{dX(z)}{dz}$，
>
> $$-z \cdot \frac{d}{dz}\left(\frac{1}{1-az^{-1}}\right) = -z \cdot \left(\frac{-az^{-2}}{(1-az^{-1})^2}\right) = \frac{az^{-1}}{(1-az^{-1})^2}$$
>
> 收敛域 $\lvert z\rvert > \lvert a\rvert$。
