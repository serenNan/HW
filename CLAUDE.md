# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个强化学习课程的作业项目（HW2），专注于 Windy Gridworld 环境下的 SARSA 和 Q-learning 算法实现。

**环境配置：**
- 主要开发语言：Python (Jupyter Notebook)
- 使用 conda 虚拟环境
- 依赖：numpy, matplotlib

## 问题描述

### Windy Gridworld 变种

基于经典的 Windy Gridworld 环境，本项目有以下特殊设置：

1. **8向移动（国王移动）**：允许对角线移动
   - 动作空间：`{'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}`
   - 初始策略：每个方向均等概率 1/8

2. **死亡方格**：位置 (1,10) 为终止状态
   - 奖励：-100

3. **风的影响**：与标准 Windy Gridworld 相同
   - 例如：在 (6,4) 向 'ne' 移动，无风到 (5,5)，有风到 (4,5)
   - 风会修改垂直方向的移动结果

4. **吸收状态变种**（任务7）：在 (1,4) 添加吸收状态
   - 奖励：+5

## 作业任务

HW2.pdf 定义了以下任务：

1. 使用 SARSA 和 Q-learning 从三个起始位置找到最优策略：
   - (7,1), (4,1), (1,7)

2. 对比仅允许 Rook 移动（4向）的情况

3. 让 LLM 在不指定算法的情况下生成代码，观察其选择的算法

4. 让 LLM 分别生成 SARSA 和 Q-learning 代码，验证结果一致性

5. 测试 LLM 是否能仅通过模型描述生成最优轨迹
   - 例如：从 (1,1) 开始遵循最优策略的轨迹

6. 测试不允许对角线移动的情况

7. 添加吸收状态 (1,4) 奖励为5，重复任务 1-6

## 代码架构

### 核心实现（SARSA.ipynb）

**状态和动作表示：**
- 状态 `s`：元组 `(x, y)` 表示网格位置
- 动作 `a`：字符串或函数引用（如 'n', 'e', u, d, l, r）

**关键函数：**
- `u(s)`, `d(s)`, `l(s)`, `r(s)`：基本4向移动函数
- `random_action()`：随机选择动作
- `reward(s, a)`：返回状态-动作对的奖励
- `sarsa(s, a)`：SARSA 算法单步更新
- `greedy_sarsa(s, a, q)`：epsilon-greedy 策略的 SARSA
- `B(V)`：Bellman 更新或值函数计算
- `idx(t)`：索引辅助函数

**算法实现模式：**
1. **随机策略 SARSA**：使用均匀随机动作选择
2. **ε-greedy SARSA**：结合探索与利用
3. **Q-learning**：off-policy 学习

**可视化：**
- 使用 matplotlib 绘制学习曲线和策略
- 网格图显示：死亡状态（黑色）、吸收状态（蓝色）、风向（灰色箭头）

## 运行和测试

### Jupyter Notebook 执行
```bash
# 启动 Jupyter
jupyter notebook SARSA.ipynb

# 或使用 JupyterLab
jupyter lab SARSA.ipynb
```

### 典型工作流
1. 定义环境参数（网格大小、特殊状态位置、风向）
2. 初始化 Q 表或值函数
3. 运行 SARSA 或 Q-learning 算法
4. 可视化学习过程和最优策略
5. 对比不同起始位置和动作空间的结果

## 实现注意事项

### 算法关键点
- **SARSA**：on-policy，使用 (S, A, R, S', A') 五元组更新
- **Q-learning**：off-policy，使用 max Q(S', a') 更新
- 需要正确处理终止状态（死亡和吸收状态）
- epsilon-greedy 策略需要平衡探索率

### 环境边界处理
- 网格边界检查
- 风的影响计算
- 对角线移动的边界情况

### 参数调优
- 学习率 α（alpha）
- 折扣因子 γ（gamma）
- 探索率 ε（epsilon）
- 训练回合数

## 与 LLM 交互测试

任务 3-6 涉及测试 LLM 的代码生成能力：
- 观察算法选择（SARSA vs Q-learning vs 其他）
- 验证生成代码的正确性
- 测试推理最优策略的能力
- 比较不同约束条件下的表现

### 验证标准
- 算法收敛性
- 最优策略合理性
- 与手写代码结果一致性
- 特殊状态处理正确性
