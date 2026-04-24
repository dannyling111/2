#!/usr/bin/env python3
"""Autonomous iteration runner for AVOS.

Runs self-improvement rounds without human input:
1) propose
2) score
3) critique
4) revise
5) keep best
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict
from statistics import mean
from typing import Dict, List


@dataclass
class Plan:
    niche: str
    offer: str
    acquisition: str
    validation: str
    automation_stack: str
    risks: List[str]


@dataclass
class RoundResult:
    round_id: int
    score: Dict[str, float]
    total: float
    critique: List[str]
    plan: Plan


def initial_plan(topic: str) -> Plan:
    return Plan(
        niche="泛职业人群",
        offer=f"{topic}诊断网页 + 报告",
        acquisition="内容平台泛流量",
        validation="上线后观察访问量",
        automation_stack="前端表单 + 规则引擎",
        risks=["用户太泛", "付费路径不清晰", "反馈闭环弱"],
    )


def evaluate(plan: Plan) -> Dict[str, float]:
    niche_focus = 9 if "泛" not in plan.niche else 5
    paid_offer = 8 if any(k in plan.offer for k in ["模板", "咨询", "订阅", "训练营"]) else 6
    growth = 8 if "SEO" in plan.acquisition or "矩阵" in plan.acquisition else 6
    mvp_speed = 9 if "前端" in plan.automation_stack or "规则" in plan.automation_stack else 7
    differentiation = 8 if "行业" in plan.niche or "垂直" in plan.niche else 6
    automation = 9 if "自动" in plan.validation or "回流" in plan.validation else 6
    fit = 9 if "GitHub" in plan.automation_stack or "Markdown" in plan.automation_stack else 7
    return {
        "pain": niche_focus,
        "willingness_to_pay": paid_offer,
        "growth": growth,
        "mvp_speed": mvp_speed,
        "differentiation": differentiation,
        "automation": automation,
        "resource_fit": fit,
    }


def critique(score: Dict[str, float], plan: Plan) -> List[str]:
    notes: List[str] = []
    if score["pain"] < 8:
        notes.append("把目标人群从‘泛职业’收敛到一个高痛点垂直职业。")
    if score["willingness_to_pay"] < 8:
        notes.append("在免费诊断后加入低价模板包与中价咨询，形成阶梯收费。")
    if score["growth"] < 8:
        notes.append("把获客从‘泛流量’改为SEO长尾+内容矩阵双引擎。")
    if score["automation"] < 8:
        notes.append("加入自动反馈回流：用户评分结果写入迭代队列。")
    if "反馈闭环弱" in plan.risks:
        notes.append("新增每轮复盘指标：输入完成率、复制率、分享率。")
    return notes


def revise(plan: Plan, notes: List[str], round_id: int) -> Plan:
    new_plan = Plan(**asdict(plan))
    for n in notes:
        if "收敛" in n:
            new_plan.niche = "自由职业内容创作者（想把AI能力产品化）"
        elif "阶梯收费" in n:
            new_plan.offer = "免费诊断 + 39元模板包 + 299元咨询"
        elif "双引擎" in n:
            new_plan.acquisition = "SEO长尾页面 + 短视频/图文内容矩阵"
        elif "自动反馈回流" in n:
            new_plan.validation = "自动收集用户评分并回流到下一轮策略"
        elif "复盘指标" in n:
            new_plan.validation += "；追踪输入完成率/复制率/分享率"

    if round_id >= 3 and "GitHub" not in new_plan.automation_stack:
        new_plan.automation_stack += " + GitHub Actions + Markdown沉淀"

    new_plan.risks = [r for r in new_plan.risks if r != "反馈闭环弱"] + ["样本量不足"]
    return new_plan


def run(topic: str, rounds: int) -> List[RoundResult]:
    history: List[RoundResult] = []
    plan = initial_plan(topic)

    for i in range(1, rounds + 1):
        score = evaluate(plan)
        total = round(mean(score.values()), 2)
        notes = critique(score, plan)
        history.append(RoundResult(i, score, total, notes, plan))
        plan = revise(plan, notes, i)

    return history


def convergence_advice(history: List[RoundResult], patience: int = 3) -> str:
    if len(history) < 2:
        return "样本轮次不足，建议至少运行 5 轮。"

    deltas = [round(history[i].total - history[i - 1].total, 2) for i in range(1, len(history))]
    stable = sum(1 for d in deltas[-patience:] if d <= 0.01) if len(deltas) >= patience else 0
    best = max(history, key=lambda x: x.total)

    if stable >= patience:
        return (
            f"得分已在最近 {patience} 轮基本收敛（最优 Round {best.round_id}, {best.total}）。"
            "建议下一步切换到真实用户数据优化，而不是盲目增加轮次。"
        )
    return "仍存在提升空间，建议再跑 3-5 轮并引入新的策略分支。"


def render_markdown(history: List[RoundResult]) -> str:
    best = max(history, key=lambda x: x.total)
    lines = [
        "# AVOS 自动迭代报告",
        "",
        f"- 轮次: {len(history)}",
        f"- 最优得分: {best.total}",
        f"- 最优轮次: Round {best.round_id}",
        f"- 迭代建议: {convergence_advice(history)}",
        "",
    ]
    for r in history:
        lines.extend(
            [
                f"## Round {r.round_id}",
                f"- 总分: {r.total}",
                f"- 方案: {r.plan.offer}",
                f"- 人群: {r.plan.niche}",
                f"- 获客: {r.plan.acquisition}",
                f"- 验证: {r.plan.validation}",
                "- 本轮批评:",
            ]
        )
        if r.critique:
            lines.extend([f"  - {c}" for c in r.critique])
        else:
            lines.append("  - 无明显短板，继续做数据化优化。")
        lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run AVOS autonomous iteration rounds.")
    parser.add_argument("--rounds", type=int, default=5, help="Number of self-iteration rounds.")
    parser.add_argument("--topic", type=str, default="AI时代职业赚钱路径诊断器", help="Topic for planning.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rounds = max(1, args.rounds)
    history = run(topic=args.topic, rounds=rounds)
    print(render_markdown(history))


if __name__ == "__main__":
    main()
