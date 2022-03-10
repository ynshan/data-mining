from config.path import json_path
import json
from config.params import ParamsInfo


def main():
    # with open(json_path, 'r') as json_file:
    #     model_params = json.load(json_file)
    #     config_list = []
    #     for item in model_params:
    #         config_list.append(ParamsInfo(item))
    # for group_params in config_list:
    #     if group_params:
    #         # 配置
    #         plan_model = group_params.plan_model  # 选券模式
    #         group_id = group_params.group_id  # 候选集分组
    #         sub_group_num = group_params.split_num  # 规划选券每组的数量
    #
    #         # 规划目标
    #         plan_target = group_params.plan_target
    #         # 约束条件
    #         constrain_params = group_params.constrain_dict.get("1")
    #         discount = constrain_params.drink_discount_constrain
    #         constrain_params.constrain_type = group_params.constrain_type
    #         print(discount.dict())
    #         print(constrain_params.constrain_type)
    constrain_dict = {}
    for constrain_level, constrain_params in constrain_dict.items():
        print("pk")


if __name__ == "__main__":
    main()
