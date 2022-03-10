from dataclasses import dataclass


@dataclass
class CandidateInfo:
    proposal_id: int
    user_pay_amount: float = 15.0
