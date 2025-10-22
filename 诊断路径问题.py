"""
诊断路径是否走向了错误的终点
"""

def diagnose_path_endpoints(path, env, task_name):
    """
    诊断路径终点是否正确
    """
    print(f"\n{'='*70}")
    print(f"🔍 诊断 {task_name}")
    print(f"{'='*70}")

    # 检查起点
    print(f"起点: {path[0]}")

    # 检查终点
    endpoint = path[-1]
    print(f"终点: {endpoint}")

    # 判断终点类型
    if endpoint == env.goal_state:
        print(f"✅ 正确！终点是目标状态(4,8) - 绿色方格")
        status = "正确"
    elif endpoint == env.death_state:
        print(f"❌ 错误！终点是死亡状态(1,10) - 黑色方格")
        print(f"   这不应该发生！路径不应该走向死亡状态！")
        status = "严重错误"
    elif endpoint == env.absorbing_state:
        print(f"⚠️  注意：终点是吸收状态(1,4) - 蓝色方格")
        print(f"   这取决于起点是否值得绕路获得+5奖励")
        status = "需要分析"
    else:
        print(f"❌ 错误！终点不是任何终止状态")
        print(f"   路径可能没有完成")
        status = "错误"

    # 检查路径是否经过死亡状态
    if env.death_state in path[:-1]:
        print(f"\n❌ 严重错误！路径中途经过了死亡状态(1,10)！")
        death_index = path.index(env.death_state)
        print(f"   在第{death_index}步走进了死亡状态")
        status = "严重错误"

    # 打印完整路径
    print(f"\n完整路径 ({len(path)-1}步):")
    if len(path) <= 20:
        print(f"  {' → '.join(map(str, path))}")
    else:
        print(f"  {' → '.join(map(str, path[:5]))} ... {' → '.join(map(str, path[-3:]))}")

    print(f"\n结论: {status}")
    print(f"{'='*70}\n")

    return status


# 使用方法（在notebook中运行）：
"""
# 检查任务2的路径
if 'path_sarsa_rook' in locals():
    for i, start in enumerate(start_states):
        # 重新生成这个起点的路径
        Q, _ = sarsa(env_rook, start, episodes=5000, alpha=0.1, epsilon=0.1)
        policy = get_optimal_policy(Q, env_rook)
        path = get_optimal_path(policy, env_rook, start)

        diagnose_path_endpoints(path, env_rook, f"任务2 - 起点{start}")

# 检查任务7的路径
if 'env_absorbing_king' in locals():
    for start in start_states:
        Q, _ = sarsa(env_absorbing_king, start, episodes=5000, alpha=0.1, epsilon=0.1)
        policy = get_optimal_policy(Q, env_absorbing_king)
        path = get_optimal_path(policy, env_absorbing_king, start)

        diagnose_path_endpoints(path, env_absorbing_king, f"任务7(8向) - 起点{start}")
"""
