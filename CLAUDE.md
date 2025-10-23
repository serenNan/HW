# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个强化学习课程的作业项目（HW2），专注于 Windy Gridworld 环境下的 SARSA 和 Q-learning 算法实现。

**环境配置：**
- 主要开发语言：Python (Jupyter Notebook)
- 使用 conda 虚拟环境（建议：`rl-hw`）
- 依赖：numpy, matplotlib, jupyter

**核心文件：**
- `HW2_Solution.ipynb` - ⭐ 主要实现文件，包含所有任务的完整实现
- `SARSA.ipynb` - 原始参考代码
- `HW2.pdf` - 作业要求文档
- `坐标系统完全正确版.md` - 坐标系统详细说明

## 问题描述

### Windy Gridworld 变种

基于经典的 Windy Gridworld 环境，本项目有以下特殊设置：

**⚠️ 重要：坐标系统**
- 代码使用 **0-based 坐标系**，左上角为原点 (0,0)
- 网格大小：7行 × 10列（行0-6，列0-9）
- 文档中提到的坐标需要转换：文档(row, col) → 代码(row-1, col-1)

1. **8向移动（国王移动）**：允许对角线移动
   - 动作空间：`{'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}`
   - 初始策略：每个方向均等概率 1/8

2. **特殊状态**（0-based 坐标）：
   - 目标状态：(3,7) - 奖励 +10
   - 死亡状态：(0,9) - 奖励 -100
   - 吸收状态（任务7）：(0,3) - 奖励 +5

3. **风的影响**：特定列有向上的风
   - 列 3,4,5: 向上推 1 格
   - 列 6,7: 向上推 2 格
   - 列 8: 向上推 1 格
   - 风会修改垂直方向的移动结果

## 作业任务概览

HW2.pdf 定义了以下7个任务（**注意：文档使用1-based坐标，代码使用0-based坐标**）：

| 任务 | 类型 | 状态 | 说明 |
|------|------|------|------|
| 任务1 | 编程 | ✅ 已完成 | SARSA和Q-Learning，8向移动，三个起点 |
| 任务2 | 编程 | ✅ 已完成 | 4向移动对比 |
| 任务3 | LLM测试 | ⏸️ 需手动 | LLM自动算法选择 |
| 任务4 | LLM测试 | ⏸️ 需手动 | LLM分别实现两种算法 |
| 任务5 | LLM测试 | ⏸️ 需手动 | LLM纯推理最优轨迹 |
| 任务6 | LLM测试 | ⏸️ 需手动 | 4向移动下的LLM表现 |
| 任务7 | 编程 | ✅ 已完成 | 添加吸收状态，重复任务1-6 |

**编程任务（任务1,2,7）已在 `HW2_Solution.ipynb` 中完成。**
**LLM测试任务（任务3-6）需要手动与LLM交互完成。**

## 代码架构

### 主要实现（HW2_Solution.ipynb）

**核心类：`WindyGridworld`**
```python
class WindyGridworld:
    def __init__(self, king_moves=True, absorbing_state=None):
        # king_moves: True=8向移动, False=4向移动
        # absorbing_state: 吸收状态位置，如(0,3)
```

**关键方法：**
- `step(state, action)` - 执行动作，返回 (next_state, reward, done)
- `is_terminal(state)` - 判断是否为终止状态
- `random_action()` - 随机选择动作

**算法实现：**
- `sarsa(env, start_state, episodes, alpha, gamma, epsilon)` - SARSA 算法（on-policy）
- `q_learning(env, start_state, episodes, alpha, gamma, epsilon)` - Q-learning 算法（off-policy）

**辅助函数：**
- `get_optimal_policy(Q, env)` - 从Q表提取最优策略
- `get_optimal_path(policy, env, start_state)` - 生成最优路径
- `plot_learning_curve(steps_list, title, labels)` - 绘制学习曲线
- `visualize_gridworld(env, path, policy)` - 可视化网格世界和策略

**可视化特点：**
- 使用 matplotlib 生成高质量图形
- 颜色标记：目标（绿色）、死亡（黑色）、吸收（蓝色）
- 风力区域：黄色（弱风）、小麦色（强风）
- 策略箭头：蓝色箭头显示最优动作方向
- 路径标记：红色线条和圆点

## 运行和测试

### 环境准备
```bash
# 激活 conda 环境
conda activate rl-hw

# 如果环境不存在，创建新环境
conda create -n rl-hw python=3.10
conda activate rl-hw
conda install numpy matplotlib jupyter
```

### 运行主要实现
```bash
# 启动 Jupyter Notebook（推荐用于查看结果）
jupyter notebook HW2_Solution.ipynb

# 或使用 JupyterLab
jupyter lab HW2_Solution.ipynb
```

**执行方式：**
- 点击 `Cell → Run All` 运行所有单元格
- 或逐个运行单元格查看中间结果
- 预计生成约15个可视化图表

### 预期输出
- **学习曲线图**：显示算法收敛过程
- **策略可视化**：显示最优策略和路径
- **路径统计**：打印路径长度和累积奖励
- **对比分析**：SARSA vs Q-learning, 8向 vs 4向

### 快速验证
```python
# 在 Jupyter 中运行单个实验
env = WindyGridworld(king_moves=True)
Q, steps = q_learning(env, (6,0), episodes=10000)
policy = get_optimal_policy(Q, env)
path = get_optimal_path(policy, env, (6,0))
print(f"路径长度: {len(path)-1} 步")
visualize_gridworld(env, path, policy)
```

## 实现注意事项

### ⚠️ 坐标系统陷阱
**最重要的注意事项**：代码使用 0-based 坐标，文档使用 1-based 坐标！

- 代码中起点 (6,0) 对应文档中的 (7,1)
- 目标状态 (3,7) 对应文档中的 (4,8)
- 死亡状态 (0,9) 对应文档中的 (1,10)
- 吸收状态 (0,3) 对应文档中的 (1,4)

**转换公式**：
```
代码坐标 = 文档坐标 - 1
文档坐标 = 代码坐标 + 1
```

详细说明见：`坐标系统完全正确版.md`

### 算法关键点
- **SARSA**：on-policy，使用 (S, A, R, S', A') 五元组更新，学习实际执行的策略
- **Q-learning**：off-policy，使用 max Q(S', a') 更新，学习理论最优策略
- 需要正确处理终止状态（目标、死亡、吸收状态）
- epsilon-greedy 策略需要平衡探索率（建议 ε=0.1）

### 风力计算
- 风只影响垂直方向（行坐标）
- **先执行动作，再应用风力**
- 风向始终向上（减小行号）
- 边界检查在应用风力之后

### 默认参数（已在代码中优化）
```python
alpha = 0.1        # 学习率
gamma = 1.0        # 折扣因子（无折扣，因为是episodic任务）
epsilon = 0.1      # 探索率（10%探索）
episodes = 10000   # 训练回合数
```

## 修改代码时的注意事项

### 禁止的操作
- ❌ 不要修改坐标系统（会导致所有结果错误）
- ❌ 不要随意改变奖励值（会影响策略）
- ❌ 不要在已有代码基础上新建文件（遵循用户的八荣八耻原则）

### 允许的操作
- ✅ 调整超参数（alpha, epsilon, episodes）
- ✅ 修改可视化样式
- ✅ 添加新的分析功能（在现有cell中）
- ✅ 优化算法性能

### 常见修改需求
1. **调整训练轮数**：修改 `episodes` 参数
2. **改变探索率**：修改 `epsilon` 参数
3. **添加新起点**：在 `start_states` 列表中添加
4. **测试不同风力**：修改 `self.wind` 字典

---

## 任务详细说明

### 任务1：SARSA和Q-Learning（8向移动）

**目标**：使用两种算法从三个起点找到最优策略

**环境设置**：
- 动作空间：8向移动（King's moves）
- 起点（0-based）：(6,0), (3,0), (0,6)
- 文档坐标：(7,1), (4,1), (1,7)

**实现位置**：`HW2_Solution.ipynb` - Cell 11

**预期结果**：
- 每个起点生成最优路径
- SARSA和Q-Learning结果应相近
- 路径长度：7-15步（取决于起点）
- 生成6张图（3个起点 × 2种算法）

**关键代码**：
```python
env_king = WindyGridworld(king_moves=True)
Q_sarsa, steps_sarsa = sarsa(env_king, start, episodes=10000)
Q_qlearn, steps_qlearn = q_learning(env_king, start, episodes=10000)
```

---

### 任务2：4向移动对比

**目标**：对比仅允许Rook移动（上下左右）的情况

**环境设置**：
- 动作空间：4向移动（'n', 'e', 's', 'w'）
- 相同的三个起点

**实现位置**：`HW2_Solution.ipynb` - Cell 13

**预期差异**：
- 路径长度增加（无法对角线移动）
- 可能需要更多步骤避开死亡状态
- 收敛速度可能变慢

**关键代码**：
```python
env_rook = WindyGridworld(king_moves=False)
```

---

### 任务3：LLM自动算法选择

**目标**：测试LLM在未指定算法时会选择什么

**操作方式**：⏸️ 需手动完成

**提示词模板**：
```
请为Windy Gridworld问题编写强化学习代码，环境设定：
- 7×10网格，左上角为(0,0)
- 目标状态(3,7)，死亡状态(0,9)
- 8向移动（King's moves）
- 特定列有向上的风（列3-5风力1，列6-7风力2，列8风力1）
- 从(6,0)找到到(3,7)的最优策略
```

**观察要点**：
- LLM选择的算法（SARSA / Q-Learning / 其他）
- 选择的理由是否合理
- 代码质量和正确性
- 结果与任务1的对比

**参考实现**：`HW2_Solution.ipynb` - Cell 19

---

### 任务4：LLM算法对比验证

**目标**：让LLM分别实现SARSA和Q-Learning，验证一致性

**操作方式**：⏸️ 需手动完成

**测试步骤**：
1. 提示词A："请实现SARSA算法解决Windy Gridworld..."
2. 提示词B："请实现Q-Learning算法解决Windy Gridworld..."
3. 运行两份代码
4. 对比结果

**验证内容**：
- 路径长度是否一致
- 最优策略是否相同
- Q值是否接近
- 学习曲线是否相似

**参考实现**：`HW2_Solution.ipynb` - Cell 21

---

### 任务5：LLM纯推理最优轨迹

**目标**：测试LLM能否不编写代码，仅通过推理给出最优路径

**操作方式**：⏸️ 需手动完成

**提示词模板**：
```
在Windy Gridworld环境中（7×10网格，左上角为原点(0,0)），
有以下设定：
- 列3-5有1格向上的风，列6-7有2格向上的风，列8有1格向上的风
- 目标状态(3,7)，死亡状态(0,9)
- 允许8向移动（King's moves）
- 如果从(6,0)开始并遵循最优策略，请直接给出到达(3,7)的轨迹
```

**评估标准**：
- 是否正确考虑风的影响
- 是否避开死亡状态
- 路径是否合理
- 与实际最优路径的差距

**参考实现**：`HW2_Solution.ipynb` - Cell 23

---

### 任务6：4向移动下的LLM表现

**目标**：测试LLM在4向移动约束下的适应能力

**操作方式**：⏸️ 需手动完成

**测试内容**：
- 重复任务3（自动选择算法，4向）
- 重复任务4（对比验证，4向）
- 重复任务5（纯推理，4向）

**观察重点**：
- LLM是否理解约束变化
- 策略调整是否合理
- 路径长度预测是否准确

**参考实现**：`HW2_Solution.ipynb` - Cell 25

---

### 任务7：添加吸收状态

**目标**：在位置(0,3)添加奖励+5的吸收状态，重复任务1-6

**环境变化**：
- 新增吸收状态（0-based）：(0,3)
- 文档坐标：(1,4)
- 奖励：+5（终止状态）

**实现位置**：`HW2_Solution.ipynb` - Cell 15

**分析要点**：
- 算法是否选择吸收状态 vs 目标状态？
- 累积奖励对比：
  - 到吸收：约 -4 + 5 = +1
  - 到目标：约 -8 + 10 = +2（最优）
- 不同起点的策略差异
- SARSA vs Q-Learning的选择差异

**关键代码**：
```python
env_absorbing_king = WindyGridworld(king_moves=True, absorbing_state=(0,3))
env_absorbing_rook = WindyGridworld(king_moves=False, absorbing_state=(0,3))
```

**子任务**：
- 任务7.1：8向移动 + 吸收状态
- 任务7.2：4向移动 + 吸收状态
- 任务7.3-7.6：重复LLM测试任务（在有吸收状态的环境下）

---

## LLM测试任务通用指南

**适用于**：任务3、4、5、6及任务7中的LLM测试部分

**测试流程**：
1. 向LLM提供环境描述（不包含代码）
2. 观察LLM的算法选择和实现
3. 运行LLM生成的代码
4. 与`HW2_Solution.ipynb`的结果对比

**验证标准**：
- ✅ 算法收敛性：是否能在合理轮数内收敛
- ✅ 最优策略合理性：路径是否避开死亡状态，是否利用风力
- ✅ 与手写代码结果一致性：路径长度是否接近
- ✅ 特殊状态处理正确性：奖励和终止条件是否正确

**详细提示词模板**：见 `README.md` 或 `HW2_作业要求.md`
