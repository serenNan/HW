"""
紧急诊断：检查环境定义和路径终点
"""

print("="*80)
print("🚨 紧急诊断：检查环境配置")
print("="*80)

# 检查环境定义
print("\n【环境配置】")
print(f"目标状态 (应该是绿色): {env_king.goal_state}")
print(f"死亡状态 (应该是黑色): {env_king.death_state}")
if hasattr(env_absorbing_king, 'absorbing_state'):
    print(f"吸收状态 (应该是蓝色): {env_absorbing_king.absorbing_state}")

# 检查任务2的环境
print(f"\n任务2环境（4向移动）:")
print(f"目标状态: {env_rook.goal_state}")
print(f"死亡状态: {env_rook.death_state}")

# 检查实际路径终点
print("\n" + "="*80)
print("【路径终点检查】")
print("="*80)

# 假设最后运行的是(1,7)起点
if 'path_sarsa_rook' in dir():
    print(f"\n任务2 - 4向移动:")
    print(f"  path_sarsa_rook 终点: {path_sarsa_rook[-1]}")
    print(f"  是目标(4,8)? {path_sarsa_rook[-1] == (4,8)}")
    print(f"  是死亡(1,10)? {path_sarsa_rook[-1] == (1,10)} {'❌ 严重错误!' if path_sarsa_rook[-1] == (1,10) else ''}")
    print(f"  完整路径: {path_sarsa_rook}")

if 'path_sarsa_abs' in dir():
    print(f"\n任务7 - 吸收状态:")
    print(f"  path_sarsa_abs 终点: {path_sarsa_abs[-1]}")
    print(f"  是目标(4,8)? {path_sarsa_abs[-1] == (4,8)}")
    print(f"  是吸收(1,4)? {path_sarsa_abs[-1] == (1,4)}")
    print(f"  是死亡(1,10)? {path_sarsa_abs[-1] == (1,10)}")
    print(f"  完整路径: {path_sarsa_abs}")

# 测试环境的step函数
print("\n" + "="*80)
print("【环境行为测试】")
print("="*80)

test_cases = [
    ((4, 8), "到达目标状态"),
    ((1, 10), "到达死亡状态"),
    ((1, 4), "到达吸收状态（任务7）"),
]

for state, desc in test_cases:
    next_s, reward, done = env_king.step(state, 'n')
    print(f"\n从 {state} ({desc}):")
    print(f"  执行动作'n'后: next={next_s}, reward={reward}, done={done}")
    print(f"  is_terminal? {env_king.is_terminal(state)}")

# 检查奖励函数
print("\n" + "="*80)
print("【奖励函数测试】")
print("="*80)

test_transitions = [
    ((5, 8), 'n', "接近目标"),
    ((1, 9), 'e', "接近死亡状态"),
]

for state, action, desc in test_transitions:
    next_s, reward, done = env_king.step(state, action)
    print(f"\n{desc}: {state} --{action}--> {next_s}")
    print(f"  奖励: {reward}")
    print(f"  结束: {done}")
    print(f"  下一状态是目标? {next_s == env_king.goal_state}")
    print(f"  下一状态是死亡? {next_s == env_king.death_state}")

print("\n" + "="*80)
print("请把这个输出完整复制给我！")
print("="*80)
