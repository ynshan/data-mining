from core.util.files import read_single_csv_file
from config.path import candidate_path


# 候选用户集解析, 数据格式：member_id, proposal_id, group_id, user_pay_amount
def member_proposal_candidate_dict(file_path):
    member_proposal_dict = {}
    for item in read_single_csv_file(file_path):
        # if item["member_id"] not in member_proposal_dict:
        #     member_proposal_dict[item["member_id"]] = {}
        profit = item.get("user_pay_amount", 13.2)
        if not profit:
            print("ok")
            profit = 15.0
        member_proposal_dict.setdefault(item["member_id"], []).append(profit)
    return member_proposal_dict






