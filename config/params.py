#!/usr/bin/env python
# encoding: utf-8
"""
   Desc: 配置文件信息
"""
from typing import Dict


class ParamsInfo:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            # 随机和规划均必填
            plan_model = int(item['plan_model'])   # 选券模式 0 随机，1 规划，3 自定义
            group_id = str(item["group_id"])   # 选券分组id
            split_num = int(item["split_num"])  # 分组数量
            # 规划
            plan_target = int(item.get("plan_target", 0))  # 目标：1 概率最大化，2 收益最大化
            constrain_type = int(item.get("constrain_type", 0))   # 约束类型
            predict_data_info = item.get("predict_mode_info", {})  # 购买概率/收益 路径及版本
            # 规划约束条件
            constrain_dict = {key: GlobalConstrain(value) for key, value in item["constrain_condition_info"].items()}
            self.plan_model = plan_model
            self.split_num = split_num
            self.group_id = group_id
            self.plan_target = plan_target
            self.predict_data_info = predict_data_info
            self.constrain_type = constrain_type
            self.constrain_dict = constrain_dict


class GlobalConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            drink_discount_constrain = {}
            if "drink_discount_constrain" in item:
                drink_discount_constrain = DiscountConstrain(item.get("drink_discount_constrain"))
            food_discount_constrain = {}
            if "food_discount_constrain" in item:
                food_discount_constrain = DiscountConstrain(item.get("food_discount_constrain"))
            proposal_constrain = {}
            if "proposal_constrain" in item:
                proposal_constrain = {i: ProposalConstrain(element) for i, element in
                                      enumerate(item["proposal_constrain"])}
            coupon_group_constrain = {}
            if "coupon_group_list_constrain" in item:
                coupon_group_constrain = {i: CouponGroupConstrain(element) for i, element in
                                          enumerate(item["coupon_group_list_constrain"])}
            single_profit_constrain = {}
            if "single_profit_constrain" in item:
                single_profit_constrain = SingleProfitConstrain(item.get("single_profit_constrain"))

            custom_drink_discount_constrain = {}
            if "custom_drink_discount_constrain" in item:
                custom_drink_discount_constrain = CustomDiscountConstrain(item.get("custom_drink_discount_constrain"))

            self.drink_discount_constrain = drink_discount_constrain
            self.food_discount_constrain = food_discount_constrain
            self.proposal_constrain = proposal_constrain
            self.coupon_group_constrain = coupon_group_constrain
            self.single_profit_constrain = single_profit_constrain
            self.custom_drink_discount_constrain = custom_drink_discount_constrain


class DiscountConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            avg_discount = float(item["avg_discount"])
            discount_flutter_info = item["discount_flutter_info"]
            flutter_default = discount_flutter_info["1"]
            default_high = float(flutter_default["high_flutter"])
            default_low = float(flutter_default["low_flutter"])
            discount_up = discount_flutter_info["2"]
            up_high = float(discount_up["high_flutter"])
            up_low = float(discount_up["low_flutter"])
            discount_down = discount_flutter_info["3"]
            down_high = float(discount_down["high_flutter"])
            down_low = float(discount_down["low_flutter"])
            self.avg_discount = avg_discount
            self.default_high = default_high
            self.default_low = default_low
            self.down_high = down_high
            self.down_low = down_low
            self.up_high = up_high
            self.up_low = up_low

    def dict(self):
        return {"avg_discount": self.avg_discount, "high_flutter": self.default_high, "low_flutter": self.default_low}


class ProposalConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            proposal_id = int(item["proposal_id"])
            max = float(item["max"])
            min = float(item["min"])
            priority = int(item["priority"])
            self.proposal = proposal_id
            self.max = max
            self.min = min
            self.priority = priority

    def dict(self):
        return {"proposal_id": self.proposal, "max": self.max, "min": self.min, "priority": self.priority}


class CouponGroupConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            group_key = int(item["coupon_group_key"])
            max = float(item["max"])
            min = float(item["min"])
            priority = int(item["priority"])
            type = int(item["coupon_apply_type"])
            self.group_key = group_key
            self.max = max
            self.min = min
            self.priority = priority
            self.type = type

    def dict(self):
        return {"group_key": self.group_key, "max": self.max, "min": self.min, "priority": self.priority, "type": self.type}


class SingleProfitConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            avg_single_profit = float(item["avg_amount"])
            profit_flutter_info = item["amount_flutter_info"]
            flutter_default = profit_flutter_info["1"]
            default_high = float(flutter_default["high_flutter"])
            default_low = float(flutter_default["low_flutter"])
            discount_up = profit_flutter_info["2"]
            up_high = float(discount_up["high_flutter"])
            up_low = float(discount_up["low_flutter"])
            discount_down = profit_flutter_info["3"]
            down_high = float(discount_down["high_flutter"])
            down_low = float(discount_down["low_flutter"])
            self.avg_single_profit = avg_single_profit
            self.default_high = default_high
            self.default_low = default_low
            self.down_high = down_high
            self.down_low = down_low
            self.up_high = up_high
            self.up_low = up_low

    def dict(self):
        return {"avg_single_profit": self.avg_single_profit, "high_flutter": self.default_high, "low_flutter": self.default_low}


class CustomDiscountConstrain:
    def __init__(self, item: Dict[str, any] = None):
        if item:
            target_ratio = float(item["discount_target_ratio"])
            low_flutter = float(item["low_flutter"])
            self.target_ratio = target_ratio
            self.low_flutter = low_flutter

    def dict(self):
        return {"target_ratio": self.target_ratio, "low_flutter": self.low_flutter}
